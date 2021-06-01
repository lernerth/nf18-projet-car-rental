from utils import *

################# AJOUTER LOCATION #################

#### entretien ####

def ajouter_entretien():
    print("Une location doit être associée à un entretien :\n")
    valeurs = [
        choisir_societe(),
        choisir_agent("technique"),
     ]
    insert("Entretien", ["societe", "agent_tech"], valeurs) # voir plus tard pour ajouter date etc.

    # on renvoie l'id de cet entretien (logiquement, c'est le dernier ajout dans la table entretien)
    return recupDernierAjout("id_entretien", "Entretien")


### Facturations ###

def ajouter_facturation_professionnel(idClient):
    valeurs = [
        idClient,
        choisir_agent("commercial"),
        False
    ]
    insert("Facturation", ["clientProfessionnel", "agent_com", "etat_payement"], valeurs)
    return recupDernierAjout("idFacturation", "Facturation")


def ajouter_facturation_particulier(idClient):
    valeurs = [
        idClient,
        choisir_agent("commercial"),
        False
    ]
    insert("Facturation", ["clientParticulier", "agent_com", "etat_payement"], valeurs)
    return recupDernierAjout("idFacturation", "Facturation")

### Locations professionnel et particulier ###

def ajouter_location_professionnel(id_contrat, idClient):
    valeurs = [
        id_contrat,
        choisir_conducteur(idClient)
    ]
    insert("LocationProfessionnel", ["id_contrat", "conducteur"], valeurs)

def ajouter_location_particulier(id_contrat, idClient):
    valeurs = [
        id_contrat,
        idClient
    ]
    insert("LocationParticulier", ["id_contrat", "particulier"], valeurs)

### ajouter un nouveau client ###

def ajouter_client_prof():
    valeurs = [
        input("Nom : "),
        input("Adresse mail : "),
        input("Numero de telephone : "),
        input("Numero de siret : "),
        input("Numero de carte bancaire : "),
    ]
    insert("Entreprise", ["nom","mail","tel","siret","num_bancaire"], valeurs)
    return recupDernierAjout("id_client", "Entreprise")

def ajouter_client_part():
    valeurs = [
        input("Nom : "),
        input("Prenom : "),
        input("Adresse mail : "),
        input("Numero de telephone : "),
        input("Numero de permis : "),
        input("Date de naissance (DD/MM/AAAA) : ")
    ]
    insert("Entreprise", ["nom", "prenom" "mail", "tel", "siret", "num_bancaire"], valeurs)
    return recupDernierAjout("id_client", "Particulier")

### Récupérer l'identifiant d'un client selon son type (professionnel ou particulier), ajouter le client si besoin ###

def getIdClient(typeClient):
    if typeClient == 1:
        idClient = choisir_client_prof()
        if idClient == -1:
            idClient = ajouter_client_prof()
    else:
        idClient = choisir_client_part()
        if idClient == -1:
            idClient = ajouter_client_part()
    return idClient


### Location générale ###

def ajouter_location():

    # CLIENT
    print("*** Informations Client ***\n")
    typeClient = input("\tClient Professionnel (1) ou Particulier (2) : ")
    while typeClient != "1" and typeClient != "2":
        typeClient = input("\tVeuillez taper 1 ou 2 pour indiquer le type du client : ")
    idClient = getIdClient(typeClient)
    print("\n")

    # VEHICULE
    print("*** Choix du véhicule ***\n")
    #afficher tous les véhicules disponibles à la location
    immat = choisir_vehicule_nouvelle_location()

    # on récupère son nombre de kilomètres:
    query = "SELECT nb_km FROM Vehicule WHERE immat='%s';" %immat
    curseur.execute(query)
    nb_km = curseur.fetchone()

    # on associe la location à un entretien
    id_entretien = ajouter_entretien()

    # on crée une facturation
    if typeClient == 1:
        id_facturation = ajouter_facturation_professionnel(idClient)
    else:
        id_facturation = ajouter_facturation_particulier(idClient)

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
    id_contrat = recupDernierAjout("id_contrat", "Location")

    # on remplit ensuite la table LocationParticulier ou la table LocationProfessionnel c'est selon
    if typeClient == 1:
        ajouter_location_professionnel(id_contrat, idClient)
    else:
        ajouter_location_particulier(id_contrat, idClient)


############### ANNULER LOCATION ###############

def annuler_location():
    c_location = input("\t Contrat de la location à supprimer : ")
    query = "DELETE FROM Location WHERE id_contrat='%s';" %c_location
    curseur.execute(query)
    conn.commit()
    # NB : la cascade est permise grâce au code SQL (voir delete cascade)


############### MODIFIER LOCATION ###############

def modifier_location():
    afficher("\nVoici la liste des locations actuelles", select_all("location"))
    # pour l'instant seuls des attributs string peuvent être modifiés
    id_contrat = input("\tID Contrat de la location à modifier : ")
    nom_col = input("\tParametre à modifier : ")
    nouvelle_valeur = input("\tNouvelle valeur : ")
    query = "UPDATE Location SET %s='%s' WHERE id_contrat='%s';" %(nom_col, nouvelle_valeur, id_contrat)
    curseur.execute(query)
    conn.commit()


############### PAYER FACTURATION ###############


def payer_facturation():
    afficher("Liste des facturations pas encore payer", table)
    id_facturation = input("\t id de la facturation : ")
    moyen_payement = input("\t Moyen de payement : ")
    query = "UPDATE Facturation SET date_payement=current_date, moyen_reglement='%s', etat_payement=TRUE WHERE idFacturation='%s';" %(moyen_payement, id_facturation)
    curseur.execute(query)
    conn.commit()


########## VALIDATION FINALE PAR UN AGENT COM ##########

def validation_finale_location():
    agent_com = choisir_agent("commercial")
    afficher("Liste des locations", select_all("location"))
    location = input("\t ID contrat de la loc : ")
    valeurs = [
        agent_com,
        location,
        "today",
        input("\tResultat de la validation (1:ok / 0:not ok)")
    ]
    insert("ValidationFinale", ["agent_com", "location", "date_validation", "resultat_validation"], valeurs)


########## CONTROLE PAR UN AGENT TECH = MAJ DE ENTRETIEN ##########

def controler_apres_location():
    afficher("Liste des entretien", select_all("entretien"))
    id_entretien = input("\tId de l'entretien : ")
    date_ent = input("\tDate_entretien : ")
    date_ctrl = input("\tDate_controle : ")
    resultat = input("\tResultat du controle : ")
    query = "UPDATE Entretien SET date_entretien='%s', date_controle='%s', resultat='%s' WHERE id_entretien='%s';" %(date_ent, date_ctrl, resultat, id_entretien)
    curseur.execute(query)
    conn.commit()


