from utils import *

def bilan_vehicule():
    immat = input('Entrez l immatriculation d un véhicule pour le bilan. ')
    location_passee(immat)
    location_present(immat)
    location_future(immat)
    argent_total(immat)
    duree_moy_location(immat)


def location_passee(immat):
    query = "SELECT id_contrat, date_debut,date_fin FROM Location inner join Vehicule ON Location.vehicule_immat=Vehicule.immat where Location.date_fin::date<current_date  and Vehicule.immat='%s'" % immat
    curseur.execute(query)
    raw = curseur.fetchone()
    print("voici les locations passees")
    while raw:
        print ("idcontrat: ", raw[0], "date début:", raw[1], "date fin:", raw[2])
        raw = curseur.fetchone()


def location_present(immat):
    query = "SELECT id_contrat, date_debut,date_fin FROM Location inner join Vehicule ON Location.vehicule_immat=Vehicule.immat WHERE date_debut::date<=current_date and date_fin::date>=current_date and Vehicule.immat='%s'" % immat
    curseur.execute(query)
    raw = curseur.fetchone()
    print("voici la location presente")
    while raw:
        print ("idcontrat:", raw[0], "date début:", raw[1], "date fin:", raw[2])
        raw = curseur.fetchone()

def location_future(immat):
    query = "SELECT id_contrat, date_debut,date_fin FROM Location inner join Vehicule ON Location.vehicule_immat=Vehicule.immat WHERE date_debut::date>current_date and Vehicule.immat='%s'" % immat
    curseur.execute(query)
    raw = curseur.fetchone()
    print("voici les locations futures")
    while raw:
        print ("idcontrat:", raw[0], "date début:", raw[1], "date fin:", raw[2])
        raw = curseur.fetchone()


def argent_total(immat):
    query = "SELECT SUM(Facturation.montant) FROM Location inner join Facturation ON Location.facturation=Facturation.idFacturation inner join Vehicule on Location.vehicule_immat=Vehicule.immat WHERE etat_payement='TRUE' AND date_fin::date<current_date and Vehicule.immat='%s'" % immat
    curseur.execute(query)
    raw1 = curseur.fetchone()
    while raw1:
    print("voici l argent generee par la voiture:" raw1)

def duree_moy_location(immat):
    query = "SELECT AVG(DATEDIFF(day, 'date_fin', 'date_deb')) FROM Location inner join Vehicule ON Location.vehicule_immat=Vehicule.immat where date_fin::date<current_date and Vehicule.immat='%s'" % immat 
    curseur.execute(query)
    raw1 = curseur.fetchone()
    raw = curseur.fetchone()
    print("Voici la duree moyenne de location du véhicule (en jours)")
    while raw:
        print (raw)
        raw = curseur.fetchone()
