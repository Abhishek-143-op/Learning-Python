            #Here I am learning About Dictinory and Sets.

print(
"""

--------------------------------------Dictinory---------------------------------------------------

*****************************************Starts with the curly {} Brackets 
                                           variable = {"Keys" : "Value"} 



Dictinory is the set of the key0-Value pair .
as shown:

NOTE: 
-----------------------------DATATYPE of Keys and Values-----------------------------------------------------------
1. Key :In the key we can add any datatype but the condition is key should be immuteable (cannot be changed).
                                                                        |-Strings , Int, Bool , float,
                                                                        tuple (only if contain immutable content),
                                                                         frozeen set (special immuteable set) ,etc

                                                                         
2. Values : Can be of any dataype (not restrection.)
""")
dictinory1= {
            "Name":"Abhishek",
            "Age":"18",           #string DATATYPE-- both keys and value.
            "Roll no.":"341123" ,
            231:True ,             #Int datatype : Key , Boolean Datatype: Value.
            101: ["Math", "Science"],  #Int Datatype: key, String Datatype: Value.
            3.14: True,            #Int Datatype:key, Boolean Datatype : Value.
            (1, 2): 45.6   #Tuple Datatype: key, Int Datatype : Value.
            }

#  Using the dictionary functions 
print(
"""

-----------------------Most Common function for Dictinory--------------------------------------------------------------
| Method                          | Description                                                               | Example                         |
| ------------------------------- | ------------------------------------------------------------------------- | ------------------------------- |
| `dict.clear()`                  | Removes all items from the dictionary                                     | `d.clear()` → `{}`              |
| `dict.copy()`                   | Returns a shallow copy of the dictionary                                  | `d2 = d.copy()`                 |
| `dict.get(key, default)`        | Returns value for key, or `default` if key not found                      | `d.get("age", 0)`               |
| `dict.items()`                  | Returns a view of `(key, value)` pairs                                    | `list(d.items())`               |
| `dict.keys()`                   | Returns a view of all keys                                                | `list(d.keys())`                |
| `dict.values()`                 | Returns a view of all values                                              | `list(d.values())`              |
| `dict.pop(key, default)`        | Removes and returns the value for key; returns `default` if not found     | `d.pop("name", "NA")`           |
| `dict.popitem()`                | Removes and returns the last inserted `(key, value)` pair                 | `d.popitem()`                   |
| `dict.update(other_dict)`       | Updates the dictionary with key-value pairs from another dict or iterable | `d.update({"age": 25})`         |
| `dict.setdefault(key, default)` | Returns value for key; if missing, sets it to `default` and returns it    | `d.setdefault("city", "Delhi")` |
| `dict.fromkeys(seq, value)`     | Creates a new dict with keys from `seq` and all values set to `value`     | `dict.fromkeys(["a", "b"], 0)`  |


""",

dictinory1.get("Age"),
dictinory1.keys(),
dictinory1.pop("Age"),
dictinory1.update({"Marks":"[23,54,12]"}),
dictinory1.setdefault(("name","John")),
dictinory1.values(),
dictinory1.items(),

)

print ("""
------------------------------------Learning about the sets --------------------------------------------------------
        What is a set?
       
***************************STARTS WITH THE CURLY BRACKETS {}.
                                Variable : {___,____,____,...}-------------SETS
****************************SETS USING CONSTRUCTOR :
                                    set() constructor
                                                    The set() function creates a new set object.
                                                    You can pass any iterable (list, tuple, string, etc.) to it.
                                                    If no argument is passed, it creates an empty set.


       SET: 
            -A set is an unordered collection of unique elements.
            -It’s mutable (you can add/remove items), but the elements inside must be immutable.
            -Think of it like a mathematical set: no duplicates, order doesn’t matter.
                 EXAMPLE OF SETS :
""")
# Using curly braces
fruits = {"apple", "banana", "cherry"}

