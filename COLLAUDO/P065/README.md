# P065: output dei collaudi

[Indice dei collaudi](../README.md) · [Codice e istruzioni](../../projects/P065/README.md)

Esito registrato: **PASS**. [Run 39849393701](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701) · [job 120071206449](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701/job/120071206449).

Commit del runner: `44cd421247ca2bfe838baa735cf6180134f80464`. Sorgenti applicativi congelati: `32e201b1fb1258c4e7c77d32af323b966647b908`.

Ambiente registrato: Ubuntu 24.04 x86_64; Python 3.12.15 (main, Oct  1 2026, 02:35:59) [GCC 13.3.0]. Artifact: `p041-p080-core-39849393701-1` (ID `12456886835`); record originale: `P065/results.json`.

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

Rapporto registrato: 13 metodi unittest; failures 0, errors 0, skipped 0; sottocasi dichiarati 126.

**stdout** — [file TXT](streams/001_unittest_project_suite.stdout.txt)

```text
{"errors": 0, "failures": 0, "project": "P065", "skipped": 0, "subcases": 126, "successful": true, "tests_run": 13}
```

**stderr** — [file TXT](streams/001_unittest_project_suite.stderr.txt)

```text
test_100_seeded_html_roundtrips (test_p065.WebDefenseTests.test_100_seeded_html_roundtrips) ... ok
test_cross_session_token_is_rejected (test_p065.WebDefenseTests.test_cross_session_token_is_rejected) ... ok
test_csp_is_on_failure_responses_too (test_p065.WebDefenseTests.test_csp_is_on_failure_responses_too) ... ok
test_expiration_exact_boundary (test_p065.WebDefenseTests.test_expiration_exact_boundary) ... ok
test_generated_token_properties (test_p065.WebDefenseTests.test_generated_token_properties) ... ok
test_get_cannot_modify_state (test_p065.WebDefenseTests.test_get_cannot_modify_state) ... ok
test_html_encoding_quotes_ampersand_and_script (test_p065.WebDefenseTests.test_html_encoding_quotes_ampersand_and_script) ... ok
test_input_limits_and_unknown_session (test_p065.WebDefenseTests.test_input_limits_and_unknown_session) ... ok
test_logout_invalidates_csrf (test_p065.WebDefenseTests.test_logout_invalidates_csrf) ... ok
test_missing_wrong_and_malformed_csrf_deny_without_mutation (test_p065.WebDefenseTests.test_missing_wrong_and_malformed_csrf_deny_without_mutation) ... ok
test_request_modifies_state_and_encodes_output (test_p065.WebDefenseTests.test_request_modifies_state_and_encodes_output) ... ok
test_session_expiry_overflow_and_precision_rejected (test_p065.WebDefenseTests.test_session_expiry_overflow_and_precision_rejected) ... ok
test_token_reusable_inside_its_session (test_p065.WebDefenseTests.test_token_reusable_inside_its_session) ... ok

----------------------------------------------------------------------
Ran 13 tests in 0.009s

OK
```

## Demo — processi separati dalle suite

Questi output provengono dalle demo eseguite dal runner. Non costituiscono nuovi metodi unittest.

### 002 · demo_web_defense

Comando registrato (array degli argomenti; segnaposto dei metadati documentati nel manifest):

```json
["<PYTHON_HOME>/bin/python", "-B", "src/web_defense.py"]
```

Esito: **PASS** · codice di uscita: `0`.

**stdout** — [file TXT](streams/002_demo_web_defense.stdout.txt)

```text
Richiesta valida: 200
HTML: <p>&lt;b&gt;Ciao&lt;/b&gt; &amp; arrivederci</p>
Token mancante: 403
Sessione scaduta: 403
CSP: default-src 'none'; script-src 'none'; object-src 'none'; base-uri 'none'; frame-ancestors 'none'; form-action 'self'
```

**stderr** — [file TXT](streams/002_demo_web_defense.stderr.txt)

Il processo non ha emesso byte su stderr. Il file collegato è vuoto (0 byte).

## Controlli runtime

Il record di questo progetto non contiene controlli classificati come `runtime_check`. L’assenza non aggiunge una verifica runtime alle suite del progetto.

## Verifica e provenienza

[Registro strutturato](registro.json) · [Hash e trasformazioni](MANIFEST.json) · [Policy](../AUDIT.md) · [Indice](../README.md)
