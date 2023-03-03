from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature
# Create your views here.


def index(request):
    feature1 = Feature()
    feature1.id = 1
    feature1.name = 'Fast'
    feature1.is_true = True
    feature1.details = 'Our service is very quick'

    feature2 = Feature()
    feature2.id = 2
    feature2.name = 'Reliable'
    feature2.is_true = True
    feature2.details = 'Our service is very reliable'

    feature3 = Feature()
    feature3.id = 3
    feature3.name = 'Easy to use'
    feature3.is_true = False
    feature3.details = 'Our service is easy to use'

    feature4 = Feature()
    feature4.id = 4
    feature4.name = 'Affordable'
    feature4.is_true = True
    feature4.details = 'Our service is very affordable'

    features = [feature1, feature2, feature3, feature4]

    return render(request, 'index.html', {'features': features})
