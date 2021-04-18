from project.deliveries.drink import Drink
from project.deliveries.food import Food
from project.deliveries.product_repository import ProductRepository
from project.sales.customer import Customer
from project.sales.customer_repository import CustomerRepository


class Shop:
    def __init__(self):
        self.product_repository = ProductRepository()
        self.customer_repository = CustomerRepository()

    def deliver(self, product_type: str, name: str):
        if product_type == 'Food':
            return self.product_repository.add(Food(name))
        elif product_type == 'Drink':
            return self.product_repository.add(Drink(name))

    def sell(self, customer_name: str, **shopping_list):
        result = []
        customer = Customer(customer_name)
        if self.customer_repository.find(customer_name) == 'None':
            self.customer_repository.add(customer)
        for product_name, quantity in shopping_list.items():
            product = self.product_repository.find(product_name)
            if product is not 'None':
                if product.quantity - quantity <= 0:
                    customer.products[product_name] = product.quantity
                    self.product_repository.products.remove(product)
                    result.append(f"Left quantity of {product_name}: {0}")
                else:
                    customer.products[product_name] = product.quantity - quantity
                    result.append(self.product_repository.decrease(product, quantity))
        return '\n'.join(result)


shop = Shop()
print(shop.deliver('Food', 'eggs'))
print(shop.deliver('Food', 'bread'))
print(shop.deliver('Drink', 'water'))
print(shop.deliver('Drink', 'milk'))
customer = Customer('George')
print(shop.customer_repository.add(customer))
print(shop.sell('George', **{'bread': 10, 'eggs': 8, 'water': 20, 'milk': 5, 'cola': 18}))
print(customer.name)
print([c.products for c in shop.customer_repository.customers])