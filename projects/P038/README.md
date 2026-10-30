# P038: Prenotazioni per eventi: requisiti e diagrammi

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P038/README.md) · [Registro del collaudo](../../collaudo/P038/registro.json)

**Sezione:** [Sezione 3: Ingegneria e progettazione del software](../../docs/CATALOGO.md#sezione-3-ingegneria-e-progettazione-del-software).

**Argomenti:** Analisi dei requisiti · UML · Concorrenza.

Gestisci prenotazioni per eventi senza superare i posti disponibili. Il servizio Java protegge le operazioni simultanee sulla stessa istanza; il test concorrente mette alla prova la prenotazione dell’ultimo posto.

Apri un terminale nella cartella `projects/P038` ed esegui da lì i comandi. I blocchi seguenti usano la sintassi di Linux/Bash; per Windows consulta la sezione dedicata.

## Requisiti e versioni

**Tecnologie utilizzate:** Java.

- JDK Java 17 come ambiente didattico; patch del collaudo non registrata

Dipendenze:

- JDK 17 con javac e java; solo libreria standard, senza framework di test esterni.

## Preparazione

Installa il compilatore o il kit di sviluppo (SDK) indicato nei requisiti. Le versioni documentate descrivono gli strumenti usati nei collaudi; con strumenti diversi, verifica il risultato eseguendo i test.

```bash
mkdir -p build
javac -d build src/Ticketing.java tests/TicketingTest.java tests/TicketingConcurrentTest.java
```

## Avvio

```bash
java -cp build Ticketing
```

## Test

Il primo test controlla capienza e annullamento. Il secondo invia 100 richieste concorrenti per un solo posto e verifica che ne riesca esattamente una. Entrambi stampano `PASS` quando i rispettivi controlli sono riusciti.

```bash
java -ea -cp build TicketingTest
java -ea -cp build TicketingConcurrentTest
```

Mantieni `-ea` nei comandi Java: attiva le asserzioni, cioè i controlli che devono riuscire perché il test sia superato.

## Perimetro del laboratorio

- Con l’opzione `-Xlint:all`, il compilatore segnala che alcune classi ausiliarie si trovano nello stesso file sorgente. Nei collaudi conservati questi avvisi non hanno impedito la compilazione e tutti i test registrati sono riusciti.

## Windows

Il programma usa soltanto la libreria standard Java. Il classpath, cioè il percorso in cui Java cerca le classi compilate, contiene una sola cartella. Il codice non richiede funzioni specifiche di Linux e può essere usato con un JDK 17 compatibile; i collaudi documentati in questa pagina non comprendono una prova nativa su Windows.

Nel Prompt dei comandi di Windows, crea la cartella con `if not exist build mkdir build`; in PowerShell usa `New-Item -ItemType Directory -Force build`. Con il JDK installato, i comandi `javac` e `java` riportati sopra restano uguali. Mantieni `-ea` quando esegui i test.

## Collaudi documentati

I materiali conservati documentano un collaudo su Linux con esito positivo per le suite disponibili e le prove aggiuntive. Il riepilogo storico del gruppo P001–P040 non indica una data precisa.

Consulta **Output verificati** e **Registro del collaudo**, all’inizio della pagina, per leggere comandi, ambiente e limiti di ciascuna prova. I risultati documentati descrivono quei collaudi; per verificare la copia che stai usando, esegui i test sul tuo computer.
