# P037 — API REST per trasporto pubblico

Espone un’API locale dedicata al trasporto pubblico e ne verifica le risposte.

Tutti i comandi partono dalla cartella `projects/P037`. I blocchi seguenti usano la sintassi di Linux/Bash.

## Requisiti e versioni

Linguaggio: Python.

- Python 3.12.14

Dipendenze:

- FastAPI e Pydantic importati da src/app.py.
- HTTPX per TestClient e dipendenze transitive compatibili FastAPI/Starlette.
- Uvicorn per il server ASGI; non viene avviato dal test TestClient.

Le versioni dei pacchetti esterni non sono fissate nei materiali di questo progetto. Il comando di installazione resta quindi non bloccato a versioni specifiche; non si promette che riproduca esattamente l’ambiente storico.

## Preparazione

Comandi per una shell Linux/Bash dalla cartella projects/P037. Installare Python 3.12 prima della preparazione; dopo l’attivazione, python indica l’interprete dell’ambiente virtuale .venv. Riattivare l’ambiente in ogni nuovo terminale. Le versioni indicate descrivono gli ambienti documentati, non un minimo universale.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
python -m pip install fastapi httpx uvicorn
```

## Avvio

```bash
python -m uvicorn app:app --app-dir src --host 127.0.0.1 --port 8000
```

L’avvio del servizio resta in primo piano. Usare un altro terminale per i controlli oppure interrompere con `Ctrl+C`.

## Test

```bash
python tests/test_p037.py
```

## Perimetro del laboratorio

- Mancano requirements.txt e versioni bloccate nel progetto; il log P037 non registra le versioni esatte delle dipendenze.
- Il log P037 riporta un avviso di deprecazione Starlette/HTTPX con suite superata; non dimostra compatibilità di future combinazioni di versioni.

## Windows

File privi di dipendenze Bash/POSIX; Windows nativo plausibile con dipendenze compatibili, non fissate dal progetto. Nessun collaudo Windows. Nessun test Windows nativo è attestato da questo README.

Per la parte Python nativa, dal **Prompt dei comandi (cmd.exe)**, nella cartella del progetto:

```bat
py -3.12 -m venv .venv
.venv\Scripts\activate.bat
```

Dopo l’attivazione, usare i comandi `python` di installazione, avvio e test indicati sopra. In alternativa, anche da PowerShell, invocare direttamente `.\.venv\Scripts\python.exe` al posto di `python`: non serve attivare script né cambiare la policy di esecuzione. Il comando di attivazione Bash non va copiato in PowerShell.

## Collaudi documentati

Collaudo storico su Linux: le suite disponibili e i casi aggiuntivi risultano superati. Il riepilogo del gruppo P001–P040 non riporta una data puntuale; questi risultati non sono stati rieseguiti per preparare il README.

Queste istruzioni sono state ricavate dai file e dai collaudi conservati. La preparazione dei README non ha eseguito nuove suite né modificato il codice.
