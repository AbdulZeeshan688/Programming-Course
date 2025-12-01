# A10_T7.py

def generateField(rows, cols, mines):
    board = [[0]*cols for _ in range(rows)]

    for r,c in mines:
        board[r][c] = "*"

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == "*":
                continue
            count = 0
            for dr in [-1,0,1]:
                for dc in [-1,0,1]:
                    nr=r+dr; nc=c+dc
                    if 0<=nr<rows and 0<=nc<cols:
                        if board[nr][nc]=="*":
                            count+=1
            board[r][c] = count
    return board

def printField(board):
    for row in board:
        print(" ".join(str(x) for x in row))

def main():
    rows = int(input("Rows: "))
    cols = int(input("Cols: "))
    m = int(input("Number of mines: "))

    mines=[]
    for i in range(m):
        r=int(input("Mine row: "))
        c=int(input("Mine col: "))
        mines.append((r,c))

    field = generateField(rows, cols, mines)
    printField(field)

main()
