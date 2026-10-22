# P076 — Consigliare corsi in base agli interessi: recommender system

Ordina corsi per similarità coseno fra vettori assegnati manualmente.

Tutti i comandi partono dalla cartella `projects/P076`. I blocchi seguenti usano la sintassi di Linux/Bash.

## Requisiti e versioni

Linguaggio: Python.

- Python 3.12.14 (ambiente documentato)
- numpy 2.3.5 (ambiente documentato)

Dipendenze:

- numpy 2.3.5 — Array e calcoli numerici; dipendenza diretta di sorgente e/o test.

## Preparazione

Comandi per una shell Linux/Bash dalla cartella projects/P076. Installare Python 3.12 prima della preparazione; dopo l’attivazione, python indica l’interprete dell’ambiente virtuale .venv. Riattivare l’ambiente in ogni nuovo terminale. Le versioni indicate descrivono gli ambienti documentati, non un minimo universale.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
python -m pip install -r ../../requirements-p061-p080.txt
```

## Avvio

```bash
python -B src/recommender.py
```

## Test

```bash
python -B run_tests.py
```

## Perimetro del laboratorio

- Il README registra anche scikit-learn 1.8.0 nell’ambiente comune, ma src/recommender.py, run_tests.py e tests/test_p076.py non lo importano: non è una dipendenza diretta di questo progetto.
- Il file requirements-p061-p080.txt prepara l’ambiente condiviso del gruppo: comprende anche pacchetti non importati direttamente da questo singolo progetto.

## Windows

Windows: Nativo plausibile con Python 3.12 e pacchetti numerici compatibili installati. Il progetto lavora su array, dati sintetici e file locali, senza richiamare strumenti Unix; la riproduzione numerica puntuale resta legata alle versioni registrate. Nessun test Windows nativo è attestato da questo README.

Per la parte Python nativa, dal **Prompt dei comandi (cmd.exe)**, nella cartella del progetto:

```bat
py -3.12 -m venv .venv
.venv\Scripts\activate.bat
```

Dopo l’attivazione, usare i comandi `python` di installazione, avvio e test indicati sopra. In alternativa, anche da PowerShell, invocare direttamente `.\.venv\Scripts\python.exe` al posto di `python`: non serve attivare script né cambiare la policy di esecuzione. Il comando di attivazione Bash non va copiato in PowerShell.

## Collaudi documentati

Documentazione del 18 ottobre 2026: demo ed esempi acquisiti con l’ambiente indicato; suite congelata di 112 metodi unittest già verificata. Nessuna suite è stata rieseguita per preparare questo README.

Queste istruzioni sono state ricavate dai file e dai collaudi conservati. La preparazione dei README non ha eseguito nuove suite né modificato il codice.
