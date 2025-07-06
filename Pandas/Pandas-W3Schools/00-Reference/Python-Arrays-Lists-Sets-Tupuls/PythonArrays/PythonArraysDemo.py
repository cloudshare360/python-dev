import array

my_array = array.array('i', [1, 2, 3])

print("print(type(my_array))", type(my_array))
my_list = [1, "hello", 3.14]

print("my_list = [1, 'hello', 3.14]", type(my_list))   # <class 'list'>


# Arrays are used to store multiple values in one single variable:
# Create an array containing car names:
cars = ["Ford", "Volvo", "BMW"]

'''
What is an Array?
An array is a special variable, which can hold more than one value at a time.
If you have a list of items (a list of car names, for example), storing the cars in single variables could look like this:

car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"

An array can hold many values under a single name, and you can access the values by referring to an index number.

Access the Elements of an Array
You refer to an array element by referring to the index number.
Get the value of the first array item:
'''

x = cars[0]
print("\ncar array:", cars, "\nfirst element of car array:", x);

# Modify the value of the first array item:
cars[0] = "Toyota"

print("\ncar array after modification:", cars);

# lenght of array

lenOfArray = len(cars);

print("length of array: len(cars):", lenOfArray)

# Looping Array Elements
for x in cars:
  print(x)

# Adding Array Elements
cars.append("Honda")

print("adding element to array using append:cars.append('Honda')", cars);

# Removing Array Elements
# Delete the second element of the cars array:
print("printing array before pop", cars);
print("removing element from array using pop:cars.pop(1)", cars.pop(1));

print("printing array after pop", cars);
#Delete the element that has the value "Volvo":
cars.remove("Honda")

print("printing array after pcars.remove('Honda')", cars);

my_var = [1, 2, 3]
print(type(my_var))  # Output: <class 'list'>