# P069: Hardening Linux: un audit riproducibile di permessi e configurazione

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P069/README.md) · [Registro del collaudo](../../collaudo/P069/registro.json)

Controlla permessi POSIX e configurazioni sintetiche con un audit in sola lettura.

Tutti i comandi partono dalla cartella `projects/P069`. I blocchi seguenti usano la sintassi di Linux/Bash.

## Requisiti e versioni

Linguaggio: Python.

- Python 3.12.14 (ambiente documentato)

Dipendenze:

- Libreria standard Python; nessun pacchetto pip aggiuntivo.

## Preparazione

Comandi per una shell Linux/Bash dalla cartella projects/P069. Installare Python 3.12 prima della preparazione; dopo l’attivazione, python indica l’interprete dell’ambiente virtuale .venv. Riattivare l’ambiente in ogni nuovo terminale. Le versioni indicate descrivono gli ambienti documentati, non un minimo universale.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
```

## Avvio

```bash
python -B src/hardening_audit.py
```

## Esempio documentale

Riproduce i casi sui permessi, sul collegamento simbolico e sulle configurazioni sintetiche. Crea soltanto file temporanei, rimossi al termine. Dalla cartella `projects/P069`, con l’ambiente Python preparato:

```bash
python -B worked_example.py
```

Eseguire su Linux; da Windows usare WSL e una cartella nel filesystem Linux, per conservare la semantica dei permessi POSIX.

## Test

```bash
python -B run_tests.py
```

## Windows

I calcoli puri sui modi numerici possono funzionare in Windows, ma gli esercizi e i test applicano chmod e confrontano bit POSIX; creano inoltre symlink. L’audit dei permessi reali va riprodotto in un filesystem Linux/WSL, senza equiparare i bit POSIX alle ACL Windows. Per riprodurre l’intero laboratorio da Windows usare WSL con una distribuzione Linux e una cartella nel filesystem Linux, non una cartella montata da C:. Nessun test Windows nativo è attestato da questo README.

## Collaudi documentati

Documentazione del 18 ottobre 2026: demo ed esempi acquisiti con l’ambiente indicato; suite congelata di 8 metodi unittest già verificata. Nessuna suite è stata rieseguita per preparare questo README.

Queste istruzioni sono state ricavate dai file e dai collaudi conservati. La preparazione dei README non ha eseguito nuove suite né modificato il codice.
