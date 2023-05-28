import numpy as np
from tkinter import *
from tkinter import messagebox
from socket import * 
from threading import Thread 

player = 0 

def create_board():
    board = np.zeros((6 , 7))
    return board

def clicked1():
        global player
        if(btn1["bg"]=="yellow"):
            if(player==1):
                player=0
                btn1["bg"] = "blue"
                sendPlay(1)	
                board[0][0]=2
                print(board)
                check(board)

def clicked2():
        global player
        if(btn2["bg"]=="yellow"):
                if(player==1):
                        player=0
                        btn2["bg"] = "blue"
                        sendPlay(2)	
                        board[0][1]=2
                        print(board)
                        check(board)
            
def clicked3():
        global player
        if(btn3["bg"]=="yellow"):
                if(player==1):
                        player=0
                        btn3["bg"] = "blue"
                        sendPlay(3)	
                        board[0][2]=2
                        print(board)
                        check(board)
            
def clicked4():
        global player
        if(btn4["bg"]=="yellow"):
                if(player==1):
                        player=0
                        btn4["bg"] = "blue"
                        sendPlay(4)	
                        board[0][3]=2
                        print(board)
                        check(board)
            
def clicked5():
        global player
        if(btn5["bg"]=="yellow"):
                if(player==1):
                        player=0
                        btn5["bg"] = "blue"
                        sendPlay(5)	
                        board[0][4]=22
                        print(board)
                        check(board)
            
def clicked6():
        global player
        if(btn6["bg"]=="yellow"):
                if(player==1):
                        player=0
                        btn6["bg"] = "blue"
                        sendPlay(6)	    
                        board[0][5]=2
                        print(board)
                        check(board)
            
def clicked7():
        global player
        if(btn7["bg"]=="yellow"):
                if(player==1):
                        player=0
                        btn7["bg"] = "blue"
                        sendPlay(7)	
                        board[0][6]=2
                        print(board)
                        check(board)
            
def clicked8():
        global player
        if(btn8["bg"]=="yellow"):
                if(player==1):
                        player=0
                        btn8["bg"] = "blue"
                        sendPlay(8)
                        board[1][0]=2
                        print(board)
                        check(board)
            
def clicked9():
        global player
        if(btn9["bg"]=="yellow"):
                if(player==1):
                        player=0
                        btn9["bg"] = "blue"
                        sendPlay(9)	
                        board[1][1]=2
                        print(board)
                        check(board)  
            
def clicked10():
        global player
        if(btn10["bg"]=="yellow"):
                if(player==1):
                        player=0
                        btn10["bg"] = "blue"
                        sendPlay(10)	
                        board[1][2]=2
                        print(board)
                        check(board)                
        
def clicked11():
        global player
        if(btn11["bg"]=="yellow"):
                if(player==1):
                        player=0
                        btn11["bg"] = "blue"
                        sendPlay(11)	
                        board[1][3]=2
                        print(board)
                        check(board)
        
def clicked12():
        global player
        if(btn12["bg"]=="yellow"):
                if(player==1):
                        player=0
                        btn12["bg"] = "blue"
                        sendPlay(12)	
                        board[1][4]=2
                        print(board)
                        check(board)
                
def clicked13():
        global player
        if(btn13["bg"]=="yellow"):
                if(player==1):
                        player=0
                        btn13["bg"] = "blue"
                        sendPlay(13)	
                        board[1][5]=2
                        print(board)
                        check(board)
                        
def clicked14():
        global player
        if(btn14["bg"]=="yellow"):
                if(player==1):
                        player=0
                        btn14["bg"] = "blue"
                        sendPlay(14)	
                        board[1][6]=2
                        print(board)
                        check(board)
                        
def clicked15():
        global player
        if(btn15["bg"]=="yellow"):
                if(player==1):
                        player=0
                        btn15["bg"] = "blue"
                        sendPlay(15)	
                        board[2][0]=2
                        print(board)
                        check(board)
                                
def clicked16():
        global player
        if(btn16["bg"]=="yellow"):
                if(player==1):
                        player=0
                        btn16["bg"] = "blue"
                        sendPlay(16)	
                        board[2][1]=2
                        print(board)
                        check(board)
                                
