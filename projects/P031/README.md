# P031: Salvare telemetria IoT in MongoDB

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P031/README.md) · [Registro del collaudo](../../collaudo/P031/registro.json)

**Sezione:** [Sezione 2: Database e gestione dei dati](../../docs/CATALOGO.md#sezione-2-database-e-gestione-dei-dati).

**Argomenti:** Database NoSQL · IoT simulato · Telemetria.

Confronta un modello Python di telemetria con esempi MongoDB separati.

Tutti i comandi partono dalla cartella `projects/P031`. I blocchi seguenti usano la sintassi di Linux/Bash.

## Requisiti e versioni

Linguaggio: Python / JavaScript per mongosh.

- Python 3.12.14
- MongoDB 8.0.14

Dipendenze:

- Libreria standard Python; nessun pacchetto esterno per i test presenti.
- Per mongo/telemetry_examples.js soltanto: server MongoDB e client mongosh. Il modello Python non importa driver MongoDB.

## Preparazione

Comandi per una shell Linux/Bash dalla cartella projects/P031. Installare Python 3.12 prima della preparazione; dopo l’attivazione, python indica l’interprete dell’ambiente virtuale .venv. Riattivare l’ambiente in ogni nuovo terminale. Le versioni indicate descrivono gli ambienti documentati, non un minimo universale.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
```

## Avvio

Non è presente un’applicazione dimostrativa autonoma: usare i test sotto come punto di ingresso eseguibile.

## Test

```bash
python tests/test_invalid_metrics.py
python tests/test_p031.py
```

Questi test verificano la validazione delle misure e la costruzione del documento Python. Non richiedono un database e non eseguono `mongo/telemetry_examples.js`: il modello Python e lo script JavaScript sono due percorsi di esecuzione separati. La prova sul database reale è descritta nei collaudi documentati sotto.

## Perimetro del laboratorio

- Distinguere test Python ed esecuzione MongoDB. Il modello Python serializza il timestamp in stringa ISO; lo script mongosh usa BSON Date.
- Versione di mongosh e configurazione server non registrate nel log sintetico.

## Windows

API Python portabili e pathlib; nessun comando Bash o requisito POSIX rilevato. python deve indicare l’interprete scelto. Compatibilità dedotta dal codice, non collaudata su Windows. Per MongoDB serve separatamente un motore/client compatibile o un server raggiungibile; il modello Python non impone WSL. Nessun test Windows nativo è attestato da questo README.

Per la parte Python nativa, dal **Prompt dei comandi (cmd.exe)**, nella cartella del progetto:

```bat
py -3.12 -m venv .venv
.venv\Scripts\activate.bat
```

Dopo l’attivazione, usare i comandi `python` di installazione, avvio e test indicati sopra. In alternativa, anche da PowerShell, invocare direttamente `.\.venv\Scripts\python.exe` al posto di `python`: non serve attivare script né cambiare la policy di esecuzione. Il comando di attivazione Bash non va copiato in PowerShell.

## Collaudi documentati

Collaudo storico su Linux: le suite disponibili e i casi aggiuntivi risultano superati. Il riepilogo del gruppo P001–P040 non riporta una data puntuale; questi risultati non sono stati rieseguiti per preparare il README. Le prove del modello Python e quelle del motore di database sono evidenze separate.

Nel [collaudo automatizzato del 22 ottobre 2026](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701), il runner ha eseguito lo script originale `mongo/telemetry_examples.js` tramite `mongosh` su MongoDB 8.0.14, avviato in un container Docker. Tutte le 12 asserzioni sul database reale sono risultate superate: verificano la versione del motore, l’inserimento, i tipi BSON, l’indice composto e i risultati della query con filtro per dispositivo, ordinamento temporale e limite. Le due suite Python sono state eseguite separatamente. Le evidenze sono nel [registro P031](../../collaudo/P031/registro.json) e nell’[output della prova sul motore](../../collaudo/P031/streams/003_step_3.stdout.txt); la procedura è nella funzione `engine_suite` del [runner](../../tools/ci_p001_p040/runner.py).

La dicitura storica `MongoDB script STATIC QA` nell’output di `test_p031.py` non attesta l’esecuzione dello script: l’esecuzione su MongoDB è documentata separatamente come `engine_suite` nel registro.

Queste istruzioni sono state ricavate dai file e dai collaudi conservati. La preparazione dei README non ha eseguito nuove suite né modificato il codice.
