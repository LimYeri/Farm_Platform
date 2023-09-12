from django import template

register = template.Library()

@register.filter
def calculate_total_price(products):
    total_price = sum([product.price for product in products])
    return total_price