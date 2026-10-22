# P067 — HTTPS sotto il cofano: TLS, certificati e PKI

Esegue un handshake TLS su loopback usando certificati e chiavi temporanei.

Tutti i comandi partono dalla cartella `projects/P067`. I blocchi seguenti usano la sintassi di Linux/Bash.

## Requisiti e versioni

Linguaggio: Python.

- Python 3.12.14 (ambiente documentato)
- cryptography 50.0.2 (ambiente documentato)
- OpenSSL 3.5.8 (prova documentale)

Dipendenze:

- cryptography 50.0.2 — Generazione e lettura dei certificati X.509 e delle chiavi; dipendenza diretta di sorgente e test.

## Preparazione

Comandi per una shell Linux/Bash dalla cartella projects/P067. Installare Python 3.12 prima della preparazione; dopo l’attivazione, python indica l’interprete dell’ambiente virtuale .venv. Riattivare l’ambiente in ogni nuovo terminale. Le versioni indicate descrivono gli ambienti documentati, non un minimo universale.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
python -m pip install -r ../../requirements-p061-p080.txt
```

## Avvio

```bash
python -B src/cert_check.py
```

## Test

```bash
python -B run_tests.py
```

## Perimetro del laboratorio

- Il README registra OpenSSL 3.5.8. Il modulo ssl deve supportare almeno TLS 1.2; la versione e il cifrario negoziati non sono risultati fissi.
- Per il laboratorio completo su Windows usare una cartella nel filesystem Linux di WSL, così il controllo dei permessi conserva la semantica POSIX.
- Il file requirements-p061-p080.txt prepara l’ambiente condiviso del gruppo: comprende anche pacchetti non importati direttamente da questo singolo progetto.

## Windows

La demo usa socket loopback, ssl e cryptography, compatibili in linea di principio con un runtime Windows adatto. Il test test_new_files_and_private_key_mode confronta senza skip stat.S_IMODE(...st_mode) con 0o600: il requisito POSIX non va promesso su Windows nativo. Per riprodurre l’intero laboratorio da Windows usare WSL con una distribuzione Linux e una cartella nel filesystem Linux, non una cartella montata da C:. Nessun test Windows nativo è attestato da questo README.

## Collaudi documentati

Documentazione del 18 ottobre 2026: demo ed esempi acquisiti con l’ambiente indicato; suite congelata di 14 metodi unittest già verificata. Nessuna suite è stata rieseguita per preparare questo README.

Queste istruzioni sono state ricavate dai file e dai collaudi conservati. La preparazione dei README non ha eseguito nuove suite né modificato il codice.
