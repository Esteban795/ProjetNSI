from tkinter import *
from tkinter.messagebox import *
from tournoi import Tournoi
from tinydb import TinyDB
import json
import os,glob

DEV_MODE = True

def display_db():
    dbs.set([i for i in glob.glob("*.json")])

def select_db():
    filename = existing_dbs.get("active")
    if filename == "":
        showerror("Error","No tournament selected.")

def delete_db():
    filename = existing_dbs.get("active")
    if filename == "":
        showerror("Error","No tournament selected.")
    elif askokcancel("Delete a tournament","Are you sure you want to delete this tournament ?"):
        os.remove(filename)
        display_db()

def tournament_creation(nb,n,l,d,nb_t):
    liste = [nb,n,l,d,nb_t]
    if "" in liste or nb is str or nb_t is str:
        showerror("Error","Make sure to fill every field ! Also pay attention to the informations you set for each field : number of players must be a number, as well as number of rounds")
    else:
        tournament_object = Tournoi(int(nb),n,l,d,int(nb_t))
        tournament_file_name = "_".join(tournament_object.nom.split(" ")) + ".json"
        if tournament_file_name not in glob.glob("*.json"):
            with open(tournament_file_name,"w") as file:
                json.dump(tournament_object.serialize(),file,indent=4)
            display_db()


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

create = Button(create_tournament,text="CREATE",command=lambda: tournament_creation(nb_players_entry.get(),tournament_name_entry.get(),location_entry.get(),date_entry.get(),nb_rounds_entry.get()))
create.place(x=235,y=175)
#### 



###Select tournament
select_tournament = LabelFrame(main_frame,text="OR SELECT AN ALREADY EXISTING TOURNAMENT",width=495,height=295)
select_tournament.place(x=505,y=0)
dbs = StringVar()
display_db()

existing_dbs = Listbox(select_tournament, width=30,height=15,listvariable=dbs)
existing_dbs.place(x=10,y=30)
scrollbar = Scrollbar(select_tournament,orient="vertical")
scrollbar.config(command=existing_dbs.yview)
scrollbar.place(x=200,y=50)
existing_dbs.config(yscrollcommand=scrollbar.set)

refresh_button = Button(select_tournament,text="REFRESH TOURNAMENT LIST",command=display_db,width=25)
refresh_button.place(x=300,y=15)

select_db_button = Button(select_tournament,text="SELECT THIS TOURNAMENT",command=select_db,width=25)
select_db_button.place(x=300,y=50)

delete_db_button = Button(select_tournament,text="REMOVE A TOURNAMENT",command=delete_db,width=25)
delete_db_button.place(x=300,y=85)
################################



launcher.geometry("1005x400")
launcher.title("Tournament Manager")
launcher.resizable(width=False,height=False)
launcher.mainloop()