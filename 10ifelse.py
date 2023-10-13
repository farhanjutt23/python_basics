#in the ifelse program we can write the our gmail and password if our password is correct then print congratiolation other wise sorry
# gmail= farhanrasool0422@gmail.com
#password=165609
email= input("enter ur gmail")
password= input("enter ur password")
if email == 'farhanrasool0422@gmail.com' and password == '165609':
    print("congratiolation you are login")
elif  email == 'farhanrasool0422@gmail.com' and password !='165609': 
    print("ur password is incorrect")
    password= input("enter password again")
    print("congratilation ur passoword is correct")   
else:
    print("your password and gmail is incoreect")
    print("please try again if u want to login ur password")
