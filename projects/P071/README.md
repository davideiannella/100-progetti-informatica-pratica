# P071: Individuare le minacce: metodo STRIDE e priorità di intervento

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P071/README.md) · [Registro del collaudo](../../collaudo/P071/registro.json)

**Sezione:** [Sezione 7: Sicurezza informatica](../../docs/CATALOGO.md#sezione-7-sicurezza-informatica).

**Argomenti:** Sicurezza · Modellazione delle minacce.

Il progetto organizza le minacce secondo le categorie STRIDE e assegna priorità usando scale numeriche ordinate. Il registro locale aiuta a confrontare i rischi e a motivare le contromisure, senza trasformare i punteggi in probabilità.

Apri un terminale nella cartella `projects/P071`. I comandi qui sotto sono scritti per Linux con Bash; per Windows consulta la sezione dedicata.

## Requisiti e versioni

**Tecnologie utilizzate:** Python.

- Python 3.12.14 (ambiente documentato)

Dipendenze:

- Libreria standard Python; nessun pacchetto pip aggiuntivo.

## Preparazione

Installa Python 3.12, poi esegui i comandi qui sotto per creare e attivare un ambiente virtuale dedicato al progetto, nella cartella `.venv`. Dopo l’attivazione, il comando `python` usa questo ambiente. Riattivalo ogni volta che apri un nuovo terminale.

Le versioni elencate sono quelle degli ambienti documentati; non indicano la versione minima compatibile.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
```

## Avvio

Esegui la dimostrazione per vedere una categoria STRIDE, la priorità del rischio prima e dopo una contromisura e il rifiuto di un valore non valido.

```bash
python -B src/threat_model.py
```

## Esempio documentale

Stampa le scale di rischio e i casi STRIDE degli esempi, inclusi i controlli sui valori non validi. Dalla cartella `projects/P071`, con l’ambiente Python preparato:

```bash
python -B worked_example.py
```

## Test

Esegui i test automatici del progetto:

```bash
python -B run_tests.py
```

Nel riepilogo, `OK` indica che tutti i test eseguiti sono passati. Il report JSON riporta quanti test sono stati eseguiti e gli eventuali errori o fallimenti.

## Windows

I sorgenti e i test usano librerie Python e percorsi gestiti con `pathlib`. Dalla lettura del codice non emergono dipendenze da comandi Unix o richieste di privilegi di amministratore. Le prove conservate non documentano un collaudo su Windows nativo.

Apri il **Prompt dei comandi (cmd.exe)** nella cartella del progetto, poi crea e attiva l’ambiente virtuale:

```bat
py -3.12 -m venv .venv
.venv\Scripts\activate.bat
```

Dopo l’attivazione, esegui con `python` i comandi di installazione, avvio e test indicati sopra. Se usi PowerShell, puoi richiamare direttamente `.\.venv\Scripts\python.exe` al posto di `python`: in questo modo non devi attivare script né cambiare la policy di esecuzione. Non copiare in PowerShell il comando di attivazione scritto per Bash.

## Collaudi documentati

**Ultimo collaudo: 30 ottobre 2026 — superato.** Le verifiche del progetto sono riuscite su Ubuntu 24.04 nel [collaudo pubblico P001–P080](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/41134634700), eseguito sul commit `35b49f130493`.

### Prove precedenti

La documentazione del 18 ottobre 2026 descrive una suite di 8 metodi di test `unittest`. I collegamenti «Output verificati» e «Registro del collaudo», all’inizio della pagina, riportano risultati, comandi e ambiente delle prove conservate.
