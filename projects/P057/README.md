# P057: Una funzione per verificare immagini e metadati

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P057/README.md) · [Registro del collaudo](../../collaudo/P057/registro.json)

**Sezione:** [Sezione 6: Cloud e affidabilità dei servizi](../../docs/CATALOGO.md#sezione-6-cloud-e-affidabilità-dei-servizi).

**Argomenti:** Elaborazione delle immagini · Validazione · Integrità dei dati.

Valida immagini e metadati con una funzione locale e dati creati dai test.

Tutti i comandi partono dalla cartella `projects/P057`. I blocchi seguenti usano la sintassi di Linux/Bash.

## Requisiti e versioni

Linguaggio: Python / Pillow.

- Python 3.12.14 (collaudo locale storico)

Dipendenze:

- Pillow 12.1.0 — Verifica e decodifica delle immagini; import PIL nel sorgente e nei test.

## Preparazione

Comandi per una shell Linux/Bash dalla cartella projects/P057. Installare Python 3.12 prima della preparazione; dopo l’attivazione, python indica l’interprete dell’ambiente virtuale .venv. Riattivare l’ambiente in ogni nuovo terminale. Le versioni indicate descrivono gli ambienti documentati, non un minimo universale.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
python -m pip install Pillow==12.1.0
```

## Avvio

Non è presente un’applicazione dimostrativa autonoma: usare i test sotto come punto di ingresso eseguibile.

## Test

```bash
python tests/test_p057.py
```

## Perimetro del laboratorio

- Funzione locale senza entrypoint cloud. Il test genera un PNG e verifica i limiti; non sono previsti deploy, upload o collegamenti a provider.
- Collaudo locale soltanto: non vengono attivati servizi cloud e non esistono istruzioni di deployment serverless verificato.

## Windows

Il codice usa Python e moduli multipiattaforma; non sono presenti script Bash nel progetto. La plausibilità non equivale a un collaudo Windows. Nessun test Windows nativo è attestato da questo README.

Per la parte Python nativa, dal **Prompt dei comandi (cmd.exe)**, nella cartella del progetto:

```bat
py -3.12 -m venv .venv
.venv\Scripts\activate.bat
```

Dopo l’attivazione, usare i comandi `python` di installazione, avvio e test indicati sopra. In alternativa, anche da PowerShell, invocare direttamente `.\.venv\Scripts\python.exe` al posto di `python`: non serve attivare script né cambiare la policy di esecuzione. Il comando di attivazione Bash non va copiato in PowerShell.

## Collaudi documentati

Collaudo storico del 2026-10-16: Test locali registrati; nessun nuovo test eseguito durante questa revisione.

Queste istruzioni sono state ricavate dai file e dai collaudi conservati. La preparazione dei README non ha eseguito nuove suite né modificato il codice.
