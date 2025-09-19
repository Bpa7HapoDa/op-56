
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from books.views import book_ru, book_en, book_usa, books_list, book_detail
from horse_race.views import race

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book_ru/', book_ru, name='book_ru'),
    path('book_en/', book_en, name='book_en'),
    path('book_usa/', book_usa, name='book_usa'),
    path('books_list/', books_list, name='books_list'),
    path('books_list/<int:id>/', book_detail, name='book_detail'),
    path('race/', race, name='race'),
    path('', include('basket.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
