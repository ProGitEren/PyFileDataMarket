import random


player = input('Your name: ')
listofgame = ['rock', 'scissors', 'paper']


while True:
    computerhand = random.choice(listofgame)
    try:
        playerhand = input('rock/scissors/paper')
        playerhand = playerhand.lower()
        print(f'Player: {playerhand}')
        print(f'computer: {computerhand}')
        if playerhand not in listofgame:
            raise Exception("Not Listed")
        if playerhand == 'rock':
            if computerhand == 'rock':
                print('Tie')
            elif computerhand == 'scissors':
                print('You won')
            else:
                print('You lost')
        if playerhand == 'scissors':
            if computerhand == 'scissors':
                print('Tie')
            elif computerhand == 'paper':
                print('You won')
            else:
                print('You lost')
        if playerhand == 'paper':
            if computerhand == 'paper':
                print('Tie')
            elif computerhand == 'rock':
                print('You won')
            else:
                print('You lost')
        answer = input('Do you want con?(y for yes n for n): ')
        if answer=='n':
            break

    except Exception as err:
        print(err)
    except:
        print('Not appropriate input')





