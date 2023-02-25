from django.urls import path
from .views import index, redirect_urls

urlpatterns = [
    path('', index, name='index'),
    path('<slug>/', redirect_urls, name='redirect_urls'),
]
