# P080: Assistente con citazioni: ricerca nei testi senza LLM

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P080/README.md) · [Registro del collaudo](../../collaudo/P080/registro.json)

**Sezione:** [Sezione 8: Intelligenza artificiale e analisi dei dati](../../docs/CATALOGO.md#sezione-8-intelligenza-artificiale-e-analisi-dei-dati).

**Argomenti:** Ricerca nei testi · Recupero di informazioni · Citazioni delle fonti.

Il progetto cerca informazioni in note locali con TF-IDF, un metodo che rappresenta i testi attraverso il peso delle parole. Restituisce un estratto della nota scelta con l’identificativo della fonte; non usa un modello linguistico per generare la risposta.

Apri un terminale nella cartella `projects/P080`. I comandi qui sotto sono scritti per Linux con Bash; per Windows consulta la sezione dedicata.

## Requisiti e versioni

**Tecnologie utilizzate:** Python · scikit-learn.

- Python 3.12.14 (ambiente documentato)
- scikit-learn 1.8.0 (ambiente documentato)
- numpy 2.3.5 (ambiente documentato)

Dipendenze:

- scikit-learn 1.8.0 — Modelli, trasformazioni o metriche importati dal progetto.
- numpy 2.3.5 — Versione registrata nell’ambiente condiviso; dipendenza transitiva del calcolo numerico di scikit-learn, non importata direttamente da rag.py.

## Preparazione

Installa Python 3.12, poi esegui i comandi qui sotto per creare e attivare un ambiente virtuale dedicato al progetto, nella cartella `.venv`. Dopo l’attivazione, il comando `python` usa questo ambiente. Riattivalo ogni volta che apri un nuovo terminale.

Le versioni elencate sono quelle degli ambienti documentati; non indicano la versione minima compatibile.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
python -m pip install -r ../../requirements-p061-p080.txt
```

## Avvio

Esegui la dimostrazione per vedere una risposta con la sua fonte e i casi in cui l’assistente si astiene perché non trova una corrispondenza sufficiente.

```bash
python src/rag.py
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

La documentazione del 18 ottobre 2026 descrive una suite di 114 metodi di test `unittest`. I collegamenti «Output verificati» e «Registro del collaudo», all’inizio della pagina, riportano risultati, comandi e ambiente delle prove conservate.
