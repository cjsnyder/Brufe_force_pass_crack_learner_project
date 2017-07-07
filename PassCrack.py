""" PassCrack ~ Conner Snyder ~ 7/7/17
Purpose - Demonstrate basic concepts and show progress towards larger projects
Suggested by: Sydni from FBLA """
import string

finalPass = ""
def checkPass(password):
    for letter in password:
        if letter in string.printable:
            finalPass += letter
    return finalPass

userPassword = input("Enter your password: ")
print(checkPass(userPassword))
