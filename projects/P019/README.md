# P019: Coda di emergenze in C++ con priority_queue e STL

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P019/README.md) · [Registro del collaudo](../../collaudo/P019/registro.json)

**Sezione:** [Sezione 1: Programmazione, algoritmi e strutture dati](../../docs/CATALOGO.md#sezione-1-programmazione-algoritmi-e-strutture-dati).

**Argomenti:** Strutture dati · Code con priorità.

Sceglie la prossima emergenza con una coda di priorità C++. Il numero di priorità più basso viene servito prima; a pari priorità vale l’ordine di arrivo.

Apri un terminale nella cartella `projects/P019` ed esegui da lì i comandi. I blocchi principali usano Bash su Linux; trovi le indicazioni per Windows nella sezione dedicata.

## Requisiti e versioni

**Tecnologie utilizzate:** C++.

- C++17

Dipendenze:

- g++ con supporto a C++17
- Libreria standard C++

## Preparazione

Installa il compilatore o il kit di sviluppo indicato nei requisiti, poi apri un terminale Bash nella cartella del progetto. Esegui i comandi seguenti per preparare il laboratorio. Le versioni documentate non garantiscono lo stesso comportamento con strumenti diversi.

```bash
mkdir -p build
```

## Avvio

La demo stampa `emergenza`, la descrizione della richiesta con priorità maggiore.

```bash
g++ -std=c++17 -Wall -Wextra -Werror src/dispatcher.cpp -o build/dispatcher
./build/dispatcher
```

## Test

Il programma stampa `P019: priority_queue PASS` se l’ordine delle richieste e il rifiuto della priorità non valida superano i controlli.

```bash
g++ -std=c++17 -Wall -Wextra -Werror -O1 -g -fsanitize=undefined -fno-sanitize-recover=all tests/test_dispatcher.cpp -o build/test_dispatcher
./build/test_dispatcher
```

## Perimetro del laboratorio

- Il programma dimostrativo stampa la descrizione della prima emergenza estratta. I test verificano anche l’ordine delle richieste con la stessa priorità.

## Windows

Il sorgente usa la libreria standard C++ e non richiede interfacce POSIX. Può essere compilato anche con un compilatore C++17 per Windows, adattando le opzioni agli strumenti scelti. Qui non è documentato un collaudo su Windows.

Per usare gli stessi comandi da Windows, scegli WSL con una distribuzione Linux. Se preferisci un compilatore Windows, adatta la creazione della cartella `build`, i percorsi degli eseguibili e le opzioni del sanitizer, lo strumento che rileva alcune operazioni non definite dallo standard.

## Collaudi documentati

**Ultimo collaudo: 30 ottobre 2026 — superato.** Le verifiche del progetto sono riuscite su Ubuntu 24.04 nel [collaudo pubblico P001–P080](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/41134634700), eseguito sul commit `35b49f130493`.

### Prove precedenti

Nel [collaudo del 22 ottobre 2026](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701), le verifiche della versione di allora sono riuscite su Ubuntu 24.04.

Apri **Output verificati** e **Registro del collaudo**, all’inizio di questa pagina, per consultare comandi, esiti e limiti delle prove pubblicate. Esegui i test anche sul tuo computer e ripetili dopo ogni modifica al codice.
