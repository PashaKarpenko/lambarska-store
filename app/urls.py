from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('products/single-product/', views.single_product, name='single-product'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

]
