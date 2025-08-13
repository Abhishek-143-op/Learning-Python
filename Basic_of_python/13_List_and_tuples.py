print("""
---------------------------------------------LIST-----------------------------------------------------------------
      
      a list is an ordered,
 changeable (mutable) collection of elements 
      that can store different data types in a single container.\n 
      
      ---->lists starts with the squared brackets [].



      example:""")
list1 = ["Abhishek" , 69 , True , 69.9999] #This is the list which contains the different datatype within it.
"""      |________|  |__|  |___|  |_____|
             |        |      |       |
             0        1      2       3   ---> +ve Indexes.
            -4       -3     -2      -1   ---> -ve Indexes. 

"""
print(list1[0], list1[2], list1[1],list1[3]) # Just like the string --> lists can be index as shown above

#Just like the string list slicing also can be done . All the string slicing concepts can be applied here .


print(list1[0:100:1])
print(list1[3:4])

#Just like the string function there are list functions 
print("""

      ---------------------------Common Funtions for the Lists---------------------------------------------
| Function         | Purpose                                              | Example                           | Output                                             |
| ---------------- | ---------------------------------------------------- | --------------------------------- | -------------------------------------------------  |
| append(x)        | Add an item to the end                               | fruits.append("orange")`          | ['apple', 'banana', 'orange']`                     |
| insert(i, x)     | Insert at a specific index                           | fruits.insert(1, "grape")`        | ['apple', 'grape', 'banana', 'orange']`            |
| extend(iterable) | Add multiple items from another list/iterable        | fruits.extend(["kiwi", "melon"])` | ['apple', 'banana', 'kiwi', 'melon']`              |
| remove(x)        | Remove first matching value                          | fruits.remove("banana")`          | ['apple', 'kiwi', 'melon']`                        |
| pop(i)           | Remove and return item at index *(last if no index)* | fruits.pop()`                     | Returns `'melon'`, list becomes `['apple', 'kiwi']`|
|--->***clear()    | Remove all items                                     | fruits.clear()`                   | []`                                                |
| index(x)         | Return index of first match                          | fruits.index("apple")`            | 0`                                                 |
| count(x)         | Count how many times an item appears                 | nums.count(2)`                    | 3` if list is `[1,2,2,2,3]`                        |
| sort()           | Sort in ascending order (changes list)               | nums.sort()`                      | [1,2,3,4]`                                         |
| reverse()        | Reverse order (changes list)                         | nums.reverse()`                   | [4,3,2,1]`                                         |
| copy()           | Make a shallow copy                                  | new_list = fruits.copy()`         |  Copy of list                                      |
\n \t\t\tExamples:

""")

# Python List Functions Examples with Output

# Starting list
fruits = ["apple", "banana", "cherry"]
print("Original list:", fruits)
# Output: Original list: ['apple', 'banana', 'cherry']

# append() - add at the end
fruits.append("orange")
print("After append:", fruits)
# Output: After append: ['apple', 'banana', 'cherry', 'orange']

# insert() - add at a specific position
fruits.insert(1, "grape")
print("After insert at index 1:", fruits)
# Output: After insert at index 1: ['apple', 'grape', 'banana', 'cherry', 'orange']

# extend() - add multiple elements
fruits.extend(["kiwi", "melon"])
print("After extend:", fruits)
# Output: After extend: ['apple', 'grape', 'banana', 'cherry', 'orange', 'kiwi', 'melon']

# remove() - remove by value/ name or list member name.
fruits.remove("banana")
print("After remove 'banana':", fruits)
# Output: After remove 'banana': ['apple', 'grape', 'cherry', 'orange', 'kiwi', 'melon']

# pop(i=index) - remove by index and return value
popped_item = fruits.pop(2)
print("Popped item:", popped_item)
# Output: Popped item: cherry
print("After pop at index 2:", fruits)
# Output: After pop at index 2: ['apple', 'grape', 'orange', 'kiwi', 'melon']

# index() - find position of an item
pos = fruits.index("apple")
print("Index of 'apple':", pos)
# Output: Index of 'apple': 0

# count() - count occurrences
nums = [1, 2, 2, 3, 2, 4]
print("Count of 2 in nums:", nums.count(2))
# Output: Count of 2 in nums: 3

# sort() - sort list in place
nums.sort()             #Sorting has an varients. 
print("Sorted nums:", nums)    #sort the list in the asscending order.
# Output: Sorted nums: [1, 2, 2, 2, 3, 4]

