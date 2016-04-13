import re

def validemail(): 
    email= userInput = input("please enter an email: ");
    match= re.search(r'[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+.[a-zA-Z]',email)
    if match:
        print("Valid Email")
    else:
        print("Invalid Email")
    
    
validemail() 