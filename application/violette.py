from utils import *

################# AJOUTER LOCATION #################

#### entretien ####

def ajouter_entretien(immat):
    query = """SELECT v.agent_tech FROM Vehicule v WHERE v.immat = '%s'""" %immat
    curseur.execute(query)
    ag = curseur.fetchone()
    valeurs = [
        choisir_societe(),
        ag,
     ]
    insert("Entretien", ["societe", "agent_tech"], valeurs) # voir plus tard pour ajouter date etc.

    # on renvoie l'id de cet entretien (logiquement, c'est le dernier ajout dans la table entretien)
    return recupDernierAjout("id_entretien", "Entretien")


### Facturations ###

def ajouter_facturation_professionnel(idClient):
    idFact = choisir_facturation_entreprise(idClient)
    if idFact == -1:
        print("Ajout d'une nouvelle facturation: ")
        valeurs = [
            idClient,
            choisir_agent("commercial"),
            False
        ]
        insert("Facturation", ["clientProfessionnel", "agent_com", "etat_payement"], valeurs)
        return recupDernierAjout("idFacturation", "Facturation")
    else:
        return idFact

#ajouter_facturation_professionnel(2)

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


### Récupérer l'identifiant d'un client selon son type (professionnel ou particulier), ajouter le client si besoin ###

def getIdClient(typeClient):
    if typeClient=="1":
        idClient = choisir_client_prof()
        if idClient=="-1":
            idClient = ajouter_client_prof()
    else:
        idClient = choisir_client_part()
        if idClient == "-1":
            idClient = ajouter_client_part()
    return idClient


### Location générale ###

def ajouter_location():

    # CLIENT
    print("*** Informations Client ***\n")
    typeClient = input("Client Professionnel (1) ou Particulier (2) : ")
    while typeClient != "1" and typeClient != "2":
        typeClient = input("Veuillez taper 1 ou 2 pour indiquer le type du client : ")
    idClient = getIdClient(typeClient)
    print("\n")

    # DATES
    print("*** Dates Location ***\n")
    date_deb_location = input("Date debut (format YYYY-MM-DD) : ")
    date_fin_location = input("Date fin (format YYYY-MM-DD) : ")
    print("\n")

    # VEHICULE
    print("*** Choix du véhicule ***\n")
    #afficher tous les véhicules disponibles à la location
    immat = choisir_vehicule_nouvelle_location(date_deb_location, date_fin_location)
    print("\n")

    # on récupère son nombre de kilomètres:
    query = "SELECT nb_km FROM Vehicule WHERE immat='%s';" %immat
    curseur.execute(query)
    nb_km = curseur.fetchone()

    # ENTRETIEN
    print("*** Entretien ***\n")
    id_entretien = ajouter_entretien(immat)
    print("\n")

    # FACTURATION
    print("*** Facturation ***\n")
    if typeClient == "1":
        id_facturation = ajouter_facturation_professionnel(idClient)
    else:
        id_facturation = ajouter_facturation_particulier(idClient)

    valeurs = [
        date_deb_location,
        date_fin_location,
        nb_km,
        immat,
        id_entretien,
        id_facturation
    ]
    insert("Location", ["date_debut", "date_fin", "km_parcourus", "vehicule_immat", "entretien", "facturation"], valeurs)

    # on récupère l'id contrat de la location qui vient d'être créée
    id_contrat = recupDernierAjout("id_contrat", "Location")

    # on remplit ensuite la table LocationParticulier ou la table LocationProfessionnel c'est selon
    if typeClient == "1":
        ajouter_location_professionnel(id_contrat, idClient)
    else:
        ajouter_location_particulier(id_contrat, idClient)

    print("\nLa location a bien ete ajoutee !\n")


############### MODIFIER LOCATION ###############

def modifier_location():
    afficher("Voici la liste des locations actuelles", select_all("location"))
    id_contrat = input("ID Contrat de la location à modifier : ")
    nom_col = input("Parametre à modifier : ")
    nouvelle_valeur = input("Nouvelle valeur : ")
    query = "UPDATE Location SET %s='%s' WHERE id_contrat='%s';" %(nom_col, nouvelle_valeur, id_contrat)
    curseur.execute(query)
    conn.commit()


############### ANNULER LOCATION ###############

def annuler_location():
    afficher("Locations : ", select_all("location"))
    c_location = input("Contrat de la location à supprimer : ")
    query = "DELETE FROM Location WHERE id_contrat='%s';" %c_location
    curseur.execute(query)
    conn.commit()
    # NB : la cascade est permise grâce au code SQL (voir create.sql tables location pro et part)


############### PAYER FACTURATION ###############

def payer_facturation():
    ifFact = choisir_factu_impayee()
    moyen_payement = input("Moyen de payement : ")
    query = "UPDATE Facturation SET date_payement=current_date, moyen_reglement='%s', etat_payement=TRUE WHERE idFacturation='%s';" % (moyen_payement, ifFact)
    curseur.execute(query)
    conn.commit()


########## VALIDATION FINALE PAR UN AGENT COM ##########

def validation_finale_location():
    agent_com = choisir_agent("commercial")
    location = choisir_location_a_valider()
    valeurs = [
        agent_com,
        location,
        input("Resultat de la validation (1:ok / 0:not ok) : ")
    ]
    insert("ValidationFinale", ["agent_com", "location", "resultat_validation"], valeurs)
    query = "UPDATE ValidationFinale SET date_validation=current_date WHERE location='%s';" % location
    curseur.execute(query)


########## CONTROLE PAR UN AGENT TECH = MAJ DE ENTRETIEN ##########

def controler_apres_location():
    agent = int(choisir_agent("technique"))
    query = """SELECT * FROM Entretien e WHERE e.agent_tech = %d""" %agent
    curseur.execute(query)
    listeEnt = curseur.fetchall()
    afficher("Liste des entretiens", listeEnt)
    id_entretien = input("Id de l'entretien : ")
    date_ent = input("Date_entretien (YYYY-MM-DD) : ")
    date_ctrl = input("Date_controle (YYYY-MM-DD) : ")
    resultat = input("Resultat du controle : ")
    query = "UPDATE Entretien SET date_entretien='%s', date_controle='%s', resultat='%s' WHERE id_entretien='%s';" %(date_ent, date_ctrl, resultat, id_entretien)
    curseur.execute(query)
    conn.commit()


