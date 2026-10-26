# P041: Motore di notifiche con il pattern Strategy

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../COLLAUDO/P041/README.md) · [Registro del collaudo](../../COLLAUDO/P041/registro.json)

Seleziona strategie di notifica mediante un modello Java locale.

Tutti i comandi partono dalla cartella `projects/P041`. I blocchi seguenti usano la sintassi di Linux/Bash.

## Requisiti e versioni

Linguaggio: Java.

- JDK 17.0.20 (collaudo locale storico)

Dipendenze:

- Libreria standard Java JDK 17 — Nessuna dipendenza esterna o framework di test. Le verifiche usano assert Java.

## Preparazione

Comandi per una shell Linux/Bash dalla cartella projects/P041. Installare prima il compilatore o SDK indicato nei requisiti. Le versioni documentate non costituiscono una garanzia per toolchain diverse.

```bash
mkdir -p build
```

## Avvio

Non è presente un’applicazione dimostrativa autonoma: usare i test sotto come punto di ingresso eseguibile.

## Test

```bash
javac -d build src/Notifications.java tests/NotificationsTest.java
java -ea -cp build NotificationsTest
```

Mantenere `-ea` nei comandi Java: abilita le asserzioni usate dalle verifiche.

## Perimetro del laboratorio

- Non è presente un main applicativo autonomo: compilare e avviare le classi di test dalla cartella del progetto.

## Windows

JDK 17 e comandi javac/java sono plausibili su Windows; i nomi dei sorgenti sono espliciti e il classpath contiene una sola directory. Nessuno script POSIX è richiesto. Nessun test Windows nativo è attestato da questo README.

I blocchi di compilazione sono per GNU/Linux: percorsi degli eseguibili, creazione della cartella `build` e opzioni del sanitizer vanno adattati alla toolchain Windows. WSL permette di seguire la stessa sequenza Linux.

## Collaudi documentati

Collaudo storico del 2026-10-16: Test locali registrati; nessun nuovo test eseguito durante questa revisione.

Queste istruzioni sono state ricavate dai file e dai collaudi conservati. La preparazione dei README non ha eseguito nuove suite né modificato il codice.
