# last exercise:
# function
# input - [1,2,3, [1,2], [3,4]]
# output - 2


def func (l):
    list_count = 0
    for i in l:
        if type(i)==list:
            list_count+=1
    return list_count

a = [1,2,3, [1,2], [3,4]]
print(func(a))