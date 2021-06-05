try:
    import debug_config as cfg
except:
    import config as cfg

import psycopg2
from tabulate import tabulate
from datetime import date, datetime

"""
    Connecter à la base de données
"""
conn = psycopg2.connect(dbname=cfg.DBNAME, user=cfg.DBUSER,
                        password=cfg.DBPWD, host=cfg.DBHOST, port=cfg.DBPORT)
curseur = conn.cursor()


"""
    Afficher table
"""

def afficher(text, table):
    header = [desc[0] for desc in curseur.description]
    print(text + "\n")
    print(tabulate(table, headers=header), end="\n\n")
    # for row in table:
    #     print("======================================")
    #     for i in range(len(row)):
    #         print("\t", header[i], ":", row[i], sep=" ", end="\n")


"""
    Retrouver toutes les lignes d'une table
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

"""
    Cette fonction permet a utilisateur de choisir un agent
    @type:  - "technique" si cherchez agent technique
            - "commercial" si cherchez agent commercial
"""

def choisir_agent_tech(nom, prenom):
    query = """SELECT * FROM Employe
                JOIN AgentTechnique ON Employe.id_employe = AgentTechnique.id_employe
                WHERE LOWER(Employe.nom) LIKE %s
                   AND LOWER(Employe.prenom) LIKE %s;"""
    curseur.execute(query, ("%" + nom.lower() + "%", "%" + prenom.lower() + "%"))
    agents = curseur.fetchall()
    afficher("Voici la liste des agents correspondants", agents)
    return input("Entrez id de l'agent choisi : ")


def choisir_agent_com(nom, prenom):
    query = """SELECT * FROM Employe
                JOIN AgentCommercial ON Employe.id_employe = AgentCommercial.id_employe
                WHERE LOWER(Employe.nom) LIKE %s
                   AND LOWER(Employe.prenom) LIKE %s;"""
    curseur.execute(query, ("%" + nom.lower() + "%", "%" + prenom.lower() + "%"))
    agents = curseur.fetchall()
    afficher("Voici la liste des agents correspondants", agents)
    return input("Entrez id de l'agent choisi : ")


def choisir_agent(type_agent):
    print("Choix de l'agent", type_agent, ":")
    nom = input("\tNom (laissez vide pour ne pas prendre en compte) : ")
    prenom = input("\tPrenom (laissez vide pour ne pas prendre en compte) : ")
    type_agent_switcher = {
        "technique": choisir_agent_tech,
        "commercial": choisir_agent_com
    }
    return type_agent_switcher.get(type_agent)(nom, prenom)

# print("%s" %choisir_agent("technique"))

'''
    Récupérer un élément de la dernière insertion dans une table
'''

def recupDernierAjout(col, table):
    query = "SELECT %s FROM %s;" % (col, table)
    curseur.execute(query)
    raw = curseur.fetchone()
    next_raw = curseur.fetchone()
    while next_raw:
        raw = next_raw
        next_raw = curseur.fetchone()
    return raw

'''
    Choisir client (même principe que choisir agent)
'''

def choisir_client_prof():
    nom = input("Entrez le nom de l'entreprise (laissez vide pour ne pas prendre en compte) : ")
    query = """SELECT * FROM Entreprise
                WHERE LOWER(Entreprise.nom) LIKE %s;"""
    curseur.execute(query, ("%" + nom.lower() + "%",))
    clients = curseur.fetchall()
    afficher("Voici la liste des clients professionnels correspondants :", clients)
    return input("Entrez id du client choisi ou -1 si le client n'existe pas et que vous souhaitez l'ajouter : ")

#print("%s" %choisir_client_prof())

def choisir_client_part():
    nom = input("Entrez le nom du client (laissez vide pour ne pas prendre en compte) : ")
    prenom = input("Entrez le prenom du client (laissez vide pour ne pas prendre en compte) : ")
    query = """SELECT * FROM Particulier
                WHERE LOWER(Particulier.nom) LIKE %s
                    AND LOWER(Particulier.prenom) LIKE %s;"""
    curseur.execute(query, ("%" + nom.lower() + "%", "%" + prenom.lower() + "%"))
    clients = curseur.fetchall()
    afficher("Voici la liste des clients correspondants :", clients)
    return input("Entrez id du client choisi, ou -1 si le client n'existe pas et que vous souhaitez l'ajouter : ")

#print("%s" %choisir_client_part())

'''
    Choisir un véhicule
'''

def choisir_vehicule_nouvelle_location(date_deb_location, date_fin_location):

    date_deb_location = datetime.strptime(date_deb_location, "%Y-%m-%d").date()
    date_fin_location = datetime.strptime(date_fin_location, "%Y-%m-%d").date()

    modele = input("Modele (laissez vide si vous n'avez pas de preference) : ")

    #Retrouver tous les vehicules avec leurs locations
    query = """SELECT v.immat, v.modele, l.date_debut, l.date_fin FROM Vehicule v
                LEFT JOIN Location l ON v.immat = l.vehicule_immat
                WHERE v.modele LIKE %s
                ORDER BY v.immat, l.date_debut;"""
    curseur.execute(query, ("%" + modele.lower() + "%",))
    vehicules = curseur.fetchall()
    #afficher("test requete : ", vehicules)

    vehicules_dipos = []

    i = 0
    while i < len(vehicules):
        debut = i
        fin = i
        while (fin + 1) < len(vehicules) and vehicules[fin + 1][0] == vehicules[debut][0]:
            fin += 1
        # 2018-06-15
        # 2018-07-10
        # print("Immat:", vehicules[debut][0], debut, fin, sep=" ", end="\n")

        if fin - debut + 1 == 1: # Une seule location en cours
            if (vehicules[debut][2] is None) or (date_fin_location < vehicules[debut][2]) or (vehicules[debut][3] < date_deb_location):
                vehicules_dipos.append(vehicules[debut][:2])

        else:                    # Plusieurs locations en cours
            # Verifier si on peut louer avant la premiere location
            if (date_fin_location < vehicules[debut][2]):
                vehicules_dipos.append(vehicules[debut][:2])
                i = fin + 1
                continue

            # Verifier si on peut louer apres la derniere location
            if (date_deb_location > vehicules[fin][3]):
                vehicules_dipos.append(vehicules[fin][:2])
                i = fin + 1
                continue

            while debut < fin:
                if (vehicules[debut][3] < date_deb_location) and (date_fin_location < vehicules[debut + 1][2]):
                    vehicules_dipos.append(vehicules[debut][:2])
                    break
                debut += 1

        i = fin + 1

    
    afficher("Voici la liste vehicules disponibles selon les dates choisies et les preferences enregistrees :", vehicules_dipos)

    return input("Entrez l'immatriculation du vehicule choisi : ")

# print("%s" % choisir_vehicule_nouvelle_location())

'''
    Choisir une société d'entretien
'''
def choisir_societe():
    nom = input("Nom de la societe d'entretien recherchee (laisser vide pour voir toutes les societes enregistrees) : ")
    query = """SELECT * FROM SocieteEntretien
                    WHERE LOWER(SocieteEntretien.nom) LIKE %s;"""
    curseur.execute(query, ("%" + nom.lower() + "%",))
    societes = curseur.fetchall()
    afficher("Voici la liste des societes d'entretien correspondants :", societes)
    return str(input("Entrer le numero de siret de la societe choisie : "))

#print("%s" %choisir_societe())

'''
    Choisir un conducteur
'''

def ajouter_conducteur(idClient):
    print("*** Ajout d'un nouveau conducteur ***")
    valeurs = [
        idClient,
        input("Nom : "),
        input("Prenom : "),
        input("Date de naissance (YYYY-MM-DD) : "),
        input("Numero de permis : ")
    ]
    insert("Conducteur", ["entreprise", "nom", "prenom", "date_naissance", "num_permis"], valeurs)
    return recupDernierAjout("num_permis", "Conducteur")

def choisir_conducteur(idClient):
    print("\n*** Choix du conducteur ***")
    query = """SELECT * FROM Conducteur WHERE Conducteur.entreprise = %s;"""
    curseur.execute(query, (idClient,))
    conducteurs = curseur.fetchall()
    afficher("\nVoici la liste des conducteurs deja enregistres pour cette societe : ", conducteurs)
    choixCond = input("Entrez le numero de permis du conducteur choisi ou taper -1 pour ajouter un nouveau conducteur : ")
    if choixCond == "-1":
        choixCond = ajouter_conducteur(idClient)
    return choixCond

#print("%s" %choisir_conducteur(1))

def choisir_modele():
    query = """SELECT nom FROM Modele"""
    curseur.execute(query)
    nomsModeles=curseur.fetchall()
    afficher("Modele (choisir parmi les possibilités ci-dessous) :", nomsModeles)
    choixMod = input("Choix du modele (attention a l'orthographe!) : ")
    return choixMod

#print(choisir_modele())

def choisir_agence():
    query = """SELECT * FROM Agence"""
    curseur.execute(query)
    listeAg = curseur.fetchall()
    afficher("Agence : ", listeAg)
    choixAg = input("Id de l'agence choisie : ")
    return choixAg

def choisir_carburant():
    query = """SELECT * FROM TypeCarburant"""
    curseur.execute(query)
    carb = curseur.fetchall()
    afficher("Carburant :", carb)
    choixC = input("Votre choix : ")
    return choixC

def choisir_factu_impayee():
    query = """SELECT f.idFacturation, f.montant, p.nom, p.prenom, p.mail FROM Facturation f JOIN Particulier p ON f.clientParticulier = p.id_client WHERE f.etat_payement is FALSE"""
    curseur.execute(query)
    facImp = curseur.fetchall()
    afficher("Locations de particulier impayees a ce jour :", facImp)

    query = """SELECT f.idFacturation, f.montant, e.nom, e.mail FROM Facturation f JOIN Entreprise e ON f.clientProfessionnel = e.id_client WHERE f.etat_payement is FALSE"""
    curseur.execute(query)
    facImp = curseur.fetchall()
    afficher("Locations de professionnel impayees a ce jour :", facImp)

    choixF = input("Id de la facturation a regler : ")
    return choixF

#print("%s" %choisir_factu_impayee())


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

#print(ajouter_client_prof())

def ajouter_client_part():
    valeurs = [
        input("Nom : "),
        input("Prenom : "),
        input("Adresse mail : "),
        input("Numero de telephone : "),
        input("Adresse (non obligatoire) : "),
        input("Numero de permis : "),
        input("Date de naissance (YYYY-MM-DD) : "),
        input("Numero de carte bancaire : ")
    ]
    insert("Particulier", ["nom", "prenom", "mail", "telephone", "adresse", "num_permis", "date_naissance", "num_bancaire"], valeurs)
    return recupDernierAjout("id_client", "Particulier")

#print(ajouter_client_part())

def choisir_location_a_valider():
    query = """SELECT * FROM Location l LEFT JOIN ValidationFinale v ON l.id_contrat = v.location
                EXCEPT 
                SELECT * FROM Location l JOIN ValidationFinale v ON l.id_contrat = v.location"""
    curseur.execute(query)
    aff = curseur.fetchall()
    afficher("\nLocations non validees a ce jour :", aff)
    choix = input("ID contrat de la loc : ")
    return choix

#choisir_location_a_valider()

def choisir_facturation_entreprise(idClientPro):
    query = """SELECT f.idFacturation, f.montant FROM Facturation f JOIN Entreprise e 
                ON f.clientProfessionnel=e.id_client
                WHERE e.id_client='%s' AND f.etat_payement=false;""" % idClientPro
    curseur.execute(query)
    aff = curseur.fetchall()
    afficher("\nFacturations impayees associees a cette entreprise: ", aff)
    c = int(input("Choisir une facturation parmi celle existante ou taper -1 pour un creer une nouvelle : "))
    return c
