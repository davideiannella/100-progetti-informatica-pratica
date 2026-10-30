# Strumenti di collaudo

[Pagina principale](../README.md) · [Risultati P001–P100](../collaudo/README.md)

Questi strumenti coordinano le verifiche automatiche. Per provare un singolo laboratorio, segui prima il README nella sua cartella `projects/Pnnn`.

Per controllare i collegamenti interni dalla cartella principale esegui `python tools/check_links.py`. Il controllo segnala percorsi e sezioni mancanti.

| Strumento | Funzione |
|---|---|
| [Controllo collegamenti](check_links.py) | Verifica che i file e le sezioni collegate esistano, senza eseguire i laboratori |
| [Script P001–P040](ci_p001_p040/runner.py) | Suite dei progetti e controlli dei motori database |
| [Script P041–P080](ci_p041_p080/runner.py) | Suite e dimostrazioni locali del gruppo |
| [Script P081–P100](collaudo_p081_p100.py) | Suite Python, controllo delle impronte e raccolta degli output |

I programmi che avviano più test sono chiamati anche runner. Le loro configurazioni sono nei [workflow](../.github/workflows). Gli ambienti e i risultati delle esecuzioni documentate sono riportati nei registri di collaudo.
