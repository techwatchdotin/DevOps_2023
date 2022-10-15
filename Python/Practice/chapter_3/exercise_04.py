# problem
# ask user to input a number containing more than one digit
# example - 1256
# calculate 1+2+5+6 and print

# algorithm - (method to solve problem in human language)
# ask input in string, i.e don't change string to int
# example - "1256"
# int(example[0]) + int(example[1])... go upto len(example)

num = input("Enter a number containing more that one digit : ")

# while loop :
total = 0
i = 0
while i < len(num):
    total += int(num[i])
    i += 1

print(total)

# # for loop:

# total = 0

# for i in num:
#     total += int(i)

# print(total)