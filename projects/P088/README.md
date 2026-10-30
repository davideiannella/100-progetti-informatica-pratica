# P088: Parcheggio virtuale: eventi, occupazione e idempotenza

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P088/README.md) · [Registro del collaudo](../../collaudo/P088/registro.json)

**Sezione:** [Sezione 9: IoT e simulazione di sistemi](../../docs/CATALOGO.md#sezione-9-iot-e-simulazione-di-sistemi).

**Argomenti:** IoT simulato · Gestione degli eventi · Idempotenza.

Il programma aggiorna i posti occupati e liberi di un parcheggio virtuale a ogni ingresso o uscita. Gestisce anche gli eventi ripetuti: ricevere di nuovo lo stesso evento restituisce l’esito già registrato e non modifica una seconda volta l’occupazione.

Tutti i comandi partono dalla cartella `projects/P088`. I blocchi seguenti usano la sintassi di Linux/Bash.

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

Installa Python 3.12, poi esegui i comandi seguenti dalla cartella `projects/P088` in Linux/Bash. Creano e attivano un ambiente virtuale nella cartella `.venv`, dove tenere separati i pacchetti del progetto. Dopo l’attivazione, `python` usa l’interprete di questo ambiente. Riattiva l’ambiente quando apri un nuovo terminale.

Le versioni elencate descrivono gli ambienti già provati, non la versione minima utilizzabile in ogni situazione. I test sono stati verificati sui runner Ubuntu di GitHub Actions con Python 3.12.15 e 3.13.16 il 22 ottobre 2026.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
```

## Avvio

```bash
python src/smart_parking.py
```

## Cosa vedrai

Il riepilogo JSON mostra 7 eventi: 4 accettati e 3 rifiutati, con il motivo di ogni rifiuto. Alla fine entrambi i posti sono occupati e i posti liberi sono 0. Per un’uscita viene calcolata una sosta di 70 secondi; `duplicate_same_result: true` conferma che il reinvio restituisce lo stesso risultato.

## Test

```bash
python run_tests.py
```

Alla fine dell’esecuzione, `OK` indica che tutti i test hanno avuto esito positivo.

## Perimetro del laboratorio

- Posti, veicoli ed eventi sono simulati e conservati in memoria. Il laboratorio non comprende telecamere, riconoscimento delle targhe o pagamenti.
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

Il 21 ottobre 2026 erano documentati i collaudi Linux con Python 3.12.14, 3.12.15 e 3.13.16. Il 22 ottobre 2026, nel [run pubblico 39699184959](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39699184959) sul commit `711f91b76ea819e2e57a400ad33c98afda3b6e62`, i 22 metodi di test di questo progetto sono passati in tutti e quattro i job: Ubuntu/Linux con Python 3.12.15 e 3.13.16; Windows Server 2025 con Python 3.12.10 e 3.13.16. Ogni job ha superato complessivamente 377 metodi per P081–P100 senza test saltati o errori, ha verificato la compilazione sintattica di 60 file Python e l’integrità di 289 file tramite hash. Il controllo degli hash comprende i sorgenti degli altri progetti, ma i test del run riguardano soltanto P081–P100.

Queste istruzioni sono state ricavate dai file e dai collaudi conservati.
