from django.shortcuts import render


def index(request):
    return render(request, 'app/index.html')

def products(request):
    return render(request, 'app/products.html')

def single_product(request):
    return render(request, 'app/single-product.html')


def about(request):
    return render(request, 'app/about.html')

def contact(request):
    return render(request, 'app/contact.html')