from django.db import models
from django.contrib.auth.models import User  # extending the default User model by django
from PIL import Image  #to resize the profile image  pillow library external lib need to install


class Profile(models.Model): # extending the default User model by django
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    #settings.py MEDIA_ROOT = ''
    # MEDIA_URL = ''

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self): # already exists and we alter to resize the profile pictures
        super().save()

        img = Image.open(self.image.path)

        if img.height>300 or img.width>300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)