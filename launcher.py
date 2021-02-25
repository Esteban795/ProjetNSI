from tkinter import *
from tkinter.simpledialog import *
from tkinter.messagebox import *
from tournoi import Tournoi
import os 

def tournament(nb,n,l,d,nb_t):
    x = Tournoi(nb,n,l,d,nb_t)
    print(x.serialize())

launcher = Tk()

title = Label(launcher,text="Tournament Manager",font=("Times New Roman", 35, "bold"))
title.pack()

main_frame = Frame(launcher,width=1000,height=500)
main_frame.place(x=0,y=100)

create_tournament = LabelFrame(main_frame,text="CREATE A TOURNAMENT HERE",width=495,height=295)
create_tournament.place(x=5,y=0)

### Create tournament fields
tournament_name = Label(create_tournament,text="Tournament name :",padx=10)
tournament_name.place(x=0,y=25)
tournament_name_entry = Entry(create_tournament)
tournament_name_entry.place(x=200,y=25)

nb_players = Label(create_tournament,text="Number of players : ",padx=10)
nb_players.place(x=0,y=50)
nb_players_entry = Entry(create_tournament)
nb_players_entry.place(x=200,y=50)

location = Label(create_tournament,text="Location of the tournament : ",padx=10)
location.place(x=0,y=75)
location_entry = Entry(create_tournament)
location_entry.place(x=200,y=75)

date = Label(create_tournament,text="Date of the tournament : ",padx=10)
date.place(x=0,y=100)
date_entry = Entry(create_tournament)
date_entry.place(x=200,y=100)

nb_rounds = Label(create_tournament,text="How many rounds : ",padx=10)
nb_rounds.place(x=0,y=125)
nb_rounds_entry = Entry(create_tournament)
nb_rounds_entry.place(x=200,y=125)

create = Button(create_tournament,text="CREATE",command= lambda: tournament(nb_players_entry.get(),tournament_name_entry.get(),location_entry.get(),date_entry.get(),nb_rounds_entry.get()))
create.place(x=235,y=175)
#### 


select_tournament = LabelFrame(main_frame,text="OR SELECT AN ALREADY EXISTING TOURNAMENT",width=495,height=295)
select_tournament.place(x=505,y=0)

###" Select tournament"
launcher.geometry("1005x400")
launcher.title("Tournament Manager")
launcher.mainloop()