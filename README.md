# OOP Bank Account

A simple command-line banking system developed using Python and Object-Oriented Programming. The project stores transaction records in a CSV file and uses Pandas for basic dataset analysis.

## Features

- Create and manage bank accounts
- Deposit and withdraw money
- Check current balance
- View transaction history
- Store account and transaction details in a CSV file
- Retrieve existing account details
- Analyze transaction data using Pandas

## Technologies Used

- Python
- Pandas
- CSV
- Object-Oriented Programming (OOP)

## Project Files

```text
OOP-Bank-Account/
│
├── bank_account.py      # Banking system
├── analysis.py          # Pandas data analysis
├── transactions.csv     # Transaction dataset
├── .gitignore
└── README.md
```

## Banking System

The `bank_account.py` program provides a simple menu-driven banking system:

```text
1. Deposit
2. Withdraw
3. Check Balance
4. Transaction History
5. Exit
```

Successful deposits and withdrawals are automatically stored in `transactions.csv` along with the account holder, transaction type, amount, and updated balance.

## Pandas Dataset Analysis

The `analysis.py` file reads the transaction dataset using Pandas and performs:

- Dataset information
- Deposit and withdrawal summary
- Account-wise transaction analysis
- Latest account balances
- Basic statistical analysis

## How to Run

### 1. Install Pandas

```bash
pip install pandas
```

### 2. Run the Banking System

```bash
python bank_account.py
```

Use the menu to deposit, withdraw, check the balance, or view transaction history.

### 3. Run the Dataset Analysis

After performing transactions, run:

```bash
python analysis.py
```

This analyzes the updated `transactions.csv` file using Pandas.

## Objective

This project demonstrates the practical use of Object-Oriented Programming, file handling, exception handling, CSV data storage, and Pandas for basic data analysis.