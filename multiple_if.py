a=int(input("Enter your age:"))
#if statement1
if(a%2==0):
    print("a is even")
#End of if statement1    

#if statement2
if(a>18):
     print("You are above the age of concent")
     print("Good for you")
elif(a<0):
    print("You are entering an invalid negative age")
elif(a==0):
    print("Yopu are entering 0 which is not a valid age")
else:
    print("You are below the age of concent")
#End of if statement2
print("End of a program")