from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def character_counter(request):
    context = {
        'name': 'Oleg',
        'age': 32,
        'country': 'Moldova'
    }
    return render(request, 'character_counter.html', context)
