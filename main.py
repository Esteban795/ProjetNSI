from tournoi import Tournoi
from player import Player
from match import Match,Round
from player import Player
from tkinter import *
import json

def main(filename):
    def add_player():
        add_player_gui = Tk()
        lastname = Label(add_player_gui,text="Lastname : ")
        lastname.place(x=10,y=10)
        lastname_entry = Entry(add_player_gui)
        lastname_entry.place(x=100,y=10)

        firstname = Label(add_player_gui,text="Firstname : ")
        firstname.place(x=10,y=35)
        firstname_entry = Entry(add_player_gui)
        firstname_entry.place(x=100,y=35)

        date_naissance = Label(add_player_gui,text="Born on :")
        date_naissance.place(x=10,y=60)
        date_naissance_entry = Entry(add_player_gui)
        date_naissance_entry.place(x=100,y=60)


        add_player_gui.title("Add a player")
        add_player_gui.geometry("300x300")
        add_player_gui.mainloop()

    def retrieve_existing_players():
        """Retrieves already added players from the tournament"""
        liste = []
        for i in tournament.serialize()["liste_joueurs"]:
            s = f"{i['id']}. {i['nom_famille']} {i['prenom']}"
            liste.append(s)
        players.set(liste)

    gui = Tk()
    gui.geometry("800x600")
    gui.resizable(width=False,height=False)
    gui.title(" ".join(["Tournament Manager : ",filename]))
    with open(filename,"r") as fichier:
        tournament_json = json.load(fichier)
        nb_players = tournament_json["nb_joueurs"]
        name = tournament_json["nom"]
        location = tournament_json["lieu"]
        date = tournament_json["date"]
        nb_rounds = tournament_json["nb_tours"]
        player_list = tournament_json["liste_joueurs"]
        players_who_lost = tournament_json["liste_perdants"]
        rounds_list = tournament_json["liste_rounds"]
        tournament = Tournoi(nb_players,name,location,date,nb_rounds,player_list,rounds_list,players_who_lost)
        print(tournament.serialize())
    #####

    #Players frame
    players_frame = LabelFrame(gui,text="PLAYERS OPTIONS",width=395,height=295)
    players_frame.place(x=5,y=0)
    players = StringVar()
    retrieve_existing_players()
    players_list = Listbox(players_frame,listvariable=players,width=20,height=15)
    players_list.place(x=10,y=10)

    add_player_button = Button(players_frame,text="ADD A PLAYER",command=add_player)
    add_player_button.place(x=150,y=10)
    #######
    rank_frame = LabelFrame(gui,width=395,height=295,text="RANKING")
    rank_frame.place(x=405,y=0)
    gui.mainloop()
