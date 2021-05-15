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