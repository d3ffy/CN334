from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ecommerce_index_views(request):
    return HttpResponse('Welcome to CN334 Tanasit Views!')
def home_page(request):
    return render(request, 'homePage.html')

def category_page(request):
    return render(request, 'categoryPage.html')

def checkout_page(request):
    return render(request, 'checkoutPage.html')

def product_page(request):
    return render(request, 'productPage.html')

def contact_page(request):
    return render(request, 'contactPage.html')
