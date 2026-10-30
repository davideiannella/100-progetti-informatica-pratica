# P049: Trasferire file con frame e controllo di integrità

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P049/README.md) · [Registro del collaudo](../../collaudo/P049/registro.json)

**Sezione:** [Sezione 4: Reti di calcolatori](../../docs/CATALOGO.md#sezione-4-reti-di-calcolatori).

**Argomenti:** Reti · Protocolli · Integrità dei dati.

Verifica trasferimenti locali con frame e controllo dell’integrità.

Apri un terminale nella cartella `projects/P049` ed esegui da lì tutti i comandi. Gli esempi usano Linux e Bash; per Windows, segui anche la sezione dedicata.

## Requisiti e versioni

**Tecnologie utilizzate:** Python · socket · struct · hashlib.

- Python 3.12.14 (collaudo locale storico)

Dipendenze:

- Libreria standard Python con Python 3.12.14 — socket, threading, hashlib, json, struct

## Preparazione

Installa Python 3.12, poi esegui questi comandi nella cartella del progetto. L’ambiente virtuale `.venv` tiene separate le dipendenze del laboratorio; dopo l’attivazione, `python` usa l’interprete di questo ambiente. Riattivalo ogni volta che apri un nuovo terminale. Le versioni indicate descrivono i collaudi documentati e non sono necessariamente le versioni minime richieste.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
```

## Avvio

Esegui i comandi della sezione Test per provare il laboratorio. I test richiamano il codice e verificano i risultati; non c’è un’applicazione dimostrativa separata.

## Test

I test verificano la ricostruzione dei dati, anche quando arrivano in più parti, e il rifiuto di nomi, dimensioni o impronte non validi. Se i controlli passano, stampano messaggi `PASS`.

```bash
python tests/test_p049.py
python tests/test_edges.py
```

## Perimetro del laboratorio

- Esegui i comandi dalla cartella del progetto. I test mostrano come usare il codice e controllano i risultati dei casi previsti.

## Windows

I test usano `socket.socketpair`, che crea due socket collegati, e thread per eseguire invio e ricezione in parallelo. Puoi provarli con Python 3.12 su Windows senza script Bash; il comportamento dei socket su Windows non è stato verificato nelle prove documentate.

Per la parte Python, apri il **Prompt dei comandi (cmd.exe)** nella cartella del progetto ed esegui:

```bat
py -3.12 -m venv .venv
.venv\Scripts\activate.bat
```

Dopo l’attivazione, usa i comandi `python` di installazione, avvio e test indicati sopra. In alternativa, anche da PowerShell, sostituisci `python` con `.\.venv\Scripts\python.exe`: in questo caso non serve attivare script o modificare le regole di esecuzione di PowerShell. Non copiare il comando di attivazione Bash in PowerShell.

## Collaudi documentati

Collaudo storico del 2026-10-16: Test locali registrati.

Queste istruzioni sono state ricavate dai file e dai collaudi conservati.
