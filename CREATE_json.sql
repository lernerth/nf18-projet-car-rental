-- 

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
