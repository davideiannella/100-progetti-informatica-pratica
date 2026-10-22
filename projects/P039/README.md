# P039 — Food delivery e confini tra servizi

Modella ordini di consegna e separazione delle responsabilità applicative.

Tutti i comandi partono dalla cartella `projects/P039`. I blocchi seguenti usano la sintassi di Linux/Bash.

## Requisiti e versioni

Linguaggio: Java.

- JDK Java 17 come ambiente didattico; patch del collaudo non registrata

Dipendenze:

- JDK 17 con javac e java; solo libreria standard, senza framework di test esterni.

## Preparazione

Comandi per una shell Linux/Bash dalla cartella projects/P039. Installare prima il compilatore o SDK indicato nei requisiti. Le versioni documentate non costituiscono una garanzia per toolchain diverse.

```bash
mkdir -p build
javac -d build src/FoodDelivery.java tests/FoodDeliveryTest.java tests/FoodDeliveryLimitsTest.java
```

## Avvio

```bash
java -cp build FoodDelivery
```

## Test

```bash
java -ea -cp build FoodDeliveryTest
java -ea -cp build FoodDeliveryLimitsTest
```

Mantenere `-ea` nei comandi Java: abilita le asserzioni usate dalle verifiche.

## Perimetro del laboratorio

- La compilazione storica con -Xlint:all segnala classi ausiliarie nello stesso sorgente; tutti i test registrati sono passati. Nessuna modifica al codice proposta.

## Windows

Solo libreria standard Java e classpath con un’unica cartella. Nessun Bash/POSIX. Windows nativo plausibile con JDK 17, non verificato. Nessun test Windows nativo è attestato da questo README.

I blocchi di compilazione sono per GNU/Linux: percorsi degli eseguibili, creazione della cartella `build` e opzioni del sanitizer vanno adattati alla toolchain Windows. WSL permette di seguire la stessa sequenza Linux.

## Collaudi documentati

Collaudo storico su Linux: le suite disponibili e i casi aggiuntivi risultano superati. Il riepilogo del gruppo P001–P040 non riporta una data puntuale; questi risultati non sono stati rieseguiti per preparare il README.

Queste istruzioni sono state ricavate dai file e dai collaudi conservati. La preparazione dei README non ha eseguito nuove suite né modificato il codice.
