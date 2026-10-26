# P033: Analisi delle vendite con uno schema a stella

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P033/README.md) · [Registro del collaudo](../../collaudo/P033/registro.json)

**Sezione:** [Sezione 2: Database e gestione dei dati](../../docs/CATALOGO.md#sezione-2-database-e-gestione-dei-dati).

**Argomenti:** Data warehouse · Analisi dei dati.

Esamina vendite mediante un database con schema a stella.

Tutti i comandi partono dalla cartella `projects/P033`. I blocchi seguenti usano la sintassi di Linux/Bash.

## Requisiti e versioni

Linguaggio: SQL (SQLite) / Python per il collaudo.

- Python 3.12.14
- SQLite 3.53.1

Dipendenze:

- Python con modulo standard sqlite3 funzionante; database dei test in memoria.
- File della sottocartella sql, mantenendo la struttura del progetto.

## Preparazione

Comandi per una shell Linux/Bash dalla cartella projects/P033. Installare Python 3.12 prima della preparazione; dopo l’attivazione, python indica l’interprete dell’ambiente virtuale .venv. Riattivare l’ambiente in ogni nuovo terminale. Le versioni indicate descrivono gli ambienti documentati, non un minimo universale.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
```

## Avvio

Non è presente un’applicazione dimostrativa autonoma: usare i test sotto come punto di ingresso eseguibile.

## Test

```bash
python tests/test_p033.py
```

## Windows

API Python portabili e pathlib; nessun comando Bash o requisito POSIX rilevato. python deve indicare l’interprete scelto. Compatibilità dedotta dal codice, non collaudata su Windows. Nessun test Windows nativo è attestato da questo README.

Per la parte Python nativa, dal **Prompt dei comandi (cmd.exe)**, nella cartella del progetto:

```bat
py -3.12 -m venv .venv
.venv\Scripts\activate.bat
```

Dopo l’attivazione, usare i comandi `python` di installazione, avvio e test indicati sopra. In alternativa, anche da PowerShell, invocare direttamente `.\.venv\Scripts\python.exe` al posto di `python`: non serve attivare script né cambiare la policy di esecuzione. Il comando di attivazione Bash non va copiato in PowerShell.

## Collaudi documentati

Collaudo storico su Linux: le suite disponibili e i casi aggiuntivi risultano superati. Il riepilogo del gruppo P001–P040 non riporta una data puntuale; questi risultati non sono stati rieseguiti per preparare il README.

Queste istruzioni sono state ricavate dai file e dai collaudi conservati. La preparazione dei README non ha eseguito nuove suite né modificato il codice.
