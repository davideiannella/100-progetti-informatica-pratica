# P032: Grafo di mobilità urbana

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P032/README.md) · [Registro del collaudo](../../collaudo/P032/registro.json)

**Sezione:** [Sezione 2: Database e gestione dei dati](../../docs/CATALOGO.md#sezione-2-database-e-gestione-dei-dati).

**Argomenti:** Database a grafo · Mobilità · Ricerca di percorsi.

Cerchi il percorso con il minor tempo totale fra alcune fermate. Il modello Python lavora in memoria; l’esempio Cypher si esegue separatamente su Neo4j.

Apri un terminale nella cartella `projects/P032` ed esegui da lì i comandi. I blocchi seguenti usano la sintassi di Linux/Bash; per Windows consulta la sezione dedicata.

## Requisiti e versioni

**Tecnologie utilizzate:** Python · Cypher (Neo4j).

- Python 3.12.14
- Neo4j 5.26.0

Dipendenze:

- Libreria standard Python; nessun pacchetto esterno per i test presenti.
- Per cypher/mobility.cypher soltanto: server Neo4j e client Cypher. Nessun driver Neo4j importato dal modello Python.

## Preparazione

Installa Python 3.12, poi crea e attiva l’ambiente virtuale con i comandi seguenti. Dopo l’attivazione, `python` usa l’interprete dell’ambiente `.venv`. Riattiva l’ambiente ogni volta che apri un nuovo terminale. Le versioni elencate descrivono gli ambienti documentati: non sono necessariamente le versioni minime richieste.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
```

## Avvio

Per provare il laboratorio, esegui i test della sezione seguente: creano i dati di esempio e chiamano le operazioni previste. Non è presente un’applicazione dimostrativa separata.

## Test

Il test Python controlla il percorso A–B–C e il costo totale di 12 minuti. Stampa `PASS` se il risultato coincide. La dicitura storica `Cypher STATIC QA` non indica che il test abbia eseguito lo script sul database.

```bash
python tests/test_p032.py
```

## Perimetro del laboratorio

- Il test Python non esegue lo script Cypher: le verifiche del modello e del database restano separate. Il solo log sintetico non permette di ricostruire il comando e la configurazione del client.

## Windows

Il modello Python usa funzioni portabili e `pathlib` per i percorsi; non richiede WSL né funzioni specifiche di Linux. Per la parte Neo4j servono separatamente il database e un client compatibile, oppure un server raggiungibile. Dopo aver attivato l’ambiente, usa il suo comando `python`. I collaudi documentati in questa pagina non comprendono una prova nativa su Windows.

Per preparare Python su Windows, apri il **Prompt dei comandi (cmd.exe)** nella cartella del progetto ed esegui:

```bat
py -3.12 -m venv .venv
.venv\Scripts\activate.bat
```

Dopo l’attivazione, esegui i comandi `python` di installazione, avvio e test indicati sopra. In alternativa, anche da PowerShell, usa direttamente `.\.venv\Scripts\python.exe` al posto di `python`: non devi attivare script né cambiare le regole di esecuzione di PowerShell. Non copiare in PowerShell il comando di attivazione Bash.

## Collaudi documentati

I materiali conservati documentano un collaudo su Linux con esito positivo per le suite disponibili e le prove aggiuntive. Il riepilogo storico del gruppo P001–P040 non indica una data precisa. I test Python e le prove sul database controllano due percorsi distinti: leggi separatamente i rispettivi risultati.

Consulta **Output verificati** e **Registro del collaudo**, all’inizio della pagina, per leggere comandi, ambiente e limiti di ciascuna prova. I risultati documentati descrivono quei collaudi; per verificare la copia che stai usando, esegui i test sul tuo computer.
