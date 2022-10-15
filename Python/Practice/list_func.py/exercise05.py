# common elements finder function
# define a function which take 2 lists as input and return a list 
# which contains common elements of both lists.

# example:
# input ----> [1,2,5,8], [1,2,7,6]
# output ---> [1,2]

#----------------------------------------------------------------( Method - 1)-----------------------------------------------------------------

# def common (l1,l2):
#     com = []
#     for i in l1:
#         for j in l2:
#             if j == i:
#                 com.append(j)
#     return com

# a = [1,2,5,8]
# b =  [1,2,7,6]

# print(common(a, b))

# --------------------------------------------------------------(Method - 2)----------------------------------------------------------------------

def common(l1,l2):
    output = []
    for i in l1:
        if i in l2:
            output.append(i)
    return output

a = [1,2,5,8]
b =  [1,2,7,6]

print(common(a, b))