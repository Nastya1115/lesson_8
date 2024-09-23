from django.shortcuts import render, redirect
from myapp.models import *

# Create your views here.
def main_page(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(
        request,
        template_name="main.html",
        context=context
    )

def products_page(request, product_id):
    product = Product.objects.get(id=product_id)
    reviews = Review.objects.filter(product=product_id)
    print(product)
    context = {
        "product": product,
        "reviews": reviews,
    }

    if request.method == "POST":
        author = request.POST.get("author-field")
        text = request.POST.get("text-field")
        rating = request.POST.get("rating-field")

        Review.objects.create(product = product, author = author, text = text, rating = rating)

    return render(
        request,
        template_name="add_review.html",
        context=context,
    )
