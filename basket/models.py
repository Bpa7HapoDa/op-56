from django.db import models
from django.core.validators import RegexValidator

phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="Номер телефона должен быть в формате: '+999999999'. Допускается до 15 цифр."
)
# card_regex = RegexValidator(
#     regex=r'^(?:4\d{12}(?:\d{3})?|5[1-5]\d{14}|6(?:011|5\d\d)\d{12}|3[47]\d{13}|3(?:0[0-5]|[68]\d)\d{11}|(?:2131|1800)\d{11})$',
#     message="Неверный формат номера карты.")

class Basket(models.Model):
    CHOICE_TYPE = (
        ('Выполнено', 'Выполнено'),
        ('Не выполнено', 'Не выполнено')
    )
    title = models.CharField(max_length=50, verbose_name='Название заказа')
    choice_type = models.CharField(max_length=50, verbose_name='Выберите вариант',
                              choices=CHOICE_TYPE)
    created_at = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=15,verbose_name='Номер телефона', 
                                    validators=[phone_regex])
    card_number = models.CharField(max_length=19,verbose_name='Номер карты')
    expiry_date = models.CharField(max_length=5)
    cvv_code = models.CharField(max_length=4)
    
    def __str___(self):
        return f'{self.title} - {self.CHOICE_TYPE}'
