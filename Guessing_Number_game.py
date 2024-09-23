import random
#we can guess the number between 1 to 100
num=random.randint(1,100) #use of random int is any value asign of any variable  
guess=int(input("enter the number any 1 To 100"))
while guess!=num:
    if guess<num :
        print("your guess is too low")
    elif guess >num:
        print("your guess is too high")
    guess=int(input("guess again"))
print("you guess is right")