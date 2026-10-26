# P044: output dei collaudi

[Indice dei collaudi](../README.md) · [Codice e istruzioni](../../projects/P044/README.md)

Esito registrato: **PASS**. [Run 39849393701](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701) · [job 120071206449](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701/job/120071206449).

Commit del runner: `44cd421247ca2bfe838baa735cf6180134f80464`. Sorgenti applicativi congelati: `32e201b1fb1258c4e7c77d32af323b966647b908`.

Ambiente registrato: Ubuntu 24.04 x86_64; Python 3.12.15 (main, Oct  1 2026, 02:35:59) [GCC 13.3.0]. Artifact: `p041-p080-core-39849393701-1` (ID `12456886835`); record originale: `P044/results.json`.

Questa pagina deriva dai risultati CI già acquisiti. Non è stata eseguita una nuova suite per prepararla. I blocchi riportano il testo emesso, dopo le sole sostituzioni di metadati indicate nel manifest. I TXT conservano i terminatori originali; per la lettura Markdown i terminatori sono normalizzati.

`unittest` scrive normalmente il proprio rapporto su **stderr**: la presenza di testo in quel canale non equivale a un errore. Esito e codice di uscita sono riportati separatamente.

I programmi di assert possono stampare soltanto un riepilogo o niente. I sottocasi non nominati dal processo restano non nominati: questa raccolta non ricostruisce nomi, valori o esiti di singoli assert. I rapporti `unittest` compatti a punti non rendono disponibili i nomi dei metodi.

## Suite di test

### 002 · DocumentEdgesTest

Comando registrato (array degli argomenti; segnaposto dei metadati documentati nel manifest):

```json
["java", "-ea", "-cp", "build", "DocumentEdgesTest"]
```

Esito: **PASS** · codice di uscita: `0`.

**stdout** — [file TXT](streams/002_DocumentEdgesTest.stdout.txt)

```text
P044 PASS: snapshot immutabile e 100 aggiornamenti concorrenti
```

**stderr** — [file TXT](streams/002_DocumentEdgesTest.stderr.txt)

Il processo non ha emesso byte su stderr. Il file collegato è vuoto (0 byte).

### 003 · DocumentVersioningTest

Comando registrato (array degli argomenti; segnaposto dei metadati documentati nel manifest):

```json
["java", "-ea", "-cp", "build", "DocumentVersioningTest"]
```

Esito: **PASS** · codice di uscita: `0`.

**stdout** — [file TXT](streams/003_DocumentVersioningTest.stdout.txt)

```text
P044: document versioning PASS
```

**stderr** — [file TXT](streams/003_DocumentVersioningTest.stderr.txt)

Il processo non ha emesso byte su stderr. Il file collegato è vuoto (0 byte).

## Demo

Il record di questo progetto non contiene processi classificati come demo.

## Controlli runtime

Il record di questo progetto non contiene controlli classificati come `runtime_check`. L’assenza non aggiunge una verifica runtime alle suite del progetto.

## Preparazione e diagnostica — stream separati

Compilazione, ripristino dipendenze e controlli della toolchain sono distinti dalle suite. I collegamenti aprono i relativi output reali.

### 001 · javac_compile

Comando registrato (array degli argomenti; segnaposto dei metadati documentati nel manifest):

```json
["javac", "-d", "build", "src/DocumentVersioning.java", "tests/DocumentEdgesTest.java", "tests/DocumentVersioningTest.java"]
```

Esito: **PASS** · codice di uscita: `0`.

[stdout — 0 byte](streams/001_javac_compile.stdout.txt)

[stderr — 0 byte](streams/001_javac_compile.stderr.txt)

## Verifica e provenienza

[Registro strutturato](registro.json) · [Hash e trasformazioni](MANIFEST.json) · [Policy](../AUDIT.md) · [Indice](../README.md)
