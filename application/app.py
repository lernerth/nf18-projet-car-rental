from utils import *
from decimal import Decimal
import bang
import thomas
import violette
import noe


"""
    Afficher un menu
    Retourner une fonction qui réalise l'option choisie par utilisateur
"""


def menu(menu_items):
    for item in menu_items:
        print("\t", item, ". ", menu_items[item][0], sep="", end="\n")
    choix = input("> ")
    if choix in menu_items:
        return menu_items[choix][-1]
    else:
        return None



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
    "1": ["Afficher liste des véhicules", bang.afficher_vehicules],
    "2": ["Ajouter un véhicule", bang.ajouter_vehicule],
    "3": ["Ajouter une location", violette.ajouter_location],
    "4": ["Annuler une location", violette.annuler_location],
    "5": ["Modifier une location", violette.modifier_location],
    "6": ["Payer une facturation", violette.payer_facturation],
    "7": ["Valider une location", violette.validation_finale_location],
    "8": ["Controler un entretien", violette.controler_apres_location],
    "9": ["Bilan par client", thomas.bilan_client],
    "10": ["Bilan par vehicule", noe.bilan_vehicule],
    "11": ["Bilan par categorie", bang.bilan_par_categorie],
    "12": ["Trace des agents", bang.trace_agent],
    "0": ["Quitter le programme", quitter]
}

## ajouter une fonction pour ajouter un client

def main():
    while True:
        print("\nSélectionnez une option :")
        action_choisie = menu(menu_items)
        if action_choisie is not None:
            action_choisie()


main()