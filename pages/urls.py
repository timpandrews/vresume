from django.urls import path

from pages import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('resume', views.resume, name='resume'),
    path('xp', views.xp, name='xp'),
    path('contact', views.contact, name='contact'),
]