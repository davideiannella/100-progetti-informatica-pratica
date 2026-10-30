# P039: Consegne a domicilio e separazione dei servizi

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P039/README.md) · [Registro del collaudo](../../collaudo/P039/registro.json)

**Sezione:** [Sezione 3: Ingegneria e progettazione del software](../../docs/CATALOGO.md#sezione-3-ingegneria-e-progettazione-del-software).

**Argomenti:** Architettura software · Separazione delle responsabilità.

Separi la gestione dello stato degli ordini dalla stima del tempo di consegna. Le due classi Java lavorano nello stesso programma: il laboratorio non realizza servizi distribuiti.

Apri un terminale nella cartella `projects/P039` ed esegui da lì i comandi. I blocchi seguenti usano la sintassi di Linux/Bash; per Windows consulta la sezione dedicata.

## Requisiti e versioni

**Tecnologie utilizzate:** Java.

- JDK Java 17 come ambiente didattico; patch del collaudo non registrata

Dipendenze:

- JDK 17 con javac e java; solo libreria standard, senza framework di test esterni.

## Preparazione

Installa il compilatore o il kit di sviluppo (SDK) indicato nei requisiti. Le versioni documentate descrivono gli strumenti usati nei collaudi; con strumenti diversi, verifica il risultato eseguendo i test.

```bash
mkdir -p build
javac -d build src/FoodDelivery.java tests/FoodDeliveryTest.java tests/FoodDeliveryLimitsTest.java
```

## Avvio

```bash
java -cp build FoodDelivery
```

## Test

Il primo test controlla lo stato dell’ordine e la stima della consegna. Il secondo verifica il rifiuto di uno stato nullo e di un calcolo che supera il limite dei numeri interi, chiamato overflow. Entrambi stampano `PASS` se i controlli riescono.

```bash
java -ea -cp build FoodDeliveryTest
java -ea -cp build FoodDeliveryLimitsTest
```

Mantieni `-ea` nei comandi Java: attiva le asserzioni, cioè i controlli che devono riuscire perché il test sia superato.

## Perimetro del laboratorio

- Con l’opzione `-Xlint:all`, il compilatore segnala che alcune classi ausiliarie si trovano nello stesso file sorgente. Nei collaudi conservati questi avvisi non hanno impedito la compilazione e tutti i test registrati sono riusciti.

## Windows

Il programma usa soltanto la libreria standard Java. Il classpath, cioè il percorso in cui Java cerca le classi compilate, contiene una sola cartella. Il codice non richiede funzioni specifiche di Linux e può essere usato con un JDK 17 compatibile; i collaudi documentati in questa pagina non comprendono una prova nativa su Windows.

Nel Prompt dei comandi di Windows, crea la cartella con `if not exist build mkdir build`; in PowerShell usa `New-Item -ItemType Directory -Force build`. Con il JDK installato, i comandi `javac` e `java` riportati sopra restano uguali. Mantieni `-ea` quando esegui i test.

## Collaudi documentati

**Ultimo collaudo: 30 ottobre 2026 — superato.** Le verifiche del progetto sono riuscite su Ubuntu 24.04 nel [collaudo pubblico P001–P080](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/41134634700), eseguito sul commit `35b49f130493`.

### Prove precedenti

Nel [collaudo del 22 ottobre 2026](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701), le verifiche della versione di allora sono riuscite su Ubuntu 24.04.

Consulta **Output verificati** e **Registro del collaudo**, all’inizio della pagina, per leggere comandi, ambiente e limiti di ciascuna prova. I risultati documentati descrivono quei collaudi; per verificare la copia che stai usando, esegui i test sul tuo computer.
