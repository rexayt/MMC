from django.contrib import admin
from django.urls import path
from .views import artemoderna, main,olimpiada,revIndustrial,santosDumont

urlpatterns = [
    path('', main, name='main'),
    path('arteModerna', artemoderna, name='artemoderna'),
    path('olimpiada', olimpiada, name='olimpiadas'),
    path('revindustrial',revIndustrial,name='revolucaoindustrial'),
    path('santosdumont',santosDumont, name='santosdumont')
]
