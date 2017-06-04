from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Product
from .forms import ProductAddForm


def create_view(request):
    form = ProductAddForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        title = data.get("title")
        description = data.get("description")
        price = data.get("price")
        new_obj = Product.objects.create(title=title, description=description, price=price)
        new_obj.save()
    template_name = "create_view.html"
    context = {
        "form": form
    }
    return render(request, template_name=template_name, context=context)


def detail_slug_view(request, slug=None):
    # One Item
    try:
        product = get_object_or_404(Product, slug=slug)
    except Product.MultipleObjectsReturned:
        product = Product.objects.filter(slug=slug).order_by("-title").first()
    # print(slug)
    # product = 1
    template_name = "detail_view.html"
    context = {
        "object": product
    }
    return render(request, template_name=template_name, context=context)


def detail_view(request, object_id):
    # One Item
    product = get_object_or_404(Product, id=object_id)
    template_name = "detail_view.html"
    context = {
        "object": product
    }
    return render(request, template_name=template_name, context=context)


def list_view(request):
    # list of items
    print(request)
    queryset = Product.objects.all()
    template_name = "list_view.html"
    context = {
        "queryset": queryset
    }
    return render(request, template_name=template_name, context=context)
