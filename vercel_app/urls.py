
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from django.views.static import serve
from . import views

urlpatterns = [
    # path(r'media/', serve,{'document_root': settings.MEDIA_ROOT}),
    # path(r'static/', serve,{'document_root': settings.STATIC_ROOT}),
    # path("__reload__/", include("django_browser_reload.urls")),
    path(r'', views.index, name="home"),
    path('admin/', admin.site.urls),
] 

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)