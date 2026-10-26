# P086: output dei collaudi

[Indice dei collaudi](../README.md) · [Codice e istruzioni](../../projects/P086/README.md)

Esito registrato: **PASS in tutte le quattro combinazioni**. [Run 39893701054](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39893701054) · commit `3ab7bdfedb20a443bd71fe4e4ffe3c1dd67bd707`.

Comando effettivo del [runner a quel commit](https://github.com/davideiannella/100-progetti-informatica-pratica/blob/3ab7bdfedb20a443bd71fe4e4ffe3c1dd67bd707/tools/collaudo_p081_p100.py): `[sys.executable, "-B", "run_tests.py"]`, con directory di lavoro `projects/P086`. `sys.executable` indica l’interprete della combinazione riportata sotto; il suo percorso host assoluto non è registrato nella summary.

I quattro rapporti sono output CI preesistenti, non nuove esecuzioni preparate per questa pagina. Ogni ambiente ha verificato gli hash dei 299 sorgenti, compilato 60 file Python e completato 20 suite per 377 metodi complessivi.

`unittest` scrive normalmente il rapporto dettagliato su **stderr**: questo non equivale a un errore. I nomi e gli esiti sotto provengono dalle righe effettivamente emesse; non sono stati ricostruiti dal codice. I TXT mantengono i byte e i terminatori originali, compreso CRLF su Windows; i blocchi Markdown normalizzano soltanto i terminatori.

## Suite — quattro ambienti CI

### ubuntu-latest-python-3.12

Artifact: `output-p081-p100-ubuntu-latest-python-3.12` (ID `12476170749`). [Summary originale](../ambienti/ubuntu-latest-python-3.12.summary.json).

OS: `Linux` · piattaforma: `Linux-6.17.0-1022-azure-x86_64-with-glibc2.39` · Python: `3.12.15 (main, Oct  1 2026, 02:35:59) [GCC 13.3.0]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **18** · skipped: `0`.

**stdout** — [file TXT](streams/ubuntu-latest-python-3.12.stdout.txt)

Il processo non ha emesso byte su stdout. Il file collegato è vuoto (0 byte).

**stderr** — [file TXT](streams/ubuntu-latest-python-3.12.stderr.txt)

```text
test_alert_equality_is_not_exceedance (test_p086.AirMonitorTests.test_alert_equality_is_not_exceedance) ... ok
test_alert_event_has_origin_and_time (test_p086.AirMonitorTests.test_alert_event_has_origin_and_time) ... ok
test_alerts_are_independent (test_p086.AirMonitorTests.test_alerts_are_independent) ... ok
test_configurable_thresholds (test_p086.AirMonitorTests.test_configurable_thresholds) ... ok
test_device_and_schema (test_p086.AirMonitorTests.test_device_and_schema) ... ok
test_duplicate_timestamp_rejected (test_p086.AirMonitorTests.test_duplicate_timestamp_rejected) ... ok
test_empty_summary (test_p086.AirMonitorTests.test_empty_summary) ... ok
test_history_and_readings_cannot_be_edited (test_p086.AirMonitorTests.test_history_and_readings_cannot_be_edited) ... ok
test_invalid_reading_is_atomic (test_p086.AirMonitorTests.test_invalid_reading_is_atomic) ... ok
test_invalid_thresholds (test_p086.AirMonitorTests.test_invalid_thresholds) ... ok
test_late_event_does_not_change_state (test_p086.AirMonitorTests.test_late_event_does_not_change_state) ... ok
test_nonfinite_and_wrong_numeric_types (test_p086.AirMonitorTests.test_nonfinite_and_wrong_numeric_types) ... ok
test_order_is_per_device (test_p086.AirMonitorTests.test_order_is_per_device) ... ok
test_out_of_range (test_p086.AirMonitorTests.test_out_of_range) ... ok
test_range_endpoints (test_p086.AirMonitorTests.test_range_endpoints) ... ok
test_summary_real_values (test_p086.AirMonitorTests.test_summary_real_values) ... ok
test_units_are_explicit (test_p086.AirMonitorTests.test_units_are_explicit) ... ok
test_valid_reading (test_p086.AirMonitorTests.test_valid_reading) ... ok

----------------------------------------------------------------------
Ran 18 tests in 0.003s

OK
```

### ubuntu-latest-python-3.13

Artifact: `output-p081-p100-ubuntu-latest-python-3.13` (ID `12476095990`). [Summary originale](../ambienti/ubuntu-latest-python-3.13.summary.json).

OS: `Linux` · piattaforma: `Linux-6.17.0-1022-azure-x86_64-with-glibc2.39` · Python: `3.13.16 (main, Oct  1 2026, 02:37:54) [GCC 13.3.0]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **18** · skipped: `0`.

**stdout** — [file TXT](streams/ubuntu-latest-python-3.13.stdout.txt)

Il processo non ha emesso byte su stdout. Il file collegato è vuoto (0 byte).

**stderr** — [file TXT](streams/ubuntu-latest-python-3.13.stderr.txt)

```text
test_alert_equality_is_not_exceedance (test_p086.AirMonitorTests.test_alert_equality_is_not_exceedance) ... ok
test_alert_event_has_origin_and_time (test_p086.AirMonitorTests.test_alert_event_has_origin_and_time) ... ok
test_alerts_are_independent (test_p086.AirMonitorTests.test_alerts_are_independent) ... ok
test_configurable_thresholds (test_p086.AirMonitorTests.test_configurable_thresholds) ... ok
test_device_and_schema (test_p086.AirMonitorTests.test_device_and_schema) ... ok
test_duplicate_timestamp_rejected (test_p086.AirMonitorTests.test_duplicate_timestamp_rejected) ... ok
test_empty_summary (test_p086.AirMonitorTests.test_empty_summary) ... ok
test_history_and_readings_cannot_be_edited (test_p086.AirMonitorTests.test_history_and_readings_cannot_be_edited) ... ok
test_invalid_reading_is_atomic (test_p086.AirMonitorTests.test_invalid_reading_is_atomic) ... ok
test_invalid_thresholds (test_p086.AirMonitorTests.test_invalid_thresholds) ... ok
test_late_event_does_not_change_state (test_p086.AirMonitorTests.test_late_event_does_not_change_state) ... ok
test_nonfinite_and_wrong_numeric_types (test_p086.AirMonitorTests.test_nonfinite_and_wrong_numeric_types) ... ok
test_order_is_per_device (test_p086.AirMonitorTests.test_order_is_per_device) ... ok
test_out_of_range (test_p086.AirMonitorTests.test_out_of_range) ... ok
test_range_endpoints (test_p086.AirMonitorTests.test_range_endpoints) ... ok
test_summary_real_values (test_p086.AirMonitorTests.test_summary_real_values) ... ok
test_units_are_explicit (test_p086.AirMonitorTests.test_units_are_explicit) ... ok
test_valid_reading (test_p086.AirMonitorTests.test_valid_reading) ... ok

----------------------------------------------------------------------
Ran 18 tests in 0.003s

OK
```

### windows-latest-python-3.12

Artifact: `output-p081-p100-windows-latest-python-3.12` (ID `12475927047`). [Summary originale](../ambienti/windows-latest-python-3.12.summary.json).

OS: `Windows` · piattaforma: `Windows-2025Server-10.0.26100-SP0` · Python: `3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **18** · skipped: `0`.

**stdout** — [file TXT](streams/windows-latest-python-3.12.stdout.txt)

Il processo non ha emesso byte su stdout. Il file collegato è vuoto (0 byte).

**stderr** — [file TXT](streams/windows-latest-python-3.12.stderr.txt)

```text
test_alert_equality_is_not_exceedance (test_p086.AirMonitorTests.test_alert_equality_is_not_exceedance) ... ok
test_alert_event_has_origin_and_time (test_p086.AirMonitorTests.test_alert_event_has_origin_and_time) ... ok
test_alerts_are_independent (test_p086.AirMonitorTests.test_alerts_are_independent) ... ok
test_configurable_thresholds (test_p086.AirMonitorTests.test_configurable_thresholds) ... ok
test_device_and_schema (test_p086.AirMonitorTests.test_device_and_schema) ... ok
test_duplicate_timestamp_rejected (test_p086.AirMonitorTests.test_duplicate_timestamp_rejected) ... ok
test_empty_summary (test_p086.AirMonitorTests.test_empty_summary) ... ok
test_history_and_readings_cannot_be_edited (test_p086.AirMonitorTests.test_history_and_readings_cannot_be_edited) ... ok
test_invalid_reading_is_atomic (test_p086.AirMonitorTests.test_invalid_reading_is_atomic) ... ok
test_invalid_thresholds (test_p086.AirMonitorTests.test_invalid_thresholds) ... ok
test_late_event_does_not_change_state (test_p086.AirMonitorTests.test_late_event_does_not_change_state) ... ok
test_nonfinite_and_wrong_numeric_types (test_p086.AirMonitorTests.test_nonfinite_and_wrong_numeric_types) ... ok
test_order_is_per_device (test_p086.AirMonitorTests.test_order_is_per_device) ... ok
test_out_of_range (test_p086.AirMonitorTests.test_out_of_range) ... ok
test_range_endpoints (test_p086.AirMonitorTests.test_range_endpoints) ... ok
test_summary_real_values (test_p086.AirMonitorTests.test_summary_real_values) ... ok
test_units_are_explicit (test_p086.AirMonitorTests.test_units_are_explicit) ... ok
test_valid_reading (test_p086.AirMonitorTests.test_valid_reading) ... ok

----------------------------------------------------------------------
Ran 18 tests in 0.002s

OK
```

### windows-latest-python-3.13

Artifact: `output-p081-p100-windows-latest-python-3.13` (ID `12475826902`). [Summary originale](../ambienti/windows-latest-python-3.13.summary.json).

OS: `Windows` · piattaforma: `Windows-2025Server-10.0.26100-SP0` · Python: `3.13.16 (tags/v3.13.16:cbc944f, Sep 30 2026, 19:17:50) [MSC v.1944 64 bit (AMD64)]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **18** · skipped: `0`.

**stdout** — [file TXT](streams/windows-latest-python-3.13.stdout.txt)

Il processo non ha emesso byte su stdout. Il file collegato è vuoto (0 byte).

**stderr** — [file TXT](streams/windows-latest-python-3.13.stderr.txt)

```text
test_alert_equality_is_not_exceedance (test_p086.AirMonitorTests.test_alert_equality_is_not_exceedance) ... ok
test_alert_event_has_origin_and_time (test_p086.AirMonitorTests.test_alert_event_has_origin_and_time) ... ok
test_alerts_are_independent (test_p086.AirMonitorTests.test_alerts_are_independent) ... ok
test_configurable_thresholds (test_p086.AirMonitorTests.test_configurable_thresholds) ... ok
test_device_and_schema (test_p086.AirMonitorTests.test_device_and_schema) ... ok
test_duplicate_timestamp_rejected (test_p086.AirMonitorTests.test_duplicate_timestamp_rejected) ... ok
test_empty_summary (test_p086.AirMonitorTests.test_empty_summary) ... ok
test_history_and_readings_cannot_be_edited (test_p086.AirMonitorTests.test_history_and_readings_cannot_be_edited) ... ok
test_invalid_reading_is_atomic (test_p086.AirMonitorTests.test_invalid_reading_is_atomic) ... ok
test_invalid_thresholds (test_p086.AirMonitorTests.test_invalid_thresholds) ... ok
test_late_event_does_not_change_state (test_p086.AirMonitorTests.test_late_event_does_not_change_state) ... ok
test_nonfinite_and_wrong_numeric_types (test_p086.AirMonitorTests.test_nonfinite_and_wrong_numeric_types) ... ok
test_order_is_per_device (test_p086.AirMonitorTests.test_order_is_per_device) ... ok
test_out_of_range (test_p086.AirMonitorTests.test_out_of_range) ... ok
test_range_endpoints (test_p086.AirMonitorTests.test_range_endpoints) ... ok
test_summary_real_values (test_p086.AirMonitorTests.test_summary_real_values) ... ok
test_units_are_explicit (test_p086.AirMonitorTests.test_units_are_explicit) ... ok
test_valid_reading (test_p086.AirMonitorTests.test_valid_reading) ... ok

----------------------------------------------------------------------
Ran 18 tests in 0.002s

OK
```

## Demo e controlli runtime

Questa matrice esegue le suite `run_tests.py`. Le summary non classificano processi separati come demo o controlli runtime: non sono aggiunti output o esiti di tali categorie.

## Verifica e provenienza

[Registro strutturato](registro.json) · [Hash e trasformazioni](MANIFEST.json) · [Policy](../AUDIT.md) · [Indice](../README.md)
