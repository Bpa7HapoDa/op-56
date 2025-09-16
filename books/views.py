from django.shortcuts import render
from django.http import HttpResponse
def book_ru(request):
    if request.method == 'GET':
        return HttpResponse('Книга на русском')
def book_en(request):
    if request.method == 'GET':
        return HttpResponse('An english book')
def book_usa(request):
    if request.method == 'GET':
        return HttpResponse('An america book')