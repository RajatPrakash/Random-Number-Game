import random

guess = random.randint(0, 10)
print(' You will only be given 3 attempts, try to crack it ')
guess_time = 3
flag = 0

while guess_time != 0:
    if guess_time == 1:
        print('Do you want the hint! , Yes | No ')
        hint = input('Want!').lower()
        if hint == 'yes':
            print('there is None  ;) ')
        else:
            print('GO try your luck for the last time')

    user_input = int(input('GUESS: '))
    if user_input == guess:
        #  print('Bravo you won the Game')
        flag =0
        break
    else:
        flag = 1
        guess_time = guess_time-1


if flag == 0:
    print(f' congrats buddy you Won Guessed number was {guess}')
elif flag == 1:
    print(f'You loose Buddy, guessed was {guess}')