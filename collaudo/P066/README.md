# P066: output dei collaudi

[Indice dei collaudi](../README.md) · [Codice e istruzioni](../../projects/P066/README.md)

Esito registrato: **PASS**. [Run 39849393701](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701) · [job 120071206449](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701/job/120071206449).

Commit del runner: `44cd421247ca2bfe838baa735cf6180134f80464`. Sorgenti applicativi congelati: `32e201b1fb1258c4e7c77d32af323b966647b908`.

Ambiente registrato: Ubuntu 24.04 x86_64; Python 3.12.15 (main, Oct  1 2026, 02:35:59) [GCC 13.3.0]. Artifact: `p041-p080-core-39849393701-1` (ID `12456886835`); record originale: `P066/results.json`.

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

Rapporto registrato: 25 metodi unittest; failures 0, errors 0, skipped 0; sottocasi dichiarati 487.

**stdout** — [file TXT](streams/001_unittest_project_suite.stdout.txt)

```text
{"errors": 0, "failures": 0, "project": "P066", "skipped": 0, "subcases": 487, "successful": true, "tests_run": 25}
```

**stderr** — [file TXT](streams/001_unittest_project_suite.stderr.txt)

```text
test_100_seeded_fractional_sequences_against_decimal_reference (test_p066.RateLimitTests.test_100_seeded_fractional_sequences_against_decimal_reference) ... ok
test_100_seeded_sequences_against_reference (test_p066.RateLimitTests.test_100_seeded_sequences_against_reference) ... ok
test_clock_reversal_rejected_without_append (test_p066.RateLimitTests.test_clock_reversal_rejected_without_append) ... ok
test_extreme_windows_keep_same_time_requests (test_p066.RateLimitTests.test_extreme_windows_keep_same_time_requests) ... ok
test_invalid_parameters (test_p066.RateLimitTests.test_invalid_parameters) ... ok
test_keys_are_independent_and_capacity_bounded (test_p066.RateLimitTests.test_keys_are_independent_and_capacity_bounded) ... ok
test_large_integer_limiter_boundary_is_exact (test_p066.RateLimitTests.test_large_integer_limiter_boundary_is_exact) ... ok
test_local_pipeline_denies_before_resource (test_p066.RateLimitTests.test_local_pipeline_denies_before_resource) ... ok
test_original_limit_and_boundary (test_p066.RateLimitTests.test_original_limit_and_boundary) ... ok
test_rounded_cutoff_does_not_expire_recent_event (test_p066.RateLimitTests.test_rounded_cutoff_does_not_expire_recent_event) ... ok
test_100_seeded_large_integer_token_boundaries (test_p066.TokenTests.test_100_seeded_large_integer_token_boundaries) ... ok
test_100_seeded_lifetime_and_tampering_cases (test_p066.TokenTests.test_100_seeded_lifetime_and_tampering_cases) ... ok
test_algorithm_and_header_allowlist (test_p066.TokenTests.test_algorithm_and_header_allowlist) ... ok
test_base64url_is_strict_and_canonical (test_p066.TokenTests.test_base64url_is_strict_and_canonical) ... ok
test_configuration_rejected (test_p066.TokenTests.test_configuration_rejected) ... ok
test_expiry_exact_boundary_and_fractional_now (test_p066.TokenTests.test_expiry_exact_boundary_and_fractional_now) ... ok
test_issuer_and_audience_are_required (test_p066.TokenTests.test_issuer_and_audience_are_required) ... ok
test_json_duplicates_and_nonfinite_values_rejected (test_p066.TokenTests.test_json_duplicates_and_nonfinite_values_rejected) ... ok
test_large_integer_token_times_keep_exact_boundaries (test_p066.TokenTests.test_large_integer_token_times_keep_exact_boundaries) ... ok
test_malformed_tokens_fail_as_value_error (test_p066.TokenTests.test_malformed_tokens_fail_as_value_error) ... ok
test_missing_unknown_and_mistyped_claims (test_p066.TokenTests.test_missing_unknown_and_mistyped_claims) ... ok
test_not_before_and_issued_at (test_p066.TokenTests.test_not_before_and_issued_at) ... ok
test_signed_roundtrip_and_original_roles (test_p066.TokenTests.test_signed_roundtrip_and_original_roles) ... ok
test_unknown_roles_deny_instead_of_escalating (test_p066.TokenTests.test_unknown_roles_deny_instead_of_escalating) ... ok
test_wrong_key_and_tampered_payload (test_p066.TokenTests.test_wrong_key_and_tampered_payload) ... ok

----------------------------------------------------------------------
Ran 25 tests in 0.059s

OK
```

## Demo — processi separati dalle suite

Questi output provengono dalle demo eseguite dal runner. Non costituiscono nuovi metodi unittest.

### 002 · demo_auth_api

Comando registrato (array degli argomenti; segnaposto dei metadati documentati nel manifest):

```json
["<PYTHON_HOME>/bin/python", "-B", "src/auth_api.py"]
```

Esito: **PASS** · codice di uscita: `0`.

**stdout** — [file TXT](streams/002_demo_auth_api.stdout.txt)

```text
Lettura: 200
Amministrazione: 403
Token a exp: 401
Limite richieste: 429
```

**stderr** — [file TXT](streams/002_demo_auth_api.stderr.txt)

Il processo non ha emesso byte su stderr. Il file collegato è vuoto (0 byte).

## Controlli runtime

Il record di questo progetto non contiene controlli classificati come `runtime_check`. L’assenza non aggiunge una verifica runtime alle suite del progetto.

## Verifica e provenienza

[Registro strutturato](registro.json) · [Hash e trasformazioni](MANIFEST.json) · [Policy](../AUDIT.md) · [Indice](../README.md)
