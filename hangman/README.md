- while '-' in word or ' ' in word:
  keep searching the word, if the word is '-' and ' '
  this words.py contain '-' and ' ' which we don't want it

- return word.upper()
  once it found the word that are not either '-' or ' '
  return that word

set() is a built-in function used to create a set, which is an unordered collection of unique elements. It can take an iterable as an argument (like a list, tuple, or string), or no arguments to create an empty set. Sets are mutable, meaning elements can be added or removed, but the elements themselves must be immutable (e.g., numbers, strings, tuples). Sets are useful for removing duplicates and performing mathematical set operations like union, intersection, and difference.

# Creating an empty set

empty_set = set()
print(empty_set)

# Output: set()

# Creating a set from a list

my_list = [1, 2, 2, 3, 4, 4, 5]
my_set = set(my_list)
print(my_set)

# Output: {1, 2, 3, 4, 5}

# Creating a set from a tuple

my_tuple = (10, 20, 20, 30)
my_set_from_tuple = set(my_tuple)
print(my_set_from_tuple)

# Output: {10, 20, 30}

# Creating a set from a string

my_string = "hello"
my_set_from_string = set(my_string)
print(my_set_from_string)

# Output: {'h', 'e', 'l', 'o'}

https://docs.python.org/3/library/string.html
The string module in Python provides a collection of string-related constants and functions. To use it, it must first be imported using the statement import string. This makes the module's contents available for use in the current scope.
Commonly used components of the string module include:
Constants:
string.ascii_letters: Concatenation of lowercase and uppercase ASCII letters.
string.ascii_lowercase: Lowercase ASCII letters.
string.ascii_uppercase: Uppercase ASCII letters.
string.digits: Decimal digits (0-9).
string.hexdigits: Hexadecimal digits (0-9, a-f, A-F).
string.octdigits: Octal digits (0-7).
string.punctuation: ASCII punctuation characters.
string.printable: Combination of digits, letters, punctuation, and whitespace.
string.whitespace: Whitespace characters (space, tab, newline, etc.).

############ - add() - ##########

1. Set add() method
   The add() method is used to add a single element to a set. If the element is already in the set, it won't be added again because sets only store unique values.
   Python

my_set = {1, 2, 3}
my_set.add(4) # my_set is now {1, 2, 3, 4}
my_set.add(2) # my_set remains {1, 2, 3, 4}

2. List append(), insert() and extend() methods
   append(): Adds an element to the end of a list.
   insert(index, element): Inserts an element at a specific position in a list.
   extend(): Appends elements from another list (or any iterable) to the current list.

my_list = [1, 2, 3]
my_list.append(4) # my_list is now [1, 2, 3, 4]
my_list.insert(1, 5) # my_list is now [1, 5, 2, 3, 4]
my_list.extend([6, 7]) # my_list is now [1, 5, 2, 3, 4, 6, 7]

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1) # Output: [1, 2, 3, 4, 5, 6]
list1.extend((7, 8))
print(list1) # Output: [1, 2, 3, 4, 5, 6, 7, 8]
list1.extend("abc")
print(list1) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 'a', 'b', 'c']

The extend() method differs from append(), which adds the entire iterable as a single element to the end of the list.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.append(list2)
print(list1) # Output: [1, 2, 3, [4, 5, 6]]

3. Custom Class Addition (**add** method)
   If you define your own class, you can specify how the + operator should behave when used with instances of your class by defining the **add** method.

class Point:
def **init**(self, x, y):
self.x = x
self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2 # p3 is a new Point object with x=4 and y=6

############ - join() - ##########
The join() method in Python concatenates elements of an iterable (like a list, tuple, or set) into a single string, using a specified separator. It is called on a string, with the iterable as its argument. The syntax is separator.join(iterable). The method returns a new string and does not modify the original iterable. All elements in the iterable must be strings, or a TypeError will be raised. When using a dictionary as the iterable, join() only concatenates the keys.
w
ords = ["Hello", "world", "from", "Python"]
sentence = " ".join(words)
print(sentence) # Output: Hello world from Python

items = ["apple", "banana", "cherry"]
comma_separated = ", ".join(items)
print(comma_separated) # Output: apple, banana, cherry

my_tuple = ("John", "Peter", "Vicky")
x = "#".join(my_tuple)
print(x) # Output: John#Peter#Vicky
