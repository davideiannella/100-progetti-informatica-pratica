# P049: Trasferire file con frame e controllo di integrità

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P049/README.md) · [Registro del collaudo](../../collaudo/P049/registro.json)

Verifica trasferimenti locali con frame e controllo dell’integrità.

Tutti i comandi partono dalla cartella `projects/P049`. I blocchi seguenti usano la sintassi di Linux/Bash.

## Requisiti e versioni

Linguaggio: Python.

- Python 3.12.14 (collaudo locale storico)

Dipendenze:

- Libreria standard Python con Python 3.12.14 — socket, threading, hashlib, json, struct

## Preparazione

Comandi per una shell Linux/Bash dalla cartella projects/P049. Installare Python 3.12 prima della preparazione; dopo l’attivazione, python indica l’interprete dell’ambiente virtuale .venv. Riattivare l’ambiente in ogni nuovo terminale. Le versioni indicate descrivono gli ambienti documentati, non un minimo universale.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
```

## Avvio

Non è presente un’applicazione dimostrativa autonoma: usare i test sotto come punto di ingresso eseguibile.

## Test

```bash
python tests/test_p049.py
python tests/test_edges.py
```

## Perimetro del laboratorio

- Eseguire i comandi dalla cartella del progetto. Il modulo contiene funzioni del laboratorio; i test sono il punto di ingresso per l’esecuzione dimostrativa.

## Windows

La suite usa socket.socketpair e thread: l’esecuzione è plausibile con Python 3.12 su Windows, ma la portabilità dei socket non è stata collaudata qui. Nessuno script Bash è richiesto. Nessun test Windows nativo è attestato da questo README.

Per la parte Python nativa, dal **Prompt dei comandi (cmd.exe)**, nella cartella del progetto:

```bat
py -3.12 -m venv .venv
.venv\Scripts\activate.bat
```

Dopo l’attivazione, usare i comandi `python` di installazione, avvio e test indicati sopra. In alternativa, anche da PowerShell, invocare direttamente `.\.venv\Scripts\python.exe` al posto di `python`: non serve attivare script né cambiare la policy di esecuzione. Il comando di attivazione Bash non va copiato in PowerShell.

## Collaudi documentati

Collaudo storico del 2026-10-16: Test locali registrati; nessun nuovo test eseguito durante questa revisione.

Queste istruzioni sono state ricavate dai file e dai collaudi conservati. La preparazione dei README non ha eseguito nuove suite né modificato il codice.
