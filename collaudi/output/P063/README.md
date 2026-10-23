# P063 — output reali dei collaudi

Esito registrato: **PASS**. [Run 39849393701](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701) · [job 120071206449](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701/job/120071206449).

Commit del runner: `44cd421247ca2bfe838baa735cf6180134f80464`. Sorgenti applicativi congelati: `32e201b1fb1258c4e7c77d32af323b966647b908`.

Ambiente registrato: Ubuntu 24.04 x86_64; Python 3.12.15 (main, Oct  1 2026, 02:35:59) [GCC 13.3.0]. Artifact: `p041-p080-core-39849393701-1` (ID `12456886835`); record originale: `P063/results.json`.

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

Rapporto registrato: 19 metodi unittest; failures 0, errors 0, skipped 0; sottocasi dichiarati 133.

**stdout** — [file TXT](streams/001_unittest_project_suite.stdout.txt)

```text
{"errors": 0, "failures": 0, "project": "P063", "skipped": 0, "subcases": 133, "successful": true, "tests_run": 19}
```

**stderr** — [file TXT](streams/001_unittest_project_suite.stderr.txt)

```text
test_audit_has_no_secrets (test_auth_service.AuthenticationTests.test_audit_has_no_secrets) ... ok
test_bad_credentials_have_generic_message (test_auth_service.AuthenticationTests.test_bad_credentials_have_generic_message) ... ok
test_corrupted_hash_fails_closed (test_auth_service.AuthenticationTests.test_corrupted_hash_fails_closed) ... ok
test_lockout_exact_boundary (test_auth_service.AuthenticationTests.test_lockout_exact_boundary) ... ok
test_logout_and_unknown_token (test_auth_service.AuthenticationTests.test_logout_and_unknown_token) ... ok
test_malformed_totp_is_rejected (test_auth_service.AuthenticationTests.test_malformed_totp_is_rejected) ... ok
test_password_is_scrypt_not_cleartext (test_auth_service.AuthenticationTests.test_password_is_scrypt_not_cleartext) ... ok
test_registration_constraints_and_duplicate (test_auth_service.AuthenticationTests.test_registration_constraints_and_duplicate) ... ok
test_replay_state_survives_database_reopen (test_auth_service.AuthenticationTests.test_replay_state_survives_database_reopen) ... ok
test_secret_and_configuration_validation (test_auth_service.AuthenticationTests.test_secret_and_configuration_validation) ... ok
test_session_expires_at_exact_deadline_and_is_removed (test_auth_service.AuthenticationTests.test_session_expires_at_exact_deadline_and_is_removed) ... ok
test_success_resets_failure_counter (test_auth_service.AuthenticationTests.test_success_resets_failure_counter) ... ok
test_timezone_and_epoch_boundaries (test_auth_service.AuthenticationTests.test_timezone_and_epoch_boundaries) ... ok
test_totp_replay_is_rejected (test_auth_service.AuthenticationTests.test_totp_replay_is_rejected) ... ok
test_unique_salts_for_same_password (test_auth_service.AuthenticationTests.test_unique_salts_for_same_password) ... ok
test_username_normalization_and_password_spaces_preserved (test_auth_service.AuthenticationTests.test_username_normalization_and_password_spaces_preserved) ... ok
test_valid_login_and_session (test_auth_service.AuthenticationTests.test_valid_login_and_session) ... ok
test_100_seeded_time_window_properties (test_auth_service.TOTPReferenceTests.test_100_seeded_time_window_properties) ... ok
test_rfc6238_sha1_vectors (test_auth_service.TOTPReferenceTests.test_rfc6238_sha1_vectors) ... ok

----------------------------------------------------------------------
Ran 19 tests in 6.878s

OK
```

## Demo — processi separati dalle suite

Questi output provengono dalle demo eseguite dal runner. Non costituiscono nuovi metodi unittest.

### 002 · demo_auth_service

Comando registrato (array degli argomenti; segnaposto dei metadati documentati nel manifest):

```json
["<PYTHON_HOME>/bin/python", "-B", "src/auth_service.py"]
```

Esito: **PASS** · codice di uscita: `0`.

**stdout** — [file TXT](streams/002_demo_auth_service.stdout.txt)

```text
Algoritmo password: scrypt
Primo login: True
Stesso TOTP riutilizzato: False
Sessione valida: True
Dopo logout: False
```

**stderr** — [file TXT](streams/002_demo_auth_service.stderr.txt)

Il processo non ha emesso byte su stderr. Il file collegato è vuoto (0 byte).

## Controlli runtime

Il record di questo progetto non contiene controlli classificati come `runtime_check`. L’assenza non aggiunge una verifica runtime alle suite del progetto.

## Verifica e provenienza

[Registro strutturato](registro.json) · [Hash e trasformazioni](MANIFEST.json) · [Policy](../AUDIT.md) · [Indice](../README.md)
