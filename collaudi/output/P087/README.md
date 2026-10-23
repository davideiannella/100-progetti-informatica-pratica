# P087 — output reali dei collaudi

Esito registrato: **PASS in tutte le quattro combinazioni**. [Run 39893701054](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39893701054) · commit `3ab7bdfedb20a443bd71fe4e4ffe3c1dd67bd707`.

Comando effettivo del [runner a quel commit](https://github.com/davideiannella/100-progetti-informatica-pratica/blob/3ab7bdfedb20a443bd71fe4e4ffe3c1dd67bd707/tools/collaudo_p081_p100.py): `[sys.executable, "-B", "run_tests.py"]`, con directory di lavoro `projects/P087`. `sys.executable` indica l’interprete della combinazione riportata sotto; il suo percorso host assoluto non è registrato nella summary.

I quattro rapporti sono output CI preesistenti, non nuove esecuzioni preparate per questa pagina. Ogni ambiente ha verificato gli hash dei 299 sorgenti, compilato 60 file Python e completato 20 suite per 377 metodi complessivi.

`unittest` scrive normalmente il rapporto dettagliato su **stderr**: questo non equivale a un errore. I nomi e gli esiti sotto provengono dalle righe effettivamente emesse; non sono stati ricostruiti dal codice. I TXT mantengono i byte e i terminatori originali, compreso CRLF su Windows; i blocchi Markdown normalizzano soltanto i terminatori.

## Suite — quattro ambienti CI

### ubuntu-latest-python-3.12

Artifact: `output-p081-p100-ubuntu-latest-python-3.12` (ID `12476170749`). [Summary originale](../ambienti/ubuntu-latest-python-3.12.summary.json).

OS: `Linux` · piattaforma: `Linux-6.17.0-1022-azure-x86_64-with-glibc2.39` · Python: `3.12.15 (main, Oct  1 2026, 02:35:59) [GCC 13.3.0]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **23** · skipped: `0`.

**stdout** — [file TXT](streams/ubuntu-latest-python-3.12.stdout.txt)

Il processo non ha emesso byte su stdout. Il file collegato è vuoto (0 byte).

**stderr** — [file TXT](streams/ubuntu-latest-python-3.12.stderr.txt)

```text
test_collector_conflicting_id_rejected (test_p087.SmartMeterTests.test_collector_conflicting_id_rejected) ... ok
test_collector_duplicate_ignored (test_p087.SmartMeterTests.test_collector_duplicate_ignored) ... ok
test_demo_and_weighted_average (test_p087.SmartMeterTests.test_demo_and_weighted_average) ... ok
test_empty_collector_summary (test_p087.SmartMeterTests.test_empty_collector_summary) ... ok
test_inconsistent_energy_and_total_rejected (test_p087.SmartMeterTests.test_inconsistent_energy_and_total_rejected) ... ok
test_initial_time_and_register (test_p087.SmartMeterTests.test_initial_time_and_register) ... ok
test_invalid_alert_limit (test_p087.SmartMeterTests.test_invalid_alert_limit) ... ok
test_invalid_event_schema (test_p087.SmartMeterTests.test_invalid_event_schema) ... ok
test_invalid_identifiers (test_p087.SmartMeterTests.test_invalid_identifiers) ... ok
test_invalid_initial_values (test_p087.SmartMeterTests.test_invalid_initial_values) ... ok
test_invalid_power_and_time (test_p087.SmartMeterTests.test_invalid_power_and_time) ... ok
test_meter_id_conflict_is_atomic (test_p087.SmartMeterTests.test_meter_id_conflict_is_atomic) ... ok
test_meter_retry_is_idempotent (test_p087.SmartMeterTests.test_meter_retry_is_idempotent) ... ok
test_missing_interval_then_replay (test_p087.SmartMeterTests.test_missing_interval_then_replay) ... ok
test_nonincreasing_time_rejected (test_p087.SmartMeterTests.test_nonincreasing_time_rejected) ... ok
test_overflow_rejected (test_p087.SmartMeterTests.test_overflow_rejected) ... ok
test_overlap_and_reordered_event_rejected (test_p087.SmartMeterTests.test_overlap_and_reordered_event_rejected) ... ok
test_power_alert_threshold_is_strict (test_p087.SmartMeterTests.test_power_alert_threshold_is_strict) ... ok
test_seconds_to_hours (test_p087.SmartMeterTests.test_seconds_to_hours) ... ok
test_unrepresentable_increment_rejected (test_p087.SmartMeterTests.test_unrepresentable_increment_rejected) ... ok
test_variable_intervals (test_p087.SmartMeterTests.test_variable_intervals) ... ok
test_wrong_device_rejected (test_p087.SmartMeterTests.test_wrong_device_rejected) ... ok
test_zero_power_is_valid (test_p087.SmartMeterTests.test_zero_power_is_valid) ... ok

----------------------------------------------------------------------
Ran 23 tests in 0.003s

OK
```

### ubuntu-latest-python-3.13

Artifact: `output-p081-p100-ubuntu-latest-python-3.13` (ID `12476095990`). [Summary originale](../ambienti/ubuntu-latest-python-3.13.summary.json).

OS: `Linux` · piattaforma: `Linux-6.17.0-1022-azure-x86_64-with-glibc2.39` · Python: `3.13.16 (main, Oct  1 2026, 02:37:54) [GCC 13.3.0]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **23** · skipped: `0`.

**stdout** — [file TXT](streams/ubuntu-latest-python-3.13.stdout.txt)

Il processo non ha emesso byte su stdout. Il file collegato è vuoto (0 byte).

**stderr** — [file TXT](streams/ubuntu-latest-python-3.13.stderr.txt)

```text
test_collector_conflicting_id_rejected (test_p087.SmartMeterTests.test_collector_conflicting_id_rejected) ... ok
test_collector_duplicate_ignored (test_p087.SmartMeterTests.test_collector_duplicate_ignored) ... ok
test_demo_and_weighted_average (test_p087.SmartMeterTests.test_demo_and_weighted_average) ... ok
test_empty_collector_summary (test_p087.SmartMeterTests.test_empty_collector_summary) ... ok
test_inconsistent_energy_and_total_rejected (test_p087.SmartMeterTests.test_inconsistent_energy_and_total_rejected) ... ok
test_initial_time_and_register (test_p087.SmartMeterTests.test_initial_time_and_register) ... ok
test_invalid_alert_limit (test_p087.SmartMeterTests.test_invalid_alert_limit) ... ok
test_invalid_event_schema (test_p087.SmartMeterTests.test_invalid_event_schema) ... ok
test_invalid_identifiers (test_p087.SmartMeterTests.test_invalid_identifiers) ... ok
test_invalid_initial_values (test_p087.SmartMeterTests.test_invalid_initial_values) ... ok
test_invalid_power_and_time (test_p087.SmartMeterTests.test_invalid_power_and_time) ... ok
test_meter_id_conflict_is_atomic (test_p087.SmartMeterTests.test_meter_id_conflict_is_atomic) ... ok
test_meter_retry_is_idempotent (test_p087.SmartMeterTests.test_meter_retry_is_idempotent) ... ok
test_missing_interval_then_replay (test_p087.SmartMeterTests.test_missing_interval_then_replay) ... ok
test_nonincreasing_time_rejected (test_p087.SmartMeterTests.test_nonincreasing_time_rejected) ... ok
test_overflow_rejected (test_p087.SmartMeterTests.test_overflow_rejected) ... ok
test_overlap_and_reordered_event_rejected (test_p087.SmartMeterTests.test_overlap_and_reordered_event_rejected) ... ok
test_power_alert_threshold_is_strict (test_p087.SmartMeterTests.test_power_alert_threshold_is_strict) ... ok
test_seconds_to_hours (test_p087.SmartMeterTests.test_seconds_to_hours) ... ok
test_unrepresentable_increment_rejected (test_p087.SmartMeterTests.test_unrepresentable_increment_rejected) ... ok
test_variable_intervals (test_p087.SmartMeterTests.test_variable_intervals) ... ok
test_wrong_device_rejected (test_p087.SmartMeterTests.test_wrong_device_rejected) ... ok
test_zero_power_is_valid (test_p087.SmartMeterTests.test_zero_power_is_valid) ... ok

----------------------------------------------------------------------
Ran 23 tests in 0.003s

OK
```

### windows-latest-python-3.12

Artifact: `output-p081-p100-windows-latest-python-3.12` (ID `12475927047`). [Summary originale](../ambienti/windows-latest-python-3.12.summary.json).

OS: `Windows` · piattaforma: `Windows-2025Server-10.0.26100-SP0` · Python: `3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **23** · skipped: `0`.

**stdout** — [file TXT](streams/windows-latest-python-3.12.stdout.txt)

Il processo non ha emesso byte su stdout. Il file collegato è vuoto (0 byte).

**stderr** — [file TXT](streams/windows-latest-python-3.12.stderr.txt)

```text
test_collector_conflicting_id_rejected (test_p087.SmartMeterTests.test_collector_conflicting_id_rejected) ... ok
test_collector_duplicate_ignored (test_p087.SmartMeterTests.test_collector_duplicate_ignored) ... ok
test_demo_and_weighted_average (test_p087.SmartMeterTests.test_demo_and_weighted_average) ... ok
test_empty_collector_summary (test_p087.SmartMeterTests.test_empty_collector_summary) ... ok
test_inconsistent_energy_and_total_rejected (test_p087.SmartMeterTests.test_inconsistent_energy_and_total_rejected) ... ok
test_initial_time_and_register (test_p087.SmartMeterTests.test_initial_time_and_register) ... ok
test_invalid_alert_limit (test_p087.SmartMeterTests.test_invalid_alert_limit) ... ok
test_invalid_event_schema (test_p087.SmartMeterTests.test_invalid_event_schema) ... ok
test_invalid_identifiers (test_p087.SmartMeterTests.test_invalid_identifiers) ... ok
test_invalid_initial_values (test_p087.SmartMeterTests.test_invalid_initial_values) ... ok
test_invalid_power_and_time (test_p087.SmartMeterTests.test_invalid_power_and_time) ... ok
test_meter_id_conflict_is_atomic (test_p087.SmartMeterTests.test_meter_id_conflict_is_atomic) ... ok
test_meter_retry_is_idempotent (test_p087.SmartMeterTests.test_meter_retry_is_idempotent) ... ok
test_missing_interval_then_replay (test_p087.SmartMeterTests.test_missing_interval_then_replay) ... ok
test_nonincreasing_time_rejected (test_p087.SmartMeterTests.test_nonincreasing_time_rejected) ... ok
test_overflow_rejected (test_p087.SmartMeterTests.test_overflow_rejected) ... ok
test_overlap_and_reordered_event_rejected (test_p087.SmartMeterTests.test_overlap_and_reordered_event_rejected) ... ok
test_power_alert_threshold_is_strict (test_p087.SmartMeterTests.test_power_alert_threshold_is_strict) ... ok
test_seconds_to_hours (test_p087.SmartMeterTests.test_seconds_to_hours) ... ok
test_unrepresentable_increment_rejected (test_p087.SmartMeterTests.test_unrepresentable_increment_rejected) ... ok
test_variable_intervals (test_p087.SmartMeterTests.test_variable_intervals) ... ok
test_wrong_device_rejected (test_p087.SmartMeterTests.test_wrong_device_rejected) ... ok
test_zero_power_is_valid (test_p087.SmartMeterTests.test_zero_power_is_valid) ... ok

----------------------------------------------------------------------
Ran 23 tests in 0.002s

OK
```

### windows-latest-python-3.13

Artifact: `output-p081-p100-windows-latest-python-3.13` (ID `12475826902`). [Summary originale](../ambienti/windows-latest-python-3.13.summary.json).

OS: `Windows` · piattaforma: `Windows-2025Server-10.0.26100-SP0` · Python: `3.13.16 (tags/v3.13.16:cbc944f, Sep 30 2026, 19:17:50) [MSC v.1944 64 bit (AMD64)]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **23** · skipped: `0`.

**stdout** — [file TXT](streams/windows-latest-python-3.13.stdout.txt)

Il processo non ha emesso byte su stdout. Il file collegato è vuoto (0 byte).

**stderr** — [file TXT](streams/windows-latest-python-3.13.stderr.txt)

```text
test_collector_conflicting_id_rejected (test_p087.SmartMeterTests.test_collector_conflicting_id_rejected) ... ok
test_collector_duplicate_ignored (test_p087.SmartMeterTests.test_collector_duplicate_ignored) ... ok
test_demo_and_weighted_average (test_p087.SmartMeterTests.test_demo_and_weighted_average) ... ok
test_empty_collector_summary (test_p087.SmartMeterTests.test_empty_collector_summary) ... ok
test_inconsistent_energy_and_total_rejected (test_p087.SmartMeterTests.test_inconsistent_energy_and_total_rejected) ... ok
test_initial_time_and_register (test_p087.SmartMeterTests.test_initial_time_and_register) ... ok
test_invalid_alert_limit (test_p087.SmartMeterTests.test_invalid_alert_limit) ... ok
test_invalid_event_schema (test_p087.SmartMeterTests.test_invalid_event_schema) ... ok
test_invalid_identifiers (test_p087.SmartMeterTests.test_invalid_identifiers) ... ok
test_invalid_initial_values (test_p087.SmartMeterTests.test_invalid_initial_values) ... ok
test_invalid_power_and_time (test_p087.SmartMeterTests.test_invalid_power_and_time) ... ok
test_meter_id_conflict_is_atomic (test_p087.SmartMeterTests.test_meter_id_conflict_is_atomic) ... ok
test_meter_retry_is_idempotent (test_p087.SmartMeterTests.test_meter_retry_is_idempotent) ... ok
test_missing_interval_then_replay (test_p087.SmartMeterTests.test_missing_interval_then_replay) ... ok
test_nonincreasing_time_rejected (test_p087.SmartMeterTests.test_nonincreasing_time_rejected) ... ok
test_overflow_rejected (test_p087.SmartMeterTests.test_overflow_rejected) ... ok
test_overlap_and_reordered_event_rejected (test_p087.SmartMeterTests.test_overlap_and_reordered_event_rejected) ... ok
test_power_alert_threshold_is_strict (test_p087.SmartMeterTests.test_power_alert_threshold_is_strict) ... ok
test_seconds_to_hours (test_p087.SmartMeterTests.test_seconds_to_hours) ... ok
test_unrepresentable_increment_rejected (test_p087.SmartMeterTests.test_unrepresentable_increment_rejected) ... ok
test_variable_intervals (test_p087.SmartMeterTests.test_variable_intervals) ... ok
test_wrong_device_rejected (test_p087.SmartMeterTests.test_wrong_device_rejected) ... ok
test_zero_power_is_valid (test_p087.SmartMeterTests.test_zero_power_is_valid) ... ok

----------------------------------------------------------------------
Ran 23 tests in 0.002s

OK
```

## Demo e controlli runtime

Questa matrice esegue le suite `run_tests.py`. Le summary non classificano processi separati come demo o controlli runtime: non sono aggiunti output o esiti di tali categorie.

## Verifica e provenienza

[Registro strutturato](registro.json) · [Hash e trasformazioni](MANIFEST.json) · [Policy](../AUDIT.md) · [Indice](../README.md)
