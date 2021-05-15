try:
    import debug_config as cfg
except:
    import config as cfg
import pandas as pd
import psycopg2
from decimal import Decimal
import bang


"""
    Connecter à la base de données
"""
conn = psycopg2.connect(dbname=cfg.DBNAME, user=cfg.DBUSER,
                        password=cfg.DBPWD, host=cfg.DBHOST, port=cfg.DBPORT)
curseur = conn.cursor()

"""
    Afficher un menu
    Retourner une fonction qui réalise l'option choisie par utilisateur
"""


def menu(menu_items):
    for item in menu_items:
        print(item, ". ", menu_items[item][0], sep="", end="\n")
    return menu_items[input("> ")][-1]


"""
    Retrouver toutes les lignes d'un table
"""


def select_all(table):
    query = "SELECT * FROM %s" % table
    curseur.execute(query)
    return curseur.fetchall()


"""
    Insérer des données
"""


def insert(table, colonnes, valeurs):
    query = "INSERT INTO %s(%s) VALUES(%s);" % (
        table, ",".join(colonnes), ",".join(["%s"] * len(colonnes)))
    curseur.execute(query, valeurs)
    conn.commit()

def ajouter_agence():
    valeurs = [
        input("\tNom : "),
        input("\tAdresse : "),
        input("\tSIRET : "),
        input("\tMail : "),
        input("\tTéléphone : ")
    ]
    insert("Agence", ["nom", "adresse", "siret", "mail", "telephone"], valeurs)

def ajouter_vehicule():
    valeurs = [
        input("\tImmatriculation : "),
        input("\tModele : "),
        input("\tType carburant : "),
        input("\tCouleur : "),
        input("\tNb kilometres parcourus : "),
        input("\tID agence ? "),
        input("\tID d'agent technique : ")
    ]
    insert("Vehicule", ["immat", "modele", "carburant",
           "couleur", "nb_km", "agence", "agent_tech"], valeurs)


"""
    Afficher des tables
"""


def afficher_agences():
    for row in select_all("Agence"):
        print(row)


def afficher_vehicules():
    for row in select_all("Vehicule"):
        print(row)


"""
    Quitter programme
"""


def quitter():
    curseur.close()
    conn.close()
    exit(0)


# Définir listes des menus ici
# Forme: "x": ["y", z]
# Avec: x: numero de menu
#       y: texte
#       z: la fonction correspondante
menu_items = {
    "1": ["Afficher liste des agences", afficher_agences],
    "2": ["Afficher liste des véhicules", afficher_vehicules],
    "3": ["Ajouter une agence", ajouter_agence],
    "4": ["Ajouter une véhicule", ajouter_vehicule],
    "5": ["Bilan par categorie", lambda : bang.bilan_par_categorie(curseur)],
    "6": ["...", ...],
    "7": ["...", ...],
    "0": ["Quitter le programme", quitter]
}


def main():
    while True:
        action_choisie = menu(menu_items)
        action_choisie()


main()