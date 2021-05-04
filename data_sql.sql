INSERT INTO Agence (nom)
VALUES
('RENTACAR');

INSERT INTO Employe (nom, prenom, agence)
VALUES 
('Durocher', 'Violette', 1),
('Nguyen', 'Bang', 1),
('Lerner', 'Thomas', 1),
('Redouin', 'Noe', 1),
('Tki', 'JeanMich', 1);

INSERT INTO AgentTechnique 
VALUES 
(1),(2);

INSERT INTO AgentCommercial
VALUES
(3),(4);

INSERT INTO SocieteEntretien 
VALUES 
(36252187900034, 'Carglass'),
(55252187900021, 'EpongeOmax');

INSERT INTO AssocAgenceSocieteEntretien 
VALUES 
(1,36252187900034),
(1,55252187900021); 

INSERT INTO Option
VALUES
('GPS'),('AC'),('Start and Stop');

INSERT INTO TypeCarburant
VALUES 
('essence'),('gasoil'), ('sans plomb95'), ('sans plomb98');

INSERT INTO Marque
VALUES 
('Peugeot'),('Chevrolet'),('Renault'),('Citroën'),('Volkswagen'),('Ford'),('Toyota');

INSERT INTO CategorieVehicule
VALUES
('Citadine'), ('Berline'), ('berline petite'), ('berline moyenne'), ('berline grande'), ('4X4 SUV'), ('Pickup'), ('utilitaire');

INSERT INTO Modele (nom, marque, categorie)
VALUES
('twingo', 'Renault', 'Citadine'),
('spark', 'Chevrolet', 'Citadine'),
('golf', 'Volkswagen', 'Berline'),
('clio', 'Renault', 'Citadine'),
('208', 'Peugeot', 'Citadine');

INSERT INTO Vehicule (immat,modele,carburant,couleur,nb_km,agence,agent_tech)
VALUES
('AA123AA', '208', 'essence', 'bleu', 3000, 1, 1),
('BB123BB', '208', 'sans plomb98', 'gris', 100, 1, 1),
('CC123CC', 'clio', 'sans plomb95', 'rouge', 25000, 1, 2),
('DD123DD', 'clio', 'essence', 'blanc', 400, 1, 2),
('EE123EE', 'clio', 'essence', 'rouge', 5000, 1, 2),
('FF123FF', 'twingo', 'essence', 'noir', 12000, 1, 2),
('GG123GG', 'golf', 'essence', 'noir', 1200, 1, 1),
('HH123HH', 'golf', 'gasoil', 'gris', 4000, 1, 2);

INSERT INTO Location(date_debut ,date_fin,km_parcourus,vehicule_immat,entretien ,facturation ) VALUES 
('05/08/2020', '12/12/2020',3000,'AA123AA', 1,2),
('07/03/2020', '06/01/2021',400,'DD123DD', 2,1),
('07/03/2020', '06/01/2021',4000,'HH123HH', 3,2);


INSERT INTO Particulier(nom,prenom,num_bancaire,mail ,telephone, adresse ,num_permis, date_naissance) VALUES
('Albert','Pinot', '0000 1111 2222 3333', 'albertpinot@gmail.com', '0695605788','20AW24096', '07/07/1998'),
('Charles','Renard', '1111 2222 0000 3333', 'charlesrenard@live.fr', '0678607898','19AW24696', '03/07/2000');
LocationParticulier
Entreprise
Conducteur
LocationProfessionnel
Facturation
ValidationFinale
Entretien