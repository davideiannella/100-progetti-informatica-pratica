# P076: Consigliare corsi in base agli interessi

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P076/README.md) · [Registro del collaudo](../../collaudo/P076/registro.json)

**Sezione:** [Sezione 8: Intelligenza artificiale e analisi dei dati](../../docs/CATALOGO.md#sezione-8-intelligenza-artificiale-e-analisi-dei-dati).

**Argomenti:** Sistemi di raccomandazione · Similarità tra contenuti.

Il progetto ordina un catalogo di corsi in base agli interessi indicati. Usa la similarità coseno per confrontare liste di valori numerici assegnati manualmente ai corsi e al profilo dell’utente.

Apri un terminale nella cartella `projects/P076`. I comandi qui sotto sono scritti per Linux con Bash; per Windows consulta la sezione dedicata.

## Requisiti e versioni

**Tecnologie utilizzate:** Python · NumPy.

- Python 3.12.14 (ambiente documentato)
- numpy 2.3.5 (ambiente documentato)

Dipendenze:

- numpy 2.3.5 — Array e calcoli numerici; dipendenza diretta di sorgente e/o test.

## Preparazione

Installa Python 3.12, poi esegui i comandi qui sotto per creare e attivare un ambiente virtuale dedicato al progetto, nella cartella `.venv`. Dopo l’attivazione, il comando `python` usa questo ambiente. Riattivalo ogni volta che apri un nuovo terminale.

Le versioni elencate sono quelle degli ambienti documentati; non indicano la versione minima compatibile.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
python -m pip install -r ../../requirements-p061-p080.txt
```

## Avvio

Esegui la dimostrazione per leggere i corsi consigliati, ordinati in base al punteggio di similarità con il profilo.

```bash
python -B src/recommender.py
```

## Esempio documentale

Stampa le raccomandazioni degli esempi, le parità, il catalogo vuoto e le esclusioni dell’esercizio. Dalla cartella `projects/P076`, con l’ambiente Python preparato:

```bash
python -B examples.py
```

## Test

Esegui i test automatici del progetto:

```bash
python -B run_tests.py
```

Nel riepilogo, `OK` indica che tutti i test eseguiti sono passati. Il report JSON riporta quanti test sono stati eseguiti e gli eventuali errori o fallimenti.

## Perimetro del laboratorio

- L’ambiente condiviso comprende anche scikit-learn 1.8.0. I file `src/recommender.py`, `run_tests.py` e `tests/test_p076.py` non lo importano: non è una dipendenza diretta di questo progetto.
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

La documentazione del 18 ottobre 2026 descrive una suite di 112 metodi di test `unittest`. I collegamenti «Output verificati» e «Registro del collaudo», all’inizio della pagina, riportano risultati, comandi e ambiente delle prove conservate.
