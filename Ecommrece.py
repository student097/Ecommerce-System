class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} - ${self.price} (Stock: {self.stock})"


class ShoppingCart:
    def __init__(self):
        self.cart = {}

    def add_to_cart(self, product, quantity):
        if product.stock >= quantity:
            if product.product_id in self.cart:
                self.cart[product.product_id]['quantity'] += quantity
            else:
                self.cart[product.product_id] = {'product': product, 'quantity': quantity}
            product.stock -= quantity
            print(f"Added {quantity} of {product.name} to the cart.")
        else:
            print(f"Not enough stock for {product.name}.")

    def remove_from_cart(self, product_id):
        if product_id in self.cart:
            product = self.cart[product_id]['product']
            quantity = self.cart[product_id]['quantity']
            product.stock += quantity
            del self.cart[product_id]
            print(f"Removed {product.name} from the cart.")
        else:
            print("Product not in cart.")

    def view_cart(self):
        if not self.cart:
            print("Your cart is empty.")
        else:
            print("Shopping Cart:")
            for item in self.cart.values():
                product = item['product']
                quantity = item['quantity']
                print(f"{product.name} - ${product.price} x {quantity}")

    def checkout(self):
        total = sum(item['product'].price * item['quantity'] for item in self.cart.values())
        self.cart.clear()
        print(f"Checkout complete. Total: ${total}")


# Example usage
if __name__ == "__main__":
    # Sample products
    product1 = Product(1, "Laptop", 1200, 10)
    product2 = Product(2, "Phone", 800, 20)

    # Shopping cart
    cart = ShoppingCart()

    # Add products to cart
    cart.add_to_cart(product1, 1)
    cart.add_to_cart(product2, 2)

    # View cart
    cart.view_cart()

    # Remove a product
    cart.remove_from_cart(1)

    # View cart again
    cart.view_cart()

    # Checkout
    cart.checkout()