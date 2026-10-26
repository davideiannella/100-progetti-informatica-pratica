# P021: Simulare una coda di traffico

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P021/README.md) · [Registro del collaudo](../../collaudo/P021/registro.json)

**Sezione:** [Sezione 1: Programmazione, algoritmi e strutture dati](../../docs/CATALOGO.md#sezione-1-programmazione-algoritmi-e-strutture-dati).

**Argomenti:** Simulazione · Gestione delle code.

Simula il comportamento di una coda di traffico.

Tutti i comandi partono dalla cartella `projects/P021`. I blocchi seguenti usano la sintassi di Linux/Bash.

## Requisiti e versioni

Linguaggio: C++.

- C++ C++17

Dipendenze:

- Compilatore C++17 e libreria standard C++; nessuna libreria esterna.

## Preparazione

Comandi per una shell Linux/Bash dalla cartella projects/P021. Installare prima il compilatore o SDK indicato nei requisiti. Le versioni documentate non costituiscono una garanzia per toolchain diverse.

Non sono previsti ulteriori comandi di preparazione oltre all’installazione della toolchain indicata.

## Avvio

```bash
g++ -std=c++17 src/traffic.cpp -o traffic
./traffic
```

## Test

```bash
g++ -std=c++17 tests/test_traffic.cpp -o test_progetto
./test_progetto
```

## Perimetro del laboratorio

- Il comando essenziale non riattiva automaticamente le opzioni -Wall -Wextra -Werror -O1 -g -fsanitize=undefined -fno-sanitize-recover=all del collaudo storico.

## Windows

Solo libreria standard C++, senza pthread o API POSIX. Windows nativo plausibile con compilatore C++17. Per riprodurre i controlli GNU/UBSan storici occorre una toolchain che li supporti: WSL è un’opzione, non un requisito del programma. Nessun test Windows nativo è attestato da questo README.

I blocchi di compilazione sono per GNU/Linux: percorsi degli eseguibili, creazione della cartella `build` e opzioni del sanitizer vanno adattati alla toolchain Windows. WSL permette di seguire la stessa sequenza Linux.

## Collaudi documentati

Collaudo storico su Linux: le suite disponibili e i casi aggiuntivi risultano superati. Il riepilogo del gruppo P001–P040 non riporta una data puntuale; questi risultati non sono stati rieseguiti per preparare il README.

Queste istruzioni sono state ricavate dai file e dai collaudi conservati. La preparazione dei README non ha eseguito nuove suite né modificato il codice.
