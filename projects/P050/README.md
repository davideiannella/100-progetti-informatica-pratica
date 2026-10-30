# P050: Stimare gli access point di un magazzino

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P050/README.md) · [Registro del collaudo](../../collaudo/P050/registro.json)

**Sezione:** [Sezione 4: Reti di calcolatori](../../docs/CATALOGO.md#sezione-4-reti-di-calcolatori).

**Argomenti:** Reti wireless · Pianificazione della capacità.

Calcola una stima didattica degli access point necessari a un magazzino.

Apri un terminale nella cartella `projects/P050` ed esegui da lì tutti i comandi. Gli esempi usano Linux e Bash; per Windows, segui anche la sezione dedicata.

## Requisiti e versioni

**Tecnologie utilizzate:** Python.

- Python 3.12.14 (collaudo locale storico)

Dipendenze:

- Libreria standard Python con Python 3.12.14 — dataclasses

## Preparazione

Installa Python 3.12, poi esegui questi comandi nella cartella del progetto. L’ambiente virtuale `.venv` tiene separate le dipendenze del laboratorio; dopo l’attivazione, `python` usa l’interprete di questo ambiente. Riattivalo ogni volta che apri un nuovo terminale. Le versioni indicate descrivono i collaudi documentati e non sono necessariamente le versioni minime richieste.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
```

## Avvio

Esegui i comandi della sezione Test per provare il laboratorio. I test richiamano il codice e verificano i risultati; non c’è un’applicazione dimostrativa separata.

## Test

I test controllano l’arrotondamento, il piano delle quattro zone, i canali e il rifiuto di input non validi. Se i controlli passano, stampano un messaggio `PASS`.

```bash
python tests/test_p050.py
```

## Perimetro del laboratorio

- Esegui i comandi dalla cartella del progetto. I test mostrano come usare il codice e controllano i risultati dei casi previsti.
- Il numero di dispositivi e l’obiettivo di dispositivi per access point devono essere interi positivi. Valori decimali, booleani e non finiti sono rifiutati; una zona vuota va esclusa dal piano. Il risultato è una stima di capacità, senza misure di copertura o interferenze radio.

## Windows

Il codice usa Python e librerie multipiattaforma, senza script Bash nel progetto. Per provare il laboratorio su Windows, prepara l’ambiente con i passaggi seguenti. L’esecuzione nativa su Windows non è stata collaudata nelle prove documentate.

Per la parte Python, apri il **Prompt dei comandi (cmd.exe)** nella cartella del progetto ed esegui:

```bat
py -3.12 -m venv .venv
.venv\Scripts\activate.bat
```

Dopo l’attivazione, usa i comandi `python` di installazione, avvio e test indicati sopra. In alternativa, anche da PowerShell, sostituisci `python` con `.\.venv\Scripts\python.exe`: in questo caso non serve attivare script o modificare le regole di esecuzione di PowerShell. Non copiare il comando di attivazione Bash in PowerShell.

## Collaudi documentati

Collaudo storico del 2026-10-16: Test locali registrati.

Queste istruzioni sono state ricavate dai file e dai collaudi conservati.
