-- 

SELECT v.immat, opt.* -- permet d' afficher toute les options pour un même véhicule
FROM Vehicule v, JSON_ARRAY_ELEMENTS(v.liste_options) opt;

-- trouver la catégorie d un véhicule
SELECT v.immat, CAST (v.modele->'categorie'->>'nom' AS VARCHAR) AS categorie, CAST(v.modele->'categorie'->>'description' AS VARCHAR) AS description
FROM Vehicule v;

-- trouver le modele d un véhicule
SELECT v.immat, CAST(v.modele->>'nom' AS VARCHAR) AS modele, CAST(v.modele->>'nb_portes' AS INTEGER) AS nbre_portes
FROM Vehicule v;
