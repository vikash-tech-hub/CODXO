import random 
char="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&*(){}[]"
length=int(input("enter the password length"))
password=""
for i in range(length):
    password+=random.choice(char)
print(password)

