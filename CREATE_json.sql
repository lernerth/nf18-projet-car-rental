-- 

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
