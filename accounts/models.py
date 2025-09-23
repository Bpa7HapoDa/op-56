from django.db import models
from django.contrib.auth.models import User 

GENDER = (
    ('М', 'М'),
    ('Ж', 'Ж')
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    
    phone_number = models.CharField(max_length=14, default='+996')
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=100, choices=GENDER)

    class Meta:
        verbose_name = 'профиль'
        verbose_name_plural = 'профили'

    def __str__(self):
        return f'Профиль пользователя {self.user.username}'