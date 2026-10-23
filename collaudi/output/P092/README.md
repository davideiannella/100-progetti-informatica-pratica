# P092 — output reali dei collaudi

Esito registrato: **PASS in tutte le quattro combinazioni**. [Run 39893701054](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39893701054) · commit `3ab7bdfedb20a443bd71fe4e4ffe3c1dd67bd707`.

Comando effettivo del [runner a quel commit](https://github.com/davideiannella/100-progetti-informatica-pratica/blob/3ab7bdfedb20a443bd71fe4e4ffe3c1dd67bd707/tools/collaudo_p081_p100.py): `[sys.executable, "-B", "run_tests.py"]`, con directory di lavoro `projects/P092`. `sys.executable` indica l’interprete della combinazione riportata sotto; il suo percorso host assoluto non è registrato nella summary.

I quattro rapporti sono output CI preesistenti, non nuove esecuzioni preparate per questa pagina. Ogni ambiente ha verificato gli hash dei 299 sorgenti, compilato 60 file Python e completato 20 suite per 377 metodi complessivi.

`unittest` scrive normalmente il rapporto dettagliato su **stderr**: questo non equivale a un errore. I nomi e gli esiti sotto provengono dalle righe effettivamente emesse; non sono stati ricostruiti dal codice. I TXT mantengono i byte e i terminatori originali, compreso CRLF su Windows; i blocchi Markdown normalizzano soltanto i terminatori.

## Suite — quattro ambienti CI

### ubuntu-latest-python-3.12

Artifact: `output-p081-p100-ubuntu-latest-python-3.12` (ID `12476170749`). [Summary originale](../ambienti/ubuntu-latest-python-3.12.summary.json).

OS: `Linux` · piattaforma: `Linux-6.17.0-1022-azure-x86_64-with-glibc2.39` · Python: `3.12.15 (main, Oct  1 2026, 02:35:59) [GCC 13.3.0]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **22** · skipped: `0`.

**stdout** — [file TXT](streams/ubuntu-latest-python-3.12.stdout.txt)

```text
test_audit_is_copied_and_excludes_shared_secret (test_p092.UpdateTests.test_audit_is_copied_and_excludes_shared_secret) ... ok
test_demo_reports_simulated_rollback_and_replay_rejection (test_p092.UpdateTests.test_demo_reports_simulated_rollback_and_replay_rejection) ... ok
test_device_constructor_validation (test_p092.UpdateTests.test_device_constructor_validation) ... ok
test_digest_types_lengths_and_non_ascii_rejected (test_p092.UpdateTests.test_digest_types_lengths_and_non_ascii_rejected) ... ok
test_equal_older_or_invalid_current_version_rejected (test_p092.UpdateTests.test_equal_older_or_invalid_current_version_rejected) ... ok
test_health_failure_does_not_consume_version (test_p092.UpdateTests.test_health_failure_does_not_consume_version) ... ok
test_health_failure_restores_complete_modeled_snapshot (test_p092.UpdateTests.test_health_failure_restores_complete_modeled_snapshot) ... ok
test_health_requires_bool_and_has_no_effect_on_invalid_input (test_p092.UpdateTests.test_health_requires_bool_and_has_no_effect_on_invalid_input) ... ok
test_manifest_field_tampering_rejected (test_p092.UpdateTests.test_manifest_field_tampering_rejected) ... ok
test_manifest_matches_independent_hmac_calculation (test_p092.UpdateTests.test_manifest_matches_independent_hmac_calculation) ... ok
test_missing_extra_or_path_fields_rejected (test_p092.UpdateTests.test_missing_extra_or_path_fields_rejected) ... ok
test_payload_contract (test_p092.UpdateTests.test_payload_contract) ... ok
test_payload_tampering_rejected_without_state_change (test_p092.UpdateTests.test_payload_tampering_rejected_without_state_change) ... ok
test_replay_after_apply_does_not_replace_previous (test_p092.UpdateTests.test_replay_after_apply_does_not_replace_previous) ... ok
test_rollback_once_does_not_toggle (test_p092.UpdateTests.test_rollback_once_does_not_toggle) ... ok
test_rollback_preserves_high_watermark_against_replay (test_p092.UpdateTests.test_rollback_preserves_high_watermark_against_replay) ... ok
test_secret_contract (test_p092.UpdateTests.test_secret_contract) ... ok
test_serialization_key_order_does_not_change_verification (test_p092.UpdateTests.test_serialization_key_order_does_not_change_verification) ... ok
test_valid_update_stores_version_and_payload (test_p092.UpdateTests.test_valid_update_stores_version_and_payload) ... ok
test_version_boundaries_are_inclusive (test_p092.UpdateTests.test_version_boundaries_are_inclusive) ... ok
test_versions_reject_bool_nan_fraction_and_out_of_range (test_p092.UpdateTests.test_versions_reject_bool_nan_fraction_and_out_of_range) ... ok
test_wrong_key_rejected (test_p092.UpdateTests.test_wrong_key_rejected) ... ok

----------------------------------------------------------------------
Ran 22 tests in 0.003s

OK
```

**stderr** — [file TXT](streams/ubuntu-latest-python-3.12.stderr.txt)

Il processo non ha emesso byte su stderr. Il file collegato è vuoto (0 byte).

### ubuntu-latest-python-3.13

Artifact: `output-p081-p100-ubuntu-latest-python-3.13` (ID `12476095990`). [Summary originale](../ambienti/ubuntu-latest-python-3.13.summary.json).

OS: `Linux` · piattaforma: `Linux-6.17.0-1022-azure-x86_64-with-glibc2.39` · Python: `3.13.16 (main, Oct  1 2026, 02:37:54) [GCC 13.3.0]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **22** · skipped: `0`.

**stdout** — [file TXT](streams/ubuntu-latest-python-3.13.stdout.txt)

```text
test_audit_is_copied_and_excludes_shared_secret (test_p092.UpdateTests.test_audit_is_copied_and_excludes_shared_secret) ... ok
test_demo_reports_simulated_rollback_and_replay_rejection (test_p092.UpdateTests.test_demo_reports_simulated_rollback_and_replay_rejection) ... ok
test_device_constructor_validation (test_p092.UpdateTests.test_device_constructor_validation) ... ok
test_digest_types_lengths_and_non_ascii_rejected (test_p092.UpdateTests.test_digest_types_lengths_and_non_ascii_rejected) ... ok
test_equal_older_or_invalid_current_version_rejected (test_p092.UpdateTests.test_equal_older_or_invalid_current_version_rejected) ... ok
test_health_failure_does_not_consume_version (test_p092.UpdateTests.test_health_failure_does_not_consume_version) ... ok
test_health_failure_restores_complete_modeled_snapshot (test_p092.UpdateTests.test_health_failure_restores_complete_modeled_snapshot) ... ok
test_health_requires_bool_and_has_no_effect_on_invalid_input (test_p092.UpdateTests.test_health_requires_bool_and_has_no_effect_on_invalid_input) ... ok
test_manifest_field_tampering_rejected (test_p092.UpdateTests.test_manifest_field_tampering_rejected) ... ok
test_manifest_matches_independent_hmac_calculation (test_p092.UpdateTests.test_manifest_matches_independent_hmac_calculation) ... ok
test_missing_extra_or_path_fields_rejected (test_p092.UpdateTests.test_missing_extra_or_path_fields_rejected) ... ok
test_payload_contract (test_p092.UpdateTests.test_payload_contract) ... ok
test_payload_tampering_rejected_without_state_change (test_p092.UpdateTests.test_payload_tampering_rejected_without_state_change) ... ok
test_replay_after_apply_does_not_replace_previous (test_p092.UpdateTests.test_replay_after_apply_does_not_replace_previous) ... ok
test_rollback_once_does_not_toggle (test_p092.UpdateTests.test_rollback_once_does_not_toggle) ... ok
test_rollback_preserves_high_watermark_against_replay (test_p092.UpdateTests.test_rollback_preserves_high_watermark_against_replay) ... ok
test_secret_contract (test_p092.UpdateTests.test_secret_contract) ... ok
test_serialization_key_order_does_not_change_verification (test_p092.UpdateTests.test_serialization_key_order_does_not_change_verification) ... ok
test_valid_update_stores_version_and_payload (test_p092.UpdateTests.test_valid_update_stores_version_and_payload) ... ok
test_version_boundaries_are_inclusive (test_p092.UpdateTests.test_version_boundaries_are_inclusive) ... ok
test_versions_reject_bool_nan_fraction_and_out_of_range (test_p092.UpdateTests.test_versions_reject_bool_nan_fraction_and_out_of_range) ... ok
test_wrong_key_rejected (test_p092.UpdateTests.test_wrong_key_rejected) ... ok

----------------------------------------------------------------------
Ran 22 tests in 0.003s

OK
```

**stderr** — [file TXT](streams/ubuntu-latest-python-3.13.stderr.txt)

Il processo non ha emesso byte su stderr. Il file collegato è vuoto (0 byte).

### windows-latest-python-3.12

Artifact: `output-p081-p100-windows-latest-python-3.12` (ID `12475927047`). [Summary originale](../ambienti/windows-latest-python-3.12.summary.json).

OS: `Windows` · piattaforma: `Windows-2025Server-10.0.26100-SP0` · Python: `3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **22** · skipped: `0`.

**stdout** — [file TXT](streams/windows-latest-python-3.12.stdout.txt)

```text
test_audit_is_copied_and_excludes_shared_secret (test_p092.UpdateTests.test_audit_is_copied_and_excludes_shared_secret) ... ok
test_demo_reports_simulated_rollback_and_replay_rejection (test_p092.UpdateTests.test_demo_reports_simulated_rollback_and_replay_rejection) ... ok
test_device_constructor_validation (test_p092.UpdateTests.test_device_constructor_validation) ... ok
test_digest_types_lengths_and_non_ascii_rejected (test_p092.UpdateTests.test_digest_types_lengths_and_non_ascii_rejected) ... ok
test_equal_older_or_invalid_current_version_rejected (test_p092.UpdateTests.test_equal_older_or_invalid_current_version_rejected) ... ok
test_health_failure_does_not_consume_version (test_p092.UpdateTests.test_health_failure_does_not_consume_version) ... ok
test_health_failure_restores_complete_modeled_snapshot (test_p092.UpdateTests.test_health_failure_restores_complete_modeled_snapshot) ... ok
test_health_requires_bool_and_has_no_effect_on_invalid_input (test_p092.UpdateTests.test_health_requires_bool_and_has_no_effect_on_invalid_input) ... ok
test_manifest_field_tampering_rejected (test_p092.UpdateTests.test_manifest_field_tampering_rejected) ... ok
test_manifest_matches_independent_hmac_calculation (test_p092.UpdateTests.test_manifest_matches_independent_hmac_calculation) ... ok
test_missing_extra_or_path_fields_rejected (test_p092.UpdateTests.test_missing_extra_or_path_fields_rejected) ... ok
test_payload_contract (test_p092.UpdateTests.test_payload_contract) ... ok
test_payload_tampering_rejected_without_state_change (test_p092.UpdateTests.test_payload_tampering_rejected_without_state_change) ... ok
test_replay_after_apply_does_not_replace_previous (test_p092.UpdateTests.test_replay_after_apply_does_not_replace_previous) ... ok
test_rollback_once_does_not_toggle (test_p092.UpdateTests.test_rollback_once_does_not_toggle) ... ok
test_rollback_preserves_high_watermark_against_replay (test_p092.UpdateTests.test_rollback_preserves_high_watermark_against_replay) ... ok
test_secret_contract (test_p092.UpdateTests.test_secret_contract) ... ok
test_serialization_key_order_does_not_change_verification (test_p092.UpdateTests.test_serialization_key_order_does_not_change_verification) ... ok
test_valid_update_stores_version_and_payload (test_p092.UpdateTests.test_valid_update_stores_version_and_payload) ... ok
test_version_boundaries_are_inclusive (test_p092.UpdateTests.test_version_boundaries_are_inclusive) ... ok
test_versions_reject_bool_nan_fraction_and_out_of_range (test_p092.UpdateTests.test_versions_reject_bool_nan_fraction_and_out_of_range) ... ok
test_wrong_key_rejected (test_p092.UpdateTests.test_wrong_key_rejected) ... ok

----------------------------------------------------------------------
Ran 22 tests in 0.002s

OK
```

**stderr** — [file TXT](streams/windows-latest-python-3.12.stderr.txt)

Il processo non ha emesso byte su stderr. Il file collegato è vuoto (0 byte).

### windows-latest-python-3.13

Artifact: `output-p081-p100-windows-latest-python-3.13` (ID `12475826902`). [Summary originale](../ambienti/windows-latest-python-3.13.summary.json).

OS: `Windows` · piattaforma: `Windows-2025Server-10.0.26100-SP0` · Python: `3.13.16 (tags/v3.13.16:cbc944f, Sep 30 2026, 19:17:50) [MSC v.1944 64 bit (AMD64)]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **22** · skipped: `0`.

**stdout** — [file TXT](streams/windows-latest-python-3.13.stdout.txt)

```text
test_audit_is_copied_and_excludes_shared_secret (test_p092.UpdateTests.test_audit_is_copied_and_excludes_shared_secret) ... ok
test_demo_reports_simulated_rollback_and_replay_rejection (test_p092.UpdateTests.test_demo_reports_simulated_rollback_and_replay_rejection) ... ok
test_device_constructor_validation (test_p092.UpdateTests.test_device_constructor_validation) ... ok
test_digest_types_lengths_and_non_ascii_rejected (test_p092.UpdateTests.test_digest_types_lengths_and_non_ascii_rejected) ... ok
test_equal_older_or_invalid_current_version_rejected (test_p092.UpdateTests.test_equal_older_or_invalid_current_version_rejected) ... ok
test_health_failure_does_not_consume_version (test_p092.UpdateTests.test_health_failure_does_not_consume_version) ... ok
test_health_failure_restores_complete_modeled_snapshot (test_p092.UpdateTests.test_health_failure_restores_complete_modeled_snapshot) ... ok
test_health_requires_bool_and_has_no_effect_on_invalid_input (test_p092.UpdateTests.test_health_requires_bool_and_has_no_effect_on_invalid_input) ... ok
test_manifest_field_tampering_rejected (test_p092.UpdateTests.test_manifest_field_tampering_rejected) ... ok
test_manifest_matches_independent_hmac_calculation (test_p092.UpdateTests.test_manifest_matches_independent_hmac_calculation) ... ok
test_missing_extra_or_path_fields_rejected (test_p092.UpdateTests.test_missing_extra_or_path_fields_rejected) ... ok
test_payload_contract (test_p092.UpdateTests.test_payload_contract) ... ok
test_payload_tampering_rejected_without_state_change (test_p092.UpdateTests.test_payload_tampering_rejected_without_state_change) ... ok
test_replay_after_apply_does_not_replace_previous (test_p092.UpdateTests.test_replay_after_apply_does_not_replace_previous) ... ok
test_rollback_once_does_not_toggle (test_p092.UpdateTests.test_rollback_once_does_not_toggle) ... ok
test_rollback_preserves_high_watermark_against_replay (test_p092.UpdateTests.test_rollback_preserves_high_watermark_against_replay) ... ok
test_secret_contract (test_p092.UpdateTests.test_secret_contract) ... ok
test_serialization_key_order_does_not_change_verification (test_p092.UpdateTests.test_serialization_key_order_does_not_change_verification) ... ok
test_valid_update_stores_version_and_payload (test_p092.UpdateTests.test_valid_update_stores_version_and_payload) ... ok
test_version_boundaries_are_inclusive (test_p092.UpdateTests.test_version_boundaries_are_inclusive) ... ok
test_versions_reject_bool_nan_fraction_and_out_of_range (test_p092.UpdateTests.test_versions_reject_bool_nan_fraction_and_out_of_range) ... ok
test_wrong_key_rejected (test_p092.UpdateTests.test_wrong_key_rejected) ... ok

----------------------------------------------------------------------
Ran 22 tests in 0.002s

OK
```

**stderr** — [file TXT](streams/windows-latest-python-3.13.stderr.txt)

Il processo non ha emesso byte su stderr. Il file collegato è vuoto (0 byte).

## Demo e controlli runtime

Questa matrice esegue le suite `run_tests.py`. Le summary non classificano processi separati come demo o controlli runtime: non sono aggiunti output o esiti di tali categorie.

## Verifica e provenienza

[Registro strutturato](registro.json) · [Hash e trasformazioni](MANIFEST.json) · [Policy](../AUDIT.md) · [Indice](../README.md)
