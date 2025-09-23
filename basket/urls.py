from django.views.generic import ListView
from django.urls import path, include
from . import views
from books.views import BookListView

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('books/', BookListView.as_view(), name='books'),
    path('basket_list/', views.read_basket_view, name='basket_list'),
    path('create_basket/', views.create_basket_view, name='create_basket'),
    path('update_basket/<int:id>/', views.update_basket_view, name='update_basket'),
    path('delete_basket/<int:id>/', views.delete_basket_view, name='delet_basket'),
    path('basket_detail/<int:id>/', views.basket_detail, name='basket_detail'),
    path('clothes/', include('clothes.urls')),
]


