# EXERCISE - WATCH COCO

# Ask user's name and age
# If user's name start with ('a' or 'A') and age is above 10 then
# Print "You can watch coco movie"
# Else print "Sorry - You cannot watch COCO"

username = input("Enter your name : ")
userage = int(input("Enter your age : "))

if username[0] == 'a' or username[0]=='A' and userage > 10:
    print("You can watch COCO movie")
else:
    print("Sorry - You can't watch COCO")