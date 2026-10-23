# P067 — output reali dei collaudi

Esito registrato: **PASS**. [Run 39849393701](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701) · [job 120071206449](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701/job/120071206449).

Commit del runner: `44cd421247ca2bfe838baa735cf6180134f80464`. Sorgenti applicativi congelati: `32e201b1fb1258c4e7c77d32af323b966647b908`.

Ambiente registrato: Ubuntu 24.04 x86_64; Python 3.12.15 (main, Oct  1 2026, 02:35:59) [GCC 13.3.0]. Artifact: `p041-p080-core-39849393701-1` (ID `12456886835`); record originale: `P067/results.json`.

Questa pagina deriva dai risultati CI già acquisiti. Non è stata eseguita una nuova suite per prepararla. I blocchi riportano il testo emesso, dopo le sole sostituzioni di metadati indicate nel manifest. I TXT conservano i terminatori originali; per la lettura Markdown i terminatori sono normalizzati.

`unittest` scrive normalmente il proprio rapporto su **stderr**: la presenza di testo in quel canale non equivale a un errore. Esito e codice di uscita sono riportati separatamente.

I programmi di assert possono stampare soltanto un riepilogo o niente. I sottocasi non nominati dal processo restano non nominati: questa raccolta non ricostruisce nomi, valori o esiti di singoli assert. I rapporti `unittest` compatti a punti non rendono disponibili i nomi dei metodi.

## Suite di test

### 001 · unittest_project_suite

Comando registrato (array degli argomenti; segnaposto dei metadati documentati nel manifest):

```json
["<PYTHON_HOME>/bin/python", "-B", "run_tests.py"]
```

Esito: **PASS** · codice di uscita: `0`.

Rapporto registrato: 14 metodi unittest; failures 0, errors 0, skipped 0; sottocasi dichiarati 0.

**stdout** — [file TXT](streams/001_unittest_project_suite.stdout.txt)

```text
{"errors": 0, "failures": 0, "skipped": 0, "tests_run": 14}
```

**stderr** — [file TXT](streams/001_unittest_project_suite.stderr.txt)

```text
test_compatibility_api_normalizes_fingerprint (test_p067.TLSLabTests.test_compatibility_api_normalizes_fingerprint) ... ok
test_expired_certificate_rejected (test_p067.TLSLabTests.test_expired_certificate_rejected) ... ok
test_fingerprint_is_sha256_of_der (test_p067.TLSLabTests.test_fingerprint_is_sha256_of_der) ... ok
test_future_certificate_rejected (test_p067.TLSLabTests.test_future_certificate_rejected) ... ok
test_hostname_rejected (test_p067.TLSLabTests.test_hostname_rejected) ... ok
test_invalid_lab_parameters (test_p067.TLSLabTests.test_invalid_lab_parameters) ... ok
test_ip_is_not_dns_san (test_p067.TLSLabTests.test_ip_is_not_dns_san) ... ok
test_malformed_certificate_rejected (test_p067.TLSLabTests.test_malformed_certificate_rejected) ... ok
test_new_files_and_private_key_mode (test_p067.TLSLabTests.test_new_files_and_private_key_mode) ... ok
test_payload_boundaries (test_p067.TLSLabTests.test_payload_boundaries) ... ok
test_real_handshake_and_echo (test_p067.TLSLabTests.test_real_handshake_and_echo) ... ok
test_unknown_ca_rejected (test_p067.TLSLabTests.test_unknown_ca_rejected) ... ok
test_wrong_extended_key_usage_rejected (test_p067.TLSLabTests.test_wrong_extended_key_usage_rejected) ... ok
test_wrong_private_key_rejected (test_p067.TLSLabTests.test_wrong_private_key_rejected) ... ok

----------------------------------------------------------------------
Ran 14 tests in 0.079s

OK
```

## Demo — processi separati dalle suite

Questi output provengono dalle demo eseguite dal runner. Non costituiscono nuovi metodi unittest.

### 002 · demo_cert_check

Comando registrato (array degli argomenti; segnaposto dei metadati documentati nel manifest):

```json
["<PYTHON_HOME>/bin/python", "-B", "src/cert_check.py"]
```

Esito: **PASS** · codice di uscita: `0`.

**stdout** — [file TXT](streams/002_demo_cert_check.stdout.txt)

```text
TLS verificato: ciao TLS
Impronta corrispondente: True
Hostname errato: RIFIUTATO
```

**stderr** — [file TXT](streams/002_demo_cert_check.stderr.txt)

Il processo non ha emesso byte su stderr. Il file collegato è vuoto (0 byte).

## Controlli runtime

Il record di questo progetto non contiene controlli classificati come `runtime_check`. L’assenza non aggiunge una verifica runtime alle suite del progetto.

## Verifica e provenienza

[Registro strutturato](registro.json) · [Hash e trasformazioni](MANIFEST.json) · [Policy](../AUDIT.md) · [Indice](../README.md)
