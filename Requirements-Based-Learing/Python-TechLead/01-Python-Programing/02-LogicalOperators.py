#1. and Operator
print("# and → both must be True:", True and True)     # True
print("# and → if one is False:", True and False)       # False
print("# and → with expressions:", (5 > 3) and (10 < 15))  # True

#  2. or Operator
print("# or → one must be True:", True or False)        # True
print("# or → both False:", False or False)              # False
print("# or → with expressions:", (5 > 7) or (10 < 12))   # True

#3. not Operator
print("# not → reverses True:", not True)               # False
print("# not → reverses False:", not False)             # True
print("# not → with expression:", not(5 > 3))           # False