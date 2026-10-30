# P014: Prenotazioni concorrenti senza duplicati

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P014/README.md) · [Registro del collaudo](../../collaudo/P014/registro.json)

**Sezione:** [Sezione 1: Programmazione, algoritmi e strutture dati](../../docs/CATALOGO.md#sezione-1-programmazione-algoritmi-e-strutture-dati).

**Argomenti:** Concorrenza · Sincronizzazione.

Gestisce più richieste di prenotazione dello stesso posto. Un lock per posto protegge il controllo e l’assegnazione, così nella stessa istanza del servizio una sola richiesta riceve conferma.

Apri un terminale nella cartella `projects/P014` ed esegui da lì i comandi. I blocchi principali usano Bash su Linux; trovi le indicazioni per Windows nella sezione dedicata.

## Requisiti e versioni

**Tecnologie utilizzate:** Java.

- JDK 17 o successivo come base proposta; versione esatta del JDK del collaudo storico non registrata nel riepilogo consultato

Dipendenze:

- JDK con javac e java; solo libreria standard Java

## Preparazione

Installa il compilatore o il kit di sviluppo indicato nei requisiti, poi apri un terminale Bash nella cartella del progetto. Esegui i comandi seguenti per preparare il laboratorio. Le versioni documentate non garantiscono lo stesso comportamento con strumenti diversi.

```bash
mkdir -p build
javac -Xlint:all -d build src/SeatBooking.java tests/SeatBookingTest.java
```

## Avvio

La demo prenota un posto libero e stampa `true`.

```bash
java -cp build SeatBooking
```

## Test

Il test stampa `PASS` e indica una sola prenotazione riuscita sullo stesso posto, dopo cento richieste concorrenti.

```bash
java -ea -cp build SeatBookingTest
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
