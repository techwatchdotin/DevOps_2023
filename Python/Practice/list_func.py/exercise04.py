# filter odd even
# define a function
# input
# list ---> [1,2,3,4,5,6,7]
# output ----> [[1,3,5,7],[2,4,6]]

def odd_even (l):
    odd = []
    even = []
    for i in l:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return [odd,even]

listA = list(range(1,10))
print(odd_even(listA))