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
('Charles','Renard', '1111 2222 0000 3333', 'charlesrenard@live.fr', '0678607898','19AW24696', '03/07/2000'),
('Louis','Barre', '1111 7777 0000 3333', 'louisbarre@live.fr', '0679907898','19AW28896', '03/08/2001');
INSERT INTO LocationParticulier(id_contrat, particulier ) VALUES
(1,1),
(2,3);

INSERT INTO Entreprise(nom,num_bancaire,mail,tel,siret) VALUES 

('Nike','1234111122223333','nike@gmail.com','0646734566','11122294112344'),

('Zumbacafew','2223133356778444','zbc.jul@gmail.com','0744532458','33523256623454'),

('Popelop','2236654467553332','popelop@wanadoo.fr','0623443355','66665545544567'),

('Tchikita','4466443277664344','tchiki.tchiki@orange.fr','0677665454','33455566547654'),
('Machine de A','5544644433234444','quedescracks@gmail.com','0788665644','00322274431467');

INSERT INTO Conducteur(num_permis, nom, prenom, date_naissance, entreprise) VALUES 
	('182640728375', 'Dubois', 'Paul', 19/10/1970, 'Nike'),
	('183946253046', 'Dupont', 'Etienne', 23/01/1986, 'Popelop'),
	('039527393527', 'Sombrero', 'Antony', 06/05/1976, 'Popelop'),
	('103846389847', 'Geigberg', 'David', 12/12/1992, 'ZumbaCafew'),
	('109372573296', 'Oui-Oui', 'Medhi', 25/12/1994, 'Tchikita');

LocationProfessionnel

INSERT INTO Facturation(idfacturation, clientParticulier, clientProfessionel, agent_com,
                        montant, date_payment, moyen_reglement, etat_payement) 
        VALUES  (1, NULL, '182640728375', 1, 1200, '12-09-2020', 'CB',     TRUE), 
                (2, NULL, '039527393527', 2, 1500, '12-10-2020', 'CB',     TRUE),
                (3, 1,    NULL,           1, 1000, '12-01-2021', 'paypal', TRUE);

INSERT INTO ValidationFinale(agent_com, location, date_validation, resultat_validation)
        VALUES  (1, 1, '15-1-2021', TRUE),
                (1, 1, '13-1-2021', TRUE),
                (2, 1, '14-1-2021', TRUE);

INSERT INTO Entretien(identretien, date_entretien, date_controle, 
                        resultat, societe, agent_tech)
        VALUES  (1, '20-01-2021', '21-01-2021', 'abc', '36252187900034', 1),
                (2, '20-02-2021', '21-03-2021', 'xyz', '55252187900021', 2),
                (3, '20-03-2021', '21-05-2021', 'xyz', '36252187900034', 1);