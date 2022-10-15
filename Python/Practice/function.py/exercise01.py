# define a function which takes two number as input and return greater of two numbers.

def greater (num1, num2):
    if num1 > num2:
        return f"{num1} is greater than {num2}"
    return f"{num2} is greater than {num1}"

num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))

print(greater(num1, num2))