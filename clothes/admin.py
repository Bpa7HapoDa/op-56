from django.contrib import admin
from .models import Tag, Clothes

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id','name')

@admin.register(Clothes)
class ClothesAdmin(admin.ModelAdmin):
    list_display = ('id','title','price')
    filter_horizontal = ('tags',)
