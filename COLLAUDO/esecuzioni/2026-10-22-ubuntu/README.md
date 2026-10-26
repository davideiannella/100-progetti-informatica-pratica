# Collaudo pubblico P001–P080

Il [run 39849393701](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701), concluso il 22 ottobre 2026, ha superato **80 progetti su 80 e cinque job su cinque** su Ubuntu 24.04. Il commit eseguito è `44cd421247ca2bfe838baa735cf6180134f80464`. I risultati riguardano questo run e gli ambienti registrati nei log.

Il codice didattico e i test originali restano quelli del commit congelato `32e201b1fb1258c4e7c77d32af323b966647b908`. Le modifiche successive organizzano documentazione e collaudo pubblico. Il job P001–P040 controlla tutte le **299 impronte SHA-256 prima e dopo**, senza differenze; ciascun progetto P041–P080 verifica inoltre l'integrità dei propri file originali nella copia temporanea di esecuzione.

## Come leggere i numeri

| Ambito | Suite originali eseguite | Metodi `unittest` | Controlli aggiuntivi |
| --- | ---: | ---: | --- |
| P001–P040 | 48 | 60 | MongoDB: 12 asserzioni; Neo4j: 6 asserzioni |
| P041–P053 e P057–P080 | 48 | 1352 | 27 processi dimostrativi |
| P054 | 3 | 8 | 5 controlli Docker e 2 processi dimostrativi |
| P055 | 1 | 0 | 6 controlli Compose/PostgreSQL |
| P056 | 1 | 0 | 10 controlli Kubernetes |

Le **101 suite originali** comprendono 39 processi `unittest` e 62 programmi di assert. I **1420 metodi `unittest`** appartengono a quelle suite: non si sommano al numero delle suite. I 1084 sottocasi registrati da P061–P066 sono interni ai metodi e non si sommano ai 1420. Le due suite dei motori database, le loro 18 asserzioni, i 21 controlli runtime e le 29 demo sono categorie separate. Alcuni programmi di assert verificano molti dati o casi randomizzati: non ne ricaviamo un numero artificiale di metodi di test.

I 10 controlli di P056 comprendono la verifica HTTP ripetuta da tre Pod distinti. Il processo di port-forward viene fermato intenzionalmente (`STOPPED`, codice `-15`) durante la pulizia. Il fallimento della liveness e il successivo riavvio sono indotti e osservati dalla prova.

## Ambienti realmente eseguiti

Tutti i cinque job usano Ubuntu 24.04 e Python 3.12.15. Sono registrati Java Temurin 17.0.20.1, gcc/g++ 13.3.0 (C11/C++17 con UBSan), SQLite 3.45.1, MongoDB 8.0.14 e Neo4j 5.26.0. Nei quattro progetti C# P022, P023, P040 e P042, `dotnet --version` conferma SDK **8.0.426** dentro le copie temporanee. Il `dotnet --info` generale mostra anche SDK 10.0.401 preinstallato sul runner; non è la versione selezionata per quei progetti.

P054 esegue un container Docker reale e verifica HTTP, input e utente non root. P055 esegue Nginx, API e PostgreSQL 17.11 con Docker Compose 2.38.2, controllando anche la persistenza dopo i riavvii. P056 crea un cluster kind 0.33.0 con Kubernetes 1.37.0 (kubectl 1.37.1), verifica tre repliche, Service, HTTP, ricreazione di un Pod, liveness e recupero. Docker Engine è 28.0.4. Le versioni effettive delle dipendenze Python sono negli artifact e in `RIEPILOGO.json`.

P057 resta una verifica locale del laboratorio, P059 una simulazione di scaling e P060 una verifica di suite, gate e artefatto locale. Queste prove non sono deployment su provider cloud; anche il cluster kind è locale al runner GitHub. Questo run non dimostra esecuzione nativa Windows dei primi 80 progetti. La [matrice P081–P100](../2026-10-22-multipiattaforma/RUN.json) documenta separatamente Linux e Windows con Python 3.12 e 3.13.

## Il primo tentativo è conservato

Il [run 39847787696](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39847787696), commit `30babaf161101b104948b9857db4c5ff1b2a2cc5`, ha concluso quattro job con successo e uno con errore. Tutte le 48 suite originali P001–P040 erano già PASS. Il controllo CI aggiunto per la direzione del percorso Neo4j produceva soltanto cinque risultati: in assenza di percorsi inversi non usciva la sesta riga richiesta.

Il runner aggiunto è stato corretto con `WITH count` prima di `RETURN`, mantenendo obbligatorie tutte e sei le asserzioni. È stato inoltre selezionato SDK .NET 8.0.426 nelle sole copie temporanee. Nel nuovo run tutte e sei le asserzioni Neo4j sono vere. Nessun sorgente o test originale è stato cambiato. I due tentativi sono due run distinti del workflow, numeri 1 e 2; ciascuno ha `run_attempt: 1` nell'API GitHub.

## File e verifica indipendente

- [RIEPILOGO.json](RIEPILOGO.json): 80 progetti, stati, contatori, versioni, integrità e confronto dei tentativi.
- [RIEPILOGO_COMPLETO.json.gz](RIEPILOGO_COMPLETO.json.gz): dettagli derivati sanificati; nessun risultato numerico modificato.
- [RUNS.json](RUNS.json), [jobs.json](jobs.json) e [first_attempt_jobs.json](first_attempt_jobs.json): provenienza, date, stati e passaggi pubblici.
- [artifacts.json](artifacts.json) e [first_attempt_artifacts.json](first_attempt_artifacts.json): ID, dimensioni, URL e digest ufficiali degli artifact originali.
- [MANIFEST_LOG.json](MANIFEST_LOG.json): elenco dei dieci log operativi UTF-8, URL dei job, ordine di eventuali parti e SHA-256 pubblici.
- [SANIFICAZIONE_LOG.json](../../SANIFICAZIONE_LOG.json): trasformazioni applicate anche ai quattro log P081–P100.

I log nei due tentativi conservano comandi operativi, output, errori e codici di uscita presenti. Sono omesse le sezioni di preparazione del runner, checkout, configurazione di accesso e pulizia; percorsi host e metadati interni sono sostituiti da segnaposto. Il primo errore Neo4j e il relativo esito restano visibili. Non sono log integrali del runner.

Gli ZIP originali, le parti e gli strumenti di ricomposizione non sono distribuiti nel repository. Gli originali completi restano nell’archivio personale. I digest ufficiali GitHub riguardano quei download originali; gli hash del manifest pubblico riguardano i derivati sanificati e non devono essere confrontati come se fossero lo stesso file. I registri download_verification conservano il riscontro originario dei digest e dei membri ZIP.

Per verificare i log, dalla cartella `COLLAUDO/esecuzioni/2026-10-22-ubuntu`:

```python
import hashlib, json
from pathlib import Path
base = Path('.')
manifest = json.loads((base / 'MANIFEST_LOG.json').read_text(encoding='utf-8'))
for record in manifest['files']:
    data = (base / record['file']).read_bytes()
    assert hashlib.sha256(data).hexdigest() == record['sha256']
print('Hash pubblici verificati')
```

Per ripetere le prove, consultare il [workflow](../../../.github/workflows/collaudo-p001-p080.yml) e gli [ambienti](../../../docs/AMBIENTI.md). I risultati restano circoscritti alle prove e agli ambienti documentati.
