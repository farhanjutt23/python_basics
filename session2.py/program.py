#write a program that input the any three number from the user then write the sum of the numbers
number=int(input("Enter a number"))
a=number%10 
number=number//10
b=number%10
number=number//10
c=number%10
number=number//10
d=number%10
print("The sum of the 4 digits number",a+b+c+d)


