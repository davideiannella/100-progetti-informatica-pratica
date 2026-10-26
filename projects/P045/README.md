# P045: Pianificare subnet IPv4 per un campus

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../COLLAUDO/P045/README.md) · [Registro del collaudo](../../COLLAUDO/P045/registro.json)

Convalida un piano di sottoreti IPv4 e ne stampa la configurazione didattica.

Tutti i comandi partono dalla cartella `projects/P045`. I blocchi seguenti usano la sintassi di Linux/Bash.

## Requisiti e versioni

Linguaggio: Python.

- Python 3.12.14 (collaudo locale storico)

Dipendenze:

- Libreria standard Python con Python 3.12.14 — dataclasses, ipaddress, typing, unittest

## Preparazione

Comandi per una shell Linux/Bash dalla cartella projects/P045. Installare Python 3.12 prima della preparazione; dopo l’attivazione, python indica l’interprete dell’ambiente virtuale .venv. Riattivare l’ambiente in ogni nuovo terminale. Le versioni indicate descrivono gli ambienti documentati, non un minimo universale.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
```

## Avvio

```bash
python src/network_plan.py
```

## Test

```bash
python tests/test_network_plan.py
```

## Perimetro del laboratorio

- Eseguire i comandi dalla cartella del progetto. Il modulo contiene funzioni del laboratorio; i test sono il punto di ingresso per l’esecuzione dimostrativa.

## Windows

Il codice usa Python e moduli multipiattaforma; non sono presenti script Bash nel progetto. La plausibilità non equivale a un collaudo Windows. Nessun test Windows nativo è attestato da questo README.

Per la parte Python nativa, dal **Prompt dei comandi (cmd.exe)**, nella cartella del progetto:

```bat
py -3.12 -m venv .venv
.venv\Scripts\activate.bat
```

Dopo l’attivazione, usare i comandi `python` di installazione, avvio e test indicati sopra. In alternativa, anche da PowerShell, invocare direttamente `.\.venv\Scripts\python.exe` al posto di `python`: non serve attivare script né cambiare la policy di esecuzione. Il comando di attivazione Bash non va copiato in PowerShell.

## Collaudi documentati

Collaudo storico del 2026-10-16: Test locali registrati; nessun nuovo test eseguito durante questa revisione.

Queste istruzioni sono state ricavate dai file e dai collaudi conservati. La preparazione dei README non ha eseguito nuove suite né modificato il codice.
