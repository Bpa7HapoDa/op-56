from django.views.generic import ListView
from django.shortcuts import render
from .models import Clothes, Tag

class ClothesListView(ListView):
    model = Clothes
    template_name = 'clothes/clothes_list.html'
    context_object_name = 'clothes'
    paginate_by = 12

    def get_queryset(self):
        qs = super().get_queryset().prefetch_related('tags')
        tag = self.request.GET.get('tag')
        if tag:
            qs = qs.filter(tags__name=tag)
        return qs

def clothes_buttons_view(request):
    tags = Tag.objects.values_list('name', flat=True).distinct()
    selected = request.GET.get('tag', '').strip()
    clothes = Clothes.objects.all()
    if selected:
        clothes = clothes.filter(tags__name__iexact=selected)
    return render(request, 'clothes/clothes_buttons.html', {'tags': tags, 'clothes': clothes, 'selected': selected})
