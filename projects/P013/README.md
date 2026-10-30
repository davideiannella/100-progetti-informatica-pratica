# P013: Biblioteca digitale a oggetti

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P013/README.md) · [Registro del collaudo](../../collaudo/P013/registro.json)

**Sezione:** [Sezione 1: Programmazione, algoritmi e strutture dati](../../docs/CATALOGO.md#sezione-1-programmazione-algoritmi-e-strutture-dati).

**Argomenti:** Programmazione a oggetti · Gestione di collezioni.

Registra libri, utenti, prestiti e restituzioni con oggetti Java. Controlla disponibilità e scadenze; i dati restano in memoria durante l’esecuzione.

Apri un terminale nella cartella `projects/P013` ed esegui da lì i comandi. I blocchi principali usano Bash su Linux; trovi le indicazioni per Windows nella sezione dedicata.

## Requisiti e versioni

**Tecnologie utilizzate:** Java.

- JDK 17 o successivo come base proposta; versione esatta del JDK del collaudo storico non registrata nel riepilogo consultato

Dipendenze:

- JDK con javac e java; solo libreria standard Java

## Preparazione

Installa il compilatore o il kit di sviluppo indicato nei requisiti, poi apri un terminale Bash nella cartella del progetto. Esegui i comandi seguenti per preparare il laboratorio. Le versioni documentate non garantiscono lo stesso comportamento con strumenti diversi.

```bash
mkdir -p build
javac -Xlint:all -d build src/LibraryApp.java tests/LibraryTest.java
```

## Avvio

La demo registra un prestito e stampa `Disponibile? false`: il libro risulta già in prestito.

```bash
java -cp build LibraryApp
```

## Test

Il programma di verifica stampa `P013: 5 test PASS` quando supera i controlli previsti su prestiti, restituzioni e disponibilità.

```bash
java -ea -cp build LibraryTest
```

Conserva `-ea` nei comandi Java: abilita le asserzioni, cioè i controlli usati dal programma di verifica.

## Perimetro del laboratorio

- La preparazione compila sia il codice sia i test nella cartella `build`. La demo e le verifiche usano queste classi compilate.

## Windows

Puoi preparare il progetto su Windows con JDK 17 e i comandi `javac` e `java` disponibili nel terminale. La compatibilità è dedotta dai sorgenti; qui non è documentato un collaudo su Windows.

Nel Prompt dei comandi di Windows (`cmd.exe`), sostituisci `mkdir -p build` con `if not exist build mkdir build`. I comandi `javac` e `java` restano uguali: nei test conserva `-ea` per abilitare le asserzioni. WSL non è necessario.

## Collaudi documentati

**Ultimo collaudo: 31 ottobre 2026 — superato.** Le verifiche del progetto sono riuscite su Ubuntu 24.04 nel [collaudo pubblico P001–P080](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/41142475728), eseguito sul commit `c8303920c4f4`.

### Prove precedenti

Nel [collaudo del 22 ottobre 2026](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701), le verifiche della versione di allora sono riuscite su Ubuntu 24.04.

Apri **Output verificati** e **Registro del collaudo**, all’inizio di questa pagina, per consultare comandi, esiti e limiti delle prove pubblicate. Esegui i test anche sul tuo computer e ripetili dopo ogni modifica al codice.
