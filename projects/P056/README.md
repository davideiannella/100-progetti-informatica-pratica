# P056: Tre repliche e controlli di salute in Kubernetes

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P056/README.md) · [Registro del collaudo](../../collaudo/P056/registro.json)

**Sezione:** [Sezione 6: Cloud e affidabilità dei servizi](../../docs/CATALOGO.md#sezione-6-cloud-e-affidabilità-dei-servizi).

**Argomenti:** Cloud e container · Orchestrazione · Affidabilità dei servizi.

Prova un semplice server HTTP sul tuo computer oppure eseguilo in Kubernetes con tre repliche, cioè tre copie del servizio. I due percorsi sono alternativi.

Apri un terminale nella cartella `projects/P056` ed esegui da lì tutti i comandi. Gli esempi usano Linux e Bash; per Windows, segui anche la sezione dedicata.

## Requisiti e versioni

**Tecnologie utilizzate:** Python · YAML · Docker · Kubernetes · kind · kubectl.

- Python 3.12.14 (collaudo locale storico)
- Python nel container 3.12-slim (configurato e collaudato)
- Docker Engine / kind / kubectl 28.0.4 / 0.33.0 / 1.37.1 (collaudo runtime storico)

Dipendenze:

- Libreria standard Python con Python 3.12 — Server HTTP minimale; nessun framework applicativo esterno.
- PyYAML 6.0.3 — Il test strutturale importa yaml.

## Preparazione

Installa Python 3.12, poi esegui questi comandi nella cartella del progetto. L’ambiente virtuale `.venv` tiene separate le dipendenze del laboratorio; dopo l’attivazione, `python` usa l’interprete di questo ambiente. Riattivalo ogni volta che apri un nuovo terminale. Le versioni indicate descrivono i collaudi documentati e non sono necessariamente le versioni minime richieste.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-test.txt
```

## Avvio

Per la prova locale, avvia il server con il comando seguente. Risponde su `127.0.0.1:8000` e resta attivo nel terminale fino a `Ctrl+C`.

```bash
python src/app.py
```

In alternativa, prova il percorso Kubernetes: servono Docker con container Linux, kind e kubectl. I comandi seguenti creano il cluster dedicato `p056-lab`, che non deve già esistere. L’opzione `--context kind-p056-lab` indirizza i comandi successivi a quel cluster.

```bash
docker build -t p056-demo-api:1.0 .
kind create cluster --name p056-lab
kind load docker-image p056-demo-api:1.0 --name p056-lab
kubectl --context kind-p056-lab apply -f k8s/deployment.yaml
kubectl --context kind-p056-lab rollout status deployment/demo-api
kubectl --context kind-p056-lab port-forward service/demo-api 8080:80
```

L’ultimo comando apre un collegamento fra una porta del tuo computer e il Service, chiamato port forwarding. Il Service è raggiungibile su `127.0.0.1:8080` finché il comando resta attivo.

## Test

```bash
python tests/test_p056.py
```

Il test Python controlla la configurazione YAML e la presenza dei file. Non avvia il cluster e non prova i controlli di salute (probe) o le richieste HTTP.

## Perimetro del laboratorio

- I test Python riguardano soltanto YAML e presenza dei file. Per eseguire Kubernetes servono Docker Linux, kind, kubectl e il cluster kind preparato. Con `imagePullPolicy: Never`, l’immagine deve essere già caricata nei nodi.
- I comandi Kubernetes creano il cluster dedicato `p056-lab`. Se esiste già, usa quello senza ripetere la creazione oppure scegli un altro nome e aggiorna tutti i riferimenti. Il percorso locale e quello Kubernetes sono alternativi.

## Windows

Il Dockerfile usa `useradd` e una base Linux. Anche il collaudo storico della liveness riguarda Linux: usa `SIGSTOP` per sospendere un processo nel container e osservare il riavvio. Su Windows puoi preparare il percorso con Docker Desktop e WSL2, l’ambiente Linux di Windows. Il container e il cluster restano Linux; queste prove non attestano un’esecuzione nativa su Windows.

Per la parte Python, apri il **Prompt dei comandi (cmd.exe)** nella cartella del progetto ed esegui:

```bat
py -3.12 -m venv .venv
.venv\Scripts\activate.bat
```

Dopo l’attivazione, usa i comandi `python` di installazione, avvio e test indicati sopra. In alternativa, anche da PowerShell, sostituisci `python` con `.\.venv\Scripts\python.exe`: in questo caso non serve attivare script o modificare le regole di esecuzione di PowerShell. Non copiare il comando di attivazione Bash in PowerShell.

## Collaudi documentati

Collaudo storico del 2026-10-16/17: Suite YAML locale; secondo tentativo kind su GitHub Actions riuscito per tre Pod pronti, Service HTTP, ricreazione Pod e liveness.

Queste istruzioni sono state ricavate dai file e dai collaudi conservati.
