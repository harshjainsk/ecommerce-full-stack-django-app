from django.shortcuts import render
from .models import Product
# Create your views here.


def get_products(request, slug):

    try:
        product = Product.objects.get(slug_field = slug)

        return render(request, "product/product.html", context = {"product":product})
    
    except Exception as e:

        print(e)