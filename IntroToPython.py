# Strings

first_name = "pranav"
last_name = "rao"
print(f"{first_name} {last_name} is currently working")

# Functions and Lists


def calculate_expense(expenses):
    total = 0
    for expense in expenses:
        total = total + expense
    return total


pranav_expense = [45,67,32,47]
manish_expense = [34,78,96,42]

total = calculate_expense(pranav_expense)
print(f"pranav's expense {total}")
total = calculate_expense(manish_expense)
print(f"manish's expense {total}")

# For loop
n = int(input("Enter a no:"))
for i in range(0,n):
    for j in range(0,i+1):
        print("* ",end='')
    print()