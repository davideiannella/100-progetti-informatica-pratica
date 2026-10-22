-- Imprese con comune e provincia
SELECT i.RagioneSociale,c.Nome AS Comune,p.Nome AS Provincia
FROM Impresa i JOIN Comune c ON c.CodiceComune=i.CodiceComune
JOIN Provincia p ON p.CodiceProvincia=c.CodiceProvincia
ORDER BY p.Nome,c.Nome,i.RagioneSociale;

-- Numero imprese per provincia
SELECT p.Nome, COUNT(*) AS NumeroImprese
FROM Provincia p JOIN Comune c ON c.CodiceProvincia=p.CodiceProvincia
JOIN Impresa i ON i.CodiceComune=c.CodiceComune
GROUP BY p.CodiceProvincia,p.Nome ORDER BY NumeroImprese DESC;
