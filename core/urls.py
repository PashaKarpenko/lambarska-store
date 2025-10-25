"""
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from core.views import IndexView, AboutView, SizesView, ContactView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('sizes/', SizesView.as_view(), name='sizes'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('shoes/', include('shoes.urls')),
    path('cart/', include('cart.urls')),

    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
