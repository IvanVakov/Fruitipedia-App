
from django.contrib import admin
from django.urls import path, include

from fruitipediaApp.fruits import views

urlpatterns = [
    path('', include('fruitipediaApp.fruits.urls')),
    path('admin/', admin.site.urls),

    path('categories/create/', views.create_category, name='create-category'),
]
