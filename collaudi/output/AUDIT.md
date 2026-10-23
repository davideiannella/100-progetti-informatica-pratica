# Audit della raccolta degli output

La raccolta è una trasformazione documentale di artifact CI già scaricati. Non importa i sorgenti, non esegue suite e non aggiunge risultati di assert. L’analisi legge esclusivamente JSON, TXT, log e ZIP già presenti.

## Provenienza e byte

I nove ZIP originali (cinque del run 39849393701 e quattro del run 39893701054) sono stati nuovamente confrontati localmente con i digest SHA-256 ufficiali già acquisiti. Tutti coincidono. Gli archivi originali sono privati e non vengono pubblicati qui. `ARTIFACTS.json` ne riporta ID, nome, run, commit, dimensione e digest, senza URL firmati.

Ogni record P001–P080 è identico al membro JSON dello ZIP ufficiale. Dove lo ZIP contiene anche un file stream `.log`, i byte UTF-8 del campo JSON sono confrontati con quel file e con il membro dell’archivio. Per P001–P040 la fonte è il valore JSON decodificato e ricodificato UTF-8: l’hash dello stream non è l’hash del testo JSON con gli escape. Per P081–P100 ogni TXT pubblicato è confrontato byte per byte con il membro dello ZIP; le summary sono copie esatte. I CRLF Windows sono conservati nei TXT. Il solo rendering nei blocchi Markdown converte CRLF/CR in LF e aggiunge un terminatore prima della chiusura del blocco quando necessario.

Ogni `Pnnn/MANIFEST.json` registra l’hash del record sorgente, il membro o puntatore JSON dello stream, dimensione e SHA-256 prima e dopo, e le regole applicate. `registro.json` conserva comando, stato, exit code e metadati dei passi, con collegamenti agli stream. I campi strutturati trasformati hanno hash prima/dopo della serializzazione JSON UTF-8 con indentazione 2 e newline finale. Il manifest generale identifica con SHA-256 i manifest dei 100 progetti. Nessun hash pubblico è presentato come se identificasse un file originale quando identifica una copia derivata.

## Sanitizzazione limitata ai metadati

- `python_host_prefix`: il prefisso assoluto della toolchain Python del runner è sostituito con `<PYTHON_HOME>`; il resto del percorso e il messaggio tecnico rimangono.
- `runner_workspace_prefix`: il prefisso della directory di lavoro GitHub è sostituito con `<RUNNER_WORKSPACE>`; i percorsi relativi dei progetti rimangono.
- Nei record runtime P054–P056, nomi temporanei di cluster/container e Pod, nomi di volumi temporanei, nonce del record runtime, UID interni, ID container e indirizzi interni del runtime sono sostituiti con segnaposto stabili e distinti. Anche gli ID interni negli argomenti `docker exec` delle suite motore P031/P032 sono sostituiti. Sono preservati stato, conteggi, HTTP status, valori applicativi, exit code, `restartCount`, condizione `ready`, messaggi delle probe e timestamp. Gli IP didattici P045 e il loopback sono conservati.
- Eventuali righe di intestazione Authorization, Proxy-Authorization, Cookie o Set-Cookie sarebbero sostituite solo nel valore. Nessuna intestazione di credenziale è presente negli stream selezionati.

Non sono pubblicati bootstrap del runner, checkout, configurazioni di accesso, URL SAS o ZIP. Le parole “token”, “password” e “secret” nei nomi dei test e nei messaggi didattici non sono credenziali e rimangono intatte. Warning e output tecnico sono conservati. I 160 stream P081–P100 (compresi quelli vuoti) non richiedono alcuna sostituzione.

## Suite, demo e runtime

Sono presenti tutti i 101 processi di suite originali P001–P080, le due suite aggiuntive dei motori database e i loro stdout/stderr, oltre alle 29 demo. I 21 controlli runtime P054–P056 sono riportati come record strutturati effettivi, distinti dagli stream di processo e senza inventare un exit code individuale. I log ausiliari di avvio, build container, inspect, polling e pulizia dei tre runtime non vengono duplicati: i manifest ne conservano hash e dimensioni originali e le pagine collegano i registri operativi pubblici dello stesso run. In P056 sono mantenuti i dieci controlli reali, evitando di ripetere i grandi dump Kubernetes. Non sono attribuiti a questo run output del registro storico 38982515580.

Le quattro combinazioni P081–P100 conservano ciascuna le 377 righe effettive `test_nome (...) ... ok`, più `Ran ... tests` e `OK`. Le quantità sono controllate per progetto e poi sommate per ambiente: 377, 377, 377, 377. Non si deduce da una singola suite una prova per tutti i suoi assert interni. Tutti i file sono inferiori a 90000 byte, non compressi.

## Verifiche documentali

Verificati i 100 record di provenienza, i digest dei nove archivi, l’identità dei membri estratti, tutti gli stream inclusi e le trasformazioni dichiarate, le quattro matrici da 377 righe test, la presenza dei 100 README, i collegamenti relativi e l’assenza di credenziali/URL firmati e percorsi host nei file pubblicati. Le verifiche sui documenti non sono nuove esecuzioni dei progetti. L’errore del primo tentativo P001–P080 resta nel registro pubblico del tentativo 1 e non viene sostituito da output sintetici.
