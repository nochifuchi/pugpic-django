from django.test import SimpleTestCase
from django.urls import reverse, resolve
from app.views import index, users_detail, signup, photos_new, photos_detail, photos_delete
from django.contrib.auth import views as auth_views


class TestUrls(SimpleTestCase):

    def test_index_url_resolves(self):
        url = reverse('app:index')
        self.assertEquals(resolve(url).func, index)
        self.assertEquals(resolve(url).route, '')

    def test_users_detail_url_resolves(self):
        url = reverse('app:users_detail', args=[1])
        self.assertEquals(resolve(url).func, users_detail)
        self.assertEquals(resolve(url).route, 'users/<int:pk>/')

    def test_photos_new_url_resolved(self):
        url = reverse('app:photos_new')
        self.assertEquals(resolve(url).func, photos_new)
        self.assertEquals(resolve(url).route, 'photos/new/')

    def test_photos_detail_url_resolved(self):
        url = reverse('app:photos_detail', args=[1])
        self.assertEquals(resolve(url).func, photos_detail)
        self.assertEquals(resolve(url).route, 'photos/<int:pk>/')

    def test_photos_delete_url_resolved(self):
        url = reverse('app:photos_delete', args=[1])
        self.assertEquals(resolve(url).func, photos_delete)
        self.assertEquals(resolve(url).route, 'photos/<int:pk>/delete/')

    def test_signup_url_resolved(self):
        url = reverse('app:signup')
        self.assertEquals(resolve(url).func, signup)
        self.assertEquals(resolve(url).route, 'signup/')

    def test_login_url_resolved(self):
        url = reverse('app:login')
        self.assertEquals(resolve(url).url_name, 'login')
        self.assertEquals(resolve(url).route, 'login/')

    def test_logout_url_resolved(self):
        url = reverse('app:logout')
        self.assertEquals(resolve(url).url_name, 'logout')
        self.assertEquals(resolve(url).route, 'logout/')