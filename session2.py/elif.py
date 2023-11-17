email=input("enter the your mail")
pasword=input("enter the password ")
if email=='farhanrasool0422@gmail.com' and pasword =='12345':
  print("welcome to your account")
elif email=='farhanrasool0422@gmail.com' and pasword !='12345':
    pasword= input("enter your password again")
    if email=='farhanrasool0422@gmail.com' and pasword =='12345':
        print("finaly welcome to the ur account")
    else:
        print("na beta tum se na ho pae ga")
else:
    print("you can enter the incorect password")

    