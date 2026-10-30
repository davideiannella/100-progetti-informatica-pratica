# P018: Sincronizzare produttore e consumatore

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P018/README.md) · [Registro del collaudo](../../collaudo/P018/registro.json)

**Sezione:** [Sezione 1: Programmazione, algoritmi e strutture dati](../../docs/CATALOGO.md#sezione-1-programmazione-algoritmi-e-strutture-dati).

**Argomenti:** Concorrenza · Thread · Sincronizzazione.

Un produttore inserisce valori in un buffer e un consumatore li estrae. Mutex e variabili di condizione della libreria pthread coordinano le attese quando il buffer è pieno o vuoto.

Apri un terminale nella cartella `projects/P018` ed esegui da lì i comandi. I blocchi principali usano Bash su Linux; trovi le indicazioni per Windows nella sezione dedicata.

## Requisiti e versioni

**Tecnologie utilizzate:** C · pthread · Linux.

- C11

Dipendenze:

- gcc con supporto a C11
- Libreria standard C
- POSIX threads (pthread)
- Linker GNU con --wrap per tests/test_pc_failures.c

## Preparazione

Installa il compilatore o il kit di sviluppo indicato nei requisiti, poi apri un terminale Bash nella cartella del progetto. Esegui i comandi seguenti per preparare il laboratorio. Le versioni documentate non garantiscono lo stesso comportamento con strumenti diversi.

```bash
mkdir -p build
```

## Avvio

La demo produce i numeri da 1 a 100 e stampa `sum=5050` dopo che il consumatore li ha sommati.

```bash
gcc -std=c11 -Wall -Wextra -Werror src/producer_consumer.c -pthread -o build/producer_consumer
./build/producer_consumer
```

## Test

La prima prova stampa `P018: producer-consumer PASS; sum=5050`. La seconda simula errori di inizializzazione e creazione dei thread: se riesce, termina con codice di uscita 0 senza stampare testo.

```bash
gcc -std=c11 -Wall -Wextra -Werror -O1 -g -fsanitize=undefined -fno-sanitize-recover=all tests/test_pc.c -pthread -o build/test_pc
./build/test_pc
gcc -std=c11 -Wall -Wextra -Werror -O1 -g -fsanitize=undefined -fno-sanitize-recover=all tests/test_pc_failures.c -pthread -Wl,--wrap=pthread_mutex_init -Wl,--wrap=pthread_cond_init -Wl,--wrap=pthread_create -o build/test_pc_failures
./build/test_pc_failures
```

## Perimetro del laboratorio

- Il programma dimostrativo stampa la somma dei valori consumati. Le prove separate controllano il risultato e gli errori previsti durante la preparazione dei thread.

## Windows

Per eseguire l’intera suite con gli stessi comandi servono Linux/POSIX, pthread e il linker GNU. Da Windows, usa WSL con una distribuzione Linux e conserva il progetto nel filesystem Linux, non in una cartella montata da `C:`. Qui non sono documentati collaudi su WSL o Windows nativo.

## Collaudi documentati

Nel collaudo storico su Linux, le suite disponibili e i casi aggiuntivi hanno superato i controlli previsti. Il riepilogo storico del gruppo P001–P040 non specifica la data delle prove.

Apri **Output verificati** e **Registro del collaudo**, all’inizio di questa pagina, per consultare comandi, esiti e limiti delle prove pubblicate. Esegui i test anche sul tuo computer e ripetili dopo ogni modifica al codice.
