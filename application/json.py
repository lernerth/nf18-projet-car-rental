

def option_vehicule(client):
    sql = "SELECT SUM(montant) FROM Facturation JOIN Entreprise ON Facturation.ClientProfessionnel=Entreprise.id_client WHERE Entreprise.id_client = %s AND Facturation.etat_payement = TRUE"
    curseur.execute(sql, (client,))
    result = curseur.fetchone()
    option = result[0]
    return paye_pro
