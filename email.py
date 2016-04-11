def validemail(): 
    email= userInput = input("please enter an email: ");
    validemail= (r"[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+.[a-zA-Z]",email)
    if validemail:
        print("Valid Email")
    else:
        print("Invalid Email")
    
    
validemail() 