def clicked17():
        global player
        if(btn17["bg"]=="yellow"):
                if(player==1):
                        player=0
                        btn17["bg"] = "blue"
                        sendPlay(17)	
                        board[2][2]=2
                        print(board)
                        check(board)
                                
def clicked18():
        global player
        if(btn18["bg"]=="yellow"):
                if(player==1):
                        player=0
                        btn18["bg"] = "blue"
                        sendPlay(18)	
                        board[2][3]=2
                        print(board)
                        check(board)
                                
def clicked19():
        global player
        if(btn19["bg"]=="yellow"):
                if(player==1):
                        player=0
                        btn19["bg"] = "blue"
                        sendPlay(19)	
                        board[2][4]=2
                        print(board)
                        check(board)
                                
def clicked20():
        global player
        if(btn20["bg"]=="yellow"):
                if(player==1):
                        player=0
                        btn20["bg"] = "blue"
                        sendPlay(20)	
                        board[2][5]=2
                        print(board)
                        check(board)
                                
def clicked21():
        global player
        if(btn21["bg"]=="yellow"):
                if(player==1):
                        player=0
                        btn21["bg"] = "blue"
                        sendPlay(21)	
                        board[2][6]=2
                        print(board)
                        check(board)
                                
def clicked22():
        global player
        if(btn22["bg"]=="yellow"):
                if(player==1):
                        player=0
                        btn22["bg"] = "blue"
                        sendPlay(22)	
                        board[3][0]=2
                        print(board)
                        check(board)  
                
def clicked23():
        global player
        if(btn23["bg"]=="yellow"):
                if(player==1):
                        player=0
                        btn23["bg"] = "blue"
                        sendPlay(23)	
                        board[3][1]=2
                        print(board)
                        check(board)
                
def clicked24():
        global player
        if(btn24["bg"]=="yellow"):
                if(player==1):
                        player=0
                        btn24["bg"] = "blue"
                        sendPlay(24)	
                        board[3][2]=2
                        print(board)
                        check(board)  
                
def clicked25():
        global player
        if(btn25["bg"]=="yellow"):
                if(player==1):
                        player=0
                        btn25["bg"] = "blue"
                        sendPlay(25)	
                        board[3][3]=2
                        print(board)
                        check(board) 
                
def clicked26():
        global player
        if(btn26["bg"]=="yellow"):
                if(player==1):
                        player=0
                        btn26["bg"] = "blue"
                        sendPlay(26)	
                        board[3][4]=2
                        print(board)
                        check(board)
                
def clicked27():
        global player
        if(btn27["bg"]=="yellow"):
                if(player==1):
                        player=0
                        btn27["bg"] = "blue"
                        sendPlay(27)	
                        board[3][5]=2
                        print(board)
                        check(board) 
                
def clicked28():
        global player
        if(btn28["bg"]=="yellow"):
                if(player==1):
                        player=0
                        btn28["bg"] = "blue"
                        sendPlay(28)	
                        board[3][6]=2
                        print(board)
                        check(board)
                    
def clicked29():
        global player
        if(btn29["bg"]=="yellow"):
                if(player==1):
                        player=0
                        btn29["bg"] = "blue"
                        sendPlay(29)	
                        board[4][0]=2
                        print(board)
                        check(board)
                        
def clicked30():
        global player
        if(btn30["bg"]=="yellow"):
                if(player==1):
                        player=0
                        btn30["bg"] = "blue"
                        sendPlay(30)	
                        board[4][1]=2
                        print(board)
                        check(board)
                        
def clicked31():
        global player
        if(btn31["bg"]=="yellow"):
                if(player==1):
                        player=0
                        btn31["bg"] = "blue"
                        sendPlay(31)	
                        board[4][2]=2
                        print(board)
                        check(board)
                        
def clicked32():
        global player
        if(btn32["bg"]=="yellow"):
                if(player==1):
                        player=0
                        btn32["bg"] = "blue"
                        sendPlay(32)	
                        board[4][3]=2
                        print(board)
                        check(board)
                        
