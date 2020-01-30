import os
os.system('cls')

number1 = int(input("How many numbers does your arithmetic mean have? "))
total_sum = 0
for n in range (number1):
    number2 = float(input("Number: "))
    total_sum += number2
result = total_sum / number1
print("The result is", result)
input()
