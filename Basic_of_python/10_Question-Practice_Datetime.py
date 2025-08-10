  #-----------------Practice question on the previous concepts -------------------------------------------------------------------

print("Q1.  Write a python program to display a user entered name followed by Good Afternoon using input () function.\n")

name=str(input("Enter your Name :"))
print("Good afternoon , ",name)

print(""" \n
      Q2.   Write a program to fill in a letter template given below with name and date. 
                          letter = '''
                            Dear <|Name|>,
                            You are selected!
                            <|Date|>
                                  '''

      """)
from datetime import datetime
print("Dear ",name,",\n \t \t you are selected! \n ","\t \t",datetime.now().date(),datetime.now().time())


#----------------------------------------------cONCEPT FROM DATE AND TIME ---------------------------------------------------
print(
""" 
To use date and time feature you need to Import datetime

-------------from datetime import datetime: 
                                 This will give access to---|
                                                            |
                                                 1.  datetime.now() --> gets current date and time

                                                 2.  .date()  --> extracts only the date

                                                 3.  .time() -->  extracts only the time                         

Then using the these to print date and time  as shown:
"""
)
from datetime import datetime

now = datetime.now()
print("Current Date and Time:", now)

print("\nWe can also extract individual unit form date and time:")
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)

print("Concept of formating the date :")
print("""
      
variable.strftime() = string format time- --> It lets you customize how the date/time is printed.
         |________|
             |
        Important with respect to datetime str. or format
      

""")
print(now.strftime("%d-%m-%Y %I:%M %p"))

print("""
\n where 
      
| Code | Meaning             | Example Output |
| ---- | ------------------- | -------------- |
| `%d` | Day (2 digits)      | `06`           |
| `%m` | Month (2 digits)    | `08`           |
| `%Y` | Year (4 digits)     | `2025`         |
| `%y` | Year (2 digits)     | `25`           |
| `%H` | Hour (24-hour)      | `22`           |
| `%I` | Hour (12-hour)      | `10`           |
| `%M` | Minute              | `45`           |
| `%S` | Seconds             | `20`           |
| `%p` | AM or PM            | `PM`           |
| `%B` | Full month name     | `August`       |
| `%A` | Full weekday name   | `Wednesday`    |
| `%a` | Abbreviated weekday | `Wed`          |


""")

print(now.strftime("Today is %A, %d %B %Y - Time: %I:%M:%S %p"))  # output: Today is Wednesday, 06 August 2025 - Time: 10:45:20 PM


print(datetime.now().time())   # Output: 22:45:20.501023
print("""
      Want to Add or Subtract Days?
            Use timedelta: as shown
      
""")
from datetime import datetime, timedelta

print("Today:", datetime.now().date())
print("Tomorrow:", datetime.now().date() + timedelta(days=1))
print("Yesterday:", datetime.now().date() - timedelta(days=1))

print("""
      \n
| Task                      | Code Example                              |
| ------------------------- | ----------------------------------------- |
| Current date & time       | `datetime.now()`                          |
| Just date                 | `datetime.now().date()` or `date.today()` |
| Just time                 | `datetime.now().time()`                   |
| Format output             | `strftime("%d-%m-%Y")`                    |
| Extract part (e.g., year) | `now.year`, `now.hour`, etc.              |
| Add/subtract time         | `timedelta(days=1)`                       |
\n 
FINAL EXAMPLE ALL IN 1 CODE :
      
""")
from datetime import datetime, timedelta

now = datetime.now()
print("Current Date:", now.date())
print("Current Time:", now.time())
print("Formatted:", now.strftime("%A, %d %B %Y - %I:%M %p"))
print("Tomorrow:", now.date() + timedelta(days=1))

print("PRACTICAL EXAMPLE FOR USING THE DATE AND TIME ")

# Saving Timestamps in Files or Logs

from datetime import datetime

now = datetime.now()
filename = now.strftime("backup_%Y%m%d_%H%M%S.txt")#******************************VIP*************
"""                     |________________________|
                                    |
                              Very Important for future.

"""
print("Saving file as:", filename)

#OUTPUT: Saving file as: backup_20250806_235102.txt

print("\nValid Function Calls with Correct Syntax")
print("""
| Code                    | ✅ Valid? | Output           | Explanation                 |
| ----------------------- | ---------  | ----------------- | --------------------------|
| `datetime.now()`        | ✅ Yes    | full date + time | Most commonly used          |
| `datetime.today()`      | ✅ Yes    | full date + time | Same as `now()`             |
| `datetime.now().date()` | ✅ Yes    | only date        | Extracts date part          |
| `datetime.now().time()` | ✅ Yes    | only time        | Extracts time part          |
| `date.today()`          | ✅ Yes    | only date        | Use when you only need date |
| `datetime.now().year`   | ✅ Yes    | just year        | Example: `2025`             |
| `datetime.now().month`  | ✅ Yes    | just month       | Example: `08`               |
| `datetime.now().day`    | ✅ Yes    | just day         | Example: `06`               |
| `datetime.now().hour`   | ✅ Yes    | just hour        | Example: `22`               |
| `datetime.now().minute` | ✅ Yes    | just minute      | Example: `45`               |
| `datetime.now().second` | ✅ Yes    | just seconds     | Example: `30`               |

      
"""
)