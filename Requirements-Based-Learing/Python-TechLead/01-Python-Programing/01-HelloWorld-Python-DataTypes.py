print("Hello World!")
x = 10

print("x", x);
# variable_name = value
name = "Alice"     # string
age = 25           # integer
height = 5.8       # float
is_student = True  # boolean

# Identify the type

print(type(name))       # <class 'str'>
print(type(age))        # <class 'int'>
print(type(height))     # <class 'float'>
print(type(is_student)) # <class 'bool'>

# use type hinting
name: str = "Alice"
age: int = 25
height: float = 5.8
is_student: bool = True
print("******** with type hinting")
print(type(name))       # <class 'str'>
print(type(age))        # <class 'int'>
print(type(height))     # <class 'float'>
print(type(is_student)) # <class 'bool'>

# Data Type Conversion

# Conversions to int
print("# float -> int → truncates decimal:", int(3.9))         # 3
print("# str (numeric) -> int → converts:", int("123"))        # 123
print("# bool -> int → True becomes 1:", int(True))            # 1
print("# bool -> int → False becomes 0:", int(False))          # 0

# Conversions to float
print("# int -> float → adds .0:", float(5))                     # 5.0
print("# str (int) -> float → converts:", float("7"))            # 7.0
print("# str (float) -> float → converts:", float("7.5"))        # 7.5
print("# bool -> float → True becomes 1.0:", float(True))        # 1.0
print("# bool -> float → False becomes 0.0:", float(False))      # 0.0

#Conversions to str
print("# int -> str → converts:", str(123))                      # '123'
print("# float -> str → converts:", str(3.14))                   # '3.14'
print("# bool -> str → converts:", str(True))                    # 'True'
print("# list -> str → converts as string:", str([1, 2]))        # '[1, 2]'
print("# dict -> str → converts as string:", str({"a": 1}))      # "{'a': 1}"
print("# None -> str → converts:", str(None))                    # 'None'
#. Conversions to bool
print("# int -> bool → 0 is False, others True:", bool(1))       # True
print("# int -> bool → 0 is False:", bool(0))                    # False
print("# float -> bool → non-zero is True:", bool(3.14))         # True
print("# str (non-empty) -> bool → True:", bool("hello"))       # True
print("# str (empty) -> bool → False:", bool(""))                # False
print("# list (empty) -> bool → False:", bool([]))               # False
print("# list (non-empty) -> bool → True:", bool([1, 2]))        # True