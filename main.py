from tournoi import Tournoi
from match import Match,Round
from player import Player
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter import ttk
import json

import os
def main(filename):
    def on_closing():
        if askokcancel("Quit","Are you sure you want to quit ?"):
            rewrite_json(filename)
            gui.destroy()

    def rewrite_json(path):
        with open(path,"w") as fichier:
            json.dump(tournament.serialize(),fichier,indent=4)
    
    def load():
        f = askopenfile(filetypes=[("json files",".json")],initialdir=os.getcwd())
        if f != "":
            path = "{0.name}".format(f)
            gui.destroy()
            main(path)
    gui = Tk()
    gui.geometry("1000x700")
    frame = Frame(gui)
    frame.pack()
    
    mainmenu = Menu(frame)
    mainmenu.add_command(label = "Save", command=lambda:rewrite_json(filename))  
    mainmenu.add_command(label = "Load", command=load)
    mainmenu.add_command(label = "Exit", command=gui.destroy)
 
    gui.config(menu = mainmenu)

    gui.resizable(width=False,height=False)
    gui.title(" ".join(["Tournament Manager : ",filename]))
    with open(filename,"r") as fichier:
        tournament_json = json.load(fichier)
        tournament = Tournoi(tournament_json["nb_players"],tournament_json["name"],tournament_json["location"],tournament_json["date"],tournament_json["number_of_rounds"],tournament_json["players_list"],tournament_json["list_of_rounds"],tournament_json["players_who_lost"],tournament_json["players_still_in_the_tournament"])
    #####

    #Players frame
    def remove_player():
        player = players_list.get("active")
        if len(tournament.players_list) > 0 and askokcancel("Validation","Are you sure you want te remove '{}' from the tournament ?".format(player[3:])):
            player_id = int(player[0])
            index = 0  
            for i in range(len(tournament.players_list)):
                if tournament.players_list[i]["id"] == player_id:
                    index = i
                    del tournament.players_list[index]
                    break
            for j in range(index,len(tournament.players_list),1):
                tournament.players_list[j]["id"] = j + 1
            retrieve_existing_players()
            update_nb_players()
            change_order()
    def remove_all_players():
        if askokcancel("Validation","Are you sure you want to remove all players from this tournament ?"):
            tournament.players_list = []
            retrieve_existing_players()
            update_nb_players()
            change_order()
    def add_player():
        def add_this_player():
            player = Player(lastname_entry.get(),firstname_entry.get(),date_naissance_entry.get(),sexe_entry.get(),int(rank_entry.get()),identifier)
            tournament.ajouter_joueur(player.serialize())
            add_player_gui.destroy()
            retrieve_existing_players()
            update_nb_players()
            change_order()
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

        identifier = len(tournament.players_list) + 1

        add = Button(add_player_gui,text="ADD THIS PLAYER",command=add_this_player)
        add.place(x=100,y=160)
        
        add_player_gui.title("Add a player")
        add_player_gui.geometry("300x200")
        add_player_gui.mainloop()
    def retrieve_existing_players():
        """Retrieves already added players from the tournament"""
        liste = []
        for i in tournament.serialize()["players_list"]:
            s = f"{i['id']}. {i['lastname']} {i['firstname']}"
            liste.append(s)
        players.set(liste)
    def update_nb_players():
        current_nb_players.set("All players of this tournament ({})".format(len(tournament.players_list)))
    def modify_infos():
        player_id = int(players_list.get("active")[0])
        for i in tournament.players_list:
            if i["id"] == player_id:
                def modify_this_player():
                    i["lastname"] = lastname.get()
                    i["firstname"] = firstname.get()
                    i["date"] = date_naissance.get()
                    i["sexe"] = sexe.get()
                    i["rank"] = int(rank.get())
                    modify_gui.destroy()
                    change_order()

                modify_gui = Tk()
                lastname = StringVar(modify_gui,value=i["lastname"])
                firstname = StringVar(modify_gui,value=i["firstname"])
                date_naissance = StringVar(modify_gui,value=i["date"])
                sexe = StringVar(modify_gui,value=i['sexe'])
                rank = StringVar(modify_gui,value=i["rank"])

                lastname_label = Label(modify_gui,text="Lastname : ")
                lastname_label.place(x=10,y=10)
                lastname_entry = Entry(modify_gui,textvariable=lastname)
                lastname_entry.place(x=100,y=10)

                firstname_label = Label(modify_gui,text="Firstname : ")
                firstname_label.place(x=10,y=35)
                firstname_entry = Entry(modify_gui,textvariable=firstname)
                firstname_entry.place(x=100,y=35)

                date_naissance_label = Label(modify_gui,text="Born on :")
                date_naissance_label.place(x=10,y=60)
                date_naissance_entry = Entry(modify_gui,textvariable=date_naissance)
                date_naissance_entry.place(x=100,y=60)

                sexe_label = Label(modify_gui,text="Gender : ")
                sexe_label.place(x=10,y=85)
                sexe_entry = Entry(modify_gui,textvariable=sexe)
                sexe_entry.place(x=100,y=85)

                rank_label = Label(modify_gui,text="Rank : ")
                rank_label.place(x=10,y=110)
                rank_entry = Entry(modify_gui,textvariable=rank)
                rank_entry.place(x=100,y=110)

                modify = Button(modify_gui,text="MODIFY THE INFORMATION PLAYER",command=modify_this_player)
                modify.place(x=75,y=160)
                modify_gui.title("Modifying '{} {}'".format(i["lastname"],i["firstname"]))
                modify_gui.geometry("350x200")
                modify_gui.mainloop()
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

    
    add_player_button = Button(players_frame,text="ADD A PLAYER",command=add_player,width=35,bg="white",fg="black",activebackground="white",activeforeground="black")
    add_player_button.place(x=220,y=50)

    remove_player_button = Button(players_frame,text="REMOVE SELECTED PLAYER",command=remove_player,width=35,bg="white",fg="black",activebackground="white",activeforeground="black")
    remove_player_button.place(x=220,y=80)

    modify_infos_button = Button(gui,text="MODIFY SELECTED PLAYER'S INFORMATIONS",command=modify_infos,width=35,bg="white",fg="black",activebackground="white",activeforeground="black")
    modify_infos_button.place(x=225,y=125)

    remove_all_player_button = Button(players_frame,text="REMOVE ALL PLAYERS",command=remove_all_players,width=35,bg="white",fg="black",activebackground="white",activeforeground="black")
    remove_all_player_button.place(x=215,y=190)


    #######


    #Rank frame
    rank_list = StringVar()
    def change_order(*args):
        sort_method = order_by_menu_value.get()
        if sort_method == "ASCENDING":
            lst = sorted([i for i in tournament.players_list],key=lambda j:j["rank"])
        else:
            lst = sorted([i for i in tournament.players_list],key=lambda j:j["rank"],reverse=True)
        rank_list.set(["{}. {} {}".format(i["rank"],i["lastname"],i['firstname']) for i in lst])

    rank_frame = LabelFrame(gui,width=395,height=200,text="RANKING")
    rank_frame.place(x=605,y=0)
    
    order_by = ["ASCENDING","DESCENDING"]
    order_by_menu_value = StringVar()
    order_by_menu_value.trace('w',change_order)
    order_by_menu = ttk.Combobox(rank_frame,values=order_by,width=15,state="readonly",textvariable=order_by_menu_value)
    order_by_menu.set("PICK AN OPTION")
    order_by_menu.place(x=10,y=10)

    
    rank_list.set(["{}. {} {}".format(i["rank"],i["lastname"],i['firstname']) for i in tournament.players_list])
    rank_listbox = Listbox(rank_frame,listvariable=rank_list,width=30,height=10)
    rank_listbox.place(x=150,y=10)
    ######################

    gui.protocol("WM_DELETE_WINDOW", on_closing)
    gui.mainloop()

x = "Tournoi_du_Mans.json"
#main(x)