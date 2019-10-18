# urls mysite

from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('account/', include('account.urls')),
    path('about/', include('about.urls')),
]
