# 1. Check if a Number is Even or Odd


num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# 2. Check if a Year is a Leap Year

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")



# 3. Divisible by both 3 and 5

num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by 3 and 5")
else:
    print("Not divisible by 3 and 5")



# 4. Eligible to Vote

age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")



# 5. Check if a number is a multiple of 10

num = int(input("Enter a number: "))
if num % 10 == 0:
    print("Multiple of 10")
else:
    print("Not a multiple of 10")



# 6. Compare two numbers and print the smaller one

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a < b:
    print("Smaller number is:", a)
else:
    print("Smaller number is:", b)




# 7. Classification based on divisibility

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
elif num % 5 == 0:
    print("Divisible by 5")
else:
    print("Odd" if num % 2 != 0 else "Not divisible by 2 or 5")



# 8. Age classification

age = int(input("Enter your age: "))
if age < 13:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 59:
    print("Adult")
else:
    print("Senior")



# 9. Check range of a number

num = int(input("Enter a number: "))
if num < 0:
    print("Below 0")
elif num < 10:
    print("Between 0 and 10")
elif num < 50:
    print("Between 10 and 50")
else:
    print("Above 50")




# 10. Temperature to Fahrenheit & Comment

celsius = float(input("Enter temperature in Celsius: "))
if celsius < 0:
    print("Below freezing point")
elif celsius < 25:
    print("Cool")
elif celsius <= 40:
    print("Warm")
else:
    print("Hot")