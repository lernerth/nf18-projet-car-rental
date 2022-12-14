--------------------
CREATE TABLE Agence(
  id_agence SERIAL PRIMARY KEY,
  nom VARCHAR,
  adresse VARCHAR,
  siret VARCHAR(14),
  mail VARCHAR,
  telephone VARCHAR(10),
  CONSTRAINT check_mel CHECK(mail SIMILAR TO '([a-zA-Z0-9.]+)@([a-zA-Z0-9]+).([a-zA-Z0-9]+)'),
  CONSTRAINT check_tel CHECK(telephone SIMILAR TO '[0-9]{10}'),
  CONSTRAINT check_siret CHECK(siret SIMILAR TO '[0-9]{14}')
);

CREATE TABLE Employe(
  id_employe SERIAL PRIMARY KEY,
  nom VARCHAR,
  prenom VARCHAR,
  agence INTEGER REFERENCES Agence(id_agence)
);


CREATE TABLE AgentTechnique(
  id_employe INTEGER REFERENCES Employe(id_employe) PRIMARY KEY
);


CREATE TABLE AgentCommercial(
  id_employe INTEGER REFERENCES Employe(id_employe) PRIMARY KEY
);


CREATE TABLE SocieteEntretien(
  siret VARCHAR(14) PRIMARY KEY,
  nom VARCHAR,
  CONSTRAINT check_siret CHECK(siret SIMILAR TO '[0-9]{14}')
);


CREATE TABLE AssocAgenceSocieteEntretien(
  id_agence INTEGER REFERENCES Agence(id_agence),
  siret VARCHAR(14) REFERENCES SocieteEntretien(siret),
  PRIMARY KEY(id_agence, siret)
);

-- CREATE TYPE Resultat_entretien AS ENUM('Tres bon etat', 'Bon etat', 'Etat correct', 'Mauvais etat');

CREATE TABLE Entretien(
  id_entretien SERIAL PRIMARY KEY,
  date_entretien DATE,
  date_controle DATE,
  resultat VARCHAR,
  societe VARCHAR(14) REFERENCES SocieteEntretien(siret) NOT NULL,
  agent_tech INTEGER REFERENCES AgentTechnique(id_employe) NOT NULL
);


CREATE TABLE Particulier(
  id_client SERIAL PRIMARY KEY,
  nom VARCHAR NOT NULL,
  prenom VARCHAR NOT NULL,
  num_bancaire VARCHAR NOT NULL,
  mail VARCHAR NOT NULL,
  telephone VARCHAR(10) NOT NULL,
  adresse VARCHAR,
  num_permis VARCHAR(9) UNIQUE NOT NULL,
  date_naissance DATE NOT NULL,
  CONSTRAINT check_age check(AGE(date_naissance) >= INTERVAL '21 years'),
  CONSTRAINT check_tel CHECK(telephone SIMILAR TO '[0-9]{10}'),
  CONSTRAINT check_mail CHECK(mail SIMILAR TO '([a-zA-Z0-9.]+)@([a-zA-Z0-9]+).([a-zA-Z0-9]+)'),
  CONSTRAINT check_num_permis CHECK(num_permis SIMILAR TO '[0-9A-Z]{9}'),
  CONSTRAINT num_bancaire CHECK(num_bancaire SIMILAR TO '[0-9]{16}')
);


CREATE TABLE Entreprise(
  id_client SERIAL PRIMARY KEY,
  nom VARCHAR NOT NULL,
  num_bancaire VARCHAR NOT NULL,
  mail VARCHAR NOT NULL,
  tel VARCHAR NOT NULL,
  adresse VARCHAR,
  siret VARCHAR(14) NOT NULL,
  CONSTRAINT check_tel CHECK(tel SIMILAR TO '[0-9]{10}'),
  CONSTRAINT check_mail CHECK(mail SIMILAR TO '([a-zA-Z0-9.]+)@([a-zA-Z0-9]+).([a-zA-Z0-9]+)'),
  CONSTRAINT num_bancaire CHECK(num_bancaire SIMILAR TO '[0-9]{16}'),
  CONSTRAINT check_siret CHECK(siret SIMILAR TO '[0-9]{14}')
);


CREATE TABLE Conducteur(
  num_permis VARCHAR PRIMARY KEY,
  nom VARCHAR NOT NULL,
  prenom VARCHAR NOT NULL,
  date_naissance DATE NOT NULL,
  entreprise INTEGER NOT NULL,
  CONSTRAINT fk_entreprise FOREIGN KEY(entreprise) REFERENCES Entreprise(id_client),
  CONSTRAINT check_age check(AGE(date_naissance) >= INTERVAL '21 years'),
  CONSTRAINT check_num_permis CHECK(num_permis SIMILAR TO '[0-9A-Z]{9}')
);


CREATE TABLE Facturation(
  idFacturation SERIAL PRIMARY KEY,
  clientParticulier INTEGER REFERENCES Particulier(id_client),
  clientProfessionnel INTEGER REFERENCES Entreprise(id_client),
  agent_com INTEGER NOT NULL,
  montant MONEY,
  date_payement DATE,
  moyen_reglement VARCHAR,
  etat_payement BOOLEAN NOT NULL,
  FOREIGN KEY(agent_com) REFERENCES AgentCommercial(id_employe)
);


CREATE TABLE TypeCarburant(
  nom VARCHAR PRIMARY KEY
);


CREATE TABLE Vehicule(
  immat VARCHAR(7) UNIQUE,
  modele JSON,
  liste_options JSON,
  carburant VARCHAR NOT NULL,
  couleur VARCHAR NOT NULL,
  nb_km DECIMAL NOT NULL,
  agence INTEGER NOT NULL,
  agent_tech INTEGER,
  PRIMARY KEY(immat),
  FOREIGN KEY(carburant) REFERENCES TYPECARBURANT(nom),
  FOREIGN KEY(agence) REFERENCES AGENCE(id_agence),
  FOREIGN KEY(agent_tech) REFERENCES AGENTTECHNIQUE(id_employe),
  CONSTRAINT check_immat CHECK(immat SIMILAR TO '[0-9A-Z]{7}')
);


CREATE TABLE Location(
  id_contrat SERIAL PRIMARY KEY,
  date_debut DATE NOT NULL,
  date_fin DATE,
  km_parcourus DECIMAL NOT NULL,
  vehicule_immat VARCHAR(7) NOT NULL,
  entretien INTEGER UNIQUE NOT NULL,
  facturation INTEGER NOT NULL,
  agent_com INTEGER NOT NULL,
  validation_finale JSON,
  FOREIGN KEY(vehicule_immat) REFERENCES Vehicule(immat),
  FOREIGN KEY(entretien) REFERENCES Entretien(id_entretien),
  FOREIGN KEY(facturation) REFERENCES Facturation(idFacturation),
  FOREIGN KEY(agent_com) REFERENCES AgentCommercial(id_employe)
);


CREATE TABLE LocationParticulier(
  id_contrat INTEGER REFERENCES Location(id_contrat) ON DELETE CASCADE,
  particulier INTEGER NOT NULL,
  FOREIGN KEY(particulier) REFERENCES Particulier(id_client),
  PRIMARY KEY(id_contrat)
);


CREATE TABLE LocationProfessionnel(
  id_contrat INTEGER REFERENCES Location(id_contrat) ON DELETE CASCADE,
  conducteur VARCHAR(13) NOT NULL,
  FOREIGN KEY(conducteur) REFERENCES Conducteur(num_permis),
  PRIMARY KEY(id_contrat)
);