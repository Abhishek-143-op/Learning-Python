               #Learning about the string function 
"""
String function are function or built in methods used to manuplaite and operate operation of string 
"""
     #           Here's the list of most common used strings 
print(" 1. len(Variable)--- Used to know the length of string ")
print(len("Abhi")) #output : 4
A="Abhishek"
print(len(A))



print("  2. str(Variable)--- Used to convert any datatype to string ")
B=123
print(str(B))  #output → '123' String before it was int
print(
"""   \n                                 Case Conversion-- STRING FUNCTION
 |----------------------------------------------------------------------------------------------------------------|
 |lower()	     |    Converts all characters to lowercase	        |     "HeLLo".lower() → 'hello'               |  
 |upper()     	|    Converts all characters to uppercase    	   |     "hi".upper() → 'HI'                     | 
 |capitalize() |	 Capitalizes first letter	                  |     "python".capitalize() → 'Python'        |        
 |title()	     |    Capitalizes first letter of each word   	   |     "hello world".title() → 'Hello World'   |           
 |swapcase()   |    Swaps lowercase to uppercase and vice verse     |     "Hi Abhi".swapcase() → 'hI ABHI'        |         
 |----------------------------------------------------------------------------------------------------------------|

 \n
""")
print
(
"HeLLo".lower(),                           #    → 'hello'
"hi".upper(),                               #    → 'HI'
"python".capitalize(),                      #    → 'Python' 
"hello world".title(),                      #    → 'Hello World'
"Hi Abhi".swapcase(),                       #    → 'hI ABHI'
)

#sub means substring.

print(""" \n
                            Search & Check STRING FUNCTIONS
| Method            | Description                                    | Example                              |
| ----------------- | ---------------------------------------------- | ------------------------------------ |
| find(sub)         | Returns index of first occurrence of substring |   "hello".find("l") → 2              |
| index(sub)        | Same as  find() , but gives error if not found |   "hello".index("l") → 2             |
| startswith(sub)   | Checks if string starts with a substring       |   "python".startswith("py") → True   |
| endswith(sub)     | Checks if string ends with a substring         |   "python".endswith("on") → True     |
| in                | Checks if substring is present                 |   'th' in "python" → True            |

\n
""")

print("""\n
                       Whitespace & Character Removal
| Method     | Description                       | Example                   |
| ---------- | --------------------------------- | ------------------------- |
|  strip()   | Removes whitespace from both ends |  "  hi  ".strip() → 'hi'  |
|  lstrip()  | Removes whitespace from left      |  "  hi".lstrip() → 'hi'   |
|  rstrip()  | Removes whitespace from right     |  "hi  ".rstrip() → 'hi'   |

\n
""")

print ("""\n
                          Replace & Split
| Method              | Description             | Example                                           |
| ------------------- | ----------------------- | ------------------------------------------------- |
|  replace(old, new)  | Replaces substring      |  "goodbye".replace("good", "hello") → 'hellobye'  |
|  split(separator)   | Splits string into list |  "a,b,c".split(',') → ['a', 'b', 'c']             |
| saparator.join(list)| Joins list into string  |  ",".join(['a', 'b']) → 'a,b'                     |

 
\n
""")

print("""
\n
                              Check Type of Characters
| Method      | Description                            | Example                          |
|  ---------  | -------------------------------------- |  ------------------------- ----- |
|  isalnum()  | Checks if string is alphanumeric       |  "abc123".isalnum() → True       |
|  isalpha()  | Checks if all characters are letters   |  "abc".isalpha() → True          |
|  isdigit()  | Checks if all characters are digits    |  "123".isdigit() → True          |
|  islower()  | Checks if all characters are lowercase |  "abc".islower() → True          |
|  isupper()  | Checks if all characters are uppercase |  "ABC".isupper() → True          |
|  isspace()  | Checks if all characters are spaces    |  "   ".isspace() → True          |
|  istitle()  | Checks if string is in title case      |  "Hello World".istitle() → True` |

\n
""")

print("""
\n
                                 
                                 Special
| Method          | Description                      | Example                     |
| --------------- | -------------------------------- | --------------------------- |
|  count(sub)     | Counts occurrences of substring  |  "banana".count("a") → 3    |
|  zfill(width)   | Pads string with zeros from left |  "5".zfill(3) → '005'       |
|  center(width)  | Centers string with spaces       |  "hi".center(6) → '  hi  '  |
                                                      |                           | 
                                                       ___________________________
                                                                   |
                                                            Here 6 means total Character in the 
                                                            string 
\n
""")

      