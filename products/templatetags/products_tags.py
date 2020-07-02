from django import template
register = template.Library()
from django.shortcuts import get_object_or_404
from ..models import Product, Vote

@register.filter(name='has_user')
def has_user(user, product_id):
    p_id = int(product_id)
    product = get_object_or_404(Product, pk=product_id)
    votes = product.votes_total.all()

    flag = 0
    for vote in votes:
        if vote.user == user:
            print("found the user")
            return user

    print("didnt find the user")
    return 0
