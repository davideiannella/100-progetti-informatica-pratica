# P060: output dei collaudi

[Indice dei collaudi](../README.md) · [Codice e istruzioni](../../projects/P060/README.md)

Esito registrato: **PASS**. [Run 39849393701](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701) · [job 120071206449](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701/job/120071206449).

Commit del runner: `44cd421247ca2bfe838baa735cf6180134f80464`. Sorgenti applicativi congelati: `32e201b1fb1258c4e7c77d32af323b966647b908`.

Ambiente registrato: Ubuntu 24.04 x86_64; Python 3.12.15 (main, Oct  1 2026, 02:35:59) [GCC 13.3.0]. Artifact: `p041-p080-core-39849393701-1` (ID `12456886835`); record originale: `P060/results.json`.

Questa pagina deriva dai risultati CI già acquisiti. Non è stata eseguita una nuova suite per prepararla. I blocchi riportano il testo emesso, dopo le sole sostituzioni di metadati indicate nel manifest. I TXT conservano i terminatori originali; per la lettura Markdown i terminatori sono normalizzati.

`unittest` scrive normalmente il proprio rapporto su **stderr**: la presenza di testo in quel canale non equivale a un errore. Esito e codice di uscita sono riportati separatamente.

I programmi di assert possono stampare soltanto un riepilogo o niente. I sottocasi non nominati dal processo restano non nominati: questa raccolta non ricostruisce nomi, valori o esiti di singoli assert. I rapporti `unittest` compatti a punti non rendono disponibili i nomi dei metodi.

## Suite di test

### 001 · test_calc

Comando registrato (array degli argomenti; segnaposto dei metadati documentati nel manifest):

```json
["<PYTHON_HOME>/bin/python", "-B", "tests/test_calc.py"]
```

Esito: **PASS** · codice di uscita: `0`.

Rapporto registrato: 2 metodi unittest; failures 0, errors 0, skipped 0.

**stdout** — [file TXT](streams/001_test_calc.stdout.txt)

Il processo non ha emesso byte su stdout. Il file collegato è vuoto (0 byte).

**stderr** — [file TXT](streams/001_test_calc.stderr.txt)

```text
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

### 002 · test_edges

Comando registrato (array degli argomenti; segnaposto dei metadati documentati nel manifest):

```json
["<PYTHON_HOME>/bin/python", "-B", "tests/test_edges.py"]
```

Esito: **PASS** · codice di uscita: `0`.

Rapporto registrato: 4 metodi unittest; failures 0, errors 0, skipped 0.

**stdout** — [file TXT](streams/002_test_edges.stdout.txt)

Il processo non ha emesso byte su stdout. Il file collegato è vuoto (0 byte).

**stderr** — [file TXT](streams/002_test_edges.stderr.txt)

```text
....
----------------------------------------------------------------------
Ran 4 tests in 0.002s

OK
```

### 003 · test_p060

Comando registrato (array degli argomenti; segnaposto dei metadati documentati nel manifest):

```json
["<PYTHON_HOME>/bin/python", "-B", "tests/test_p060.py"]
```

Esito: **PASS** · codice di uscita: `0`.

**stdout** — [file TXT](streams/003_test_p060.stdout.txt)

```text
P060: local CI gates + artifact hash PASS
```

**stderr** — [file TXT](streams/003_test_p060.stderr.txt)

Il processo non ha emesso byte su stderr. Il file collegato è vuoto (0 byte).

## Demo — processi separati dalle suite

Questi output provengono dalle demo eseguite dal runner. Non costituiscono nuovi metodi unittest.

### 004 · demo_build_release

Comando registrato (array degli argomenti; segnaposto dei metadati documentati nel manifest):

```json
["<PYTHON_HOME>/bin/python", "-B", "build_release.py"]
```

Esito: **PASS** · codice di uscita: `0`.

**stdout** — [file TXT](streams/004_demo_build_release.stdout.txt)

```text
{
  "artifact": "release.zip",
  "sha256": "d5cf9e77c3cbd09302a6800f76d2eaf637a7623ec9fdcb373b80c5f4e5ff66e3"
}
```

**stderr** — [file TXT](streams/004_demo_build_release.stderr.txt)

Il processo non ha emesso byte su stderr. Il file collegato è vuoto (0 byte).

## Controlli runtime

Il record di questo progetto non contiene controlli classificati come `runtime_check`. L’assenza non aggiunge una verifica runtime alle suite del progetto.

## Verifica e provenienza

[Registro strutturato](registro.json) · [Hash e trasformazioni](MANIFEST.json) · [Policy](../AUDIT.md) · [Indice](../README.md)
