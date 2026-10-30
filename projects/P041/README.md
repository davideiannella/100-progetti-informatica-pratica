# P041: Motore di notifiche con il pattern Strategy

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P041/README.md) · [Registro del collaudo](../../collaudo/P041/registro.json)

**Sezione:** [Sezione 3: Ingegneria e progettazione del software](../../docs/CATALOGO.md#sezione-3-ingegneria-e-progettazione-del-software).

**Argomenti:** Programmazione a oggetti · Pattern di progettazione.

Scegli il canale email o SMS mantenendo lo stesso servizio di notifica. Il pattern Strategy permette di sostituire il comportamento del canale; qui l’invio è simulato da una stringa.

Apri un terminale nella cartella `projects/P041` ed esegui da lì tutti i comandi. Gli esempi usano Linux e Bash; per Windows, segui anche la sezione dedicata.

## Requisiti e versioni

**Tecnologie utilizzate:** Java.

- JDK 17.0.20 (collaudo locale storico)

Dipendenze:

- Libreria standard Java JDK 17 — Nessuna dipendenza esterna o framework di test. Le verifiche usano assert Java.

## Preparazione

Il JDK è il kit di sviluppo Java e comprende il compilatore `javac` e il comando `java`. Installa la versione indicata nei requisiti, poi crea la cartella `build` con il comando seguente. Le versioni elencate sono quelle dei collaudi documentati; con strumenti diversi occorre ripetere le verifiche.

```bash
mkdir -p build
```

## Avvio

Compila e avvia la dimostrazione dalla cartella del progetto, dopo aver creato `build` come indicato nella preparazione:

```bash
javac -d build src/Notifications.java
java -cp build Notifications
```

Il programma stampa `EMAIL:a@b.it:ciao`: è una notifica simulata, senza invio di un’email reale.

## Test

I test verificano il canale scelto, il destinatario, il messaggio e il rifiuto di un canale non registrato. Se i controlli passano, stampano un messaggio `PASS`.

```bash
javac -d build src/Notifications.java tests/NotificationsTest.java
java -ea -cp build NotificationsTest
```

Mantieni `-ea` nei comandi Java: attiva le asserzioni, cioè i controlli usati dai test.

## Perimetro del laboratorio

- Il metodo `main` di `Notifications` mostra una notifica simulata. I test verificano la scelta dei canali e il rifiuto di un canale non registrato.

## Windows

Per provare il progetto su Windows serve JDK 17. I comandi indicano tutti i file sorgenti e usano una sola cartella per le classi compilate; non servono script POSIX. L’esecuzione nativa su Windows non è stata collaudata nelle prove documentate.

Nel Prompt dei comandi Windows, crea la cartella con `mkdir build` se non esiste, poi usa gli stessi comandi `javac` e `java` riportati sopra. Con WSL puoi seguire l’intera sequenza Linux.

## Collaudi documentati

**Ultimo collaudo: 31 ottobre 2026 — superato.** Le verifiche del progetto sono riuscite su Ubuntu 24.04 nel [collaudo pubblico P001–P080](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/41142475728), eseguito sul commit `c8303920c4f4`.

### Prove precedenti

Collaudo storico del 2026-10-16: Test locali registrati.

Queste istruzioni sono state ricavate dai file e dai collaudi conservati.
