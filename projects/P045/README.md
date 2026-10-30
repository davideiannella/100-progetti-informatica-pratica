# P045: Pianificare subnet IPv4 per un campus

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P045/README.md) · [Registro del collaudo](../../collaudo/P045/registro.json)

**Sezione:** [Sezione 4: Reti di calcolatori](../../docs/CATALOGO.md#sezione-4-reti-di-calcolatori).

**Argomenti:** Reti · Indirizzamento IPv4 · Progettazione di sottoreti.

Convalida un piano di sottoreti IPv4 e ne stampa la configurazione didattica.

Apri un terminale nella cartella `projects/P045` ed esegui da lì tutti i comandi. Gli esempi usano Linux e Bash; per Windows, segui anche la sezione dedicata.

## Requisiti e versioni

**Tecnologie utilizzate:** Python · ipaddress.

- Python 3.12.14 (collaudo locale storico)

Dipendenze:

- Libreria standard Python con Python 3.12.14 — dataclasses, ipaddress, typing, unittest

## Preparazione

Installa Python 3.12, poi esegui questi comandi nella cartella del progetto. L’ambiente virtuale `.venv` tiene separate le dipendenze del laboratorio; dopo l’attivazione, `python` usa l’interprete di questo ambiente. Riattivalo ogni volta che apri un nuovo terminale. Le versioni indicate descrivono i collaudi documentati e non sono necessariamente le versioni minime richieste.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
```

## Avvio

Il programma stampa, per ogni segmento, il nome, la sottorete, il gateway previsto dal piano e il numero di indirizzi utili. Non configura router o altri apparati.

```bash
python src/network_plan.py
```

## Test

I test controllano capienza, prefissi, appartenenza alla rete principale e assenza di sovrapposizioni. Verificano anche il rifiuto di piani errati. Se i controlli passano, il riepilogo termina con `OK`.

```bash
python tests/test_network_plan.py
```

## Perimetro del laboratorio

- Esegui i comandi dalla cartella del progetto. I test mostrano come usare il codice e controllano i risultati dei casi previsti.

## Windows

Il codice usa Python e librerie multipiattaforma, senza script Bash nel progetto. Per provare il laboratorio su Windows, prepara l’ambiente con i passaggi seguenti. L’esecuzione nativa su Windows non è stata collaudata nelle prove documentate.

Per la parte Python, apri il **Prompt dei comandi (cmd.exe)** nella cartella del progetto ed esegui:

```bat
py -3.12 -m venv .venv
.venv\Scripts\activate.bat
```

Dopo l’attivazione, usa i comandi `python` di installazione, avvio e test indicati sopra. In alternativa, anche da PowerShell, sostituisci `python` con `.\.venv\Scripts\python.exe`: in questo caso non serve attivare script o modificare le regole di esecuzione di PowerShell. Non copiare il comando di attivazione Bash in PowerShell.

## Collaudi documentati

**Ultimo collaudo: 30 ottobre 2026 — superato.** Le verifiche del progetto sono riuscite su Ubuntu 24.04 nel [collaudo pubblico P001–P080](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/41134634700), eseguito sul commit `35b49f130493`.

### Prove precedenti

Collaudo storico del 2026-10-16: Test locali registrati.

Queste istruzioni sono state ricavate dai file e dai collaudi conservati.
