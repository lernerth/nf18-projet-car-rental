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
(3),(4),(5);

INSERT INTO SocieteEntretien 
VALUES 
('36252187900034', 'Carglass'),
('55252187900021', 'EpongeOmax');

INSERT INTO AssocAgenceSocieteEntretien(id_agence, siret)
VALUES 
(1,'36252187900034'),
(1,'55252187900021'); 

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

INSERT INTO Particulier(nom, prenom, num_bancaire, mail, telephone, num_permis, date_naissance) 
VALUES
('Albert','Pinot', '0000111122223333', 'albertpinot@gmail.com', '0695605788','20AW24096', '07/07/1998'),
('Charles','Renard', '1111222200003333', 'charlesrenard@live.fr', '0678607898','19AW24696', '03/07/1999'),
('Louis','Barre', '1111777700003333', 'louisbarre@live.fr', '0679907898','19AW28896', '03/08/1999');

INSERT INTO Entreprise(nom, num_bancaire, mail, tel, siret) 
VALUES 
('Nike','1234111122223333','nike@gmail.com','0646734566','11122294112344'),
('Zumbacafew','2223133356778444','zbc.jul@gmail.com','0744532458','33523256623454'),
('Popelop','2236654467553332','popelop@wanadoo.fr','0623443355','66665545544567'),
('Tchikita','4466443277664344','tchiki.tchiki@orange.fr','0677665454','33455566547654'),
('Machine de A','5544644433234444','quedescracks@gmail.com','0788665644','00322274431467');

INSERT INTO Conducteur(num_permis, nom, prenom, date_naissance, entreprise) 
VALUES 
('182640721', 'Paul', 'Dubois', '19/10/1970', 1),
('203946253', 'Etienne', 'Dupont', '23/01/1986', 1),
('039527393', 'Antony', 'Sombrero', '06/05/1976', 2),
('103846389', 'David', 'Geigberg', '12/12/1992', 3),
('109372573', 'Medhi',  'Oui-Oui', '25/12/1994', 4);

INSERT INTO Facturation(clientParticulier, clientProfessionnel, agent_com, montant, date_payement, moyen_reglement, etat_payement) 
VALUES  
-- facturations particulier
(1, NULL, 3, 500, '12-09-2019', 'cheque', TRUE), -- Albert Pinot
(3, NULL, 4, 900, NULL, NULL, FALSE), -- Charles Renard
-- facturations professionnel
(NULL, 2, 5, 1200, '02-01-2018', 'CB', TRUE), -- Zumbacafew
(NULL, 3, 5, 1500, '01-02-2021', 'paypal', TRUE), -- Popelop
(NULL, 5, 3, 1500, NULL, NULL, FALSE); -- Machine de A

INSERT INTO Entretien(date_entretien, date_controle, resultat, societe, agent_tech)
VALUES  
('12-09-2019', '15-09-2019', 'Tres bon etat', '36252187900034', 1),
('06/12/2021', NULL, NULL, '55252187900021', 2),
('06/03/2018', '10/03/2018', 'Bon etat', '55252187900021', 2),
('06/03/2018', '10/03/2018', 'Bon etat', '55252187900021', 2),
('06/03/2018', '10/03/2018', 'Etat correct', '55252187900021', 2),
('10/06/2021', NULL, NULL, '55252187900021', 2),
('10/06/2022', NULL, NULL, '36252187900034', 1);

INSERT INTO Location(date_debut, date_fin, km_parcourus, vehicule_immat, entretien, facturation) 
VALUES 
-- locations particulier
('05/08/2019', '12-09-2019', 3000, 'AA123AA', 1,1),
('07/06/2021', '06/12/2021',400,'DD123DD', 2,2),
-- locations professionnel
('02-01-2018', '06/03/2018', 4000, 'HH123HH', 3, 3), -- Zumbacafew
('02-01-2018', '06/03/2018', 4000, 'GG123GG', 4, 3), -- Zumbacafew
('02-01-2018', '06/03/2018', 4000, 'GG123GG', 5, 3), -- Zumbacafew
('01-02-2021', '10/06/2021', 300, 'GG123GG', 6, 4), -- Popelop
('08/04/2022', '10/06/2022', 600, 'GG123GG', 7, 5); -- Machine de A

INSERT INTO LocationParticulier(id_contrat, particulier) 
VALUES
(1,1),
(2,3);

INSERT INTO LocationProfessionnel(id_contrat, conducteur)
VALUES 
(3,'182640721'),
(4,'203946253'),
(5,'039527393'),
(6,'103846389'),
(7,'109372573');

INSERT INTO ValidationFinale(agent_com, location, date_validation, resultat_validation)
VALUES  
(3, 1, '15-1-2021', TRUE),
(3, 2, '13-1-2021', TRUE),
(4, 3, '14-1-2021', TRUE);


