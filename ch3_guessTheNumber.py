#Writing a gues the Number Game
import random

misteryNumber = random.randint(1,5)
for i in range (5,0,-1):
    print ('enter a numer')
    try :
        enterNumber = int(input())
        if enterNumber < misteryNumber:
            print('Your enterNumber is too low.')
        elif enterNumber > misteryNumber:
            print('Your enterNumber is too high.')
        else:
            print('This condition is the correct enterNumber!')
            break    # This condition is the correct enterNumber!
    except ValueError:
        print('Enter a valid number')


if enterNumber != misteryNumber:
    print ('you miss your chances, mistery number is:', str(misteryNumber))
