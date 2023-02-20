from django.urls import path
from . import views

urlpatterns = [
    path('', views.character_counter, name='character_counter'),
    path('counter', views.counter, name='counter')
]
