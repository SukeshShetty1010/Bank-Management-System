import random
from datetime import datetime

class Customer:
    def __init__(self, name, address, starting_balance):
        self.name = name
        self.address = address
        self.account_no = ''.join(str(random.randint(0, 9)) for _ in range(10))
        self.balance = starting_balance
        self.transactions = []
        self.loans = []

    def make_transaction(self, transaction_type, amount):
        if transaction_type == "credit":
            self.balance += amount
        elif transaction_type == "debit":
            if self.balance >= amount:
                self.balance -= amount
            else:
                print("Insufficient funds.")
                return
        transaction_id = ''.join(str(random.randint(0, 9)) for _ in range(10))
        transaction = (transaction_id, datetime.now(), self.account_no, transaction_type, amount)
        self.transactions.append(transaction)
        print("Transaction successful.")

    def take_loan(self, amount, interest):
        if len(self.loans) >= 3:
            print("You already have 3 loans. Cannot take more loans.")
            return

        print("Number of Loans:", len(self.loans))
        total_amount = amount + (amount * (interest / 100))
        installment = total_amount / 12
        print("Monthly Installment:", installment)
        confirm = input("Do you want to take the loan? (yes/no): ")
        if confirm.lower() == "yes":
            self.loans.append(total_amount)
            print("Loan taken successfully.")
        else:
            print("Loan not taken.")

    def get_passbook(self):
        if len(self.transactions) == 0:
            print("No transactions.")
        else:
            print("Transaction ID\tDate\t\t\tAccount No\tType\tAmount")
            for transaction in self.transactions[-10:]:
                transaction_id, date, account_no, transaction_type, amount = transaction
                print(f"{transaction_id}\t{date}\t{account_no}\t\t{transaction_type}\t{amount}")

    def get_account_details(self):
        print("Name:", self.name)
        print("Address:", self.address)
        print("Account No:", self.account_no)
        print("Balance:", self.balance)
        print("Number of Loans:", len(self.loans))