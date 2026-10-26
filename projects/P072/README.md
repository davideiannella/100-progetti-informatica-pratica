# P072: Mini-SOC: trasformare log sintetici in alert verificabili

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../COLLAUDO/P072/README.md) · [Registro del collaudo](../../COLLAUDO/P072/registro.json)

Analizza e correla log sintetici per produrre avvisi spiegabili.

Tutti i comandi partono dalla cartella `projects/P072`. I blocchi seguenti usano la sintassi di Linux/Bash.

## Requisiti e versioni

Linguaggio: Python.

- Python 3.12.14 (ambiente documentato)

Dipendenze:

- Libreria standard Python; nessun pacchetto pip aggiuntivo.

## Preparazione

Comandi per una shell Linux/Bash dalla cartella projects/P072. Installare Python 3.12 prima della preparazione; dopo l’attivazione, python indica l’interprete dell’ambiente virtuale .venv. Riattivare l’ambiente in ogni nuovo terminale. Le versioni indicate descrivono gli ambienti documentati, non un minimo universale.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
```

## Avvio

```bash
python -B src/mini_soc.py
```

## Esempio documentale

Riproduce i log sintetici, la normalizzazione e gli avvisi degli esempi. Dalla cartella `projects/P072`, con l’ambiente Python preparato:

```bash
python -B worked_example.py
```

## Test

```bash
python -B run_tests.py
```

## Perimetro del laboratorio

- shlex.split(..., posix=True) descrive la grammatica delle stringhe analizzate, non richiede un sistema operativo POSIX.

## Windows

Windows: Sorgente e test usano librerie Python e percorsi pathlib, senza dipendenze da comandi Unix o privilegi di amministratore rilevate nella lettura statica. Nessun test Windows nativo è attestato da questo README.

Per la parte Python nativa, dal **Prompt dei comandi (cmd.exe)**, nella cartella del progetto:

```bat
py -3.12 -m venv .venv
.venv\Scripts\activate.bat
```

Dopo l’attivazione, usare i comandi `python` di installazione, avvio e test indicati sopra. In alternativa, anche da PowerShell, invocare direttamente `.\.venv\Scripts\python.exe` al posto di `python`: non serve attivare script né cambiare la policy di esecuzione. Il comando di attivazione Bash non va copiato in PowerShell.

## Collaudi documentati

Documentazione del 18 ottobre 2026: demo ed esempi acquisiti con l’ambiente indicato; suite congelata di 111 metodi unittest già verificata. Nessuna suite è stata rieseguita per preparare questo README.

Queste istruzioni sono state ricavate dai file e dai collaudi conservati. La preparazione dei README non ha eseguito nuove suite né modificato il codice.
