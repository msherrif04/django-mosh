from django.shortcuts import render
from django.db import transaction
from store.models import Order


# from django.http import HttpResponse


# Create your views here.
def say_hello(request):
    with transaction.atomic():
        order = Order()
        order.save()

    return render(
        request,
        "hello.html",
        context={"name": "Frontera"},
    )
