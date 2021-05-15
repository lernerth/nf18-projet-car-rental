global paye
global paye_pro
global nb_loc_prevues
global nb_loc_passees
global nb_loc_encours
global nb_loc_prevues_pro
global nb_loc_passees_pro
global nb_loc_encours_pro


def bilan_client(curseur):
    try :
        choix = int(input("""Quel type de client recherchez-vous ? 
                                    1.Client Particulier 
                                    2.Client Professionnel (entreprise)
                          """))
        if choix == 1:
            client = input("Entrer le numéro de client : ")
            sql = "SELECT * FROM Particulier WHERE id_client = %s"
            curseur.execute(sql, (client,))
            row = curseur.fetchone()
            afficher_client_particulier(row)
            nombre_locations_encours(curseur, row[0])
            nombre_locations_passees(curseur, row[0])
            nombre_locations_prevues(curseur, row[0])
            total_paye(curseur, row[0])
            print("Nombre de locations passées : ", nb_loc_passees)
            print("Nombre de locations en cours : ", nb_loc_encours)
            print("Nombre de locations prévues : ", nb_loc_prevues)
            print("Total payé par le client : ", paye)

        elif choix == 2 :
            client = input("Entrer le numéro de client : ")
            sql = "SELECT * FROM Entreprise WHERE id_client = %s"
            curseur.execute(sql, (client,))
            row = curseur.fetchone()
            afficher_client_pro(row)
            nombre_locations_encours_pro(curseur, row[0])
            nombre_locations_passees_pro(curseur, row[0])
            nombre_locations_prevues_pro(curseur, row[0])
            total_paye_pro(curseur, row[0])
            print("Nombre de locations passées : ", nb_loc_passees_pro)
            print("Nombre de locations en cours : ", nb_loc_encours_pro)
            print("Nombre de locations prévues : ", nb_loc_prevues_pro)
            print("Total payé par le client : ", paye_pro)

    except ValueError:
        print("Choix incorrect, il faut entrer un entier de 1 à 4")
        return 0



def afficher_client_particulier(client):
    print(client[1], client[2], " : \n")
    print("\tDate de naissance :", client[8])
    print("\tAdresse :", client[6])
    print("\tNuméro de téléphone :", client[5])
    print("\tNuméro de permis :", client[7])
    print("\tID client :", client[0])


def afficher_client_pro(client):
    print(client[1], " : \n")
    print("\tSIRET :", client[6])
    print("\tID client :", client[0])


def nombre_locations_passees(curseur, client):
    global nb_loc_passees
    sql = "SELECT COUNT(*) FROM Location JOIN LocationParticulier ON Location.id_contrat=LocationParticulier.id_contrat WHERE LocationParticulier.particulier = %s AND Location.date_fin::date < current_date"
    curseur.execute(sql, (client,))
    result = curseur.fetchone()
    nb_loc_passees = result[0]
    return nb_loc_passees


def nombre_locations_encours(curseur, client):
    global nb_loc_encours
    sql = "SELECT COUNT (*) FROM Location JOIN LocationParticulier ON Location.id_contrat=LocationParticulier.id_contrat WHERE LocationParticulier.particulier = %s AND Location.date_fin::date > current_date and Location.date_debut::date < current_date"
    curseur.execute(sql, (client,))
    result = curseur.fetchone()
    nb_loc_encours = result[0]
    return nb_loc_encours


def nombre_locations_prevues(curseur, client):
    global nb_loc_prevues
    sql = "SELECT COUNT(*) FROM Location JOIN LocationParticulier ON Location.id_contrat=LocationParticulier.id_contrat WHERE LocationParticulier.particulier = %s AND Location.date_debut::date > current_date"
    curseur.execute(sql, (client,))
    result = curseur.fetchone()
    nb_loc_prevues = result[0]
    return nb_loc_prevues


def total_paye(curseur, client):
    global paye
    sql = "SELECT SUM(montant) FROM Facturation JOIN Particulier ON Facturation.ClientParticulier=Particulier.id_client WHERE Particulier.id_client = %s"
    curseur.execute(sql, (client,))
    result = curseur.fetchone()
    paye = result[0]
    return paye


def nombre_locations_passees_pro(curseur, client):
    global nb_loc_passees_pro
    sql = "SELECT COUNT(*) FROM Location JOIN LocationProfessionnel ON Location.id_contrat = LocationProfessionnel.id_contrat JOIN Conducteur ON LocationProfessionnel.conducteur = Conducteur.num_permis WHERE Conducteur.entreprise = %s AND Location.date_fin::date < CURRENT_DATE"
    curseur.execute(sql,(client,))
    result = curseur.fetchone()
    nb_loc_passees_pro = result[0]
    return nb_loc_passees_pro


def nombre_locations_encours_pro(curseur, client):
    global nb_loc_encours_pro
    sql = "SELECT COUNT(*) FROM Location JOIN LocationProfessionnel ON Location.id_contrat = LocationProfessionnel.id_contrat JOIN Conducteur ON LocationProfessionnel.conducteur = Conducteur.num_permis WHERE Conducteur.entreprise = %s AND Location.date_fin::date > CURRENT_DATE AND Location.date_debut::date < CURRENT_DATE"
    curseur.execute(sql,(client,))
    result = curseur.fetchone()
    nb_loc_encours_pro = result[0]
    return nb_loc_encours_pro


def nombre_locations_prevues_pro(curseur, client):
    global nb_loc_prevues_pro
    sql = "SELECT COUNT(*) FROM Location JOIN LocationProfessionnel ON Location.id_contrat = LocationProfessionnel.id_contrat JOIN Conducteur ON LocationProfessionnel.conducteur = Conducteur.num_permis WHERE Conducteur.entreprise = %s AND Location.date_debut::date > CURRENT_DATE"
    curseur.execute(sql,(client,))
    result = curseur.fetchone()
    nb_loc_prevues_pro = result[0]
    return nb_loc_prevues_pro


def total_paye_pro(curseur, client):
    global paye_pro
    sql = "SELECT SUM(montant) FROM Facturation JOIN Entreprise ON Facturation.ClientProfessionnel=Entreprise.id_client WHERE Entreprise.id_client = %s AND Facturation.etat_payement = TRUE"
    curseur.execute(sql, (client,))
    result = curseur.fetchone()
    paye_pro = result[0]
    return paye_pro
