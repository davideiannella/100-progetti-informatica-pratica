# P014: Prenotazioni concorrenti senza duplicati

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P014/README.md) · [Registro del collaudo](../../collaudo/P014/registro.json)

**Sezione:** [Sezione 1: Programmazione, algoritmi e strutture dati](../../docs/CATALOGO.md#sezione-1-programmazione-algoritmi-e-strutture-dati).

**Argomenti:** Concorrenza · Sincronizzazione.

Verifica prenotazioni concorrenti e prevenzione delle duplicazioni.

Tutti i comandi partono dalla cartella `projects/P014`. I blocchi seguenti usano la sintassi di Linux/Bash.

## Requisiti e versioni

Linguaggio: Java.

- JDK 17 o successivo come base proposta; versione esatta del JDK del collaudo storico non registrata nel riepilogo consultato

Dipendenze:

- JDK con javac e java; solo libreria standard Java

## Preparazione

Comandi per una shell Linux/Bash dalla cartella projects/P014. Installare prima il compilatore o SDK indicato nei requisiti. Le versioni documentate non costituiscono una garanzia per toolchain diverse.

```bash
mkdir -p build
javac -Xlint:all -d build src/SeatBooking.java tests/SeatBookingTest.java
```

## Avvio

```bash
java -cp build SeatBooking
```

## Test

```bash
java -ea -cp build SeatBookingTest
```

Mantenere `-ea` nei comandi Java: abilita le asserzioni usate dalle verifiche.

## Perimetro del laboratorio

- La preparazione compila sorgenti e test; la demo e le verifiche usano le classi così prodotte.

## Windows

Windows nativo plausibile con JDK 17 e javac/java nel PATH. I comandi relativi non richiedono Bash o WSL. Compatibilità dedotta dai file, non collaudata su Windows. Nessun test Windows nativo è attestato da questo README.

I blocchi di compilazione sono per GNU/Linux: percorsi degli eseguibili, creazione della cartella `build` e opzioni del sanitizer vanno adattati alla toolchain Windows. WSL permette di seguire la stessa sequenza Linux.

## Collaudi documentati

Collaudo storico su Linux: le suite disponibili e i casi aggiuntivi risultano superati. Il riepilogo del gruppo P001–P040 non riporta una data puntuale; questi risultati non sono stati rieseguiti per preparare il README.

Queste istruzioni sono state ricavate dai file e dai collaudi conservati. La preparazione dei README non ha eseguito nuove suite né modificato il codice.
