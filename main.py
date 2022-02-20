from config import GAME_CHOICE, RULES
import random

def get_user_choice():

    user_input = input('your choice:(r, p, s):\n')

    if user_input not in  GAME_CHOICE:
        print('Wrong choice!!! please try again\n')
        return get_user_choice()
    
    return user_input

def get_system_choice():

    system_input = random.choice(GAME_CHOICE)
    return system_input

def find_winer(user_choice, system_choice):

    
    match = {user_choice, system_choice}

    if len(match) == 1:
        return None

    match = tuple(sorted(match))

    return RULES[match]



def play():
    
    while True:

        user_point = 0
        system_point = 0
        user_choice = get_user_choice()
        print('user choice is :', user_choice,  '\n' )

        system_choice = get_system_choice()
        print('system choice is :', system_choice, '\n' )


        winer = find_winer(user_choice, system_choice)

        if winer == user_choice:
            user_point += 1
            print('you won!\n')
        elif winer == system_choice:
            system_point += 1
            print('you lose!\n')
        else:
            print("draw!\n")

        con = input('would you like to continue? enter y:\n')
        if con != 'y':
            if user_point > system_point:
                print('YOU WON THE GAME !!!!!!!!!!!!!!!!!!!\n')
            elif user_point < system_point:
                print('YOU LOSE THE GAME !!!!!!!!!!!!!!!!!!\n')
            else:
                print('DRAW!!!!!!!!!!!!!!!!!!!\n')
            break

play()