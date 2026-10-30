# P068: Segmentazione di rete con firewall e rilevamento dei login falliti

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P068/README.md) · [Registro del collaudo](../../collaudo/P068/registro.json)

**Sezione:** [Sezione 7: Sicurezza informatica](../../docs/CATALOGO.md#sezione-7-sicurezza-informatica).

**Argomenti:** Sicurezza delle reti · Segmentazione · Analisi dei log.

Il progetto simula regole che consentono o vietano comunicazioni tra zone di rete e riconosce sequenze di accessi falliti. Lavora su dati di esempio e non modifica il firewall del computer.

Apri un terminale nella cartella `projects/P068`. I comandi qui sotto sono scritti per Linux con Bash; per Windows consulta la sezione dedicata.

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

Esegui la dimostrazione per vedere quali comunicazioni sono ammesse e quando una sequenza di accessi falliti produce un avviso.

```bash
python -B src/network_defense.py
```

## Esempio documentale

Stampa la matrice delle regole di rete e le sequenze di login falliti usate negli esempi, senza modificare il firewall. Dalla cartella `projects/P068`, con l’ambiente Python preparato:

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

**Ultimo collaudo: 31 ottobre 2026 — superato.** Le verifiche del progetto sono riuscite su Ubuntu 24.04 nel [collaudo pubblico P001–P080](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/41142475728), eseguito sul commit `c8303920c4f4`.

### Prove precedenti

La documentazione del 18 ottobre 2026 descrive una suite di 107 metodi di test `unittest`. I collegamenti «Output verificati» e «Registro del collaudo», all’inizio della pagina, riportano risultati, comandi e ambiente delle prove conservate.
