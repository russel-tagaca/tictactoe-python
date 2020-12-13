from tkinter import *
from tkinter.messagebox import showinfo

root = Tk()
root.title('Tic-Tac-Toe')

header = Label(root, text="Turn: ")
header.pack()


varPlayer1 = StringVar()
varPlayer1.set('Player1')

scorePlayer1 = IntVar()
scorePlayer1.set(0)

scorePlayer2 = IntVar()
scorePlayer2.set(0)

varPlayer2 = StringVar()
varPlayer2.set('Player2')

currPlayer = StringVar()
currPlayer.set(varPlayer1.get())
status = Label(root, textvariable=currPlayer)
status.pack()


frame = LabelFrame(root, text="", padx=100, pady=30)
frame.pack(padx=10, pady=10)

header1 = Label(frame, text="Score")
header1.grid(row=0, column=1)

header1 = Label(frame, textvariable=scorePlayer1)
header1.grid(row=0, column=0, pady=30)

header2 = Label(frame, textvariable=scorePlayer2)
header2.grid(row=0, column=2, pady=30)


winner = [
            [1,2,3],[4,5,6],[7,8,9],
            [1,4,7],[2,5,8],[3,6,9],
            [1,5,9],[3,5,7]
        ]

player1Board = []
player2Board = []
currNumTiles = IntVar()
currNumTiles.set(0)


def popup_showinfo(player=None):
    if player is None:
        showinfo("", "No Winner")
    else:
        if (player == "Player1"):
            scorePlayer1.set(scorePlayer1.get()+1)
            print(scorePlayer1.get())
        else:
            scorePlayer2.set(scorePlayer2.get()+1)
        showinfo("", "Winner: " + player + "!")
    clear()


def findWinningTri(playerBoard):
    if (len(playerBoard) > 2):
        playerBoard.sort()
        iterNum = len(playerBoard)
        for i in range(0,len(playerBoard)-2):
            for j in range(i+1, len(playerBoard)-1):
                for k in range(j+1, len(playerBoard)):
                    if ([playerBoard[i],playerBoard[j],playerBoard[k]] in winner):
                        return True
    return False


def changePlayer(boardNum):
    if (currPlayer.get() == varPlayer1.get()):
        currPlayer.set(varPlayer2.get())
    else:
        currPlayer.set(varPlayer1.get())
        
        

def changeTile(boardNum):
    if (boardNum == 1 and row1col1['text'] == ""):
        row1col1['fg'] = 'red' if (currPlayer.get() == varPlayer1.get()) else 'blue'
        row1col1['text'] = 'X' if (currPlayer.get() == varPlayer1.get()) else 'O' 
        return True
    elif (boardNum == 2 and row1col2['text'] == ""):
        row1col2['fg'] = 'red' if (currPlayer.get() == varPlayer1.get()) else 'blue'
        row1col2['text'] = 'X' if (currPlayer.get() == varPlayer1.get()) else 'O'
        return True 
    elif (boardNum == 3 and row1col3['text'] == ""):
        row1col3['fg'] = 'red' if (currPlayer.get() == varPlayer1.get()) else 'blue'
        row1col3['text'] = 'X' if (currPlayer.get() == varPlayer1.get()) else 'O'
        return True 
    elif (boardNum == 4 and row2col1['text'] == ""):
        row2col1['fg'] = 'red' if (currPlayer.get() == varPlayer1.get()) else 'blue'
        row2col1['text'] = 'X' if (status["text"] == varPlayer1.get()) else 'O'
        return True 
    elif (boardNum == 5 and row2col2['text'] == ""):
        row2col2['fg'] = 'red' if (currPlayer.get() == varPlayer1.get()) else 'blue'
        row2col2['text'] = 'X' if (status["text"] == varPlayer1.get()) else 'O'
        return True 
    elif (boardNum == 6 and row2col3['text'] == ""):
        row2col3['fg'] = 'red' if (currPlayer.get() == varPlayer1.get()) else 'blue'
        row2col3['text'] = 'X' if (status["text"] == varPlayer1.get()) else 'O'
        return True 
    elif (boardNum == 7 and row3col1['text'] == ""):
        row3col1['fg'] = 'red' if (currPlayer.get() == varPlayer1.get()) else 'blue'
        row3col1['text'] = 'X' if (status["text"] == varPlayer1.get()) else 'O'
        return True 
    elif (boardNum == 8 and row3col2['text'] == ""):
        row3col2['fg'] = 'red' if (currPlayer.get() == varPlayer1.get()) else 'blue'
        row3col2['text'] = 'X' if (status["text"] == varPlayer1.get()) else 'O' 
        return True
    elif (boardNum == 9 and row3col3['text'] == ""):
        row3col3['fg'] = 'red' if (currPlayer.get() == varPlayer1.get()) else 'blue'
        row3col3['text'] = 'X' if (status["text"] == varPlayer1.get()) else 'O' 
        return True
    return False

