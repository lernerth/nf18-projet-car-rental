-- Cas où l'on veut simplement vider les tables, sans les supprimer

TRUNCATE TABLE Agence CASCADE;
TRUNCATE TABLE Employe CASCADE;
TRUNCATE TABLE AgentTechnique CASCADE;
TRUNCATE TABLE AgentCommercial CASCADE;
TRUNCATE TABLE SocieteEntretien CASCADE;
TRUNCATE TABLE AssocAgenceSocieteEntretien CASCADE;
TRUNCATE TABLE Entretien CASCADE;
TRUNCATE TABLE Option CASCADE;
TRUNCATE TABLE TypeCarburant CASCADE;
TRUNCATE TABLE Marque CASCADE;
TRUNCATE TABLE CategorieVehicule CASCADE;
TRUNCATE TABLE Modele CASCADE;
TRUNCATE TABLE Vehicule CASCADE;
TRUNCATE TABLE Location CASCADE;
TRUNCATE TABLE Particulier CASCADE;
TRUNCATE TABLE LocationParticulier CASCADE;
TRUNCATE TABLE Entreprise CASCADE;
TRUNCATE TABLE Conducteur CASCADE;
TRUNCATE TABLE LocationProfessionnel CASCADE;
TRUNCATE TABLE Facturation CASCADE;
TRUNCATE TABLE ValidationFinale CASCADE;

-- Cas où l'on veut supprimer toute la base de données et toutes ses données

-- DROP DATABASE NF18LocationVehicule;