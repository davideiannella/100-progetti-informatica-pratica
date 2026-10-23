# P083 — output reali dei collaudi

Esito registrato: **PASS in tutte le quattro combinazioni**. [Run 39893701054](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39893701054) · commit `3ab7bdfedb20a443bd71fe4e4ffe3c1dd67bd707`.

Comando effettivo del [runner a quel commit](https://github.com/davideiannella/100-progetti-informatica-pratica/blob/3ab7bdfedb20a443bd71fe4e4ffe3c1dd67bd707/tools/collaudo_p081_p100.py): `[sys.executable, "-B", "run_tests.py"]`, con directory di lavoro `projects/P083`. `sys.executable` indica l’interprete della combinazione riportata sotto; il suo percorso host assoluto non è registrato nella summary.

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
test_bad_clock_does_not_advance_sequence_or_rng (test_iot_simulator.IoTSimulatorTest.test_bad_clock_does_not_advance_sequence_or_rng) ... ok
test_bad_numbers_and_booleans_are_rejected (test_iot_simulator.IoTSimulatorTest.test_bad_numbers_and_booleans_are_rejected) ... ok
test_broker_rejects_bad_topic_callback_and_duplicate_subscription (test_iot_simulator.IoTSimulatorTest.test_broker_rejects_bad_topic_callback_and_duplicate_subscription) ... ok
test_conflicting_duplicate_is_rejected_without_rounding_away_difference (test_iot_simulator.IoTSimulatorTest.test_conflicting_duplicate_is_rejected_without_rounding_away_difference) ... ok
test_demo_is_three_ordered_events_and_no_persistent_transport (test_iot_simulator.IoTSimulatorTest.test_demo_is_three_ordered_events_and_no_persistent_transport) ... ok
test_device_and_sensor_configuration_are_validated (test_iot_simulator.IoTSimulatorTest.test_device_and_sensor_configuration_are_validated) ... ok
test_devices_have_independent_sequences (test_iot_simulator.IoTSimulatorTest.test_devices_have_independent_sequences) ... ok
test_failed_flush_keeps_unsent_head (test_iot_simulator.IoTSimulatorTest.test_failed_flush_keeps_unsent_head) ... ok
test_identical_retry_is_acknowledged_without_duplicate (test_iot_simulator.IoTSimulatorTest.test_identical_retry_is_acknowledged_without_duplicate) ... ok
test_malformed_json_duplicate_keys_and_wrong_root_are_rejected (test_iot_simulator.IoTSimulatorTest.test_malformed_json_duplicate_keys_and_wrong_root_are_rejected) ... ok
test_numeric_envelope_includes_boundaries (test_iot_simulator.IoTSimulatorTest.test_numeric_envelope_includes_boundaries) ... ok
test_offline_buffers_without_delivery (test_iot_simulator.IoTSimulatorTest.test_offline_buffers_without_delivery) ... ok
test_partial_callback_failure_can_retry_without_duplicate_at_collector (test_iot_simulator.IoTSimulatorTest.test_partial_callback_failure_can_retry_without_duplicate_at_collector) ... ok
test_publish_delivers_valid_schema (test_iot_simulator.IoTSimulatorTest.test_publish_delivers_valid_schema) ... ok
test_reconnection_delivers_old_events_before_new_sample (test_iot_simulator.IoTSimulatorTest.test_reconnection_delivers_old_events_before_new_sample) ... ok
test_returned_messages_cannot_corrupt_history_or_deduplication (test_iot_simulator.IoTSimulatorTest.test_returned_messages_cannot_corrupt_history_or_deduplication) ... ok
test_schema_and_fields_are_exact (test_iot_simulator.IoTSimulatorTest.test_schema_and_fields_are_exact) ... ok
test_seed_and_clock_are_reproducible (test_iot_simulator.IoTSimulatorTest.test_seed_and_clock_are_reproducible) ... ok
test_sequence_requires_nonnegative_integer (test_iot_simulator.IoTSimulatorTest.test_sequence_requires_nonnegative_integer) ... ok
test_timestamp_requires_explicit_utc (test_iot_simulator.IoTSimulatorTest.test_timestamp_requires_explicit_utc) ... ok
test_topic_and_payload_device_must_match (test_iot_simulator.IoTSimulatorTest.test_topic_and_payload_device_must_match) ... ok
test_unseen_out_of_order_is_rejected_but_old_retry_is_allowed (test_iot_simulator.IoTSimulatorTest.test_unseen_out_of_order_is_rejected_but_old_retry_is_allowed) ... ok

----------------------------------------------------------------------
Ran 22 tests in 0.005s

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
test_bad_clock_does_not_advance_sequence_or_rng (test_iot_simulator.IoTSimulatorTest.test_bad_clock_does_not_advance_sequence_or_rng) ... ok
test_bad_numbers_and_booleans_are_rejected (test_iot_simulator.IoTSimulatorTest.test_bad_numbers_and_booleans_are_rejected) ... ok
test_broker_rejects_bad_topic_callback_and_duplicate_subscription (test_iot_simulator.IoTSimulatorTest.test_broker_rejects_bad_topic_callback_and_duplicate_subscription) ... ok
test_conflicting_duplicate_is_rejected_without_rounding_away_difference (test_iot_simulator.IoTSimulatorTest.test_conflicting_duplicate_is_rejected_without_rounding_away_difference) ... ok
test_demo_is_three_ordered_events_and_no_persistent_transport (test_iot_simulator.IoTSimulatorTest.test_demo_is_three_ordered_events_and_no_persistent_transport) ... ok
test_device_and_sensor_configuration_are_validated (test_iot_simulator.IoTSimulatorTest.test_device_and_sensor_configuration_are_validated) ... ok
test_devices_have_independent_sequences (test_iot_simulator.IoTSimulatorTest.test_devices_have_independent_sequences) ... ok
test_failed_flush_keeps_unsent_head (test_iot_simulator.IoTSimulatorTest.test_failed_flush_keeps_unsent_head) ... ok
test_identical_retry_is_acknowledged_without_duplicate (test_iot_simulator.IoTSimulatorTest.test_identical_retry_is_acknowledged_without_duplicate) ... ok
test_malformed_json_duplicate_keys_and_wrong_root_are_rejected (test_iot_simulator.IoTSimulatorTest.test_malformed_json_duplicate_keys_and_wrong_root_are_rejected) ... ok
test_numeric_envelope_includes_boundaries (test_iot_simulator.IoTSimulatorTest.test_numeric_envelope_includes_boundaries) ... ok
test_offline_buffers_without_delivery (test_iot_simulator.IoTSimulatorTest.test_offline_buffers_without_delivery) ... ok
test_partial_callback_failure_can_retry_without_duplicate_at_collector (test_iot_simulator.IoTSimulatorTest.test_partial_callback_failure_can_retry_without_duplicate_at_collector) ... ok
test_publish_delivers_valid_schema (test_iot_simulator.IoTSimulatorTest.test_publish_delivers_valid_schema) ... ok
test_reconnection_delivers_old_events_before_new_sample (test_iot_simulator.IoTSimulatorTest.test_reconnection_delivers_old_events_before_new_sample) ... ok
test_returned_messages_cannot_corrupt_history_or_deduplication (test_iot_simulator.IoTSimulatorTest.test_returned_messages_cannot_corrupt_history_or_deduplication) ... ok
test_schema_and_fields_are_exact (test_iot_simulator.IoTSimulatorTest.test_schema_and_fields_are_exact) ... ok
test_seed_and_clock_are_reproducible (test_iot_simulator.IoTSimulatorTest.test_seed_and_clock_are_reproducible) ... ok
test_sequence_requires_nonnegative_integer (test_iot_simulator.IoTSimulatorTest.test_sequence_requires_nonnegative_integer) ... ok
test_timestamp_requires_explicit_utc (test_iot_simulator.IoTSimulatorTest.test_timestamp_requires_explicit_utc) ... ok
test_topic_and_payload_device_must_match (test_iot_simulator.IoTSimulatorTest.test_topic_and_payload_device_must_match) ... ok
test_unseen_out_of_order_is_rejected_but_old_retry_is_allowed (test_iot_simulator.IoTSimulatorTest.test_unseen_out_of_order_is_rejected_but_old_retry_is_allowed) ... ok

----------------------------------------------------------------------
Ran 22 tests in 0.005s

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
test_bad_clock_does_not_advance_sequence_or_rng (test_iot_simulator.IoTSimulatorTest.test_bad_clock_does_not_advance_sequence_or_rng) ... ok
test_bad_numbers_and_booleans_are_rejected (test_iot_simulator.IoTSimulatorTest.test_bad_numbers_and_booleans_are_rejected) ... ok
test_broker_rejects_bad_topic_callback_and_duplicate_subscription (test_iot_simulator.IoTSimulatorTest.test_broker_rejects_bad_topic_callback_and_duplicate_subscription) ... ok
test_conflicting_duplicate_is_rejected_without_rounding_away_difference (test_iot_simulator.IoTSimulatorTest.test_conflicting_duplicate_is_rejected_without_rounding_away_difference) ... ok
test_demo_is_three_ordered_events_and_no_persistent_transport (test_iot_simulator.IoTSimulatorTest.test_demo_is_three_ordered_events_and_no_persistent_transport) ... ok
test_device_and_sensor_configuration_are_validated (test_iot_simulator.IoTSimulatorTest.test_device_and_sensor_configuration_are_validated) ... ok
test_devices_have_independent_sequences (test_iot_simulator.IoTSimulatorTest.test_devices_have_independent_sequences) ... ok
test_failed_flush_keeps_unsent_head (test_iot_simulator.IoTSimulatorTest.test_failed_flush_keeps_unsent_head) ... ok
test_identical_retry_is_acknowledged_without_duplicate (test_iot_simulator.IoTSimulatorTest.test_identical_retry_is_acknowledged_without_duplicate) ... ok
test_malformed_json_duplicate_keys_and_wrong_root_are_rejected (test_iot_simulator.IoTSimulatorTest.test_malformed_json_duplicate_keys_and_wrong_root_are_rejected) ... ok
test_numeric_envelope_includes_boundaries (test_iot_simulator.IoTSimulatorTest.test_numeric_envelope_includes_boundaries) ... ok
test_offline_buffers_without_delivery (test_iot_simulator.IoTSimulatorTest.test_offline_buffers_without_delivery) ... ok
test_partial_callback_failure_can_retry_without_duplicate_at_collector (test_iot_simulator.IoTSimulatorTest.test_partial_callback_failure_can_retry_without_duplicate_at_collector) ... ok
test_publish_delivers_valid_schema (test_iot_simulator.IoTSimulatorTest.test_publish_delivers_valid_schema) ... ok
test_reconnection_delivers_old_events_before_new_sample (test_iot_simulator.IoTSimulatorTest.test_reconnection_delivers_old_events_before_new_sample) ... ok
test_returned_messages_cannot_corrupt_history_or_deduplication (test_iot_simulator.IoTSimulatorTest.test_returned_messages_cannot_corrupt_history_or_deduplication) ... ok
test_schema_and_fields_are_exact (test_iot_simulator.IoTSimulatorTest.test_schema_and_fields_are_exact) ... ok
test_seed_and_clock_are_reproducible (test_iot_simulator.IoTSimulatorTest.test_seed_and_clock_are_reproducible) ... ok
test_sequence_requires_nonnegative_integer (test_iot_simulator.IoTSimulatorTest.test_sequence_requires_nonnegative_integer) ... ok
test_timestamp_requires_explicit_utc (test_iot_simulator.IoTSimulatorTest.test_timestamp_requires_explicit_utc) ... ok
test_topic_and_payload_device_must_match (test_iot_simulator.IoTSimulatorTest.test_topic_and_payload_device_must_match) ... ok
test_unseen_out_of_order_is_rejected_but_old_retry_is_allowed (test_iot_simulator.IoTSimulatorTest.test_unseen_out_of_order_is_rejected_but_old_retry_is_allowed) ... ok

----------------------------------------------------------------------
Ran 22 tests in 0.004s

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
test_bad_clock_does_not_advance_sequence_or_rng (test_iot_simulator.IoTSimulatorTest.test_bad_clock_does_not_advance_sequence_or_rng) ... ok
test_bad_numbers_and_booleans_are_rejected (test_iot_simulator.IoTSimulatorTest.test_bad_numbers_and_booleans_are_rejected) ... ok
test_broker_rejects_bad_topic_callback_and_duplicate_subscription (test_iot_simulator.IoTSimulatorTest.test_broker_rejects_bad_topic_callback_and_duplicate_subscription) ... ok
test_conflicting_duplicate_is_rejected_without_rounding_away_difference (test_iot_simulator.IoTSimulatorTest.test_conflicting_duplicate_is_rejected_without_rounding_away_difference) ... ok
test_demo_is_three_ordered_events_and_no_persistent_transport (test_iot_simulator.IoTSimulatorTest.test_demo_is_three_ordered_events_and_no_persistent_transport) ... ok
test_device_and_sensor_configuration_are_validated (test_iot_simulator.IoTSimulatorTest.test_device_and_sensor_configuration_are_validated) ... ok
test_devices_have_independent_sequences (test_iot_simulator.IoTSimulatorTest.test_devices_have_independent_sequences) ... ok
test_failed_flush_keeps_unsent_head (test_iot_simulator.IoTSimulatorTest.test_failed_flush_keeps_unsent_head) ... ok
test_identical_retry_is_acknowledged_without_duplicate (test_iot_simulator.IoTSimulatorTest.test_identical_retry_is_acknowledged_without_duplicate) ... ok
test_malformed_json_duplicate_keys_and_wrong_root_are_rejected (test_iot_simulator.IoTSimulatorTest.test_malformed_json_duplicate_keys_and_wrong_root_are_rejected) ... ok
test_numeric_envelope_includes_boundaries (test_iot_simulator.IoTSimulatorTest.test_numeric_envelope_includes_boundaries) ... ok
test_offline_buffers_without_delivery (test_iot_simulator.IoTSimulatorTest.test_offline_buffers_without_delivery) ... ok
test_partial_callback_failure_can_retry_without_duplicate_at_collector (test_iot_simulator.IoTSimulatorTest.test_partial_callback_failure_can_retry_without_duplicate_at_collector) ... ok
test_publish_delivers_valid_schema (test_iot_simulator.IoTSimulatorTest.test_publish_delivers_valid_schema) ... ok
test_reconnection_delivers_old_events_before_new_sample (test_iot_simulator.IoTSimulatorTest.test_reconnection_delivers_old_events_before_new_sample) ... ok
test_returned_messages_cannot_corrupt_history_or_deduplication (test_iot_simulator.IoTSimulatorTest.test_returned_messages_cannot_corrupt_history_or_deduplication) ... ok
test_schema_and_fields_are_exact (test_iot_simulator.IoTSimulatorTest.test_schema_and_fields_are_exact) ... ok
test_seed_and_clock_are_reproducible (test_iot_simulator.IoTSimulatorTest.test_seed_and_clock_are_reproducible) ... ok
test_sequence_requires_nonnegative_integer (test_iot_simulator.IoTSimulatorTest.test_sequence_requires_nonnegative_integer) ... ok
test_timestamp_requires_explicit_utc (test_iot_simulator.IoTSimulatorTest.test_timestamp_requires_explicit_utc) ... ok
test_topic_and_payload_device_must_match (test_iot_simulator.IoTSimulatorTest.test_topic_and_payload_device_must_match) ... ok
test_unseen_out_of_order_is_rejected_but_old_retry_is_allowed (test_iot_simulator.IoTSimulatorTest.test_unseen_out_of_order_is_rejected_but_old_retry_is_allowed) ... ok

----------------------------------------------------------------------
Ran 22 tests in 0.004s

OK
```

## Demo e controlli runtime

Questa matrice esegue le suite `run_tests.py`. Le summary non classificano processi separati come demo o controlli runtime: non sono aggiunti output o esiti di tali categorie.

## Verifica e provenienza

[Registro strutturato](registro.json) · [Hash e trasformazioni](MANIFEST.json) · [Policy](../AUDIT.md) · [Indice](../README.md)
