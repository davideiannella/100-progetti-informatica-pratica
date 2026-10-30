# P082: Controlli per l’IA: una lista di verifica tracciabile

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P082/README.md) · [Registro del collaudo](../../collaudo/P082/registro.json)

**Sezione:** [Sezione 8: Intelligenza artificiale e analisi dei dati](../../docs/CATALOGO.md#sezione-8-intelligenza-artificiale-e-analisi-dei-dati).

**Argomenti:** Governance dell’IA · Controlli · Tracciabilità.

Il programma raccoglie le informazioni essenziali di un sistema di IA e controlla quali voci di una lista di verifica sono state dichiarate complete. Imparerai a rendere visibili le attività mancanti e ad associare al sistema uno scopo, un responsabile e dei limiti d’uso.

Tutti i comandi partono dalla cartella `projects/P082`. I blocchi seguenti usano la sintassi di Linux/Bash.

## Requisiti e versioni

**Tecnologie utilizzate:** Python.

- Python 3.12 o 3.13 come riferimento verificato
- Python 3.12.14 (collaudo Linux storico)
- Python 3.12.15 (Ubuntu/Linux, GitHub Actions, 22 ottobre 2026)
- Python 3.13.16 (Ubuntu/Linux, GitHub Actions, 22 ottobre 2026)
- Python 3.12.10 (Windows Server 2025, GitHub Actions, 22 ottobre 2026)
- Python 3.13.16 (Windows Server 2025, GitHub Actions, 22 ottobre 2026)

Dipendenze:

- Libreria standard di Python

## Preparazione

Installa Python 3.12, poi esegui i comandi seguenti dalla cartella `projects/P082` in Linux/Bash. Creano e attivano un ambiente virtuale nella cartella `.venv`, dove tenere separati i pacchetti del progetto. Dopo l’attivazione, `python` usa l’interprete di questo ambiente. Riattiva l’ambiente quando apri un nuovo terminale.

Le versioni elencate descrivono gli ambienti già provati, non la versione minima utilizzabile in ogni situazione. I test sono stati verificati sui runner Ubuntu di GitHub Actions con Python 3.12.15 e 3.13.16 il 22 ottobre 2026.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
```

## Avvio

```bash
python src/governance.py
```

## Cosa vedrai

Il riepilogo JSON descrive il sistema dimostrativo `TicketAI`. Risultano completate 9 voci su 11; mancano il monitoraggio e la gestione degli incidenti, indicati da `operations:monitoring` e `operations:incident_response`. Per questo il campo `complete` vale `false`.

## Test

```bash
python run_tests.py
```

Alla fine dell’esecuzione, `OK` indica che tutti i test hanno avuto esito positivo.

## Perimetro del laboratorio

- Le voci sono dichiarazioni inserite nel programma. Il conteggio misura la completezza della lista, senza verificare l’efficacia dei controlli o attestare la conformità a una normativa.
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

**Ultimo collaudo: 30 ottobre 2026 — superato.** Le verifiche del progetto sono riuscite su Ubuntu e Windows, con Python 3.12 e 3.13, nel [collaudo pubblico P081–P100](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/41133691301), eseguito sul commit `4741cc45e376c`.

### Prove precedenti

Il 21 ottobre 2026 erano documentati i collaudi Linux con Python 3.12.14, 3.12.15 e 3.13.16. Il 22 ottobre 2026, nel [run pubblico 39699184959](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39699184959) sul commit `711f91b76ea819e2e57a400ad33c98afda3b6e62`, i 12 metodi di test di questo progetto sono passati in tutti e quattro i job: Ubuntu/Linux con Python 3.12.15 e 3.13.16; Windows Server 2025 con Python 3.12.10 e 3.13.16. Ogni job ha superato complessivamente 377 metodi per P081–P100 senza test saltati o errori, ha verificato la compilazione sintattica di 60 file Python e l’integrità di 289 file tramite hash. Il controllo degli hash comprende i sorgenti degli altri progetti, ma i test del run riguardano soltanto P081–P100.

Queste istruzioni sono state ricavate dai file e dai collaudi conservati.
