# Write a Python function that will accept as input three string values from a user. The method will return to the user a concatenation of the string values in reverse order. The function is to be called from the main method.
# In the main method, prompt the user for the three strings.


# main function defined to be called later
def main():
    # User will be asked to input 3 strings
    print("====== String Values in Reverse Order ======")
    string1 = str(input("Enter First String: "))
    string2 = str(input("Enter Second String: "))
    string3 = str(input("Enter Third String: "))
# 3 strings are concatenated
    concatenated_string = string1 + string2 + string3
# print out concatenated strings in reverse order
    print("Strings in Reverse Order: ", concatenated_string[::-1])


# calling the main function 
main()
