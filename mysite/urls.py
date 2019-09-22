# urls mysite

from django.contrib import admin
from django.urls import path, include

from . import views
from about import views as aboutViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('about/', aboutViews.index),
    path('', views.index),
]
