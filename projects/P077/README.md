# P077: Leggere e smistare ticket automaticamente con NLP

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P077/README.md) · [Registro del collaudo](../../collaudo/P077/registro.json)

**Sezione:** [Sezione 8: Intelligenza artificiale e analisi dei dati](../../docs/CATALOGO.md#sezione-8-intelligenza-artificiale-e-analisi-dei-dati).

**Argomenti:** Intelligenza artificiale · Elaborazione del linguaggio naturale · Classificazione.

Il progetto assegna richieste di assistenza inventate alle categorie accesso, fatturazione e tecnico. Mostra anche come astenersi dalla scelta quando un testo non contiene alcun termine conosciuto dal modello.

Apri un terminale nella cartella `projects/P077`. I comandi qui sotto sono scritti per Linux con Bash; per Windows consulta la sezione dedicata.

## Requisiti e versioni

**Tecnologie utilizzate:** Python · NumPy · scikit-learn.

- Python 3.12.14 (ambiente documentato)
- numpy 2.3.5 (ambiente documentato)
- scikit-learn 1.8.0 (ambiente documentato)

Dipendenze:

- numpy 2.3.5 — Array e calcoli numerici; dipendenza diretta di sorgente e/o test.
- scikit-learn 1.8.0 — Modelli, trasformazioni o metriche importati dal progetto.

## Preparazione

Installa Python 3.12, poi esegui i comandi qui sotto per creare e attivare un ambiente virtuale dedicato al progetto, nella cartella `.venv`. Dopo l’attivazione, il comando `python` usa questo ambiente. Riattivalo ogni volta che apri un nuovo terminale.

Le versioni elencate sono quelle degli ambienti documentati; non indicano la versione minima compatibile.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
python -m pip install -r ../../requirements-p061-p080.txt
```

## Avvio

Esegui l’esperimento per leggere la categoria prevista per ogni ticket di test, le misure di qualità e l’esempio di astensione per parole sconosciute.

```bash
python src/ticket_nlp.py
```

## Test

Esegui i test automatici del progetto:

```bash
python run_tests.py
```

Nel riepilogo, `OK` indica che tutti i test eseguiti sono passati. Il report JSON riporta quanti test sono stati eseguiti e gli eventuali errori o fallimenti.

## Perimetro del laboratorio

- L’installazione deve includere anche i pacchetti da cui dipende scikit-learn. I registri citati non elencano la versione di ogni dipendenza.
- Il file `requirements-p061-p080.txt` prepara un ambiente condiviso dai progetti P061–P080. Per questo include anche pacchetti che questo progetto non usa direttamente.

## Windows

Su Windows servono Python 3.12 e versioni compatibili dei pacchetti numerici indicati. Il progetto lavora su array, dati sintetici e file locali e non richiama strumenti Unix. Per riprodurre gli stessi risultati numerici, usa le versioni registrate. Le prove conservate non documentano un collaudo su Windows nativo.

Apri il **Prompt dei comandi (cmd.exe)** nella cartella del progetto, poi crea e attiva l’ambiente virtuale:

```bat
py -3.12 -m venv .venv
.venv\Scripts\activate.bat
```

Dopo l’attivazione, esegui con `python` i comandi di installazione, avvio e test indicati sopra. Se usi PowerShell, puoi richiamare direttamente `.\.venv\Scripts\python.exe` al posto di `python`: in questo modo non devi attivare script né cambiare la policy di esecuzione. Non copiare in PowerShell il comando di attivazione scritto per Bash.

## Collaudi documentati

La documentazione del 18 ottobre 2026 descrive una suite di 115 metodi di test `unittest`. I collegamenti «Output verificati» e «Registro del collaudo», all’inizio della pagina, riportano risultati, comandi e ambiente delle prove conservate. Il conteggio di 115 si riferisce alla suite storica; la suite attuale comprende anche un test sul numero di ticket dopo l’ampliamento del dataset.
