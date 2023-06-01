from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.URLField(null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.user}'
    

class palettes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    color_1 = models.CharField(max_length=50)
    color_2 = models.CharField(max_length=50)
    color_3 = models.CharField(max_length=50)
    color_4 = models.CharField(max_length=50)
    color_5 = models.CharField(max_length=50)