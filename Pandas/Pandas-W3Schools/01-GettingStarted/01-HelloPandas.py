import pandas

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)

myvar = pandas.DataFrame(myvar, index = ["x", "y", "z"])

print(myvar)