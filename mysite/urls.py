# urls mysite

from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', include('about.urls')),
    path('account/', include('account.urls')),
    path('', views.index),
]
