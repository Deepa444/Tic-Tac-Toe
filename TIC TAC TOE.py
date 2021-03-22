#TIC TAC Game

'''
1.create board
2. two players
3.flip(swap)players
4.check who is the winner
    ->row(3)
    ->columns(3)
    ->diagonals(2)
5.draw
    player--X
    player--O'''


#creation of the board

board=["-","-","-",
       "-","-","-",
       "-","-","-"]

current_player="X"
gameisgoing=True
winner=None
def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

def handle_turn():
    position=int(input("Choose a random position from 0 to 8:"))
    if position<8:
        board[position]=current_player
    if position>8:
        position=int(input("Plz... Choose a random position from 0 to 8:"))
    board[position]=current_player

def swap_player():
    global current_player
    if current_player=="X":
        current_player="O"
    elif current_player=="O":
        current_player="X"

def check_who_is_the_winner():
    global winner
    row_winner=check_row()
    col_winner=check_column()
    dia_winner=check_diagonal()
    check_tie()

    if row_winner:
        winner=row_winner
    elif col_winner:
        winner=col_winner
    else:
        winner=dia_winner

def check_row():
    global gameisgoing

    #player can win in three rows
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"

    if row1 or row2 or row3:
        gameisgoing=False

    if row1:
        return board[0]
    elif row2:
        return board[5]
    elif row3:
        return board[6]

'''
0 1 2
3 4 5
6 7 8
'''
def check_column():
    global  gameisgoing
    #player can win in three rows
    col1 = board[0] == board[3] == board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"

    if col1 or col2 or col3:
        gameisgoing=False

    if col1:
        return board[3]
    elif col2:
        return board[1]
    elif col3:
        return board[5]

def check_diagonal():
    global gameisgoing
    #player can win in two diagonals
    dia1=board[0]==board[4]==board[8]!="-"
    dia2=board[2]==board[4]==board[6]!="-"

    if dia1 or dia2:
        gameisgoing=False

    if dia1:
        return board[0]
    elif dia2:
        return board[6]

def check_tie():
    global gameisgoing

    if "-" not in board:
        gameisgoing=False
        print("Match is Tied")

def play_game():
    while gameisgoing:
        display_board()
        handle_turn()
        swap_player()
        check_who_is_the_winner()
    if winner=="X":
        print("X is the Winner")
    elif winner=="O":
        print("O is the Winner")
play_game()

