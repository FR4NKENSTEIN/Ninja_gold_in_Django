from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ninjaGold),
    url(r'^process_gold$', views.processor),
    url(r'^destroy$', views.destroyer),
]