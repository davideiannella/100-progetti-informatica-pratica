# P060 — Pipeline CI con test e integrità della release

Esegue test e costruisce una release locale; include un esempio di workflow CI.

Tutti i comandi partono dalla cartella `projects/P060`. I blocchi seguenti usano la sintassi di Linux/Bash.

## Requisiti e versioni

Linguaggio: Python / GitHub Actions YAML.

- Python 3.12.14 (collaudo locale storico)
- Python nel workflow 3.13 (configurato, non eseguito su GitHub Actions)

Dipendenze:

- Libreria standard Python con Python 3.12.14 — math, hashlib, json, pathlib, py_compile, zipfile, unittest, subprocess

## Preparazione

Comandi per una shell Linux/Bash dalla cartella projects/P060. Installare Python 3.12 prima della preparazione; dopo l’attivazione, python indica l’interprete dell’ambiente virtuale .venv. Riattivare l’ambiente in ogni nuovo terminale. Le versioni indicate descrivono gli ambienti documentati, non un minimo universale.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
```

## Avvio

```bash
python build_release.py
```

## Test

```bash
python -m unittest discover -s tests -v
```

## Perimetro del laboratorio

- Il workflow in .github/workflows/ci.yml si attiva soltanto quando il contenuto di P060 costituisce la radice di un repository autonomo. La copia annidata in projects/P060 non viene scoperta come workflow dal repository generale. Non sono previsti deployment o pubblicazione degli artefatti.
- Il workflow configura Python 3.13; il collaudo locale documentato usa Python 3.12.14. Il risultato locale non dimostra un’esecuzione remota né identità universale degli archivi fra sistemi operativi.

## Windows

Test e builder usano la libreria standard e sono plausibili su Windows. Il workflow richiede esplicitamente ubuntu-latest, quindi non documenta una build Windows. Non è garantita l’identità dei byte ZIP fra sistemi operativi diversi. Nessun test Windows nativo è attestato da questo README.

Per la parte Python nativa, dal **Prompt dei comandi (cmd.exe)**, nella cartella del progetto:

```bat
py -3.12 -m venv .venv
.venv\Scripts\activate.bat
```

Dopo l’attivazione, usare i comandi `python` di installazione, avvio e test indicati sopra. In alternativa, anche da PowerShell, invocare direttamente `.\.venv\Scripts\python.exe` al posto di `python`: non serve attivare script né cambiare la policy di esecuzione. Il comando di attivazione Bash non va copiato in PowerShell.

## Collaudi documentati

Collaudo storico del 2026-10-16: Test e build locali riusciti; nessuna esecuzione remota del workflow P060 e nessun deploy. Non sono stati eseguiti nuovi test.

Queste istruzioni sono state ricavate dai file e dai collaudi conservati. La preparazione dei README non ha eseguito nuove suite né modificato il codice.
