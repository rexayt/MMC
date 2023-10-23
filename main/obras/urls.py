from django.contrib import admin
from django.urls import path
from .views import artemoderna, main,olimpiada,revIndustrial,santosDumont, ingressos, sign_up

urlpatterns = [
    path('', main, name='main'),
    path('arteModerna', artemoderna, name='artemoderna'),
    path('olimpiada', olimpiada, name='olimpiadas'),
    path('revindustrial',revIndustrial,name='revolucaoindustrial'),
    path('santosdumont',santosDumont, name='santosdumont'),
    path('ingressos',ingressos, name='ingressos'),
    path('sign_up', sign_up, name='sign_up'),

]
