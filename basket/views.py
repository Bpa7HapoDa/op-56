from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms

# CRUD - Create Read Update Delete

def create_basket_view(request):
    if request.method == 'POST':
        form = forms.BasketForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('basket_list')
    else:
        form = forms.BasketForm()
    return render(request, 'create_basket.html', context={'form': form})

def read_basket_view(request):
    if request.method == 'GET':
        basket = models.Basket.objects.all().order_by('-id')
        context = {'basket': basket}
        return render(request, 'basket_list.html', context=context)
def update_basket_view(request, id):
    basket_id = get_object_or_404(models.Basket, id=id)
    if request.method == 'POST':
        form = forms.BasketForm(request.POST, instance=basket_id)
        if form.is_valid():
            form.save()
            return redirect('basket_list')
    else:
        form = forms.BasketForm(instance=basket_id)
    context = {
        'form' : form,
        'basket_id': basket_id,
        
    }
    return render(request, 'update_basket.html', context=context)
def delete_basket_view(request, id):
    basket_id = get_object_or_404(models.Basket, id=id)
    basket_id.delete()
    return redirect('basket_list')
def basket_detail(request, id):
    if request.method == 'GET':
        basket_id = get_object_or_404(models.Basket, id=id)
        return render(request, 'basket_detail.html', context={'basket_id': basket_id})
