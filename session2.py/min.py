#write a program to find the min number
a=input("enter the first number")
b=input("enter the second number")
c=input("enter the third number")
if a<b and a<c:
    print("the min number is ",a)
elif b<a and b<c:
    print("the min number is ", b)
else:
    print("the min number is ",  c)
    