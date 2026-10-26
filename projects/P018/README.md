# P018: Sincronizzare produttore e consumatore

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../COLLAUDO/P018/README.md) · [Registro del collaudo](../../COLLAUDO/P018/registro.json)

Coordina un produttore e un consumatore con primitive pthread.

Tutti i comandi partono dalla cartella `projects/P018`. I blocchi seguenti usano la sintassi di Linux/Bash.

## Requisiti e versioni

Linguaggio: C.

- C11

Dipendenze:

- gcc con supporto a C11
- Libreria standard C
- POSIX threads (pthread)
- Linker GNU con --wrap per tests/test_pc_failures.c

## Preparazione

Comandi per una shell Linux/Bash dalla cartella projects/P018. Installare prima il compilatore o SDK indicato nei requisiti. Le versioni documentate non costituiscono una garanzia per toolchain diverse.

```bash
mkdir -p build
```

## Avvio

```bash
gcc -std=c11 -Wall -Wextra -Werror src/producer_consumer.c -pthread -o build/producer_consumer
./build/producer_consumer
```

## Test

```bash
gcc -std=c11 -Wall -Wextra -Werror -O1 -g -fsanitize=undefined -fno-sanitize-recover=all tests/test_pc.c -pthread -o build/test_pc
./build/test_pc
gcc -std=c11 -Wall -Wextra -Werror -O1 -g -fsanitize=undefined -fno-sanitize-recover=all tests/test_pc_failures.c -pthread -Wl,--wrap=pthread_mutex_init -Wl,--wrap=pthread_cond_init -Wl,--wrap=pthread_create -o build/test_pc_failures
./build/test_pc_failures
```

## Perimetro del laboratorio

- Il main dimostrativo stampa la somma. Comando derivato dal sorgente e dalle opzioni del collaudo dei test.

## Windows

Per riprodurre senza adattamenti l’intera suite è necessario un ambiente Linux/POSIX con pthread e linker GNU: su Windows usare WSL. Non dichiarare supporto nativo Windows sulla sola base del sorgente C. Nessun collaudo WSL/Windows eseguito. Per riprodurre l’intero laboratorio da Windows usare WSL con una distribuzione Linux e una cartella nel filesystem Linux, non una cartella montata da C:. Nessun test Windows nativo è attestato da questo README.

## Collaudi documentati

Collaudo storico su Linux: le suite disponibili e i casi aggiuntivi risultano superati. Il riepilogo del gruppo P001–P040 non riporta una data puntuale; questi risultati non sono stati rieseguiti per preparare il README.

Queste istruzioni sono state ricavate dai file e dai collaudi conservati. La preparazione dei README non ha eseguito nuove suite né modificato il codice.
