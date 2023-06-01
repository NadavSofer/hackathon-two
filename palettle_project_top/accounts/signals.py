from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    print(f'creating profile for: {instance}')
    if created:
        new_profile = UserProfile.objects.create(user = instance)
        print(f'creating profile: {new_profile}')
    pass