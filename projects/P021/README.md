# P021: Simulare una coda di traffico

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P021/README.md) · [Registro del collaudo](../../collaudo/P021/registro.json)

**Sezione:** [Sezione 1: Programmazione, algoritmi e strutture dati](../../docs/CATALOGO.md#sezione-1-programmazione-algoritmi-e-strutture-dati).

**Argomenti:** Simulazione · Gestione delle code.

Simuli una corsia con un solo punto di servizio. Il programma conta i veicoli che terminano entro un istante scelto e calcola la loro attesa media.

Apri un terminale nella cartella `projects/P021` ed esegui da lì i comandi. I blocchi seguenti usano la sintassi di Linux/Bash; per Windows consulta la sezione dedicata.

## Requisiti e versioni

**Tecnologie utilizzate:** C++.

- Standard C++17.

Dipendenze:

- Compilatore C++17 e libreria standard C++; nessuna libreria esterna.

## Preparazione

Installa il compilatore o il kit di sviluppo (SDK) indicato nei requisiti. Le versioni documentate descrivono gli strumenti usati nei collaudi; con strumenti diversi, verifica il risultato eseguendo i test.

Dopo l’installazione degli strumenti richiesti, puoi passare ai comandi seguenti.

## Avvio

```bash
g++ -std=c++17 src/traffic.cpp -o traffic
./traffic
```

## Test

Il test controlla i tre veicoli dell’esempio, l’attesa media, la coda vuota e il rifiuto di un arrivo negativo. La scritta `PASS` indica che questi controlli sono riusciti.

```bash
g++ -std=c++17 tests/test_traffic.cpp -o test_progetto
./test_progetto
```

## Perimetro del laboratorio

- Il comando di compilazione mostrato sopra è quello essenziale. Non include le opzioni aggiuntive usate nel collaudo storico: `-Wall -Wextra -Werror -O1 -g -fsanitize=undefined -fno-sanitize-recover=all`. Per riprodurre anche quei controlli, serve un compilatore che le supporti.

## Windows

Il programma usa soltanto la libreria standard C++, senza `pthread` o funzioni POSIX specifiche dei sistemi Unix. Può quindi essere compilato con strumenti C++17 compatibili su Windows, ma questa pagina non documenta un collaudo nativo Windows. Per ripetere anche i controlli GNU/UBSan del collaudo storico servono strumenti che li supportino. WSL offre un ambiente Linux su Windows ed è una possibilità, non un requisito del programma.

I comandi di compilazione mostrati usano la sintassi GNU/Linux. Su Windows adatta i percorsi degli eseguibili e le opzioni aggiuntive agli strumenti scelti. Con WSL puoi seguire la stessa sequenza Linux.

## Collaudi documentati

**Ultimo collaudo: 30 ottobre 2026 — superato.** Le verifiche del progetto sono riuscite su Ubuntu 24.04 nel [collaudo pubblico P001–P080](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/41134634700), eseguito sul commit `35b49f130493`.

### Prove precedenti

Nel [collaudo del 22 ottobre 2026](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701), le verifiche della versione di allora sono riuscite su Ubuntu 24.04.

Consulta **Output verificati** e **Registro del collaudo**, all’inizio della pagina, per leggere comandi, ambiente e limiti di ciascuna prova. I risultati documentati descrivono quei collaudi; per verificare la copia che stai usando, esegui i test sul tuo computer.
