#Program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user
m1=int(input("Enter the marks of DSA:"))
m2=int(input("Enter the marks of DBMS:"))
m3=int(input("Enter the marks of OS:"))
total_marks=(m1+m2+m3)/3
if(total_marks>=40 and m1>=33 and m2>=33 and m3>=33):
    print("You are pass")
elif(total_marks>=40 and m1<=33 and m2>=33 and m3>=33):
    print("You are fail in DSA")
elif(total_marks>=40 and m1>=33 and m2<=33 and m3>=33):
    print("You are fail in DBMS")
elif(total_marks>=40 and m1>=33 and m2>=33 and m3<=33):
    print("You are fail in OS")
else:
    print("You are fail in all subjects")
