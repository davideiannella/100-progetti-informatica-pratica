# P017: Buffer circolare: gestire dati continui con memoria fissa

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P017/README.md) · [Registro del collaudo](../../collaudo/P017/registro.json)

**Sezione:** [Sezione 1: Programmazione, algoritmi e strutture dati](../../docs/CATALOGO.md#sezione-1-programmazione-algoritmi-e-strutture-dati).

**Argomenti:** Strutture dati · Gestione della memoria.

Conserva un numero limitato di valori e riutilizza le stesse posizioni di memoria. Se il buffer è pieno, rifiuta il nuovo valore senza sovrascrivere quelli in attesa.

Apri un terminale nella cartella `projects/P017` ed esegui da lì i comandi. I blocchi principali usano Bash su Linux; trovi le indicazioni per Windows nella sezione dedicata.

## Requisiti e versioni

**Tecnologie utilizzate:** C.

- C11

Dipendenze:

- gcc con supporto a C11
- Libreria standard C

## Preparazione

Installa il compilatore o il kit di sviluppo indicato nei requisiti, poi apri un terminale Bash nella cartella del progetto. Esegui i comandi seguenti per preparare il laboratorio. Le versioni documentate non garantiscono lo stesso comportamento con strumenti diversi.

```bash
mkdir -p build
```

## Avvio

Per provare il buffer, compila ed esegui il test della sezione seguente. Il sorgente del buffer è una libreria, senza un programma dimostrativo separato.

## Test

Se le operazioni sul buffer rispettano i controlli previsti, il programma stampa `P017: ring buffer PASS`.

```bash
gcc -std=c11 -Wall -Wextra -Werror -O1 -g -fsanitize=undefined -fno-sanitize-recover=all tests/test_ring_buffer.c src/ring_buffer.c -o build/test_ring_buffer
./build/test_ring_buffer
```

## Perimetro del laboratorio

- Il sorgente del buffer è una libreria senza `main`. Il programma da compilare ed eseguire per provarla è `tests/test_ring_buffer.c`.

## Windows

Il sorgente usa soltanto la libreria standard C e può essere compilato anche con un compilatore C11 per Windows. La compatibilità delle opzioni, in particolare `-fsanitize=undefined`, dipende dagli strumenti scelti e va verificata. Qui non è documentato un collaudo su Windows.

Per usare gli stessi comandi da Windows, scegli WSL con una distribuzione Linux. Se preferisci un compilatore Windows, adatta la creazione della cartella `build`, i percorsi degli eseguibili e le opzioni del sanitizer, lo strumento che rileva alcune operazioni non definite dallo standard.

## Collaudi documentati

**Ultimo collaudo: 31 ottobre 2026 — superato.** Le verifiche del progetto sono riuscite su Ubuntu 24.04 nel [collaudo pubblico P001–P080](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/41142475728), eseguito sul commit `c8303920c4f4`.

### Prove precedenti

Nel [collaudo del 22 ottobre 2026](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701), le verifiche della versione di allora sono riuscite su Ubuntu 24.04.

Apri **Output verificati** e **Registro del collaudo**, all’inizio di questa pagina, per consultare comandi, esiti e limiti delle prove pubblicate. Esegui i test anche sul tuo computer e ripetili dopo ogni modifica al codice.
