# P055 — output reali dei collaudi

Esito registrato: **PASS**. [Run 39849393701](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701) · [job 120071206976](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701/job/120071206976).

Commit del runner: `44cd421247ca2bfe838baa735cf6180134f80464`. Sorgenti applicativi congelati: `32e201b1fb1258c4e7c77d32af323b966647b908`.

Ambiente registrato: Ubuntu 24.04 x86_64; Python 3.12.15 (main, Oct  1 2026, 02:35:59) [GCC 13.3.0]. Artifact: `p055-runtime-39849393701-1` (ID `12456527740`); record originale: `P055/results.json`.

Questa pagina deriva dai risultati CI già acquisiti. Non è stata eseguita una nuova suite per prepararla. I blocchi riportano il testo emesso, dopo le sole sostituzioni di metadati indicate nel manifest. I TXT conservano i terminatori originali; per la lettura Markdown i terminatori sono normalizzati.

`unittest` scrive normalmente il proprio rapporto su **stderr**: la presenza di testo in quel canale non equivale a un errore. Esito e codice di uscita sono riportati separatamente.

I programmi di assert possono stampare soltanto un riepilogo o niente. I sottocasi non nominati dal processo restano non nominati: questa raccolta non ricostruisce nomi, valori o esiti di singoli assert. I rapporti `unittest` compatti a punti non rendono disponibili i nomi dei metodi.

## Suite di test

### 001 · test_p055

Comando registrato (array degli argomenti; segnaposto dei metadati documentati nel manifest):

```json
["<PYTHON_HOME>/bin/python", "-B", "tests/test_p055.py"]
```

Esito: **PASS** · codice di uscita: `0`.

**stdout** — [file TXT](streams/001_test_p055.stdout.txt)

```text
P055 PASS: SQLite e struttura Compose; runtime container separato
```

**stderr** — [file TXT](streams/001_test_p055.stderr.txt)

Il processo non ha emesso byte su stderr. Il file collegato è vuoto (0 byte).

## Demo

Il record di questo progetto non contiene processi classificati come demo.

## Controlli runtime reali — record strutturati

I controlli seguenti sono record JSON del runner, separati dagli stream delle suite. Non hanno un proprio exit code di processo: il runner ne registra stato e dettaglio. Il JSON conserva le verifiche e i valori tecnici; nomi e indirizzi interni sono sostituiti con segnaposto stabili.

### 006 · P055 create through Nginx/API/PostgreSQL

```json
{
  "kind": "runtime_check",
  "name": "P055 create through Nginx/API/PostgreSQL",
  "status": "PASS",
  "detail": [
    201,
    {
      "id": 1,
      "name": "<RUNTIME_RECORD_001>"
    }
  ],
  "sequence": 6
}
```

### 007 · P055 duplicate HTTP 409

```json
{
  "kind": "runtime_check",
  "name": "P055 duplicate HTTP 409",
  "status": "PASS",
  "detail": [
    409,
    {
      "detail": "duplicate"
    }
  ],
  "sequence": 7
}
```

### 008 · P055 invalid input HTTP 422

```json
{
  "kind": "runtime_check",
  "name": "P055 invalid input HTTP 422",
  "status": "PASS",
  "detail": [
    422,
    {
      "detail": [
        {
          "type": "value_error",
          "loc": [
            "body",
            "name"
          ],
          "msg": "Value error, blank name",
          "input": " ",
          "ctx": {
            "error": {}
          }
        }
      ]
    }
  ],
  "sequence": 8
}
```

### 010 · P055 persistence after api restart

```json
{
  "kind": "runtime_check",
  "name": "P055 persistence after api restart",
  "status": "PASS",
  "detail": [
    200,
    [
      {
        "id": 1,
        "name": "<RUNTIME_RECORD_001>"
      }
    ]
  ],
  "sequence": 10
}
```

### 012 · P055 persistence after db restart

```json
{
  "kind": "runtime_check",
  "name": "P055 persistence after db restart",
  "status": "PASS",
  "detail": [
    200,
    [
      {
        "id": 1,
        "name": "<RUNTIME_RECORD_001>"
      }
    ]
  ],
  "sequence": 12
}
```

### 014 · P055 native PostgreSQL major version

```json
{
  "kind": "runtime_check",
  "name": "P055 native PostgreSQL major version",
  "status": "PASS",
  "detail": "17.11",
  "sequence": 14
}
```

[Registro operativo pubblico completo dello stesso run](../../CI_P001_P080/tentativo_2/job_120071206976.log) · [Provenienza e manifest dei log](../../CI_P001_P080/README.md).

## Verifica e provenienza

[Registro strutturato](registro.json) · [Hash e trasformazioni](MANIFEST.json) · [Policy](../AUDIT.md) · [Indice](../README.md)
