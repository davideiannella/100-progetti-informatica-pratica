# P100: output dei collaudi

[Indice dei collaudi](../README.md) · [Codice e istruzioni](../../projects/P100/README.md)

Esito registrato: **PASS in tutte le quattro combinazioni**. [Run 39893701054](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39893701054) · commit `3ab7bdfedb20a443bd71fe4e4ffe3c1dd67bd707`.

Comando effettivo del [runner a quel commit](https://github.com/davideiannella/100-progetti-informatica-pratica/blob/3ab7bdfedb20a443bd71fe4e4ffe3c1dd67bd707/tools/collaudo_p081_p100.py): `[sys.executable, "-B", "run_tests.py"]`, con directory di lavoro `projects/P100`. `sys.executable` indica l’interprete della combinazione riportata sotto; il suo percorso host assoluto non è registrato nella summary.

I quattro rapporti sono output CI preesistenti, non nuove esecuzioni preparate per questa pagina. Ogni ambiente ha verificato gli hash dei 299 sorgenti, compilato 60 file Python e completato 20 suite per 377 metodi complessivi.

`unittest` scrive normalmente il rapporto dettagliato su **stderr**: questo non equivale a un errore. I nomi e gli esiti sotto provengono dalle righe effettivamente emesse; non sono stati ricostruiti dal codice. I TXT mantengono i byte e i terminatori originali, compreso CRLF su Windows; i blocchi Markdown normalizzano soltanto i terminatori.

## Suite — quattro ambienti CI

### ubuntu-latest-python-3.12

Artifact: `output-p081-p100-ubuntu-latest-python-3.12` (ID `12476170749`). [Summary originale](../ambienti/ubuntu-latest-python-3.12.summary.json).

OS: `Linux` · piattaforma: `Linux-6.17.0-1022-azure-x86_64-with-glibc2.39` · Python: `3.12.15 (main, Oct  1 2026, 02:35:59) [GCC 13.3.0]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **24** · skipped: `0`.

**stdout** — [file TXT](streams/ubuntu-latest-python-3.12.stdout.txt)

```text
test_methods=24; executed=24; failures=0; errors=0
```

**stderr** — [file TXT](streams/ubuntu-latest-python-3.12.stderr.txt)

```text
test_canonical_json_has_stable_key_order_and_rejects_non_json (test_smart_waste_platform.SmartWastePlatformTests.test_canonical_json_has_stable_key_order_and_rejects_non_json) ... ok
test_confidence_boundaries_and_boolean_rejection (test_smart_waste_platform.SmartWastePlatformTests.test_confidence_boundaries_and_boolean_rejection) ... ok
test_demo_numbers (test_smart_waste_platform.SmartWastePlatformTests.test_demo_numbers) ... ok
test_duplicate_conflicting_content_rejected (test_smart_waste_platform.SmartWastePlatformTests.test_duplicate_conflicting_content_rejected) ... ok
test_event_ids_are_scoped_to_device (test_smart_waste_platform.SmartWastePlatformTests.test_event_ids_are_scoped_to_device) ... ok
test_file_database_survives_close_and_keeps_dedup (test_smart_waste_platform.SmartWastePlatformTests.test_file_database_survives_close_and_keeps_dedup) ... ok
test_fill_boundaries_alert_is_greater_or_equal_80 (test_smart_waste_platform.SmartWastePlatformTests.test_fill_boundaries_alert_is_greater_or_equal_80) ... ok
test_helper_does_not_invent_model_results (test_smart_waste_platform.SmartWastePlatformTests.test_helper_does_not_invent_model_results) ... ok
test_helper_rejects_explicit_empty_or_boolean_timestamp (test_smart_waste_platform.SmartWastePlatformTests.test_helper_rejects_explicit_empty_or_boolean_timestamp) ... ok
test_identical_retry_does_not_duplicate_event_or_alert (test_smart_waste_platform.SmartWastePlatformTests.test_identical_retry_does_not_duplicate_event_or_alert) ... ok
test_invalid_event_ids_and_sql_injection_are_rejected (test_smart_waste_platform.SmartWastePlatformTests.test_invalid_event_ids_and_sql_injection_are_rejected) ... ok
test_malformed_mac_rejected_without_comparison_crash (test_smart_waste_platform.SmartWastePlatformTests.test_malformed_mac_rejected_without_comparison_crash) ... ok
test_memory_databases_do_not_persist (test_smart_waste_platform.SmartWastePlatformTests.test_memory_databases_do_not_persist) ... ok
test_nonfinite_numbers_rejected_before_any_write (test_smart_waste_platform.SmartWastePlatformTests.test_nonfinite_numbers_rejected_before_any_write) ... ok
test_payload_mutation_after_ingestion_cannot_change_database (test_smart_waste_platform.SmartWastePlatformTests.test_payload_mutation_after_ingestion_cannot_change_database) ... ok
test_random_secret_and_repr_do_not_expose_it (test_smart_waste_platform.SmartWastePlatformTests.test_random_secret_and_repr_do_not_expose_it) ... ok
test_registry_rejects_bad_ids_duplicates_and_short_secrets (test_smart_waste_platform.SmartWastePlatformTests.test_registry_rejects_bad_ids_duplicates_and_short_secrets) ... ok
test_schema_exact_no_images_or_unknown_event_types (test_smart_waste_platform.SmartWastePlatformTests.test_schema_exact_no_images_or_unknown_event_types) ... ok
test_sql_errors_are_not_silently_treated_as_duplicates (test_smart_waste_platform.SmartWastePlatformTests.test_sql_errors_are_not_silently_treated_as_duplicates) ... ok
test_tampered_payload_and_wrong_secret_rejected (test_smart_waste_platform.SmartWastePlatformTests.test_tampered_payload_and_wrong_secret_rejected) ... ok
test_timestamp_must_be_parseable_and_timezone_aware (test_smart_waste_platform.SmartWastePlatformTests.test_timestamp_must_be_parseable_and_timezone_aware) ... ok
test_transaction_rolls_back_event_if_alert_creation_fails (test_smart_waste_platform.SmartWastePlatformTests.test_transaction_rolls_back_event_if_alert_creation_fails) ... ok
test_unknown_device_rejected (test_smart_waste_platform.SmartWastePlatformTests.test_unknown_device_rejected) ... ok
test_valid_event_and_class_counts (test_smart_waste_platform.SmartWastePlatformTests.test_valid_event_and_class_counts) ... ok

----------------------------------------------------------------------
Ran 24 tests in 0.021s

OK
```

### ubuntu-latest-python-3.13

Artifact: `output-p081-p100-ubuntu-latest-python-3.13` (ID `12476095990`). [Summary originale](../ambienti/ubuntu-latest-python-3.13.summary.json).

OS: `Linux` · piattaforma: `Linux-6.17.0-1022-azure-x86_64-with-glibc2.39` · Python: `3.13.16 (main, Oct  1 2026, 02:37:54) [GCC 13.3.0]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **24** · skipped: `0`.

**stdout** — [file TXT](streams/ubuntu-latest-python-3.13.stdout.txt)

```text
test_methods=24; executed=24; failures=0; errors=0
```

**stderr** — [file TXT](streams/ubuntu-latest-python-3.13.stderr.txt)

```text
test_canonical_json_has_stable_key_order_and_rejects_non_json (test_smart_waste_platform.SmartWastePlatformTests.test_canonical_json_has_stable_key_order_and_rejects_non_json) ... ok
test_confidence_boundaries_and_boolean_rejection (test_smart_waste_platform.SmartWastePlatformTests.test_confidence_boundaries_and_boolean_rejection) ... ok
test_demo_numbers (test_smart_waste_platform.SmartWastePlatformTests.test_demo_numbers) ... ok
test_duplicate_conflicting_content_rejected (test_smart_waste_platform.SmartWastePlatformTests.test_duplicate_conflicting_content_rejected) ... ok
test_event_ids_are_scoped_to_device (test_smart_waste_platform.SmartWastePlatformTests.test_event_ids_are_scoped_to_device) ... ok
test_file_database_survives_close_and_keeps_dedup (test_smart_waste_platform.SmartWastePlatformTests.test_file_database_survives_close_and_keeps_dedup) ... ok
test_fill_boundaries_alert_is_greater_or_equal_80 (test_smart_waste_platform.SmartWastePlatformTests.test_fill_boundaries_alert_is_greater_or_equal_80) ... ok
test_helper_does_not_invent_model_results (test_smart_waste_platform.SmartWastePlatformTests.test_helper_does_not_invent_model_results) ... ok
test_helper_rejects_explicit_empty_or_boolean_timestamp (test_smart_waste_platform.SmartWastePlatformTests.test_helper_rejects_explicit_empty_or_boolean_timestamp) ... ok
test_identical_retry_does_not_duplicate_event_or_alert (test_smart_waste_platform.SmartWastePlatformTests.test_identical_retry_does_not_duplicate_event_or_alert) ... ok
test_invalid_event_ids_and_sql_injection_are_rejected (test_smart_waste_platform.SmartWastePlatformTests.test_invalid_event_ids_and_sql_injection_are_rejected) ... ok
test_malformed_mac_rejected_without_comparison_crash (test_smart_waste_platform.SmartWastePlatformTests.test_malformed_mac_rejected_without_comparison_crash) ... ok
test_memory_databases_do_not_persist (test_smart_waste_platform.SmartWastePlatformTests.test_memory_databases_do_not_persist) ... ok
test_nonfinite_numbers_rejected_before_any_write (test_smart_waste_platform.SmartWastePlatformTests.test_nonfinite_numbers_rejected_before_any_write) ... ok
test_payload_mutation_after_ingestion_cannot_change_database (test_smart_waste_platform.SmartWastePlatformTests.test_payload_mutation_after_ingestion_cannot_change_database) ... ok
test_random_secret_and_repr_do_not_expose_it (test_smart_waste_platform.SmartWastePlatformTests.test_random_secret_and_repr_do_not_expose_it) ... ok
test_registry_rejects_bad_ids_duplicates_and_short_secrets (test_smart_waste_platform.SmartWastePlatformTests.test_registry_rejects_bad_ids_duplicates_and_short_secrets) ... ok
test_schema_exact_no_images_or_unknown_event_types (test_smart_waste_platform.SmartWastePlatformTests.test_schema_exact_no_images_or_unknown_event_types) ... ok
test_sql_errors_are_not_silently_treated_as_duplicates (test_smart_waste_platform.SmartWastePlatformTests.test_sql_errors_are_not_silently_treated_as_duplicates) ... ok
test_tampered_payload_and_wrong_secret_rejected (test_smart_waste_platform.SmartWastePlatformTests.test_tampered_payload_and_wrong_secret_rejected) ... ok
test_timestamp_must_be_parseable_and_timezone_aware (test_smart_waste_platform.SmartWastePlatformTests.test_timestamp_must_be_parseable_and_timezone_aware) ... ok
test_transaction_rolls_back_event_if_alert_creation_fails (test_smart_waste_platform.SmartWastePlatformTests.test_transaction_rolls_back_event_if_alert_creation_fails) ... ok
test_unknown_device_rejected (test_smart_waste_platform.SmartWastePlatformTests.test_unknown_device_rejected) ... ok
test_valid_event_and_class_counts (test_smart_waste_platform.SmartWastePlatformTests.test_valid_event_and_class_counts) ... ok

----------------------------------------------------------------------
Ran 24 tests in 0.022s

OK
```

### windows-latest-python-3.12

Artifact: `output-p081-p100-windows-latest-python-3.12` (ID `12475927047`). [Summary originale](../ambienti/windows-latest-python-3.12.summary.json).

OS: `Windows` · piattaforma: `Windows-2025Server-10.0.26100-SP0` · Python: `3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **24** · skipped: `0`.

**stdout** — [file TXT](streams/windows-latest-python-3.12.stdout.txt)

```text
test_methods=24; executed=24; failures=0; errors=0
```

**stderr** — [file TXT](streams/windows-latest-python-3.12.stderr.txt)

```text
test_canonical_json_has_stable_key_order_and_rejects_non_json (test_smart_waste_platform.SmartWastePlatformTests.test_canonical_json_has_stable_key_order_and_rejects_non_json) ... ok
test_confidence_boundaries_and_boolean_rejection (test_smart_waste_platform.SmartWastePlatformTests.test_confidence_boundaries_and_boolean_rejection) ... ok
test_demo_numbers (test_smart_waste_platform.SmartWastePlatformTests.test_demo_numbers) ... ok
test_duplicate_conflicting_content_rejected (test_smart_waste_platform.SmartWastePlatformTests.test_duplicate_conflicting_content_rejected) ... ok
test_event_ids_are_scoped_to_device (test_smart_waste_platform.SmartWastePlatformTests.test_event_ids_are_scoped_to_device) ... ok
test_file_database_survives_close_and_keeps_dedup (test_smart_waste_platform.SmartWastePlatformTests.test_file_database_survives_close_and_keeps_dedup) ... ok
test_fill_boundaries_alert_is_greater_or_equal_80 (test_smart_waste_platform.SmartWastePlatformTests.test_fill_boundaries_alert_is_greater_or_equal_80) ... ok
test_helper_does_not_invent_model_results (test_smart_waste_platform.SmartWastePlatformTests.test_helper_does_not_invent_model_results) ... ok
test_helper_rejects_explicit_empty_or_boolean_timestamp (test_smart_waste_platform.SmartWastePlatformTests.test_helper_rejects_explicit_empty_or_boolean_timestamp) ... ok
test_identical_retry_does_not_duplicate_event_or_alert (test_smart_waste_platform.SmartWastePlatformTests.test_identical_retry_does_not_duplicate_event_or_alert) ... ok
test_invalid_event_ids_and_sql_injection_are_rejected (test_smart_waste_platform.SmartWastePlatformTests.test_invalid_event_ids_and_sql_injection_are_rejected) ... ok
test_malformed_mac_rejected_without_comparison_crash (test_smart_waste_platform.SmartWastePlatformTests.test_malformed_mac_rejected_without_comparison_crash) ... ok
test_memory_databases_do_not_persist (test_smart_waste_platform.SmartWastePlatformTests.test_memory_databases_do_not_persist) ... ok
test_nonfinite_numbers_rejected_before_any_write (test_smart_waste_platform.SmartWastePlatformTests.test_nonfinite_numbers_rejected_before_any_write) ... ok
test_payload_mutation_after_ingestion_cannot_change_database (test_smart_waste_platform.SmartWastePlatformTests.test_payload_mutation_after_ingestion_cannot_change_database) ... ok
test_random_secret_and_repr_do_not_expose_it (test_smart_waste_platform.SmartWastePlatformTests.test_random_secret_and_repr_do_not_expose_it) ... ok
test_registry_rejects_bad_ids_duplicates_and_short_secrets (test_smart_waste_platform.SmartWastePlatformTests.test_registry_rejects_bad_ids_duplicates_and_short_secrets) ... ok
test_schema_exact_no_images_or_unknown_event_types (test_smart_waste_platform.SmartWastePlatformTests.test_schema_exact_no_images_or_unknown_event_types) ... ok
test_sql_errors_are_not_silently_treated_as_duplicates (test_smart_waste_platform.SmartWastePlatformTests.test_sql_errors_are_not_silently_treated_as_duplicates) ... ok
test_tampered_payload_and_wrong_secret_rejected (test_smart_waste_platform.SmartWastePlatformTests.test_tampered_payload_and_wrong_secret_rejected) ... ok
test_timestamp_must_be_parseable_and_timezone_aware (test_smart_waste_platform.SmartWastePlatformTests.test_timestamp_must_be_parseable_and_timezone_aware) ... ok
test_transaction_rolls_back_event_if_alert_creation_fails (test_smart_waste_platform.SmartWastePlatformTests.test_transaction_rolls_back_event_if_alert_creation_fails) ... ok
test_unknown_device_rejected (test_smart_waste_platform.SmartWastePlatformTests.test_unknown_device_rejected) ... ok
test_valid_event_and_class_counts (test_smart_waste_platform.SmartWastePlatformTests.test_valid_event_and_class_counts) ... ok

----------------------------------------------------------------------
Ran 24 tests in 0.125s

OK
```

### windows-latest-python-3.13

Artifact: `output-p081-p100-windows-latest-python-3.13` (ID `12475826902`). [Summary originale](../ambienti/windows-latest-python-3.13.summary.json).

OS: `Windows` · piattaforma: `Windows-2025Server-10.0.26100-SP0` · Python: `3.13.16 (tags/v3.13.16:cbc944f, Sep 30 2026, 19:17:50) [MSC v.1944 64 bit (AMD64)]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **24** · skipped: `0`.

**stdout** — [file TXT](streams/windows-latest-python-3.13.stdout.txt)

```text
test_methods=24; executed=24; failures=0; errors=0
```

**stderr** — [file TXT](streams/windows-latest-python-3.13.stderr.txt)

```text
test_canonical_json_has_stable_key_order_and_rejects_non_json (test_smart_waste_platform.SmartWastePlatformTests.test_canonical_json_has_stable_key_order_and_rejects_non_json) ... ok
test_confidence_boundaries_and_boolean_rejection (test_smart_waste_platform.SmartWastePlatformTests.test_confidence_boundaries_and_boolean_rejection) ... ok
test_demo_numbers (test_smart_waste_platform.SmartWastePlatformTests.test_demo_numbers) ... ok
test_duplicate_conflicting_content_rejected (test_smart_waste_platform.SmartWastePlatformTests.test_duplicate_conflicting_content_rejected) ... ok
test_event_ids_are_scoped_to_device (test_smart_waste_platform.SmartWastePlatformTests.test_event_ids_are_scoped_to_device) ... ok
test_file_database_survives_close_and_keeps_dedup (test_smart_waste_platform.SmartWastePlatformTests.test_file_database_survives_close_and_keeps_dedup) ... ok
test_fill_boundaries_alert_is_greater_or_equal_80 (test_smart_waste_platform.SmartWastePlatformTests.test_fill_boundaries_alert_is_greater_or_equal_80) ... ok
test_helper_does_not_invent_model_results (test_smart_waste_platform.SmartWastePlatformTests.test_helper_does_not_invent_model_results) ... ok
test_helper_rejects_explicit_empty_or_boolean_timestamp (test_smart_waste_platform.SmartWastePlatformTests.test_helper_rejects_explicit_empty_or_boolean_timestamp) ... ok
test_identical_retry_does_not_duplicate_event_or_alert (test_smart_waste_platform.SmartWastePlatformTests.test_identical_retry_does_not_duplicate_event_or_alert) ... ok
test_invalid_event_ids_and_sql_injection_are_rejected (test_smart_waste_platform.SmartWastePlatformTests.test_invalid_event_ids_and_sql_injection_are_rejected) ... ok
test_malformed_mac_rejected_without_comparison_crash (test_smart_waste_platform.SmartWastePlatformTests.test_malformed_mac_rejected_without_comparison_crash) ... ok
test_memory_databases_do_not_persist (test_smart_waste_platform.SmartWastePlatformTests.test_memory_databases_do_not_persist) ... ok
test_nonfinite_numbers_rejected_before_any_write (test_smart_waste_platform.SmartWastePlatformTests.test_nonfinite_numbers_rejected_before_any_write) ... ok
test_payload_mutation_after_ingestion_cannot_change_database (test_smart_waste_platform.SmartWastePlatformTests.test_payload_mutation_after_ingestion_cannot_change_database) ... ok
test_random_secret_and_repr_do_not_expose_it (test_smart_waste_platform.SmartWastePlatformTests.test_random_secret_and_repr_do_not_expose_it) ... ok
test_registry_rejects_bad_ids_duplicates_and_short_secrets (test_smart_waste_platform.SmartWastePlatformTests.test_registry_rejects_bad_ids_duplicates_and_short_secrets) ... ok
test_schema_exact_no_images_or_unknown_event_types (test_smart_waste_platform.SmartWastePlatformTests.test_schema_exact_no_images_or_unknown_event_types) ... ok
test_sql_errors_are_not_silently_treated_as_duplicates (test_smart_waste_platform.SmartWastePlatformTests.test_sql_errors_are_not_silently_treated_as_duplicates) ... ok
test_tampered_payload_and_wrong_secret_rejected (test_smart_waste_platform.SmartWastePlatformTests.test_tampered_payload_and_wrong_secret_rejected) ... ok
test_timestamp_must_be_parseable_and_timezone_aware (test_smart_waste_platform.SmartWastePlatformTests.test_timestamp_must_be_parseable_and_timezone_aware) ... ok
test_transaction_rolls_back_event_if_alert_creation_fails (test_smart_waste_platform.SmartWastePlatformTests.test_transaction_rolls_back_event_if_alert_creation_fails) ... ok
test_unknown_device_rejected (test_smart_waste_platform.SmartWastePlatformTests.test_unknown_device_rejected) ... ok
test_valid_event_and_class_counts (test_smart_waste_platform.SmartWastePlatformTests.test_valid_event_and_class_counts) ... ok

----------------------------------------------------------------------
Ran 24 tests in 0.231s

OK
```

## Demo e controlli runtime

Questa matrice esegue le suite `run_tests.py`. Le summary non classificano processi separati come demo o controlli runtime: non sono aggiunti output o esiti di tali categorie.

## Verifica e provenienza

[Registro strutturato](registro.json) · [Hash e trasformazioni](MANIFEST.json) · [Policy](../AUDIT.md) · [Indice](../README.md)
