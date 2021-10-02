from tkinter import *
import tkinter as tk
import random
from PIL import Image, ImageTk
import sys
sys.setrecursionlimit(5000)
taille = 24
demitaille=12
PATH="Assets/"

def mine(event):
    global continu
    global window
    global photo0
    global photo1
    global photo2
    global photo3
    global xscroll
    global yscroll
   
    x=int((event.x+xscroll.get()[0]*500*taille)//taille)
    y=int((event.y+yscroll.get()[0]*500*taille)//taille)
    #print(x,y)
    
    global minetab
    if (continu):
        minecase(x,y)
    #print(minetab[x+100*y])

def showgridbomb():
    global casemine
    global minetab
    global can
    global photobomb

    for x in range(0,500):
        for y in range(0,500):
            if(minetab[x+500*y]==1):
                if(casemine[x+500*y]==0):
                    can.create_image(demitaille+taille*x,demitaille+taille*y, image=photobomb)

def minecase(x,y):
    global window
    global photo0
    global photo1
    global photo2
    global photo3
    global casemine
    if(casemine[x+500*y]==0):
        casemine[x+500*y]=1 #la case à été exploré 
        if (minetab[x+500*y]==1):
            fenetreToplevel=Toplevel(window)
            text=Label(fenetreToplevel, text="Perdu")
            global continu
            continu=0
            nom="save.txt"
            fichier = open(nom, "w")
            fichier.close()    
            text.pack()
            can.create_image(demitaille+taille*x,demitaille+taille*y, image=photobombexplose)
            showgridbomb()
        else:
            adj=nbadjacent(x,y)
            if(adj==0):
                can.create_image(demitaille+taille*x,demitaille+taille*y, image=photo0)
                for i in range(x-1,x+2):
                    if(i>=0 and i<=499):
                        for j in range(y-1,y+2):
                            if(j>=0 and j<=499):
                                if(casemine[i+500*j]==0):
                                    minecase(i,j)
            if(adj==1):
                can.create_image(demitaille+taille*x,demitaille+taille*y, image=photo1)
            elif(adj==2):
                can.create_image(demitaille+taille*x,demitaille+taille*y, image=photo2)
            elif(adj==3):
                can.create_image(demitaille+taille*x,demitaille+taille*y, image=photo3)
            elif(adj==4):
                can.create_image(demitaille+taille*x,demitaille+taille*y, image=photo4)
            elif(adj==5):
                can.create_image(demitaille+taille*x,demitaille+taille*y, image=photo5)
            elif(adj==6):
                can.create_image(demitaille+taille*x,demitaille+taille*y, image=photo6)
            elif(adj==7):
                can.create_image(demitaille+taille*x,demitaille+taille*y, image=photo7)
            elif(adj==8):
                can.create_image(demitaille+taille*x,demitaille+taille*y, image=photo8)
    
def loadcase(x,y):
    global window
    global casemine
    global nbbomb
    if(casemine[x+500*y]==1):
            adj=nbadjacent(x,y)
            if(adj==0):
                can.create_image(demitaille+taille*x,demitaille+taille*y, image=photo0)
            if(adj==1):
                can.create_image(demitaille+taille*x,demitaille+taille*y, image=photo1)
            elif(adj==2):
                can.create_image(demitaille+taille*x,demitaille+taille*y, image=photo2)
            elif(adj==3):
                can.create_image(demitaille+taille*x,demitaille+taille*y, image=photo3)
            elif(adj==4):
                can.create_image(demitaille+taille*x,demitaille+taille*y, image=photo4)
            elif(adj==5):
                can.create_image(demitaille+taille*x,demitaille+taille*y, image=photo5)
            elif(adj==6):
                can.create_image(demitaille+taille*x,demitaille+taille*y, image=photo6)
            elif(adj==7):
                can.create_image(demitaille+taille*x,demitaille+taille*y, image=photo7)
            elif(adj==8):
                can.create_image(demitaille+taille*x,demitaille+taille*y, image=photo8)
    elif(casemine[x+500*y]==9):
        can.create_image(demitaille+taille*x,demitaille+taille*y, image=photoflag,tags=str(x+500*y)+"a")
        nbbomb=nbbomb-1
    

def nbadjacent(i,j):
    global minetab
    nb=0
    if(i>0):
        if(j>0): 
            if minetab[(i-1)+500*(j-1)]:
                nb=nb+1
        if minetab[(i-1)+500*(j)]:
            nb=nb+1
        if(j<499):
            if minetab[(i-1)+500*(j+1)]:
                nb=nb+1
    if(j>0):
        if(minetab[(i)+500*(j-1)]):
            nb=nb+1
    if(j<499):
        if(minetab[(i)+500*(j+1)]):
            nb=nb+1

    if(i<499):
        if(j>0):
            if(minetab[(i+1)+500*(j-1)]):
                nb=nb+1
        if(minetab[(i+1)+500*(j)]):
            nb=nb+1
        if(j<499):
            if(minetab[(i+1)+500*(j+1)]):
                nb=nb+1
    return nb
            
def demine(event):
    global can
    global photo
    global xscroll
    global yscroll
    global casemine
    
    if continu==1:
        global nbbomb

        x=int((event.x+xscroll.get()[0]*500*taille)//taille)
        y=int((event.y+yscroll.get()[0]*500*taille)//taille)
        if(casemine[x+500*y]==0):
            nbbomb=nbbomb-1
            can.create_image(taille//2+taille*x,taille//2+taille*y, image=photoflag,tags=str(x+500*y)+"a")
            casemine[x+500*y]=9
        elif(casemine[x+500*y]==9):
            nbbomb=nbbomb+1
            casemine[x+500*y]=0
            can.delete(str(x+500*y)+"a")
            print("clear")

        label['text']=str(nbbomb)

def option():
    global window
    global PourcentageMine
    
    
    fenetreToplevel=Toplevel(window)
    texte2=Label(fenetreToplevel, text="Pourcentage de mine")
    w = Scale ( fenetreToplevel,variable=PourcentageMine,orient=HORIZONTAL,from_=10,to_=50 )
    btn=Button(fenetreToplevel,command=create_grid,text="set")
    w.pack()
    texte2.pack()
    btn.pack()

def new():
    global can
    global continu
    continu=1
    can.delete("all")
    print("a")
    create_grid()

def create_grid():
    global PourcentageMine
    global minetab
    global casemine
    global can
    global label
    global nbbomb
    nbbomb=500*5*PourcentageMine.get()
    label['text']=str(nbbomb)

    minetab=[]
    casemine=([0]*500)*500
    #print(casemine)
    for i in range(0,500*PourcentageMine.get()*5):
        minetab.append(1)
        
    for i in range(PourcentageMine.get()*5*500,500*500):
        minetab.append(0)
    random.shuffle(minetab)
    #print(minetab)
    for i in range(0,500):
        can.create_line(taille*i,0,taille*i,taille*500)
        can.create_line(0,taille*i,taille*500,taille*i)

def Save():
    
    if continu==1:
        nom="save.txt"
        fichier = open(nom, "w")
        for x in range(0,500):
            for y in range(0,500):
                fichier.write(str(casemine[x+500*y]))
                fichier.write(str(minetab[x+500*y]))
        fichier.close()    
        print("saved")
     
def Load():
    global continu
    global casemine
    global minetab

    new()
    nom="save.txt"
    fichier = open(nom, "r")
    continu=1
    contenu=fichier.read()
    for x in range(0,500):
            for y in range(0,500):
                #print(contenu[x+50*y])
                try:
                    casemine[x+500*y]=(int(contenu[1000*x+2*y]))
                    minetab[x+500*y]=int(contenu[1000*x+2*y+1])
                except:
                    print(contenu[1000*x+2*y])

    for x in range(0,500):
        for y in range(0,500):
            #print(casemine[x+500*y])
            if(casemine[x+500*y]==1 or casemine[x+500*y]==9 ):
                loadcase(x,y)
    
    print("loaded")
    
    

window=Tk()
window.title("Démineur")
window.geometry('800x800')
menu_widget = Menu(window)
window.config(menu=menu_widget)
submenu_widget = Menu(menu_widget, tearoff=False)
submenu_widget.add_command(label="Option",
                           command=option)
submenu_widget.add_command(label="New",
                           command=new)
submenu_widget.add_command(label="Save",
                           command=Save)
submenu_widget.add_command(label="Load",
                           command=Load)

menu_widget.add_cascade(label="Menu", menu=submenu_widget)
minetab=[]
casemine=[]
continu=1
PourcentageMine=IntVar()
PourcentageMine.set(10)

can=Canvas(window,width=750,height=750,scrollregion =(0, 0, taille*500, taille*500),bg='grey')
xscroll=Scrollbar(window, orient=HORIZONTAL)
yscroll=Scrollbar(window, orient=VERTICAL)
xscroll.grid(row=2, column=0, sticky=E+W)
yscroll.grid(row=1, column=1,  sticky=S+N)

xscroll["command"]=can.xview
yscroll["command"]=can.yview
can['xscrollcommand']=xscroll.set
can['yscrollcommand']=yscroll.set

imageflag = Image.open(PATH+"flag.PNG") 
photoflag = ImageTk.PhotoImage(imageflag)
image0 = Image.open(PATH+"0.PNG") 
photo0 = ImageTk.PhotoImage(image0) 
image1 = Image.open(PATH+"1.PNG") 
photo1 = ImageTk.PhotoImage(image1)
image2 = Image.open(PATH+"2.PNG") 
photo2 = ImageTk.PhotoImage(image2)
image3 = Image.open(PATH+"3.PNG") 
photo3 = ImageTk.PhotoImage(image3)
image4 = Image.open(PATH+"4.PNG") 
photo4 = ImageTk.PhotoImage(image4)
image5 = Image.open(PATH+"5.PNG") 
photo5 = ImageTk.PhotoImage(image5)
image6 = Image.open(PATH+"6.PNG") 
photo6 = ImageTk.PhotoImage(image6)
image7 = Image.open(PATH+"7.PNG") 
photo7 = ImageTk.PhotoImage(image7)
image8 = Image.open(PATH+"8.PNG") 
photo8 = ImageTk.PhotoImage(image8)
imagebomb = Image.open(PATH+"bomb.PNG") 
photobomb = ImageTk.PhotoImage(imagebomb)
imagebombexplose = Image.open(PATH+"bombexplose.PNG") 
photobombexplose = ImageTk.PhotoImage(imagebombexplose)

textlabel=""
nbbomb=0
label=Label(window,text=textlabel)

can.bind("<Button-1>", mine)
can.bind("<Button-3>", demine)

               
label.grid(row=0,column=0)
can.grid(row=1,column=0)
window.mainloop()
