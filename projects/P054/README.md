# P054: Preparare una release riproducibile di un’API

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../COLLAUDO/P054/README.md) · [Registro del collaudo](../../COLLAUDO/P054/registro.json)

Avvia un’API locale e costruisce un archivio di rilascio verificabile.

Tutti i comandi partono dalla cartella `projects/P054`. I blocchi seguenti usano la sintassi di Linux/Bash.

## Requisiti e versioni

Linguaggio: Python / FastAPI / Dockerfile.

- Python 3.12.14 (collaudo locale storico)
- Python nel container 3.13-slim (immagine base configurata e collaudata)
- Docker Engine 28.0.4 (collaudo runtime storico)

Dipendenze:

- FastAPI 0.143.2 — API
- Pydantic 2.14.1 — Validazione input
- Uvicorn 0.54.0 — Server ASGI
- httpx 0.28.1 — Dipendenza del TestClient usato da tests/test_http.py; presente nell’ambiente storico ma non nel requirements.txt del progetto.

## Preparazione

Comandi per una shell Linux/Bash dalla cartella projects/P054. Installare Python 3.12 prima della preparazione; dopo l’attivazione, python indica l’interprete dell’ambiente virtuale .venv. Riattivare l’ambiente in ogni nuovo terminale. Le versioni indicate descrivono gli ambienti documentati, non un minimo universale.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-test.txt
```

## Avvio

Avviare l’API; il processo resta in primo piano fino a `Ctrl+C`. La porta 18054 deve essere libera.

```bash
python -m uvicorn src.app:app --host 127.0.0.1 --port 18054
```

La creazione dell’archivio è un comando separato:

```bash
python tools/build_release.py
```

## Test

```bash
python tests/test_app.py
python tests/test_http.py
python tests/test_release_builder.py
python tools/live_http_test.py
```

Il test HTTP reale avvia e arresta Uvicorn: eseguirlo con la porta di prova libera, senza lasciare avviata un’altra copia sulla stessa porta.

## Perimetro del laboratorio

- API locale: installare i requisiti e usare Uvicorn. Dockerfile: immagine Linux, processo appuser, porta 8000. La riproducibilità documentata è quella dello ZIP nel contesto collaudato.
- Il requisito httpx del test va distinto dalle sole dipendenze di avvio dell’API. Le dipendenze transitive non sono bloccate da hash.

## Windows

useradd e la base python:3.13-slim appartengono al container Linux. Nessuno script Bash lato host è necessario per la parte Python. I container e il cluster richiedono un motore Linux: su Windows usare, per esempio, Docker Desktop con backend WSL2; questo non costituisce un collaudo Windows nativo. Nessun test Windows nativo è attestato da questo README.

Per la parte Python nativa, dal **Prompt dei comandi (cmd.exe)**, nella cartella del progetto:

```bat
py -3.12 -m venv .venv
.venv\Scripts\activate.bat
```

Dopo l’attivazione, usare i comandi `python` di installazione, avvio e test indicati sopra. In alternativa, anche da PowerShell, invocare direttamente `.\.venv\Scripts\python.exe` al posto di `python`: non serve attivare script né cambiare la policy di esecuzione. Il comando di attivazione Bash non va copiato in PowerShell.

## Collaudi documentati

Collaudo storico del 2026-10-16/17: Suite e HTTP su loopback locali; build immagine e controlli HTTP Docker riusciti in GitHub Actions. Nessuna nuova esecuzione in questa revisione.

Queste istruzioni sono state ricavate dai file e dai collaudi conservati. La preparazione dei README non ha eseguito nuove suite né modificato il codice.
