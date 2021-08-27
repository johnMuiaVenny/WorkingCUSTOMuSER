from django.db.models.signals import post_save
from .models import *
from django.dispatch import receiver


@receiver(post_save, sender=NEWUSER)
def create_users(sender, instance, created, **kwargs):
    if created:
        if instance.user_type == 'student':
            STUDENT.objects.create(user=instance, fName=instance.first_name, lName=instance.last_name)
        elif instance.user_type == 'teacher':
            TEACHER.objects.create(user=instance, fName=instance.first_name, lName=instance.last_name)
        elif instance.user_type == 'parent':
            PARENT.objects.create(user=instance, fName=instance.first_name, lName=instance.last_name)
        else:
            n=''


@receiver(post_save, sender=NEWUSER)
def update_users(sender, instance, created, **kwargs):
    if created == False:
        if instance.user_type == 'student':
            instance.student.save()
        elif instance.user_type == 'teacher':
            instance.teacher.save()
        elif instance.user_type == 'parent':
            instance.parent.save()
        else:
            n=''
