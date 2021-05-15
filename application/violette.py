from utils import *

################# AJOUTER LOCATION #################

#### entretien ####

def ajouter_entretien(curseur):
    print("Une location doit être associée à un entretien :\n")
    valeurs = [
        input("\tSociété d'entretien :"),
        input("\tAgent technique : ")
     ]
    insert("Entretien", ["societe", "agent_tech"], valeurs) # voir plus tard pour ajouter date etc.

    # on récupère l'id de cet entretien
    query = "SELECT id_entretien FROM Entretien;"
    curseur.execute(query)
    raw = cur.fetchone()
    next_raw = cur.fetchone()
    while next_raw:
        raw = next_raw
        next_raw = cur.fetchone()
    return raw # logiquement c'est le dernier entretien ajouté


''' Facturations '''

def ajouter_facturation_professionnel(idClient):
    valeurs = [
        idClient,
        input("\tAgent Commercial : "),
        0
    ]
    insert("Facturation", ["clientProfessionnel", "agent_com", "etat_payement"], val_fact)

def ajouter_facturation_professionnel(idClient):
    valeurs = [
        idClient,
        input("\tAgent Commercial : "),
        0
    ]
    insert("Facturation", ["clientParticulier", "agent_com", "etat_payement"], val_fact)


''' Locations prof et particulier '''

def ajouter_location_professionnel(id_contrat):
    valeurs = [
        id_contrat,
        input("\tConducteur (num permis) : ")
    ]
    insert("LocationProfessionnel", ["id_contrat", "conducteur"], valeurs)

def ajouter_location_particulier(id_contrat, idClient):
    valeurs = [
        id_contrat,
        idClient
    ]

''' Location générale '''

def ajouter_location():

    typeClient = input("\tClient Professionnel (1) ou Particulier (2) : ")
    while typeClient != 1 and typeClient != 2:
        typeClient = input("\tTapez 1 ou 2 pour indiquer le type du client : ")

    idClient = input("\tIdentifiant du client : ")

    # on récupère l'immatriculation du véhicule:
    immat = str(input("\tImmatriculation du véhicule :"))

    # on récupère son nombre de kilomètres:
    query = "SELECT nb_km FROM Vehicule WHERE immat='%s';" %immat
    curseur.execute(query)
    nb_km = curseur.fetchone()

    # on associe la location à un entretien
    id_entretien = ajouter_entretien()

    # on crée une facturation
    if typeClient == 1:
        ajouter_facturation_professionnel(idClient)
    else:
        ajouter_facturation_particulier(idClient)

    # on récupère l'id de la facturation qui vient d'être crée
    query = "SELECT idFacturation FROM Facturation;"
    curseur.execute(query)
    raw = cur.fetchone()
    next_raw = cur.fetchone()
    while next_raw:
        raw = next_raw
        next_raw = cur.fetchone()
    id_facturation = raw

    valeurs = [
        input("\tDate debut : "),
        input("\tDate fin : "),
        nb_km,
        immat,
        id_entretien,
        id_facturation
    ]
    insert("Location", ["date_debut", "date_fin", "km_parcourus", "vehicule_immat", "entretien", "facturation"], valeurs)

    # on récupère l'id contrat de la location qui vient d'être créée
    query = "SELECT id_contrat FROM Location;"
    curseur.execute(query)
    raw = cur.fetchone()
    next_raw = cur.fetchone()
    while next_raw:
        raw = next_raw
        next_raw = cur.fetchone()
    id_contrat = raw

    # on remplit ensuite la table LocationParticulier ou la table LocationProfessionnel c'est selon
    if typeClient == 1:
        ajouter_location_professionnel(id_contrat)
    else:
        ajouter_location_particulier(id_contrat, idClient)


############### ANNULER LOCATION ###############

def annuler_location():
    c_location = input("\t Contrat de la location à supprimer : ")
    query = "DELETE CASCADE FROM Location WHERE id_contrat='%s';" %c_location
    curseur.execute(query)
    # pour que la cascade marche faut peut être rajouter une contrainte dans le code sql des tables LocatProf et locPart:
    # ALTER TABLE nom_table
    # ADD [CONSTRAINT fk_col_ref]
    # FOREIGN KEY (colonne)
    # REFERENCES table_ref(col_ref)
    # ON DELETE CASCADE;

############### MODIFIER LOCATION ###############

def modifier_location():
    # pour l'instant seuls des attributs string peuvent être modifiés
    c_location = str(input("\tContrat de la location à modifier : "))
    nom_col = str(input("\tParamètre à modifier : "))
    nouvelle_valeur = input("\tNouvelle valeur : ")
    query = "UPDATE Location SET %s='%s' WHERE id_contrat='%s';" %(nom_col, nouvelle_valeur, id_contrat)
    curseur.execute(query)


############### PAYER FACTURATION ###############

from datetime import date

today = date.today()

def payer_facturation():
    # ce serait bien d'afficher le montant qui s'apprête à être réglé (plus tard)
    id_facturation = input("\t id de la facturation : ")
    moyen_payement = input("\t Moyen de payement : ")
    query = "UPDATE Facturation SET date_payement=today, moyen_reglement=%s, etat_payement=1 WHERE idFacturation=%d;" %(moyen_payement, id_facturation)
    curseur.execute(query)


############### PAYER FACTURATION ###############

def validation_finale_location():
    ...



"""
Agent Technique
def controler_apres_location()
"""