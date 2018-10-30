from django.db.models.signals import post_save #when a user is created what to do
from django.contrib.auth.models import User
from django.dispatch import receiver
from . models import Profile


@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):  #create_profile is the receiver when the user is created
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()
    # . apps.py under class
    #def ready(self):
    #  import users.signals
