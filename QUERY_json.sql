-- 

SELECT v.nom, opt.* -- permet d' afficher toute les options pour un même véhicule
FROM Vehicule v, JSON_ARRAY_ELEMENTS(v.option) opt;
