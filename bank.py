from customer import Customer

class Bank:
    def __init__(self):
        self.customers = {}

    def create_account(self, name, address, starting_balance):
        customer = Customer(name, address, starting_balance)
        self.customers[customer.account_no] = customer
        return customer.account_no

    def get_customer(self, account_no):
        return self.customers.get(account_no)