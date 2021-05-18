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
    curseur.execute(query, ("%" + nom + "%", "%" + prenom + "%"))
    agents = curseur.fetchall()
    afficher("Voici la liste des agents correspondants", agents)
    return input("Entrez id d'agent choisi : ")


def choisir_agent_com(nom, prenom):
    query = """SELECT * FROM Employe
                JOIN AgentCommercial ON Employe.id_employe = AgentCommercial.id_employe
                WHERE LOWER(Employe.nom) LIKE %s
                   AND LOWER(Employe.prenom) LIKE %s;"""
    curseur.execute(query, ("%" + nom + "%", "%" + prenom + "%"))
    agents = curseur.fetchall()
    afficher("Voici la liste des agents correspondants", agents)
    return input("Entrez id d'agent choisi : ")

def choisir_agent(type_agent):
    nom = input("Entrez le nom d'agent (laissez vide pour ne pas prendre en compte) ")
    prenom = input("Entrez le prenom d'agent (laissez vide pour ne pas prendre en compte) ")
    type_agent_switcher = {
        "technique": choisir_agent_tech,
        "commercial": choisir_agent_com
    }
    return type_agent_switcher.get(type_agent)(nom, prenom)
