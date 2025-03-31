# a program to calculate the grade of a student from his marks from the following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F
m1=int(input("Enter the marks of DSA:"))
m2=int(input("Enter the marks of OS:"))
m3=int(input("Enter the marks of Python:"))
m4=int(input("Enter the marks of DBMS:"))
total_marks=(m1+m2+m3+m4)/4
if(90<total_marks<=100):
    print("You are excellent!")
elif(80<total_marks<=90):
    print("You scored A Grade")
elif(70<total_marks<=80):
    print("You scored B Grade")
elif(60<total_marks<=70):
    print("You scored C Grade")
elif(50<total_marks<=60):
    print("You scored D Grade")
elif(0<total_marks>50):
    print("You scored F Grade")
else:
    print("Enter proper marks")
    