def boardClick(btn_entry):
#   if tile change is successful (player is able to make his move):
#      update player's list of tiles
#       update current number of tiles on the board
#       find:
#           1)
#           if any tiles are a winner
#           show pop up for winner
#           clear the board
#           2)
#           if all tiles are filled and no winner
#           show pop up for no winner
#           clear the board 
#
#       always change player - win or draw
    if changeTile(btn_entry):
        currNumTiles.set(currNumTiles.get()+1)
        if (currPlayer.get() == varPlayer1.get()):
            player1Board.append(btn_entry)
            if (findWinningTri(player1Board)):
                popup_showinfo(varPlayer1.get())
        else:
            player2Board.append(btn_entry)
            if (findWinningTri(player2Board)):
                popup_showinfo(varPlayer2.get())
        if (currNumTiles.get() == 9):
            popup_showinfo()
        changePlayer(btn_entry)

def clear():
    print("Clear")
    currNumTiles.set(0)
    row1col1['text'] = ''
    row1col2['text'] = ''
    row1col3['text'] = ''
    row2col1['text'] = ''
    row2col2['text'] = ''
    row2col3['text'] = ''
    row3col1['text'] = ''
    row3col2['text'] = ''
    row3col3['text'] = ''
    player1Board.clear()
    player2Board.clear()


row1col1 = Button(frame, text="", fg="black", height=2, width=5, command=lambda: boardClick(1))
row1col2 = Button(frame, text="", fg="black", height=2, width=5, command=lambda: boardClick(2))
row1col3 = Button(frame, text="", fg="black", height=2, width=5, command=lambda: boardClick(3))

row1col1.grid(row=2, column=0)
row1col2.grid(row=2, column=1)
row1col3.grid(row=2, column=2)

row2col1 = Button(frame, text="", fg="red", height=2, width=5, command=lambda: boardClick(4))
row2col2 = Button(frame, text="", fg="red", height=2, width=5, command=lambda: boardClick(5))
row2col3 = Button(frame, text="", fg="red", height=2, width=5, command=lambda: boardClick(6))

row2col1.grid(row=3, column=0)
row2col2.grid(row=3, column=1)
row2col3.grid(row=3, column=2)

row3col1 = Button(frame, text="", fg="red", height=2, width=5, command=lambda: boardClick(7))
row3col2 = Button(frame, text="", fg="red", height=2, width=5, command=lambda: boardClick(8))
row3col3 = Button(frame, text="", fg="red", height=2, width=5, command=lambda: boardClick(9))

row3col1.grid(row=4, column=0)
row3col2.grid(row=4, column=1)
row3col3.grid(row=4, column=2)

empty = Label(frame, text="")
empty.grid(row=5,column=0,columnspan=3)

again_btn = Button(frame, text="New", fg="Black", height=1, width=5, command=lambda: clear())
again_btn.grid(row=6,column=1)

root.mainloop()