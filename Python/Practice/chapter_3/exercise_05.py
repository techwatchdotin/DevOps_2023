# ask user for name
# Example - Kaushlendra Kumar
# print count of each character
# Output : 

# k : 2
# a : 3
# u : 2
# s : 1
# h : 1
# l : 1
# e : 1
# n : 1
# d : 1
#   : 1
# r : 2


name = input("Enter your name : ")
name = name.lower().strip()

#while loop:
# temp_var = ""
# i = 0
# # while i < len(name):
# #     if i not in temp_var:
# #         print(f"{name[i]} : {name.count[i]}")


# # for loop :

temp_var = ""
for i in name:
    if i not in temp_var:
        print(f"{i} : {name.count(i)}")
        temp_var += i


