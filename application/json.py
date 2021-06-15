
def option_vehicule():
    sql = "SELECT v.immat, opt.* FROM Vehicule v, JSON_ARRAY_ELEMENTS(v.liste_options) opt"
    curseur.execute(sql, (client,))
    raw = curseur.fetchone()
    while raw:
        print ("immatriculation: ", raw[0], "option:", raw[1])
        raw = curseur.fetchone()

