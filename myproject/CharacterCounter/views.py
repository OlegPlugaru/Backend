from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def character_counter(request):
    return render(request, 'character_counter.html')


def counter(request):
    text = request.POST['text']
    amount_of_character = len(text)
    return render(request, 'counter.html', {'amount': amount_of_character})
