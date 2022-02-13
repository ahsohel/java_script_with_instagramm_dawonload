from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('going_for_insta/', views.going_for_insta, name= 'going_for_insta'),
]
