# Banking System - README

This project is a simple Python implementation of a Banking System that allows users to create accounts, make transactions, take loans, view passbook, and get account details. It makes use of Object-Oriented Programming (OOP) concepts and provides a command-line interface for interacting with the system.

## Features
1. **Create Account**: Users can create a new bank account by providing their name, address, and starting balance. Each account is assigned a unique 10-digit account number.

2. **Make Transaction**: Account holders can make credit or debit transactions using their account number. The system records the date and time of each transaction and maintains a transaction history.

3. **Take Loan**: Customers can apply for loans by providing their account number, loan amount, and interest rate. The system calculates the monthly installment and allows customers to take a loan if they have less than three existing loans.

4. **Print Passbook**: Users can view their recent transactions by entering their account number. The system displays the last 10 transactions, including the transaction ID, date, account number, type (credit/debit), and amount.

5. **Get Account Details**: Customers can retrieve their account details, including name, address, account number, current balance, and the number of loans on the account.

## Data Structure
The project uses the following data structure:
- **Dictionary**: The `Bank` class stores all customer objects in a dictionary. The account number serves as the key, and the corresponding `Customer` object is the value.

## Functions
### Customer Class
1. `make_transaction(transaction_type, amount)`: Allows a customer to make credit or debit transactions.
2. `take_loan(amount, interest)`: Enables a customer to apply for a loan and calculates the monthly installment.
3. `get_passbook()`: Displays the last 10 transactions for a customer.
4. `get_account_details()`: Prints customer account details.

### Bank Class
1. `create_account(name, address, starting_balance)`: Creates a new bank account for a customer.
2. `get_customer(account_no)`: Retrieves the customer object based on the account number.

### Main
The `main.py` file provides a user-friendly command-line interface for interacting with the Banking System. Users can choose from various options to perform different banking operations.

## Usage
1. Clone the repository to your local machine.
2. Run `main.py` to start the Banking System.
3. Follow the on-screen prompts to perform account-related operations.

## Dependencies
The project uses Python 3.x, and no additional external libraries are required.

## License
This project is open-source and available under the MIT License. Feel free to modify and distribute it.

## Contributions
Contributions to the project are welcome. If you find any issues or want to add new features, please create a pull request.

## Acknowledgments
This project was created as part of a learning exercise to practice OOP concepts in Python.

