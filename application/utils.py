try:
    import debug_config as cfg
except:
    import config as cfg
import psycopg2
from tabulate import tabulate

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
    return input("Entrez id d'agent choisi : ")


def choisir_agent_com(nom, prenom):
    query = """SELECT * FROM Employe
                JOIN AgentCommercial ON Employe.id_employe = AgentCommercial.id_employe
                WHERE LOWER(Employe.nom) LIKE %s
                   AND LOWER(Employe.prenom) LIKE %s;"""
    curseur.execute(query, ("%" + nom.lower() + "%", "%" + prenom.lower() + "%"))
    agents = curseur.fetchall()
    afficher("Voici la liste des agents correspondants", agents)
    return input("Entrez id d'agent choisi : ")


def choisir_agent(type_agent):
    nom = input("Entrez le nom d'agent (laissez vide pour ne pas prendre en compte) : ")
    prenom = input("Entrez le prenom d'agent (laissez vide pour ne pas prendre en compte) : ")
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
    query = "SELECT %s FROM %s;" %(col,table)
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
    afficher("\nVoici la liste des clients professionnels correspondants :", clients)
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
    afficher("\nVoici la liste des clients correspondants :", clients)
    return input("Entrez id du client choisi, ou -1 si le client n'existe pas et que vous souhaitez l'ajouter : ")

#print("%s" %choisir_client_part())

'''
    Choisir un véhicule
'''

def choisir_vehicule():
    modele = input("Modele du vehicule recherche (laisser vide pour voir toutes les possibilites) : ")
    query = """SELECT v.immat, v.modele, l.* FROM Vehicule v
                LEFT JOIN Location l
                ON v.immat = l.vehicule_immat
                WHERE (l.id_contrat is null OR current_date > l.date_fin)
                    AND LOWER(v.modele) LIKE %s"""
    curseur.execute(query, ("%" + modele.lower() + "%",))
    vehicules = curseur.fetchall()
    afficher("Voici la liste vehicules disponibles a la location correspondants", vehicules)
    return input("Entrez l'immatriculation du vehicule choisi : ")

print("%s" % choisir_vehicule())

'''
    Choisir une société d'entretien
'''
def choisir_societe():
    nom = input("Nom de la societe d'entretien recherchee (laisser vide pour voir toutes les societes enregistrees) : ")
    query = """SELECT * FROM SocieteEntretien
                    WHERE LOWER(SocieteEntretien.nom) LIKE %s;"""
    curseur.execute(query, ("%" + nom.lower() + "%",))
    societes = curseur.fetchall()
    afficher("\nVoici la liste des societes d'entretien correspondants :", societes)
    return input("Entrer le numero de siret de la societe choisie : ")

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
        input("Date de naissance (JJ/MM/AAAA) : "),
        input("Numero de permis : ")
    ]
    insert("Conducteur", ["entreprise", "nom", "prenom", "date_naissance", "num_permis"], valeurs)
    return recupDernierAjout("num_permis", "Conducteur")

def choisir_conducteur(idClient):
    query = """SELECT * FROM Conducteur WHERE Conducteur.entreprise = %s;"""
    curseur.execute(query, (idClient,))
    conducteurs = curseur.fetchall()
    afficher("\nVoici la liste des conducteurs deja enregistres pour cette societe : ", conducteurs)
    choixCond = input("Entrez le numero de permis du conducteur choisi ou taper -1 pour ajouter un nouveau conducteur : ")
    if choixCond == "-1":
        choixCond = ajouter_conducteur(idClient)
    return choixCond

#print("%s" %choisir_conducteur(1))

