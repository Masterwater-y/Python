import tkinter as tk
import tkinter.messagebox
window=tk.Tk()
wtitle=tk.StringVar()
window.title('井字棋')
window.geometry('400x400')

def check(x,y,pos):
    flag=True
    for i in range(2):
        if val[x][i]!=val[x][i+1]:
            flag=False
    if flag:
        return(val[x][y])
    flag=True
    for i in range(2):
        if val[i][y]!=val[i+1][y]:
            flag=False
    if flag:
        return(val[x][y])
    if pos in {0,2,6,8}:
        if pos in {0,8}:
            if val[0][0]==val[1][1]==val[2][2]:
                return(val[x][y])
        if pos in {2,6}:
            if val[0][2]==val[1][1]==val[2][0]:
                return(val[x][y])
    turnn.set('现在轮到'+turn+'下棋')

def clean():
    for i in range(3):
        for j in range(3):
            val[i][j]=0
    global turn
    turn='X'
    for i in range(9):
        sym[i].set('')
    turnn.set('现在轮到'+turn+'下棋')
def press(pos):
    x=pos//3
    y=pos-x*3
    global turn
    if (val[x][y]!='X') and (val[x][y]!='O'):
        val[x][y]=turn
        sym[pos].set(turn)
        if turn=='X':
            turn='O'
        else:
            turn='X'
        turnn.set('现在轮到'+turn+'下棋')
    flag=check(x,y,pos)    
    if (flag=='X') or (flag=='O'):
        if tkinter.messagebox.askokcancel(flag+'选手胜利',flag+'选手胜利,再来一局吗'):
            clean()
chess=[]
sym=[]
val=[[0 for i in range(4)]for j in range(4)]
turn='X'
turnn=tk.StringVar()
turnn.set('现在轮到'+turn+'下棋')
showturn=tk.Label(window, textvariable=turnn,width=30, font=('Arial', 12),height=5, bg='black',fg='white')
showturn.place(x=0,y=200,anchor='nw')
for i in range(9):
    sym.append(tk.StringVar())

chess.append(tk.Button(window, textvariable=sym[0], width=3, height=1, command=lambda:press(0)))
chess.append(tk.Button(window, textvariable=sym[1], width=3, height=1, command=lambda:press(1)))
chess.append(tk.Button(window, textvariable=sym[2], width=3, height=1, command=lambda:press(2)))
chess.append(tk.Button(window, textvariable=sym[3], width=3, height=1, command=lambda:press(3)))
chess.append(tk.Button(window, textvariable=sym[4], width=3, height=1, command=lambda:press(4)))
chess.append(tk.Button(window, textvariable=sym[5], width=3, height=1, command=lambda:press(5)))
chess.append(tk.Button(window, textvariable=sym[6], width=3, height=1, command=lambda:press(6)))
chess.append(tk.Button(window, textvariable=sym[7], width=3, height=1, command=lambda:press(7)))
chess.append(tk.Button(window, textvariable=sym[8], width=3, height=1, command=lambda:press(8)))
for i in range(3):
    for j in range(3):
        chess[3*i+j].grid(row=i,column=j,padx=10,pady=10)

window.mainloop()

