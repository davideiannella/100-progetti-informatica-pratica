# Revisione dei progetti del 31 ottobre 2026

[Pagina principale](../README.md) · [Catalogo](CATALOGO.md) · [Registri dei collaudi](../collaudo/README.md)

Questa revisione completa il [controllo del 30 ottobre](REVISIONE_2026_10_30.md). Corregge quattro casi con numeri molto grandi, aggiunge i test corrispondenti e allinea il testo del Kindle ai sorgenti.

## Correzioni e test

| Progetto | Comportamento corretto |
|---|---|
| [P001](../projects/P001/README.md) | La media delle attese usa `statistics.mean`: due attese pari a `1e308` danno una media pari a `1e308`, senza una somma intermedia infinita. |
| [P002](../projects/P002/README.md) | La media dei consumi usa `statistics.mean`: letture finite molto grandi producono una media valida senza un errore nella somma intermedia. |
| [P006](../projects/P006/README.md) | Una destinazione irraggiungibile resta distinta da un percorso il cui costo minimo supera il limite numerico. Un percorso alternativo con costo finito viene ancora considerato. |
| [P012](../projects/P012/README.md) | Se una combinazione caricabile supera il limite del valore totale, il programma segnala `OverflowError` e non restituisce una scelta basata su valori infiniti. |

Per P006 e P012, il limite dei totali è quello dei numeri `float` di Python, indicato da `sys.float_info.max`; vale anche quando i dati sono interi. Le istruzioni dei progetti spiegano questo limite. I nuovi test verificano gli errori individuati, le alternative valide e i casi ordinari. Le medie sono state confrontate anche con un riferimento razionale; percorsi e zaini con un confronto indipendente delle possibili soluzioni.

## Chiarezza delle istruzioni

P008 ora precisa che la soglia viene raggiunta **o superata**, in accordo con il confronto `>=`. P038 e P039 riportano la versione Java registrata nel collaudo del 22 ottobre: Temurin 17.0.20.1+1.

Nel Kindle, tutte le cento sezioni «Soluzione ragionata» sono in riquadro. I quattro sorgenti corretti e le relative spiegazioni sono aggiornati. In P080 la descrizione dei test parla di «soglie», evitando di attribuire alla suite una prova specifica dell'uguaglianza che non contiene.

## Collaudi eseguiti

Le esecuzioni riguardano il commit `c8303920c4f49daa20e31e4466d3869a97174124`:

- [P001–P080](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/41142475728): cinque job riusciti su Ubuntu, inclusi i database e i container previsti dai progetti.
- [P081–P100](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/41142475640): quattro job riusciti, su Ubuntu e Windows con Python 3.12 e 3.13.

La data è il **31 ottobre 2026**, nel fuso italiano `Europe/Rome`. Gli orari originali UTC e gli esiti dei singoli job sono nel [registro di questa verifica](COLLAUDO_2026_10_31.json). I sorgenti, i test e il manifest non cambiano nell'aggiornamento successivo delle sole date e dei collegamenti.

I risultati precedenti conservano la loro data e i loro conteggi. I nuovi test possono aumentare il numero delle verifiche rispetto agli output storici del libro. Per ripetere le prove, segui i comandi nel README del progetto.

I controlli coprono i casi e gli ambienti documentati. L'anteprima del Kindle convertita da Amazon va verificata prima della pubblicazione.