# reverse() - reverse list in place
nums.reverse()
print("Reversed nums:", nums)  
# Output: Reversed nums: [4, 3, 2, 2, 2, 1]

# copy() - create a shallow copy
nums_copy = nums.copy()
print("Copied list:", nums_copy)
# Output: Copied list: [4, 3, 2, 2, 2, 1]

# clear() - remove all items
fruits.clear()
print("After clear fruits:", fruits)
# Output: After clear fruits: []

"""
NOTE:
-------------------------------Strings and Lists ---------------------------------------------------
1.  When we create a string and operate the string funtions on it , it just create a new of string but it donot 
       change the original string .

                                but 

      In the list if we operate the operations on litst , it just operate in the original list .It donot create copies
       of the list --- so be careful what opeartions are operating on the list 

       Therefore use identifier = List_name(or variable).copy()
                While operating the Important operation.

2. Avoid using the name of list as 'list' as in python list named class is already there 
"""

print("""
      
-----------------------------------TUPLES-----------------------------------------------------------------
      

      Tuple is an immutable , 
      ordered , 
      collection of the elements 
      
************************---->Which starts with the parenthesis '()'
      ---->Can have the mixed datatypes as lists.
      """)

tuple1= () #Empty tuple 
tuple2= (1,) #Tuple with the 1 elements comma must be there 
tuple3= (1,3,5,7) #Tuple with more than 1 elements 

print("""
      
      ----------------Common Functions for Tuples-----------------------------------------
| **Method / Function** | **Description**                                                            | **Example**              | **Output**           |
| --------------------- | -------------------------------------------------------------------------- | ------------------------ | -------------------- |
| `count(x)`            | Returns the number of times `x` appears in the tuple.                      | `(1, 2, 2, 3).count(2)`  | `2`                  |
| `index(x)`            | Returns the index of the first occurrence of `x`.                          | `(10, 20, 30).index(20)` | `1`                  |
| `len(tuple)`          | Returns the number of elements in the tuple.                               | `len((5, 6, 7))`         | `3`                  |
| `max(tuple)`          | Returns the largest element in the tuple.                                  | `max((1, 5, 3))`         | `5`                  |
| `min(tuple)`          | Returns the smallest element in the tuple.                                 | `min((1, 5, 3))`         | `1`                  |
| `sum(tuple)`          | Returns the sum of all numeric elements in the tuple.                      | `sum((1, 2, 3))`         | `6`                  |
| `tuple(iterable)`     | Converts an iterable (list, string, etc.) into a tuple.                    | `tuple([1, 2])`          | `(1, 2)`             |
| `sorted(tuple)`       | Returns a sorted list of the tuple’s elements (does not modify the tuple). | `sorted((3, 1, 2))`      | `[1, 2, 3]`          |
| `in` operator         | Checks if an element exists in the tuple.                                  | `5 in (1, 5, 7)`         | `True`               |
| `+` (concatenation)   | Combines two tuples into one.                                              | `(1, 2) + (3, 4)`        | `(1, 2, 3, 4)`       |
| `*` (repetition)      | Repeats the tuple a given number of times.                                 | `(1, 2) * 3`             | `(1, 2, 1, 2, 1, 2)` |



""")


print("""
      
            --------------Difference between the Lists and Tuples --------------------------------
| Feature              | **List**                                          | **Tuple**                                                          |
| -------------------- | ------------------------------------------------- | ------------------------------------------------------------------ |
| **Syntax**           | `[]` square brackets                              | `()` parentheses                                                   |
| **Mutability**       | ✅ Mutable – can add, remove, or change elements  | ❌ Immutable – cannot change after creation                       |
| **Order**            | ✅ Ordered                                        | ✅ Ordered                                                        |
| **Duplicates**       | ✅ Allowed                                        | ✅ Allowed                                                        |
| **Mixed Data Types** | ✅ Yes                                            | ✅ Yes                                                            |
| **Methods**          | Many (e.g., `append`, `extend`, `remove`, `sort`) | Very few (`count`, `index`)                                        |
| **Speed**            | Slower (more features, more memory)               | Faster (fixed size, lightweight)                                   |
| **Memory Use**       | More memory                                       | Less memory                                                        |
| **Hashable**         | ❌ Cannot be used as a dictionary key             | ✅ Can be used as a dictionary key (if elements are also immutable)|
| **When to Use**      | When data may change                              | When data must remain constant                                     |




""")
# List
my_list = [1, 2, 3]
my_list[0] = 10     # Works
my_list.append(4)   # Works

# Tuple
my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # ❌ Error: 'tuple' object does not support item assignment
