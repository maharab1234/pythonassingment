age = int(input("Enter age: "))

if 0 <= age <= 1:
    print("Infant")
elif 2 <= age <= 3:
    print("Toddler")
elif 4 <= age <= 12:
    print("Child")
elif 13 <= age <= 19:
    print("Teenager")
elif age >= 20:
    print("Adult")
else:
    print("Invalid age")