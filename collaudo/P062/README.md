# P062: output dei collaudi

[Indice dei collaudi](../README.md) · [Codice e istruzioni](../../projects/P062/README.md)

Esito registrato: **PASS**. [Run 39849393701](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701) · [job 120071206449](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701/job/120071206449).

Commit del runner: `44cd421247ca2bfe838baa735cf6180134f80464`. Sorgenti applicativi congelati: `32e201b1fb1258c4e7c77d32af323b966647b908`.

Ambiente registrato: Ubuntu 24.04 x86_64; Python 3.12.15 (main, Oct  1 2026, 02:35:59) [GCC 13.3.0]. Artifact: `p041-p080-core-39849393701-1` (ID `12456886835`); record originale: `P062/results.json`.

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

Rapporto registrato: 10 metodi unittest; failures 0, errors 0, skipped 0; sottocasi dichiarati 106.

**stdout** — [file TXT](streams/001_unittest_project_suite.stdout.txt)

```text
{"errors": 0, "failures": 0, "project": "P062", "skipped": 0, "subcases": 106, "successful": true, "tests_run": 10}
```

**stderr** — [file TXT](streams/001_unittest_project_suite.stderr.txt)

```text
test_100_seeded_partition_scenarios (test_p062.DisasterRecoveryTests.test_100_seeded_partition_scenarios) ... ok
test_both_down_and_missing_key_fail (test_p062.DisasterRecoveryTests.test_both_down_and_missing_key_fail) ... ok
test_catchup_and_idempotence (test_p062.DisasterRecoveryTests.test_catchup_and_idempotence) ... ok
test_clock_and_interval_validation (test_p062.DisasterRecoveryTests.test_clock_and_interval_validation) ... ok
test_invalid_initial_topology (test_p062.DisasterRecoveryTests.test_invalid_initial_topology) ... ok
test_replication_and_read_failover (test_p062.DisasterRecoveryTests.test_replication_and_read_failover) ... ok
test_stale_update_is_exposed (test_p062.DisasterRecoveryTests.test_stale_update_is_exposed) ... ok
test_unreplicated_new_key_and_multiple_updates (test_p062.DisasterRecoveryTests.test_unreplicated_new_key_and_multiple_updates) ... ok
test_values_do_not_alias (test_p062.DisasterRecoveryTests.test_values_do_not_alias) ... ok
test_write_primary_down_is_rejected (test_p062.DisasterRecoveryTests.test_write_primary_down_is_rejected) ... ok

----------------------------------------------------------------------
Ran 10 tests in 0.015s

OK
```

## Demo — processi separati dalle suite

Questi output provengono dalle demo eseguite dal runner. Non costituiscono nuovi metodi unittest.

### 002 · demo_dr

Comando registrato (array degli argomenti; segnaposto dei metadati documentati nel manifest):

```json
["<PYTHON_HOME>/bin/python", "-B", "src/dr.py"]
```

Esito: **PASS** · codice di uscita: `0`.

**stdout** — [file TXT](streams/002_demo_dr.stdout.txt)

```text
Esposizione: {'pending_writes': 1, 'affected_keys': ['ordine-1'], 'recovery_point': 10.0, 'potential_loss_window_s': 15.0}
Failover di lettura: ('ricevuto', 'zona-b')
Durata ripristino simulata: 3.0 s
Divergenze dopo recupero: []
```

**stderr** — [file TXT](streams/002_demo_dr.stderr.txt)

Il processo non ha emesso byte su stderr. Il file collegato è vuoto (0 byte).

## Controlli runtime

Il record di questo progetto non contiene controlli classificati come `runtime_check`. L’assenza non aggiunge una verifica runtime alle suite del progetto.

## Verifica e provenienza

[Registro strutturato](registro.json) · [Hash e trasformazioni](MANIFEST.json) · [Policy](../AUDIT.md) · [Indice](../README.md)
