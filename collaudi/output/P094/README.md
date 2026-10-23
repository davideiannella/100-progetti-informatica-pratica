# P094 — output reali dei collaudi

Esito registrato: **PASS in tutte le quattro combinazioni**. [Run 39893701054](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39893701054) · commit `3ab7bdfedb20a443bd71fe4e4ffe3c1dd67bd707`.

Comando effettivo del [runner a quel commit](https://github.com/davideiannella/100-progetti-informatica-pratica/blob/3ab7bdfedb20a443bd71fe4e4ffe3c1dd67bd707/tools/collaudo_p081_p100.py): `[sys.executable, "-B", "run_tests.py"]`, con directory di lavoro `projects/P094`. `sys.executable` indica l’interprete della combinazione riportata sotto; il suo percorso host assoluto non è registrato nella summary.

I quattro rapporti sono output CI preesistenti, non nuove esecuzioni preparate per questa pagina. Ogni ambiente ha verificato gli hash dei 299 sorgenti, compilato 60 file Python e completato 20 suite per 377 metodi complessivi.

`unittest` scrive normalmente il rapporto dettagliato su **stderr**: questo non equivale a un errore. I nomi e gli esiti sotto provengono dalle righe effettivamente emesse; non sono stati ricostruiti dal codice. I TXT mantengono i byte e i terminatori originali, compreso CRLF su Windows; i blocchi Markdown normalizzano soltanto i terminatori.

## Suite — quattro ambienti CI

### ubuntu-latest-python-3.12

Artifact: `output-p081-p100-ubuntu-latest-python-3.12` (ID `12476170749`). [Summary originale](../ambienti/ubuntu-latest-python-3.12.summary.json).

OS: `Linux` · piattaforma: `Linux-6.17.0-1022-azure-x86_64-with-glibc2.39` · Python: `3.12.15 (main, Oct  1 2026, 02:35:59) [GCC 13.3.0]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **20** · skipped: `0`.

**stdout** — [file TXT](streams/ubuntu-latest-python-3.12.stdout.txt)

```text
test_capacity_contract (test_p094.CityTests.test_capacity_contract) ... ok
test_conflicting_event_id_is_rejected_across_streams (test_p094.CityTests.test_conflicting_event_id_is_rejected_across_streams) ... ok
test_demo_has_eight_records_and_two_free_stalls (test_p094.CityTests.test_demo_has_eight_records_and_two_free_stalls) ... ok
test_duplicate_parking_event_is_idempotent (test_p094.CityTests.test_duplicate_parking_event_is_idempotent) ... ok
test_duplicate_traffic_and_air_do_not_bias_mean (test_p094.CityTests.test_duplicate_traffic_and_air_do_not_bias_mean) ... ok
test_empty_measurements_are_unknown_not_zero (test_p094.CityTests.test_empty_measurements_are_unknown_not_zero) ... ok
test_event_metadata_contract (test_p094.CityTests.test_event_metadata_contract) ... ok
test_event_snapshot_cannot_mutate_internal_history (test_p094.CityTests.test_event_snapshot_cannot_mutate_internal_history) ... ok
test_large_finite_values_do_not_overflow_the_mean (test_p094.CityTests.test_large_finite_values_do_not_overflow_the_mean) ... ok
test_limits_are_validated_even_without_samples (test_p094.CityTests.test_limits_are_validated_even_without_samples) ... ok
test_numeric_validation_rejects_nonfinite_bool_negative_and_text (test_p094.CityTests.test_numeric_validation_rejects_nonfinite_bool_negative_and_text) ... ok
test_occupy_and_release_stall (test_p094.CityTests.test_occupy_and_release_stall) ... ok
test_parking_identifier_and_bool_contract (test_p094.CityTests.test_parking_identifier_and_bool_contract) ... ok
test_public_snapshot_uses_aggregate_allowlist (test_p094.CityTests.test_public_snapshot_uses_aggregate_allowlist) ... ok
test_records_keep_source_zone_timestamp_and_unit (test_p094.CityTests.test_records_keep_source_zone_timestamp_and_unit) ... ok
test_stale_or_concurrent_parking_event_cannot_revert_state (test_p094.CityTests.test_stale_or_concurrent_parking_event_cannot_revert_state) ... ok
test_three_samples_match_hand_calculation (test_p094.CityTests.test_three_samples_match_hand_calculation) ... ok
test_threshold_equality_does_not_trigger_alert (test_p094.CityTests.test_threshold_equality_does_not_trigger_alert) ... ok
test_units_cannot_be_silently_mixed (test_p094.CityTests.test_units_cannot_be_silently_mixed) ... ok
test_zero_readings_are_valid (test_p094.CityTests.test_zero_readings_are_valid) ... ok

----------------------------------------------------------------------
Ran 20 tests in 0.002s

OK
```

**stderr** — [file TXT](streams/ubuntu-latest-python-3.12.stderr.txt)

Il processo non ha emesso byte su stderr. Il file collegato è vuoto (0 byte).

### ubuntu-latest-python-3.13

Artifact: `output-p081-p100-ubuntu-latest-python-3.13` (ID `12476095990`). [Summary originale](../ambienti/ubuntu-latest-python-3.13.summary.json).

OS: `Linux` · piattaforma: `Linux-6.17.0-1022-azure-x86_64-with-glibc2.39` · Python: `3.13.16 (main, Oct  1 2026, 02:37:54) [GCC 13.3.0]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **20** · skipped: `0`.

**stdout** — [file TXT](streams/ubuntu-latest-python-3.13.stdout.txt)

```text
test_capacity_contract (test_p094.CityTests.test_capacity_contract) ... ok
test_conflicting_event_id_is_rejected_across_streams (test_p094.CityTests.test_conflicting_event_id_is_rejected_across_streams) ... ok
test_demo_has_eight_records_and_two_free_stalls (test_p094.CityTests.test_demo_has_eight_records_and_two_free_stalls) ... ok
test_duplicate_parking_event_is_idempotent (test_p094.CityTests.test_duplicate_parking_event_is_idempotent) ... ok
test_duplicate_traffic_and_air_do_not_bias_mean (test_p094.CityTests.test_duplicate_traffic_and_air_do_not_bias_mean) ... ok
test_empty_measurements_are_unknown_not_zero (test_p094.CityTests.test_empty_measurements_are_unknown_not_zero) ... ok
test_event_metadata_contract (test_p094.CityTests.test_event_metadata_contract) ... ok
test_event_snapshot_cannot_mutate_internal_history (test_p094.CityTests.test_event_snapshot_cannot_mutate_internal_history) ... ok
test_large_finite_values_do_not_overflow_the_mean (test_p094.CityTests.test_large_finite_values_do_not_overflow_the_mean) ... ok
test_limits_are_validated_even_without_samples (test_p094.CityTests.test_limits_are_validated_even_without_samples) ... ok
test_numeric_validation_rejects_nonfinite_bool_negative_and_text (test_p094.CityTests.test_numeric_validation_rejects_nonfinite_bool_negative_and_text) ... ok
test_occupy_and_release_stall (test_p094.CityTests.test_occupy_and_release_stall) ... ok
test_parking_identifier_and_bool_contract (test_p094.CityTests.test_parking_identifier_and_bool_contract) ... ok
test_public_snapshot_uses_aggregate_allowlist (test_p094.CityTests.test_public_snapshot_uses_aggregate_allowlist) ... ok
test_records_keep_source_zone_timestamp_and_unit (test_p094.CityTests.test_records_keep_source_zone_timestamp_and_unit) ... ok
test_stale_or_concurrent_parking_event_cannot_revert_state (test_p094.CityTests.test_stale_or_concurrent_parking_event_cannot_revert_state) ... ok
test_three_samples_match_hand_calculation (test_p094.CityTests.test_three_samples_match_hand_calculation) ... ok
test_threshold_equality_does_not_trigger_alert (test_p094.CityTests.test_threshold_equality_does_not_trigger_alert) ... ok
test_units_cannot_be_silently_mixed (test_p094.CityTests.test_units_cannot_be_silently_mixed) ... ok
test_zero_readings_are_valid (test_p094.CityTests.test_zero_readings_are_valid) ... ok

----------------------------------------------------------------------
Ran 20 tests in 0.002s

OK
```

**stderr** — [file TXT](streams/ubuntu-latest-python-3.13.stderr.txt)

Il processo non ha emesso byte su stderr. Il file collegato è vuoto (0 byte).

### windows-latest-python-3.12

Artifact: `output-p081-p100-windows-latest-python-3.12` (ID `12475927047`). [Summary originale](../ambienti/windows-latest-python-3.12.summary.json).

OS: `Windows` · piattaforma: `Windows-2025Server-10.0.26100-SP0` · Python: `3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **20** · skipped: `0`.

**stdout** — [file TXT](streams/windows-latest-python-3.12.stdout.txt)

```text
test_capacity_contract (test_p094.CityTests.test_capacity_contract) ... ok
test_conflicting_event_id_is_rejected_across_streams (test_p094.CityTests.test_conflicting_event_id_is_rejected_across_streams) ... ok
test_demo_has_eight_records_and_two_free_stalls (test_p094.CityTests.test_demo_has_eight_records_and_two_free_stalls) ... ok
test_duplicate_parking_event_is_idempotent (test_p094.CityTests.test_duplicate_parking_event_is_idempotent) ... ok
test_duplicate_traffic_and_air_do_not_bias_mean (test_p094.CityTests.test_duplicate_traffic_and_air_do_not_bias_mean) ... ok
test_empty_measurements_are_unknown_not_zero (test_p094.CityTests.test_empty_measurements_are_unknown_not_zero) ... ok
test_event_metadata_contract (test_p094.CityTests.test_event_metadata_contract) ... ok
test_event_snapshot_cannot_mutate_internal_history (test_p094.CityTests.test_event_snapshot_cannot_mutate_internal_history) ... ok
test_large_finite_values_do_not_overflow_the_mean (test_p094.CityTests.test_large_finite_values_do_not_overflow_the_mean) ... ok
test_limits_are_validated_even_without_samples (test_p094.CityTests.test_limits_are_validated_even_without_samples) ... ok
test_numeric_validation_rejects_nonfinite_bool_negative_and_text (test_p094.CityTests.test_numeric_validation_rejects_nonfinite_bool_negative_and_text) ... ok
test_occupy_and_release_stall (test_p094.CityTests.test_occupy_and_release_stall) ... ok
test_parking_identifier_and_bool_contract (test_p094.CityTests.test_parking_identifier_and_bool_contract) ... ok
test_public_snapshot_uses_aggregate_allowlist (test_p094.CityTests.test_public_snapshot_uses_aggregate_allowlist) ... ok
test_records_keep_source_zone_timestamp_and_unit (test_p094.CityTests.test_records_keep_source_zone_timestamp_and_unit) ... ok
test_stale_or_concurrent_parking_event_cannot_revert_state (test_p094.CityTests.test_stale_or_concurrent_parking_event_cannot_revert_state) ... ok
test_three_samples_match_hand_calculation (test_p094.CityTests.test_three_samples_match_hand_calculation) ... ok
test_threshold_equality_does_not_trigger_alert (test_p094.CityTests.test_threshold_equality_does_not_trigger_alert) ... ok
test_units_cannot_be_silently_mixed (test_p094.CityTests.test_units_cannot_be_silently_mixed) ... ok
test_zero_readings_are_valid (test_p094.CityTests.test_zero_readings_are_valid) ... ok

----------------------------------------------------------------------
Ran 20 tests in 0.002s

OK
```

**stderr** — [file TXT](streams/windows-latest-python-3.12.stderr.txt)

Il processo non ha emesso byte su stderr. Il file collegato è vuoto (0 byte).

### windows-latest-python-3.13

Artifact: `output-p081-p100-windows-latest-python-3.13` (ID `12475826902`). [Summary originale](../ambienti/windows-latest-python-3.13.summary.json).

OS: `Windows` · piattaforma: `Windows-2025Server-10.0.26100-SP0` · Python: `3.13.16 (tags/v3.13.16:cbc944f, Sep 30 2026, 19:17:50) [MSC v.1944 64 bit (AMD64)]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **20** · skipped: `0`.

**stdout** — [file TXT](streams/windows-latest-python-3.13.stdout.txt)

```text
test_capacity_contract (test_p094.CityTests.test_capacity_contract) ... ok
test_conflicting_event_id_is_rejected_across_streams (test_p094.CityTests.test_conflicting_event_id_is_rejected_across_streams) ... ok
test_demo_has_eight_records_and_two_free_stalls (test_p094.CityTests.test_demo_has_eight_records_and_two_free_stalls) ... ok
test_duplicate_parking_event_is_idempotent (test_p094.CityTests.test_duplicate_parking_event_is_idempotent) ... ok
test_duplicate_traffic_and_air_do_not_bias_mean (test_p094.CityTests.test_duplicate_traffic_and_air_do_not_bias_mean) ... ok
test_empty_measurements_are_unknown_not_zero (test_p094.CityTests.test_empty_measurements_are_unknown_not_zero) ... ok
test_event_metadata_contract (test_p094.CityTests.test_event_metadata_contract) ... ok
test_event_snapshot_cannot_mutate_internal_history (test_p094.CityTests.test_event_snapshot_cannot_mutate_internal_history) ... ok
test_large_finite_values_do_not_overflow_the_mean (test_p094.CityTests.test_large_finite_values_do_not_overflow_the_mean) ... ok
test_limits_are_validated_even_without_samples (test_p094.CityTests.test_limits_are_validated_even_without_samples) ... ok
test_numeric_validation_rejects_nonfinite_bool_negative_and_text (test_p094.CityTests.test_numeric_validation_rejects_nonfinite_bool_negative_and_text) ... ok
test_occupy_and_release_stall (test_p094.CityTests.test_occupy_and_release_stall) ... ok
test_parking_identifier_and_bool_contract (test_p094.CityTests.test_parking_identifier_and_bool_contract) ... ok
test_public_snapshot_uses_aggregate_allowlist (test_p094.CityTests.test_public_snapshot_uses_aggregate_allowlist) ... ok
test_records_keep_source_zone_timestamp_and_unit (test_p094.CityTests.test_records_keep_source_zone_timestamp_and_unit) ... ok
test_stale_or_concurrent_parking_event_cannot_revert_state (test_p094.CityTests.test_stale_or_concurrent_parking_event_cannot_revert_state) ... ok
test_three_samples_match_hand_calculation (test_p094.CityTests.test_three_samples_match_hand_calculation) ... ok
test_threshold_equality_does_not_trigger_alert (test_p094.CityTests.test_threshold_equality_does_not_trigger_alert) ... ok
test_units_cannot_be_silently_mixed (test_p094.CityTests.test_units_cannot_be_silently_mixed) ... ok
test_zero_readings_are_valid (test_p094.CityTests.test_zero_readings_are_valid) ... ok

----------------------------------------------------------------------
Ran 20 tests in 0.002s

OK
```

**stderr** — [file TXT](streams/windows-latest-python-3.13.stderr.txt)

Il processo non ha emesso byte su stderr. Il file collegato è vuoto (0 byte).

## Demo e controlli runtime

Questa matrice esegue le suite `run_tests.py`. Le summary non classificano processi separati come demo o controlli runtime: non sono aggiunti output o esiti di tali categorie.

## Verifica e provenienza

[Registro strutturato](registro.json) · [Hash e trasformazioni](MANIFEST.json) · [Policy](../AUDIT.md) · [Indice](../README.md)
