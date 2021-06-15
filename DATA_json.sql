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

INSERT INTO TypeCarburant
VALUES
('essence'),('gasoil'), ('sans plomb95'), ('sans plomb98');

INSERT INTO Vehicule (immat, modele, liste_options, carburant, couleur, nb_km, agence, agent_tech)
VALUES (
'AA123AA',
'{"nom":"C4", "nb_portes":4, "marque":{"nom":"citroen"},
	"categorie":{"nom":"berline", "description":"voiture de ville"}}',
'["climatisation","limiteur de vitesse","sieges massants"]',
'essence',
'bleu',
3000,
1,
2
);

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



INSERT INTO Entretien(societe, agent_tech)
VALUES  
('36252187900034', 2);

INSERT INTO Location (date_debut, date_fin, km_parcourus, vehicule_immat, entretien, facturation, agent_com, validation_finale)
VALUES (
	'2021-09-18',
	'2022-01-02',
	1004,
	'AA123AA',
	1,
	1,
	3,
	'{"date":"2021-06-15", "resultat":TRUE}'
);
INSERT INTO LocationParticulier(id_contrat, particulier) 
VALUES
(1,1);
