# P055 — Collegare Web API e database con Compose

Affianca un esercizio SQLite locale a uno stack Web–API–PostgreSQL in container.

Tutti i comandi partono dalla cartella `projects/P055`. I blocchi seguenti usano la sintassi di Linux/Bash.

## Requisiti e versioni

Linguaggio: Python / SQL / YAML / Docker Compose.

- Python 3.12.14 (collaudo locale storico)
- Python nel container API 3.12-slim (configurato e collaudato)
- PostgreSQL 17.11 osservata; tag postgres:17-alpine (collaudo runtime storico)
- Nginx 1.28-alpine (configurato e avviato nel collaudo storico)
- Docker Engine / Compose 28.0.4 / 2.38.2 (collaudo runtime storico)

Dipendenze:

- FastAPI 0.143.2 — API nel container
- Pydantic 2.14.1 — Validazione input
- Uvicorn 0.54.0 — Server API
- psycopg[binary] 3.3.6 — Accesso PostgreSQL
- PyYAML 6.0.3 — Lettura compose.yaml nella suite locale; assente da api/requirements.txt.
- sqlite3 libreria standard Python — Esercizio locale separato dal database PostgreSQL del Compose.

## Preparazione

Comandi per una shell Linux/Bash dalla cartella projects/P055. Installare Python 3.12 prima della preparazione; dopo l’attivazione, python indica l’interprete dell’ambiente virtuale .venv. Riattivare l’ambiente in ogni nuovo terminale. Le versioni indicate descrivono gli ambienti documentati, non un minimo universale.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-test.txt
```

## Avvio

```bash
docker compose up --build
```

L’avvio del servizio resta in primo piano. Usare un altro terminale per i controlli oppure interrompere con `Ctrl+C`.

## Test

```bash
python tests/test_p055.py
```

La suite Python verifica il modello SQLite e la configurazione Compose; non sostituisce una prova dello stack PostgreSQL in esecuzione.

## Perimetro del laboratorio

- Il test Python prova SQLite e la struttura Compose. L’avvio completo richiede Docker con container Linux e Compose; il collaudo PostgreSQL è un’evidenza separata dal test Python.

## Windows

Le immagini nginx:1.28-alpine, postgres:17-alpine e python:3.12-slim sono Linux. Non attribuire il collaudo Linux a Windows nativo. I container e il cluster richiedono un motore Linux: su Windows usare, per esempio, Docker Desktop con backend WSL2; questo non costituisce un collaudo Windows nativo. Nessun test Windows nativo è attestato da questo README.

Per la parte Python nativa, dal **Prompt dei comandi (cmd.exe)**, nella cartella del progetto:

```bat
py -3.12 -m venv .venv
.venv\Scripts\activate.bat
```

Dopo l’attivazione, usare i comandi `python` di installazione, avvio e test indicati sopra. In alternativa, anche da PowerShell, invocare direttamente `.\.venv\Scripts\python.exe` al posto di `python`: non serve attivare script né cambiare la policy di esecuzione. Il comando di attivazione Bash non va copiato in PowerShell.

## Collaudi documentati

Collaudo storico del 2026-10-16/17: Suite SQLite/configurazione locale; stack Nginx–API–PostgreSQL riuscito su GitHub Actions, persistenza dopo riavvio API e DB. Nessuna suite rieseguita per questo README.

Queste istruzioni sono state ricavate dai file e dai collaudi conservati. La preparazione dei README non ha eseguito nuove suite né modificato il codice.
