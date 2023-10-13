#write a program that input the salary and grade , its add 50% bnouns if the grade is grater then
#15 its add 25% if the grde is 15 or less then the 15 and then display the total salry
s=int(input("enter the salary"))
g=int(input("enter the grade"))

if g>=15:
    b=s*50/100   #its add 50% bouns if the g is 15or 15+
else:
    b=s*25/100    #its add 25% bouns if the g is less then 15
s=s+b
print("YOUR TOTAL SALARY IS RS",s)
