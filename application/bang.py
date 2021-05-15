# Bilan et statistiques par catégorie

def bilan_par_categorie(curseur):
    query =  """SELECT 	total.categorie, total.nb_vehicules, encours.nb_vehicules AS nb_vehicules_en_location,
                        total.pourcentage AS pourcentage_total_vehicules, statistique.argent_rapporte
                FROM
                    (SELECT CategorieVehicule.nom as categorie, COUNT(Vehicule.immat) as nb_vehicules, (COUNT(Vehicule.immat) * 100.0 / SUM(COUNT(Vehicule.immat)) over ()) as pourcentage FROM CategorieVehicule
                        JOIN Modele ON Modele.categorie = CategorieVehicule.nom
                        JOIN Vehicule ON Modele.nom = Vehicule.modele
                        GROUP BY CategorieVehicule.nom) AS total
                JOIN (SELECT 	CategorieVehicule.nom as categorie,
                                SUM(CASE WHEN Location.date_debut <= current_date AND current_date <= Location.date_fin THEN 1 ELSE 0 END) as nb_vehicules
                    FROM CategorieVehicule
                        JOIN Modele ON Modele.categorie = CategorieVehicule.nom
                        JOIN Vehicule ON Modele.nom = Vehicule.modele
                        JOIN Location ON Location.vehicule_immat = Vehicule.immat
                        GROUP BY CategorieVehicule.nom) AS encours ON total.categorie = encours.categorie
                JOIN (SELECT argent.categorie, SUM(argent.montant) as argent_rapporte FROM
                        (SELECT DISTINCT CategorieVehicule.nom as categorie, Facturation.montant  FROM Location
                            JOIN Facturation ON Facturation.idfacturation = Location.facturation
                            JOIN Vehicule ON Vehicule.immat = Location.vehicule_immat
                            JOIN Modele ON Vehicule.modele = Modele.nom
                            JOIN CategorieVehicule ON CategorieVehicule.nom = Modele.categorie
                            WHERE Facturation.etat_payement = TRUE) AS argent
                    GROUP BY argent.categorie) AS statistique ON statistique.categorie = encours.categorie;"""
    curseur.execute(query)
    resultats = curseur.fetchall()
    print("\n")
    for row in resultats:
        print("Pour la catégorie",row[0], ": ")
        print("\tNombre de véhicules total dans cette catégorie : ",row[1])
        print("\tNombre de véhicules de cette catégorie actuellement en location : ",row[2])
        print("\tProportion des vehicules entrant dans cette catégorie : ",row[3])
        print("\tTotal d'argent généré par les locations de cette catégorie : ", row[4])
        print("\n")