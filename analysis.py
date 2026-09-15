import pandas as pd


df = pd.read_csv("transactions.csv")


print("=" * 50)
print("           TRANSACTION DATA")
print("=" * 50)

print(df.to_string(index=False))


print("\n" + "=" * 50)
print("           DATASET INFORMATION")
print("=" * 50)

print("Number of transactions:", len(df))
print("Number of columns:", len(df.columns))
print("Columns:", list(df.columns))


print("\n" + "=" * 50)
print("           TRANSACTION SUMMARY")
print("=" * 50)

summary = df.groupby("Type")["Amount"].agg(
    ["count", "sum", "mean"]
)

print(summary)


print("\n" + "=" * 50)
print("           ACCOUNT SUMMARY")
print("=" * 50)

account_summary = df.groupby(
    ["Account Holder", "Account"]
)["Amount"].sum()

print(account_summary)


print("\n" + "=" * 50)
print("           ACCOUNT BALANCES")
print("=" * 50)

latest_balance = df.groupby(
    ["Account Holder", "Account"]
)["Balance"].last()

print(latest_balance)


print("\n" + "=" * 50)
print("           BASIC STATISTICS")
print("=" * 50)

print(df["Amount"].describe())