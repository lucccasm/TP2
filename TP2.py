"""
TP2 : Système de gestion de livres pour une bibliothèque

Groupe de laboratoire : XX
Numéro d'équipe :  YY
Noms et matricules : Nom1 (Matricule1), Nom2 (Matricule2)
"""

##########################################################################################################
# PARTIE 1 : Création du système de gestion et ajout de la collection actuelle
##########################################################################################################

# TODO : Écrire votre code ici
import csv
bibliotheque = {}

with open('collection_bibliotheque.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row[3] != "cote_rangement":
            bibliotheque[row[3]] = row[0], row[1], row[2]

print(f' \n Bibliotheque initiale : {bibliotheque} \n')


##########################################################################################################
# PARTIE 2 : Ajout d'une nouvelle collection à la bibliothèque
##########################################################################################################

with open('nouvelle_collection.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)

    for row in reader:
        cote_rangement = row[3]
        titre = row[0]
        auteur = row[1]
        if row[3] in bibliotheque:

            print(f' "Le livre  ---- {cote_rangement}  ---- {titre} par {auteur} est déjà présent dans la bibliothèque" ')
        elif cote_rangement != "cote_rangement" :
            bibliotheque[row[3]] = row[0], row[1], row[2]
            print(f' "Le livre  ----  {cote_rangement}  ---- {titre} par {auteur} a été ajouté avec succès"')


##########################################################################################################
# PARTIE 3 : Modification de la cote de rangement d'une sélection de livres
##########################################################################################################
key_ws = []

for key, value in bibliotheque.items():
    if value[1].__contains__("Shakespeare"):
        key_ws.append(key)


for key in key_ws:
    new_key = key.replace('S', 'WS')
    bibliotheque[new_key] = bibliotheque[key]
    bibliotheque.pop(key)

print(f' \n Bibliotheque avec modifications de cote : {bibliotheque} \n')




##########################################################################################################
# PARTIE 4 : Emprunts et retours de livres
##########################################################################################################
bibliotheque["emprunts"] = {}
bibliotheque["date_emprunt"] = {}
with (open('emprunts.csv', newline='') as csvfile):
    reader = csv.reader(csvfile)


    for row in reader:
            if row[0] in bibliotheque.keys():
                    bibliotheque["emprunts"][row[0]] = "emprunté"
                    bibliotheque["date_emprunt"][row[0]] = row[1]

            for key in bibliotheque.keys():
                    if key not in bibliotheque["emprunts"].keys():
                        if not key .__contains__ ("emprunt"):
                            bibliotheque["emprunts"][key] = "disponible"


print(f' \n Bibliotheque avec ajout des emprunts : {bibliotheque} \n')


##########################################################################################################
# PARTIE 5 : Livres en retard
##########################################################################################################
'''
import datetime
bibliotheque["frais_retard"]= {}
bibliotheque["livres_perdus"]= {}

date_actuelle = datetime.datetime.today().date
date_livre= datetime.strptime(bibliotheque["date_emprunt"])

difference = date_actuelle - date_livre

days_between = difference.days

if days_between >= 365:
    bibliotheque["livres_perdus"] = "livre perdu"
elif 50 <= days_between < 365:
    bibliotheque["frais_retard"] = "frais de retard de 100 $"
elif days_between < 50:
    bibliotheque["frais_retard"] = f"frais de retard de {days_between * 2} $"


print(f' \n Bibliotheque avec ajout des retards et frais : {bibliotheque} \n')


print(datetime.date.today())


import datetime

date_live= datetime.datetime.today().date()
date_object = datetime.datetime.strptime(date_live, "%Y-%m-%d").date()

'''