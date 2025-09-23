from django.urls import path
from .views import ClothesListView, clothes_buttons_view

app_name = 'clothes'
urlpatterns = [
    path('', ClothesListView.as_view(), name='list'),
    path('buttons/', clothes_buttons_view, name='buttons'),
]
