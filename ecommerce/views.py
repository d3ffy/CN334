from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import requests

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

@csrf_exempt
def basic_request(request):
    if request.method == "GET":
        return JsonResponse({"status":"GET Pass"}, safe=False)
    if request.method == "POST":
        return JsonResponse({"status":"POST Pass"}, safe=False)
    
@csrf_exempt
def tokenize(request):
  if request.method == "POST":
    try:
        sentence = request.POST['text']
    except:
        return JsonResponse({"error":"Input not found"}, safe=False, status=500)
    url = "https://api.aiforthai.in.th/tlexplus"
    data = {'text':sentence}
    headers = {
        'Apikey': "3vA3wfXxuLwX9L7vvCluzFViqbiRtErj"
        }
    response = requests.post(url, data=data, headers=headers)
    reponse_json = response.json()
    return JsonResponse({"student":"student_id", "tokenize":reponse_json}, safe=False)
  return JsonResponse({"error":"Method not allowed!"}, safe=False, status=403)