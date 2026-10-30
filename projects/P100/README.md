# P100: Progetto finale: metadati dei rifiuti, HMAC e SQLite

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P100/README.md) · [Registro del collaudo](../../collaudo/P100/registro.json)

**Sezione:** [Sezione 10: Progetti integrati](../../docs/CATALOGO.md#sezione-10-progetti-integrati).

**Argomenti:** IoT simulato · Sicurezza · Database.

Il progetto finale riunisce dispositivi virtuali, controllo dei messaggi e un database SQLite per raccogliere dati sui rifiuti. Ogni messaggio viene autenticato con un HMAC, cioè un codice calcolato con un segreto condiviso; se i dati sono validi, il programma registra l’evento e l’eventuale segnalazione nella stessa operazione di database.

Tutti i comandi partono dalla cartella `projects/P100`. I blocchi seguenti usano la sintassi di Linux/Bash.

## Requisiti e versioni

**Tecnologie utilizzate:** Python · SQL · SQLite.

- Python 3.12 o 3.13 come riferimento verificato
- Python 3.12.14 (collaudo Linux storico)
- Python 3.12.15 (Ubuntu/Linux, GitHub Actions, 22 ottobre 2026)
- Python 3.13.16 (Ubuntu/Linux, GitHub Actions, 22 ottobre 2026)
- Python 3.12.10 (Windows Server 2025, GitHub Actions, 22 ottobre 2026)
- Python 3.13.16 (Windows Server 2025, GitHub Actions, 22 ottobre 2026)

Dipendenze:

- Libreria standard di Python
- sqlite3 incluso nel runtime Python; SQLite 3.53.1 registrato nel rapporto locale P096_P100

## Preparazione

Installa Python 3.12, poi esegui i comandi seguenti dalla cartella `projects/P100` in Linux/Bash. Creano e attivano un ambiente virtuale nella cartella `.venv`, dove tenere separati i pacchetti del progetto. Dopo l’attivazione, `python` usa l’interprete di questo ambiente. Riattiva l’ambiente quando apri un nuovo terminale.

Le versioni elencate descrivono gli ambienti già provati, non la versione minima utilizzabile in ogni situazione. I test sono stati verificati sui runner Ubuntu di GitHub Actions con Python 3.12.15 e 3.13.16 il 22 ottobre 2026.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
```

## Avvio

```bash
python src/smart_waste_platform.py
```

## Cosa vedrai

Il riepilogo JSON mostra 2 eventi, uno per la carta e uno per il vetro, e 1 segnalazione di riempimento. Il primo inserimento riesce (`first_inserted: true`), mentre il reinvio dello stesso evento non crea una copia (`retry_inserted: false`). La demo usa SQLite in memoria, come indica `storage: ":memory:"`.

## Test

```bash
python run_tests.py
```

Alla fine dell’esecuzione, `OK` indica che tutti i test hanno avuto esito positivo.

## Perimetro del laboratorio

- Categoria del rifiuto, confidenza e riempimento sono dati forniti dal chiamante: il programma non classifica immagini. Per conservare i dati fra esecuzioni occorre scegliere un file SQLite; la demo non richiede servizi cloud o dispositivi fisici.
- Nessuna rete, credenziale, periferica o servizio esterno richiesto per demo e test.

## Windows

Test eseguiti nativamente sui runner GitHub Actions Windows Server 2025 con Python 3.12.10 e 3.13.16, il 22 ottobre 2026. WSL non è necessario per questo laboratorio. L’esito attesta gli ambienti dei runner e i casi provati; non garantisce ogni configurazione Windows. Evidenza pubblica: [run 39699184959](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39699184959).

Per la parte Python nativa, dal **Prompt dei comandi (cmd.exe)**, nella cartella del progetto:

```bat
py -3.12 -m venv .venv
.venv\Scripts\activate.bat
```

Dopo l’attivazione, usa i comandi `python` di installazione, avvio e test indicati sopra. In alternativa, anche da PowerShell, usa direttamente `.\.venv\Scripts\python.exe` al posto di `python`: non serve attivare script né cambiare la policy di esecuzione. Il comando di attivazione Bash non va copiato in PowerShell.

## Collaudi documentati

Il 21 ottobre 2026 erano documentati i collaudi Linux con Python 3.12.14, 3.12.15 e 3.13.16. Il 22 ottobre 2026, nel [run pubblico 39699184959](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39699184959) sul commit `711f91b76ea819e2e57a400ad33c98afda3b6e62`, i 24 metodi di test di questo progetto sono passati in tutti e quattro i job: Ubuntu/Linux con Python 3.12.15 e 3.13.16; Windows Server 2025 con Python 3.12.10 e 3.13.16. Ogni job ha superato complessivamente 377 metodi per P081–P100 senza test saltati o errori, ha verificato la compilazione sintattica di 60 file Python e l’integrità di 289 file tramite hash. Il controllo degli hash comprende i sorgenti degli altri progetti, ma i test del run riguardano soltanto P081–P100.

Queste istruzioni sono state ricavate dai file e dai collaudi conservati. La preparazione dei README non ha eseguito nuove suite né modificato il codice.
