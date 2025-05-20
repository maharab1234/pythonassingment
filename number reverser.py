num = int(input("Enter a number: "))
sum = 0
digits = len(str(num))

for digit in str(num):
    sum += int(digit) ** digits

if sum == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")