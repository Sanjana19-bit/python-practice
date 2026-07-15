#Loop
# a = int(input('Enter the number'))
# i = 1
# while i<11:
#     print(a*i)
#     i+=1 
# else:
#     print('limit crossed')


#Guessing game
#generate a random integer betweeen 1 and 100
import random
jackpot=random.randint(1,100)

guess= input(input('guess karo'))
counter =1
while(guess != jackpot):
    if guess<jackpot:
        print('galt! guess higher')
    else:
        print('galt!guess lower')  
    guess = int(input('guess karo'))
    counter += 1
else:
    print('correct guess')
    print('attempts',counter)