def clicked33():
        global player
        if(btn33["bg"]=="yellow"):
                if(player==1):
                        player=0
                        btn33["bg"] = "blue"
                        sendPlay(33)	
                        board[4][4]=2
                        print(board)
                        check(board)
                        
def clicked34():
        global player
        if(btn34["bg"]=="yellow"):
                if(player==1):
                        player=0
                        btn34["bg"] = "blue"
                        sendPlay(34)	
                        board[4][5]=2
                        print(board)
                        check(board)
                        
def clicked35():
        global player
        if(btn35["bg"]=="yellow"):
                if(player==1):
                        player=0
                        btn35["bg"] = "blue"
                        sendPlay(35)	
                        board[4][6]=2
                        print(board)
                        check(board)
                        
def clicked36():
        global player
        if(btn36["bg"]=="yellow"):
                if(player==1):
                        player=0
                        btn36["bg"] = "blue"
                        sendPlay(36)	
                        board[5][0]=2
                        print(board)
                        check(board)
                                
def clicked37():
        global player
        if(btn37["bg"]=="yellow"):
                if(player==1):
                        player=0
                        btn37["bg"] = "blue"
                        sendPlay(37)	
                        board[5][1]=2
                        print(board)
                        check(board)
                                
def clicked38():
        global player
        if(btn38["bg"]=="yellow"):
                if(player==1):
                        player=0
                        btn38["bg"] = "blue"
                        sendPlay(38)	
                        board[5][2]=2
                        print(board)
                        check(board)
                                    
def clicked39():
        global player
        if(btn39["bg"]=="yellow"):
                if(player==1):
                        player=0
                        btn39["bg"] = "blue"
                        sendPlay(39)	
                        board[5][3]=2
                        print(board)
                        check(board)
                            
def clicked40():
        global player
        if(btn40["bg"]=="yellow"):
                if(player==1):
                        player=0
                        btn40["bg"] = "blue"
                        sendPlay(40)	
                        board[5][4]=2
                        print(board)
                        check(board)
                        
def clicked41():
        global player
        if(btn41["bg"]=="yellow"):
                if(player==1):
                        player=0
                        btn41["bg"] = "blue"
                        sendPlay(41)	
                        board[5][5]=2
                        print(board)
                        check(board)
                        
def clicked42():
        global player
        if(btn42["bg"]=="yellow"):
                if(player==1):
                        player=0
                        btn42["bg"] = "blue"
                        sendPlay(42)	
                        board[5][6]=2
                        print(board)
                        check(board)

def check(board):
    # Check horizontal locations for win
    for c in range(4):
        for r in range(6):
            if (board[r][c] == 1 and board[r][c+1] == 1 and board[r][c+2] == 1 and board[r][c+3] == 1)or(board[r][c] == 2 and board[r][c+1] == 2 and board[r][c+2] == 2 and board[r][c+3] == 2):
                if(board[r][c] == 1):
                    win("red player")
                else:
                    win("blue player")
                return

    # Check vertical locations for win
    for c in range(7):
        for r in range(3):
            if(board[r][c] == 1 and board[r+1][c] == 1 and board[r+2][c] == 1 and board[r+3][c] == 1)or(board[r][c] == 2 and board[r+1][c] == 2 and board[r+2][c] == 2 and board[r+3][c] == 2):
                if(board[r][c] == 1):
                    win("red player")
                else:
                    win("blue player")
                return 
            
def win(player):
    messagebox.showinfo("winner", player +" is win")
    wind.destroy()

def sendPlay(n):
    n = str(n)
    n = n.encode()
    soc.send(n)
    
def rec(c):
    while True:
      p = c.recv(10)
      applayPlay(p)

def applayPlay(p):
    p = p.decode()
    p = int(p)
    handlePlay(p)
      
def handlePlay(n):
    global player
    player = 1 
    butList[n]["bg"] = "red"
    board[n]=1

board = create_board()
butList = list()

wind = Tk()
wind.title("4 In Row Game Server")
wind.configure(background='black')
wind.geometry("580x460+500+100") 

lb1 = Label(wind,text="player1" ,font=('Helvetiica',15),bg='black',fg='white')
lb1.grid(row = 0)

