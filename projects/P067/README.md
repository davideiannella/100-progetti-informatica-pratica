# P067: Come funziona HTTPS: TLS, certificati e PKI

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P067/README.md) · [Registro del collaudo](../../collaudo/P067/registro.json)

**Sezione:** [Sezione 7: Sicurezza informatica](../../docs/CATALOGO.md#sezione-7-sicurezza-informatica).

**Argomenti:** Sicurezza delle comunicazioni · TLS · Certificati.

Il progetto apre una connessione TLS tra due programmi sullo stesso computer, usando certificati e chiavi temporanei. Mostra come viene verificata l’identità del server: è il livello di sicurezza usato da HTTPS, senza implementare il protocollo HTTP.

Apri un terminale nella cartella `projects/P067`. I comandi qui sotto sono scritti per Linux con Bash; per Windows consulta la sezione dedicata.

## Requisiti e versioni

**Tecnologie utilizzate:** Python · cryptography · TLS.

- Python 3.12.14 (ambiente documentato)
- cryptography 50.0.2 (ambiente documentato)
- OpenSSL 3.5.8 (prova documentale)

Dipendenze:

- cryptography 50.0.2 — Generazione e lettura dei certificati X.509 e delle chiavi; dipendenza diretta di sorgente e test.

## Preparazione

Installa Python 3.12, poi esegui i comandi qui sotto per creare e attivare un ambiente virtuale dedicato al progetto, nella cartella `.venv`. Dopo l’attivazione, il comando `python` usa questo ambiente. Riattivalo ogni volta che apri un nuovo terminale.

Le versioni elencate sono quelle degli ambienti documentati; non indicano la versione minima compatibile.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
python -m pip install -r ../../requirements-p061-p080.txt
```

## Avvio

Esegui la dimostrazione per vedere l’esito dello scambio TLS locale, la verifica dell’impronta del certificato e il rifiuto di un nome del server errato.

```bash
python -B src/cert_check.py
```

## Esempio documentale

L’esempio mostra uno scambio TLS sullo stesso computer e sei casi in cui un certificato viene rifiutato. Certificati e chiavi vengono creati in cartelle temporanee e rimossi al termine. Dopo aver preparato l’ambiente Python, esegui dalla cartella `projects/P067`:

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

## Perimetro del laboratorio

- L’ambiente documentato usa OpenSSL 3.5.8. Il modulo `ssl` deve supportare almeno TLS 1.2. La versione TLS e il cifrario scelti durante la connessione possono cambiare da un ambiente all’altro.
- Per eseguire tutto il laboratorio da Windows, usa WSL e una cartella nel filesystem Linux: il controllo dei permessi richiede il comportamento POSIX.
- Il file `requirements-p061-p080.txt` prepara un ambiente condiviso dai progetti P061–P080. Per questo include anche pacchetti che questo progetto non usa direttamente.

## Windows

Per riprodurre l’intero laboratorio da Windows, usa WSL con una distribuzione Linux. Salva il progetto nel filesystem Linux, non in una cartella montata dall’unità C:.

La demo usa socket locali, `ssl` e `cryptography`, che possono funzionare anche con un’installazione Windows adatta. La suite richiede però i permessi POSIX: il test `test_new_files_and_private_key_mode` verifica che `stat.S_IMODE(...st_mode)` sia uguale a `0o600` e non viene saltato su Windows. Le prove conservate non documentano un collaudo su Windows nativo.

## Collaudi documentati

La documentazione del 18 ottobre 2026 descrive una suite di 14 metodi di test `unittest`. I collegamenti «Output verificati» e «Registro del collaudo», all’inizio della pagina, riportano risultati, comandi e ambiente delle prove conservate.
