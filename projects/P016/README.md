# P016: Monitor di processi da riga di comando

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P016/README.md) · [Registro del collaudo](../../collaudo/P016/registro.json)

Legge informazioni dei processi Linux dal filesystem /proc.

Tutti i comandi partono dalla cartella `projects/P016`. I blocchi seguenti usano la sintassi di Linux/Bash.

## Requisiti e versioni

Linguaggio: C.

- C11

Dipendenze:

- gcc con supporto a C11
- Libreria standard C
- Linux con filesystem /proc e API POSIX (unistd.h, pid_t, getpid)
- Python 3.12 per tests/test_cli.py; il test richiama gcc

## Preparazione

Comandi per una shell Linux/Bash dalla cartella projects/P016. Installare Python 3.12 prima della preparazione; dopo l’attivazione, python indica l’interprete dell’ambiente virtuale .venv. Riattivare l’ambiente in ogni nuovo terminale. Le versioni indicate descrivono gli ambienti documentati, non un minimo universale.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
mkdir -p build
```

## Avvio

```bash
gcc -std=c11 -Wall -Wextra -Werror src/process_monitor.c -o build/monitor
./build/monitor
```

## Test

```bash
gcc -std=c11 -Wall -Wextra -Werror -O1 -g -fsanitize=undefined -fno-sanitize-recover=all tests/test_process_monitor.c -o build/test_process_monitor
./build/test_process_monitor
python tests/test_cli.py
```

## Perimetro del laboratorio

- Senza argomenti legge il processo corrente; si può fornire un PID positivo come argomento. Comando ricavato dal main e dal comando di compilazione in tests/test_cli.py.

## Windows

Windows nativo non compatibile con questo sorgente, che legge /proc. Usare una distribuzione Linux in WSL per seguire invariati codice e comandi; il monitor vede i processi Linux di quell’ambiente. Nessun collaudo WSL/Windows eseguito. Per riprodurre l’intero laboratorio da Windows usare WSL con una distribuzione Linux e una cartella nel filesystem Linux, non una cartella montata da C:. Nessun test Windows nativo è attestato da questo README.

## Collaudi documentati

Collaudo storico su Linux: le suite disponibili e i casi aggiuntivi risultano superati. Il riepilogo del gruppo P001–P040 non riporta una data puntuale; questi risultati non sono stati rieseguiti per preparare il README.

Queste istruzioni sono state ricavate dai file e dai collaudi conservati. La preparazione dei README non ha eseguito nuove suite né modificato il codice.