btn1=Button(wind,text=" ",bg="yellow",fg="black",width=6,height=3,font='Helvetiica',command=clicked1)
btn1.grid(row=1,column=1)
btn2=Button(wind,text=" ",bg="yellow",fg="black",width=6,height=3,font='Helvetiica',command=clicked2)
btn2.grid(row=1,column=2)
btn3=Button(wind,text=" ",bg="yellow",fg="black",width=6,height=3,font='Helvetiica',command=clicked3)
btn3.grid(row=1,column=3)
btn4=Button(wind,text=" ",bg="yellow",fg="black",width=6,height=3,font='Helvetiica',command=clicked4)
btn4.grid(row=1,column=4)
btn5=Button(wind,text=" ",bg="yellow",fg="black",width=6,height=3,font='Helvetiica',command=clicked5)
btn5.grid(row=1,column=5)
btn6=Button(wind,text=" ",bg="yellow",fg="black",width=6,height=3,font='Helvetiica',command=clicked6)
btn6.grid(row=1,column=6)
btn7=Button(wind,text=" ",bg="yellow",fg="black",width=6,height=3,font='Helvetiica',command=clicked7)
btn7.grid(row=1,column=7)

btn8=Button(wind,text=" ",bg="yellow",fg="black",width=6,height=3,font='Helvetiica',command=clicked8)
btn8.grid(row=2,column=1)
btn9=Button(wind,text=" ",bg="yellow",fg="black",width=6,height=3,font='Helvetiica',command=clicked9)
btn9.grid(row=2,column=2)
btn10=Button(wind,text=" ",bg="yellow",fg="black",width=6,height=3,font='Helvetiica',command=clicked10)
btn10.grid(row=2,column=3)
btn11=Button(wind,text=" ",bg="yellow",fg="black",width=6,height=3,font='Helvetiica',command=clicked11)
btn11.grid(row=2,column=4)
btn12=Button(wind,text=" ",bg="yellow",fg="black",width=6,height=3,font='Helvetiica',command=clicked12)
btn12.grid(row=2,column=5)
btn13=Button(wind,text=" ",bg="yellow",fg="black",width=6,height=3,font='Helvetiica',command=clicked13)
btn13.grid(row=2,column=6)
btn14=Button(wind,text=" ",bg="yellow",fg="black",width=6,height=3,font='Helvetiica',command=clicked14)
btn14.grid(row=2,column=7)

btn15=Button(wind,text=" ",bg="yellow",fg="black",width=6,height=3,font='Helvetiica',command=clicked15)
btn15.grid(row=3,column=1)
btn16=Button(wind,text=" ",bg="yellow",fg="black",width=6,height=3,font='Helvetiica',command=clicked16)
btn16.grid(row=3,column=2)
btn17=Button(wind,text=" ",bg="yellow",fg="black",width=6,height=3,font='Helvetiica',command=clicked17)
btn17.grid(row=3,column=3)
btn18=Button(wind,text=" ",bg="yellow",fg="black",width=6,height=3,font='Helvetiica',command=clicked18)
btn18.grid(row=3,column=4)
btn19=Button(wind,text=" ",bg="yellow",fg="black",width=6,height=3,font='Helvetiica',command=clicked19)
btn19.grid(row=3,column=5)
btn20=Button(wind,text=" ",bg="yellow",fg="black",width=6,height=3,font='Helvetiica',command=clicked20)
btn20.grid(row=3,column=6)
btn21=Button(wind,text=" ",bg="yellow",fg="black",width=6,height=3,font='Helvetiica',command=clicked21)
btn21.grid(row=3,column=7)

btn22=Button(wind,text=" ",bg="yellow",fg="black",width=6,height=3,font='Helvetiica',command=clicked22)
btn22.grid(row=4,column=1)
btn23=Button(wind,text=" ",bg="yellow",fg="black",width=6,height=3,font='Helvetiica',command=clicked23)
btn23.grid(row=4,column=2)
btn24=Button(wind,text=" ",bg="yellow",fg="black",width=6,height=3,font='Helvetiica',command=clicked24)
btn24.grid(row=4,column=3)
btn25=Button(wind,text=" ",bg="yellow",fg="black",width=6,height=3,font='Helvetiica',command=clicked25)
btn25.grid(row=4,column=4)
btn26=Button(wind,text=" ",bg="yellow",fg="black",width=6,height=3,font='Helvetiica',command=clicked26)
btn26.grid(row=4,column=5)
btn27=Button(wind,text=" ",bg="yellow",fg="black",width=6,height=3,font='Helvetiica',command=clicked27)
btn27.grid(row=4,column=6)
btn28=Button(wind,text=" ",bg="yellow",fg="black",width=6,height=3,font='Helvetiica',command=clicked28)
btn28.grid(row=4,column=7)

