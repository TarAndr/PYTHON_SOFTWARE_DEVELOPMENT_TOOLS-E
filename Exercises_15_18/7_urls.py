# urls.py

from django.urls import path
from .views import add_human

urlpatterns = [
    path('add_human/', add_human, name='add_human'),
    # Добавьте другие URL-пути, если необходимо
]
