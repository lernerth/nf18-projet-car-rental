try:
    import debug_config as cfg
except:
    import config as cfg
import psycopg2
from decimal import Decimal


"""
    Connecter à la base de données
"""
host = "tuxa.sme.utc.fr"

port = " 9503 "

data = "dbNF18p056”

user = "NF18p056"

pass = " cIGh5MzU "
conn = psycopg2.connect(host, port, data, user, pass))
curseur = conn.cursor()




from datetime import date

today = date.today()

def location_passee():
    x = input('Entrez l immatriculation d un véhicule pour connaître ses anciennes locations. ')
    query = "SELECT id_contrat, date_debut,date_fin FROM Location inner join Vehicule ON Location.vehicule_immat=Vehicule.immat where date_fin::date<current_date  and Vehicule.immat=%s" %x 
    curseur.execute(query)
    raw = cur.fetchone()
    while raw:
    print ("idcontrat:" raw[0], "date début:" raw[1], "date fin:" raw[2])
    raw = cur.fetchone()


def location_present():
    x = input('Entrez l immatriculation d un véhicule pour connaître la location presente. ')
    query = "SELECT id_contrat, date_debut,date_fin FROM Location inner join Vehicule ON Location.vehicule_immat=Vehicule.immat WHERE date_debut::date<=current_date and date_fin::date>=surrent_date and Vehicule.immat=%s" %x
    curseur.execute(query)
    raw = cur.fetchone()
    while raw:
    print ("idcontrat:" raw[0], "date début:" raw[1], "date fin:" raw[2])
    raw = cur.fetchone()

def location_future():
     x = input('Entrez l immatriculation d un véhicule pour connaître ses locations futurs ')
    query = "SELECT id_contrat, date_debut,date_fin FROM Location inner join Vehicule ON Location.vehicule_immat=Vehicule.immat WHERE date_debut::date>current_date and Vehicule.immat=%s" %x
    curseur.execute(query)
    raw = cur.fetchone()
    while raw:
    print ("idcontrat:" raw[0], "date début:" raw[1], "date fin:" raw[2])
    raw = cur.fetchone()


def argent_total():
    x = input('Entrez l immatriculation d un véhicule pour connaître l argent total qu il a gagné')
    query = "SELECT SUM(montant) FROM Facturation inner join LocationParticulier ON LocationParticulier.particulier=Facturation.clientParticulier inner join Location ON Location.id_contrat=LocationParticulier.id_contrat inner join Vehicule ON Location.vehicule_immat=Vehicule.immat WHERE date_fin::date<current_date and Vehicule.immat=%s" %x
    curseur.execute(query)
    raw1 = cur.fetchone()
    query = "SELECT SUM(montant) FROM Facturation inner join LocationProfessionel ON LocationProfessionel.conducteur=Facturation.clientProfessionel inner join Location ON Location.id_contrat=LocationProfessionnel.id_contrat inner join Vehicule onLocation.vehicule_immat=Vehicule.immat WHERE etat_payement='1' AND date_fin::date<current_date and Vehicule.immat=%s" %x
    curseur.execute(query)
    raw2 = cur.fetchone()
    a= raw1 + raw2
    print(a)

def dureemoylocation():
    x = input('Entrez l immatriculation d un véhicule pour connaître sa surée moyenne de location ')
    query = "SELECT AVG(date_fin-date_debut) FROM Location inner join Vehicule ON Location.vehicule_immat=Vehicule.immat where date_fin::date<current_date and Vehicule.immat=%s" %x 
     curseur.execute(query)
    raw1 = cur.fetchone()
    raw = cur.fetchone()
    while raw:
    print (raw)
    raw = cur.fetchone()
