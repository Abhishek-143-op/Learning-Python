Character = input("Enter the Character/Alphabet (a-z) to check wether is it vowel or Consonant : ").lower()

if Character in 'aeiou':
    print(f"The {Character} is the Vowel . ")
elif Character.isalpha():
    print(f"The {Character} is the Consonant . ")
else: 
    print(f"Please enter the Valid input Character / Alphabet (a-z)")
    
    