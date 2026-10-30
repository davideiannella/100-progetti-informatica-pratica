# P016: Monitor di processi da riga di comando

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P016/README.md) · [Registro del collaudo](../../collaudo/P016/registro.json)

**Sezione:** [Sezione 1: Programmazione, algoritmi e strutture dati](../../docs/CATALOGO.md#sezione-1-programmazione-algoritmi-e-strutture-dati).

**Argomenti:** Sistemi operativi · Linux · Monitoraggio dei processi.

Legge il nome e la memoria residente di un processo Linux attraverso `/proc`. Il monitor distingue un PID non valido da un processo che non riesce a leggere.

Apri un terminale nella cartella `projects/P016` ed esegui da lì i comandi. I blocchi principali usano Bash su Linux; trovi le indicazioni per Windows nella sezione dedicata.

## Requisiti e versioni

**Tecnologie utilizzate:** C · Python · Linux.

- C11

Dipendenze:

- gcc con supporto a C11
- Libreria standard C
- Linux con filesystem /proc e API POSIX (unistd.h, pid_t, getpid)
- Python 3.12 per tests/test_cli.py; il test richiama gcc

## Preparazione

Installa gli strumenti elencati nei requisiti, compreso Python 3.12, poi apri un terminale Bash nella cartella del progetto. I comandi seguenti creano e attivano `.venv`, un ambiente Python separato per questo laboratorio. Dopo l’attivazione, `python` usa l’interprete di quell’ambiente; riattivalo ogni volta che apri un nuovo terminale. Le versioni indicate descrivono gli ambienti documentati, non la versione minima compatibile.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
mkdir -p build
```

## Avvio

Il monitor stampa PID, nome del processo e memoria residente in kB. Senza argomenti osserva il proprio processo; i valori possono cambiare tra le esecuzioni.

```bash
gcc -std=c11 -Wall -Wextra -Werror src/process_monitor.c -o build/monitor
./build/monitor
```

## Test

Le due prove stampano messaggi con `PASS` se i controlli riescono. Il nome del processo osservato può cambiare tra un’esecuzione e l’altra.

```bash
gcc -std=c11 -Wall -Wextra -Werror -O1 -g -fsanitize=undefined -fno-sanitize-recover=all tests/test_process_monitor.c -o build/test_process_monitor
./build/test_process_monitor
python tests/test_cli.py
```

## Perimetro del laboratorio

- Senza argomenti, il monitor legge il processo corrente. Puoi fornire come argomento un PID positivo per osservare un altro processo.

## Windows

Questo sorgente legge `/proc` e richiede Linux. Da Windows, usa WSL con una distribuzione Linux e conserva il progetto nel filesystem Linux, non in una cartella montata da `C:`. Puoi così seguire gli stessi comandi; il monitor osserverà i processi Linux di quell’ambiente. Qui non sono documentati collaudi su WSL o Windows nativo.

## Collaudi documentati

**Ultimo collaudo: 31 ottobre 2026 — superato.** Le verifiche del progetto sono riuscite su Ubuntu 24.04 nel [collaudo pubblico P001–P080](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/41142475728), eseguito sul commit `c8303920c4f4`.

### Prove precedenti

Nel [collaudo del 22 ottobre 2026](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701), le verifiche della versione di allora sono riuscite su Ubuntu 24.04.

Apri **Output verificati** e **Registro del collaudo**, all’inizio di questa pagina, per consultare comandi, esiti e limiti delle prove pubblicate. Esegui i test anche sul tuo computer e ripetili dopo ogni modifica al codice.
