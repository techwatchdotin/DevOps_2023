# find : to find the position of any word/character
# replace : to replace

string = "She is a beautiful and she is a dancer as well"

# string=string.replace(" ", "_")

# print(string)

# string=string.replace("_", " ", 2)

# print(string)

# print(string.find("is"))
# print(string.find("is", 5))

# if we don't know the position of fist "is":

is_pos1 = string.find("is")
is_pos2 = string.find("is", is_pos1 + 1)

print(is_pos2)

