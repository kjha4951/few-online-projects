import random

top_of_range=input("Type a number: ")
if top_of_range.isdigit():
    top_of_range=int(top_of_range)
    
    if top_of_range==0:
        print("please type a number which is greater then zero next time.")
        quit()
else:
    print("Please type number next time.")
    quit()
random_number=random.randint(0,top_of_range)#it will except 11
# print(random_number)

guesses=0

while  True:
   
    user_guess=input("Make a guess: ")
    guesses += 1
    if user_guess.isdigit():
       user_guess=int(user_guess)
    
    else:
        print("Please type number next time.")
        continue
   
    if user_guess==random_number:
        print("you got it! ")
        break
    
    elif user_guess>random_number:
           print("you are above the number ")
    else:
           print("you are below the number")
    

print("you got it in "+ str(guesses) + " gueesses")