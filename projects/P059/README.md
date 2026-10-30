# P059: Simulare cache e distribuzione delle richieste

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P059/README.md) · [Registro del collaudo](../../collaudo/P059/registro.json)

**Sezione:** [Sezione 6: Cloud e affidabilità dei servizi](../../docs/CATALOGO.md#sezione-6-cloud-e-affidabilità-dei-servizi).

**Argomenti:** Architettura dei sistemi · Cache · Bilanciamento simulato.

Simula la distribuzione delle richieste fra backend disponibili, cioè i componenti che le elaborano. Una cache conserva i risultati già ottenuti e li riusa senza chiamare di nuovo il backend. Non vengono contattati servizi esterni.

Apri un terminale nella cartella `projects/P059` ed esegui da lì tutti i comandi. Gli esempi usano Linux e Bash; per Windows, segui anche la sezione dedicata.

## Requisiti e versioni

**Tecnologie utilizzate:** Python.

- Python 3.12.14 (collaudo locale storico)

Dipendenze:

- Libreria standard Python con Python 3.12.14 — Il sorgente non importa librerie esterne.

## Preparazione

Installa Python 3.12, poi esegui questi comandi nella cartella del progetto. L’ambiente virtuale `.venv` tiene separate le dipendenze del laboratorio; dopo l’attivazione, `python` usa l’interprete di questo ambiente. Riattivalo ogni volta che apri un nuovo terminale. Le versioni indicate descrivono i collaudi documentati e non sono necessariamente le versioni minime richieste.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
```

## Avvio

Esegui i comandi della sezione Test per provare il laboratorio. I test richiamano il codice e verificano i risultati; non c’è un’applicazione dimostrativa separata.

## Test

I test controllano la rotazione fra backend, il riuso della cache e gli errori quando manca un backend disponibile o il caricamento fallisce. Se i controlli passano, stampano messaggi `PASS`.

```bash
python tests/test_p059.py
python tests/test_edges.py
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

Collaudo storico del 2026-10-16: Test locali registrati.

Queste istruzioni sono state ricavate dai file e dai collaudi conservati.
