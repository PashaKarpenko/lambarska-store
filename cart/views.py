from django.views import View
from django.views.generic import ListView, TemplateView
from django.shortcuts import get_object_or_404, redirect

from cart.models import Cart, CartItem
from shoes.models import Shoe


class CartDetailView(TemplateView):
    template_name = 'cart/cart_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        session_key = self.request.session.session_key

        if not session_key:
            self.request.session.create()
            session_key = self.request.session.session_key

        cart, created = Cart.objects.get_or_create(session_key=session_key)
        items = cart.items.select_related('product')

        context['cart_items'] = items
        context['total_price'] = sum(item.product.price for item in items)
        return context



class CartAddView(View):
    def post(self, request, product_id):
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key

        cart, created = Cart.objects.get_or_create(session_key=session_key)
        product = get_object_or_404(Shoe, id=product_id)

        item, created = CartItem.objects.get_or_create(cart=cart, product=product)

        return redirect('cart_detail')


class CartRemoveView(View):
    def post(self, request, product_id):
        session_key = request.session.session_key
        if not session_key:
            return redirect('cart_detail')

        try:
            cart = Cart.objects.get(session_key=session_key)
            item = get_object_or_404(CartItem, cart=cart, product_id=product_id)
            item.delete()
        except Cart.DoesNotExist:
            pass

        return redirect('cart_detail')
