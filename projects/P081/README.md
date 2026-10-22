# P081 — Prompt injection: annotare i documenti senza attribuire loro autorità

Annota contenuti documentali potenzialmente ostili senza trasformarli in istruzioni.

Tutti i comandi partono dalla cartella `projects/P081`. I blocchi seguenti usano la sintassi di Linux/Bash.

## Requisiti e versioni

Linguaggio: Python.

- Python 3.12 o 3.13 come riferimento verificato
- Python 3.12.14 (collaudo Linux storico)
- Python 3.12.15 (collaudo Linux storico)
- Python 3.13.16 (collaudo Linux storico)

Dipendenze:

- Libreria standard di Python

## Preparazione

Comandi per una shell Linux/Bash dalla cartella projects/P081. Installare Python 3.12 prima della preparazione; dopo l’attivazione, python indica l’interprete dell’ambiente virtuale .venv. Riattivare l’ambiente in ogni nuovo terminale. Le versioni indicate descrivono gli ambienti documentati, non un minimo universale.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
```

## Avvio

```bash
python src/rag_guard.py
```

## Test

```bash
python run_tests.py
```

## Perimetro del laboratorio

- Nessuna rete, credenziale, periferica o servizio esterno richiesto per demo e test.

## Windows

Windows nativo plausibile in base ai sorgenti e ai test Python, che non richiedono Bash, /proc o API POSIX. Questa valutazione statica non equivale a un collaudo sul sistema. Nessun test Windows nativo è attestato da questo README.

Per la parte Python nativa, dal **Prompt dei comandi (cmd.exe)**, nella cartella del progetto:

```bat
py -3.12 -m venv .venv
.venv\Scripts\activate.bat
```

Dopo l’attivazione, usare i comandi `python` di installazione, avvio e test indicati sopra. In alternativa, anche da PowerShell, invocare direttamente `.\.venv\Scripts\python.exe` al posto di `python`: non serve attivare script né cambiare la policy di esecuzione. Il comando di attivazione Bash non va copiato in PowerShell.

## Collaudi documentati

Collaudi del 21 ottobre 2026: 14 metodi di test del progetto superati su Linux con Python 3.12.14, su Ubuntu in GitHub Actions con Python 3.12.15 e con Python 3.13.16. Sono risultati storici distinti da un collaudo Windows. Nessuna suite è stata rieseguita per preparare questo README.

Queste istruzioni sono state ricavate dai file e dai collaudi conservati. La preparazione dei README non ha eseguito nuove suite né modificato il codice.
