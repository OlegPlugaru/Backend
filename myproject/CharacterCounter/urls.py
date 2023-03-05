from django.urls import path
from . import views

urlpatterns = [
    path('', views.character_counter, name='character_counter'),
    path('char_counter', views.char_counter, name='char_counter')
]
