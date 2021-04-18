from project.deliveries.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        if product.name in [p.name for p in self.products]:
            raise ValueError(f"Product {product.name} already exists.")
        else:
            self.products.append(product)
            return f'Product {product.name} successfully added to inventory.'

    def decrease(self, product: Product, quantity: int):
        product.quantity -= quantity
        product_name = product.name
        product_quantity = product.quantity
        return f"Left quantity of {product_name}: {product_quantity}"

    def find(self, product_name: str):
        if product_name in [p.name for p in self.products]:
            product = [p for p in self.products if p.name == product_name][0]
            return product
        else:
            return 'None'
