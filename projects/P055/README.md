# P055: Collegare Web API e database con Compose

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P055/README.md) · [Registro del collaudo](../../collaudo/P055/registro.json)

**Sezione:** [Sezione 6: Cloud e affidabilità dei servizi](../../docs/CATALOGO.md#sezione-6-cloud-e-affidabilità-dei-servizi).

**Argomenti:** Cloud e container · API web · Database.

Avvia insieme NGINX, un’API e PostgreSQL tramite Docker Compose. Il progetto include anche un esercizio SQLite locale, separato dai servizi in container.

Apri un terminale nella cartella `projects/P055` ed esegui da lì tutti i comandi. Gli esempi usano Linux e Bash; per Windows, segui anche la sezione dedicata.

## Requisiti e versioni

**Tecnologie utilizzate:** Python · FastAPI · Docker Compose · NGINX · PostgreSQL · SQLite.

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

Installa Python 3.12, poi esegui questi comandi nella cartella del progetto. L’ambiente virtuale `.venv` tiene separate le dipendenze del laboratorio; dopo l’attivazione, `python` usa l’interprete di questo ambiente. Riattivalo ogni volta che apri un nuovo terminale. Le versioni indicate descrivono i collaudi documentati e non sono necessariamente le versioni minime richieste.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-test.txt
```

## Avvio

```bash
docker compose up --build
```

I servizi restano attivi nel terminale. Apri un altro terminale per i controlli oppure interrompi l’esecuzione con `Ctrl+C`.

## Test

```bash
python tests/test_p055.py
```

Questo comando verifica il modello SQLite e la configurazione Compose. Per controllare anche PostgreSQL occorre avviare e provare i servizi in container.

## Perimetro del laboratorio

- Il test Python controlla SQLite e i file di configurazione Compose. L’avvio completo richiede Docker con container Linux e Compose. I risultati del collaudo PostgreSQL sono documentati separatamente.

## Windows

Le immagini `nginx:1.28-alpine`, `postgres:17-alpine` e `python:3.12-slim` richiedono container Linux. Su Windows puoi usare, per esempio, Docker Desktop con WSL2, l’ambiente Linux di Windows. Il collaudo documentato riguarda i servizi in Linux e non dimostra un’esecuzione nativa su Windows.

Per la parte Python, apri il **Prompt dei comandi (cmd.exe)** nella cartella del progetto ed esegui:

```bat
py -3.12 -m venv .venv
.venv\Scripts\activate.bat
```

Dopo l’attivazione, usa i comandi `python` di installazione, avvio e test indicati sopra. In alternativa, anche da PowerShell, sostituisci `python` con `.\.venv\Scripts\python.exe`: in questo caso non serve attivare script o modificare le regole di esecuzione di PowerShell. Non copiare il comando di attivazione Bash in PowerShell.

## Collaudi documentati

**Ultimo collaudo: 31 ottobre 2026 — superato.** Le verifiche del progetto sono riuscite su Ubuntu 24.04 nel [collaudo pubblico P001–P080](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/41142475728), eseguito sul commit `c8303920c4f4`.

### Prove precedenti

Collaudo storico del 2026-10-16/17: Suite SQLite/configurazione locale; stack Nginx–API–PostgreSQL riuscito su GitHub Actions, persistenza dopo riavvio API e DB.

Queste istruzioni sono state ricavate dai file e dai collaudi conservati.
