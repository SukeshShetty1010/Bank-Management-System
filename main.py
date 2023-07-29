from bank import Bank

# Test the classes
bank = Bank()

while True:
    print("\n1. Create Account")
    print("2. Make Transaction")
    print("3. Take Loan")
    print("4. Print Passbook")
    print("5. Get Account Details")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter customer name: ")
        address = input("Enter customer address: ")
        starting_balance = float(input("Enter starting balance: "))
        account_no = bank.create_account(name, address, starting_balance)
        print("Customer created with Account No:", account_no)
    elif choice == 2:
        account_no = input("Enter account number: ")
        customer = bank.get_customer(account_no)
        if customer:
            amount = float(input("Enter transaction amount: "))
            transaction_type = input("Enter transaction type (credit/debit): ").lower()
            customer.make_transaction(transaction_type, amount)
        else:
            print("Account not found.")
    elif choice == 3:
        account_no = input("Enter account number: ")
        customer = bank.get_customer(account_no)
        if customer:
            amount = float(input("Enter loan amount: "))
            interest = float(input("Enter loan interest rate: "))
            customer.take_loan(amount, interest)
        else:
            print("Account not found.")
    elif choice == 4:
        account_no = input("Enter account number: ")
        customer = bank.get_customer(account_no)
        if customer:
            print("\nPassbook:")
            customer.get_passbook()
        else:
            print("Account not found.")
    elif choice == 5:
        account_no = input("Enter account number: ")
        customer = bank.get_customer(account_no)
        if customer:
            customer.get_account_details()
        else:
            print("Account not found.")
    elif choice == 6:
        break
    else:
        print("Invalid choice. Please try again.")