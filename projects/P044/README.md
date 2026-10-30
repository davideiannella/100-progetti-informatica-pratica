# P044: Conservare versioni immutabili dei documenti

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P044/README.md) · [Registro del collaudo](../../collaudo/P044/registro.json)

**Sezione:** [Sezione 3: Ingegneria e progettazione del software](../../docs/CATALOGO.md#sezione-3-ingegneria-e-progettazione-del-software).

**Argomenti:** Versionamento dei dati · Immutabilità · Concorrenza.

Conserva e confronta versioni di documenti nel modello Java.

Apri un terminale nella cartella `projects/P044` ed esegui da lì tutti i comandi. Gli esempi usano Linux e Bash; per Windows, segui anche la sezione dedicata.

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
javac -d build src/DocumentVersioning.java
java -cp build DocumentVersioning
```

Il programma crea il documento `D`, lo aggiorna e stampa `Version[number=2, content=v2, author=luca]`.

## Test

I test controllano le versioni salvate, la copia non modificabile dello storico e 100 aggiornamenti concorrenti. Se i controlli passano, stampano messaggi `PASS`.

```bash
javac -d build src/DocumentVersioning.java tests/DocumentVersioningTest.java tests/DocumentEdgesTest.java
java -ea -cp build DocumentVersioningTest
java -ea -cp build DocumentEdgesTest
```

Mantieni `-ea` nei comandi Java: attiva le asserzioni, cioè i controlli usati dai test.

## Perimetro del laboratorio

- Il metodo `main` di `DocumentVersioning` mostra la creazione e l’aggiornamento di un documento. I test verificano lo storico non modificabile e la numerazione durante gli aggiornamenti concorrenti. I dati restano soltanto in memoria.

## Windows

Per provare il progetto su Windows serve JDK 17. I comandi indicano tutti i file sorgenti e usano una sola cartella per le classi compilate; non servono script POSIX. L’esecuzione nativa su Windows non è stata collaudata nelle prove documentate.

Nel Prompt dei comandi Windows, crea la cartella con `mkdir build` se non esiste, poi usa gli stessi comandi `javac` e `java` riportati sopra. Con WSL puoi seguire l’intera sequenza Linux.

## Collaudi documentati

**Ultimo collaudo: 30 ottobre 2026 — superato.** Le verifiche del progetto sono riuscite su Ubuntu 24.04 nel [collaudo pubblico P001–P080](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/41134634700), eseguito sul commit `35b49f130493`.

### Prove precedenti

Collaudo storico del 2026-10-16: Test locali registrati.

Queste istruzioni sono state ricavate dai file e dai collaudi conservati.
