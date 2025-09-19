from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=10, verbose_name='Ваше имя')
    ticket_number = models.PositiveIntegerField(verbose_name='Введите номер билета', default='01')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'

class Race(models.Model):
    member = models.OneToOneField(Member, on_delete=models.CASCADE, related_name='member')
    created_at = models.DateTimeField(auto_now_add=True)
    race_name = models.IntegerField(verbose_name='Введите номер тура ')

    def __str__(self):
        return f'{self.member} - {self.race_name}'
    class Meta:
        verbose_name = 'тур'
        verbose_name_plural = 'туры'
