# P002: Analisi dei consumi domestici da CSV

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P002/README.md) · [Registro del collaudo](../../collaudo/P002/registro.json)

Elabora consumi memorizzati in CSV e verifica i risultati su dati di prova.

Tutti i comandi partono dalla cartella `projects/P002`. I blocchi seguenti usano la sintassi di Linux/Bash.

## Requisiti e versioni

Linguaggio: Python.

- Python 3.12.x; collaudo storico con 3.12.14

Dipendenze:

- Libreria standard di Python

## Preparazione

Comandi per una shell Linux/Bash dalla cartella projects/P002. Installare Python 3.12 prima della preparazione; dopo l’attivazione, python indica l’interprete dell’ambiente virtuale .venv. Riattivare l’ambiente in ogni nuovo terminale. Le versioni indicate descrivono gli ambienti documentati, non un minimo universale.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
```

## Avvio

Non è presente un’applicazione dimostrativa autonoma: usare i test sotto come punto di ingresso eseguibile.

## Test

```bash
python tests/test_p002.py
```

## Perimetro del laboratorio

- Il file in src definisce funzioni o classi; non contiene un programma interattivo né un punto di avvio dimostrativo. La suite di test è il punto di ingresso eseguibile.

## Windows

Windows nativo plausibile con Python 3.12 e comando python disponibile; i test usano pathlib per localizzare src. Bash e WSL non necessari per questi comandi. Compatibilità dedotta dai file, non collaudata su Windows. Nessun test Windows nativo è attestato da questo README.

Per la parte Python nativa, dal **Prompt dei comandi (cmd.exe)**, nella cartella del progetto:

```bat
py -3.12 -m venv .venv
.venv\Scripts\activate.bat
```

Dopo l’attivazione, usare i comandi `python` di installazione, avvio e test indicati sopra. In alternativa, anche da PowerShell, invocare direttamente `.\.venv\Scripts\python.exe` al posto di `python`: non serve attivare script né cambiare la policy di esecuzione. Il comando di attivazione Bash non va copiato in PowerShell.

## Collaudi documentati

Collaudo storico su Linux: le suite disponibili e i casi aggiuntivi risultano superati. Il riepilogo del gruppo P001–P040 non riporta una data puntuale; questi risultati non sono stati rieseguiti per preparare il README.

Queste istruzioni sono state ricavate dai file e dai collaudi conservati. La preparazione dei README non ha eseguito nuove suite né modificato il codice.
