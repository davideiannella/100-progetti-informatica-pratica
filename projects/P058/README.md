# P058: Creare backup e verificarli prima del ripristino

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P058/README.md) · [Registro del collaudo](../../collaudo/P058/registro.json)

**Sezione:** [Sezione 6: Cloud e affidabilità dei servizi](../../docs/CATALOGO.md#sezione-6-cloud-e-affidabilità-dei-servizi).

**Argomenti:** Backup · Ripristino · Integrità dei dati.

Crea e verifica backup, controllando che un errore non distrugga la destinazione.

Apri un terminale nella cartella `projects/P058` ed esegui da lì tutti i comandi. Gli esempi usano Linux e Bash; per Windows, segui anche la sezione dedicata.

## Requisiti e versioni

**Tecnologie utilizzate:** Python.

- Python 3.12.14 (collaudo locale storico)

Dipendenze:

- Libreria standard Python con Python 3.12.14 — hashlib, os, re, tempfile, pathlib

## Preparazione

Installa Python 3.12, poi esegui questi comandi nella cartella del progetto. L’ambiente virtuale `.venv` tiene separate le dipendenze del laboratorio; dopo l’attivazione, `python` usa l’interprete di questo ambiente. Riattivalo ogni volta che apri un nuovo terminale. Le versioni indicate descrivono i collaudi documentati e non sono necessariamente le versioni minime richieste.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
```

## Avvio

Questo esempio altera una copia di backup e verifica che il ripristino venga rifiutato senza danneggiare il file di destinazione. Se il controllo riesce, stampa `Target conservato`.

```bash
python demo_corrupt_backup.py
```

## Test

I test verificano il recupero della copia originale, il rifiuto di un’etichetta già usata e la protezione della destinazione quando il backup è corrotto. Se i controlli passano, stampano messaggi `PASS`.

```bash
python tests/test_p058.py
python tests/test_edges.py
```

## Perimetro del laboratorio

- Esegui i comandi dalla cartella del progetto. I test mostrano come usare il codice e controllano i risultati dei casi previsti.
- Il filesystem della cartella dei backup deve supportare `os.link`, che crea un nuovo nome riferito agli stessi dati del file. Il ripristino prepara il file temporaneo nella cartella di destinazione, così `os.replace` opera sullo stesso filesystem. Il laboratorio non garantisce la conservazione dei dati dopo un guasto hardware.

## Windows

Python e `pathlib` sono multipiattaforma. Per provare `create_backup` su Windows serve però un filesystem locale che supporti gli hard link, per esempio NTFS. File aperti e permessi possono impedire la sostituzione della destinazione. L’esecuzione nativa su Windows non è stata collaudata nelle prove documentate.

Per la parte Python, apri il **Prompt dei comandi (cmd.exe)** nella cartella del progetto ed esegui:

```bat
py -3.12 -m venv .venv
.venv\Scripts\activate.bat
```

Dopo l’attivazione, usa i comandi `python` di installazione, avvio e test indicati sopra. In alternativa, anche da PowerShell, sostituisci `python` con `.\.venv\Scripts\python.exe`: in questo caso non serve attivare script o modificare le regole di esecuzione di PowerShell. Non copiare il comando di attivazione Bash in PowerShell.

## Collaudi documentati

**Ultimo collaudo: 31 ottobre 2026 — superato.** Le verifiche del progetto sono riuscite su Ubuntu 24.04 nel [collaudo pubblico P001–P080](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/41142475728), eseguito sul commit `c8303920c4f4`.

### Prove precedenti

Collaudo storico del 2026-10-16: Test locali registrati.

Queste istruzioni sono state ricavate dai file e dai collaudi conservati.
