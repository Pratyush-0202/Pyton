num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("odd")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)

ch = input("Enter a character: ").lower()
if ch in 'aeiou':
    print("Vowel")
elif ch.isalpha():
    print("Consonant")
else:
    print("Not a letter")

x = eval(input("Enter any value: "))
if isinstance(x, int):
    print("Integer")
elif isinstance(x, float):
    print("Float")
elif isinstance(x, str):
    print("String")
else:
    print("Other type")

s = input("Enter a string: ")
print("Palindrome" if s == s[::-1] else "Not Palindrome")

lst = eval(input("Enter a list: "))
print("Long list" if len(lst) > 5 else "Short list")

student = {"name": "John", "age": 20}
print("Age found" if "age" in student else "Age not found")

set1 = eval(input("Enter first set: "))
set2 = eval(input("Enter second set: "))
if set1.issubset(set2):
    print("First is subset of second")
elif set2.issubset(set1):
    print("Second is subset of first")
else:
    print("No subset relation")

tpl = eval(input("Enter a tuple: "))
print("Match" if tpl[0] == tpl[-1] else "No Match")

num = int(input("Enter a number: "))
if num < 0:
    print("Negative")
elif num == 0:
    print("Zero")
else:
    print("Positive")

marks = int(input("Enter marks (0-100): "))
if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 50:
    print("C")
else:
    print("Fail")

ch = input("Enter a character: ")
if ch.lower() in 'aeiou':
    print("Vowel")
elif ch.isalpha():
    print("Consonant")
else:
    print("Not an alphabet")

n = int(input("Enter number: "))
if n % 2 == 0 and n % 3 == 0:
    print("Divisible by 2 and 3")
elif n % 2 == 0:
    print("Divisible by 2")
elif n % 3 == 0:
    print("Divisible by 3")
else:
    print("Not divisible by 2 or 3")

s = input("Enter a string: ")
if len(s) == 0:
    print("Empty string")
elif s[0].lower() in 'aeiou':
    print("Starts with vowel")
else:
    print("Starts with consonant")

lst = eval(input("Enter a list: "))
if len(lst) == 0:
    print("Empty list")
elif len(lst) <= 3:
    print("Small list")
elif len(lst) <= 6:
    print("Medium list")
else:
    print("Large list")

student = {"name": "John", "age": 20, "marks": 85}
marks = student["marks"]
if marks >= 90:
    print("Excellent")
elif marks >= 75:
    print("Very Good")
elif marks >= 50:
    print("Average")
else:
    print("Poor")

month = int(input("Enter month number (1–12): "))
if month in (1,3,5,7,8,10,12):
    print("31 days")
elif month in (4,6,9,11):
    print("30 days")
elif month == 2:
    print("28 or 29 days")
else:
    print("Invalid month")

n = int(input("Enter a number: "))
if n < 10:
    print("Single digit")
elif n < 100:
    print("Two digits")
elif n < 1000:
    print("Three digits")
else:
    print("More than three digits")

temp = float(input("Enter temperature in Celsius: "))
if temp < 0:
    print("Freezing")
elif temp <= 20:
    print("Cold")
elif temp <= 30:
    print("Warm")
else:
    print("Hot")
    
s = input("Enter a string: ")
if len(s) == 0:
    print("Empty string")
elif len(s) <= 4:
    print("Short string")
elif len(s) <= 9:
    print("Medium string")
else:
    print("Long string")

n = int(input("Enter number: "))
if n % 4 == 0 and n % 6 == 0:
    print("Divisible by 4 and 6")
elif n % 4 == 0:
    print("Divisible by 4")
elif n % 6 == 0:
    print("Divisible by 6")
else:
    print("Not divisible by 4 or 6")

num = float(input("Enter a floating number: "))
if num < 0:
    print("Negative float")
elif num == 0:
    print("Zero")
elif num < 1:
    print("Fractional")
else:
    print("Positive float")

ch = input("Enter a character: ")
if ch.isdigit():
    print("Digit")
elif ch.isupper():
    print("Uppercase Letter")
elif ch.islower():
    print("Lowercase Letter")
else:
    print("Special character")

s = eval(input("Enter a set: "))
if len(s) == 0:
    print("Empty set")
elif len(s) == 1:
    print("Singleton set")
elif len(s) <= 4:
    print("Small set")
else:
    print("Large set")

year = int(input("Enter a year: "))
if year % 400 == 0:
    print("Leap Year")
elif year % 100 == 0:
    print("Not a Leap Year")
elif year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")

