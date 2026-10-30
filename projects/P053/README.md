# P053: Simulare FIFO, LRU e Clock per le pagine

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P053/README.md) · [Registro del collaudo](../../collaudo/P053/registro.json)

**Sezione:** [Sezione 5: Sistemi operativi](../../docs/CATALOGO.md#sezione-5-sistemi-operativi).

**Argomenti:** Sistemi operativi · Memoria virtuale · Sostituzione delle pagine.

Confronta FIFO, LRU e Clock contando le richieste di pagine assenti dalla memoria simulata, dette page fault. Quando la memoria è piena, i tre algoritmi scelgono in modo diverso quale pagina sostituire.

Apri un terminale nella cartella `projects/P053` ed esegui da lì tutti i comandi. Gli esempi usano Linux e Bash; per Windows, segui anche la sezione dedicata.

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

I test confrontano i conteggi dei page fault. La seconda suite verifica 400 sequenze con implementazioni di riferimento. Se i controlli passano, stampano messaggi `PASS`.

```bash
python tests/test_p053.py
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
