from django.shortcuts import render
from store.models import Product, OrderItem, Order

# from django.http import HttpResponse


# Create your views here.
def say_hello(request):
    # select_related when the other end of the relations has one instance
    # prefetch_related when the other end has many relations
    # queryset = Product.objects.prefetch_related("promotions").select_related(
    #     "collection"
    # )
    queryset = (
        Order.objects.prefetch_related("orderitem_set__product")
        .order_by("-placed_at")[:5]
        .select_related("customer")
    )

    return render(
        request,
        "hello.html",
        context={"name": "Frontera", "orders": list(queryset)},
    )
