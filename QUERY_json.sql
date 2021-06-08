-- 

SELECT v.immat, opt.* -- permet d' afficher toute les options pour un même véhicule
FROM Vehicule v, JSON_ARRAY_ELEMENTS(v.option) opt;

-- trouver la catégorie d un véhicule
SELECT CAST(v.immat,v.modele->categorie->>"nom" AS VARCHAR) AS categorie,CAST(v.modele->categorie->>"description" AS VARCHAR) AS description
FROM Vehicule v;

-- trouver le modele d un véhicule
SELECT CAST(v.immat,v.modele->>"nom" AS VARCHAR) AS modele,CAST(v.modele->>"nb_portes" AS VARCHAR) AS nbre_portes
FROM Vehicule v;