# Using set() constructor
numbers = set([1, 2, 3, 3])  # duplicates are removed
print(numbers)  # {1, 2, 3}

# Empty set (must use set(), not {} because this is an empty dictinory. )
empty_set = set()  

vegetables = {}  # This the empty dictinory not set ******************************IMP************************

print("""
----------------------------Properties of sets ---------------------------------------------
        1. Sets are unordered => Element’s order doesn’t matter
        2. Sets are unindexed => Cannot access elements by index
        3. There is no way to change items in sets  ( Inside the sets there is no way to change value or datatype).
            YOU can add and remove elements 
        4. Sets cannot contain duplicate values.
        5. Supports mathematical sets operations  Like Union , Intersection , and others .
        6. Fast membership test : SETS can check very fast that data inside set is there or not .
"""
)
#Support Mathematical operation : 
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)  # Union → {1, 2, 3, 4, 5}
print(a & b)  # Intersection → {3}



#FAST membership test means :
s = {1, 2, 3}
print(2 in s)  # True

print("""
         OPERATIONS ON SETS
                 Consider the following set:
                 s = {1,8,2,3}
                 • len(s): Returns 4, the length of the set
                 • s.remove(8): Updates the set s and removes 8 from s.
                 • s.pop(): Removes an arbitrary element from the set and return the element
                 removed.
                 • s.clear():empties the set s.
                 • s.union({8,11}): Returns a new set with all items from both sets. {1,8,2,3,11}.
                 • s.intersection({8,11}): Return a set which contains only item in both sets {8}.

""")
print(+"""
| Operation                            | Description                                             | Example                         |
| ------------------------------------ | ------------------------------------------------------- | ------------------------------- |
| `add(x)`                             | Adds an element to the set                              | `s.add(10)`                     |
| `discard(x)`                         | Removes element if it exists, **no error** if not found | `s.discard(5)`                  |
| `difference(other)` or `-`           | Returns elements in first set but not in second         | `s - {1, 2}`                    |
| `symmetric_difference(other)` or `^` | Elements in either set, but not in both                 | `s ^ {2, 3, 4}`                 |
| `isdisjoint(other)`                  | True if sets have no elements in common                 | `s.isdisjoint({10})`            |
| `issubset(other)`                    | True if all elements of set are in other                | `{1, 2} .issubset({1, 2, 3})`   |
| `issuperset(other)`                  | True if set contains all elements of other              | `{1, 2, 3} .issuperset({1, 2})` |
| `update(other)`                      | Adds all elements from another set (changes original)   | `s.update({5, 6})`              |
""")

# Initial set
s = {1, 8, 2, 3}

# add(x) → Adds an element to the set
s.add(10)
print("After add:", s)  # {1, 2, 3, 8, 10}

# discard(x) → Removes element if it exists, no error if not found
s.discard(5)
print("After discard:", s)  # {1, 2, 3, 8, 10}

# difference(other) or - → Elements in s but not in other
print("Difference:", s.difference({1, 2}))  # {3, 8, 10}
print("Difference (operator):", s - {1, 2})  # {3, 8, 10}

# symmetric_difference(other) or ^ → Elements in either set but not in both
print("Symmetric difference:", s.symmetric_difference({2, 3, 4}))  # {1, 4, 8, 10}
print("Symmetric difference (operator):", s ^ {2, 3, 4})  # {1, 4, 8, 10}

# isdisjoint(other) → True if sets have no elements in common
print("Is disjoint:", s.isdisjoint({100, 200}))  # True

# issubset(other) → True if all elements of s are in other
print("Is subset:", {1, 2}.issubset({1, 2, 3}))  # True

# issuperset(other) → True if s contains all elements of other
print("Is superset:", {1, 2, 3}.issuperset({1, 2}))  # True

# update(other) → Adds all elements from another set
s.update({5, 6})
print("After update:", s)  # {1, 2, 3, 5, 6, 8, 10}
