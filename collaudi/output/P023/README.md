# P023 — output reali dei collaudi

Esito registrato: **PASS**. [Run 39849393701](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701) · [job 120071206795](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701/job/120071206795).

Commit del runner: `44cd421247ca2bfe838baa735cf6180134f80464`. Sorgenti applicativi congelati: `32e201b1fb1258c4e7c77d32af323b966647b908`.

Ambiente registrato: Ubuntu 24.04; .NET SDK 8 + net8.0 runtime; no external NuGet feeds; Python 3.12; HTTP on loopback. Artifact: `p001-p040-complete-validation` (ID `12457560243`); record originale: `P023.json`.

Questa pagina deriva dai risultati CI già acquisiti. Non è stata eseguita una nuova suite per prepararla. I blocchi riportano il testo emesso, dopo le sole sostituzioni di metadati indicate nel manifest. I TXT conservano i terminatori originali; per la lettura Markdown i terminatori sono normalizzati.

`unittest` scrive normalmente il proprio rapporto su **stderr**: la presenza di testo in quel canale non equivale a un errore. Esito e codice di uscita sono riportati separatamente.

I programmi di assert possono stampare soltanto un riepilogo o niente. I sottocasi non nominati dal processo restano non nominati: questa raccolta non ricostruisce nomi, valori o esiti di singoli assert. I rapporti `unittest` compatti a punti non rendono disponibili i nomi dei metodi.

## Suite di test

### 004 · tests/test_http.py

Comando registrato (array degli argomenti; segnaposto dei metadati documentati nel manifest):

```json
["<PYTHON_HOME>/bin/python", "-B", "tests/test_http.py"]
```

Esito: **PASS** · codice di uscita: `0`.

**stdout** — [file TXT](streams/004_tests_test_http.py.stdout.txt)

```text
P023: HTTP reale, input invalidi, 100 creazioni concorrenti, 30 completamenti PASS
```

**stderr** — [file TXT](streams/004_tests_test_http.py.stderr.txt)

Il processo non ha emesso byte su stderr. Il file collegato è vuoto (0 byte).

## Demo

Il record di questo progetto non contiene processi classificati come demo.

## Controlli runtime

Il record di questo progetto non contiene controlli classificati come `runtime_check`. L’assenza non aggiunge una verifica runtime alle suite del progetto.

## Preparazione e diagnostica — stream separati

Compilazione, ripristino dipendenze e controlli della toolchain sono distinti dalle suite. I collegamenti aprono i relativi output reali.

### 001 · passo 1

Comando registrato (array degli argomenti; segnaposto dei metadati documentati nel manifest):

```json
["dotnet", "--version"]
```

Esito: **PASS** · codice di uscita: `0`.

[stdout — 8 byte](streams/001_step_1.stdout.txt)

[stderr — 0 byte](streams/001_step_1.stderr.txt)

### 002 · passo 2

Comando registrato (array degli argomenti; segnaposto dei metadati documentati nel manifest):

```json
["dotnet", "restore", "src/P023.csproj", "--configfile", "NuGet.ci.config"]
```

Esito: **PASS** · codice di uscita: `0`.

[stdout — 88 byte](streams/002_step_2.stdout.txt)

[stderr — 0 byte](streams/002_step_2.stderr.txt)

### 003 · passo 3

Comando registrato (array degli argomenti; segnaposto dei metadati documentati nel manifest):

```json
["dotnet", "build", "src/P023.csproj", "--no-restore", "--configuration", "Debug"]
```

Esito: **PASS** · codice di uscita: `0`.

[stdout — 128 byte](streams/003_step_3.stdout.txt)

[stderr — 0 byte](streams/003_step_3.stderr.txt)

## Verifica e provenienza

[Registro strutturato](registro.json) · [Hash e trasformazioni](MANIFEST.json) · [Policy](../AUDIT.md) · [Indice](../README.md)
