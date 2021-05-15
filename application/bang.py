# Bilan et statistiques par catégorie

def bilan_par_categorie(curseur):
    query =  """SELECT 	total.categorie AS categorie,
                        total.nb_vehicules AS nb_vehicules,
                        encours.nb_vehicules AS nb_vehicules_en_location,
                        total.pourcentage,
                        encours.argent_rapporte
                FROM
                    (SELECT CategorieVehicule.nom as categorie, COUNT(Vehicule.immat) as nb_vehicules, (COUNT(Vehicule.immat) * 100.0 / SUM(COUNT(Vehicule.immat)) over ()) as pourcentage FROM CategorieVehicule
                        JOIN Modele ON Modele.categorie = CategorieVehicule.nom
                        JOIN Vehicule ON Modele.nom = Vehicule.modele
                        GROUP BY CategorieVehicule.nom) AS total
                JOIN (SELECT 	CategorieVehicule.nom as categorie,
                                SUM(CASE
                                        WHEN Location.date_debut <= current_date AND current_date <= Location.date_fin
                                        THEN 1
                                        ELSE 0
                                    END) as nb_vehicules,
                                SUM(CASE Facturation.etat_payement
                                        WHEN TRUE
                                        THEN Facturation.montant
                                        ELSE Money(0)
                                    END) as argent_rapporte
                    FROM CategorieVehicule
                        JOIN Modele ON Modele.categorie = CategorieVehicule.nom
                        JOIN Vehicule ON Modele.nom = Vehicule.modele
                        JOIN Location ON Location.vehicule_immat = Vehicule.immat
                        JOIN Facturation ON Facturation.idfacturation = Location.facturation
                        GROUP BY CategorieVehicule.nom) AS encours
                ON total.categorie = encours.categorie;"""
    curseur.execute(query)
    resultats = curseur.fetchall()
    for row in resultats:
        print(row)