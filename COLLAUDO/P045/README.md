# P045: output dei collaudi

[Indice dei collaudi](../README.md) · [Codice e istruzioni](../../projects/P045/README.md)

Esito registrato: **PASS**. [Run 39849393701](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701) · [job 120071206449](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701/job/120071206449).

Commit del runner: `44cd421247ca2bfe838baa735cf6180134f80464`. Sorgenti applicativi congelati: `32e201b1fb1258c4e7c77d32af323b966647b908`.

Ambiente registrato: Ubuntu 24.04 x86_64; Python 3.12.15 (main, Oct  1 2026, 02:35:59) [GCC 13.3.0]. Artifact: `p041-p080-core-39849393701-1` (ID `12456886835`); record originale: `P045/results.json`.

Questa pagina deriva dai risultati CI già acquisiti. Non è stata eseguita una nuova suite per prepararla. I blocchi riportano il testo emesso, dopo le sole sostituzioni di metadati indicate nel manifest. I TXT conservano i terminatori originali; per la lettura Markdown i terminatori sono normalizzati.

`unittest` scrive normalmente il proprio rapporto su **stderr**: la presenza di testo in quel canale non equivale a un errore. Esito e codice di uscita sono riportati separatamente.

I programmi di assert possono stampare soltanto un riepilogo o niente. I sottocasi non nominati dal processo restano non nominati: questa raccolta non ricostruisce nomi, valori o esiti di singoli assert. I rapporti `unittest` compatti a punti non rendono disponibili i nomi dei metodi.

## Suite di test

### 001 · test_network_plan

Comando registrato (array degli argomenti; segnaposto dei metadati documentati nel manifest):

```json
["<PYTHON_HOME>/bin/python", "-B", "tests/test_network_plan.py"]
```

Esito: **PASS** · codice di uscita: `0`.

Rapporto registrato: 7 metodi unittest; failures 0, errors 0, skipped 0.

**stdout** — [file TXT](streams/001_test_network_plan.stdout.txt)

Il processo non ha emesso byte su stdout. Il file collegato è vuoto (0 byte).

**stderr** — [file TXT](streams/001_test_network_plan.stderr.txt)

```text
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
```

## Demo — processi separati dalle suite

Questi output provengono dalle demo eseguite dal runner. Non costituiscono nuovi metodi unittest.

### 002 · demo_network_plan

Comando registrato (array degli argomenti; segnaposto dei metadati documentati nel manifest):

```json
["<PYTHON_HOME>/bin/python", "-B", "src/network_plan.py"]
```

Esito: **PASS** · codice di uscita: `0`.

**stdout** — [file TXT](streams/002_demo_network_plan.stdout.txt)

```text
Wi-Fi studenti 10.20.0.0/23 10.20.0.1 510
Laboratorio 1 10.20.2.0/25 10.20.2.1 126
Laboratorio 2 10.20.2.128/25 10.20.2.129 126
Docenti 10.20.3.0/26 10.20.3.1 62
Segreteria 10.20.3.64/27 10.20.3.65 30
Server 10.20.3.96/27 10.20.3.97 30
Management 10.20.3.128/28 10.20.3.129 14
```

**stderr** — [file TXT](streams/002_demo_network_plan.stderr.txt)

Il processo non ha emesso byte su stderr. Il file collegato è vuoto (0 byte).

## Controlli runtime

Il record di questo progetto non contiene controlli classificati come `runtime_check`. L’assenza non aggiunge una verifica runtime alle suite del progetto.

## Verifica e provenienza

[Registro strutturato](registro.json) · [Hash e trasformazioni](MANIFEST.json) · [Policy](../AUDIT.md) · [Indice](../README.md)
