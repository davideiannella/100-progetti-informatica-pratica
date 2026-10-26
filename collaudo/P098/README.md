# P098: output dei collaudi

[Indice dei collaudi](../README.md) · [Codice e istruzioni](../../projects/P098/README.md)

Esito registrato: **PASS in tutte le quattro combinazioni**. [Run 39893701054](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39893701054) · commit `3ab7bdfedb20a443bd71fe4e4ffe3c1dd67bd707`.

Comando effettivo del [runner a quel commit](https://github.com/davideiannella/100-progetti-informatica-pratica/blob/3ab7bdfedb20a443bd71fe4e4ffe3c1dd67bd707/tools/collaudo_p081_p100.py): `[sys.executable, "-B", "run_tests.py"]`, con directory di lavoro `projects/P098`. `sys.executable` indica l’interprete della combinazione riportata sotto; il suo percorso host assoluto non è registrato nella summary.

I quattro rapporti sono output CI preesistenti, non nuove esecuzioni preparate per questa pagina. Ogni ambiente ha verificato gli hash dei 299 sorgenti, compilato 60 file Python e completato 20 suite per 377 metodi complessivi.

`unittest` scrive normalmente il rapporto dettagliato su **stderr**: questo non equivale a un errore. I nomi e gli esiti sotto provengono dalle righe effettivamente emesse; non sono stati ricostruiti dal codice. I TXT mantengono i byte e i terminatori originali, compreso CRLF su Windows; i blocchi Markdown normalizzano soltanto i terminatori.

## Suite — quattro ambienti CI

### ubuntu-latest-python-3.12

Artifact: `output-p081-p100-ubuntu-latest-python-3.12` (ID `12476170749`). [Summary originale](../ambienti/ubuntu-latest-python-3.12.summary.json).

OS: `Linux` · piattaforma: `Linux-6.17.0-1022-azure-x86_64-with-glibc2.39` · Python: `3.12.15 (main, Oct  1 2026, 02:35:59) [GCC 13.3.0]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **17** · skipped: `0`.

**stdout** — [file TXT](streams/ubuntu-latest-python-3.12.stdout.txt)

```text
test_methods=17; executed=17; failures=0; errors=0
```

**stderr** — [file TXT](streams/ubuntu-latest-python-3.12.stderr.txt)

```text
test_collector_validation_error_preserves_head (test_p098.MonitorTests.test_collector_validation_error_preserves_head) ... ok
test_conflicting_duplicate_is_rejected (test_p098.MonitorTests.test_conflicting_duplicate_is_rejected) ... ok
test_demo_numbers (test_p098.MonitorTests.test_demo_numbers) ... ok
test_devices_have_independent_sequences (test_p098.MonitorTests.test_devices_have_independent_sequences) ... ok
test_duplicate_ack_has_no_second_effect (test_p098.MonitorTests.test_duplicate_ack_has_no_second_effect) ... ok
test_invalid_event_schema_and_sequence (test_p098.MonitorTests.test_invalid_event_schema_and_sequence) ... ok
test_invalid_identity_and_online_flag (test_p098.MonitorTests.test_invalid_identity_and_online_flag) ... ok
test_invalid_samples_do_not_consume_sequence (test_p098.MonitorTests.test_invalid_samples_do_not_consume_sequence) ... ok
test_lost_ack_replay_deduplicates_then_continues (test_p098.MonitorTests.test_lost_ack_replay_deduplicates_then_continues) ... ok
test_network_error_before_acceptance_keeps_all_events (test_p098.MonitorTests.test_network_error_before_acceptance_keeps_all_events) ... ok
test_new_event_gap_is_rejected (test_p098.MonitorTests.test_new_event_gap_is_rejected) ... ok
test_offline_retains_fifo (test_p098.MonitorTests.test_offline_retains_fifo) ... ok
test_partial_flush_keeps_head_and_suffix_on_error (test_p098.MonitorTests.test_partial_flush_keeps_head_and_suffix_on_error) ... ok
test_reconnect_drains_in_order (test_p098.MonitorTests.test_reconnect_drains_in_order) ... ok
test_restart_loses_ram_state_and_detects_sequence_conflict (test_p098.MonitorTests.test_restart_loses_ram_state_and_detects_sequence_conflict) ... ok
test_snapshots_do_not_modify_buffer_or_collector (test_p098.MonitorTests.test_snapshots_do_not_modify_buffer_or_collector) ... ok
test_wrong_or_missing_ack_cannot_discard_event (test_p098.MonitorTests.test_wrong_or_missing_ack_cannot_discard_event) ... ok

----------------------------------------------------------------------
Ran 17 tests in 0.002s

OK
```

### ubuntu-latest-python-3.13

Artifact: `output-p081-p100-ubuntu-latest-python-3.13` (ID `12476095990`). [Summary originale](../ambienti/ubuntu-latest-python-3.13.summary.json).

OS: `Linux` · piattaforma: `Linux-6.17.0-1022-azure-x86_64-with-glibc2.39` · Python: `3.13.16 (main, Oct  1 2026, 02:37:54) [GCC 13.3.0]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **17** · skipped: `0`.

**stdout** — [file TXT](streams/ubuntu-latest-python-3.13.stdout.txt)

```text
test_methods=17; executed=17; failures=0; errors=0
```

**stderr** — [file TXT](streams/ubuntu-latest-python-3.13.stderr.txt)

```text
test_collector_validation_error_preserves_head (test_p098.MonitorTests.test_collector_validation_error_preserves_head) ... ok
test_conflicting_duplicate_is_rejected (test_p098.MonitorTests.test_conflicting_duplicate_is_rejected) ... ok
test_demo_numbers (test_p098.MonitorTests.test_demo_numbers) ... ok
test_devices_have_independent_sequences (test_p098.MonitorTests.test_devices_have_independent_sequences) ... ok
test_duplicate_ack_has_no_second_effect (test_p098.MonitorTests.test_duplicate_ack_has_no_second_effect) ... ok
test_invalid_event_schema_and_sequence (test_p098.MonitorTests.test_invalid_event_schema_and_sequence) ... ok
test_invalid_identity_and_online_flag (test_p098.MonitorTests.test_invalid_identity_and_online_flag) ... ok
test_invalid_samples_do_not_consume_sequence (test_p098.MonitorTests.test_invalid_samples_do_not_consume_sequence) ... ok
test_lost_ack_replay_deduplicates_then_continues (test_p098.MonitorTests.test_lost_ack_replay_deduplicates_then_continues) ... ok
test_network_error_before_acceptance_keeps_all_events (test_p098.MonitorTests.test_network_error_before_acceptance_keeps_all_events) ... ok
test_new_event_gap_is_rejected (test_p098.MonitorTests.test_new_event_gap_is_rejected) ... ok
test_offline_retains_fifo (test_p098.MonitorTests.test_offline_retains_fifo) ... ok
test_partial_flush_keeps_head_and_suffix_on_error (test_p098.MonitorTests.test_partial_flush_keeps_head_and_suffix_on_error) ... ok
test_reconnect_drains_in_order (test_p098.MonitorTests.test_reconnect_drains_in_order) ... ok
test_restart_loses_ram_state_and_detects_sequence_conflict (test_p098.MonitorTests.test_restart_loses_ram_state_and_detects_sequence_conflict) ... ok
test_snapshots_do_not_modify_buffer_or_collector (test_p098.MonitorTests.test_snapshots_do_not_modify_buffer_or_collector) ... ok
test_wrong_or_missing_ack_cannot_discard_event (test_p098.MonitorTests.test_wrong_or_missing_ack_cannot_discard_event) ... ok

----------------------------------------------------------------------
Ran 17 tests in 0.002s

OK
```

### windows-latest-python-3.12

Artifact: `output-p081-p100-windows-latest-python-3.12` (ID `12475927047`). [Summary originale](../ambienti/windows-latest-python-3.12.summary.json).

OS: `Windows` · piattaforma: `Windows-2025Server-10.0.26100-SP0` · Python: `3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **17** · skipped: `0`.

**stdout** — [file TXT](streams/windows-latest-python-3.12.stdout.txt)

```text
test_methods=17; executed=17; failures=0; errors=0
```

**stderr** — [file TXT](streams/windows-latest-python-3.12.stderr.txt)

```text
test_collector_validation_error_preserves_head (test_p098.MonitorTests.test_collector_validation_error_preserves_head) ... ok
test_conflicting_duplicate_is_rejected (test_p098.MonitorTests.test_conflicting_duplicate_is_rejected) ... ok
test_demo_numbers (test_p098.MonitorTests.test_demo_numbers) ... ok
test_devices_have_independent_sequences (test_p098.MonitorTests.test_devices_have_independent_sequences) ... ok
test_duplicate_ack_has_no_second_effect (test_p098.MonitorTests.test_duplicate_ack_has_no_second_effect) ... ok
test_invalid_event_schema_and_sequence (test_p098.MonitorTests.test_invalid_event_schema_and_sequence) ... ok
test_invalid_identity_and_online_flag (test_p098.MonitorTests.test_invalid_identity_and_online_flag) ... ok
test_invalid_samples_do_not_consume_sequence (test_p098.MonitorTests.test_invalid_samples_do_not_consume_sequence) ... ok
test_lost_ack_replay_deduplicates_then_continues (test_p098.MonitorTests.test_lost_ack_replay_deduplicates_then_continues) ... ok
test_network_error_before_acceptance_keeps_all_events (test_p098.MonitorTests.test_network_error_before_acceptance_keeps_all_events) ... ok
test_new_event_gap_is_rejected (test_p098.MonitorTests.test_new_event_gap_is_rejected) ... ok
test_offline_retains_fifo (test_p098.MonitorTests.test_offline_retains_fifo) ... ok
test_partial_flush_keeps_head_and_suffix_on_error (test_p098.MonitorTests.test_partial_flush_keeps_head_and_suffix_on_error) ... ok
test_reconnect_drains_in_order (test_p098.MonitorTests.test_reconnect_drains_in_order) ... ok
test_restart_loses_ram_state_and_detects_sequence_conflict (test_p098.MonitorTests.test_restart_loses_ram_state_and_detects_sequence_conflict) ... ok
test_snapshots_do_not_modify_buffer_or_collector (test_p098.MonitorTests.test_snapshots_do_not_modify_buffer_or_collector) ... ok
test_wrong_or_missing_ack_cannot_discard_event (test_p098.MonitorTests.test_wrong_or_missing_ack_cannot_discard_event) ... ok

----------------------------------------------------------------------
Ran 17 tests in 0.002s

OK
```

### windows-latest-python-3.13

Artifact: `output-p081-p100-windows-latest-python-3.13` (ID `12475826902`). [Summary originale](../ambienti/windows-latest-python-3.13.summary.json).

OS: `Windows` · piattaforma: `Windows-2025Server-10.0.26100-SP0` · Python: `3.13.16 (tags/v3.13.16:cbc944f, Sep 30 2026, 19:17:50) [MSC v.1944 64 bit (AMD64)]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **17** · skipped: `0`.

**stdout** — [file TXT](streams/windows-latest-python-3.13.stdout.txt)

```text
test_methods=17; executed=17; failures=0; errors=0
```

**stderr** — [file TXT](streams/windows-latest-python-3.13.stderr.txt)

```text
test_collector_validation_error_preserves_head (test_p098.MonitorTests.test_collector_validation_error_preserves_head) ... ok
test_conflicting_duplicate_is_rejected (test_p098.MonitorTests.test_conflicting_duplicate_is_rejected) ... ok
test_demo_numbers (test_p098.MonitorTests.test_demo_numbers) ... ok
test_devices_have_independent_sequences (test_p098.MonitorTests.test_devices_have_independent_sequences) ... ok
test_duplicate_ack_has_no_second_effect (test_p098.MonitorTests.test_duplicate_ack_has_no_second_effect) ... ok
test_invalid_event_schema_and_sequence (test_p098.MonitorTests.test_invalid_event_schema_and_sequence) ... ok
test_invalid_identity_and_online_flag (test_p098.MonitorTests.test_invalid_identity_and_online_flag) ... ok
test_invalid_samples_do_not_consume_sequence (test_p098.MonitorTests.test_invalid_samples_do_not_consume_sequence) ... ok
test_lost_ack_replay_deduplicates_then_continues (test_p098.MonitorTests.test_lost_ack_replay_deduplicates_then_continues) ... ok
test_network_error_before_acceptance_keeps_all_events (test_p098.MonitorTests.test_network_error_before_acceptance_keeps_all_events) ... ok
test_new_event_gap_is_rejected (test_p098.MonitorTests.test_new_event_gap_is_rejected) ... ok
test_offline_retains_fifo (test_p098.MonitorTests.test_offline_retains_fifo) ... ok
test_partial_flush_keeps_head_and_suffix_on_error (test_p098.MonitorTests.test_partial_flush_keeps_head_and_suffix_on_error) ... ok
test_reconnect_drains_in_order (test_p098.MonitorTests.test_reconnect_drains_in_order) ... ok
test_restart_loses_ram_state_and_detects_sequence_conflict (test_p098.MonitorTests.test_restart_loses_ram_state_and_detects_sequence_conflict) ... ok
test_snapshots_do_not_modify_buffer_or_collector (test_p098.MonitorTests.test_snapshots_do_not_modify_buffer_or_collector) ... ok
test_wrong_or_missing_ack_cannot_discard_event (test_p098.MonitorTests.test_wrong_or_missing_ack_cannot_discard_event) ... ok

----------------------------------------------------------------------
Ran 17 tests in 0.002s

OK
```

## Demo e controlli runtime

Questa matrice esegue le suite `run_tests.py`. Le summary non classificano processi separati come demo o controlli runtime: non sono aggiunti output o esiti di tali categorie.

## Verifica e provenienza

[Registro strutturato](registro.json) · [Hash e trasformazioni](MANIFEST.json) · [Policy](../AUDIT.md) · [Indice](../README.md)
