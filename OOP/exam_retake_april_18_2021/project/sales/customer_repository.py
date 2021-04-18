from project.sales.customer import Customer


class CustomerRepository:
    def __init__(self):
        self.customers = []

    def add(self, customer: Customer):
        if customer in self.customers:
            raise ValueError(f"Customer {customer.name} already exists.")
        else:
            self.customers.append(customer)

    def remove(self, customer_name: str):
        if customer_name in [c.name for c in self.customers]:
            customer = [c for c in self.customers if c.name == customer_name][0]
            self.customers.remove(customer)
            return f"Removed customer: {customer_name}"
        else:
            raise ValueError(f"Customer {customer_name} does not exist.")

    def find(self, customer_name: str):
        if customer_name in [c.name for c in self.customers]:
            customer = [c for c in self.customers if c.name == customer_name][0]
            return customer
        else:
            return 'None'