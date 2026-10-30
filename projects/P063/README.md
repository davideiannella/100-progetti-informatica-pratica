# P063: Login sicuro: scrypt, TOTP, blocco dei tentativi e sessioni

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P063/README.md) · [Registro del collaudo](../../collaudo/P063/registro.json)

**Sezione:** [Sezione 7: Sicurezza informatica](../../docs/CATALOGO.md#sezione-7-sicurezza-informatica).

**Argomenti:** Sicurezza · Autenticazione · Gestione delle sessioni.

Il progetto realizza un servizio locale di autenticazione: controlla la password e un codice TOTP, cioè un codice temporaneo, poi gestisce la sessione dell’utente. Include il blocco dei tentativi ripetuti e il rifiuto dei codici già usati.

Apri un terminale nella cartella `projects/P063`. I comandi qui sotto sono scritti per Linux con Bash; per Windows consulta la sezione dedicata.

## Requisiti e versioni

**Tecnologie utilizzate:** Python · SQL · SQLite.

- Python 3.12.14 (ambiente documentato)

Dipendenze:

- Libreria standard Python; nessun pacchetto pip aggiuntivo.

## Preparazione

Installa Python 3.12, poi esegui i comandi qui sotto per creare e attivare un ambiente virtuale dedicato al progetto, nella cartella `.venv`. Dopo l’attivazione, il comando `python` usa questo ambiente. Riattivalo ogni volta che apri un nuovo terminale.

Le versioni elencate sono quelle degli ambienti documentati; non indicano la versione minima compatibile.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
```

## Avvio

Esegui la dimostrazione per confrontare un accesso valido con il riutilizzo dello stesso codice TOTP e osservare la sessione prima e dopo il logout.

```bash
python src/auth_service.py
```

## Test

Esegui i test automatici del progetto:

```bash
python run_tests.py
```

Nel riepilogo, `OK` indica che tutti i test eseguiti sono passati. Il report JSON riporta quanti test sono stati eseguiti e gli eventuali errori o fallimenti.

## Perimetro del laboratorio

- L’installazione di Python deve includere `sqlite3` e la funzione `hashlib.scrypt`, che richiede il supporto OpenSSL. Non servono pacchetti pip aggiuntivi.

## Windows

Su Windows servono Python 3.12, `sqlite3` e il supporto a `hashlib.scrypt` tramite OpenSSL. Non occorrono un server HTTP o un browser. Le prove conservate non documentano un collaudo su Windows nativo.

Apri il **Prompt dei comandi (cmd.exe)** nella cartella del progetto, poi crea e attiva l’ambiente virtuale:

```bat
py -3.12 -m venv .venv
.venv\Scripts\activate.bat
```

Dopo l’attivazione, esegui con `python` i comandi di installazione, avvio e test indicati sopra. Se usi PowerShell, puoi richiamare direttamente `.\.venv\Scripts\python.exe` al posto di `python`: in questo modo non devi attivare script né cambiare la policy di esecuzione. Non copiare in PowerShell il comando di attivazione scritto per Bash.

## Collaudi documentati

La documentazione del 18 ottobre 2026 descrive una suite di 19 metodi di test `unittest`. I collegamenti «Output verificati» e «Registro del collaudo», all’inizio della pagina, riportano risultati, comandi e ambiente delle prove conservate.
