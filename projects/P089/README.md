# P089: Rifiuti disegnati: una pipeline di visione sintetica

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P089/README.md) · [Registro del collaudo](../../collaudo/P089/registro.json)

**Sezione:** [Sezione 9: IoT e simulazione di sistemi](../../docs/CATALOGO.md#sezione-9-iot-e-simulazione-di-sistemi).

**Argomenti:** Intelligenza artificiale · Visione artificiale · Immagini sintetiche.

Classifica rappresentazioni sintetiche di rifiuti senza usare fotografie di materiali reali.

Tutti i comandi partono dalla cartella `projects/P089`. I blocchi seguenti usano la sintassi di Linux/Bash.

## Requisiti e versioni

Linguaggio: Python.

- Python 3.12 o 3.13 come riferimento verificato
- Python 3.12.14 (collaudo Linux storico)
- Python 3.12.15 (Ubuntu/Linux, GitHub Actions, 22 ottobre 2026)
- Python 3.13.16 (Ubuntu/Linux, GitHub Actions, 22 ottobre 2026)
- Python 3.12.10 (Windows Server 2025, GitHub Actions, 22 ottobre 2026)
- Python 3.13.16 (Windows Server 2025, GitHub Actions, 22 ottobre 2026)

Dipendenze:

- NumPy 2.3.5
- scikit-learn 1.8.0
- SciPy 1.17.0
- joblib 1.5.3
- threadpoolctl 3.6.0
- Pillow 12.3.0

## Preparazione

Comandi per una shell Linux/Bash dalla cartella projects/P089. Installare Python 3.12 prima della preparazione; dopo l’attivazione, python indica l’interprete dell’ambiente virtuale .venv. Riattivare l’ambiente in ogni nuovo terminale. Le versioni indicate descrivono gli ambienti documentati, non un minimo universale. Test verificati sui runner Ubuntu di GitHub Actions con Python 3.12.15 e 3.13.16 il 22 ottobre 2026.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
python -m pip install -r ../../requirements-p081-p100.txt
```

## Avvio

```bash
python src/cv_waste_synthetic.py
```

## Test

```bash
python run_tests.py
```

## Perimetro del laboratorio

- Il file requirements-p081-p100.txt prepara l’ambiente condiviso del gruppo: può includere pacchetti usati da altri progetti.
- Nessun servizio o hardware per demo e test. L’installazione iniziale dei pacchetti richiede accesso al repository dei pacchetti o una copia locale delle dipendenze.

## Windows

Test eseguiti nativamente sui runner GitHub Actions Windows Server 2025 con Python 3.12.10 e 3.13.16, il 22 ottobre 2026. WSL non è necessario per questo laboratorio. L’esito attesta gli ambienti dei runner e i casi provati; non garantisce ogni configurazione Windows. Evidenza pubblica: [run 39699184959](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39699184959).

Per la parte Python nativa, dal **Prompt dei comandi (cmd.exe)**, nella cartella del progetto:

```bat
py -3.12 -m venv .venv
.venv\Scripts\activate.bat
```

Dopo l’attivazione, usare i comandi `python` di installazione, avvio e test indicati sopra. In alternativa, anche da PowerShell, invocare direttamente `.\.venv\Scripts\python.exe` al posto di `python`: non serve attivare script né cambiare la policy di esecuzione. Il comando di attivazione Bash non va copiato in PowerShell.

## Collaudi documentati

Il 21 ottobre 2026 erano documentati i collaudi Linux con Python 3.12.14, 3.12.15 e 3.13.16. Il 22 ottobre 2026, nel [run pubblico 39699184959](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39699184959) sul commit `711f91b76ea819e2e57a400ad33c98afda3b6e62`, i 18 metodi di test di questo progetto sono passati in tutti e quattro i job: Ubuntu/Linux con Python 3.12.15 e 3.13.16; Windows Server 2025 con Python 3.12.10 e 3.13.16. Ogni job ha superato complessivamente 377 metodi per P081–P100 senza test saltati o errori, ha verificato la compilazione sintattica di 60 file Python e l’integrità di 289 file tramite hash. Il controllo degli hash comprende i sorgenti degli altri progetti, ma i test del run riguardano soltanto P081–P100.

Queste istruzioni sono state ricavate dai file e dai collaudi conservati. La preparazione dei README non ha eseguito nuove suite né modificato il codice.
