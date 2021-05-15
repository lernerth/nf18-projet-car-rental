from utils import *
from decimal import Decimal
import bang
import thomas
import violette



"""
    Afficher un menu
    Retourner une fonction qui réalise l'option choisie par utilisateur
"""


def menu(menu_items):
    for item in menu_items:
        print(item, ". ", menu_items[item][0], sep="", end="\n")
    return menu_items[input("> ")][-1]




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





"""
    Quitter programme
"""


def quitter():
    curseur.close()
    conn.close()
    exit(0)

def ajouter_location_professionnel(id_contrat):
    valeurs = [
        id_contrat,
        input("\tConducteur (num permis) : ")
    ]
    insert("LocationProfessionnel", ["id_contrat", "conducteur"], valeurs)
# Définir listes des menus ici
# Forme: "x": ["y", z]
# Avec: x: numero de menu
#       y: texte
#       z: la fonction correspondante
menu_items = {
    "1": ["Afficher liste des véhicules", afficher_vehicules],
    "2": ["Ajouter une véhicule", ajouter_vehicule],
    "3": ["Ajouter une location", lambda : violette.ajouter_location(curseur)],
    "4": ["Annuler une location", lambda : violette.annuler_location(curseur)],
    "5": ["Modifier une location", lambda : violette.modifier_location(curseur)],
    "6": ["Payer une facturation", lambda : violette.payer_facturation(curseur)],
    "7": ["Valider une location", violette.validation_finale_location],
    "8": ["Controler un entretien", lambda : violette.controler_apres_location(curseur)],
    "9": ["Bilan par client", lambda : thomas.bilan_client(curseur)],
    # "10": ["Bilan par vehicule", lambda : Noe.(curseur)],
    "11": ["Bilan par categorie", lambda : bang.bilan_par_categorie(curseur)],
    "0": ["Quitter le programme", quitter]
}


def main():
    while True:
        action_choisie = menu(menu_items)
        action_choisie()


main()