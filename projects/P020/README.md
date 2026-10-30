# P020: Gestire la memoria in C++ con RAII e smart pointer

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P020/README.md) · [Registro del collaudo](../../collaudo/P020/registro.json)

**Sezione:** [Sezione 1: Programmazione, algoritmi e strutture dati](../../docs/CATALOGO.md#sezione-1-programmazione-algoritmi-e-strutture-dati).

**Argomenti:** Programmazione a oggetti · Gestione della memoria · Gestione delle risorse.

Gestisce un piccolo inventario con `unique_ptr`, che rende esplicito chi possiede un articolo e ne libera automaticamente la memoria. I test controllano anche duplicati, quantità e overflow.

Apri un terminale nella cartella `projects/P020` ed esegui da lì i comandi. I blocchi principali usano Bash su Linux; trovi le indicazioni per Windows nella sezione dedicata.

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

La demo inserisce un articolo e stampa `1`, il numero di articoli presenti nell’inventario.

```bash
g++ -std=c++17 -Wall -Wextra -Werror src/inventory.cpp -o build/inventory
./build/inventory
```

## Test

La prima prova stampa `P020: RAII unique_ptr PASS`. La seconda verifica il limite della quantità: se riesce, termina con codice di uscita 0 senza stampare testo.

```bash
g++ -std=c++17 -Wall -Wextra -Werror -O1 -g -fsanitize=undefined -fno-sanitize-recover=all tests/test_inventory.cpp -o build/test_inventory
./build/test_inventory
g++ -std=c++17 -Wall -Wextra -Werror -O1 -g -fsanitize=undefined -fno-sanitize-recover=all tests/test_inventory_limits.cpp -o build/test_inventory_limits
./build/test_inventory_limits
```

## Perimetro del laboratorio

- Il programma dimostrativo inserisce un articolo e stampa quanti articoli contiene l’inventario. I test controllano anche ricerche, duplicati e aggiornamenti della quantità.

## Windows

Il sorgente usa `unique_ptr`, `vector` e `numeric_limits`, che appartengono alla libreria standard C++. Può essere compilato anche con un compilatore C++17 per Windows, adattando le opzioni agli strumenti scelti. Qui non è documentato un collaudo su Windows.

Per usare gli stessi comandi da Windows, scegli WSL con una distribuzione Linux. Se preferisci un compilatore Windows, adatta la creazione della cartella `build`, i percorsi degli eseguibili e le opzioni del sanitizer, lo strumento che rileva alcune operazioni non definite dallo standard.

## Collaudi documentati

Nel collaudo storico su Linux, le suite disponibili e i casi aggiuntivi hanno superato i controlli previsti. Il riepilogo storico del gruppo P001–P040 non specifica la data delle prove.

Apri **Output verificati** e **Registro del collaudo**, all’inizio di questa pagina, per consultare comandi, esiti e limiti delle prove pubblicate. Esegui i test anche sul tuo computer e ripetili dopo ogni modifica al codice.
