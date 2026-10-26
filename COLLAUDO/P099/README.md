# P099: output dei collaudi

[Indice dei collaudi](../README.md) · [Codice e istruzioni](../../projects/P099/README.md)

Esito registrato: **PASS in tutte le quattro combinazioni**. [Run 39893701054](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39893701054) · commit `3ab7bdfedb20a443bd71fe4e4ffe3c1dd67bd707`.

Comando effettivo del [runner a quel commit](https://github.com/davideiannella/100-progetti-informatica-pratica/blob/3ab7bdfedb20a443bd71fe4e4ffe3c1dd67bd707/tools/collaudo_p081_p100.py): `[sys.executable, "-B", "run_tests.py"]`, con directory di lavoro `projects/P099`. `sys.executable` indica l’interprete della combinazione riportata sotto; il suo percorso host assoluto non è registrato nella summary.

I quattro rapporti sono output CI preesistenti, non nuove esecuzioni preparate per questa pagina. Ogni ambiente ha verificato gli hash dei 299 sorgenti, compilato 60 file Python e completato 20 suite per 377 metodi complessivi.

`unittest` scrive normalmente il rapporto dettagliato su **stderr**: questo non equivale a un errore. I nomi e gli esiti sotto provengono dalle righe effettivamente emesse; non sono stati ricostruiti dal codice. I TXT mantengono i byte e i terminatori originali, compreso CRLF su Windows; i blocchi Markdown normalizzano soltanto i terminatori.

## Suite — quattro ambienti CI

### ubuntu-latest-python-3.12

Artifact: `output-p081-p100-ubuntu-latest-python-3.12` (ID `12476170749`). [Summary originale](../ambienti/ubuntu-latest-python-3.12.summary.json).

OS: `Linux` · piattaforma: `Linux-6.17.0-1022-azure-x86_64-with-glibc2.39` · Python: `3.12.15 (main, Oct  1 2026, 02:35:59) [GCC 13.3.0]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **20** · skipped: `0`.

**stdout** — [file TXT](streams/ubuntu-latest-python-3.12.stdout.txt)

```text
test_methods=20; executed=20; failures=0; errors=0
```

**stderr** — [file TXT](streams/ubuntu-latest-python-3.12.stderr.txt)

```text
test_all_negative_or_nonfinite_weights_rejected_even_off_path (test_p099.LogisticsTests.test_all_negative_or_nonfinite_weights_rejected_even_off_path) ... ok
test_demo_numbers (test_p099.LogisticsTests.test_demo_numbers) ... ok
test_disconnected_and_unknown_nodes (test_p099.LogisticsTests.test_disconnected_and_unknown_nodes) ... ok
test_eta_is_separate_arithmetic (test_p099.LogisticsTests.test_eta_is_separate_arithmetic) ... ok
test_graph_shape_and_missing_destination_rejected (test_p099.LogisticsTests.test_graph_shape_and_missing_destination_rejected) ... ok
test_invalid_history_and_window (test_p099.LogisticsTests.test_invalid_history_and_window) ... ok
test_mean_near_float_limit_stays_finite (test_p099.LogisticsTests.test_mean_near_float_limit_stays_finite) ... ok
test_moving_average_uses_last_k (test_p099.LogisticsTests.test_moving_average_uses_last_k) ... ok
test_overflowing_route_is_rejected (test_p099.LogisticsTests.test_overflowing_route_is_rejected) ... ok
test_parallel_edges_choose_cheaper (test_p099.LogisticsTests.test_parallel_edges_choose_cheaper) ... ok
test_route_improves_direct_cost (test_p099.LogisticsTests.test_route_improves_direct_cost) ... ok
test_routing_is_deterministic_across_input_order (test_p099.LogisticsTests.test_routing_is_deterministic_across_input_order) ... ok
test_shipment_cannot_skip_or_repeat_state_with_new_id (test_p099.LogisticsTests.test_shipment_cannot_skip_or_repeat_state_with_new_id) ... ok
test_shipment_transitions_and_idempotent_retry (test_p099.LogisticsTests.test_shipment_transitions_and_idempotent_retry) ... ok
test_tracking_conflict_and_nonincreasing_time_rejected (test_p099.LogisticsTests.test_tracking_conflict_and_nonincreasing_time_rejected) ... ok
test_tracking_invalid_values_do_not_mutate (test_p099.LogisticsTests.test_tracking_invalid_values_do_not_mutate) ... ok
test_tracking_snapshot_and_terminal_state (test_p099.LogisticsTests.test_tracking_snapshot_and_terminal_state) ... ok
test_warehouse_allocation_and_insufficiency (test_p099.LogisticsTests.test_warehouse_allocation_and_insufficiency) ... ok
test_warehouse_invalid_quantities_do_not_mutate (test_p099.LogisticsTests.test_warehouse_invalid_quantities_do_not_mutate) ... ok
test_zero_weights_cycles_and_same_node (test_p099.LogisticsTests.test_zero_weights_cycles_and_same_node) ... ok

----------------------------------------------------------------------
Ran 20 tests in 0.002s

OK
```

### ubuntu-latest-python-3.13

Artifact: `output-p081-p100-ubuntu-latest-python-3.13` (ID `12476095990`). [Summary originale](../ambienti/ubuntu-latest-python-3.13.summary.json).

OS: `Linux` · piattaforma: `Linux-6.17.0-1022-azure-x86_64-with-glibc2.39` · Python: `3.13.16 (main, Oct  1 2026, 02:37:54) [GCC 13.3.0]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **20** · skipped: `0`.

**stdout** — [file TXT](streams/ubuntu-latest-python-3.13.stdout.txt)

```text
test_methods=20; executed=20; failures=0; errors=0
```

**stderr** — [file TXT](streams/ubuntu-latest-python-3.13.stderr.txt)

```text
test_all_negative_or_nonfinite_weights_rejected_even_off_path (test_p099.LogisticsTests.test_all_negative_or_nonfinite_weights_rejected_even_off_path) ... ok
test_demo_numbers (test_p099.LogisticsTests.test_demo_numbers) ... ok
test_disconnected_and_unknown_nodes (test_p099.LogisticsTests.test_disconnected_and_unknown_nodes) ... ok
test_eta_is_separate_arithmetic (test_p099.LogisticsTests.test_eta_is_separate_arithmetic) ... ok
test_graph_shape_and_missing_destination_rejected (test_p099.LogisticsTests.test_graph_shape_and_missing_destination_rejected) ... ok
test_invalid_history_and_window (test_p099.LogisticsTests.test_invalid_history_and_window) ... ok
test_mean_near_float_limit_stays_finite (test_p099.LogisticsTests.test_mean_near_float_limit_stays_finite) ... ok
test_moving_average_uses_last_k (test_p099.LogisticsTests.test_moving_average_uses_last_k) ... ok
test_overflowing_route_is_rejected (test_p099.LogisticsTests.test_overflowing_route_is_rejected) ... ok
test_parallel_edges_choose_cheaper (test_p099.LogisticsTests.test_parallel_edges_choose_cheaper) ... ok
test_route_improves_direct_cost (test_p099.LogisticsTests.test_route_improves_direct_cost) ... ok
test_routing_is_deterministic_across_input_order (test_p099.LogisticsTests.test_routing_is_deterministic_across_input_order) ... ok
test_shipment_cannot_skip_or_repeat_state_with_new_id (test_p099.LogisticsTests.test_shipment_cannot_skip_or_repeat_state_with_new_id) ... ok
test_shipment_transitions_and_idempotent_retry (test_p099.LogisticsTests.test_shipment_transitions_and_idempotent_retry) ... ok
test_tracking_conflict_and_nonincreasing_time_rejected (test_p099.LogisticsTests.test_tracking_conflict_and_nonincreasing_time_rejected) ... ok
test_tracking_invalid_values_do_not_mutate (test_p099.LogisticsTests.test_tracking_invalid_values_do_not_mutate) ... ok
test_tracking_snapshot_and_terminal_state (test_p099.LogisticsTests.test_tracking_snapshot_and_terminal_state) ... ok
test_warehouse_allocation_and_insufficiency (test_p099.LogisticsTests.test_warehouse_allocation_and_insufficiency) ... ok
test_warehouse_invalid_quantities_do_not_mutate (test_p099.LogisticsTests.test_warehouse_invalid_quantities_do_not_mutate) ... ok
test_zero_weights_cycles_and_same_node (test_p099.LogisticsTests.test_zero_weights_cycles_and_same_node) ... ok

----------------------------------------------------------------------
Ran 20 tests in 0.002s

OK
```

### windows-latest-python-3.12

Artifact: `output-p081-p100-windows-latest-python-3.12` (ID `12475927047`). [Summary originale](../ambienti/windows-latest-python-3.12.summary.json).

OS: `Windows` · piattaforma: `Windows-2025Server-10.0.26100-SP0` · Python: `3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **20** · skipped: `0`.

**stdout** — [file TXT](streams/windows-latest-python-3.12.stdout.txt)

```text
test_methods=20; executed=20; failures=0; errors=0
```

**stderr** — [file TXT](streams/windows-latest-python-3.12.stderr.txt)

```text
test_all_negative_or_nonfinite_weights_rejected_even_off_path (test_p099.LogisticsTests.test_all_negative_or_nonfinite_weights_rejected_even_off_path) ... ok
test_demo_numbers (test_p099.LogisticsTests.test_demo_numbers) ... ok
test_disconnected_and_unknown_nodes (test_p099.LogisticsTests.test_disconnected_and_unknown_nodes) ... ok
test_eta_is_separate_arithmetic (test_p099.LogisticsTests.test_eta_is_separate_arithmetic) ... ok
test_graph_shape_and_missing_destination_rejected (test_p099.LogisticsTests.test_graph_shape_and_missing_destination_rejected) ... ok
test_invalid_history_and_window (test_p099.LogisticsTests.test_invalid_history_and_window) ... ok
test_mean_near_float_limit_stays_finite (test_p099.LogisticsTests.test_mean_near_float_limit_stays_finite) ... ok
test_moving_average_uses_last_k (test_p099.LogisticsTests.test_moving_average_uses_last_k) ... ok
test_overflowing_route_is_rejected (test_p099.LogisticsTests.test_overflowing_route_is_rejected) ... ok
test_parallel_edges_choose_cheaper (test_p099.LogisticsTests.test_parallel_edges_choose_cheaper) ... ok
test_route_improves_direct_cost (test_p099.LogisticsTests.test_route_improves_direct_cost) ... ok
test_routing_is_deterministic_across_input_order (test_p099.LogisticsTests.test_routing_is_deterministic_across_input_order) ... ok
test_shipment_cannot_skip_or_repeat_state_with_new_id (test_p099.LogisticsTests.test_shipment_cannot_skip_or_repeat_state_with_new_id) ... ok
test_shipment_transitions_and_idempotent_retry (test_p099.LogisticsTests.test_shipment_transitions_and_idempotent_retry) ... ok
test_tracking_conflict_and_nonincreasing_time_rejected (test_p099.LogisticsTests.test_tracking_conflict_and_nonincreasing_time_rejected) ... ok
test_tracking_invalid_values_do_not_mutate (test_p099.LogisticsTests.test_tracking_invalid_values_do_not_mutate) ... ok
test_tracking_snapshot_and_terminal_state (test_p099.LogisticsTests.test_tracking_snapshot_and_terminal_state) ... ok
test_warehouse_allocation_and_insufficiency (test_p099.LogisticsTests.test_warehouse_allocation_and_insufficiency) ... ok
test_warehouse_invalid_quantities_do_not_mutate (test_p099.LogisticsTests.test_warehouse_invalid_quantities_do_not_mutate) ... ok
test_zero_weights_cycles_and_same_node (test_p099.LogisticsTests.test_zero_weights_cycles_and_same_node) ... ok

----------------------------------------------------------------------
Ran 20 tests in 0.002s

OK
```

### windows-latest-python-3.13

Artifact: `output-p081-p100-windows-latest-python-3.13` (ID `12475826902`). [Summary originale](../ambienti/windows-latest-python-3.13.summary.json).

OS: `Windows` · piattaforma: `Windows-2025Server-10.0.26100-SP0` · Python: `3.13.16 (tags/v3.13.16:cbc944f, Sep 30 2026, 19:17:50) [MSC v.1944 64 bit (AMD64)]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **20** · skipped: `0`.

**stdout** — [file TXT](streams/windows-latest-python-3.13.stdout.txt)

```text
test_methods=20; executed=20; failures=0; errors=0
```

**stderr** — [file TXT](streams/windows-latest-python-3.13.stderr.txt)

```text
test_all_negative_or_nonfinite_weights_rejected_even_off_path (test_p099.LogisticsTests.test_all_negative_or_nonfinite_weights_rejected_even_off_path) ... ok
test_demo_numbers (test_p099.LogisticsTests.test_demo_numbers) ... ok
test_disconnected_and_unknown_nodes (test_p099.LogisticsTests.test_disconnected_and_unknown_nodes) ... ok
test_eta_is_separate_arithmetic (test_p099.LogisticsTests.test_eta_is_separate_arithmetic) ... ok
test_graph_shape_and_missing_destination_rejected (test_p099.LogisticsTests.test_graph_shape_and_missing_destination_rejected) ... ok
test_invalid_history_and_window (test_p099.LogisticsTests.test_invalid_history_and_window) ... ok
test_mean_near_float_limit_stays_finite (test_p099.LogisticsTests.test_mean_near_float_limit_stays_finite) ... ok
test_moving_average_uses_last_k (test_p099.LogisticsTests.test_moving_average_uses_last_k) ... ok
test_overflowing_route_is_rejected (test_p099.LogisticsTests.test_overflowing_route_is_rejected) ... ok
test_parallel_edges_choose_cheaper (test_p099.LogisticsTests.test_parallel_edges_choose_cheaper) ... ok
test_route_improves_direct_cost (test_p099.LogisticsTests.test_route_improves_direct_cost) ... ok
test_routing_is_deterministic_across_input_order (test_p099.LogisticsTests.test_routing_is_deterministic_across_input_order) ... ok
test_shipment_cannot_skip_or_repeat_state_with_new_id (test_p099.LogisticsTests.test_shipment_cannot_skip_or_repeat_state_with_new_id) ... ok
test_shipment_transitions_and_idempotent_retry (test_p099.LogisticsTests.test_shipment_transitions_and_idempotent_retry) ... ok
test_tracking_conflict_and_nonincreasing_time_rejected (test_p099.LogisticsTests.test_tracking_conflict_and_nonincreasing_time_rejected) ... ok
test_tracking_invalid_values_do_not_mutate (test_p099.LogisticsTests.test_tracking_invalid_values_do_not_mutate) ... ok
test_tracking_snapshot_and_terminal_state (test_p099.LogisticsTests.test_tracking_snapshot_and_terminal_state) ... ok
test_warehouse_allocation_and_insufficiency (test_p099.LogisticsTests.test_warehouse_allocation_and_insufficiency) ... ok
test_warehouse_invalid_quantities_do_not_mutate (test_p099.LogisticsTests.test_warehouse_invalid_quantities_do_not_mutate) ... ok
test_zero_weights_cycles_and_same_node (test_p099.LogisticsTests.test_zero_weights_cycles_and_same_node) ... ok

----------------------------------------------------------------------
Ran 20 tests in 0.002s

OK
```

## Demo e controlli runtime

Questa matrice esegue le suite `run_tests.py`. Le summary non classificano processi separati come demo o controlli runtime: non sono aggiunti output o esiti di tali categorie.

## Verifica e provenienza

[Registro strutturato](registro.json) · [Hash e trasformazioni](MANIFEST.json) · [Policy](../AUDIT.md) · [Indice](../README.md)
