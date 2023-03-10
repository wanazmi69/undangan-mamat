
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    # path("__reload__/", include("django_browser_reload.urls")),
    path(r'', views.index, name="home"),
    path('admin/', admin.site.urls),
]
