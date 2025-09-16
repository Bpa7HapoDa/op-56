from django.db import models

class Books(models.Model):
    CATEGORY_BOOKS = (
        ('Фантастика', "Фантастика"),
        ('Учебное', 'Учебное'),
        ('Детективы', 'Детективы')
    )
    title = models.CharField(max_length=50, verbose_name='укажите название книги')
    images = models.ImageField(upload_to='books/', verbose_name='загрузите фото')
    description = models.TextField(verbose_name='укажите описание книги')
    link_book = models.URLField(verbose_name='вставьте доп ссылку на контент', max_length=200, blank=True)
    category_books = models.CharField(max_length=50, choices=CATEGORY_BOOKS, default='Фантастика')
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(verbose_name='Введите почту автора', blank=True)
    file = models.FileField(upload_to="media/", blank=True)
    size = models.IntegerField(verbose_name='Введите количество страниц', blank=True)
    tags = models.TextField(verbose_name='укажите теги книги')
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'книгу'
        verbose_name_plural = 'Книги'