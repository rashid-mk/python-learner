import random
import time
a=1 
b=6
want_to_roll_again = 'y'
while want_to_roll_again=='y':
    print('Rolling the dice...')
    time.sleep(1)
    dice_value=random.randint(a,b)
    print(dice_value)
    want_to_roll_again=str(input('Roll the dice again? (y / n) : '))
    want_to_roll_again=want_to_roll_again.lower()