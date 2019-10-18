# urls mysite

from django.contrib import admin
from django.urls import path, include

from . import views
from about import views as aboutViews
from account import views as accountViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', aboutViews.index),
    path('account/', accountViews.index),
    path('', views.index),
]
