# P096 — output reali dei collaudi

Esito registrato: **PASS in tutte le quattro combinazioni**. [Run 39893701054](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39893701054) · commit `3ab7bdfedb20a443bd71fe4e4ffe3c1dd67bd707`.

Comando effettivo del [runner a quel commit](https://github.com/davideiannella/100-progetti-informatica-pratica/blob/3ab7bdfedb20a443bd71fe4e4ffe3c1dd67bd707/tools/collaudo_p081_p100.py): `[sys.executable, "-B", "run_tests.py"]`, con directory di lavoro `projects/P096`. `sys.executable` indica l’interprete della combinazione riportata sotto; il suo percorso host assoluto non è registrato nella summary.

I quattro rapporti sono output CI preesistenti, non nuove esecuzioni preparate per questa pagina. Ogni ambiente ha verificato gli hash dei 299 sorgenti, compilato 60 file Python e completato 20 suite per 377 metodi complessivi.

`unittest` scrive normalmente il rapporto dettagliato su **stderr**: questo non equivale a un errore. I nomi e gli esiti sotto provengono dalle righe effettivamente emesse; non sono stati ricostruiti dal codice. I TXT mantengono i byte e i terminatori originali, compreso CRLF su Windows; i blocchi Markdown normalizzano soltanto i terminatori.

## Suite — quattro ambienti CI

### ubuntu-latest-python-3.12

Artifact: `output-p081-p100-ubuntu-latest-python-3.12` (ID `12476170749`). [Summary originale](../ambienti/ubuntu-latest-python-3.12.summary.json).

OS: `Linux` · piattaforma: `Linux-6.17.0-1022-azure-x86_64-with-glibc2.39` · Python: `3.12.15 (main, Oct  1 2026, 02:35:59) [GCC 13.3.0]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **19** · skipped: `0`.

**stdout** — [file TXT](streams/ubuntu-latest-python-3.12.stdout.txt)

```text
test_methods=19; executed=19; failures=0; errors=0
```

**stderr** — [file TXT](streams/ubuntu-latest-python-3.12.stderr.txt)

```text
test_catalog_rejects_duplicates_and_invalid_metadata (test_p096.EcommerceTests.test_catalog_rejects_duplicates_and_invalid_metadata) ... ok
test_create_reserves_once_and_publishes (test_p096.EcommerceTests.test_create_reserves_once_and_publishes) ... ok
test_demo_numbers (test_p096.EcommerceTests.test_demo_numbers) ... ok
test_exact_stock_can_be_allocated_then_exhausted (test_p096.EcommerceTests.test_exact_stock_can_be_allocated_then_exhausted) ... ok
test_insufficient_and_unknown_stock_do_not_create (test_p096.EcommerceTests.test_insufficient_and_unknown_stock_do_not_create) ... ok
test_invalid_identifiers_are_rejected (test_p096.EcommerceTests.test_invalid_identifiers_are_rejected) ... ok
test_invalid_order_quantities_are_rejected_before_mutation (test_p096.EcommerceTests.test_invalid_order_quantities_are_rejected_before_mutation) ... ok
test_invalid_transition_and_post_shipping_refund (test_p096.EcommerceTests.test_invalid_transition_and_post_shipping_refund) ... ok
test_inventory_set_requires_nonnegative_integer (test_p096.EcommerceTests.test_inventory_set_requires_nonnegative_integer) ... ok
test_local_create_rollback_after_publisher_failure (test_p096.EcommerceTests.test_local_create_rollback_after_publisher_failure) ... ok
test_local_refund_rollback_after_publisher_failure (test_p096.EcommerceTests.test_local_refund_rollback_after_publisher_failure) ... ok
test_recommendations_are_sorted_and_category_only (test_p096.EcommerceTests.test_recommendations_are_sorted_and_category_only) ... ok
test_refund_restores_stock_once (test_p096.EcommerceTests.test_refund_restores_stock_once) ... ok
test_refunded_order_cannot_ship_and_unknown_cannot_refund (test_p096.EcommerceTests.test_refunded_order_cannot_ship_and_unknown_cannot_refund) ... ok
test_retry_after_refund_does_not_reopen_order (test_p096.EcommerceTests.test_retry_after_refund_does_not_reopen_order) ... ok
test_retry_conflict_leaves_all_state_unchanged (test_p096.EcommerceTests.test_retry_conflict_leaves_all_state_unchanged) ... ok
test_retry_is_idempotent (test_p096.EcommerceTests.test_retry_is_idempotent) ... ok
test_returned_snapshots_do_not_mutate_internal_state (test_p096.EcommerceTests.test_returned_snapshots_do_not_mutate_internal_state) ... ok
test_shipping_and_delivery_are_idempotent (test_p096.EcommerceTests.test_shipping_and_delivery_are_idempotent) ... ok

----------------------------------------------------------------------
Ran 19 tests in 0.002s

OK
```

### ubuntu-latest-python-3.13

Artifact: `output-p081-p100-ubuntu-latest-python-3.13` (ID `12476095990`). [Summary originale](../ambienti/ubuntu-latest-python-3.13.summary.json).

OS: `Linux` · piattaforma: `Linux-6.17.0-1022-azure-x86_64-with-glibc2.39` · Python: `3.13.16 (main, Oct  1 2026, 02:37:54) [GCC 13.3.0]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **19** · skipped: `0`.

**stdout** — [file TXT](streams/ubuntu-latest-python-3.13.stdout.txt)

```text
test_methods=19; executed=19; failures=0; errors=0
```

**stderr** — [file TXT](streams/ubuntu-latest-python-3.13.stderr.txt)

```text
test_catalog_rejects_duplicates_and_invalid_metadata (test_p096.EcommerceTests.test_catalog_rejects_duplicates_and_invalid_metadata) ... ok
test_create_reserves_once_and_publishes (test_p096.EcommerceTests.test_create_reserves_once_and_publishes) ... ok
test_demo_numbers (test_p096.EcommerceTests.test_demo_numbers) ... ok
test_exact_stock_can_be_allocated_then_exhausted (test_p096.EcommerceTests.test_exact_stock_can_be_allocated_then_exhausted) ... ok
test_insufficient_and_unknown_stock_do_not_create (test_p096.EcommerceTests.test_insufficient_and_unknown_stock_do_not_create) ... ok
test_invalid_identifiers_are_rejected (test_p096.EcommerceTests.test_invalid_identifiers_are_rejected) ... ok
test_invalid_order_quantities_are_rejected_before_mutation (test_p096.EcommerceTests.test_invalid_order_quantities_are_rejected_before_mutation) ... ok
test_invalid_transition_and_post_shipping_refund (test_p096.EcommerceTests.test_invalid_transition_and_post_shipping_refund) ... ok
test_inventory_set_requires_nonnegative_integer (test_p096.EcommerceTests.test_inventory_set_requires_nonnegative_integer) ... ok
test_local_create_rollback_after_publisher_failure (test_p096.EcommerceTests.test_local_create_rollback_after_publisher_failure) ... ok
test_local_refund_rollback_after_publisher_failure (test_p096.EcommerceTests.test_local_refund_rollback_after_publisher_failure) ... ok
test_recommendations_are_sorted_and_category_only (test_p096.EcommerceTests.test_recommendations_are_sorted_and_category_only) ... ok
test_refund_restores_stock_once (test_p096.EcommerceTests.test_refund_restores_stock_once) ... ok
test_refunded_order_cannot_ship_and_unknown_cannot_refund (test_p096.EcommerceTests.test_refunded_order_cannot_ship_and_unknown_cannot_refund) ... ok
test_retry_after_refund_does_not_reopen_order (test_p096.EcommerceTests.test_retry_after_refund_does_not_reopen_order) ... ok
test_retry_conflict_leaves_all_state_unchanged (test_p096.EcommerceTests.test_retry_conflict_leaves_all_state_unchanged) ... ok
test_retry_is_idempotent (test_p096.EcommerceTests.test_retry_is_idempotent) ... ok
test_returned_snapshots_do_not_mutate_internal_state (test_p096.EcommerceTests.test_returned_snapshots_do_not_mutate_internal_state) ... ok
test_shipping_and_delivery_are_idempotent (test_p096.EcommerceTests.test_shipping_and_delivery_are_idempotent) ... ok

----------------------------------------------------------------------
Ran 19 tests in 0.002s

OK
```

### windows-latest-python-3.12

Artifact: `output-p081-p100-windows-latest-python-3.12` (ID `12475927047`). [Summary originale](../ambienti/windows-latest-python-3.12.summary.json).

OS: `Windows` · piattaforma: `Windows-2025Server-10.0.26100-SP0` · Python: `3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **19** · skipped: `0`.

**stdout** — [file TXT](streams/windows-latest-python-3.12.stdout.txt)

```text
test_methods=19; executed=19; failures=0; errors=0
```

**stderr** — [file TXT](streams/windows-latest-python-3.12.stderr.txt)

```text
test_catalog_rejects_duplicates_and_invalid_metadata (test_p096.EcommerceTests.test_catalog_rejects_duplicates_and_invalid_metadata) ... ok
test_create_reserves_once_and_publishes (test_p096.EcommerceTests.test_create_reserves_once_and_publishes) ... ok
test_demo_numbers (test_p096.EcommerceTests.test_demo_numbers) ... ok
test_exact_stock_can_be_allocated_then_exhausted (test_p096.EcommerceTests.test_exact_stock_can_be_allocated_then_exhausted) ... ok
test_insufficient_and_unknown_stock_do_not_create (test_p096.EcommerceTests.test_insufficient_and_unknown_stock_do_not_create) ... ok
test_invalid_identifiers_are_rejected (test_p096.EcommerceTests.test_invalid_identifiers_are_rejected) ... ok
test_invalid_order_quantities_are_rejected_before_mutation (test_p096.EcommerceTests.test_invalid_order_quantities_are_rejected_before_mutation) ... ok
test_invalid_transition_and_post_shipping_refund (test_p096.EcommerceTests.test_invalid_transition_and_post_shipping_refund) ... ok
test_inventory_set_requires_nonnegative_integer (test_p096.EcommerceTests.test_inventory_set_requires_nonnegative_integer) ... ok
test_local_create_rollback_after_publisher_failure (test_p096.EcommerceTests.test_local_create_rollback_after_publisher_failure) ... ok
test_local_refund_rollback_after_publisher_failure (test_p096.EcommerceTests.test_local_refund_rollback_after_publisher_failure) ... ok
test_recommendations_are_sorted_and_category_only (test_p096.EcommerceTests.test_recommendations_are_sorted_and_category_only) ... ok
test_refund_restores_stock_once (test_p096.EcommerceTests.test_refund_restores_stock_once) ... ok
test_refunded_order_cannot_ship_and_unknown_cannot_refund (test_p096.EcommerceTests.test_refunded_order_cannot_ship_and_unknown_cannot_refund) ... ok
test_retry_after_refund_does_not_reopen_order (test_p096.EcommerceTests.test_retry_after_refund_does_not_reopen_order) ... ok
test_retry_conflict_leaves_all_state_unchanged (test_p096.EcommerceTests.test_retry_conflict_leaves_all_state_unchanged) ... ok
test_retry_is_idempotent (test_p096.EcommerceTests.test_retry_is_idempotent) ... ok
test_returned_snapshots_do_not_mutate_internal_state (test_p096.EcommerceTests.test_returned_snapshots_do_not_mutate_internal_state) ... ok
test_shipping_and_delivery_are_idempotent (test_p096.EcommerceTests.test_shipping_and_delivery_are_idempotent) ... ok

----------------------------------------------------------------------
Ran 19 tests in 0.002s

OK
```

### windows-latest-python-3.13

Artifact: `output-p081-p100-windows-latest-python-3.13` (ID `12475826902`). [Summary originale](../ambienti/windows-latest-python-3.13.summary.json).

OS: `Windows` · piattaforma: `Windows-2025Server-10.0.26100-SP0` · Python: `3.13.16 (tags/v3.13.16:cbc944f, Sep 30 2026, 19:17:50) [MSC v.1944 64 bit (AMD64)]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **19** · skipped: `0`.

**stdout** — [file TXT](streams/windows-latest-python-3.13.stdout.txt)

```text
test_methods=19; executed=19; failures=0; errors=0
```

**stderr** — [file TXT](streams/windows-latest-python-3.13.stderr.txt)

```text
test_catalog_rejects_duplicates_and_invalid_metadata (test_p096.EcommerceTests.test_catalog_rejects_duplicates_and_invalid_metadata) ... ok
test_create_reserves_once_and_publishes (test_p096.EcommerceTests.test_create_reserves_once_and_publishes) ... ok
test_demo_numbers (test_p096.EcommerceTests.test_demo_numbers) ... ok
test_exact_stock_can_be_allocated_then_exhausted (test_p096.EcommerceTests.test_exact_stock_can_be_allocated_then_exhausted) ... ok
test_insufficient_and_unknown_stock_do_not_create (test_p096.EcommerceTests.test_insufficient_and_unknown_stock_do_not_create) ... ok
test_invalid_identifiers_are_rejected (test_p096.EcommerceTests.test_invalid_identifiers_are_rejected) ... ok
test_invalid_order_quantities_are_rejected_before_mutation (test_p096.EcommerceTests.test_invalid_order_quantities_are_rejected_before_mutation) ... ok
test_invalid_transition_and_post_shipping_refund (test_p096.EcommerceTests.test_invalid_transition_and_post_shipping_refund) ... ok
test_inventory_set_requires_nonnegative_integer (test_p096.EcommerceTests.test_inventory_set_requires_nonnegative_integer) ... ok
test_local_create_rollback_after_publisher_failure (test_p096.EcommerceTests.test_local_create_rollback_after_publisher_failure) ... ok
test_local_refund_rollback_after_publisher_failure (test_p096.EcommerceTests.test_local_refund_rollback_after_publisher_failure) ... ok
test_recommendations_are_sorted_and_category_only (test_p096.EcommerceTests.test_recommendations_are_sorted_and_category_only) ... ok
test_refund_restores_stock_once (test_p096.EcommerceTests.test_refund_restores_stock_once) ... ok
test_refunded_order_cannot_ship_and_unknown_cannot_refund (test_p096.EcommerceTests.test_refunded_order_cannot_ship_and_unknown_cannot_refund) ... ok
test_retry_after_refund_does_not_reopen_order (test_p096.EcommerceTests.test_retry_after_refund_does_not_reopen_order) ... ok
test_retry_conflict_leaves_all_state_unchanged (test_p096.EcommerceTests.test_retry_conflict_leaves_all_state_unchanged) ... ok
test_retry_is_idempotent (test_p096.EcommerceTests.test_retry_is_idempotent) ... ok
test_returned_snapshots_do_not_mutate_internal_state (test_p096.EcommerceTests.test_returned_snapshots_do_not_mutate_internal_state) ... ok
test_shipping_and_delivery_are_idempotent (test_p096.EcommerceTests.test_shipping_and_delivery_are_idempotent) ... ok

----------------------------------------------------------------------
Ran 19 tests in 0.002s

OK
```

## Demo e controlli runtime

Questa matrice esegue le suite `run_tests.py`. Le summary non classificano processi separati come demo o controlli runtime: non sono aggiunti output o esiti di tali categorie.

## Verifica e provenienza

[Registro strutturato](registro.json) · [Hash e trasformazioni](MANIFEST.json) · [Policy](../AUDIT.md) · [Indice](../README.md)
