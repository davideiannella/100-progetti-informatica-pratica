# P051: Confrontare FCFS, SJF e Round Robin

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P051/README.md) · [Registro del collaudo](../../collaudo/P051/registro.json)

**Sezione:** [Sezione 5: Sistemi operativi](../../docs/CATALOGO.md#sezione-5-sistemi-operativi).

**Argomenti:** Sistemi operativi · Scheduling.

Confronta tre regole per assegnare il processore ai processi: FCFS, SJF e Round Robin. Il modello permette di osservare come cambiano le attese quando cambia l’ordine di esecuzione.

Apri un terminale nella cartella `projects/P051` ed esegui da lì tutti i comandi. Gli esempi usano Linux e Bash; per Windows, segui anche la sezione dedicata.

## Requisiti e versioni

**Tecnologie utilizzate:** Python.

- Python 3.12.14 (collaudo locale storico)

Dipendenze:

- Libreria standard Python con Python 3.12.14 — collections, random

## Preparazione

Installa Python 3.12, poi esegui questi comandi nella cartella del progetto. L’ambiente virtuale `.venv` tiene separate le dipendenze del laboratorio; dopo l’attivazione, `python` usa l’interprete di questo ambiente. Riattivalo ogni volta che apri un nuovo terminale. Le versioni indicate descrivono i collaudi documentati e non sono necessariamente le versioni minime richieste.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
```

## Avvio

Esegui i comandi della sezione Test per provare il laboratorio. I test richiamano il codice e verificano i risultati; non c’è un’applicazione dimostrativa separata.

## Test

I test confrontano attese e completamenti con i risultati previsti. La seconda suite confronta anche 250 casi con una simulazione indipendente. Se i controlli passano, stampano messaggi `PASS`.

```bash
python tests/test_p051.py
python tests/test_reference.py
```

## Perimetro del laboratorio

- Esegui i comandi dalla cartella del progetto. I test mostrano come usare il codice e controllano i risultati dei casi previsti.

## Windows

Il codice usa Python e librerie multipiattaforma, senza script Bash nel progetto. Per provare il laboratorio su Windows, prepara l’ambiente con i passaggi seguenti. L’esecuzione nativa su Windows non è stata collaudata nelle prove documentate.

Per la parte Python, apri il **Prompt dei comandi (cmd.exe)** nella cartella del progetto ed esegui:

```bat
py -3.12 -m venv .venv
.venv\Scripts\activate.bat
```

Dopo l’attivazione, usa i comandi `python` di installazione, avvio e test indicati sopra. In alternativa, anche da PowerShell, sostituisci `python` con `.\.venv\Scripts\python.exe`: in questo caso non serve attivare script o modificare le regole di esecuzione di PowerShell. Non copiare il comando di attivazione Bash in PowerShell.

## Collaudi documentati

**Ultimo collaudo: 31 ottobre 2026 — superato.** Le verifiche del progetto sono riuscite su Ubuntu 24.04 nel [collaudo pubblico P001–P080](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/41142475728), eseguito sul commit `c8303920c4f4`.

### Prove precedenti

Collaudo storico del 2026-10-16: Test locali registrati.

Queste istruzioni sono state ricavate dai file e dai collaudi conservati.
