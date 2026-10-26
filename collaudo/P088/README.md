# P088: output dei collaudi

[Indice dei collaudi](../README.md) · [Codice e istruzioni](../../projects/P088/README.md)

Esito registrato: **PASS in tutte le quattro combinazioni**. [Run 39893701054](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39893701054) · commit `3ab7bdfedb20a443bd71fe4e4ffe3c1dd67bd707`.

Comando effettivo del [runner a quel commit](https://github.com/davideiannella/100-progetti-informatica-pratica/blob/3ab7bdfedb20a443bd71fe4e4ffe3c1dd67bd707/tools/collaudo_p081_p100.py): `[sys.executable, "-B", "run_tests.py"]`, con directory di lavoro `projects/P088`. `sys.executable` indica l’interprete della combinazione riportata sotto; il suo percorso host assoluto non è registrato nella summary.

I quattro rapporti sono output CI preesistenti, non nuove esecuzioni preparate per questa pagina. Ogni ambiente ha verificato gli hash dei 299 sorgenti, compilato 60 file Python e completato 20 suite per 377 metodi complessivi.

`unittest` scrive normalmente il rapporto dettagliato su **stderr**: questo non equivale a un errore. I nomi e gli esiti sotto provengono dalle righe effettivamente emesse; non sono stati ricostruiti dal codice. I TXT mantengono i byte e i terminatori originali, compreso CRLF su Windows; i blocchi Markdown normalizzano soltanto i terminatori.

## Suite — quattro ambienti CI

### ubuntu-latest-python-3.12

Artifact: `output-p081-p100-ubuntu-latest-python-3.12` (ID `12476170749`). [Summary originale](../ambienti/ubuntu-latest-python-3.12.summary.json).

OS: `Linux` · piattaforma: `Linux-6.17.0-1022-azure-x86_64-with-glibc2.39` · Python: `3.12.15 (main, Oct  1 2026, 02:35:59) [GCC 13.3.0]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **22** · skipped: `0`.

**stdout** — [file TXT](streams/ubuntu-latest-python-3.12.stdout.txt)

Il processo non ha emesso byte su stdout. Il file collegato è vuoto (0 byte).

**stderr** — [file TXT](streams/ubuntu-latest-python-3.12.stderr.txt)

```text
test_capacity_never_overflows (test_p088.ParkingTests.test_capacity_never_overflows) ... ok
test_conflicting_id_rejected_without_changes (test_p088.ParkingTests.test_conflicting_id_rejected_without_changes) ... ok
test_demo_values_and_cached_old_snapshot (test_p088.ParkingTests.test_demo_values_and_cached_old_snapshot) ... ok
test_duplicate_enter_has_no_effect (test_p088.ParkingTests.test_duplicate_enter_has_no_effect) ... ok
test_duplicate_exit_after_new_arrival_is_safe (test_p088.ParkingTests.test_duplicate_exit_after_new_arrival_is_safe) ... ok
test_enter_and_exit_duration (test_p088.ParkingTests.test_enter_and_exit_duration) ... ok
test_equal_time_events_are_allowed (test_p088.ParkingTests.test_equal_time_events_are_allowed) ... ok
test_exit_empty_spot (test_p088.ParkingTests.test_exit_empty_spot) ... ok
test_exit_wrong_vehicle (test_p088.ParkingTests.test_exit_wrong_vehicle) ... ok
test_initial_capacity (test_p088.ParkingTests.test_initial_capacity) ... ok
test_invalid_capacity (test_p088.ParkingTests.test_invalid_capacity) ... ok
test_invalid_ids (test_p088.ParkingTests.test_invalid_ids) ... ok
test_invalid_input_is_atomic (test_p088.ParkingTests.test_invalid_input_is_atomic) ... ok
test_invalid_kind_and_schema (test_p088.ParkingTests.test_invalid_kind_and_schema) ... ok
test_invalid_spot_types_and_bounds (test_p088.ParkingTests.test_invalid_spot_types_and_bounds) ... ok
test_invalid_times (test_p088.ParkingTests.test_invalid_times) ... ok
test_late_unique_event_rejected (test_p088.ParkingTests.test_late_unique_event_rejected) ... ok
test_no_negative_occupancy_after_repeated_exit (test_p088.ParkingTests.test_no_negative_occupancy_after_repeated_exit) ... ok
test_rejected_retry_keeps_original_result (test_p088.ParkingTests.test_rejected_retry_keeps_original_result) ... ok
test_rejection_does_not_advance_time_watermark (test_p088.ParkingTests.test_rejection_does_not_advance_time_watermark) ... ok
test_snapshot_and_audit_do_not_expose_mutable_state (test_p088.ParkingTests.test_snapshot_and_audit_do_not_expose_mutable_state) ... ok
test_vehicle_cannot_occupy_two_spots (test_p088.ParkingTests.test_vehicle_cannot_occupy_two_spots) ... ok

----------------------------------------------------------------------
Ran 22 tests in 0.002s

OK
```

### ubuntu-latest-python-3.13

Artifact: `output-p081-p100-ubuntu-latest-python-3.13` (ID `12476095990`). [Summary originale](../ambienti/ubuntu-latest-python-3.13.summary.json).

OS: `Linux` · piattaforma: `Linux-6.17.0-1022-azure-x86_64-with-glibc2.39` · Python: `3.13.16 (main, Oct  1 2026, 02:37:54) [GCC 13.3.0]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **22** · skipped: `0`.

**stdout** — [file TXT](streams/ubuntu-latest-python-3.13.stdout.txt)

Il processo non ha emesso byte su stdout. Il file collegato è vuoto (0 byte).

**stderr** — [file TXT](streams/ubuntu-latest-python-3.13.stderr.txt)

```text
test_capacity_never_overflows (test_p088.ParkingTests.test_capacity_never_overflows) ... ok
test_conflicting_id_rejected_without_changes (test_p088.ParkingTests.test_conflicting_id_rejected_without_changes) ... ok
test_demo_values_and_cached_old_snapshot (test_p088.ParkingTests.test_demo_values_and_cached_old_snapshot) ... ok
test_duplicate_enter_has_no_effect (test_p088.ParkingTests.test_duplicate_enter_has_no_effect) ... ok
test_duplicate_exit_after_new_arrival_is_safe (test_p088.ParkingTests.test_duplicate_exit_after_new_arrival_is_safe) ... ok
test_enter_and_exit_duration (test_p088.ParkingTests.test_enter_and_exit_duration) ... ok
test_equal_time_events_are_allowed (test_p088.ParkingTests.test_equal_time_events_are_allowed) ... ok
test_exit_empty_spot (test_p088.ParkingTests.test_exit_empty_spot) ... ok
test_exit_wrong_vehicle (test_p088.ParkingTests.test_exit_wrong_vehicle) ... ok
test_initial_capacity (test_p088.ParkingTests.test_initial_capacity) ... ok
test_invalid_capacity (test_p088.ParkingTests.test_invalid_capacity) ... ok
test_invalid_ids (test_p088.ParkingTests.test_invalid_ids) ... ok
test_invalid_input_is_atomic (test_p088.ParkingTests.test_invalid_input_is_atomic) ... ok
test_invalid_kind_and_schema (test_p088.ParkingTests.test_invalid_kind_and_schema) ... ok
test_invalid_spot_types_and_bounds (test_p088.ParkingTests.test_invalid_spot_types_and_bounds) ... ok
test_invalid_times (test_p088.ParkingTests.test_invalid_times) ... ok
test_late_unique_event_rejected (test_p088.ParkingTests.test_late_unique_event_rejected) ... ok
test_no_negative_occupancy_after_repeated_exit (test_p088.ParkingTests.test_no_negative_occupancy_after_repeated_exit) ... ok
test_rejected_retry_keeps_original_result (test_p088.ParkingTests.test_rejected_retry_keeps_original_result) ... ok
test_rejection_does_not_advance_time_watermark (test_p088.ParkingTests.test_rejection_does_not_advance_time_watermark) ... ok
test_snapshot_and_audit_do_not_expose_mutable_state (test_p088.ParkingTests.test_snapshot_and_audit_do_not_expose_mutable_state) ... ok
test_vehicle_cannot_occupy_two_spots (test_p088.ParkingTests.test_vehicle_cannot_occupy_two_spots) ... ok

----------------------------------------------------------------------
Ran 22 tests in 0.002s

OK
```

### windows-latest-python-3.12

Artifact: `output-p081-p100-windows-latest-python-3.12` (ID `12475927047`). [Summary originale](../ambienti/windows-latest-python-3.12.summary.json).

OS: `Windows` · piattaforma: `Windows-2025Server-10.0.26100-SP0` · Python: `3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **22** · skipped: `0`.

**stdout** — [file TXT](streams/windows-latest-python-3.12.stdout.txt)

Il processo non ha emesso byte su stdout. Il file collegato è vuoto (0 byte).

**stderr** — [file TXT](streams/windows-latest-python-3.12.stderr.txt)

```text
test_capacity_never_overflows (test_p088.ParkingTests.test_capacity_never_overflows) ... ok
test_conflicting_id_rejected_without_changes (test_p088.ParkingTests.test_conflicting_id_rejected_without_changes) ... ok
test_demo_values_and_cached_old_snapshot (test_p088.ParkingTests.test_demo_values_and_cached_old_snapshot) ... ok
test_duplicate_enter_has_no_effect (test_p088.ParkingTests.test_duplicate_enter_has_no_effect) ... ok
test_duplicate_exit_after_new_arrival_is_safe (test_p088.ParkingTests.test_duplicate_exit_after_new_arrival_is_safe) ... ok
test_enter_and_exit_duration (test_p088.ParkingTests.test_enter_and_exit_duration) ... ok
test_equal_time_events_are_allowed (test_p088.ParkingTests.test_equal_time_events_are_allowed) ... ok
test_exit_empty_spot (test_p088.ParkingTests.test_exit_empty_spot) ... ok
test_exit_wrong_vehicle (test_p088.ParkingTests.test_exit_wrong_vehicle) ... ok
test_initial_capacity (test_p088.ParkingTests.test_initial_capacity) ... ok
test_invalid_capacity (test_p088.ParkingTests.test_invalid_capacity) ... ok
test_invalid_ids (test_p088.ParkingTests.test_invalid_ids) ... ok
test_invalid_input_is_atomic (test_p088.ParkingTests.test_invalid_input_is_atomic) ... ok
test_invalid_kind_and_schema (test_p088.ParkingTests.test_invalid_kind_and_schema) ... ok
test_invalid_spot_types_and_bounds (test_p088.ParkingTests.test_invalid_spot_types_and_bounds) ... ok
test_invalid_times (test_p088.ParkingTests.test_invalid_times) ... ok
test_late_unique_event_rejected (test_p088.ParkingTests.test_late_unique_event_rejected) ... ok
test_no_negative_occupancy_after_repeated_exit (test_p088.ParkingTests.test_no_negative_occupancy_after_repeated_exit) ... ok
test_rejected_retry_keeps_original_result (test_p088.ParkingTests.test_rejected_retry_keeps_original_result) ... ok
test_rejection_does_not_advance_time_watermark (test_p088.ParkingTests.test_rejection_does_not_advance_time_watermark) ... ok
test_snapshot_and_audit_do_not_expose_mutable_state (test_p088.ParkingTests.test_snapshot_and_audit_do_not_expose_mutable_state) ... ok
test_vehicle_cannot_occupy_two_spots (test_p088.ParkingTests.test_vehicle_cannot_occupy_two_spots) ... ok

----------------------------------------------------------------------
Ran 22 tests in 0.002s

OK
```

### windows-latest-python-3.13

Artifact: `output-p081-p100-windows-latest-python-3.13` (ID `12475826902`). [Summary originale](../ambienti/windows-latest-python-3.13.summary.json).

OS: `Windows` · piattaforma: `Windows-2025Server-10.0.26100-SP0` · Python: `3.13.16 (tags/v3.13.16:cbc944f, Sep 30 2026, 19:17:50) [MSC v.1944 64 bit (AMD64)]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **22** · skipped: `0`.

**stdout** — [file TXT](streams/windows-latest-python-3.13.stdout.txt)

Il processo non ha emesso byte su stdout. Il file collegato è vuoto (0 byte).

**stderr** — [file TXT](streams/windows-latest-python-3.13.stderr.txt)

```text
test_capacity_never_overflows (test_p088.ParkingTests.test_capacity_never_overflows) ... ok
test_conflicting_id_rejected_without_changes (test_p088.ParkingTests.test_conflicting_id_rejected_without_changes) ... ok
test_demo_values_and_cached_old_snapshot (test_p088.ParkingTests.test_demo_values_and_cached_old_snapshot) ... ok
test_duplicate_enter_has_no_effect (test_p088.ParkingTests.test_duplicate_enter_has_no_effect) ... ok
test_duplicate_exit_after_new_arrival_is_safe (test_p088.ParkingTests.test_duplicate_exit_after_new_arrival_is_safe) ... ok
test_enter_and_exit_duration (test_p088.ParkingTests.test_enter_and_exit_duration) ... ok
test_equal_time_events_are_allowed (test_p088.ParkingTests.test_equal_time_events_are_allowed) ... ok
test_exit_empty_spot (test_p088.ParkingTests.test_exit_empty_spot) ... ok
test_exit_wrong_vehicle (test_p088.ParkingTests.test_exit_wrong_vehicle) ... ok
test_initial_capacity (test_p088.ParkingTests.test_initial_capacity) ... ok
test_invalid_capacity (test_p088.ParkingTests.test_invalid_capacity) ... ok
test_invalid_ids (test_p088.ParkingTests.test_invalid_ids) ... ok
test_invalid_input_is_atomic (test_p088.ParkingTests.test_invalid_input_is_atomic) ... ok
test_invalid_kind_and_schema (test_p088.ParkingTests.test_invalid_kind_and_schema) ... ok
test_invalid_spot_types_and_bounds (test_p088.ParkingTests.test_invalid_spot_types_and_bounds) ... ok
test_invalid_times (test_p088.ParkingTests.test_invalid_times) ... ok
test_late_unique_event_rejected (test_p088.ParkingTests.test_late_unique_event_rejected) ... ok
test_no_negative_occupancy_after_repeated_exit (test_p088.ParkingTests.test_no_negative_occupancy_after_repeated_exit) ... ok
test_rejected_retry_keeps_original_result (test_p088.ParkingTests.test_rejected_retry_keeps_original_result) ... ok
test_rejection_does_not_advance_time_watermark (test_p088.ParkingTests.test_rejection_does_not_advance_time_watermark) ... ok
test_snapshot_and_audit_do_not_expose_mutable_state (test_p088.ParkingTests.test_snapshot_and_audit_do_not_expose_mutable_state) ... ok
test_vehicle_cannot_occupy_two_spots (test_p088.ParkingTests.test_vehicle_cannot_occupy_two_spots) ... ok

----------------------------------------------------------------------
Ran 22 tests in 0.002s

OK
```

## Demo e controlli runtime

Questa matrice esegue le suite `run_tests.py`. Le summary non classificano processi separati come demo o controlli runtime: non sono aggiunti output o esiti di tali categorie.

## Verifica e provenienza

[Registro strutturato](registro.json) · [Hash e trasformazioni](MANIFEST.json) · [Policy](../AUDIT.md) · [Indice](../README.md)
