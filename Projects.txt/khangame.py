# Guessing number game, try to beat it

import random 



def khang():
    while True:
        try:
        
            x = range(1,100)
            n = random.randint(1, 100)
            lol = int(input('Enter a number from 1-100: '))
            if lol in x :
                print('Number')
                if lol > n:
                    print('Too high')
                    continue
                if lol < n:
                    print('Too low')
                    continue
                elif lol == n:
                    ('you got it 😎')
                    break

                   
            else:
                print('try again')
                continue

        except ValueError as e:
            print(f'{e} Try again')
 
khang()
