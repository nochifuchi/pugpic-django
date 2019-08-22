from django.test import TestCase, Client
from django.shortcuts import reverse
from ..models import Photo
from django.contrib.auth.models import User

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index_url = reverse('app:index')
        self.users_detail_url = reverse('app:users_detail', args=[1])
        self.signup_url = reverse('app:signup')
        self.photos_new_url = reverse('app:photos_new')
        self.photos_detail_url = reverse('app:photos_detail', args=[1])
        self.photos_delete_url = reverse('app:photos_delete', args=[1])


    def test_index_GET(self):
        response = self.client.get(self.index_url)
        #print(response.context)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/index.html')

    def test_users_detail_GET(self):
        self.user = User.objects.create(
            username = 'user',
        )

        response = self.client.post(self.users_detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/users_detail.html')

    def test_signup_GET(self):
        response = self.client.get(self.signup_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/signup.html')

    def test_signup_POST(self):
        response = self.client.post(self.signup_url, {
            'username': 'test',
            'password': 'password',
        })

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/signup.html')

    def test_photos_detail_GET(self):
        self.user = User.objects.create(
            username = 'user',
        )
        self.photo = Photo.objects.create(
            image = 'imaage',
            comment = 'comment',
            user = self.user,
            created_at = 'comment',
        )

        response = self.client.get(self.photos_detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/photos_detail.html')

    """
    def test_photos_delete_POST(self):
        self.user = User.objects.create(
            username = 'user',
            id = 1,
        )
        self.photo = Photo.objects.create(
            image = 'imaage',
            comment = 'comment',
            user = self.user,
            created_at = 'comment',
        )
        response = self.client.post(self.photos_delete_url)
        print(response)
        self.assertEquals(response.status_code, 302)
        self.assertTemplateUsed(response, 'app/photos_delete.html')
    """