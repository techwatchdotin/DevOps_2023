# take two comma separed inputs from user
# 1.) user's name
# 2.) a single character

# Output - print 2 lines
# 1.) user's name lenth
# 2.) count the character that user inputed (bonus : case insensitive count)


name, char = input("Enter your name and character you want to count : ").split(",")

name=name.lower().strip()
char=char.lower().strip()

print(f"Lenth of your name is {len(name)}")
print(f"Count of \"{char}\" in your name is {name.count(char)}")



# print(f"Lenth of your name is {len(name)}")

# count = 0
# for i in name:
#     if i==char:
#         count+=1
# print(f"Count of \"{char}\" in your name is {count}")

