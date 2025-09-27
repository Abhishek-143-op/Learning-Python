'''
Write a program to generate multiplication tables from 2 to 20 and write it to the
different files. Place these files in a folder for a 13 – year old.
'''

import os
a=int(input("Enter the no. for which you want to create table : "))
def table(a):
    for i in range (1,11):
        print(f"{a} * {i}= {(a)*i}")

table(a)
        