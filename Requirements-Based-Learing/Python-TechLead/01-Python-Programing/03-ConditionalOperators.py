#  1. Using Logical Operators in if Statements
age = 20

if age >= 18 and age <= 65:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# 2. Filtering Data Based on Multiple Conditions
users = [
    {"name": "Alice", "country": "USA", "is_active": True},
    {"name": "Raj", "country": "India", "is_active": True},
    {"name": "Bob", "country": "India", "is_active": False},
]

# Filter active users from India
for user in users:
    if user["country"] == "India" and user["is_active"]:
        print(f"{user['name']} is an active user from India.")

# What is a Ladder if Statement?
#Grading System
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

age = 17

if age >= 18:
    print("You are eligible to vote.")
elif age >= 16:
    print("You can register for pre-voter ID.")
else:
    print("You are too young to vote.")

#  1. Ternary Conditional Expression (One-line if-else)
# value_if_true if condition else value_if_false

age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)  # Output: Adult

is_raining = True
activity = "Indoor" if is_raining else "Outdoor"
print(activity)

# match-case Statement (Python 3.10+)
day = "Monday"

match day:
    case "Saturday" | "Sunday":
        print("Weekend")
    case _:
        print("Weekday")

day = "Sunday"
match day:
    case "Saturday" | "Sunday":
        print("Weekend")
    case _:
        print("Weekday")

data = []

if data:
    print("Data is present")
else:
    print("Data is empty")

print(4 or 5)         # ?
print("" and "Hello") # ?
print(None or "Data") # ?
print("Data" or None) # ?

count = 1
while count <= 5:
    print("Count:", count)
    count += 1

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

for i in range(5):
    print("Number:", i)

for i in range(0, 10, 2):
    print(i)

for i in range(0, 15, 3):
    print(i)


for i in range(10, 0, -1):
    print(i)

for i in range(10, 0, -2):
    print(i)

for i in range(20, 0, -5):
    print(i)

for i in range(0, 21, 5):
    print(i)