# Preparare l’ambiente di esecuzione

[Torna al README](../README.md) · [Catalogo dei progetti](CATALOGO.md) · [Esiti e log](../collaudi/README.md)

Parti dal README del laboratorio scelto. I suoi comandi si eseguono dalla cartella `projects/Pnnn`, salvo indicazione diversa; i comandi aggregati in questa pagina si eseguono invece dalla **radice del repository**. Non occorre installare tutti i linguaggi e tutti i servizi per svolgere un singolo progetto.

## Scegliere il sistema

| Caso | Ambiente da usare |
|---|---|
| P081–P100 | Python 3.12 o 3.13 su Linux oppure Windows nativo; la matrice pubblica verifica entrambi |
| P001–P080 in generale | Linux/Ubuntu per riprodurre le sequenze Bash e i collaudi pubblici; l’eventuale portabilità Windows è descritta nel README del singolo progetto |
| P016 | Linux: il monitor legge `/proc` e osserva i processi di quell’ambiente |
| P018 | Linux/POSIX con `pthread` e toolchain GNU per eseguire la suite invariata |
| P067 e P069 | Linux con filesystem POSIX per i test di permessi; da Windows usare WSL con file nel filesystem Linux |
| P054–P056 | Runtime per container Linux; Docker, Compose e Kubernetes richiedono preparazione aggiuntiva |

**WSL esegue Linux su Windows: non è una prova Windows nativa.** Per lavorare da WSL, clona il repository in una cartella come `~/progetti/100-progetti-informatica-pratica`, evitando `/mnt/c` per i laboratori sui permessi. Installa gli strumenti nella distribuzione Linux e crea lì l’ambiente virtuale; non riutilizzare una `.venv` creata su Windows.

I restanti progetti Python, Java o .NET possono usare API portabili, ma la lettura dei sorgenti non sostituisce una prova sul sistema scelto. P058 richiede inoltre un filesystem che supporti gli hard link; per P063 il runtime Python deve includere SQLite e `hashlib.scrypt`. I dettagli restano nei rispettivi README.

## Python su Linux o WSL

Installa prima la versione di Python indicata dal progetto, con il modulo `venv` disponibile. Per un laboratorio Python, dalla sua cartella:

```bash
python3.12 --version
python3.12 -m venv .venv
. .venv/bin/activate
python --version
```

Ora `python` e `python -m pip` usano quell’ambiente. Esegui le installazioni richieste dal README, quindi avvio e test. Per esempio, dalla cartella `projects/P001`:

```bash
python tests/test_queue_manager.py
```

Riattiva l’ambiente quando apri un nuovo terminale. Per P081–P100 puoi usare `python3.13` al posto di `python3.12`, creando una nuova `.venv` dedicata.

## Python su Windows nativo

Installa Python nella versione indicata dal laboratorio. Questi comandi presuppongono che il selettore `py -3.12` trovi Python 3.12; se non è disponibile, usa il percorso dell’interprete installato e verifica la versione con `--version`.

Dal **Prompt dei comandi**, nella cartella del progetto:

```bat
py -3.12 -m venv .venv
.venv\Scripts\activate.bat
python --version
```

