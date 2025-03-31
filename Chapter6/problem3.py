#a program to find whether a given username contains less than 10 characters or not.
user=input("Enter your usrename:")
if(len(user)<10):
    print("Username contains less than 10 characters")
else:
    print("Username contains more than 10 character and is valid")