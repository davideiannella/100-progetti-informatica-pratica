# P069: Controllare la sicurezza di Linux: permessi e configurazione

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P069/README.md) · [Registro del collaudo](../../collaudo/P069/registro.json)

**Sezione:** [Sezione 7: Sicurezza informatica](../../docs/CATALOGO.md#sezione-7-sicurezza-informatica).

**Argomenti:** Sicurezza dei sistemi · Hardening Linux · Permessi.

Il progetto controlla i permessi POSIX dei file e alcune configurazioni create per il laboratorio. L’audit legge questi dati e segnala i problemi previsti dalle regole, senza correggerli automaticamente.

Apri un terminale nella cartella `projects/P069`. I comandi qui sotto sono scritti per Linux con Bash; per Windows consulta la sezione dedicata.

## Requisiti e versioni

**Tecnologie utilizzate:** Python · Linux.

- Python 3.12.14 (ambiente documentato)

Dipendenze:

- Libreria standard Python; nessun pacchetto pip aggiuntivo.

## Preparazione

Installa Python 3.12, poi esegui i comandi qui sotto per creare e attivare un ambiente virtuale dedicato al progetto, nella cartella `.venv`. Dopo l’attivazione, il comando `python` usa questo ambiente. Riattivalo ogni volta che apri un nuovo terminale.

Le versioni elencate sono quelle degli ambienti documentati; non indicano la versione minima compatibile.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
```

## Avvio

Esegui la dimostrazione per leggere le segnalazioni sui permessi e sulle configurazioni di esempio.

```bash
python -B src/hardening_audit.py
```

## Esempio documentale

Riproduce i casi sui permessi, sul collegamento simbolico e sulle configurazioni sintetiche. Crea soltanto file temporanei, rimossi al termine. Dalla cartella `projects/P069`, con l’ambiente Python preparato:

```bash
python -B worked_example.py
```

Esegui l’esempio su Linux. Se usi Windows, apri WSL e salva il progetto nel filesystem Linux, così i permessi POSIX mantengono il comportamento previsto.

## Test

Esegui i test automatici del progetto:

```bash
python -B run_tests.py
```

Nel riepilogo, `OK` indica che tutti i test eseguiti sono passati. Il report JSON riporta quanti test sono stati eseguiti e gli eventuali errori o fallimenti.

## Windows

Per riprodurre l’intero laboratorio da Windows, usa WSL con una distribuzione Linux. Salva il progetto nel filesystem Linux, non in una cartella montata dall’unità C:.

I calcoli sui valori numerici dei permessi possono funzionare anche su Windows. Gli esercizi e i test usano però `chmod`, controllano i bit POSIX e creano collegamenti simbolici. Questi permessi non equivalgono alle ACL, cioè alle liste di controllo degli accessi di Windows. Le prove conservate non documentano un collaudo su Windows nativo.

## Collaudi documentati

**Ultimo collaudo: 31 ottobre 2026 — superato.** Le verifiche del progetto sono riuscite su Ubuntu 24.04 nel [collaudo pubblico P001–P080](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/41142475728), eseguito sul commit `c8303920c4f4`.

### Prove precedenti

La documentazione del 18 ottobre 2026 descrive una suite di 8 metodi di test `unittest`. I collegamenti «Output verificati» e «Registro del collaudo», all’inizio della pagina, riportano risultati, comandi e ambiente delle prove conservate.
