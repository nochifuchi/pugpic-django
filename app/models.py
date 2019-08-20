from django.db import models
from django.contrib.auth.models import User

class Photo(models.Model):
    #title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='photos')
    comment = models.TextField(max_length=200, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment

