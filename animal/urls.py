from django.contrib import admin
from django.urls import path

from aniPages import views

urlpatterns = [
    path('index/', views.PostList.as_view()),
    path('admin/', admin.site.urls),

]
