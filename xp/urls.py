from django.urls import path

from xp import views

urlpatterns = [
    path('xp', views.XpList.as_view(), name='xp'),
    path('xp/<slug:slug>', views.XpDetail.as_view(), name='xp_detail'),
]
