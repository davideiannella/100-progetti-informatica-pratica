# P060: Pipeline CI con test e integrità della release

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P060/README.md) · [Registro del collaudo](../../collaudo/P060/registro.json)

**Sezione:** [Sezione 6: Cloud e affidabilità dei servizi](../../docs/CATALOGO.md#sezione-6-cloud-e-affidabilità-dei-servizi).

**Argomenti:** DevOps · Integrazione continua · Verifica della release.

Esegui i test e prepara un pacchetto di rilascio sul tuo computer. Il progetto include anche un workflow di integrazione continua (CI): una sequenza di attività proposta per GitHub Actions.

Apri un terminale nella cartella `projects/P060` ed esegui da lì tutti i comandi. Gli esempi usano Linux e Bash; per Windows, segui anche la sezione dedicata.

## Requisiti e versioni

**Tecnologie utilizzate:** Python · YAML · GitHub Actions (workflow di esempio).

- Python 3.12.14 (collaudo locale storico)
- Python nel workflow 3.13 (configurato, non eseguito su GitHub Actions)

Dipendenze:

- Libreria standard Python con Python 3.12.14 — math, hashlib, json, pathlib, py_compile, zipfile, unittest, subprocess

## Preparazione

Installa Python 3.12, poi esegui questi comandi nella cartella del progetto. L’ambiente virtuale `.venv` tiene separate le dipendenze del laboratorio; dopo l’attivazione, `python` usa l’interprete di questo ambiente. Riattivalo ogni volta che apri un nuovo terminale. Le versioni indicate descrivono i collaudi documentati e non sono necessariamente le versioni minime richieste.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
```

## Avvio

Questo comando crea `release.zip` e `release_manifest.json`. Il manifest riporta il nome dell’archivio e la sua impronta SHA-256, utile per controllarne l’integrità.

```bash
python build_release.py
```

## Test

I test verificano la somma, gli input non validi, gli iteratori e l’integrità del pacchetto. Se i controlli passano, il riepilogo di `unittest` termina con `OK`.

```bash
python -m unittest discover -s tests -v
```

## Perimetro del laboratorio

- Per usare il workflow `.github/workflows/ci.yml` su GitHub, colloca il contenuto di P060 nella cartella principale di un repository autonomo. Dentro `projects/P060`, GitHub non lo riconosce come workflow del repository del libro. Il progetto non distribuisce l’applicazione e non pubblica i pacchetti prodotti.
- Il workflow configura Python 3.13, mentre il collaudo locale documentato usa Python 3.12.14. Una prova riuscita sul tuo computer non dimostra che il workflow sia stato eseguito su GitHub o che i byte dello ZIP siano identici su ogni sistema operativo.

## Windows

I test e il programma che crea il pacchetto usano la libreria standard Python e possono essere provati su Windows con i passaggi seguenti. Il workflow richiede invece `ubuntu-latest`: riguarda quindi una build Linux. Le prove documentate non comprendono Windows nativo e non garantiscono ZIP con byte identici fra sistemi operativi diversi.

Per la parte Python, apri il **Prompt dei comandi (cmd.exe)** nella cartella del progetto ed esegui:

```bat
py -3.12 -m venv .venv
.venv\Scripts\activate.bat
```

Dopo l’attivazione, usa i comandi `python` di installazione, avvio e test indicati sopra. In alternativa, anche da PowerShell, sostituisci `python` con `.\.venv\Scripts\python.exe`: in questo caso non serve attivare script o modificare le regole di esecuzione di PowerShell. Non copiare il comando di attivazione Bash in PowerShell.

## Collaudi documentati

**Ultimo collaudo: 30 ottobre 2026 — superato.** Le verifiche del progetto sono riuscite su Ubuntu 24.04 nel [collaudo pubblico P001–P080](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/41134634700), eseguito sul commit `35b49f130493`.

### Prove precedenti

Collaudo storico del 2026-10-16: Test e build locali riusciti; nessuna esecuzione remota del workflow P060 e nessun deploy.

Queste istruzioni sono state ricavate dai file e dai collaudi conservati.
