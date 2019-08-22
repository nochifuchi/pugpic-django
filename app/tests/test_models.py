from django.test import TestCase
from ..models import Photo
from django.contrib.auth.models import User

class TestModels(TestCase):

    def setUp(self):
        self.user1 = User.objects.create(
          username = 'user',
        )
        self.photo1 = Photo.objects.create(
          image = 'imaage',
          comment = 'comment',
          user = self.user1,
          created_at = 'comment',
        )

    def test_photo_create(self):
        saved_photo = Photo.objects.all()
        self.assertEqual(self.photo1.comment, 'comment')
        self.assertEqual(saved_photo.count(), 1)