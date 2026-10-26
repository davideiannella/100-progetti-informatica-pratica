# P020: Memoria C++ con RAII e smart pointer

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P020/README.md) · [Registro del collaudo](../../collaudo/P020/registro.json)

**Sezione:** [Sezione 1: Programmazione, algoritmi e strutture dati](../../docs/CATALOGO.md#sezione-1-programmazione-algoritmi-e-strutture-dati).

**Argomenti:** Programmazione a oggetti · Gestione della memoria · Gestione delle risorse.

Sperimenta proprietà delle risorse e gestione della memoria con RAII e smart pointer.

Tutti i comandi partono dalla cartella `projects/P020`. I blocchi seguenti usano la sintassi di Linux/Bash.

## Requisiti e versioni

Linguaggio: C++.

- C++17

Dipendenze:

- g++ con supporto a C++17
- Libreria standard C++

## Preparazione

Comandi per una shell Linux/Bash dalla cartella projects/P020. Installare prima il compilatore o SDK indicato nei requisiti. Le versioni documentate non costituiscono una garanzia per toolchain diverse.

```bash
mkdir -p build
```

## Avvio

```bash
g++ -std=c++17 -Wall -Wextra -Werror src/inventory.cpp -o build/inventory
./build/inventory
```

## Test

```bash
g++ -std=c++17 -Wall -Wextra -Werror -O1 -g -fsanitize=undefined -fno-sanitize-recover=all tests/test_inventory.cpp -o build/test_inventory
./build/test_inventory
g++ -std=c++17 -Wall -Wextra -Werror -O1 -g -fsanitize=undefined -fno-sanitize-recover=all tests/test_inventory_limits.cpp -o build/test_inventory_limits
./build/test_inventory_limits
```

## Perimetro del laboratorio

- Il main dimostrativo inserisce un articolo e stampa la dimensione dell’inventario. Comando derivato dal sorgente.

## Windows

Windows nativo plausibile con un compilatore C++17: unique_ptr, vector e numeric_limits appartengono alla libreria standard. I flag GNU, il sanitizer e il percorso di avvio richiedono una toolchain compatibile o adattamenti; WSL permette di seguire la sequenza GNU/Linux. Nessun test Windows eseguito. Nessun test Windows nativo è attestato da questo README.

I blocchi di compilazione sono per GNU/Linux: percorsi degli eseguibili, creazione della cartella `build` e opzioni del sanitizer vanno adattati alla toolchain Windows. WSL permette di seguire la stessa sequenza Linux.

## Collaudi documentati

Collaudo storico su Linux: le suite disponibili e i casi aggiuntivi risultano superati. Il riepilogo del gruppo P001–P040 non riporta una data puntuale; questi risultati non sono stati rieseguiti per preparare il README.

Queste istruzioni sono state ricavate dai file e dai collaudi conservati. La preparazione dei README non ha eseguito nuove suite né modificato il codice.
