# Esiti e output dei collaudi

Questa cartella raccoglie evidenze già prodotte per i laboratori di **100 progetti di informatica pratica**. Permette di leggere gli esiti, confrontare gli output e risalire all’ambiente della prova. La preparazione della raccolta non ha eseguito nuove suite né modificato i sorgenti.

## P081–P100: quattro job pubblici riusciti

Il riferimento è il [run GitHub Actions 39701559280](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39701559280), concluso con successo il **22 ottobre 2026**, sul commit [`32e201b1fb1258c4e7c77d32af323b966647b908`](https://github.com/davideiannella/100-progetti-informatica-pratica/commit/32e201b1fb1258c4e7c77d32af323b966647b908).

| Ambiente registrato | Python effettivo | Job | Riepilogo | Log |
|---|---|---|---|---|
| Windows Server 2025 | 3.13.16 | [119571736513](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39701559280/job/119571736513) | [JSON](ci_P081_P100/119571736513.summary.json) | [log](ci_P081_P100/119571736513.log) |
| Ubuntu/Linux | 3.13.16 | [119571736757](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39701559280/job/119571736757) | [JSON](ci_P081_P100/119571736757.summary.json) | [log](ci_P081_P100/119571736757.log) |
| Windows Server 2025 | 3.12.10 | [119571736870](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39701559280/job/119571736870) | [JSON](ci_P081_P100/119571736870.summary.json) | [log](ci_P081_P100/119571736870.log) |
| Ubuntu/Linux | 3.12.15 | [119571737066](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39701559280/job/119571737066) | [JSON](ci_P081_P100/119571737066.summary.json) | [log](ci_P081_P100/119571737066.log) |

Ogni job registra **20 suite riuscite, 377 metodi di test, zero skip, 60 file Python compilati sintatticamente e 299 hash SHA-256 verificati senza differenze**. Sono gli stessi 377 metodi ripetuti in quattro ambienti, non quattro insiemi distinti di test. La verifica degli hash riguarda i file elencati nel manifest; non equivale all’esecuzione delle suite P001–P080.

Le dipendenze registrate nei quattro job sono NumPy 2.3.5, SciPy 1.17.0, scikit-learn 1.8.0, joblib 1.5.3, threadpoolctl 3.6.0 e Pillow 12.3.0. Le versioni complete di Python e del sistema sono nei JSON. Le etichette del workflow `3.12` e `3.13` possono risolvere a versioni correttive diverse su Linux e Windows: la tabella riporta quelle effettivamente registrate.

I riepiloghi sono stati confrontati con il JSON compreso fra `COLLAUDO_SUMMARY_BEGIN` e `COLLAUDO_SUMMARY_END` nei log: tutti e quattro coincidono. I campi aggiuntivi `job_id`, `job_name` e `run_url` identificano la provenienza. Il [riscontro dei registri](RISCONTRO_EVIDENZE.json) documenta questi confronti.

Il workflow stampa il risultato aggregato di ciascuna suite; per i casi riusciti non riversa nel log pubblico tutto lo stdout/stderr dei singoli test. Per leggere anche i nomi dei test e gli output dettagliati è disponibile [OUTPUT_DETTAGLIATI_STORICI_LINUX.json](ci_P081_P100/OUTPUT_DETTAGLIATI_STORICI_LINUX.json): contiene la distinta esecuzione locale Linux del **21 ottobre 2026**, con 377 metodi e Python 3.12.14. I digest dei suoi 60 file Python coincidono con i sorgenti consegnati. I risultati non sono attribuiti ai quattro job pubblici; quel summary locale non elenca separatamente tutte le versioni delle dipendenze.

## P001–P080: che cosa è stato verificato

La [panoramica per progetto](storico/PANORAMICA_P001_P080.md) e l’[indice JSON](storico/INDICE_P001_P080.json) riportano stato, perimetro e limiti degli ottanta laboratori precedenti. Il [registro aggregato completo, compresso in gzip](storico/EVIDENZE_P001_P080.json.gz) conserva comandi, codici di uscita e output storici. Gli [ambienti registrati](storico/AMBIENTI_STORICI.json) restano distinti per gruppo.

- **P001–P040:** 40 progetti con esito storico `passed` nelle verifiche disponibili su Linux. Alcune compilazioni .NET furono adattate all’ambiente contenitore. Le prove aggiuntive dei motori reali MongoDB e Neo4j sono in [MOTORI_P031_P032.json](storico/MOTORI_P031_P032.json), separate dai precedenti controlli del modello Python e degli script.
- **P041–P060:** 20 progetti con esito storico `passed` su Linux, entro il perimetro di ogni registro. Alcuni progetti sono modelli o simulazioni. Per P054–P056, le verifiche locali iniziali e i successivi collaudi di container reali sono documentati separatamente qui sotto.
- **P061–P080:** l’esecuzione indipendente del 18 ottobre 2026 registra 20 progetti riusciti e **1.339 metodi unittest**; i conteggi sono stati riscontrati negli output conservati. Comprende prove locali e dati sintetici, secondo il progetto.

Questi registri non attestano un collaudo nativo Windows di P001–P080. Per i laboratori POSIX, `/proc` o permessi di file, seguire le istruzioni Linux/WSL dei README. Un modello di rete, scheduling, replica o rischio non dimostra il funzionamento di apparati o infrastrutture reali. Le metriche su dati sintetici non misurano la qualità su dati operativi.

## P054–P056: distinguere il tentativo locale dai runtime remoti

Il [tentativo locale del 17 ottobre](storico/DOCKER_LOCALE_BLOCCATO.json) registra il daemon Docker **bloccato**, **zero immagini costruite, zero servizi Compose avviati e zero cluster Kubernetes creati**. Il controllo delle configurazioni non viene presentato come esecuzione di container.

Successivamente furono svolte prove reali su runner Linux remoti. I [metadati di provenienza](storico/DOCKER_REMOTO_PROVENIENZA.json) conservano run ID, commit, versioni e cronologia; i tre registri riportano i comandi e gli output:

| Progetto | Evidenza del runtime riuscito | Comandi riusciti | Asserzioni riuscite |
|---|---|---:|---:|
| P054 | [Docker, HTTP e utente non root](storico/P054_runtime_results.json) | 8 | 5 |
| P055 | [Compose, Nginx, API e PostgreSQL 17.11; persistenza dopo riavvio](storico/P055_runtime_results.json) | 11 | 6 |
| P056 | [Kubernetes con kind: tre repliche, Service, ricreazione del Pod e liveness](storico/P056_runtime_results.json.gz) | 128 | 9 |

Le prove Docker/Kubernetes provengono da un repository di collaudo allora **non pubblico**: i registri esportati sono qui consultabili, mentre non viene promesso l’accesso ai suoi link Actions privati. P054 e P055 riuscirono nel run `38981849010`; l’esito complessivo di quel run fu `failure` perché il primo tentativo P056 terminò per timeout nella prova di fault injection. P056 riuscì nel successivo run `38982515580`, dopo la correzione del runner di prova; il registro dichiara invariati i sorgenti applicativi.

I precedenti [test di servizi HTTP e PGlite](storico/SERVIZI_INTERMEDI_P055_P056.json) sono mantenuti come stadio distinto: non sono PostgreSQL nativo né Kubernetes. I valori di runtime, i tempi e gli identificativi tecnici nei log restano quelli originari.

## Dieci esempi documentali P067–P076

Gli [esiti delle esecuzioni](supplementari/ESECUZIONI.json) del 22 ottobre 2026 registrano **dieci avvii riusciti, stderr vuoto e nessuna suite eseguita**. Gli stdout sono gli output acquisiti, non esempi ricostruiti per questa pagina:

| Progetto | Output | Perimetro |
|---|---|---|
| P067 | [stdout](supplementari/P067.stdout.log) | Handshake TLS reale su loopback; certificati temporanei e sei rifiuti attesi |
| P068 | [stdout](supplementari/P068.stdout.log) | Matrice di policy e sequenze sintetiche; nessuna modifica al firewall |
| P069 | [stdout](supplementari/P069.stdout.log) | File temporanei, permessi e configurazioni sintetiche |
| P070 | [stdout](supplementari/P070.stdout.log) | Workflow tabletop e verifica di integrità del ripristino |
| P071 | [stdout](supplementari/P071.stdout.log) | Matrice didattica di rischio e categorie STRIDE |
| P072 | [stdout](supplementari/P072.stdout.log) | Parser e regole su log sintetici |
| P073 | [stdout](supplementari/P073.stdout.log) | Regressione e metriche su dati sintetici |
| P074 | [stdout](supplementari/P074.stdout.log) | Soglie, matrice di confusione e metriche di classificazione |
| P075 | [stdout](supplementari/P075.stdout.log) | Rilevamento di anomalie sintetiche |
| P076 | [stdout](supplementari/P076.stdout.log) | Punteggi e ordinamento di un catalogo didattico |

L’ambiente registrato è Linux, Python 3.12.14 e OpenSSL 3.5.8, con cryptography 50.0.2, NumPy 2.3.5, SciPy 1.17.0, scikit-learn 1.8.0, joblib 1.5.3 e threadpoolctl 3.6.0. I digest di stdout e stderr coincidono con quelli dei metadati originali. Certificati temporanei, cifrari negoziati e arrotondamenti numerici possono variare tra esecuzioni; non sono valori da imporre al proprio computer.

## Ripetere una verifica

Preparare un ambiente virtuale come indicato nel [README generale](../README.md). Dalla radice del repository, per P081–P100:

```text
python -m pip install -r requirements-p081-p100.txt
python -B tools/collaudo_p081_p100.py
```

Il comando controlla il manifest, compila i file Python, esegue le venti suite e scrive i nuovi risultati nella propria cartella `test-results`. È possibile avviare anche il [workflow pubblico](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/workflows/collaudo-p081-p100.yml) quando si dispone dei permessi sul repository o su una propria copia.

Per ripetere un esempio P067–P076, installare `requirements-p061-p080.txt`, entrare nella cartella del progetto e usare il comando corrispondente:

| Progetti | Comando dell’esempio |
|---|---|
| P067–P072 | `python -B worked_example.py` |
| P073–P076 | `python -B examples.py` |

Per la sua suite usare invece `python -B run_tests.py`. P067 e P069 richiedono Linux o WSL con file nel filesystem Linux per conservare la semantica POSIX dei permessi. Per P001–P060 e per i deployment Docker/Kubernetes seguire il README del singolo progetto: linguaggi, compilatori, servizi e comandi non sono uniformi.

## Consultare i registri compressi

I due registri più voluminosi sono distribuiti integralmente in formato `.json.gz`: [P056](storico/P056_runtime_results.json.gz) e [P001–P080](storico/EVIDENZE_P001_P080.json.gz). La compressione conserva ogni byte delle rispettive copie sanificate già verificate: nessun comando, stdout o stderr è stato abbreviato. Il [riepilogo P056](storico/P056_runtime_results.summary.json) e l’[indice P001–P080](storico/INDICE_P001_P080.json) permettono una prima lettura senza decompressione.

Con 7-Zip, aprire il file `.gz` ed estrarre il JSON. In alternativa, dalla radice del repository salvare ed eseguire questo codice Python:

```python
from pathlib import Path
import gzip
import hashlib
import json

base = Path("collaudi")
manifest = json.loads((base / "PROVENIENZA_SANIFICAZIONE.json").read_text(encoding="utf-8"))
for record in manifest["distribution_compression"]["archives"]:
    archive = base / record["file"]
    data = gzip.decompress(archive.read_bytes())
    assert hashlib.sha256(data).hexdigest() == record["uncompressed_sha256"]
    output = archive.with_suffix("")
    output.write_bytes(data)
    print(output, len(data), "byte; SHA-256 verificato")
```

I digest dei file gzip e dei JSON decompressi sono distinti e riportati nella provenienza. Le impronte dei 137 originali e delle relative copie sanificate restano quelle della raccolta di partenza. Questa preparazione modifica solo il formato di distribuzione e i rimandi documentali; non aggiunge esiti di esecuzioni successive.

## Integrità e sanificazione

[PROVENIENZA_SANIFICAZIONE.json](PROVENIENZA_SANIFICAZIONE.json) registra i digest SHA-256 degli originali, delle copie sanificate e dei file pubblici. Gli originali integrali restano conservati separatamente. I percorsi assoluti dell’host o del runner sono sostituiti con `<ambiente_di_test>` per non pubblicare nomi e strutture degli ambienti di lavoro. I percorsi delle API e dei container, i numeri, gli esiti, i tempi, gli avvisi e gli errori delle prove sono preservati. La maschera `***` presente nei log Actions era già applicata da GitHub.

I riepiloghi e gli indici sono documenti derivati esplicitamente identificati; non vengono presentati come stdout. Gli output contengono dati sintetici o identificativi tecnici temporanei delle prove. L’unico indirizzo email nei registri è quello pubblico dei manutentori dell’immagine Nginx, proveniente dalle etichette Docker. La [verifica della raccolta](RISCONTRO_EVIDENZE.json) comprende la ricerca di percorsi privati e formati comuni di credenziali, oltre al confronto degli esiti. Non contiene chiavi private, token di accesso o dati personali dell’autore.
