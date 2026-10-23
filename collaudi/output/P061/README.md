# P061 — output reali dei collaudi

Esito registrato: **PASS**. [Run 39849393701](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701) · [job 120071206449](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701/job/120071206449).

Commit del runner: `44cd421247ca2bfe838baa735cf6180134f80464`. Sorgenti applicativi congelati: `32e201b1fb1258c4e7c77d32af323b966647b908`.

Ambiente registrato: Ubuntu 24.04 x86_64; Python 3.12.15 (main, Oct  1 2026, 02:35:59) [GCC 13.3.0]. Artifact: `p041-p080-core-39849393701-1` (ID `12456886835`); record originale: `P061/results.json`.

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

Rapporto registrato: 9 metodi unittest; failures 0, errors 0, skipped 0; sottocasi dichiarati 118.

**stdout** — [file TXT](streams/001_unittest_project_suite.stdout.txt)

```text
{"errors": 0, "failures": 0, "project": "P061", "skipped": 0, "subcases": 118, "successful": true, "tests_run": 9}
```

**stderr** — [file TXT](streams/001_unittest_project_suite.stderr.txt)

```text
test_100_seeded_windows_against_reference (test_p061.ObservabilityTests.test_100_seeded_windows_against_reference) ... ok
test_empty_window_is_unknown (test_p061.ObservabilityTests.test_empty_window_is_unknown) ... ok
test_invalid_records_are_atomic (test_p061.ObservabilityTests.test_invalid_records_are_atomic) ... ok
test_invalid_thresholds (test_p061.ObservabilityTests.test_invalid_thresholds) ... ok
test_original_degraded_case (test_p061.ObservabilityTests.test_original_degraded_case) ... ok
test_original_healthy_case (test_p061.ObservabilityTests.test_original_healthy_case) ... ok
test_structured_log_is_one_json_line (test_p061.ObservabilityTests.test_structured_log_is_one_json_line) ... ok
test_sum_overflow_does_not_count_request (test_p061.ObservabilityTests.test_sum_overflow_does_not_count_request) ... ok
test_threshold_equality_and_both_alerts (test_p061.ObservabilityTests.test_threshold_equality_and_both_alerts) ... ok

----------------------------------------------------------------------
Ran 9 tests in 0.007s

OK
```

## Demo — processi separati dalle suite

Questi output provengono dalle demo eseguite dal runner. Non costituiscono nuovi metodi unittest.

### 002 · demo_observability

Comando registrato (array degli argomenti; segnaposto dei metadati documentati nel manifest):

```json
["<PYTHON_HOME>/bin/python", "-B", "src/observability.py"]
```

Esito: **PASS** · codice di uscita: `0`.

**stdout** — [file TXT](streams/002_demo_observability.stdout.txt)

```text
Finestra vuota: ['no_data']
Richieste=4; disponibilità=100.00%; media=112.5 ms
Alert: []
{"component": "catalogo", "latency_ms": 500.0, "ok": false, "trace_id": "trace-lab-1"}
Dopo il guasto: disponibilità=80.00%; alert=['availability']
```

**stderr** — [file TXT](streams/002_demo_observability.stderr.txt)

Il processo non ha emesso byte su stderr. Il file collegato è vuoto (0 byte).

## Controlli runtime

Il record di questo progetto non contiene controlli classificati come `runtime_check`. L’assenza non aggiunge una verifica runtime alle suite del progetto.

## Verifica e provenienza

[Registro strutturato](registro.json) · [Hash e trasformazioni](MANIFEST.json) · [Policy](../AUDIT.md) · [Indice](../README.md)
