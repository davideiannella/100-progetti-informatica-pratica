# P057: Una funzione per verificare immagini e metadati

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P057/README.md) · [Registro del collaudo](../../collaudo/P057/registro.json)

**Sezione:** [Sezione 6: Cloud e affidabilità dei servizi](../../docs/CATALOGO.md#sezione-6-cloud-e-affidabilità-dei-servizi).

**Argomenti:** Elaborazione delle immagini · Validazione · Integrità dei dati.

Controlla che i dati ricevuti siano un’immagine leggibile, poi ricava formato, dimensioni e impronta SHA-256. La funzione lavora sul tuo computer; i test creano le immagini di prova.

Apri un terminale nella cartella `projects/P057` ed esegui da lì tutti i comandi. Gli esempi usano Linux e Bash; per Windows, segui anche la sezione dedicata.

## Requisiti e versioni

**Tecnologie utilizzate:** Python · Pillow.

- Python 3.12.14 (collaudo locale storico)

Dipendenze:

- Pillow 12.1.0 — Verifica e decodifica delle immagini; import PIL nel sorgente e nei test.

## Preparazione

Installa Python 3.12, poi esegui questi comandi nella cartella del progetto. L’ambiente virtuale `.venv` tiene separate le dipendenze del laboratorio; dopo l’attivazione, `python` usa l’interprete di questo ambiente. Riattivalo ogni volta che apri un nuovo terminale. Le versioni indicate descrivono i collaudi documentati e non sono necessariamente le versioni minime richieste.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
python -m pip install Pillow==12.1.0
```

## Avvio

Esegui i comandi della sezione Test per provare il laboratorio. I test richiamano il codice e verificano i risultati; non c’è un’applicazione dimostrativa separata.

## Test

Il test crea un PNG di 3×2 pixel, controlla formato, dimensioni e impronta, poi prova dati vuoti o non validi. Se i controlli passano, stampa un messaggio `PASS`.

```bash
python tests/test_p057.py
```

## Perimetro del laboratorio

- La funzione viene richiamata soltanto in locale. Il test genera un PNG e verifica che siano rifiutati alcuni contenuti non validi. Non sono previsti caricamenti di file o collegamenti a fornitori cloud.
- Il collaudo riguarda il computer locale. Non vengono attivati servizi cloud e non è documentata una procedura verificata per pubblicare la funzione su una piattaforma serverless.

## Windows

Il codice usa Python e librerie multipiattaforma, senza script Bash nel progetto. Per provare il laboratorio su Windows, prepara l’ambiente con i passaggi seguenti. L’esecuzione nativa su Windows non è stata collaudata nelle prove documentate.

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
