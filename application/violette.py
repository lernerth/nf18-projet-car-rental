from utils import *

################# AJOUTER LOCATION #################

#### entretien ####

# 36252187900034

def ajouter_entretien():
    print("Une location doit être associée à un entretien :\n")
    valeurs = [
        input("\tSociété d'entretien (num SIRET) :"),
        input("\tAgent technique : ")
     ]
    insert("Entretien", ["societe", "agent_tech"], valeurs) # voir plus tard pour ajouter date etc.

    # on récupère l'id de cet entretien
    query = "SELECT id_entretien FROM Entretien ORDER BY id_entretien;"
    curseur.execute(query)
    raw = curseur.fetchone()
    next_raw = curseur.fetchone()
    while next_raw:
        raw = next_raw
        next_raw = curseur.fetchone()
    return raw # logiquement c'est le dernier entretien ajouté


### Facturations ###

def ajouter_facturation_professionnel(idClient):
    valeurs = [
        idClient,
        input("\tAgent Commercial : "),
        False
    ]
    insert("Facturation", ["clientProfessionnel", "agent_com", "etat_payement"], valeurs)



def ajouter_facturation_particulier(idClient):
    valeurs = [
        idClient,
        input("\tAgent Commercial : "),
        False
    ]
    insert("Facturation", ["clientParticulier", "agent_com", "etat_payement"], valeurs)


### Locations prof et particulier ###

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
    insert("LocationParticulier", ["id_contrat", "particulier"], valeurs)

### Location générale ###

def ajouter_location():

    typeClient = input("\tClient Professionnel (1) ou Particulier (2) : ")
    while typeClient != "1" and typeClient != "2":
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
    query = "SELECT idFacturation FROM Facturation ORDER BY idFacturation;"
    curseur.execute(query)
    raw = curseur.fetchone()
    next_raw = curseur.fetchone()
    while next_raw:
        raw = next_raw
        next_raw = curseur.fetchone()
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
    query = "SELECT id_contrat FROM Location ORDER BY id_contrat;"
    curseur.execute(query)
    raw = curseur.fetchone()
    next_raw = curseur.fetchone()
    while next_raw:
        raw = next_raw
        next_raw = curseur.fetchone()
    id_contrat = raw

    # on remplit ensuite la table LocationParticulier ou la table LocationProfessionnel c'est selon
    if typeClient == 1:
        ajouter_location_professionnel(id_contrat)
    else:
        ajouter_location_particulier(id_contrat, idClient)


############### ANNULER LOCATION ###############

def annuler_location():
    c_location = input("\t Contrat de la location à supprimer : ")
    query = "DELETE FROM Location WHERE id_contrat='%s';" %c_location
    curseur.execute(query)
    conn.commit()
    # pour que la cascade marche faut peut être rajouter une contrainte dans le code sql des tables LocatProf et locPart:
    # ALTER TABLE nom_table
    # ADD [CONSTRAINT fk_col_ref]
    # FOREIGN KEY (colonne)
    # REFERENCES table_ref(col_ref)
    # ON DELETE CASCADE;

############### MODIFIER LOCATION ###############

def modifier_location():
    afficher("\nVoici la liste des locations actuelles", select_all("location"))
    # pour l'instant seuls des attributs string peuvent être modifiés
    id_contrat = input("\tID Contrat de la location à modifier : ")
    nom_col = input("\tParamètre à modifier : ")
    nouvelle_valeur = input("\tNouvelle valeur : ")
    query = "UPDATE Location SET %s='%s' WHERE id_contrat='%s';" %(nom_col, nouvelle_valeur, id_contrat)
    curseur.execute(query)
    conn.commit()


############### PAYER FACTURATION ###############


def payer_facturation():
    # ce serait bien d'afficher le montant qui s'apprête à être réglé (plus tard)
    id_facturation = input("\t id de la facturation : ")
    moyen_payement = input("\t Moyen de payement : ")
    query = "UPDATE Facturation SET date_payement=current_date, moyen_reglement='%s', etat_payement=TRUE WHERE idFacturation='%s';" %(moyen_payement, id_facturation)
    curseur.execute(query)
    conn.commit()


########## VALIDATION FINALE PAR UN AGENT COM ##########

def validation_finale_location():
    valeurs = [
        input("\t Agent Comm : "),
        input("\t Contrat de la loc : "),
        "today",
        input("\tResultat de la validation (1:ok / 0:not ok)")
    ]
    insert("ValidationFinale", ["agent_com", "location", "date_validation", "resultat_validation"], valeurs) 


########## CONTROLE PAR UN AGENT TECH = MAJ DE ENTRETIEN ##########

def controler_apres_location():
    id_entretien = input("\tId de l'entretien : ")
    date_ent = input("\tDate_entretien : ")
    date_ctrl = input("\tDate_controle : ")
    resultat = input("\tResultat du controle : ")
    query = "UPDATE Entretien SET date_entretien='%s', date_controle='%s', resultat='%s' WHERE id_entretien='%s';" %(date_ent, date_ctrl, resultat, id_entretien)
    curseur.execute(query)
    conn.commit()

