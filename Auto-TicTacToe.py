import time
import system_position
from system_position import check_win

#values of the different positions
v = {
    1: " ",
    2: " ",
    3: " ", 
    4: " ", 
    5: " ",
    6: " ", 
    7: " ", 
    8: " ", 
    9: " "
}

winning_rows = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
winning_rows2 = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]

#board showing allocation of different grids to certain number
board_chart = '''
|1|2|3|
|4|5|6|
|7|8|9|
'''
print("\nTICTACTOE (vs Computer)\n")

time.sleep(0.3)
level = input("\nChoose level: Easy/Medium/Hard(E/M/H): ").lower()
play_first = input("First chance -> x/o(player/system): ").lower()
time.sleep(0.3)

time.sleep(1)
print("\nAssign the value of 'x' in a particlular grid by entering the allotted positon.")
print("(Type '0' anytime to get the board chart)\n")
print(board_chart)
time.sleep(0.5)

i=0

#locations available for player and system
locations=[1,2,3,4,5,6,7,8,9]

options = ["x", "o"]

oLoc=0
xLoc=0

#Player plays first
if play_first == "x":
    while True:
        #this increment in 'i' is for checking 'Tie' situation
        i=i+1

        #Player's Turn: ----------------------
        while True:
            try:
                xLoc = int(input('\nx: '))
                if xLoc in locations:
                    break
                elif xLoc == 0:
                    print(board_chart)
                else:
                    print("Invalid Input, Try Again")
                    continue
            except:
                print("Invalid Input, Try Again")
                continue

        #Assigning x's position (player's positon)
        v[xLoc] = 'x'

        #this location gets removed from that list as it has been used
        locations.remove(xLoc)

        #board showing x's position
        board = f'''
        |{v[1]}|{v[2]}|{v[3]}|
        |{v[4]}|{v[5]}|{v[6]}|
        |{v[7]}|{v[8]}|{v[9]}|
        '''
        print(board)

        #logic if there is a 'win' for x or a 'tie' or 'the game is still on'
        if check_win(v, winning_rows2)==1:
            time.sleep(0.5)
            print("\nPlayer WINS !")
            time.sleep(2)
            break
        elif i==5:
            time.sleep(0.5)
            print("\nTIE")
            time.sleep(2)
            break
        else:
            pass

        #System's Turn: ----------------------
        oLoc=0

        # Function for getting the most approriate position for system (according to the level selected)

        get = system_position.win(v, oLoc, options, level, winning_rows)
        if get != 0:
            oLoc = get

        else:
            if level == "easy" or level == "e":
                oLoc = system_position.system_logic_easy(v, options, xLoc, oLoc, i, locations)
            if level == "medium" or level == "m":
                oLoc = system_position.system_logic_medium_second(v, options, xLoc, oLoc, i, locations)
            if level == "hard" or level == "h":
                oLoc = system_position.system_logic_hard_second(v, options, xLoc, oLoc, i, locations)
            
        #final location of 'o' (system)
        v[oLoc] = 'o'
        locations.remove(oLoc)

        board = f'''
        |{v[1]}|{v[2]}|{v[3]}|
        |{v[4]}|{v[5]}|{v[6]}|
        |{v[7]}|{v[8]}|{v[9]}|
        '''

        #interactive text for engaging the player
        time.sleep(0.5)
        print('\nComputer is thinking...')
        time.sleep(1.5)
        print(board)

        #logic to check if there is a 'win' or 'the game is still going on' for system
        if check_win(v, winning_rows2)==0:
            time.sleep(0.5)
            print("\nComputer WINS !")
            time.sleep(2)
            break
        else:
            continue

#System plays first
if play_first == "o":
    #System's Turn: ----------------------
    while True:
        i=i+1

        oLoc=0


        # Function for getting the most approriate position for system (according to the level selected)
        
        get = system_position.win(v, oLoc, options, level, winning_rows)
        if get != 0:
            oLoc = get

        else:
            if level == "easy" or level == "e":
                oLoc = system_position.system_logic_easy(v, options, xLoc, oLoc, i, locations)
            if level == "medium" or level == "m":
                oLoc = system_position.system_logic_medium_first(v, options, xLoc, oLoc, i, locations)
            if level == "hard" or level == "h":
                oLoc = system_position.system_logic_hard_first(v, options, xLoc, oLoc, i, locations)

        #final location of 'o' (system)
        v[oLoc] = 'o'
        locations.remove(oLoc)

        board = f'''
        |{v[1]}|{v[2]}|{v[3]}|
        |{v[4]}|{v[5]}|{v[6]}|
        |{v[7]}|{v[8]}|{v[9]}|
        '''

        #interactive text for engaging the player
        time.sleep(0.5)
        print('\nComputer is thinking...')
        time.sleep(1.5)
        print(board)

        #logic to check if there is a 'win' or 'the game is still going on' for system
        if check_win(v, winning_rows2)==0:
            time.sleep(0.5)
            print("\nComputer WINS !")
            time.sleep(2)
            break
        elif i==5:
            time.sleep(0.5)
            print("\nTIE")
            time.sleep(2)
            break
        else:
            pass

    #Player's Turn: ----------------------
        while True:
            try:
                xLoc = int(input('\nx: '))
                if xLoc in locations:
                    break
                elif xLoc == 0:
                    print(board_chart)
                else:
                    print("Invalid Input, Try Again")
                    continue
            except:
                print("Invalid Input, Try Again")
                continue

        #Assigning x's position (player's positon)
        v[xLoc] = 'x'

        #this location gets removed from that list as it has been used
        locations.remove(xLoc)

        #board showing x's position
        board = f'''
        |{v[1]}|{v[2]}|{v[3]}|
        |{v[4]}|{v[5]}|{v[6]}|
        |{v[7]}|{v[8]}|{v[9]}|
        '''
        print(board)

        #logic if there is a 'win' for x or a 'tie' or 'the game is still on'
        if check_win(v, winning_rows2)==1:
            time.sleep(0.5)
            print("\nPlayer WINS !")
            time.sleep(2)
            break
        else:
            pass
