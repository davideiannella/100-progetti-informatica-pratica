# P085: output dei collaudi

[Indice dei collaudi](../README.md) · [Codice e istruzioni](../../projects/P085/README.md)

Esito registrato: **PASS in tutte le quattro combinazioni**. [Run 39893701054](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39893701054) · commit `3ab7bdfedb20a443bd71fe4e4ffe3c1dd67bd707`.

Comando effettivo del [runner a quel commit](https://github.com/davideiannella/100-progetti-informatica-pratica/blob/3ab7bdfedb20a443bd71fe4e4ffe3c1dd67bd707/tools/collaudo_p081_p100.py): `[sys.executable, "-B", "run_tests.py"]`, con directory di lavoro `projects/P085`. `sys.executable` indica l’interprete della combinazione riportata sotto; il suo percorso host assoluto non è registrato nella summary.

I quattro rapporti sono output CI preesistenti, non nuove esecuzioni preparate per questa pagina. Ogni ambiente ha verificato gli hash dei 299 sorgenti, compilato 60 file Python e completato 20 suite per 377 metodi complessivi.

`unittest` scrive normalmente il rapporto dettagliato su **stderr**: questo non equivale a un errore. I nomi e gli esiti sotto provengono dalle righe effettivamente emesse; non sono stati ricostruiti dal codice. I TXT mantengono i byte e i terminatori originali, compreso CRLF su Windows; i blocchi Markdown normalizzano soltanto i terminatori.

## Suite — quattro ambienti CI

### ubuntu-latest-python-3.12

Artifact: `output-p081-p100-ubuntu-latest-python-3.12` (ID `12476170749`). [Summary originale](../ambienti/ubuntu-latest-python-3.12.summary.json).

OS: `Linux` · piattaforma: `Linux-6.17.0-1022-azure-x86_64-with-glibc2.39` · Python: `3.12.15 (main, Oct  1 2026, 02:35:59) [GCC 13.3.0]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **17** · skipped: `0`.

**stdout** — [file TXT](streams/ubuntu-latest-python-3.12.stdout.txt)

Il processo non ha emesso byte su stdout. Il file collegato è vuoto (0 byte).

**stderr** — [file TXT](streams/ubuntu-latest-python-3.12.stderr.txt)

```text
test_audit_snapshot_and_policy_are_protected (test_p085.AccessTest.test_audit_snapshot_and_policy_are_protected) ... ok
test_badge_fields_are_validated (test_p085.AccessTest.test_badge_fields_are_validated) ... ok
test_badge_is_frozen (test_p085.AccessTest.test_badge_is_frozen) ... ok
test_demo_totals_and_reasons (test_p085.AccessTest.test_demo_totals_and_reasons) ... ok
test_duplicate_attempts_and_call_order_are_preserved (test_p085.AccessTest.test_duplicate_attempts_and_call_order_are_preserved) ... ok
test_duplicate_cannot_replace_privileges (test_p085.AccessTest.test_duplicate_cannot_replace_privileges) ... ok
test_inactive_badge_is_denied (test_p085.AccessTest.test_inactive_badge_is_denied) ... ok
test_invalid_timestamp_is_rejected_before_audit (test_p085.AccessTest.test_invalid_timestamp_is_rejected_before_audit) ... ok
test_length_boundaries (test_p085.AccessTest.test_length_boundaries) ... ok
test_malformed_request_does_not_modify_state (test_p085.AccessTest.test_malformed_request_does_not_modify_state) ... ok
test_permission_matrix (test_p085.AccessTest.test_permission_matrix) ... ok
test_registration_requires_badge (test_p085.AccessTest.test_registration_requires_badge) ... ok
test_revoke_changes_future_decisions_and_is_idempotent (test_p085.AccessTest.test_revoke_changes_future_decisions_and_is_idempotent) ... ok
test_revoke_unknown_does_not_create_badge (test_p085.AccessTest.test_revoke_unknown_does_not_create_badge) ... ok
test_trimmed_identifier_collision_is_rejected (test_p085.AccessTest.test_trimmed_identifier_collision_is_rejected) ... ok
test_unknown_badge_is_audited (test_p085.AccessTest.test_unknown_badge_is_audited) ... ok
test_unknown_zone_has_distinct_reason (test_p085.AccessTest.test_unknown_zone_has_distinct_reason) ... ok

----------------------------------------------------------------------
Ran 17 tests in 0.002s

OK
```

### ubuntu-latest-python-3.13

Artifact: `output-p081-p100-ubuntu-latest-python-3.13` (ID `12476095990`). [Summary originale](../ambienti/ubuntu-latest-python-3.13.summary.json).

OS: `Linux` · piattaforma: `Linux-6.17.0-1022-azure-x86_64-with-glibc2.39` · Python: `3.13.16 (main, Oct  1 2026, 02:37:54) [GCC 13.3.0]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **17** · skipped: `0`.

**stdout** — [file TXT](streams/ubuntu-latest-python-3.13.stdout.txt)

Il processo non ha emesso byte su stdout. Il file collegato è vuoto (0 byte).

**stderr** — [file TXT](streams/ubuntu-latest-python-3.13.stderr.txt)

```text
test_audit_snapshot_and_policy_are_protected (test_p085.AccessTest.test_audit_snapshot_and_policy_are_protected) ... ok
test_badge_fields_are_validated (test_p085.AccessTest.test_badge_fields_are_validated) ... ok
test_badge_is_frozen (test_p085.AccessTest.test_badge_is_frozen) ... ok
test_demo_totals_and_reasons (test_p085.AccessTest.test_demo_totals_and_reasons) ... ok
test_duplicate_attempts_and_call_order_are_preserved (test_p085.AccessTest.test_duplicate_attempts_and_call_order_are_preserved) ... ok
test_duplicate_cannot_replace_privileges (test_p085.AccessTest.test_duplicate_cannot_replace_privileges) ... ok
test_inactive_badge_is_denied (test_p085.AccessTest.test_inactive_badge_is_denied) ... ok
test_invalid_timestamp_is_rejected_before_audit (test_p085.AccessTest.test_invalid_timestamp_is_rejected_before_audit) ... ok
test_length_boundaries (test_p085.AccessTest.test_length_boundaries) ... ok
test_malformed_request_does_not_modify_state (test_p085.AccessTest.test_malformed_request_does_not_modify_state) ... ok
test_permission_matrix (test_p085.AccessTest.test_permission_matrix) ... ok
test_registration_requires_badge (test_p085.AccessTest.test_registration_requires_badge) ... ok
test_revoke_changes_future_decisions_and_is_idempotent (test_p085.AccessTest.test_revoke_changes_future_decisions_and_is_idempotent) ... ok
test_revoke_unknown_does_not_create_badge (test_p085.AccessTest.test_revoke_unknown_does_not_create_badge) ... ok
test_trimmed_identifier_collision_is_rejected (test_p085.AccessTest.test_trimmed_identifier_collision_is_rejected) ... ok
test_unknown_badge_is_audited (test_p085.AccessTest.test_unknown_badge_is_audited) ... ok
test_unknown_zone_has_distinct_reason (test_p085.AccessTest.test_unknown_zone_has_distinct_reason) ... ok

----------------------------------------------------------------------
Ran 17 tests in 0.002s

OK
```

### windows-latest-python-3.12

Artifact: `output-p081-p100-windows-latest-python-3.12` (ID `12475927047`). [Summary originale](../ambienti/windows-latest-python-3.12.summary.json).

OS: `Windows` · piattaforma: `Windows-2025Server-10.0.26100-SP0` · Python: `3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **17** · skipped: `0`.

**stdout** — [file TXT](streams/windows-latest-python-3.12.stdout.txt)

Il processo non ha emesso byte su stdout. Il file collegato è vuoto (0 byte).

**stderr** — [file TXT](streams/windows-latest-python-3.12.stderr.txt)

```text
test_audit_snapshot_and_policy_are_protected (test_p085.AccessTest.test_audit_snapshot_and_policy_are_protected) ... ok
test_badge_fields_are_validated (test_p085.AccessTest.test_badge_fields_are_validated) ... ok
test_badge_is_frozen (test_p085.AccessTest.test_badge_is_frozen) ... ok
test_demo_totals_and_reasons (test_p085.AccessTest.test_demo_totals_and_reasons) ... ok
test_duplicate_attempts_and_call_order_are_preserved (test_p085.AccessTest.test_duplicate_attempts_and_call_order_are_preserved) ... ok
test_duplicate_cannot_replace_privileges (test_p085.AccessTest.test_duplicate_cannot_replace_privileges) ... ok
test_inactive_badge_is_denied (test_p085.AccessTest.test_inactive_badge_is_denied) ... ok
test_invalid_timestamp_is_rejected_before_audit (test_p085.AccessTest.test_invalid_timestamp_is_rejected_before_audit) ... ok
test_length_boundaries (test_p085.AccessTest.test_length_boundaries) ... ok
test_malformed_request_does_not_modify_state (test_p085.AccessTest.test_malformed_request_does_not_modify_state) ... ok
test_permission_matrix (test_p085.AccessTest.test_permission_matrix) ... ok
test_registration_requires_badge (test_p085.AccessTest.test_registration_requires_badge) ... ok
test_revoke_changes_future_decisions_and_is_idempotent (test_p085.AccessTest.test_revoke_changes_future_decisions_and_is_idempotent) ... ok
test_revoke_unknown_does_not_create_badge (test_p085.AccessTest.test_revoke_unknown_does_not_create_badge) ... ok
test_trimmed_identifier_collision_is_rejected (test_p085.AccessTest.test_trimmed_identifier_collision_is_rejected) ... ok
test_unknown_badge_is_audited (test_p085.AccessTest.test_unknown_badge_is_audited) ... ok
test_unknown_zone_has_distinct_reason (test_p085.AccessTest.test_unknown_zone_has_distinct_reason) ... ok

----------------------------------------------------------------------
Ran 17 tests in 0.002s

OK
```

### windows-latest-python-3.13

Artifact: `output-p081-p100-windows-latest-python-3.13` (ID `12475826902`). [Summary originale](../ambienti/windows-latest-python-3.13.summary.json).

OS: `Windows` · piattaforma: `Windows-2025Server-10.0.26100-SP0` · Python: `3.13.16 (tags/v3.13.16:cbc944f, Sep 30 2026, 19:17:50) [MSC v.1944 64 bit (AMD64)]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **17** · skipped: `0`.

**stdout** — [file TXT](streams/windows-latest-python-3.13.stdout.txt)

Il processo non ha emesso byte su stdout. Il file collegato è vuoto (0 byte).

**stderr** — [file TXT](streams/windows-latest-python-3.13.stderr.txt)

```text
test_audit_snapshot_and_policy_are_protected (test_p085.AccessTest.test_audit_snapshot_and_policy_are_protected) ... ok
test_badge_fields_are_validated (test_p085.AccessTest.test_badge_fields_are_validated) ... ok
test_badge_is_frozen (test_p085.AccessTest.test_badge_is_frozen) ... ok
test_demo_totals_and_reasons (test_p085.AccessTest.test_demo_totals_and_reasons) ... ok
test_duplicate_attempts_and_call_order_are_preserved (test_p085.AccessTest.test_duplicate_attempts_and_call_order_are_preserved) ... ok
test_duplicate_cannot_replace_privileges (test_p085.AccessTest.test_duplicate_cannot_replace_privileges) ... ok
test_inactive_badge_is_denied (test_p085.AccessTest.test_inactive_badge_is_denied) ... ok
test_invalid_timestamp_is_rejected_before_audit (test_p085.AccessTest.test_invalid_timestamp_is_rejected_before_audit) ... ok
test_length_boundaries (test_p085.AccessTest.test_length_boundaries) ... ok
test_malformed_request_does_not_modify_state (test_p085.AccessTest.test_malformed_request_does_not_modify_state) ... ok
test_permission_matrix (test_p085.AccessTest.test_permission_matrix) ... ok
test_registration_requires_badge (test_p085.AccessTest.test_registration_requires_badge) ... ok
test_revoke_changes_future_decisions_and_is_idempotent (test_p085.AccessTest.test_revoke_changes_future_decisions_and_is_idempotent) ... ok
test_revoke_unknown_does_not_create_badge (test_p085.AccessTest.test_revoke_unknown_does_not_create_badge) ... ok
test_trimmed_identifier_collision_is_rejected (test_p085.AccessTest.test_trimmed_identifier_collision_is_rejected) ... ok
test_unknown_badge_is_audited (test_p085.AccessTest.test_unknown_badge_is_audited) ... ok
test_unknown_zone_has_distinct_reason (test_p085.AccessTest.test_unknown_zone_has_distinct_reason) ... ok

----------------------------------------------------------------------
Ran 17 tests in 0.001s

OK
```

## Demo e controlli runtime

Questa matrice esegue le suite `run_tests.py`. Le summary non classificano processi separati come demo o controlli runtime: non sono aggiunti output o esiti di tali categorie.

## Verifica e provenienza

[Registro strutturato](registro.json) · [Hash e trasformazioni](MANIFEST.json) · [Policy](../AUDIT.md) · [Indice](../README.md)
