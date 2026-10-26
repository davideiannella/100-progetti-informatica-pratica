# P064: output dei collaudi

[Indice dei collaudi](../README.md) · [Codice e istruzioni](../../projects/P064/README.md)

Esito registrato: **PASS**. [Run 39849393701](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701) · [job 120071206449](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701/job/120071206449).

Commit del runner: `44cd421247ca2bfe838baa735cf6180134f80464`. Sorgenti applicativi congelati: `32e201b1fb1258c4e7c77d32af323b966647b908`.

Ambiente registrato: Ubuntu 24.04 x86_64; Python 3.12.15 (main, Oct  1 2026, 02:35:59) [GCC 13.3.0]. Artifact: `p041-p080-core-39849393701-1` (ID `12456886835`); record originale: `P064/results.json`.

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

Rapporto registrato: 8 metodi unittest; failures 0, errors 0, skipped 0; sottocasi dichiarati 114.

**stdout** — [file TXT](streams/001_unittest_project_suite.stdout.txt)

```text
{"errors": 0, "failures": 0, "project": "P064", "skipped": 0, "subcases": 114, "successful": true, "tests_run": 8}
```

**stderr** — [file TXT](streams/001_unittest_project_suite.stderr.txt)

```text
test_100_seeded_literal_roundtrips (test_p064.ParameterizedQueryTests.test_100_seeded_literal_roundtrips) ... ok
test_closed_connection_error_is_not_hidden (test_p064.ParameterizedQueryTests.test_closed_connection_error_is_not_hidden) ... ok
test_input_types_and_length (test_p064.ParameterizedQueryTests.test_input_types_and_length) ... ok
test_known_and_unknown_users (test_p064.ParameterizedQueryTests.test_known_and_unknown_users) ... ok
test_metacharacters_can_be_valid_literal_username (test_p064.ParameterizedQueryTests.test_metacharacters_can_be_valid_literal_username) ... ok
test_seed_transaction_is_committed (test_p064.ParameterizedQueryTests.test_seed_transaction_is_committed) ... ok
test_sql_syntax_is_only_data (test_p064.ParameterizedQueryTests.test_sql_syntax_is_only_data) ... ok
test_unicode_and_exact_case (test_p064.ParameterizedQueryTests.test_unicode_and_exact_case) ... ok

----------------------------------------------------------------------
Ran 8 tests in 0.008s

OK
```

## Demo — processi separati dalle suite

Questi output provengono dalle demo eseguite dal runner. Non costituiscono nuovi metodi unittest.

### 002 · demo_safe_search

Comando registrato (array degli argomenti; segnaposto dei metadati documentati nel manifest):

```json
["<PYTHON_HOME>/bin/python", "-B", "src/safe_search.py"]
```

Esito: **PASS** · codice di uscita: `0`.

**stdout** — [file TXT](streams/002_demo_safe_search.stdout.txt)

```text
Ricerca anna: ('anna', 'user')
Ricerca metacaratteri: None
Utenti ancora presenti: 2
```

**stderr** — [file TXT](streams/002_demo_safe_search.stderr.txt)

Il processo non ha emesso byte su stderr. Il file collegato è vuoto (0 byte).

## Controlli runtime

Il record di questo progetto non contiene controlli classificati come `runtime_check`. L’assenza non aggiunge una verifica runtime alle suite del progetto.

## Verifica e provenienza

[Registro strutturato](registro.json) · [Hash e trasformazioni](MANIFEST.json) · [Policy](../AUDIT.md) · [Indice](../README.md)
