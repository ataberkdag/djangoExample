from django.urls import path
from .views import postHomePage

app_name = 'post'
urlpatterns = [
    path('', postHomePage, name = 'home')
]