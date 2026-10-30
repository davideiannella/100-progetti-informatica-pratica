# P027: Gestione palestra e abbonamenti

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P027/README.md) · [Registro del collaudo](../../collaudo/P027/registro.json)

**Sezione:** [Sezione 2: Database e gestione dei dati](../../docs/CATALOGO.md#sezione-2-database-e-gestione-dei-dati).

**Argomenti:** Database · Modellazione relazionale.

Registri iscritti, periodi di abbonamento e presenze ai corsi. Lo schema controlla i riferimenti fra le tabelle e l’ordine delle date, ma non verifica automaticamente se un abbonamento copre il giorno della presenza.

Apri un terminale nella cartella `projects/P027` ed esegui da lì i comandi. I blocchi seguenti usano la sintassi di Linux/Bash; per Windows consulta la sezione dedicata.

## Requisiti e versioni

**Tecnologie utilizzate:** Python · SQL · SQLite.

- Python 3.12.14
- SQLite 3.53.1

Dipendenze:

- Python con modulo standard sqlite3 funzionante; database dei test in memoria.
- File della sottocartella sql, mantenendo la struttura del progetto.

## Preparazione

Installa Python 3.12, poi crea e attiva l’ambiente virtuale con i comandi seguenti. Dopo l’attivazione, `python` usa l’interprete dell’ambiente `.venv`. Riattiva l’ambiente ogni volta che apri un nuovo terminale. Le versioni elencate descrivono gli ambienti documentati: non sono necessariamente le versioni minime richieste.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
```

## Avvio

Per provare il laboratorio, esegui i test della sezione seguente: creano i dati di esempio e chiamano le operazioni previste. Non è presente un’applicazione dimostrativa separata.

## Test

Il test inserisce un abbonamento e una presenza, poi verifica che un abbonamento con le date invertite venga rifiutato. La scritta `PASS` riguarda questi controlli, non il diritto di accesso alla palestra.

```bash
python tests/test_p027.py
```

## Windows

Il codice usa funzioni Python portabili e `pathlib` per i percorsi, senza richiedere Bash o funzioni specifiche di Linux. Dopo aver attivato l’ambiente, usa il suo comando `python`. Il codice è quindi predisposto per Windows, ma i collaudi documentati in questa pagina non comprendono una prova nativa su Windows.

Per preparare Python su Windows, apri il **Prompt dei comandi (cmd.exe)** nella cartella del progetto ed esegui:

```bat
py -3.12 -m venv .venv
.venv\Scripts\activate.bat
```

Dopo l’attivazione, esegui i comandi `python` di installazione, avvio e test indicati sopra. In alternativa, anche da PowerShell, usa direttamente `.\.venv\Scripts\python.exe` al posto di `python`: non devi attivare script né cambiare le regole di esecuzione di PowerShell. Non copiare in PowerShell il comando di attivazione Bash.

## Collaudi documentati

**Ultimo collaudo: 31 ottobre 2026 — superato.** Le verifiche del progetto sono riuscite su Ubuntu 24.04 nel [collaudo pubblico P001–P080](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/41142475728), eseguito sul commit `c8303920c4f4`.

### Prove precedenti

Nel [collaudo del 22 ottobre 2026](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701), le verifiche della versione di allora sono riuscite su Ubuntu 24.04.

Consulta **Output verificati** e **Registro del collaudo**, all’inizio della pagina, per leggere comandi, ambiente e limiti di ciascuna prova. I risultati documentati descrivono quei collaudi; per verificare la copia che stai usando, esegui i test sul tuo computer.
