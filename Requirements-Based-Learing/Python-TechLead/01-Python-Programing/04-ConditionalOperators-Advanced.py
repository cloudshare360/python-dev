#1. else Clause in Loops (Not Just for if!)
#You can use else with for and while loops — it runs only if the loop didn’t break early .

for i in range(5):
    print(i)
    if i == 10:
        break
else:
    print("Loop completed without break")

'''
for i in range(5):
    print(i)
    if i == 3:
        break
else:
    print("Loop completed without break")
'''

# 🔹 1. any() – Like Multiple or
# any(iterable)
#  Example 1: Check if any number is even
numbers = [1, 3, 4,  5]
if any(num % 2 == 0 for num in numbers):
    print("At least one even number found.")
else:
    print("No even numbers.")

numbers = [1, 3,  5]
if any(num % 2 == 0 for num in numbers):
    print("At least one even number found.")
else:
    print("No even numbers.")

#  Example 2: Instead of multiple or
# Without any():

x = 10
if x == 5 or x == 10 or x == 15:
    print("x is a multiple of 5")

# x = 10
x = 10
if any(x == val for val in [5, 10, 15]):
    print("x is a multiple of 5")

# 🔹 2. all() – Like Multiple and
# all(iterable)
# 📌 Example 1: Are all numbers positive?

numbers = [1, 2, 3, 4]
if all(num > 0 for num in numbers):
    print("All numbers are positive.")
else:
    print("Some number is not positive.")

name = "Alice"
age = 25
email = "alice@example.com"

if name != "" and age >= 18 and "@" in email:
    print("User is valid.")

if all([
    name != "",
    age >= 18,
    "@" in email
]):
    print("User is valid.")
