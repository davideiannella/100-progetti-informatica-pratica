# P095: output dei collaudi

[Indice dei collaudi](../README.md) · [Codice e istruzioni](../../projects/P095/README.md)

Esito registrato: **PASS in tutte le quattro combinazioni**. [Run 39893701054](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39893701054) · commit `3ab7bdfedb20a443bd71fe4e4ffe3c1dd67bd707`.

Comando effettivo del [runner a quel commit](https://github.com/davideiannella/100-progetti-informatica-pratica/blob/3ab7bdfedb20a443bd71fe4e4ffe3c1dd67bd707/tools/collaudo_p081_p100.py): `[sys.executable, "-B", "run_tests.py"]`, con directory di lavoro `projects/P095`. `sys.executable` indica l’interprete della combinazione riportata sotto; il suo percorso host assoluto non è registrato nella summary.

I quattro rapporti sono output CI preesistenti, non nuove esecuzioni preparate per questa pagina. Ogni ambiente ha verificato gli hash dei 299 sorgenti, compilato 60 file Python e completato 20 suite per 377 metodi complessivi.

`unittest` scrive normalmente il rapporto dettagliato su **stderr**: questo non equivale a un errore. I nomi e gli esiti sotto provengono dalle righe effettivamente emesse; non sono stati ricostruiti dal codice. I TXT mantengono i byte e i terminatori originali, compreso CRLF su Windows; i blocchi Markdown normalizzano soltanto i terminatori.

## Suite — quattro ambienti CI

### ubuntu-latest-python-3.12

Artifact: `output-p081-p100-ubuntu-latest-python-3.12` (ID `12476170749`). [Summary originale](../ambienti/ubuntu-latest-python-3.12.summary.json).

OS: `Linux` · piattaforma: `Linux-6.17.0-1022-azure-x86_64-with-glibc2.39` · Python: `3.12.15 (main, Oct  1 2026, 02:35:59) [GCC 13.3.0]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **26** · skipped: `0`.

**stdout** — [file TXT](streams/ubuntu-latest-python-3.12.stdout.txt)

```text
test_artificial_bounds_are_inclusive (test_p095.MonitorTests.test_artificial_bounds_are_inclusive) ... ok
test_below_or_above_range_opens_review (test_p095.MonitorTests.test_below_or_above_range_opens_review) ... ok
test_changed_close_cannot_overwrite_existing_note (test_p095.MonitorTests.test_changed_close_cannot_overwrite_existing_note) ... ok
test_close_unknown_ok_or_invalid_note_fails (test_p095.MonitorTests.test_close_unknown_ok_or_invalid_note_fails) ... ok
test_configuration_is_copied (test_p095.MonitorTests.test_configuration_is_copied) ... ok
test_conflicting_duplicate_cannot_replace_reading (test_p095.MonitorTests.test_conflicting_duplicate_cannot_replace_reading) ... ok
test_degenerate_range_accepts_only_its_single_bound (test_p095.MonitorTests.test_degenerate_range_accepts_only_its_single_bound) ... ok
test_demo_has_three_synthetic_readings_and_one_closed_request (test_p095.MonitorTests.test_demo_has_three_synthetic_readings_and_one_closed_request) ... ok
test_duplicate_reading_is_idempotent (test_p095.MonitorTests.test_duplicate_reading_is_idempotent) ... ok
test_identical_close_is_idempotent (test_p095.MonitorTests.test_identical_close_is_idempotent) ... ok
test_ingestor_and_unknown_identity_cannot_view (test_p095.MonitorTests.test_ingestor_and_unknown_identity_cannot_view) ... ok
test_inside_range_is_ok_without_pending_review (test_p095.MonitorTests.test_inside_range_is_ok_without_pending_review) ... ok
test_large_integer_boundaries_cannot_silently_lose_precision (test_p095.MonitorTests.test_large_integer_boundaries_cannot_silently_lose_precision) ... ok
test_metric_event_id_and_unit_are_validated (test_p095.MonitorTests.test_metric_event_id_and_unit_are_validated) ... ok
test_numeric_values_reject_nan_infinity_bool_and_text (test_p095.MonitorTests.test_numeric_values_reject_nan_infinity_bool_and_text) ... ok
test_range_configuration_rejects_invalid_shape_or_values (test_p095.MonitorTests.test_range_configuration_rejects_invalid_shape_or_values) ... ok
test_reading_is_immutable (test_p095.MonitorTests.test_reading_is_immutable) ... ok
test_readings_and_bounds_share_float_normalization (test_p095.MonitorTests.test_readings_and_bounds_share_float_normalization) ... ok
test_retry_ingest_after_close_does_not_reopen_request (test_p095.MonitorTests.test_retry_ingest_after_close_does_not_reopen_request) ... ok
test_returned_event_view_and_audit_do_not_mutate_storage (test_p095.MonitorTests.test_returned_event_view_and_audit_do_not_mutate_storage) ... ok
test_reviewer_closes_request_and_preserves_rule_classification (test_p095.MonitorTests.test_reviewer_closes_request_and_preserves_rule_classification) ... ok
test_roles_must_be_explicit_and_known (test_p095.MonitorTests.test_roles_must_be_explicit_and_known) ... ok
test_synthetic_patient_code_required (test_p095.MonitorTests.test_synthetic_patient_code_required) ... ok
test_timestamps_are_nonnegative_integer_simulated_seconds (test_p095.MonitorTests.test_timestamps_are_nonnegative_integer_simulated_seconds) ... ok
test_unknown_metric_and_wrong_object_do_not_enter_history (test_p095.MonitorTests.test_unknown_metric_and_wrong_object_do_not_enter_history) ... ok
test_viewer_cannot_ingest_or_close_and_denials_are_audited (test_p095.MonitorTests.test_viewer_cannot_ingest_or_close_and_denials_are_audited) ... ok

----------------------------------------------------------------------
Ran 26 tests in 0.003s

OK
```

**stderr** — [file TXT](streams/ubuntu-latest-python-3.12.stderr.txt)

Il processo non ha emesso byte su stderr. Il file collegato è vuoto (0 byte).

### ubuntu-latest-python-3.13

Artifact: `output-p081-p100-ubuntu-latest-python-3.13` (ID `12476095990`). [Summary originale](../ambienti/ubuntu-latest-python-3.13.summary.json).

OS: `Linux` · piattaforma: `Linux-6.17.0-1022-azure-x86_64-with-glibc2.39` · Python: `3.13.16 (main, Oct  1 2026, 02:37:54) [GCC 13.3.0]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **26** · skipped: `0`.

**stdout** — [file TXT](streams/ubuntu-latest-python-3.13.stdout.txt)

```text
test_artificial_bounds_are_inclusive (test_p095.MonitorTests.test_artificial_bounds_are_inclusive) ... ok
test_below_or_above_range_opens_review (test_p095.MonitorTests.test_below_or_above_range_opens_review) ... ok
test_changed_close_cannot_overwrite_existing_note (test_p095.MonitorTests.test_changed_close_cannot_overwrite_existing_note) ... ok
test_close_unknown_ok_or_invalid_note_fails (test_p095.MonitorTests.test_close_unknown_ok_or_invalid_note_fails) ... ok
test_configuration_is_copied (test_p095.MonitorTests.test_configuration_is_copied) ... ok
test_conflicting_duplicate_cannot_replace_reading (test_p095.MonitorTests.test_conflicting_duplicate_cannot_replace_reading) ... ok
test_degenerate_range_accepts_only_its_single_bound (test_p095.MonitorTests.test_degenerate_range_accepts_only_its_single_bound) ... ok
test_demo_has_three_synthetic_readings_and_one_closed_request (test_p095.MonitorTests.test_demo_has_three_synthetic_readings_and_one_closed_request) ... ok
test_duplicate_reading_is_idempotent (test_p095.MonitorTests.test_duplicate_reading_is_idempotent) ... ok
test_identical_close_is_idempotent (test_p095.MonitorTests.test_identical_close_is_idempotent) ... ok
test_ingestor_and_unknown_identity_cannot_view (test_p095.MonitorTests.test_ingestor_and_unknown_identity_cannot_view) ... ok
test_inside_range_is_ok_without_pending_review (test_p095.MonitorTests.test_inside_range_is_ok_without_pending_review) ... ok
test_large_integer_boundaries_cannot_silently_lose_precision (test_p095.MonitorTests.test_large_integer_boundaries_cannot_silently_lose_precision) ... ok
test_metric_event_id_and_unit_are_validated (test_p095.MonitorTests.test_metric_event_id_and_unit_are_validated) ... ok
test_numeric_values_reject_nan_infinity_bool_and_text (test_p095.MonitorTests.test_numeric_values_reject_nan_infinity_bool_and_text) ... ok
test_range_configuration_rejects_invalid_shape_or_values (test_p095.MonitorTests.test_range_configuration_rejects_invalid_shape_or_values) ... ok
test_reading_is_immutable (test_p095.MonitorTests.test_reading_is_immutable) ... ok
test_readings_and_bounds_share_float_normalization (test_p095.MonitorTests.test_readings_and_bounds_share_float_normalization) ... ok
test_retry_ingest_after_close_does_not_reopen_request (test_p095.MonitorTests.test_retry_ingest_after_close_does_not_reopen_request) ... ok
test_returned_event_view_and_audit_do_not_mutate_storage (test_p095.MonitorTests.test_returned_event_view_and_audit_do_not_mutate_storage) ... ok
test_reviewer_closes_request_and_preserves_rule_classification (test_p095.MonitorTests.test_reviewer_closes_request_and_preserves_rule_classification) ... ok
test_roles_must_be_explicit_and_known (test_p095.MonitorTests.test_roles_must_be_explicit_and_known) ... ok
test_synthetic_patient_code_required (test_p095.MonitorTests.test_synthetic_patient_code_required) ... ok
test_timestamps_are_nonnegative_integer_simulated_seconds (test_p095.MonitorTests.test_timestamps_are_nonnegative_integer_simulated_seconds) ... ok
test_unknown_metric_and_wrong_object_do_not_enter_history (test_p095.MonitorTests.test_unknown_metric_and_wrong_object_do_not_enter_history) ... ok
test_viewer_cannot_ingest_or_close_and_denials_are_audited (test_p095.MonitorTests.test_viewer_cannot_ingest_or_close_and_denials_are_audited) ... ok

----------------------------------------------------------------------
Ran 26 tests in 0.003s

OK
```

**stderr** — [file TXT](streams/ubuntu-latest-python-3.13.stderr.txt)

Il processo non ha emesso byte su stderr. Il file collegato è vuoto (0 byte).

### windows-latest-python-3.12

Artifact: `output-p081-p100-windows-latest-python-3.12` (ID `12475927047`). [Summary originale](../ambienti/windows-latest-python-3.12.summary.json).

OS: `Windows` · piattaforma: `Windows-2025Server-10.0.26100-SP0` · Python: `3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **26** · skipped: `0`.

**stdout** — [file TXT](streams/windows-latest-python-3.12.stdout.txt)

```text
test_artificial_bounds_are_inclusive (test_p095.MonitorTests.test_artificial_bounds_are_inclusive) ... ok
test_below_or_above_range_opens_review (test_p095.MonitorTests.test_below_or_above_range_opens_review) ... ok
test_changed_close_cannot_overwrite_existing_note (test_p095.MonitorTests.test_changed_close_cannot_overwrite_existing_note) ... ok
test_close_unknown_ok_or_invalid_note_fails (test_p095.MonitorTests.test_close_unknown_ok_or_invalid_note_fails) ... ok
test_configuration_is_copied (test_p095.MonitorTests.test_configuration_is_copied) ... ok
test_conflicting_duplicate_cannot_replace_reading (test_p095.MonitorTests.test_conflicting_duplicate_cannot_replace_reading) ... ok
test_degenerate_range_accepts_only_its_single_bound (test_p095.MonitorTests.test_degenerate_range_accepts_only_its_single_bound) ... ok
test_demo_has_three_synthetic_readings_and_one_closed_request (test_p095.MonitorTests.test_demo_has_three_synthetic_readings_and_one_closed_request) ... ok
test_duplicate_reading_is_idempotent (test_p095.MonitorTests.test_duplicate_reading_is_idempotent) ... ok
test_identical_close_is_idempotent (test_p095.MonitorTests.test_identical_close_is_idempotent) ... ok
test_ingestor_and_unknown_identity_cannot_view (test_p095.MonitorTests.test_ingestor_and_unknown_identity_cannot_view) ... ok
test_inside_range_is_ok_without_pending_review (test_p095.MonitorTests.test_inside_range_is_ok_without_pending_review) ... ok
test_large_integer_boundaries_cannot_silently_lose_precision (test_p095.MonitorTests.test_large_integer_boundaries_cannot_silently_lose_precision) ... ok
test_metric_event_id_and_unit_are_validated (test_p095.MonitorTests.test_metric_event_id_and_unit_are_validated) ... ok
test_numeric_values_reject_nan_infinity_bool_and_text (test_p095.MonitorTests.test_numeric_values_reject_nan_infinity_bool_and_text) ... ok
test_range_configuration_rejects_invalid_shape_or_values (test_p095.MonitorTests.test_range_configuration_rejects_invalid_shape_or_values) ... ok
test_reading_is_immutable (test_p095.MonitorTests.test_reading_is_immutable) ... ok
test_readings_and_bounds_share_float_normalization (test_p095.MonitorTests.test_readings_and_bounds_share_float_normalization) ... ok
test_retry_ingest_after_close_does_not_reopen_request (test_p095.MonitorTests.test_retry_ingest_after_close_does_not_reopen_request) ... ok
test_returned_event_view_and_audit_do_not_mutate_storage (test_p095.MonitorTests.test_returned_event_view_and_audit_do_not_mutate_storage) ... ok
test_reviewer_closes_request_and_preserves_rule_classification (test_p095.MonitorTests.test_reviewer_closes_request_and_preserves_rule_classification) ... ok
test_roles_must_be_explicit_and_known (test_p095.MonitorTests.test_roles_must_be_explicit_and_known) ... ok
test_synthetic_patient_code_required (test_p095.MonitorTests.test_synthetic_patient_code_required) ... ok
test_timestamps_are_nonnegative_integer_simulated_seconds (test_p095.MonitorTests.test_timestamps_are_nonnegative_integer_simulated_seconds) ... ok
test_unknown_metric_and_wrong_object_do_not_enter_history (test_p095.MonitorTests.test_unknown_metric_and_wrong_object_do_not_enter_history) ... ok
test_viewer_cannot_ingest_or_close_and_denials_are_audited (test_p095.MonitorTests.test_viewer_cannot_ingest_or_close_and_denials_are_audited) ... ok

----------------------------------------------------------------------
Ran 26 tests in 0.002s

OK
```

**stderr** — [file TXT](streams/windows-latest-python-3.12.stderr.txt)

Il processo non ha emesso byte su stderr. Il file collegato è vuoto (0 byte).

### windows-latest-python-3.13

Artifact: `output-p081-p100-windows-latest-python-3.13` (ID `12475826902`). [Summary originale](../ambienti/windows-latest-python-3.13.summary.json).

OS: `Windows` · piattaforma: `Windows-2025Server-10.0.26100-SP0` · Python: `3.13.16 (tags/v3.13.16:cbc944f, Sep 30 2026, 19:17:50) [MSC v.1944 64 bit (AMD64)]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **26** · skipped: `0`.

**stdout** — [file TXT](streams/windows-latest-python-3.13.stdout.txt)

```text
test_artificial_bounds_are_inclusive (test_p095.MonitorTests.test_artificial_bounds_are_inclusive) ... ok
test_below_or_above_range_opens_review (test_p095.MonitorTests.test_below_or_above_range_opens_review) ... ok
test_changed_close_cannot_overwrite_existing_note (test_p095.MonitorTests.test_changed_close_cannot_overwrite_existing_note) ... ok
test_close_unknown_ok_or_invalid_note_fails (test_p095.MonitorTests.test_close_unknown_ok_or_invalid_note_fails) ... ok
test_configuration_is_copied (test_p095.MonitorTests.test_configuration_is_copied) ... ok
test_conflicting_duplicate_cannot_replace_reading (test_p095.MonitorTests.test_conflicting_duplicate_cannot_replace_reading) ... ok
test_degenerate_range_accepts_only_its_single_bound (test_p095.MonitorTests.test_degenerate_range_accepts_only_its_single_bound) ... ok
test_demo_has_three_synthetic_readings_and_one_closed_request (test_p095.MonitorTests.test_demo_has_three_synthetic_readings_and_one_closed_request) ... ok
test_duplicate_reading_is_idempotent (test_p095.MonitorTests.test_duplicate_reading_is_idempotent) ... ok
test_identical_close_is_idempotent (test_p095.MonitorTests.test_identical_close_is_idempotent) ... ok
test_ingestor_and_unknown_identity_cannot_view (test_p095.MonitorTests.test_ingestor_and_unknown_identity_cannot_view) ... ok
test_inside_range_is_ok_without_pending_review (test_p095.MonitorTests.test_inside_range_is_ok_without_pending_review) ... ok
test_large_integer_boundaries_cannot_silently_lose_precision (test_p095.MonitorTests.test_large_integer_boundaries_cannot_silently_lose_precision) ... ok
test_metric_event_id_and_unit_are_validated (test_p095.MonitorTests.test_metric_event_id_and_unit_are_validated) ... ok
test_numeric_values_reject_nan_infinity_bool_and_text (test_p095.MonitorTests.test_numeric_values_reject_nan_infinity_bool_and_text) ... ok
test_range_configuration_rejects_invalid_shape_or_values (test_p095.MonitorTests.test_range_configuration_rejects_invalid_shape_or_values) ... ok
test_reading_is_immutable (test_p095.MonitorTests.test_reading_is_immutable) ... ok
test_readings_and_bounds_share_float_normalization (test_p095.MonitorTests.test_readings_and_bounds_share_float_normalization) ... ok
test_retry_ingest_after_close_does_not_reopen_request (test_p095.MonitorTests.test_retry_ingest_after_close_does_not_reopen_request) ... ok
test_returned_event_view_and_audit_do_not_mutate_storage (test_p095.MonitorTests.test_returned_event_view_and_audit_do_not_mutate_storage) ... ok
test_reviewer_closes_request_and_preserves_rule_classification (test_p095.MonitorTests.test_reviewer_closes_request_and_preserves_rule_classification) ... ok
test_roles_must_be_explicit_and_known (test_p095.MonitorTests.test_roles_must_be_explicit_and_known) ... ok
test_synthetic_patient_code_required (test_p095.MonitorTests.test_synthetic_patient_code_required) ... ok
test_timestamps_are_nonnegative_integer_simulated_seconds (test_p095.MonitorTests.test_timestamps_are_nonnegative_integer_simulated_seconds) ... ok
test_unknown_metric_and_wrong_object_do_not_enter_history (test_p095.MonitorTests.test_unknown_metric_and_wrong_object_do_not_enter_history) ... ok
test_viewer_cannot_ingest_or_close_and_denials_are_audited (test_p095.MonitorTests.test_viewer_cannot_ingest_or_close_and_denials_are_audited) ... ok

----------------------------------------------------------------------
Ran 26 tests in 0.002s

OK
```

**stderr** — [file TXT](streams/windows-latest-python-3.13.stderr.txt)

Il processo non ha emesso byte su stderr. Il file collegato è vuoto (0 byte).

## Demo e controlli runtime

Questa matrice esegue le suite `run_tests.py`. Le summary non classificano processi separati come demo o controlli runtime: non sono aggiunti output o esiti di tali categorie.

## Verifica e provenienza

[Registro strutturato](registro.json) · [Hash e trasformazioni](MANIFEST.json) · [Policy](../AUDIT.md) · [Indice](../README.md)
