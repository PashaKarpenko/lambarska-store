from django.urls import path
from .views import ShoesListView, ShoeDetailView

urlpatterns = [
    path('', ShoesListView.as_view(), name='shoes_list'),
    path('shoe-detail/<int:pk>', ShoeDetailView.as_view(), name='shoe_detail'),
]
