import random


def list_configure():
    x = ''
    while type(x) != int:
        try:
           x = int(input('How many players are there: '))
        except Exception as err:
            print(err)
            print('Please enter a integer number!!!')
    list0=[]
    while len(list0) < x:
        registerer = input('What is the players name: ')
        registerer = registerer.lower()
        registerer = registerer.capitalize()
        if registerer in list0:
            print('This name is already in please enter a new name or enter with surname.')
            continue

    return list0

def dice_game(players):

    list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    ##
    dictofplayers = {}
    registeredpeople=[]
    ##

    for i in range(len(players)):
        player = ''
        while player not in players or player in registeredpeople:
            player = input('Which one is going to roll the dices? ')
            player = player.lower()
            player = player.capitalize()
            if player in registeredpeople:
                print('This player is already registered. Please enter a new name or enter with surname.')



    ##
        registeredpeople.append(player)
        first = random.choice(list_of_numbers)
        second = random.choice(list_of_numbers)
        sum = first + second
        print(f'Player {player} has the sum {sum}')
        dictofplayers[player] = sum

    ##

    listofsums = list(dictofplayers.values())
    maximum=max(listofsums)
    winner = 0
    for i in dictofplayers.keys():
        if dictofplayers[i]==maximum:
            winner += 1
            print(f'Player {i} has won the game with the sum {maximum}')
    if winner > 1:
        print('More than one player has won the game no absolute winners')

def dice_game_v2(**players2):
    list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    for player in players2.keys():
        player = ''
        while player not in players2:
            player = input('Which one is going to roll the dices? ')
            player = player.lower()
            player = player.capitalize()
        first = random.choice(list_of_numbers)
        second = random.choice(list_of_numbers)
        sum = first + second
        print(f'Player {player} has the sum {sum}')
        players2[player]=sum
    listofsums = list(players2.values())
    maximum = max(listofsums)
    winner = 0
    for i in players2.keys():
       if players2[i] == maximum:
           winner += 1
           print(f'Player {i} has won the game with the sum {maximum}')
    if winner > 1:
       print('more than one winner')


Players_list=list_configure()
dice_game(Players_list)
#dice_game_v2(Eren='0', Atakan='0', Adem=0, Tuncay=0)