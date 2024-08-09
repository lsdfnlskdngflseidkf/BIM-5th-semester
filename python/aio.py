import json
import os

# File to store account information
ACCOUNT_FILE = 'accounts.json'
STATEMENT_FILE = 'statements.json'

# Load account data from file
def load_accounts():
    if os.path.exists(ACCOUNT_FILE):
        with open(ACCOUNT_FILE, 'r') as file:
            return json.load(file)
    return {}

# Save account data to file
def save_accounts(accounts):
    with open(ACCOUNT_FILE, 'w') as file:
        json.dump(accounts, file, indent=4)

# Validate user login
def validate_login(accounts, account_number, password):
    account = accounts.get(account_number)
    if account and account['password'] == password:
        return True
    return False

# Update account password
def change_password(accounts, account_number, old_password, new_password):
    account = accounts.get(account_number)
    if account and account['password'] == old_password:
        account['password'] = new_password
        save_accounts(accounts)
        return True
    return False

# Deposit funds
def deposit_funds(accounts, account_number, amount):
    account = accounts.get(account_number)
    if account:
        account['balance'] += amount
        save_accounts(accounts)
        return True, account['balance']
    return False, 0

# Withdraw funds
def withdraw_funds(accounts, account_number, amount):
    account = accounts.get(account_number)
    if account:
        min_balance = 100 if account['type'] == 'Saving' else 500
        if account['balance'] - amount >= min_balance:
            account['balance'] -= amount
            save_accounts(accounts)
            return True, account['balance']
    return False, 0

# Generate statement
def generate_statement(account_number, start_date, end_date):
    # Placeholder for statement generation logic
    return f"Statement for account {account_number} from {start_date} to {end_date}"

# Customer main menu logic
def customer_main_menu(accounts, account_number):
    while True:
        print("\nCustomer Main Menu:")
        print("1. Change Password")
        print("2. Deposit Funds")
        print("3. Withdraw Funds")
        print("4. Generate Statement")
        print("5. Logout")
        
        choice = input("Choose an option: ")

        if choice == '1':
            old_password = input("Enter old password: ")
            new_password = input("Enter new password: ")
            confirm_password = input("Confirm new password: ")
            if new_password == confirm_password:
                if change_password(accounts, account_number, old_password, new_password):
                    print("Password changed successfully.")
                else:
                    print("Failed to change password.")
            else:
                print("Passwords do not match.")

        elif choice == '2':
            amount = float(input("Enter deposit amount: "))
            if amount > 0:
                success, new_balance = deposit_funds(accounts, account_number, amount)
                if success:
                    print(f"Deposit successful. New balance: RM{new_balance:.2f}")
                else:
                    print("Failed to deposit funds.")
            else:
                print("Invalid deposit amount.")

        elif choice == '3':
            amount = float(input("Enter withdraw amount: "))
            if amount > 0:
                success, new_balance = withdraw_funds(accounts, account_number, amount)
                if success:
                    print(f"Withdrawal successful. New balance: RM{new_balance:.2f}")
                else:
                    print("Insufficient funds or failed to withdraw.")
            else:
                print("Invalid withdrawal amount.")

        elif choice == '4':
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            statement = generate_statement(account_number, start_date, end_date)
            print(statement)

        elif choice == '5':
            print("Logged out successfully.")
            break

        else:
            print("Invalid choice. Please try again.")

# Admin main menu logic
def admin_main_menu():
    # Placeholder for admin functionalities
    print("Admin menu is under construction.")

# Main program logic
def main():
    accounts = load_accounts()

    while True:
        print("\nCustomer Login:")
        account_number = input("Enter account number: ")
        password = input("Enter password: ")

        if validate_login(accounts, account_number, password):
            print("Login successful.")
            customer_main_menu(accounts, account_number)
        else:
            print("Invalid account number or password.")

if __name__ == "__main__":
    main()
