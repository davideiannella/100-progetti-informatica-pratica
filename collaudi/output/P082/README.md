# P082 — output reali dei collaudi

Esito registrato: **PASS in tutte le quattro combinazioni**. [Run 39893701054](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39893701054) · commit `3ab7bdfedb20a443bd71fe4e4ffe3c1dd67bd707`.

Comando effettivo del [runner a quel commit](https://github.com/davideiannella/100-progetti-informatica-pratica/blob/3ab7bdfedb20a443bd71fe4e4ffe3c1dd67bd707/tools/collaudo_p081_p100.py): `[sys.executable, "-B", "run_tests.py"]`, con directory di lavoro `projects/P082`. `sys.executable` indica l’interprete della combinazione riportata sotto; il suo percorso host assoluto non è registrato nella summary.

I quattro rapporti sono output CI preesistenti, non nuove esecuzioni preparate per questa pagina. Ogni ambiente ha verificato gli hash dei 299 sorgenti, compilato 60 file Python e completato 20 suite per 377 metodi complessivi.

`unittest` scrive normalmente il rapporto dettagliato su **stderr**: questo non equivale a un errore. I nomi e gli esiti sotto provengono dalle righe effettivamente emesse; non sono stati ricostruiti dal codice. I TXT mantengono i byte e i terminatori originali, compreso CRLF su Windows; i blocchi Markdown normalizzano soltanto i terminatori.

## Suite — quattro ambienti CI

### ubuntu-latest-python-3.12

Artifact: `output-p081-p100-ubuntu-latest-python-3.12` (ID `12476170749`). [Summary originale](../ambienti/ubuntu-latest-python-3.12.summary.json).

OS: `Linux` · piattaforma: `Linux-6.17.0-1022-azure-x86_64-with-glibc2.39` · Python: `3.12.15 (main, Oct  1 2026, 02:35:59) [GCC 13.3.0]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **12** · skipped: `0`.

**stdout** — [file TXT](streams/ubuntu-latest-python-3.12.stdout.txt)

Il processo non ha emesso byte su stdout. Il file collegato è vuoto (0 byte).

**stderr** — [file TXT](streams/ubuntu-latest-python-3.12.stderr.txt)

```text
test_demo_reports_two_operational_gaps (test_p082.GovernanceTest.test_demo_reports_two_operational_gaps) ... ok
test_empty_lists_every_control_in_stable_order (test_p082.GovernanceTest.test_empty_lists_every_control_in_stable_order) ... ok
test_false_and_absent_are_missing (test_p082.GovernanceTest.test_false_and_absent_are_missing) ... ok
test_full_checklist_only (test_p082.GovernanceTest.test_full_checklist_only) ... ok
test_input_is_not_modified_and_missing_is_fresh (test_p082.GovernanceTest.test_input_is_not_modified_and_missing_is_fresh) ... ok
test_input_order_does_not_change_report_order (test_p082.GovernanceTest.test_input_order_does_not_change_report_order) ... ok
test_non_mapping_rejected (test_p082.GovernanceTest.test_non_mapping_rejected) ... ok
test_record_length_boundary (test_p082.GovernanceTest.test_record_length_boundary) ... ok
test_record_rejects_each_missing_or_invalid_field (test_p082.GovernanceTest.test_record_rejects_each_missing_or_invalid_field) ... ok
test_record_trims_all_fields (test_p082.GovernanceTest.test_record_trims_all_fields) ... ok
test_truthy_non_booleans_are_rejected (test_p082.GovernanceTest.test_truthy_non_booleans_are_rejected) ... ok
test_unknown_key_catches_typo (test_p082.GovernanceTest.test_unknown_key_catches_typo) ... ok

----------------------------------------------------------------------
Ran 12 tests in 0.001s

OK
```

### ubuntu-latest-python-3.13

Artifact: `output-p081-p100-ubuntu-latest-python-3.13` (ID `12476095990`). [Summary originale](../ambienti/ubuntu-latest-python-3.13.summary.json).

OS: `Linux` · piattaforma: `Linux-6.17.0-1022-azure-x86_64-with-glibc2.39` · Python: `3.13.16 (main, Oct  1 2026, 02:37:54) [GCC 13.3.0]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **12** · skipped: `0`.

**stdout** — [file TXT](streams/ubuntu-latest-python-3.13.stdout.txt)

Il processo non ha emesso byte su stdout. Il file collegato è vuoto (0 byte).

**stderr** — [file TXT](streams/ubuntu-latest-python-3.13.stderr.txt)

```text
test_demo_reports_two_operational_gaps (test_p082.GovernanceTest.test_demo_reports_two_operational_gaps) ... ok
test_empty_lists_every_control_in_stable_order (test_p082.GovernanceTest.test_empty_lists_every_control_in_stable_order) ... ok
test_false_and_absent_are_missing (test_p082.GovernanceTest.test_false_and_absent_are_missing) ... ok
test_full_checklist_only (test_p082.GovernanceTest.test_full_checklist_only) ... ok
test_input_is_not_modified_and_missing_is_fresh (test_p082.GovernanceTest.test_input_is_not_modified_and_missing_is_fresh) ... ok
test_input_order_does_not_change_report_order (test_p082.GovernanceTest.test_input_order_does_not_change_report_order) ... ok
test_non_mapping_rejected (test_p082.GovernanceTest.test_non_mapping_rejected) ... ok
test_record_length_boundary (test_p082.GovernanceTest.test_record_length_boundary) ... ok
test_record_rejects_each_missing_or_invalid_field (test_p082.GovernanceTest.test_record_rejects_each_missing_or_invalid_field) ... ok
test_record_trims_all_fields (test_p082.GovernanceTest.test_record_trims_all_fields) ... ok
test_truthy_non_booleans_are_rejected (test_p082.GovernanceTest.test_truthy_non_booleans_are_rejected) ... ok
test_unknown_key_catches_typo (test_p082.GovernanceTest.test_unknown_key_catches_typo) ... ok

----------------------------------------------------------------------
Ran 12 tests in 0.001s

OK
```

### windows-latest-python-3.12

Artifact: `output-p081-p100-windows-latest-python-3.12` (ID `12475927047`). [Summary originale](../ambienti/windows-latest-python-3.12.summary.json).

OS: `Windows` · piattaforma: `Windows-2025Server-10.0.26100-SP0` · Python: `3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **12** · skipped: `0`.

**stdout** — [file TXT](streams/windows-latest-python-3.12.stdout.txt)

Il processo non ha emesso byte su stdout. Il file collegato è vuoto (0 byte).

**stderr** — [file TXT](streams/windows-latest-python-3.12.stderr.txt)

```text
test_demo_reports_two_operational_gaps (test_p082.GovernanceTest.test_demo_reports_two_operational_gaps) ... ok
test_empty_lists_every_control_in_stable_order (test_p082.GovernanceTest.test_empty_lists_every_control_in_stable_order) ... ok
test_false_and_absent_are_missing (test_p082.GovernanceTest.test_false_and_absent_are_missing) ... ok
test_full_checklist_only (test_p082.GovernanceTest.test_full_checklist_only) ... ok
test_input_is_not_modified_and_missing_is_fresh (test_p082.GovernanceTest.test_input_is_not_modified_and_missing_is_fresh) ... ok
test_input_order_does_not_change_report_order (test_p082.GovernanceTest.test_input_order_does_not_change_report_order) ... ok
test_non_mapping_rejected (test_p082.GovernanceTest.test_non_mapping_rejected) ... ok
test_record_length_boundary (test_p082.GovernanceTest.test_record_length_boundary) ... ok
test_record_rejects_each_missing_or_invalid_field (test_p082.GovernanceTest.test_record_rejects_each_missing_or_invalid_field) ... ok
test_record_trims_all_fields (test_p082.GovernanceTest.test_record_trims_all_fields) ... ok
test_truthy_non_booleans_are_rejected (test_p082.GovernanceTest.test_truthy_non_booleans_are_rejected) ... ok
test_unknown_key_catches_typo (test_p082.GovernanceTest.test_unknown_key_catches_typo) ... ok

----------------------------------------------------------------------
Ran 12 tests in 0.001s

OK
```

### windows-latest-python-3.13

Artifact: `output-p081-p100-windows-latest-python-3.13` (ID `12475826902`). [Summary originale](../ambienti/windows-latest-python-3.13.summary.json).

OS: `Windows` · piattaforma: `Windows-2025Server-10.0.26100-SP0` · Python: `3.13.16 (tags/v3.13.16:cbc944f, Sep 30 2026, 19:17:50) [MSC v.1944 64 bit (AMD64)]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **12** · skipped: `0`.

**stdout** — [file TXT](streams/windows-latest-python-3.13.stdout.txt)

Il processo non ha emesso byte su stdout. Il file collegato è vuoto (0 byte).

**stderr** — [file TXT](streams/windows-latest-python-3.13.stderr.txt)

```text
test_demo_reports_two_operational_gaps (test_p082.GovernanceTest.test_demo_reports_two_operational_gaps) ... ok
test_empty_lists_every_control_in_stable_order (test_p082.GovernanceTest.test_empty_lists_every_control_in_stable_order) ... ok
test_false_and_absent_are_missing (test_p082.GovernanceTest.test_false_and_absent_are_missing) ... ok
test_full_checklist_only (test_p082.GovernanceTest.test_full_checklist_only) ... ok
test_input_is_not_modified_and_missing_is_fresh (test_p082.GovernanceTest.test_input_is_not_modified_and_missing_is_fresh) ... ok
test_input_order_does_not_change_report_order (test_p082.GovernanceTest.test_input_order_does_not_change_report_order) ... ok
test_non_mapping_rejected (test_p082.GovernanceTest.test_non_mapping_rejected) ... ok
test_record_length_boundary (test_p082.GovernanceTest.test_record_length_boundary) ... ok
test_record_rejects_each_missing_or_invalid_field (test_p082.GovernanceTest.test_record_rejects_each_missing_or_invalid_field) ... ok
test_record_trims_all_fields (test_p082.GovernanceTest.test_record_trims_all_fields) ... ok
test_truthy_non_booleans_are_rejected (test_p082.GovernanceTest.test_truthy_non_booleans_are_rejected) ... ok
test_unknown_key_catches_typo (test_p082.GovernanceTest.test_unknown_key_catches_typo) ... ok

----------------------------------------------------------------------
Ran 12 tests in 0.001s

OK
```

## Demo e controlli runtime

Questa matrice esegue le suite `run_tests.py`. Le summary non classificano processi separati come demo o controlli runtime: non sono aggiunti output o esiti di tali categorie.

## Verifica e provenienza

[Registro strutturato](registro.json) · [Hash e trasformazioni](MANIFEST.json) · [Policy](../AUDIT.md) · [Indice](../README.md)
