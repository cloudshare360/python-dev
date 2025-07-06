# Python Lists
mylist = ["apple", "banana", "cherry"]
print(mylist)

'''
List Items
List items are ordered, changeable, and allow duplicate values.

List items are indexed, the first item has index [0], the second item has index [1] etc.

Ordered
When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

If you add new items to a list, the new items will be placed at the end of the list.

Changeable
The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

Allow Duplicates
Since lists are indexed, lists can have items with the same value:
'''
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# List Length
# To determine how many items a list has, use the len() function:

#Example
#Print the number of items in the list:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# List Items - Data Types
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

# Python Collections (Arrays)

'''
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
'''
# Access Items
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# Print the last item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# Range of Indexes

'''
You can specify a range of indexes by specifying where to start and where to end the range.

When specifying a range, the return value will be a new list with the specified items.

'''
# Return the third, fourth, and fifth item:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[5])
print(thislist[2:5])