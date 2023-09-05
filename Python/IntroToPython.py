# Strings

first_name = "pranav"
last_name = "rao"
print(f"{first_name} {last_name} is currently working")

# Functions and Lists
"""
     Lists are heterogeneous
"""
pranav_expense = [45,67,32,47]
manish_expense = [34,78,96,42]


def calculate_expense(expenses):
    total = 0
    for expense in expenses:
        total = total + expense
    return total

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

# Tuples
'''
    It is similar to lists but the only diff b/w lists and tuples is that
    tuples are immutable whereas lists are mutable
'''
sample = (5,6)

# Dictionary
d = {
    'pranav': 8056093064,
    'manish': 9360740214,
    'sneha': 9876543654
}
print(d)
print(d['pranav'])
d['dhanya'] = 7876543566
print(d)
for name,number in d.items():
    print(name,number)
print(d.keys())
print(d.values())

l = ["pranav","himanshu","manish"]
f = "manish"
if f in l:
    print("true")