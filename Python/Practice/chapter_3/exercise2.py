# Define is_palindrome function that take one word in string as input.
# And return True if it is palindrome else return False.

# Palindrome - word that reads same backwards as forwards.

# example:
# is_palindrome("madam") ---------> True
# is_palindrome("naman") ---------> True
# is_palindrome("horse") ---------> False

# Logic (algorithm)
# step 1 -> reverse the sting
# step 2 -> compare reversed string with original string.

def is_palindrome (l):
    if l == l[::-1]:
        return True
    return False

name = input("Enter your name : ")
print(is_palindrome(name))