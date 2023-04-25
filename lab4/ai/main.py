import numpy

#initializam vectorul de regine
def initialize_queens(n):
    #un vector pentru regine care va contine tuple linie-coloana
    queens = []
    for i in range(0, n):
        queens.append((-1, i+1))

    return queens


# initializam tabla de joc
def initialize_board(n):
    #generam o matrice nxn initializata cu 0
    m = numpy.random.randint(1, size=(n, n))
    return m

def put_restrictions_on_board(n, board, restrictions):
    for i in range(0,n):
        for j in range(0,n):
            for block in restrictions:
                if(i+1==block[0] and j+1==block[1]):
                    board[i][j]=-1
    return board

def check_row(row,board):
    for j in range(0,len(board)):
        if(board[row][j]==1):
            return False
    return True;

def check_column(column,board):
    for i in range(0,len(board)):
        if(board[i][column]==1):
            return False
    return True

def check_first_left_diagonal(row, column, board):
    curr_col=column
    curr_row=row
    while curr_row>=0 and curr_col>=0:
        if board[curr_row][curr_col]==1:
            return False
        curr_col-=1
        curr_row-=1
    return True

def check_second_left_diagonal(row, column, board):
    curr_col=column
    curr_row=row
    while curr_row<len(board) and curr_col>=0:
        if board[curr_row][curr_col]==1:
            return False
        curr_col-=1
        curr_row+=1
    return True

def posible_rows(board, column):
    rows = []
    for row in range(0,len(board)):
        if board[row][column-1]!=-1 and check_row(row,board) and check_column(column-1, board) and check_first_left_diagonal(row,column-1,board) and check_second_left_diagonal(row,column-1,board):
            rows.append(row)
    return rows

def posible_placement_of_the_next_queen(board):
    rows = []
    for row in range(0,len(board)):
        for col in range(0,len(board)):
            if board[row][col]!=-1 and check_row(row,board) and check_column(col, board) and check_first_left_diagonal(row,col,board) and check_second_left_diagonal(row,col,board):
                rows.append((row,col))
    return rows

def put_queen(row,column,board):
    if board[row][column]==0:
        board[row][column]=1
        return True
    return False

#cand va returna true=>si domeniul va fi epuizat
def FC(column, board):
    posible_values=posible_rows(board,column)
    t_posible_values=posible_values
    for i in posible_values:
        if ~(check_row(i,board) and check_column(column-1, board) and check_first_left_diagonal(i,column-1,board) and check_second_left_diagonal(i,column-1,board)):
            t_posible_values.remove(i)
    if(len(t_posible_values)==0):
        return True
    else:
        return False

def queens_problem_solve(board, i):
    domain = True
    if i == len(board):
        print(board)
        return True
    posible_r = posible_rows(board, i)
    print(posible_r,"astea sunt posibile")
    for r in posible_r:
        print(board, "asta e boardul inainte")
        put_queen(r, i, board)
        print(board,"asta e boardul dupa")
        x = posible_placement_of_the_next_queen(board)
        print(x,"prin asta iteram noi")
        for placement in x:
            if FC(placement[0], board):
                domain = False
        if domain:
            if(queens_problem_solve(board,i+1)):
                return True
                print("aici se termina domain si ", queens_problem_solve(board,i+1))
        board[r][i-1] = 0
        domain = True

n = int(input("Enter the number of queens: "))
board = initialize_board(n)
queens = initialize_queens(n)
print(board)
print("Initial positions: ")
print(queens)
blocks = []
while True:
    print("Enter blocker :")
    row = int(input("Row:"))
    column = int(input("Column:"))
    blocker = (row, column)
    if row == -1 and column == -1:
        break
    if blocker in blocks:
        print("Blocker already exists.")
    else:
        blocks.append(blocker)

print(blocks)

print(put_restrictions_on_board(n,board,blocks))

print(queens_problem_solve(board,1))

#Initial
"""
print(posible_rows(board,1))
print(posible_rows(board,2))
print(posible_rows(board,3))
print(posible_rows(board,4))
"""

