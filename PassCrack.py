""" PassCrack ~ Conner Snyder ~ 7/7/17
Purpose - Demonstrate basic concepts and show progress towards larger projects
Suggested by: Sydni from FBLA """
import string

def checkPass(password):
    finalPass = ""
    while len(finalPass) < len(password):
        for letter in password:
            if letter in string.printable:
                finalPass += letter
            print("Letter found: " + letter)
            print("Password currenly is: " + finalPass)
    print("\nCracked password is: " + finalPass)


userPassword = input("Enter your password: ")
checkPass(userPassword)
