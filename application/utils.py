try:
    import debug_config as cfg
except:
    import config as cfg
import psycopg2


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
    print(text)
    for row in table:
        print("======================================")
        for i in range(len(row)):
            print("\t", header[i], ":", row[i], sep=" ", end="\n")

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
