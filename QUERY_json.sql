-- 

SELECT v.immat, opt.* -- permet d' afficher toute les options pour un même véhicule
FROM Vehicule v, JSON_ARRAY_ELEMENTS(v.option) opt;

-- trouver la catégorie d un véhicule
SELECT CAST(v.immat,v.modele->categorie->>"nom" AS VARCHAR) AS categorie,CAST(v.modele->categorie->>"description" AS VARCHAR) AS description
FROM Vehicule v;
