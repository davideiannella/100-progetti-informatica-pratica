# P062: Ripartire dopo un guasto: replica e failover di lettura

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P062/README.md) · [Registro del collaudo](../../collaudo/P062/registro.json)

**Sezione:** [Sezione 6: Cloud e affidabilità dei servizi](../../docs/CATALOGO.md#sezione-6-cloud-e-affidabilità-dei-servizi).

**Argomenti:** Affidabilità dei sistemi · Replica · Failover simulato.

Il progetto simula un servizio con una copia principale e una secondaria. Mostra cosa accade quando la replica si interrompe e come passare le letture alla copia ancora disponibile.

Apri un terminale nella cartella `projects/P062`. I comandi qui sotto sono scritti per Linux con Bash; per Windows consulta la sezione dedicata.

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

Esegui la dimostrazione per vedere quali scritture attendono la replica, da quale copia vengono lette le informazioni e quando le due copie tornano allineate.

```bash
python src/dr.py
```

## Test

Esegui i test automatici del progetto:

```bash
python run_tests.py
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

La documentazione del 18 ottobre 2026 descrive una suite di 10 metodi di test `unittest`. I collegamenti «Output verificati» e «Registro del collaudo», all’inizio della pagina, riportano risultati, comandi e ambiente delle prove conservate.
