import csv
import os
from datetime import datetime


# Keep transactions.csv in the same folder as this Python file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(BASE_DIR, "transactions.csv")


class BankAccount:

    def __init__(self, account_holder, account_number, balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        self.balance += amount

        self.save_transaction("Deposit", amount)

        print(f"₹{amount:.2f} deposited successfully.")
        print(f"Current balance: ₹{self.balance:.2f}")

    def withdraw(self, amount):

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        if amount > self.balance:
            print("Insufficient balance.")
            return

        self.balance -= amount

        self.save_transaction("Withdrawal", amount)

        print(f"₹{amount:.2f} withdrawn successfully.")
        print(f"Current balance: ₹{self.balance:.2f}")

    def save_transaction(self, transaction_type, amount):

        fieldnames = [
            "Date",
            "Account Holder",
            "Account",
            "Type",
            "Amount",
            "Balance"
        ]

        file_exists = os.path.exists(CSV_FILE)

        with open(CSV_FILE, "a", newline="", encoding="utf-8") as file:

            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames
            )

            
            if not file_exists or os.path.getsize(CSV_FILE) == 0:
                writer.writeheader()

            writer.writerow({
                "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Account Holder": self.account_holder,
                "Account": self.account_number,
                "Type": transaction_type,
                "Amount": amount,
                "Balance": self.balance
            })

    def check_balance(self):

        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Current balance: ₹{self.balance:.2f}")


def get_account_details(account_number):

    if not os.path.exists(CSV_FILE):
        return None, 0

    account_holder = None
    latest_balance = 0

    with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:

            if row["Account"] == account_number:

                account_holder = row["Account Holder"]
                latest_balance = float(row["Balance"])

    return account_holder, latest_balance


def show_transactions(account_number):

    if not os.path.exists(CSV_FILE):

        print("No transactions found.")
        return

    found = False

    print("\n===== TRANSACTION HISTORY =====")

    with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:

            if row["Account"] == account_number:

                found = True

                print(
                    f"{row['Date']} | "
                    f"{row['Account Holder']} | "
                    f"{row['Type']} | "
                    f"₹{float(row['Amount']):.2f} | "
                    f"Balance: ₹{float(row['Balance']):.2f}"
                )

    if not found:
        print("No transactions found for this account.")


def main():

    print("=" * 45)
    print("          OOP BANK ACCOUNT")
    print("=" * 45)

    account_number = input("Enter account number: ").strip()

    account_holder, balance = get_account_details(account_number)

    if account_holder is not None:

        print("\nExisting account found.")
        print(f"Account Holder: {account_holder}")
        print(f"Current balance: ₹{balance:.2f}")

    else:

        print("\nNew account.")

        account_holder = input(
            "Enter account holder name: "
        ).strip()

        while account_holder == "":
            print("Account holder name cannot be empty.")

            account_holder = input(
                "Enter account holder name: "
            ).strip()

        balance = 0

        print("Starting balance: ₹0.00")

    account = BankAccount(
        account_holder,
        account_number,
        balance
    )

    while True:

        print("\n===== MENU =====")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            try:

                amount = float(
                    input("Enter deposit amount: ")
                )

                account.deposit(amount)

            except ValueError:

                print("Please enter a valid amount.")

        elif choice == "2":

            try:

                amount = float(
                    input("Enter withdrawal amount: ")
                )

                account.withdraw(amount)

            except ValueError:

                print("Please enter a valid amount.")

        elif choice == "3":

            account.check_balance()

        elif choice == "4":

            show_transactions(
                account.account_number
            )

        elif choice == "5":

            print(
                "\nThank you for using the Bank Account System!"
            )

            break

        else:

            print(
                "Invalid choice. Please select 1 to 5."
            )


if __name__ == "__main__":
    main()