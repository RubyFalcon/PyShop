
from django.shortcuts import render, get_object_or_404
from .models import Product
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

# Create your views here.
# /products call index needed
class ProductDetailView(DetailView):
    template_name = "products/product_detail.html"
    context = {}
    context_object_name = "product"
    queryset = Product.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Product, id = id_)


class ProductListView(ListView):
    template_name = "products/product_list.html"
    queryset = Product.objects.all()
    context_object_name = "products"

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def new(request):
    return 

def home(request):
    return render(request, "home.html")