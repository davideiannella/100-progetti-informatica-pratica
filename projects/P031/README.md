# P031: Salvare le misure di sensori IoT in MongoDB

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P031/README.md) · [Registro del collaudo](../../collaudo/P031/registro.json)

**Sezione:** [Sezione 2: Database e gestione dei dati](../../docs/CATALOGO.md#sezione-2-database-e-gestione-dei-dati).

**Argomenti:** Database NoSQL · IoT simulato · Telemetria.

Controlli misure di sensori, come temperatura e umidità, con un modello Python. Un esempio MongoDB separato mostra come salvare le letture e cercare le più recenti di un dispositivo.

Apri un terminale nella cartella `projects/P031` ed esegui da lì i comandi. I blocchi seguenti usano la sintassi di Linux/Bash; per Windows consulta la sezione dedicata.

## Requisiti e versioni

**Tecnologie utilizzate:** Python · MongoDB · JavaScript (mongosh).

- Python 3.12.14
- MongoDB 8.0.14

Dipendenze:

- Libreria standard Python; nessun pacchetto esterno per i test presenti.
- Per mongo/telemetry_examples.js soltanto: server MongoDB e client mongosh. Il modello Python non importa driver MongoDB.

## Preparazione

Installa Python 3.12, poi crea e attiva l’ambiente virtuale con i comandi seguenti. Dopo l’attivazione, `python` usa l’interprete dell’ambiente `.venv`. Riattiva l’ambiente ogni volta che apri un nuovo terminale. Le versioni elencate descrivono gli ambienti documentati: non sono necessariamente le versioni minime richieste.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
```

## Avvio

Per provare il laboratorio, esegui i test della sezione seguente: creano i dati di esempio e chiamano le operazioni previste. Non è presente un’applicazione dimostrativa separata.

## Test

```bash
python tests/test_invalid_metrics.py
python tests/test_p031.py
```

Questi test verificano la validazione delle misure e la costruzione del documento Python. Non richiedono un database e non eseguono `mongo/telemetry_examples.js`: il modello Python e lo script JavaScript sono due percorsi di esecuzione separati. La prova sul database reale è descritta nei collaudi documentati sotto.

## Perimetro del laboratorio

- Il modello Python rappresenta il timestamp, cioè la data e l’ora della lettura, come stringa ISO. Lo script `mongosh` usa invece BSON Date. Sono due percorsi separati: per collegarli serve una conversione esplicita del tipo.
- Il log sintetico non specifica la versione di `mongosh` né la configurazione del server.

## Windows

Il modello Python usa funzioni portabili e `pathlib` per i percorsi; non richiede WSL né funzioni specifiche di Linux. Per la parte MongoDB servono separatamente il database e un client compatibile, oppure un server raggiungibile. Dopo aver attivato l’ambiente, usa il suo comando `python`. I collaudi documentati in questa pagina non comprendono una prova nativa su Windows.

Per preparare Python su Windows, apri il **Prompt dei comandi (cmd.exe)** nella cartella del progetto ed esegui:

```bat
py -3.12 -m venv .venv
.venv\Scripts\activate.bat
```

Dopo l’attivazione, esegui i comandi `python` di installazione, avvio e test indicati sopra. In alternativa, anche da PowerShell, usa direttamente `.\.venv\Scripts\python.exe` al posto di `python`: non devi attivare script né cambiare le regole di esecuzione di PowerShell. Non copiare in PowerShell il comando di attivazione Bash.

## Collaudi documentati

**Ultimo collaudo: 30 ottobre 2026 — superato.** Le verifiche del progetto sono riuscite su Ubuntu 24.04 nel [collaudo pubblico P001–P080](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/41134634700), eseguito sul commit `35b49f130493`.

### Prove precedenti

Nel [collaudo del 22 ottobre 2026](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701), le verifiche della versione di allora sono riuscite su Ubuntu 24.04.

Nel [collaudo automatizzato del 22 ottobre 2026](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701), il runner ha eseguito lo script originale `mongo/telemetry_examples.js` tramite `mongosh` su MongoDB 8.0.14, avviato in un container Docker. Tutte le 12 asserzioni sul database reale sono risultate superate: verificano la versione del motore, l’inserimento, i tipi BSON, l’indice composto e i risultati della query con filtro per dispositivo, ordinamento temporale e limite. Le due suite Python sono state eseguite separatamente. Le evidenze sono nel [registro P031](../../collaudo/P031/registro.json) e nell’[output della prova sul motore](../../collaudo/P031/streams/003_step_3.stdout.txt); la procedura è nella funzione `engine_suite` del [runner](../../tools/ci_p001_p040/runner.py).

La dicitura storica `MongoDB script STATIC QA` è parte del messaggio stampato da `test_p031.py`: quel test non legge né esegue lo script MongoDB. L’esecuzione sul database è documentata separatamente come `engine_suite` nel registro.

Consulta **Output verificati** e **Registro del collaudo**, all’inizio della pagina, per leggere comandi, ambiente e limiti di ciascuna prova. I risultati documentati descrivono quei collaudi; per verificare la copia che stai usando, esegui i test sul tuo computer.
