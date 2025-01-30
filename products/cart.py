class Cart:
    def __init__(self, request):
        """Initialize the cart using the session."""
        self.session = request.session
        cart = self.session.get("cart")

        if not cart:
            cart = self.session["cart"] = {}

        self.cart = cart

    def add(self, product, quantity=1):
        """Add product to the cart or update its quantity."""
        product_id = str(product.id)

        if product_id in self.cart:
            self.cart[product_id]["quantity"] += quantity
        else:
            self.cart[product_id] = {
                "name": product.name,
                "price": str(product.price),
                "quantity": quantity,
                "image": product.image.url if product.image else None,
            }

        self.session.modified = True

    def remove(self, product):
        """Remove product from the cart."""
        product_id = str(product.id)

        if product_id in self.cart:
            del self.cart[product_id]
            self.session.modified = True

    def clear(self):
        """Empty the cart."""
        self.session["cart"] = {}
        self.session.modified = True

    def __iter__(self):
        """Iterate through cart items."""
        for item in self.cart.values():
            yield item

    def total_price(self):
        """Calculate total price."""
        return sum(float(item["price"]) * item["quantity"] for item in self.cart.values())