Dopo l’attivazione usa i comandi `python` del README. Da **PowerShell** puoi richiamare direttamente l’interprete, senza attivare script:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe --version
```

Sostituisci quindi `python` con `.\.venv\Scripts\python.exe` nei comandi di installazione e test. Per esempio, dalla cartella `projects/P081`:

```powershell
.\.venv\Scripts\python.exe -B run_tests.py
```

L’attivazione Bash `. .venv/bin/activate` non è un comando PowerShell. Gli esempi di compilazione GNU/Linux possono richiedere anche cambiamenti a percorsi, creazione delle cartelle e opzioni del compilatore: WSL permette di seguire quella sequenza nell’ambiente Linux.

## Dipendenze Python

Installa solo quanto richiesto dal progetto, con `python -m pip` dell’ambiente scelto. I due file condivisi sono:

- [requirements-p061-p080.txt](../requirements-p061-p080.txt), per i laboratori del gruppo P061–P080 che li richiedono;
- [requirements-p081-p100.txt](../requirements-p081-p100.txt), per la verifica completa P081–P100.

Dalla radice del repository, con un ambiente virtuale attivo, la verifica aggregata P081–P100 si prepara ed esegue così:

```text
python -m pip install -r requirements-p081-p100.txt
python -B tools/collaudo_p081_p100.py
```

Il comando verifica il manifest, compila i file Python ed esegue le venti suite. Scrive i risultati locali in `test-results`. Per un solo progetto entra invece nella sua cartella e segui i suoi requisiti e il comando `run_tests.py`.

Non tutti i laboratori hanno dipendenze esterne, e i requisiti di P001–P060 non sono raccolti nei due file condivisi. Gli esempi aggiuntivi P067–P072 si avviano con `python -B worked_example.py`, quelli P073–P076 con `python -B examples.py`, dalla cartella corrispondente; la suite resta `python -B run_tests.py`.

## Altri linguaggi e servizi

| Gruppo | Preparazione specifica |
|---|---|
| Java P013–P015, P038–P039, P041 e P044 | JDK 17 con `javac` e `java`; il solo runtime Java non basta a compilare |
| C P016–P018 | Compilatore C11; per P018 supporto `pthread` e linker GNU |
| C++ P019–P021 | Compilatore C++17; le opzioni GNU e UBSan richiedono la toolchain corrispondente |
| .NET P022–P023, P040 e P042 | SDK .NET 8 per i progetti `net8.0`; P023 usa anche Python per la prova HTTP |
| SQLite P024–P030, P033 e P035 | Modulo `sqlite3` di Python; gli schemi vengono usati dai test del progetto |
| MongoDB P031 e Neo4j P032 | Le prove del modello Python e quelle del motore reale sono distinte; per i motori servono server e client descritti nel README |
| P054 | Dipendenze Python del progetto; Docker serve per costruire ed eseguire il container |
| P055 | Docker Compose e stack Nginx–API–PostgreSQL; l’esercizio SQLite locale è una verifica separata |
| P056 | Docker, `kubectl` e un cluster Kubernetes di laboratorio; seguire le istruzioni per immagini, deployment e controlli di salute |

Per i container su Windows è possibile usare Docker Desktop con backend WSL 2 e container Linux. Consulta la documentazione ufficiale per i requisiti e l’integrazione con la distribuzione scelta. Una verifica del file YAML o un test Python locale non dimostrano l’avvio di Docker, Compose o Kubernetes.

Le versioni correttive riportate nei README e nei log identificano esecuzioni documentate. Per riprodurle confronta anche sistema, pacchetti, compilatore e servizi; non sostituire automaticamente una versione con l’ultima disponibile aspettandoti gli stessi risultati.

## Riproducibilità e diagnosi

Per una prova condivisibile annota commit, progetto, sistema operativo, versione degli strumenti, comando e risultato. Se usi Git, `git rev-parse HEAD` mostra il commit e `git status --short` indica eventuali modifiche locali. Conserva l’output completo, rimuovendo credenziali e dati personali prima di condividerlo.

Il [workflow P001–P080](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/workflows/collaudo-p001-p080.yml) usa Ubuntu e strumenti diversi per gruppo. Il [workflow P081–P100](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/workflows/collaudo-p081-p100.yml) usa quattro combinazioni di sistema e Python. Leggi i job e i registri della singola esecuzione: un risultato vale per quel commit, quei casi e quell’ambiente. I dettagli delle prove storiche e dei runtime reali sono nella cartella [collaudi](../collaudi/README.md).

## Documentazione ufficiale

- [Python 3.12 — ambienti virtuali](https://docs.python.org/3.12/library/venv.html)
- [Microsoft — file system Windows e Linux in WSL](https://learn.microsoft.com/it-it/windows/wsl/filesystems)
- [Docker — backend WSL 2 su Windows](https://docs.docker.com/desktop/features/wsl/)
