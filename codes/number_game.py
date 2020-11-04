import random
print("Welcome")
tries = 1
number_to_guess=random.randint(1,10)
guess=int(input('guess a number between 1 and 10 : '))
while number_to_guess !=guess:
    print('sorry wrong guess')
    if tries == 4:
        break
    elif guess < number_to_guess:
        print('your guess was lower than the number')
    else:
        print('your guess was higher than the number') 
           
    guess = int(input('please guess again : '))
    tries += 1 

if (number_to_guess==guess):
    print('won')
else: 
    print('lose')
print('game over!!!!')               
