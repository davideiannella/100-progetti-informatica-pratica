# P048: Provare TCP e UDP con socket locali

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P048/README.md) · [Registro del collaudo](../../collaudo/P048/registro.json)

**Sezione:** [Sezione 4: Reti di calcolatori](../../docs/CATALOGO.md#sezione-4-reti-di-calcolatori).

**Argomenti:** Reti · Comunicazione TCP e UDP.

Esegue scambi TCP e UDP su socket locali.

Apri un terminale nella cartella `projects/P048` ed esegui da lì tutti i comandi. Gli esempi usano Linux e Bash; per Windows, segui anche la sezione dedicata.

## Requisiti e versioni

**Tecnologie utilizzate:** Python · socket.

- Python 3.12.14 (collaudo locale storico)

Dipendenze:

- Libreria standard Python con Python 3.12.14 — socket, threading

## Preparazione

Installa Python 3.12, poi esegui questi comandi nella cartella del progetto. L’ambiente virtuale `.venv` tiene separate le dipendenze del laboratorio; dopo l’attivazione, `python` usa l’interprete di questo ambiente. Riattivalo ogni volta che apri un nuovo terminale. Le versioni indicate descrivono i collaudi documentati e non sono necessariamente le versioni minime richieste.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
```

## Avvio

Esegui i comandi della sezione Test per provare il laboratorio. I test richiamano il codice e verificano i risultati; non c’è un’applicazione dimostrativa separata.

## Test

I test inviano e ricevono dati sullo stesso computer, anche vuoti o binari, e verificano che tornino identici. Se i controlli passano, stampano messaggi `PASS`.

```bash
python tests/test_p048.py
python tests/test_edges.py
```

## Perimetro del laboratorio

- Esegui i comandi dalla cartella del progetto. I test mostrano come usare il codice e controllano i risultati dei casi previsti.
- Le prove aprono socket IPv4 su `127.0.0.1`, l’indirizzo interno al tuo computer, con porte assegnate dal sistema. Potrebbe essere necessario consentire queste connessioni nel firewall locale. Non vengono eseguite prove su Internet.

## Windows

Il codice usa Python e librerie multipiattaforma, senza script Bash nel progetto. Per provare il laboratorio su Windows, prepara l’ambiente con i passaggi seguenti. L’esecuzione nativa su Windows non è stata collaudata nelle prove documentate.

Per la parte Python, apri il **Prompt dei comandi (cmd.exe)** nella cartella del progetto ed esegui:

```bat
py -3.12 -m venv .venv
.venv\Scripts\activate.bat
```

Dopo l’attivazione, usa i comandi `python` di installazione, avvio e test indicati sopra. In alternativa, anche da PowerShell, sostituisci `python` con `.\.venv\Scripts\python.exe`: in questo caso non serve attivare script o modificare le regole di esecuzione di PowerShell. Non copiare il comando di attivazione Bash in PowerShell.

## Collaudi documentati

Collaudo storico del 2026-10-16: Test locali registrati.

Queste istruzioni sono state ricavate dai file e dai collaudi conservati.
