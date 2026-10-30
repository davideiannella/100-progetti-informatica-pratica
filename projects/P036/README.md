# P036: Progettare un gestionale per palestra con UML

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P036/README.md) · [Registro del collaudo](../../collaudo/P036/registro.json)

**Sezione:** [Sezione 3: Ingegneria e progettazione del software](../../docs/CATALOGO.md#sezione-3-ingegneria-e-progettazione-del-software).

**Argomenti:** Ingegneria del software · UML · Programmazione a oggetti.

Modelli clienti, abbonamenti, istruttori e corsi con classi Python. Il servizio controlla la validità dell’abbonamento, le prenotazioni duplicate e i posti disponibili; non gestisce lezioni distinte sul calendario.

Apri un terminale nella cartella `projects/P036` ed esegui da lì i comandi. I blocchi seguenti usano la sintassi di Linux/Bash; per Windows consulta la sezione dedicata.

## Requisiti e versioni

**Tecnologie utilizzate:** Python.

- Python 3.12.14

Dipendenze:

- Libreria standard Python; nessun pacchetto esterno per i test presenti.

## Preparazione

Installa Python 3.12, poi crea e attiva l’ambiente virtuale con i comandi seguenti. Dopo l’attivazione, `python` usa l’interprete dell’ambiente `.venv`. Riattiva l’ambiente ogni volta che apri un nuovo terminale. Le versioni elencate descrivono gli ambienti documentati: non sono necessariamente le versioni minime richieste.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
```

## Avvio

Per provare il laboratorio, esegui i test della sezione seguente: creano i dati di esempio e chiamano le operazioni previste. Non è presente un’applicazione dimostrativa separata.

## Test

Il primo test controlla che la capienza sia un intero positivo e stampa `PASS`. Il secondo esegue sette verifiche su accesso, abbonamenti, prenotazioni e annullamento: il riepilogo finale deve indicare `OK`.

```bash
python tests/test_capacity_types.py
python tests/test_gym_domain.py
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
