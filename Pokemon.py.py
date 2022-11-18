from tkinter import *
import random
from PIL import ImageTk, Image
root= Tk()
root.title("endless pokeon game")
root.geometry("600x400")
root.configure(background= "lime")
Squirtle= ImageTk.PhotoImage(Image.open("squirtle.jpg"))

player1=0
player2=0

player1_label= Label(root,text= "player1", bg="royal blue", fg= "white")
player1_label.place(relx=0.1, rely=0.3, anchor=CENTER)

player2_label= Label(root,text= "player2", bg="royal blue", fg= "white")
player2_label.place(relx=0.9, rely=0.3, anchor=CENTER)


player1_score= Label(root, bg="royal blue", fg= "white")
player1_score.place(relx=0.1, rely=0.4, anchor=CENTER)

player2_score= Label(root, bg="royal blue", fg= "white")
player2_score.place(relx=0.9, rely=0.4, anchor=CENTER)

random_label= Label(root, bg="chocolate1", fg= "white")
random_label.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()