from django.urls import path


from cart.views import CartAddView, CartDetailView

urlpatterns = [
    path('detail/', CartDetailView.as_view(), name='cart_detail'),
    path('add/<int:shoe_id>/', CartAddView.as_view(), name='add_to_cart'),
]
