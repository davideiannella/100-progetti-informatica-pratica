# P015: Chat con client e server TCP

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P015/README.md) · [Registro del collaudo](../../collaudo/P015/registro.json)

**Sezione:** [Sezione 1: Programmazione, algoritmi e strutture dati](../../docs/CATALOGO.md#sezione-1-programmazione-algoritmi-e-strutture-dati).

**Argomenti:** Reti · Comunicazione client e server · Concorrenza.

Scambia messaggi di testo fra client e server TCP sulla stessa macchina. Il server inoltra ogni messaggio a tutti i client collegati; i test verificano anche la chiusura delle connessioni.

Apri un terminale nella cartella `projects/P015` ed esegui da lì i comandi. I blocchi principali usano Bash su Linux; trovi le indicazioni per Windows nella sezione dedicata.

## Requisiti e versioni

**Tecnologie utilizzate:** Java.

- JDK 17 o successivo come base proposta; versione esatta del JDK del collaudo storico non registrata nel riepilogo consultato

Dipendenze:

- JDK con javac e java; solo libreria standard Java

## Preparazione

Installa il compilatore o il kit di sviluppo indicato nei requisiti, poi apri un terminale Bash nella cartella del progetto. Esegui i comandi seguenti per preparare il laboratorio. Le versioni documentate non garantiscono lo stesso comportamento con strumenti diversi.

```bash
mkdir -p build
```

## Avvio

Per provare la chat, esegui i due test della sezione seguente: avviano il server, collegano i client e chiudono le connessioni. Non serve avviare un programma separato.

## Test

Le due prove stampano messaggi con `PASS`: la prima verifica l’inoltro dei messaggi; la seconda controlla UTF-8 e chiusura del server con un client ancora connesso.

```bash
javac -Xlint:all -d build src/ChatServer.java tests/ChatIntegrationTest.java tests/ChatShutdownTest.java
java -ea -cp build ChatIntegrationTest
java -ea -cp build ChatShutdownTest
```

Conserva `-ea` nei comandi Java: abilita le asserzioni, cioè i controlli usati dal programma di verifica.

## Perimetro del laboratorio

- `ChatServer` non contiene un metodo `main`: i due test di integrazione lo avviano e lo chiudono.

## Windows

Puoi preparare il progetto su Windows con JDK 17 e i comandi `javac` e `java` disponibili nel terminale. La compatibilità è dedotta dai sorgenti; qui non è documentato un collaudo su Windows.

Nel Prompt dei comandi di Windows (`cmd.exe`), sostituisci `mkdir -p build` con `if not exist build mkdir build`. I comandi `javac` e `java` restano uguali: nei test conserva `-ea` per abilitare le asserzioni. WSL non è necessario.

## Collaudi documentati

Nel collaudo storico su Linux, le suite disponibili e i casi aggiuntivi hanno superato i controlli previsti. Il riepilogo storico del gruppo P001–P040 non specifica la data delle prove.

Apri **Output verificati** e **Registro del collaudo**, all’inizio di questa pagina, per consultare comandi, esiti e limiti delle prove pubblicate. Esegui i test anche sul tuo computer e ripetili dopo ogni modifica al codice.
