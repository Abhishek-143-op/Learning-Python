year = int(input("Enter the year to check whether it is a leap year or not: "))

if year % 400 == 0:
    print(f"The Year {year} is a Leap Year.")
elif year % 100 == 0:
    print(f"The Year {year} is not a Leap Year.")
elif year % 4 == 0:
    print(f"The Year {year} is a Leap Year.")
else:
    print(f"The Year {year} is not a Leap Year.")
