# P019: Coda di emergenze in C++ con priority_queue e STL

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../COLLAUDO/P019/README.md) · [Registro del collaudo](../../COLLAUDO/P019/registro.json)

Gestisce una coda di emergenze con le strutture della libreria standard C++.

Tutti i comandi partono dalla cartella `projects/P019`. I blocchi seguenti usano la sintassi di Linux/Bash.

## Requisiti e versioni

Linguaggio: C++.

- C++17

Dipendenze:

- g++ con supporto a C++17
- Libreria standard C++

## Preparazione

Comandi per una shell Linux/Bash dalla cartella projects/P019. Installare prima il compilatore o SDK indicato nei requisiti. Le versioni documentate non costituiscono una garanzia per toolchain diverse.

```bash
mkdir -p build
```

## Avvio

```bash
g++ -std=c++17 -Wall -Wextra -Werror src/dispatcher.cpp -o build/dispatcher
./build/dispatcher
```

## Test

```bash
g++ -std=c++17 -Wall -Wextra -Werror -O1 -g -fsanitize=undefined -fno-sanitize-recover=all tests/test_dispatcher.cpp -o build/test_dispatcher
./build/test_dispatcher
```

## Perimetro del laboratorio

- Il main dimostrativo stampa la descrizione della prima emergenza estratta. Comando derivato dal sorgente.

## Windows

Windows nativo plausibile con un compilatore C++17: non vi sono dipendenze POSIX. I flag GNU, il sanitizer e il percorso di avvio richiedono una toolchain compatibile o adattamenti; WSL permette di seguire la sequenza GNU/Linux. Nessun test Windows eseguito. Nessun test Windows nativo è attestato da questo README.

I blocchi di compilazione sono per GNU/Linux: percorsi degli eseguibili, creazione della cartella `build` e opzioni del sanitizer vanno adattati alla toolchain Windows. WSL permette di seguire la stessa sequenza Linux.

## Collaudi documentati

Collaudo storico su Linux: le suite disponibili e i casi aggiuntivi risultano superati. Il riepilogo del gruppo P001–P040 non riporta una data puntuale; questi risultati non sono stati rieseguiti per preparare il README.

Queste istruzioni sono state ricavate dai file e dai collaudi conservati. La preparazione dei README non ha eseguito nuove suite né modificato il codice.
