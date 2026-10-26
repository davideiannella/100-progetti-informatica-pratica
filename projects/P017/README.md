# P017: Buffer circolare: gestire dati continui con memoria fissa

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P017/README.md) · [Registro del collaudo](../../collaudo/P017/registro.json)

**Sezione:** [Sezione 1: Programmazione, algoritmi e strutture dati](../../docs/CATALOGO.md#sezione-1-programmazione-algoritmi-e-strutture-dati).

**Argomenti:** Strutture dati · Gestione della memoria.

Implementa un buffer circolare con capacità fissa e ne verifica le operazioni.

Tutti i comandi partono dalla cartella `projects/P017`. I blocchi seguenti usano la sintassi di Linux/Bash.

## Requisiti e versioni

Linguaggio: C.

- C11

Dipendenze:

- gcc con supporto a C11
- Libreria standard C

## Preparazione

Comandi per una shell Linux/Bash dalla cartella projects/P017. Installare prima il compilatore o SDK indicato nei requisiti. Le versioni documentate non costituiscono una garanzia per toolchain diverse.

```bash
mkdir -p build
```

## Avvio

Non è presente un’applicazione dimostrativa autonoma: usare i test sotto come punto di ingresso eseguibile.

## Test

```bash
gcc -std=c11 -Wall -Wextra -Werror -O1 -g -fsanitize=undefined -fno-sanitize-recover=all tests/test_ring_buffer.c src/ring_buffer.c -o build/test_ring_buffer
./build/test_ring_buffer
```

## Perimetro del laboratorio

- Il sorgente è una libreria senza main; il programma eseguibile è tests/test_ring_buffer.c.

## Windows

Windows nativo plausibile con un compilatore C11: il sorgente usa solo la libreria standard. La sequenza GNU con -fsanitize=undefined va verificata per la toolchain scelta; per riprodurre il collaudo GNU/Linux usare WSL. Nessun test Windows eseguito. Nessun test Windows nativo è attestato da questo README.

I blocchi di compilazione sono per GNU/Linux: percorsi degli eseguibili, creazione della cartella `build` e opzioni del sanitizer vanno adattati alla toolchain Windows. WSL permette di seguire la stessa sequenza Linux.

## Collaudi documentati

Collaudo storico su Linux: le suite disponibili e i casi aggiuntivi risultano superati. Il riepilogo del gruppo P001–P040 non riporta una data puntuale; questi risultati non sono stati rieseguiti per preparare il README.

Queste istruzioni sono state ricavate dai file e dai collaudi conservati. La preparazione dei README non ha eseguito nuove suite né modificato il codice.
