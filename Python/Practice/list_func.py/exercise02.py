# define a function which will take list as a argument and this function will return a reverese list.

# Example:

# [1,2,3,4] --------> [4,3,2,1]
# ['word1', 'word2']------>['word2', 'word1']

# Note : You simply do this with reverse method or [::-1]
# but try to do this with the help of append and return method



# def rev_list (list):
#     return list[::-1]




# listA = [1,2,3,4]
# listB = ['word1', 'word2', 'word3']
# print(rev_list(listA))
# print(rev_list(listB))

def rev (list):
    output = []
    for i in range (1, len(list)+1):
        popped_item = list.pop()
        output.append(popped_item)
    return output


listA = [1,2,3,4,5]
# print(listA)

# x=listA.pop()
# print(x)

print(rev(listA))