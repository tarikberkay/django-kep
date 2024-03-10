from django.db import models
from django.contrib.auth.models import User
from PIL import Image

from django.urls import reverse



# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)



class Contact(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, null=True)
    msg_subject = models.CharField(max_length=200, null=True)
    message = models.TextField(null=True)
