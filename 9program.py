#write a program to find the sum of the three numbers 
num=int(input("enter the number"))
a=num%10  # 678%10 -> 8
num= num//10       #then we get the 67 from the 678 we can // the of the 678 the answer will b 67
b=num%10   # 67%10 -> 7
num= num//10     #then we get the 6 from the 67 we can // the of the 67 the answer will b 6
c= num%10 # 6%10  ->  6
print("sum is :", a+b+c) 