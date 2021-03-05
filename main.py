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
    gui = Tk()
    gui.geometry("1000x700")
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
    #####

    #Players frame
    def remove_player():
        player = players_list.get("active")
        if len(tournament.liste_joueurs) > 0 and askokcancel("Validation","Are you sure you want te remove '{}' from the tournament ?".format(player[3:])):
            player_id = int(player[0])
            index = 0  
            for i in range(len(tournament.liste_joueurs)):
                if tournament.liste_joueurs[i]["id"] == player_id:
                    index = i
                    del tournament.liste_joueurs[index]
                    break
            for j in range(index,len(tournament.liste_joueurs),1):
                tournament.liste_joueurs[j]["id"] = j + 1
            retrieve_existing_players()
            update_nb_players()
    def remove_all_players():
        tournament.liste_joueurs = []
        retrieve_existing_players()
        update_nb_players()
    def nb_players():
        current_nb_players.set("Current number of players : {}".format(len(tournament.liste_joueurs) + len(tournament.liste_perdants)))
    def add_player():
        def add_this_player():
            player = Player(lastname_entry.get(),firstname_entry.get(),date_naissance_entry.get(),sexe_entry.get(),rank_entry.get(),identifier)
            tournament.ajouter_joueur(player.serialize())
            add_player_gui.destroy()
            retrieve_existing_players()
            update_nb_players()
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
    def update_nb_players():
        current_nb_players.set("All players of this tournament ({})".format(len(tournament.liste_joueurs)))
    def modify_infos():
        player_id = int(players_list.get("active")[0])
        for i in tournament.liste_joueurs:
            print(i)
            if i["id"] == player_id:
                infos_gui = Tk()
                
                infos_gui.title("Modifying '{} {}'".format(i["nom_famille"],i["prenom"]))
                infos_gui.geometry("350x150")
                infos_gui.mainloop()
                break

    players_frame = LabelFrame(gui,text="PLAYERS OPTIONS",width=600,height=300)
    players_frame.place(x=5,y=0)
    players = StringVar()
    retrieve_existing_players()
    current_nb_players = StringVar()
    update_nb_players()
    current_nb_players_label = Label(gui,textvariable=current_nb_players)
    current_nb_players_label.place(x=10,y=20)
    players_list = Listbox(players_frame,listvariable=players,width=25,height=15)
    players_list.place(x=10,y=30)

    
    add_player_button = Button(players_frame,text="ADD A PLAYER",command=add_player)
    add_player_button.place(x=220,y=10)

    remove_player_button = Button(players_frame,text="REMOVE SELECTED PLAYER",command=remove_player)
    remove_player_button.place(x=220,y=50)

    remove_all_player_button = Button(players_frame,text="REMOVE ALL PLAYERS",command=remove_all_players)
    remove_all_player_button.place(x=220,y=90)

    get_infos_button = Button(gui,text="MODIFY SELECTED PLAYER'S INFORMATIONS",command=modify_infos)
    get_infos_button.place(x=220,y=130)
    #######

    rank_frame = LabelFrame(gui,width=395,height=295,text="RANKING")
    rank_frame.place(x=605,y=0)
    

    icon = PhotoImage(file="img/wheels.png")
    gui.iconphoto(False,icon)
    gui.protocol("WM_DELETE_WINDOW", on_closing)
    gui.mainloop()


main("Tournoi_du_Mans.json")