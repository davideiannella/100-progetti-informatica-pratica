# P054: Preparare una release riproducibile di un’API

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P054/README.md) · [Registro del collaudo](../../collaudo/P054/registro.json)

**Sezione:** [Sezione 6: Cloud e affidabilità dei servizi](../../docs/CATALOGO.md#sezione-6-cloud-e-affidabilità-dei-servizi).

**Argomenti:** Cloud e container · Rilascio del software · API web.

Avvia un’API locale e costruisce un archivio di rilascio verificabile.

Apri un terminale nella cartella `projects/P054` ed esegui da lì tutti i comandi. Gli esempi usano Linux e Bash; per Windows, segui anche la sezione dedicata.

## Requisiti e versioni

**Tecnologie utilizzate:** Python · FastAPI · Docker.

- Python 3.12.14 (collaudo locale storico)
- Python nel container 3.13-slim (immagine base configurata e collaudata)
- Docker Engine 28.0.4 (collaudo runtime storico)

Dipendenze:

- FastAPI 0.143.2 — API
- Pydantic 2.14.1 — Validazione input
- Uvicorn 0.54.0 — Server ASGI
- httpx 0.28.1 — Dipendenza del TestClient usato da tests/test_http.py; presente nell’ambiente storico ma non nel requirements.txt del progetto.

## Preparazione

Installa Python 3.12, poi esegui questi comandi nella cartella del progetto. L’ambiente virtuale `.venv` tiene separate le dipendenze del laboratorio; dopo l’attivazione, `python` usa l’interprete di questo ambiente. Riattivalo ogni volta che apri un nuovo terminale. Le versioni indicate descrivono i collaudi documentati e non sono necessariamente le versioni minime richieste.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-test.txt
```

## Avvio

Avvia l’API con il comando seguente. Il processo resta attivo nel terminale fino a `Ctrl+C`; la porta 18054 deve essere libera.

```bash
python -m uvicorn src.app:app --host 127.0.0.1 --port 18054
```

Per creare separatamente l’archivio di rilascio, esegui:

```bash
python tools/build_release.py
```

## Test

I test controllano l’API, gli input e il pacchetto di rilascio. Le suite `unittest` terminano con `OK` quando i controlli passano; il test `test_http.py` stampa anche un messaggio `PASS`.

```bash
python tests/test_app.py
python tests/test_http.py
python tests/test_release_builder.py
python tools/live_http_test.py
```

L’ultimo comando avvia e arresta Uvicorn ed esegue richieste HTTP reali sul tuo computer. Prima di lanciarlo, arresta eventuali altre copie dell’API che usano la stessa porta.

## Perimetro del laboratorio

- Per avviare l’API locale, installa le dipendenze e usa Uvicorn. Il Dockerfile prepara invece un container Linux che esegue l’API come utente `appuser` sulla porta 8000. La riproducibilità documentata riguarda i byte dello ZIP nelle condizioni collaudate.
- `httpx` serve ai test e non al solo avvio dell’API. Le dipendenze installate indirettamente da altre librerie, dette transitive, non sono fissate tramite impronte hash.

## Windows

La parte Python sul tuo computer non richiede script Bash. Il Dockerfile usa invece `useradd` e la base `python:3.13-slim`, che richiedono container Linux. Su Windows puoi usare, per esempio, Docker Desktop con WSL2, l’ambiente Linux di Windows. Eseguire un container Linux non equivale a collaudare l’applicazione su Windows nativo; questa seconda prova non è documentata qui.

Per la parte Python, apri il **Prompt dei comandi (cmd.exe)** nella cartella del progetto ed esegui:

```bat
py -3.12 -m venv .venv
.venv\Scripts\activate.bat
```

Dopo l’attivazione, usa i comandi `python` di installazione, avvio e test indicati sopra. In alternativa, anche da PowerShell, sostituisci `python` con `.\.venv\Scripts\python.exe`: in questo caso non serve attivare script o modificare le regole di esecuzione di PowerShell. Non copiare il comando di attivazione Bash in PowerShell.

## Collaudi documentati

**Ultimo collaudo: 31 ottobre 2026 — superato.** Le verifiche del progetto sono riuscite su Ubuntu 24.04 nel [collaudo pubblico P001–P080](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/41142475728), eseguito sul commit `c8303920c4f4`.

### Prove precedenti

Collaudo storico del 2026-10-16/17: Suite e HTTP su loopback locali; build immagine e controlli HTTP Docker riusciti in GitHub Actions.

Queste istruzioni sono state ricavate dai file e dai collaudi conservati.
