import datetime

class BankingSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name):
        if name in self.accounts:
            print(f"Account for {name} already exists.")
        else:
            self.accounts[name] = {'balance': 0, 'transactions': []}
            print(f"Account created for {name}.")

    def perform_transaction(self, name, transaction_type, amount):
        if name not in self.accounts:
            print(f"No account found for {name}.")
            return
        
        if transaction_type == 'deposit':
            self.accounts[name]['balance'] += amount
            print(f"Deposited {amount} to {name}'s account.")
        elif transaction_type == 'withdraw':
            if self.accounts[name]['balance'] >= amount:
                self.accounts[name]['balance'] -= amount
                print(f"Withdrew {amount} from {name}'s account.")
            else:
                print(f"Insufficient balance for {name}.")
                return
        
        self.accounts[name]['transactions'].append({
            'type': transaction_type,
            'amount': amount,
            'date': datetime.datetime.now()
        })

    def check_balance(self, name):
        if name in self.accounts:
            print(f"{name}'s balance is {self.accounts[name]['balance']}.")
        else:
            print(f"No account found for {name}.")

    def view_transaction_history(self, name):
        if name in self.accounts:
            print(f"Transaction history for {name}:")
            for transaction in self.accounts[name]['transactions']:
                print(f"{transaction['date']} - {transaction['type']} - {transaction['amount']}")
        else:
            print(f"No account found for {name}.")

def main():
    banking_system = BankingSystem()

    while True:
        print("\n1. Create Account\n2. Deposit\n3. Withdraw\n4. Check Balance\n5. Transaction History\n6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter your name: ")
            banking_system.create_account(name)

        elif choice in ['2', '3']:
            name = input("Enter your name: ")
            transaction_type = 'deposit' if choice == '2' else 'withdraw'
            try:
                amount = float(input(f"Enter the amount to {transaction_type}: "))
                banking_system.perform_transaction(name, transaction_type, amount)
            except ValueError:
                print("Invalid amount entered. Please enter a numeric value.")

        elif choice == '4':
            name = input("Enter your name: ")
            banking_system.check_balance(name)

        elif choice == '5':
            name = input("Enter your name: ")
            banking_system.view_transaction_history(name)

        elif choice == '6':
            print("Thank you for using the Banking Management System!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
