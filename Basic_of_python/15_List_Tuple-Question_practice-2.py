                # Question practice on the list and tuple 

print("Q1.Check that a tuple cannot be changed in python.")
list1=[23,34,33,34]
tuple1=(23,34,33,34)

#Case 1 : Tuple and list side by side comparison for changing the elements---- Using append.
#tuple1.append(45) ------This will give an error as tuple cannot be changed. {commented as will give error}
list1.append(45)
print(list1,":After adding element.")

#Case 2 : Tuple and list side by side comparison for changing the elements---- Using insert.
#tuple1.insert(2,45) ------This will give an error as tuple cannot be changed. {commented as will give error}
list1.insert(2,45)
print(list1,":After inserting element at index 2")

#Case 3 : Tuple and list side by side comparison for changing the elements---- Using remove.
#tuple1.remove(34) -------This will give error as tuple cannot be changed .{Therefore commeted.}
list1.remove(34)
print(list1,":List after removing 34 -- using remove be name funtion.")

#Case 4 : Tuple and list side by side comparison for changing the elements---- Using pop.
#tuple1.pop(3) ---------This will give error as tuple cannot be changed 
list1.pop(3)
print(list1,":List after removing index 3 element usign pop function")


print("Q.2  Write a program to sum a list with 4 numbers.")
list2=[43,64,34,23]
print(list1+list2,":Here the content of List 1 and List 2 is combined .") #not sum of list 1 and list2 
print(sum(list1))
print(sum(list2))
print(sum(list1+list2))

print("""Q.3 Write a program to count the number of zeros in the following tuple:
a = (7, 0, 8, 0, 0, 9)""")

a= (7,0,8,0,0,9)

print(a.count(0))