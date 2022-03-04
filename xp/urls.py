from django.urls import path

from pages import views

urlpatterns = [
    path('xp', views.xp, name='xp'),
]