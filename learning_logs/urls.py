"""URL patterns"""

from django.urls import path

from . import views

app_name = 'learing_logs'

urlpatterns = [
    #HomePage
    path('', views.index, name='index')
]