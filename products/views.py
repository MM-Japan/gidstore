from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .cart import Cart
from .forms import ContactForm

## PRODUCT
def product_list(request):
    products = Product.objects.filter(available=True)
    return render(request, 'products/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})

## CONTACT
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')  # Redirect to a success page
    else:
        form = ContactForm()

    return render(request, 'products/contact.html', {'form': form})

def contact_success(request):
    return render(request, 'products/contact_success.html')

## CART
def add_to_cart(request, pk):
    """Add a product to the cart."""
    product = get_object_or_404(Product, pk=pk)
    cart = Cart(request)
    cart.add(product)
    return redirect("cart_detail")

def cart_detail(request):
    """Show cart contents."""
    cart = Cart(request)
    return render(request, "products/cart_detail.html", {"cart": cart})

def remove_from_cart(request, pk):
    """Remove an item from the cart."""
    product = get_object_or_404(Product, pk=pk)
    cart = Cart(request)
    cart.remove(product)
    return redirect("cart_detail")

def clear_cart(request):
    """Empty the cart."""
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")