btn29=Button(wind,text=" ",bg="yellow",fg="black",width=6,height=3,font='Helvetiica',command=clicked29)
btn29.grid(row=5,column=1)
btn30=Button(wind,text=" ",bg="yellow",fg="black",width=6,height=3,font='Helvetiica',command=clicked30)
btn30.grid(row=5,column=2)
btn31=Button(wind,text=" ",bg="yellow",fg="black",width=6,height=3,font='Helvetiica',command=clicked31)
btn31.grid(row=5,column=3)
btn32=Button(wind,text=" ",bg="yellow",fg="black",width=6,height=3,font='Helvetiica',command=clicked32)
btn32.grid(row=5,column=4)
btn33=Button(wind,text=" ",bg="yellow",fg="black",width=6,height=3,font='Helvetiica',command=clicked33)
btn33.grid(row=5,column=5)
btn34=Button(wind,text=" ",bg="yellow",fg="black",width=6,height=3,font='Helvetiica',command=clicked34)
btn34.grid(row=5,column=6)
btn35=Button(wind,text=" ",bg="yellow",fg="black",width=6,height=3,font='Helvetiica',command=clicked35)
btn35.grid(row=5,column=7)

btn36=Button(wind,text=" ",bg="yellow",fg="black",width=6,height=3,font='Helvetiica',command=clicked36)
btn36.grid(row=6,column=1)
btn37=Button(wind,text=" ",bg="yellow",fg="black",width=6,height=3,font='Helvetiica',command=clicked37)
btn37.grid(row=6,column=2)
btn38=Button(wind,text=" ",bg="yellow",fg="black",width=6,height=3,font='Helvetiica',command=clicked38)
btn38.grid(row=6,column=3)
btn39=Button(wind,text=" ",bg="yellow",fg="black",width=6,height=3,font='Helvetiica',command=clicked39)
btn39.grid(row=6,column=4)
btn40=Button(wind,text=" ",bg="yellow",fg="black",width=6,height=3,font='Helvetiica',command=clicked40)
btn40.grid(row=6,column=5)
btn41=Button(wind,text=" ",bg="yellow",fg="black",width=6,height=3,font='Helvetiica',command=clicked41)
btn41.grid(row=6,column=6)
btn42=Button(wind,text=" ",bg="yellow",fg="black",width=6,height=3,font='Helvetiica',command=clicked42)
btn42.grid(row=6,column=7)

butList.append(btn1) 
butList.append(btn2)
butList.append(btn3)
butList.append(btn4)
butList.append(btn5)
butList.append(btn6)
butList.append(btn7)
butList.append(btn8)
butList.append(btn9)
butList.append(btn10)
butList.append(btn11)
butList.append(btn12)
butList.append(btn13)
butList.append(btn14)
butList.append(btn15)
butList.append(btn16)
butList.append(btn17)
butList.append(btn18)
butList.append(btn19)
butList.append(btn20)
butList.append(btn21)
butList.append(btn22)
butList.append(btn23)
butList.append(btn24)
butList.append(btn25)
butList.append(btn26)
butList.append(btn27)
butList.append(btn28)
butList.append(btn29)
butList.append(btn30)
butList.append(btn31)
butList.append(btn32)
butList.append(btn33)
butList.append(btn34)
butList.append(btn35)
butList.append(btn36)
butList.append(btn37)
butList.append(btn38)
butList.append(btn39)
butList.append(btn40)
butList.append(btn41)
butList.append(btn42)

soc = socket(AF_INET , SOCK_STREAM)
soc.connect(("127.0.0.1" , 6002) )

t = Thread(target = rec )
t.start()

wind.mainloop()



    