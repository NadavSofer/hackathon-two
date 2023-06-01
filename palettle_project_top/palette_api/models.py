from django.db import models

# Create your models here.
class Palette(models.Model):
    color_1 = models.CharField(max_length=50)
    color_2 = models.CharField(max_length=50)
    color_3 = models.CharField(max_length=50)
    color_4 = models.CharField(max_length=50)
    color_5 = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.color_1}, {self.color_2}, {self.color_3}, {self.color_4}, {self.color_5}'
    