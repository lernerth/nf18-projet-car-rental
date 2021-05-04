-- Cas où l'on veut simplement vider les tables, sans les supprimer

TRUNCATE TABLE 'Agence';
TRUNCATE TABLE 'Employe';
TRUNCATE TABLE 'AgentTechnique';
TRUNCATE TABLE 'AgentCommercial';
TRUNCATE TABLE 'SocieteEntretien';
TRUNCATE TABLE 'AssocAgenceSocieteEntretien';
TRUNCATE TABLE 'Entretien';
TRUNCATE TABLE 'Option';
TRUNCATE TABLE 'TypeCarburant';
TRUNCATE TABLE 'Marque';
TRUNCATE TABLE 'CategorieVehicule';
TRUNCATE TABLE 'Modele';
TRUNCATE TABLE 'Vehicule';
TRUNCATE TABLE 'Location';
TRUNCATE TABLE 'Particulier';
TRUNCATE TABLE 'LocationParticulier';
TRUNCATE TABLE 'Entreprise';
TRUNCATE TABLE 'Conducteur';
TRUNCATE TABLE 'LocationProfessionnel';
TRUNCATE TABLE 'Facturation';
TRUNCATE TABLE 'ValidationFinale';

-- Cas où l'on veut supprimer toute la base de données et toutes ses données

DROP DATABASE NF18LocationVehicule;