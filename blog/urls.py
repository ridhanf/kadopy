# urls blog

from django.urls import path

from . import views 

urlpatterns = [
  path('recent/', views.recent),
  path('story/', views.story),
  path('news/', views.news),
  path('', views.index),
]
