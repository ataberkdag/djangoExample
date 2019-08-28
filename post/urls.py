from django.urls import path
from .views import postHomePage, postDetailPage, postCreatePage

app_name = 'post'

# included
urlpatterns = [
    path('', postHomePage, name = 'home'),
    path('detail/<int:id>/', postDetailPage, name = 'detail'),
    path('create/', postCreatePage, name = 'create'),
]