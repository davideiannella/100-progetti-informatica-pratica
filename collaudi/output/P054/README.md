# P054 — output reali dei collaudi

Esito registrato: **PASS**. [Run 39849393701](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701) · [job 120071206842](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701/job/120071206842).

Commit del runner: `44cd421247ca2bfe838baa735cf6180134f80464`. Sorgenti applicativi congelati: `32e201b1fb1258c4e7c77d32af323b966647b908`.

Ambiente registrato: Ubuntu 24.04 x86_64; Python 3.12.15 (main, Oct  1 2026, 02:35:59) [GCC 13.3.0]. Artifact: `p054-runtime-39849393701-1` (ID `12456212870`); record originale: `P054/results.json`.

Questa pagina deriva dai risultati CI già acquisiti. Non è stata eseguita una nuova suite per prepararla. I blocchi riportano il testo emesso, dopo le sole sostituzioni di metadati indicate nel manifest. I TXT conservano i terminatori originali; per la lettura Markdown i terminatori sono normalizzati.

`unittest` scrive normalmente il proprio rapporto su **stderr**: la presenza di testo in quel canale non equivale a un errore. Esito e codice di uscita sono riportati separatamente.

I programmi di assert possono stampare soltanto un riepilogo o niente. I sottocasi non nominati dal processo restano non nominati: questa raccolta non ricostruisce nomi, valori o esiti di singoli assert. I rapporti `unittest` compatti a punti non rendono disponibili i nomi dei metodi.

## Suite di test

### 001 · test_app

Comando registrato (array degli argomenti; segnaposto dei metadati documentati nel manifest):

```json
["<PYTHON_HOME>/bin/python", "-B", "tests/test_app.py"]
```

Esito: **PASS** · codice di uscita: `0`.

Rapporto registrato: 5 metodi unittest; failures 0, errors 0, skipped 0.

**stdout** — [file TXT](streams/001_test_app.stdout.txt)

Il processo non ha emesso byte su stdout. Il file collegato è vuoto (0 byte).

**stderr** — [file TXT](streams/001_test_app.stderr.txt)

```text
.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
```

### 002 · test_http

Comando registrato (array degli argomenti; segnaposto dei metadati documentati nel manifest):

```json
["<PYTHON_HOME>/bin/python", "-B", "tests/test_http.py"]
```

Esito: **PASS** · codice di uscita: `0`.

**stdout** — [file TXT](streams/002_test_http.stdout.txt)

```text
P054 PASS: HTTP e dipendenze dentro la release
```

**stderr** — [file TXT](streams/002_test_http.stderr.txt)

```text
<PYTHON_HOME>/lib/python3.12/site-packages/fastapi/testclient.py:1: StarletteDeprecationWarning: Using `httpx` with `starlette.testclient` is deprecated; install `httpx2` instead.
  from starlette.testclient import TestClient as TestClient  # noqa
```

### 003 · test_release_builder

Comando registrato (array degli argomenti; segnaposto dei metadati documentati nel manifest):

```json
["<PYTHON_HOME>/bin/python", "-B", "tests/test_release_builder.py"]
```

Esito: **PASS** · codice di uscita: `0`.

Rapporto registrato: 3 metodi unittest; failures 0, errors 0, skipped 0.

**stdout** — [file TXT](streams/003_test_release_builder.stdout.txt)

Il processo non ha emesso byte su stdout. Il file collegato è vuoto (0 byte).

**stderr** — [file TXT](streams/003_test_release_builder.stderr.txt)

```text
...
----------------------------------------------------------------------
Ran 3 tests in 0.010s

OK
```

## Demo — processi separati dalle suite

Questi output provengono dalle demo eseguite dal runner. Non costituiscono nuovi metodi unittest.

### 004 · demo_build_release

Comando registrato (array degli argomenti; segnaposto dei metadati documentati nel manifest):

```json
["<PYTHON_HOME>/bin/python", "-B", "tools/build_release.py"]
```

Esito: **PASS** · codice di uscita: `0`.

**stdout** — [file TXT](streams/004_demo_build_release.stdout.txt)

```text
{
  "artifact": "p054_api_release.zip",
  "files": [
    "Dockerfile",
    "requirements.txt",
    "src/app.py"
  ],
  "project": "P054",
  "python": "3.12.15",
  "sha256": "ee329706aa60fd4180877b5e462307b104ed30e6c88d0244f544e3db1b7854d6"
}
```

**stderr** — [file TXT](streams/004_demo_build_release.stderr.txt)

Il processo non ha emesso byte su stderr. Il file collegato è vuoto (0 byte).

### 005 · demo_live_http_test

Comando registrato (array degli argomenti; segnaposto dei metadati documentati nel manifest):

```json
["<PYTHON_HOME>/bin/python", "-B", "tools/live_http_test.py"]
```

Esito: **PASS** · codice di uscita: `0`.

**stdout** — [file TXT](streams/005_demo_live_http_test.stdout.txt)

```text
{
  "health": {
    "status": "ok"
  },
  "created": {
    "id": 1,
    "name": "router",
    "quantity": 2
  },
  "fetched": {
    "id": 1,
    "name": "router",
    "quantity": 2
  }
}
```

**stderr** — [file TXT](streams/005_demo_live_http_test.stderr.txt)

Il processo non ha emesso byte su stderr. Il file collegato è vuoto (0 byte).

## Controlli runtime reali — record strutturati

I controlli seguenti sono record JSON del runner, separati dagli stream delle suite. Non hanno un proprio exit code di processo: il runner ne registra stato e dettaglio. Il JSON conserva le verifiche e i valori tecnici; nomi e indirizzi interni sono sostituiti con segnaposto stabili.

### 010 · P054 Docker health HTTP

```json
{
  "kind": "runtime_check",
  "name": "P054 Docker health HTTP",
  "status": "PASS",
  "detail": [
    200,
    {
      "status": "ok"
    }
  ],
  "sequence": 10
}
```

### 011 · P054 Docker POST

```json
{
  "kind": "runtime_check",
  "name": "P054 Docker POST",
  "status": "PASS",
  "detail": [
    200,
    {
      "id": 1,
      "name": "router",
      "quantity": 2
    }
  ],
  "sequence": 11
}
```

### 012 · P054 Docker GET

```json
{
  "kind": "runtime_check",
  "name": "P054 Docker GET",
  "status": "PASS",
  "detail": [
    200,
    {
      "id": 1,
      "name": "router",
      "quantity": 2
    }
  ],
  "sequence": 12
}
```

### 013 · P054 Docker invalid input

```json
{
  "kind": "runtime_check",
  "name": "P054 Docker invalid input",
  "status": "PASS",
  "detail": [
    422,
    {
      "detail": [
        {
          "type": "greater_than_equal",
          "loc": [
            "body",
            "quantity"
          ],
          "msg": "Input should be greater than or equal to 0",
          "input": -1,
          "ctx": {
            "ge": 0
          }
        }
      ]
    }
  ],
  "sequence": 13
}
```

### 014 · P054 Docker non-root

```json
{
  "kind": "runtime_check",
  "name": "P054 Docker non-root",
  "status": "PASS",
  "detail": "appuser",
  "sequence": 14
}
```

[Registro operativo pubblico completo dello stesso run](../../CI_P001_P080/tentativo_2/job_120071206842.log) · [Provenienza e manifest dei log](../../CI_P001_P080/README.md).

## Verifica e provenienza

[Registro strutturato](registro.json) · [Hash e trasformazioni](MANIFEST.json) · [Policy](../AUDIT.md) · [Indice](../README.md)
