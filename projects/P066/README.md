# P066: Proteggere un’API: token firmati, ruoli e limite delle richieste

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P066/README.md) · [Registro del collaudo](../../collaudo/P066/registro.json)

**Sezione:** [Sezione 7: Sicurezza informatica](../../docs/CATALOGO.md#sezione-7-sicurezza-informatica).

**Argomenti:** Sicurezza delle API · Autorizzazione · Controllo delle richieste.

Combina verifica dei token, autorizzazione per ruolo e limiti delle richieste.

Tutti i comandi partono dalla cartella `projects/P066`. I blocchi seguenti usano la sintassi di Linux/Bash.

## Requisiti e versioni

Linguaggio: Python.

- Python 3.12.14 (ambiente documentato)

Dipendenze:

- Libreria standard Python; nessun pacchetto pip aggiuntivo.

## Preparazione

Comandi per una shell Linux/Bash dalla cartella projects/P066. Installare Python 3.12 prima della preparazione; dopo l’attivazione, python indica l’interprete dell’ambiente virtuale .venv. Riattivare l’ambiente in ogni nuovo terminale. Le versioni indicate descrivono gli ambienti documentati, non un minimo universale.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
```

## Avvio

```bash
python src/auth_api.py
```

## Test

```bash
python run_tests.py
```

## Windows

Windows: Sorgente e test usano librerie Python e percorsi pathlib, senza dipendenze da comandi Unix o privilegi di amministratore rilevate nella lettura statica. Nessun test Windows nativo è attestato da questo README.

Per la parte Python nativa, dal **Prompt dei comandi (cmd.exe)**, nella cartella del progetto:

```bat
py -3.12 -m venv .venv
.venv\Scripts\activate.bat
```

Dopo l’attivazione, usare i comandi `python` di installazione, avvio e test indicati sopra. In alternativa, anche da PowerShell, invocare direttamente `.\.venv\Scripts\python.exe` al posto di `python`: non serve attivare script né cambiare la policy di esecuzione. Il comando di attivazione Bash non va copiato in PowerShell.

## Collaudi documentati

Documentazione del 18 ottobre 2026: demo ed esempi acquisiti con l’ambiente indicato; suite congelata di 25 metodi unittest già verificata. Nessuna suite è stata rieseguita per preparare questo README.

Queste istruzioni sono state ricavate dai file e dai collaudi conservati. La preparazione dei README non ha eseguito nuove suite né modificato il codice.
