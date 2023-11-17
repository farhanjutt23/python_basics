#write a program to find the max number
a=input("enter the first number")
b=input("enter the second number")
c=input("enter the third number")
if a>b and a>c:
    print("the max number is ", a)
elif b>a and b>c:
    print("the max number is ",b)
else:
    print("the max number is ", c)