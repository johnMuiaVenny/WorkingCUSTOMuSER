from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver 
from .models import *





@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        PROFILE.objects.create(user=instance)

# post_save.connect(create_profile, sender=User)        


@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwargs):
    if created == False:
        instance.profile.save()

# post_save.connect(update_profile, sender=User)
