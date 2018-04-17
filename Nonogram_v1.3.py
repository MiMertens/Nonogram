import turtle
import random
import time
from itertools import groupby

#controleer of de oplossing behaald is
def Check_board(speelv, invoer):
    counter(Check_board)
    # is het speelveld gelijk aan de oplossing
    if speelv == invoer:
        end = time.time()
        hours, rem = divmod(end-start, 3600)
        minutes, seconds = divmod(rem, 60)   
        print("klaar")
        print("Het aantal zetten dat u hebt gebruikt: " + str(Check_board.count))
        print("De gebruikte tijd: {:02}:{:05.2f}".format(int(minutes),seconds))

#counter +1 voor het aantal zetten
def counter(func):
     func.count += 1

#converteer xy scherm cordinaat naar 2d list cordinaat
def fill_list(xcord,ycord,invoer):
        if xcord == -3 and ycord == 2:
            x = 0
            y = 0
        elif xcord == -3 and ycord == 1:
            x = 1
            y = 0
        elif xcord == -3 and ycord == 0:
            x = 2
            y = 0
        elif xcord == -3 and ycord == -1:
            x = 3
            y = 0
        elif xcord == -3 and ycord == -2:
            x = 4
            y = 0
        elif xcord == -3 and ycord == -3:
            x = 5
            y = 0
        elif xcord == -2 and ycord == 2:
            x = 0
            y = 1
        elif xcord == -2 and ycord == 1:
            x = 1
            y = 1
        elif xcord == -2 and ycord == 0:
            x = 2
            y = 1
        elif xcord == -2 and ycord == -1:
            x = 3
            y = 1
        elif xcord == -2 and ycord == -2:
            x = 4
            y = 1
        elif xcord == -2 and ycord == -3:
            x = 5
            y = 1
        elif xcord == -1 and ycord == 2:
            x = 0
            y = 2
        elif xcord == -1 and ycord == 1:
            x = 1
            y = 2
        elif xcord == -1 and ycord == 0:
            x = 2
            y = 2
        elif xcord == -1 and ycord == -1:
            x = 3
            y = 2
        elif xcord == -1 and ycord == -2:
            x = 4
            y = 2
        elif xcord == -1 and ycord == -3:
            x = 5
            y = 2          
        elif xcord == 0 and ycord == 2:
            x = 0
            y = 3
        elif xcord == 0 and ycord == 1:
            x = 1
            y = 3
        elif xcord == 0 and ycord == 0:
            x = 2
            y = 3
        elif xcord == 0 and ycord == -1:
            x = 3
            y = 3
        elif xcord == 0 and ycord == -2:
            x = 4
            y = 3
        elif xcord == 0 and ycord == -3:
            x = 5
            y = 3
        elif xcord == 1 and ycord == 2:
            x = 0
            y = 4
        elif xcord == 1 and ycord == 1:
            x = 1
            y = 4
        elif xcord == 1 and ycord == 0:
            x = 2
            y = 4
        elif xcord == 1 and ycord == -1:
            x = 3
            y = 4
        elif xcord == 1 and ycord == -2:
            x = 4
            y = 4
        elif xcord == 1 and ycord == -3:
            x = 5
            y = 4
        elif xcord == 2 and ycord == 2:
            x = 0
            y = 5
        elif xcord == 2 and ycord == 1:
            x = 1
            y = 5
        elif xcord == 2 and ycord == 0:
            x = 2
            y = 5
        elif xcord == 2 and ycord == -1:
            x = 3
            y = 5
        elif xcord == 2 and ycord == -2:
            x = 4
            y = 5
        elif xcord == 2 and ycord == -3:
            x = 5
            y = 5
        #geef de kleur zwart mee en pas de 2d list aan
        if invoer[x][y] == 0:
            invoer[x][y] = 1
            color = 'black'
        #geef de kleur wit mee pas de 2d list aan
        else:
            invoer[x][y] = 0
            color = 'white' 
        #cordinaar * 50 zodat het te tekenen blok start vanuit de linker onderhoek  
        x = xcord * 50
        y = ycord * 50
        fillbox(x,y,color)

#roteer de 2d list 90"
def rotate_clockwise(speelv):
    rotated90 = list(zip(*speelv[::1]))
    x = -130
    count = 0
    for i in range(6):
        y = 190
        for key, group in groupby(rotated90[count]):
            if key == 1:
                t = (list(group))
                text = str(sum(t))
                tess.penup()
                tess.goto(x,y)
                tess.pendown()
                tess.write(text, font=("Arial", 15, "normal"))            
                y -= 20
        x += 50
        count += 1

def Write_nr(speelv):
    y = 115
    count = 0
    for i in range(6):
        x = -220
        #maak een list van ieder opeenvolgend hetzelfdezelfde nummer
        for key, group in groupby(speelv[count]):
            if key == 1:
                t = (list(group))
                text = str(sum(t))
                tess.penup()
                tess.goto(x,y)
                tess.pendown()
                tess.write(text, font=("Arial", 15, "normal"))            
                x += 20
        y -= 50
        count += 1
    rotate_clockwise(speelv)

#vul de lijst speelv met random 0 en 1
def Create_list(speelv):
    # maak het aantal kolomen uit de range
    for j in range(6):
            column = []
            # maak voor iedere kolom het aantal rijen
            for i in range(6):
                #random nummer 0-1 en voeg het toe aan de lijst
                randomnr = random.randint(0,1)
                column.append(randomnr)
            #voeg de kolom toe aan het speelveld
            speelv.append(column)
    print(speelv)
    Write_nr(speelv)

#teken een box en kleur deze in
def fillbox(x,y,color):
    tess.penup() 
    tess.goto(x,y) 
    tess.pendown() 
    tess.fillcolor(color)
    tess.begin_fill()
    #viekand heeft vier zijdes
    for i in range(4):
        tess.forward(50) # move forward
        tess.left(90) # turn pen left 90 degrees
    tess.end_fill()
    Check_board(speelv,invoer)

#controleer of er binnen het speelveld word geclickt
def handler_goto(x, y):
    #cordinaar floor 50 om in de linker onderhoek van het blok te starten
    xcord = x // 50 
    ycord = y // 50
    # controleer of er binnen het speelveld word geclicked
    if 150 > x > -150 and 150 > y > -150:
        fill_list(xcord, ycord, invoer)
    else:
        print("dat is helaas niet mogelijk")

# Teken de boxes
def draw_box(x,y,size):
    tess.penup()
    tess.goto(x,y) 
    tess.pendown() 

    for i in range(4):
        tess.forward(size)
        tess.right(90)  

# bereken posities voor de boxes
def calculate_board():
    start_x = -150 
    start_y = -100 
    box_size = 50
    for i in range(6):
        for j in range(6):           
            draw_box(start_x+j*box_size,start_y+i*box_size,box_size)
    Create_list(speelv)

#list speelveld dat later random wordt gevuld
speelv = []

#2d list voor de invoer van de gebruiker
invoer = [[0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0]]

#zet de counter op 0 voor het aantal zetten
Check_board.count = 0

#start de timer
start = time.time()

#setup voor het form
turtle.setup(450,450)
wn = turtle.Screen()

# initialiseer de turlte 
tess = turtle.Turtle()
tess.speed(0)
tess.pensize(3)
tess.ht()

calculate_board()
wn.onclick(handler_goto)        
wn.listen()
turtle.mainloop()
