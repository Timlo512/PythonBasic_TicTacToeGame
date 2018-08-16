import os

# Welcome to timtimtimab TicTacToeGame Project
# It is one of the milestone projects in Complete Python3 Basic Bootcamp
# taught by Jose Portilla
# Here is the link: https://www.udemy.com/complete-python-bootcamp/
# Please feel free to run the program and/or amend the code
# if you find somewhere which can be a bug/ potential error/ place to be improved
# It would be nice if you can post it to issue, I would fix it as soon as possible

# Clear output
def clear():
    os.system('clear')

# print the board
def display_board(board):
    clear()
    print(board[0],"|",board[1],"|",board[2])
    print("---------")
    print(board[3],"|",board[4],"|",board[5])
    print("---------")
    print(board[6],"|",board[7],"|",board[8])

# Control players' turns
def preset_input():
    x = "X turn, please enter a position: "
    o = "O turn, please enter a position: "
    global player_input
    global turn
    checking_list = ['1','2','3','4','5','6','7','8','9']
    if x_count == o_count:
        turn = "X"
        player_input = input(x)
        if player_input not in checking_list:
            print("Sorry, position is not found.")
            preset_input()
        else:
            pass
    else:
        turn = "O"
        player_input = input(o)
        if player_input not in checking_list:
            print("Sorry, position is not found.")
            preset_input()
        else:
            pass
        
# Control the input from players
def input_position(player_input,turn):
    player_input = int(player_input)
    global board
    if board[player_input-1] != "X" and board[player_input-1] != "O":
        board[player_input-1] = turn
    else:
        print("Position has been occupied!Please choose another position.")

# Check the game board and see if someone win the game, or the game has been tied
def checking():
    global x_count,o_count
    x_count = board.count("X")
    o_count = board.count("O")
    status = True
    for a in range(3):
        if board[a]==board[a+3]==board[a+6]==turn:
            print ("%s player wins!Congratulation!!"%(turn))
            status = False
        else:
            continue
    if board[0]==board[1]==board[2]==turn:
        print ("%s player wins!Congratulation!!"%(turn))
        status = False
    else:
        pass
    if board[3]==board[4]==board[5]==turn:
        print ("%s player wins!Congratulation!!"%(turn))
        status = False
    else:
        pass
    if board[6]==board[7]==board[8]==turn:
        print ("%s player wins!Congratulation!!"%(turn))
        status = False
    else:
        pass
    if board[0]==board[4]==board[8]==turn:
        print ("%s player wins!Congratulation!!"%(turn))
        status = False
    else:
        pass
    if board[2]==board[4]==board[6]==turn:
        print ("%s player wins!Congratulation!!"%(turn))
        status = False
    else:
        pass
    if x_count + o_count == 9:
        print("Game over, tied")
        status = False
    return(status)

# main function to control the game flow
def tic_tac_toe_game():
    global board
    board = [1,2,3,4,5,6,7,8,9]
    display_board(board)
    while(checking()):
        preset_input()
        input_position(player_input,turn)
        display_board(board)
    restart = input("Do you want to restart the game? Y/N")
    if restart == "Y":
        tic_tac_toe_game()
    else:
        print("thank you! See you next time. bye~")
        print("To restart the game, please type tic_tac_toe_game().")

tic_tac_toe_game()
