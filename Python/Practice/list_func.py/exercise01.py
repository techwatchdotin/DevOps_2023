# define a function which will take list containing numbers as input
# And return list containing square of every elements.

# example:
# numbers = [1,2,3,4]
# square_list(numbers) ------> return ------> [1,4,9,16]


def square_list (list):
    output = []
    for i in list:
        output.append(i**2)
    return output

listA = [1,2,3,4]
print(square_list(listA))