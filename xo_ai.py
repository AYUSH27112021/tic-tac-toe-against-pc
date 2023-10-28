import random
import sys
import os
list=[1,1,1,1,1,1,1,1,1]
winning_combos = [  
                    [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                    [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6], 
                 ]

def pos_o():
    for i in range(0,8):

        if((list[winning_combos[i][0]]*list[winning_combos[i][1]])==25 and list[winning_combos[i][2]]==1):
            return (winning_combos[i][2])
        elif((list[winning_combos[i][1]]*list[winning_combos[i][2]])==25 and list[winning_combos[i][0]]==1):
            return (winning_combos[i][0])
        elif((list[winning_combos[i][0]]*list[winning_combos[i][2]])==25 and list[winning_combos[i][1]]==1):
            return (winning_combos[i][1])
    return 0 

def pos_x():
    for i in range(0,8):
        if((list[winning_combos[i][0]]*list[winning_combos[i][1]])==9 and list[winning_combos[i][2]]==1):
            return (winning_combos[i][2])
        elif((list[winning_combos[i][1]]*list[winning_combos[i][2]])==9 and list[winning_combos[i][0]]==1):
            return (winning_combos[i][0])
        elif((list[winning_combos[i][0]]*list[winning_combos[i][2]])==9 and list[winning_combos[i][1]]==1):
            return (winning_combos[i][1])
    return 0 

def go(n,symbol):
    if(symbol=='x'):
        list[n]=3
    elif(symbol=='o'):
        list[n]=5
    else:
        print("wrong choice exitting")
    printboard()

def mov_2():
    xlist=[]
    for i in range(0,9):
        if(list[i]==1):
            xlist.append(i)
    return random.choice(xlist)


def printboard():
    def plist(n):
        if(list[n]==1):
            return ' '
        elif(list[n]==3):
            return 'x'
        elif(list[n]==5):
            return 'o'
    print("------------------------------------")
    print(plist(0)+"|"+plist(1)+"|"+plist(2))
    print("=-=-=-")
    print(plist(3)+"|"+plist(4)+"|"+plist(5))
    print("=-=-=-")
    print(plist(6)+"|"+plist(7)+"|"+plist(8))

def ai(choice):
    def get_move():
        mov=int(input("enter the position to mark ->"))
        go(mov,choice)
    if(choice=='o'):
        #move 1
        go(0,'x')    
        #move 2
        get_move()
        #move 3
        if(list[8]==1):
            go(8,'x')
        else:
            go(mov_2(),'x')
        #move 4
        get_move()
        #move 5
        if(pos_x()!=0):
            go(pos_x(),'x')
            print("pc wins")
            sys.exit()
        elif(pos_o()!=0):
            go(pos_o(),'x')
        elif(list[6]==1):
            go(6,'x')
        else:
            go(2,'x')
        #move 6
        get_move()
        #move 7
        if(pos_x()!=0):
            go(pos_x(),'x')
            print("x wins")
            sys.exit()
        elif(pos_o()!=0):
            go(pos_o(),'x')
        else:
            go(mov_2(),'x')
        #move 8
        get_move()
        #move 9
        if(pos_x()!=0):
            go(pos_x(),'x')
            print("x wins")
            sys.exit()
        elif(pos_o()!=0):
            go(pos_o(),'x')
        else:
            go(mov_2(),'x')
        print("it's a draw!!better luck next time")

print("-------------tic-tac-toe--------------------\n")
while(True):
    print("------------------menu---------------------")
    print("palying aginst computer")
    print("press 1 to start \n press 2 to exit")
    type=int(input("enter your choice ->"))
    os.system('cls')
    if(type==1):
        for i in range(len(list)):
            list[i]=1         
        ai('o')
    else:
        sys.exit()

