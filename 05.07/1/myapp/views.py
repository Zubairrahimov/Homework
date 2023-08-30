from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Category, Product

def all_data(request):
    products = Product.objects.all()
    product_data = [{'id': product.id, 'name': product.name, 'description': product.description,
                     'price': str(product.price), 'category': product.category.name} for product in products]
    return JsonResponse({'products': product_data})

def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product_data = {
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'price': str(product.price),
        'category': product.category.name
    }
    return JsonResponse(product_data)
