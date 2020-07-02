from django import template
register = template.Library()
from django.shortcuts import get_object_or_404
from ..models import Product, Vote

@register.filter(name='has_user')
def has_user(user, product_id):
    p_id = int(product_id)
    product = get_object_or_404(Product, pk=product_id)
    votes = product.votes_total.all()
    print("we have made it to the search")
    flag = 0
    for vote in votes:
        if vote.user == user:
            return flag
    return flag
