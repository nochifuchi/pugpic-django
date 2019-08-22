from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User

# ページネーション
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings

def paginate_query(request, queryset, count):
    paginator = Paginator(queryset, count)
    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return page_obj

# トップページ
from .models import Photo

def index(request):
    photos = Photo.objects.all().order_by('-created_at')
    page_obj = paginate_query(request, photos, settings.PAGE_PER_ITEM)
    return render(request, 'app/index.html', {'page_obj': page_obj})

# ユーザー詳細ページ
def users_detail(request, pk):
  user = get_object_or_404(User, pk=pk)
  photos = user.photo_set.all().order_by('-created_at')
  return render(request, 'app/users_detail.html', {'user': user, 'photos': photos})

# 新規登録ページ
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            input_username = form.cleaned_data['username']
            input_password = form.cleaned_data['password1']
            new_user = authenticate(username=input_username, password=input_password)
            if new_user is not None:
                login(request, new_user)
                return redirect('app:users_detail', pk=new_user.pk)
    else:
        form = UserCreationForm()
    return render(request, 'app/signup.html', {'form': form})

# 新規投稿ページ
from django.contrib.auth.decorators import login_required
from .forms import PhotoForm
from django.contrib import messages

@login_required
def photos_new(request):
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            messages.success(request, "投稿が完了しました！")
            return redirect('app:users_detail', pk=request.user.pk)
    else:
        form = PhotoForm()
        return render(request, 'app/photos_new.html', {'form': form})

# 写真詳細ページ
def photos_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, 'app/photos_detail.html', {'photo': photo})

# 写真削除
from django.views.decorators.http import require_POST

@require_POST
def photos_delete(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    photo.delete()
    return redirect('app:users_detail', request.user.id)