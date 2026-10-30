# P037: API REST per trasporto pubblico

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P037/README.md) · [Registro del collaudo](../../collaudo/P037/registro.json)

**Sezione:** [Sezione 3: Ingegneria e progettazione del software](../../docs/CATALOGO.md#sezione-3-ingegneria-e-progettazione-del-software).

**Argomenti:** Progettazione del software · API REST.

Leggi fermate e tempi di arrivo tramite un’API locale e invii avvisi riferiti a una fermata. Il prototipo controlla i dati ricevuti e restituisce le risposte HTTP, ma non salva gli avvisi in un archivio permanente.

Apri un terminale nella cartella `projects/P037` ed esegui da lì i comandi. I blocchi seguenti usano la sintassi di Linux/Bash; per Windows consulta la sezione dedicata.

## Requisiti e versioni

**Tecnologie utilizzate:** Python · FastAPI · Pydantic · HTTPX · Uvicorn.

- Python 3.12.14

Dipendenze:

- FastAPI e Pydantic importati da src/app.py.
- HTTPX per TestClient e dipendenze transitive compatibili FastAPI/Starlette.
- Uvicorn per il server ASGI; non viene avviato dal test TestClient.

Il progetto non fissa le versioni dei pacchetti esterni. Il comando di installazione può quindi ottenere versioni diverse da quelle del collaudo storico: dopo l’installazione, esegui il test per verificare la combinazione disponibile.

## Preparazione

Installa Python 3.12, poi crea e attiva l’ambiente virtuale con i comandi seguenti. Dopo l’attivazione, `python` usa l’interprete dell’ambiente `.venv`. Riattiva l’ambiente ogni volta che apri un nuovo terminale. Le versioni elencate descrivono gli ambienti documentati: non sono necessariamente le versioni minime richieste.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
python -m pip install fastapi httpx uvicorn
```

## Avvio

```bash
python -m uvicorn app:app --app-dir src --host 127.0.0.1 --port 8000
```

Il servizio resta attivo nel terminale. Aprine un altro per eseguire i controlli; per arrestare il servizio, premi `Ctrl+C` nel terminale in cui lo hai avviato.

## Test

Il test controlla lo stato del servizio, fermate, arrivi e invio degli avvisi. Verifica anche le risposte 400 e 404 nei casi previsti e stampa `PASS` se i controlli riescono.

```bash
python tests/test_p037.py
```

## Perimetro del laboratorio

- Nella cartella del progetto non sono presenti un file `requirements.txt` né un elenco di versioni fissate. Il log sintetico P037 non riporta le versioni esatte delle dipendenze.
- Il log P037 contiene un avviso di deprecazione Starlette/HTTPX: segnala un’interfaccia il cui uso è sconsigliato e che potrebbe essere rimossa in futuro. In quella prova il test è riuscito; l’esito non garantisce la compatibilità di combinazioni future.

## Windows

Il codice non richiede Bash o funzioni specifiche di Linux e può essere eseguito su Windows con pacchetti compatibili. Le loro versioni non sono fissate dal progetto; i collaudi documentati in questa pagina non comprendono una prova nativa su Windows.

Per preparare Python su Windows, apri il **Prompt dei comandi (cmd.exe)** nella cartella del progetto ed esegui:

```bat
py -3.12 -m venv .venv
.venv\Scripts\activate.bat
```

Dopo l’attivazione, esegui i comandi `python` di installazione, avvio e test indicati sopra. In alternativa, anche da PowerShell, usa direttamente `.\.venv\Scripts\python.exe` al posto di `python`: non devi attivare script né cambiare le regole di esecuzione di PowerShell. Non copiare in PowerShell il comando di attivazione Bash.

## Collaudi documentati

**Ultimo collaudo: 30 ottobre 2026 — superato.** Le verifiche del progetto sono riuscite su Ubuntu 24.04 nel [collaudo pubblico P001–P080](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/41134634700), eseguito sul commit `35b49f130493`.

### Prove precedenti

Nel [collaudo del 22 ottobre 2026](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701), le verifiche della versione di allora sono riuscite su Ubuntu 24.04.

Consulta **Output verificati** e **Registro del collaudo**, all’inizio della pagina, per leggere comandi, ambiente e limiti di ciascuna prova. I risultati documentati descrivono quei collaudi; per verificare la copia che stai usando, esegui i test sul tuo computer.
