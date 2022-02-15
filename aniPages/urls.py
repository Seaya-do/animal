from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.PostList.as_view()),
    path('<int:pk>/', views.single_post_page),

]
