from tournoi import Tournoi
from match import Match,Round
from player import Player
from tkinter import *
from tkinter.messagebox import *
import json

def main(filename):
    def on_closing():
        if askokcancel("Quit","Are you sure you want to quit ?"):
            rewrite_json(filename)
            gui.destroy()

    def remove_player():
        player = players_list.get("active")
        if askokcancel("Validation","Are you sure you want te remove {} from the tournament ?".format(player[3:])):
            print(player[0])
        
        

    def add_player():
        def add_this_player():
            player = Player(lastname_entry.get(),firstname_entry.get(),date_naissance_entry.get(),sexe_entry.get(),rank_entry.get(),identifier)
            tournament.ajouter_joueur(player.serialize())
            add_player_gui.destroy()
            retrieve_existing_players()

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

        sexe = Label(add_player_gui,text="Gender : ")
        sexe.place(x=10,y=85)
        sexe_entry = Entry(add_player_gui)
        sexe_entry.place(x=100,y=85)

        rank = Label(add_player_gui,text="Rank : ")
        rank.place(x=10,y=110)
        rank_entry = Entry(add_player_gui)
        rank_entry.place(x=100,y=110)

        identifier = len(tournament.liste_joueurs) + 1

        add = Button(add_player_gui,text="ADD THIS PLAYER",command=add_this_player)
        add.place(x=100,y=160)
        
        add_player_gui.title("Add a player")
        add_player_gui.geometry("300x200")
        add_player_gui.mainloop()

    def retrieve_existing_players():
        """Retrieves already added players from the tournament"""
        liste = []
        for i in tournament.serialize()["liste_joueurs"]:
            s = f"{i['id']}. {i['nom_famille']} {i['prenom']}"
            liste.append(s)
        players.set(liste)

    def rewrite_json(path):
        with open(path,"w") as fichier:
            json.dump(tournament.serialize(),fichier,indent=4)
    
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
    players_list = Listbox(players_frame,listvariable=players,width=25,height=15)
    players_list.place(x=10,y=10)

    add_player_button = Button(players_frame,text="ADD A PLAYER",command=add_player)
    add_player_button.place(x=200,y=10)

    remove_player_button = Button(players_frame,text="REMOVE SELECTED PLAYER",command=remove_player)
    remove_player_button.place(x=200,y=50)
    #######
    rank_frame = LabelFrame(gui,width=395,height=295,text="RANKING")
    rank_frame.place(x=405,y=0)

    gui.protocol("WM_DELETE_WINDOW", on_closing)
    gui.mainloop()


#main("Tournoi_du_Mans.json")