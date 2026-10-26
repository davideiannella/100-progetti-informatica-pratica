# P061: Capire se un servizio sta bene: log, metriche e alert

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P061/README.md) · [Registro del collaudo](../../collaudo/P061/registro.json)

**Sezione:** [Sezione 6: Cloud e affidabilità dei servizi](../../docs/CATALOGO.md#sezione-6-cloud-e-affidabilità-dei-servizi).

**Argomenti:** Osservabilità · Metriche · Affidabilità dei servizi.

Aggrega richieste sintetiche in indicatori di disponibilità, latenza e allarme.

Tutti i comandi partono dalla cartella `projects/P061`. I blocchi seguenti usano la sintassi di Linux/Bash.

## Requisiti e versioni

Linguaggio: Python.

- Python 3.12.14 (ambiente documentato)

Dipendenze:

- Libreria standard Python; nessun pacchetto pip aggiuntivo.

## Preparazione

Comandi per una shell Linux/Bash dalla cartella projects/P061. Installare Python 3.12 prima della preparazione; dopo l’attivazione, python indica l’interprete dell’ambiente virtuale .venv. Riattivare l’ambiente in ogni nuovo terminale. Le versioni indicate descrivono gli ambienti documentati, non un minimo universale.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
```

## Avvio

```bash
python src/observability.py
```

## Test

```bash
python run_tests.py
```

## Windows

Windows: Sorgente e test usano librerie Python e percorsi pathlib, senza dipendenze da comandi Unix o privilegi di amministratore rilevate nella lettura statica. Nessun test Windows nativo è attestato da questo README.

Per la parte Python nativa, dal **Prompt dei comandi (cmd.exe)**, nella cartella del progetto:

```bat
py -3.12 -m venv .venv
.venv\Scripts\activate.bat
```

Dopo l’attivazione, usare i comandi `python` di installazione, avvio e test indicati sopra. In alternativa, anche da PowerShell, invocare direttamente `.\.venv\Scripts\python.exe` al posto di `python`: non serve attivare script né cambiare la policy di esecuzione. Il comando di attivazione Bash non va copiato in PowerShell.

## Collaudi documentati

Documentazione del 18 ottobre 2026: demo ed esempi acquisiti con l’ambiente indicato; suite congelata di 9 metodi unittest già verificata. Nessuna suite è stata rieseguita per preparare questo README.

Queste istruzioni sono state ricavate dai file e dai collaudi conservati. La preparazione dei README non ha eseguito nuove suite né modificato il codice.
