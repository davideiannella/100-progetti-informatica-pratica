# P056: Tre repliche e controlli di salute in Kubernetes

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../COLLAUDO/P056/README.md) · [Registro del collaudo](../../COLLAUDO/P056/registro.json)

Affianca un server HTTP minimale a un deployment Kubernetes con tre repliche.

Tutti i comandi partono dalla cartella `projects/P056`. I blocchi seguenti usano la sintassi di Linux/Bash.

## Requisiti e versioni

Linguaggio: Python / YAML / Kubernetes.

- Python 3.12.14 (collaudo locale storico)
- Python nel container 3.12-slim (configurato e collaudato)
- Docker Engine / kind / kubectl 28.0.4 / 0.33.0 / 1.37.1 (collaudo runtime storico)

Dipendenze:

- Libreria standard Python con Python 3.12 — Server HTTP minimale; nessun framework applicativo esterno.
- PyYAML 6.0.3 — Il test strutturale importa yaml.

## Preparazione

Comandi per una shell Linux/Bash dalla cartella projects/P056. Installare Python 3.12 prima della preparazione; dopo l’attivazione, python indica l’interprete dell’ambiente virtuale .venv. Riattivare l’ambiente in ogni nuovo terminale. Le versioni indicate descrivono gli ambienti documentati, non un minimo universale.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-test.txt
```

## Avvio

Percorso locale: il server resta in primo piano su 127.0.0.1:8000 fino a `Ctrl+C`.

```bash
python src/app.py
```

Percorso Kubernetes alternativo: richiede Docker con container Linux, kind e kubectl. Il cluster dedicato `p056-lab` deve essere ancora da creare; gli ultimi comandi usano esplicitamente il suo contesto.

```bash
docker build -t p056-demo-api:1.0 .
kind create cluster --name p056-lab
kind load docker-image p056-demo-api:1.0 --name p056-lab
kubectl --context kind-p056-lab apply -f k8s/deployment.yaml
kubectl --context kind-p056-lab rollout status deployment/demo-api
kubectl --context kind-p056-lab port-forward service/demo-api 8080:80
```

Il port forwarding resta in primo piano: il Service è raggiungibile su 127.0.0.1:8080 finché il comando rimane attivo.

## Test

```bash
python tests/test_p056.py
```

La suite Python controlla YAML e presenza dei file; non dimostra il funzionamento del cluster, dei probe o del traffico HTTP.

## Perimetro del laboratorio

- La suite Python controlla soltanto YAML e presenza dei file. Per il percorso Kubernetes occorrono Docker Linux, kind, kubectl e un cluster kind predisposto; imagePullPolicy: Never richiede l’immagine già caricata nei nodi.
- I comandi Kubernetes creano un cluster dedicato chiamato p056-lab. Se il nome è già in uso, usare il cluster esistente o scegliere un altro nome e aggiornare tutti i riferimenti. Il percorso locale e quello Kubernetes sono alternativi.

## Windows

Il Dockerfile usa useradd e la base Linux. Il test liveness storico sospende un task container con SIGSTOP nel runtime Linux: non è una prova Windows nativa. I container e il cluster richiedono un motore Linux: su Windows usare, per esempio, Docker Desktop con backend WSL2; questo non costituisce un collaudo Windows nativo. Nessun test Windows nativo è attestato da questo README.

Per la parte Python nativa, dal **Prompt dei comandi (cmd.exe)**, nella cartella del progetto:

```bat
py -3.12 -m venv .venv
.venv\Scripts\activate.bat
```

Dopo l’attivazione, usare i comandi `python` di installazione, avvio e test indicati sopra. In alternativa, anche da PowerShell, invocare direttamente `.\.venv\Scripts\python.exe` al posto di `python`: non serve attivare script né cambiare la policy di esecuzione. Il comando di attivazione Bash non va copiato in PowerShell.

## Collaudi documentati

Collaudo storico del 2026-10-16/17: Suite YAML locale; secondo tentativo kind su GitHub Actions riuscito per tre Pod pronti, Service HTTP, ricreazione Pod e liveness. Nessuna suite rieseguita per questo README.

Queste istruzioni sono state ricavate dai file e dai collaudi conservati. La preparazione dei README non ha eseguito nuove suite né modificato il codice.
