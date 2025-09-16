from django.shortcuts import render
from horse_race.models import Member, Race

def race(request):
    race = Race.objects.all().order_by('id')
    context = {
        'race': race,
    }
    return render(request, template_name='race.html', context=context)
