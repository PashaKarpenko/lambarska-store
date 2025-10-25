from django.db import models
from shoes.models import Shoe


class Cart(models.Model):
    session_key = models.CharField(max_length=40, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Shoe, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('cart', 'product')