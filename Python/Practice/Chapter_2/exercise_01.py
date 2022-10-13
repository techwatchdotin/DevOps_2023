# Ask user to input 3 numbers and you have to print average of three number using string formating.

# Bonus : try to take all three comma separated inputs in one line.

num1, num2, num3 = input("Enter the integer number : ").split(",")
print((int(num1) + int(num2) + int(num3)) / 3)