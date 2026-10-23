# P032 — output reali dei collaudi

Esito registrato: **PASS**. [Run 39849393701](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701) · [job 120071206795](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701/job/120071206795).

Commit del runner: `44cd421247ca2bfe838baa735cf6180134f80464`. Sorgenti applicativi congelati: `32e201b1fb1258c4e7c77d32af323b966647b908`.

Ambiente registrato: Ubuntu 24.04; Python 3.12; Neo4j 5.26.0 service container; cypher-shell in that image. Artifact: `p001-p040-complete-validation` (ID `12457560243`); record originale: `P032.json`.

Questa pagina deriva dai risultati CI già acquisiti. Non è stata eseguita una nuova suite per prepararla. I blocchi riportano il testo emesso, dopo le sole sostituzioni di metadati indicate nel manifest. I TXT conservano i terminatori originali; per la lettura Markdown i terminatori sono normalizzati.

`unittest` scrive normalmente il proprio rapporto su **stderr**: la presenza di testo in quel canale non equivale a un errore. Esito e codice di uscita sono riportati separatamente.

I programmi di assert possono stampare soltanto un riepilogo o niente. I sottocasi non nominati dal processo restano non nominati: questa raccolta non ricostruisce nomi, valori o esiti di singoli assert. I rapporti `unittest` compatti a punti non rendono disponibili i nomi dei metodi.

## Suite di test

### 001 · tests/test_p032.py

Comando registrato (array degli argomenti; segnaposto dei metadati documentati nel manifest):

```json
["<PYTHON_HOME>/bin/python", "-B", "tests/test_p032.py"]
```

Esito: **PASS** · codice di uscita: `0`.

**stdout** — [file TXT](streams/001_tests_test_p032.py.stdout.txt)

```text
P032: shortest path PASS; Cypher STATIC QA
```

**stderr** — [file TXT](streams/001_tests_test_p032.py.stderr.txt)

Il processo non ha emesso byte su stderr. Il file collegato è vuoto (0 byte).

## Suite aggiuntive sui motori database

Esecuzioni aggiuntive delle verifiche sul motore reale, separate dalle suite originali del progetto.

### 002 · passo 2

Comando registrato (array degli argomenti; segnaposto dei metadati documentati nel manifest):

```json
["docker", "exec", "-i", "<CONTAINER_ID_001>", "cypher-shell", "--format", "plain"]
```

Esito: **PASS** · codice di uscita: `0`.

Conteggio registrato: 6; base del conteggio: `executed Neo4j assertion queries`.

**stdout** — [file TXT](streams/002_step_2.stdout.txt)

```text
p, minutes
(:Stop {name: "Centro", id: "A"})-[:CONNECTS {minutes: 5}]->(:Stop {name: "Stazione", id: "B"})-[:CONNECTS {minutes: 7}]->(:Stop {name: "Universita", id: "C"}), 12
p, minutes
(:Stop {name: "Centro", id: "A"})-[:CONNECTS {minutes: 5}]->(:Stop {name: "Stazione", id: "B"})-[:CONNECTS {minutes: 7}]->(:Stop {name: "Universita", id: "C"}), 12
check, passed
"CI_ASSERT_version", TRUE
check, passed
"CI_ASSERT_nodes", TRUE
check, passed
"CI_ASSERT_edges", TRUE
check, passed
"CI_ASSERT_edge_values", TRUE
check, passed
"CI_ASSERT_shortest", TRUE
check, passed
"CI_ASSERT_direction", TRUE
```

**stderr** — [file TXT](streams/002_step_2.stderr.txt)

Il processo non ha emesso byte su stderr. Il file collegato è vuoto (0 byte).

## Demo

Il record di questo progetto non contiene processi classificati come demo.

## Controlli runtime

Il record di questo progetto non contiene controlli classificati come `runtime_check`. L’assenza non aggiunge una verifica runtime alle suite del progetto.

## Verifica e provenienza

[Registro strutturato](registro.json) · [Hash e trasformazioni](MANIFEST.json) · [Policy](../AUDIT.md) · [Indice](../README.md)
