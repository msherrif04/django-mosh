from django.shortcuts import render
from store.models import Product

# from django.http import HttpResponse


# Create your views here.
def say_hello(request):
    query_set = Product.objects.all()
    return render(request, "hello.html", context={"name": "Frontera"})
