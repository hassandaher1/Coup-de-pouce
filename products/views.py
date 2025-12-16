from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProductForm
from .models import Product


def public_home(request):
    """
    Interface 2 : page publique type Leboncoin.
    Liste des produits avec recherche simple.
    """
    query = request.GET.get("q", "").strip()
    category = request.GET.get("category", "").strip()

    products = Product.objects.filter(is_published=True)
    if category and category in dict(Product.CATEGORY_CHOICES):
        products = products.filter(category=category)

    if query:
        products = products.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )

    context = {
        "products": products,
        "query": query,
        "category": category,
        "categories": Product.CATEGORY_CHOICES,
    }
    return render(request, "public/home.html", context)


@login_required(login_url="admin_login")
def admin_dashboard(request):
    """
    Interface 1 : formulaire simple pour créer une nouvelle publication.
    Accessible uniquement après connexion.
    """
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("admin_dashboard")
    else:
        form = ProductForm()

    latest_products = Product.objects.order_by("-created_at")[:10]

    context = {
        "form": form,
        "latest_products": latest_products,
    }
    return render(request, "admin/dashboard.html", context)


@login_required(login_url="admin_login")
def admin_delete_product(request, product_id):
    """
    Supprime une publication (accessible uniquement après connexion).
    """
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        product.delete()
        return redirect("admin_dashboard")
    return redirect("admin_dashboard")
