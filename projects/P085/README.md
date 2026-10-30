# P085: Badge virtuali: autorizzazione per ruolo e audit delle richieste

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P085/README.md) · [Registro del collaudo](../../collaudo/P085/registro.json)

**Sezione:** [Sezione 9: IoT e simulazione di sistemi](../../docs/CATALOGO.md#sezione-9-iot-e-simulazione-di-sistemi).

**Argomenti:** Sicurezza · Autorizzazione per ruoli · Audit.

Il programma decide se un badge virtuale può accedere a una zona, in base al suo ruolo e al fatto che sia ancora attivo. Ogni richiesta viene registrata con l’esito e il motivo, così puoi ricostruire sia gli accessi consentiti sia quelli negati.

Tutti i comandi partono dalla cartella `projects/P085`. I blocchi seguenti usano la sintassi di Linux/Bash.

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

Installa Python 3.12, poi esegui i comandi seguenti dalla cartella `projects/P085` in Linux/Bash. Creano e attivano un ambiente virtuale nella cartella `.venv`, dove tenere separati i pacchetti del progetto. Dopo l’attivazione, `python` usa l’interprete di questo ambiente. Riattiva l’ambiente quando apri un nuovo terminale.

Le versioni elencate descrivono gli ambienti già provati, non la versione minima utilizzabile in ogni situazione. I test sono stati verificati sui runner Ubuntu di GitHub Actions con Python 3.12.15 e 3.13.16 il 22 ottobre 2026.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
```

## Avvio

```bash
python src/access.py
```

## Cosa vedrai

Il riepilogo JSON riporta 2 richieste consentite e 4 negate. Nel registro `audit` trovi tutte e 6 le richieste: sono distinguibili, per esempio, un ruolo privo del permesso necessario, un badge disattivato e un identificativo sconosciuto.

## Test

```bash
python run_tests.py
```

Alla fine dell’esecuzione, `OK` indica che tutti i test hanno avuto esito positivo.

## Perimetro del laboratorio

- Il laboratorio verifica le autorizzazioni associate ai badge dichiarati. Non identifica la persona che presenta il badge e non usa lettori o porte fisiche.
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

**Ultimo collaudo: 31 ottobre 2026 — superato.** Le verifiche del progetto sono riuscite su Ubuntu e Windows, con Python 3.12 e 3.13 nel [collaudo pubblico P081–P100](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/41142475640), eseguito sul commit `c8303920c4f4`.

### Prove precedenti

Il 21 ottobre 2026 erano documentati i collaudi Linux con Python 3.12.14, 3.12.15 e 3.13.16. Il 22 ottobre 2026, nel [run pubblico 39699184959](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39699184959) sul commit `711f91b76ea819e2e57a400ad33c98afda3b6e62`, i 17 metodi di test di questo progetto sono passati in tutti e quattro i job: Ubuntu/Linux con Python 3.12.15 e 3.13.16; Windows Server 2025 con Python 3.12.10 e 3.13.16. Ogni job ha superato complessivamente 377 metodi per P081–P100 senza test saltati o errori, ha verificato la compilazione sintattica di 60 file Python e l’integrità di 289 file tramite hash. Il controllo degli hash comprende i sorgenti degli altri progetti, ma i test del run riguardano soltanto P081–P100.

Queste istruzioni sono state ricavate dai file e dai collaudi conservati.
