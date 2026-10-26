# P075: Scoprire transazioni insolite con anomaly detection

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P075/README.md) · [Registro del collaudo](../../collaudo/P075/registro.json)

Misura anomalie e falsi positivi su gruppi numerici generati dal programma.

Tutti i comandi partono dalla cartella `projects/P075`. I blocchi seguenti usano la sintassi di Linux/Bash.

## Requisiti e versioni

Linguaggio: Python.

- Python 3.12.14 (ambiente documentato)
- numpy 2.3.5 (ambiente documentato)
- scikit-learn 1.8.0 (ambiente documentato)

Dipendenze:

- numpy 2.3.5 — Array e calcoli numerici; dipendenza diretta di sorgente e/o test.
- scikit-learn 1.8.0 — Modelli, trasformazioni o metriche importati dal progetto.

## Preparazione

Comandi per una shell Linux/Bash dalla cartella projects/P075. Installare Python 3.12 prima della preparazione; dopo l’attivazione, python indica l’interprete dell’ambiente virtuale .venv. Riattivare l’ambiente in ogni nuovo terminale. Le versioni indicate descrivono gli ambienti documentati, non un minimo universale.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
python -m pip install -r ../../requirements-p061-p080.txt
```

## Avvio

```bash
python -B src/anomaly.py
```

## Esempio documentale

Stampa il primo caso di anomalia, il confronto fra valori di contamination e le metriche dell’esercizio. Dalla cartella `projects/P075`, con l’ambiente Python preparato:

```bash
python -B examples.py
```

## Test

```bash
python -B run_tests.py
```

## Perimetro del laboratorio

- Le dipendenze transitive di scikit-learn vanno installate con il pacchetto; la loro versione non è riportata nei registri qui citati.
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

Documentazione del 18 ottobre 2026: demo ed esempi acquisiti con l’ambiente indicato; suite congelata di 110 metodi unittest già verificata. Nessuna suite è stata rieseguita per preparare questo README.

Queste istruzioni sono state ricavate dai file e dai collaudi conservati. La preparazione dei README non ha eseguito nuove suite né modificato il codice.
