# P012: Ottimizzazione del carico con programmazione dinamica

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P012/README.md) · [Registro del collaudo](../../collaudo/P012/registro.json)

**Sezione:** [Sezione 1: Programmazione, algoritmi e strutture dati](../../docs/CATALOGO.md#sezione-1-programmazione-algoritmi-e-strutture-dati).

**Argomenti:** Algoritmi · Ottimizzazione · Programmazione dinamica.

Sceglie quali colli caricare per ottenere il valore totale più alto senza superare la capacità del mezzo. Usa la programmazione dinamica; ogni collo può essere scelto al massimo una volta.

Apri un terminale nella cartella `projects/P012` ed esegui da lì i comandi. I blocchi principali usano Bash su Linux; trovi le indicazioni per Windows nella sezione dedicata.

## Requisiti e versioni

**Tecnologie utilizzate:** Python.

- Python 3.12.x; collaudo storico con 3.12.14

Dipendenze:

- Libreria standard di Python

## Preparazione

Installa Python 3.12, poi apri un terminale Bash nella cartella del progetto. I comandi seguenti creano e attivano `.venv`, un ambiente Python separato per questo laboratorio. Dopo l’attivazione, `python` usa l’interprete di quell’ambiente; riattivalo ogni volta che apri un nuovo terminale. Le versioni indicate descrivono gli ambienti documentati, non la versione minima compatibile.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
```

## Avvio

Per provare il progetto, esegui i test della sezione seguente. Il laboratorio fornisce funzioni o classi, senza un’applicazione interattiva separata.

## Test

Esegui il comando seguente. Se tutti i controlli passano, il riepilogo di `unittest` termina con `OK`. Il riepilogo viene scritto su `stderr`, il flusso dei messaggi diagnostici: questo, da solo, non indica un errore.

```bash
python tests/test_p012.py
```

## Perimetro del laboratorio

- Il file in `src` definisce le funzioni o le classi del progetto. I test le richiamano con dati di prova; non è prevista un’interfaccia interattiva.

## Windows

Puoi preparare il progetto su Windows con Python 3.12 e il comando `python` disponibile, senza Bash o WSL. I test usano `pathlib` per trovare la cartella `src`. La compatibilità è dedotta dai sorgenti; qui non è documentato un collaudo su Windows.

Apri il **Prompt dei comandi (cmd.exe)** nella cartella del progetto e prepara l’ambiente Python:

```bat
py -3.12 -m venv .venv
.venv\Scripts\activate.bat
```

Dopo l’attivazione, esegui i comandi `python` di installazione, avvio e test indicati sopra. In alternativa, anche da PowerShell, usa direttamente `.\.venv\Scripts\python.exe` al posto di `python`: non devi attivare script né cambiare le impostazioni che ne regolano l’esecuzione. Il comando di attivazione Bash non va copiato in PowerShell.

## Collaudi documentati

**Ultimo collaudo: 30 ottobre 2026 — superato.** Le verifiche del progetto sono riuscite su Ubuntu 24.04 nel [collaudo pubblico P001–P080](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/41134634700), eseguito sul commit `35b49f130493`.

### Prove precedenti

Nel [collaudo del 22 ottobre 2026](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701), le verifiche della versione di allora sono riuscite su Ubuntu 24.04.

Apri **Output verificati** e **Registro del collaudo**, all’inizio di questa pagina, per consultare comandi, esiti e limiti delle prove pubblicate. Esegui i test anche sul tuo computer e ripetili dopo ogni modifica al codice.
