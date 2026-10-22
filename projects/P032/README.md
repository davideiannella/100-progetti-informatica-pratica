# P032 — Grafo di mobilità urbana

Rappresenta collegamenti di mobilità in Python e include un esempio Cypher separato.

Tutti i comandi partono dalla cartella `projects/P032`. I blocchi seguenti usano la sintassi di Linux/Bash.

## Requisiti e versioni

Linguaggio: Python / Cypher.

- Python 3.12.14
- Neo4j 5.26.0

Dipendenze:

- Libreria standard Python; nessun pacchetto esterno per i test presenti.
- Per cypher/mobility.cypher soltanto: server Neo4j e client Cypher. Nessun driver Neo4j importato dal modello Python.

## Preparazione

Comandi per una shell Linux/Bash dalla cartella projects/P032. Installare Python 3.12 prima della preparazione; dopo l’attivazione, python indica l’interprete dell’ambiente virtuale .venv. Riattivare l’ambiente in ogni nuovo terminale. Le versioni indicate descrivono gli ambienti documentati, non un minimo universale.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
```

## Avvio

Non è presente un’applicazione dimostrativa autonoma: usare i test sotto come punto di ingresso eseguibile.

## Test

```bash
python tests/test_p032.py
```

## Perimetro del laboratorio

- Il test Python non esegue Cypher; le verifiche sui due livelli sono separate. Comando e configurazione client non ricostruibili dal log sintetico.

## Windows

API Python portabili e pathlib; nessun comando Bash o requisito POSIX rilevato. python deve indicare l’interprete scelto. Compatibilità dedotta dal codice, non collaudata su Windows. Per Neo4j serve separatamente un motore/client compatibile o un server raggiungibile; il modello Python non impone WSL. Nessun test Windows nativo è attestato da questo README.

Per la parte Python nativa, dal **Prompt dei comandi (cmd.exe)**, nella cartella del progetto:

```bat
py -3.12 -m venv .venv
.venv\Scripts\activate.bat
```

Dopo l’attivazione, usare i comandi `python` di installazione, avvio e test indicati sopra. In alternativa, anche da PowerShell, invocare direttamente `.\.venv\Scripts\python.exe` al posto di `python`: non serve attivare script né cambiare la policy di esecuzione. Il comando di attivazione Bash non va copiato in PowerShell.

## Collaudi documentati

Collaudo storico su Linux: le suite disponibili e i casi aggiuntivi risultano superati. Il riepilogo del gruppo P001–P040 non riporta una data puntuale; questi risultati non sono stati rieseguiti per preparare il README. Le prove del modello Python e quelle del motore di database sono evidenze separate.

Queste istruzioni sono state ricavate dai file e dai collaudi conservati. La preparazione dei README non ha eseguito nuove suite né modificato il codice.
