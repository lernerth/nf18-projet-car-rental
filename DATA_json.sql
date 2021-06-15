--

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
