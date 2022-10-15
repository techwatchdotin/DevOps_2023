# define a function that take list fo words as argument and 
# return list with reverse of every element in that list.

# example:
# ['abc', 'tuv', 'xyz'] ----> ['cba', 'vut', 'zyx']


def func (list):
    output = []
    for i in list:
        output.append(i[::-1])
    return output

l = ['abc', 'tuv', 'xyz']
print(func(l))