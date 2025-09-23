from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from books.models import Books

def book_detail(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(Books, id=id)
        context = {
            'book_id': book_id,
        }    
        return render(request, template_name='book_detail.html', context=context)

def books_list(request):
    if request.method == 'GET':
        books_list = Books.objects.all().order_by('-id')
        context = {
            'books_list': books_list,

        }
        return render(request, template_name='books_list.html', context=context)

def book_ru(request):
    if request.method == 'GET':
        return HttpResponse('Книга на русском')
def book_en(request):
    if request.method == 'GET':
        return HttpResponse('An english book')
def book_usa(request):
    if request.method == 'GET':
        return HttpResponse('An america book')

from django.views.generic import ListView
from django.shortcuts import render
try:
    from .models import Books
except Exception:
    from django.apps import apps
    Book = apps.get_model('books','Book') if apps.is_installed('books') else None

class BookListView(ListView):
    model = Books
    template_name = 'books/book_list.html'
    context_object_name = 'books'
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(title__icontains=q) | qs.filter(author__icontains=q)
        return qs
