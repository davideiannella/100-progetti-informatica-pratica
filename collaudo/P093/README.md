# P093: output dei collaudi

[Indice dei collaudi](../README.md) · [Codice e istruzioni](../../projects/P093/README.md)

Esito registrato: **PASS in tutte le quattro combinazioni**. [Run 39893701054](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39893701054) · commit `3ab7bdfedb20a443bd71fe4e4ffe3c1dd67bd707`.

Comando effettivo del [runner a quel commit](https://github.com/davideiannella/100-progetti-informatica-pratica/blob/3ab7bdfedb20a443bd71fe4e4ffe3c1dd67bd707/tools/collaudo_p081_p100.py): `[sys.executable, "-B", "run_tests.py"]`, con directory di lavoro `projects/P093`. `sys.executable` indica l’interprete della combinazione riportata sotto; il suo percorso host assoluto non è registrato nella summary.

I quattro rapporti sono output CI preesistenti, non nuove esecuzioni preparate per questa pagina. Ogni ambiente ha verificato gli hash dei 299 sorgenti, compilato 60 file Python e completato 20 suite per 377 metodi complessivi.

`unittest` scrive normalmente il rapporto dettagliato su **stderr**: questo non equivale a un errore. I nomi e gli esiti sotto provengono dalle righe effettivamente emesse; non sono stati ricostruiti dal codice. I TXT mantengono i byte e i terminatori originali, compreso CRLF su Windows; i blocchi Markdown normalizzano soltanto i terminatori.

## Suite — quattro ambienti CI

### ubuntu-latest-python-3.12

Artifact: `output-p081-p100-ubuntu-latest-python-3.12` (ID `12476170749`). [Summary originale](../ambienti/ubuntu-latest-python-3.12.summary.json).

OS: `Linux` · piattaforma: `Linux-6.17.0-1022-azure-x86_64-with-glibc2.39` · Python: `3.12.15 (main, Oct  1 2026, 02:35:59) [GCC 13.3.0]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **22** · skipped: `0`.

**stdout** — [file TXT](streams/ubuntu-latest-python-3.12.stdout.txt)

```text
test_all_scrap_has_zero_quality (test_p093.FactoryTests.test_all_scrap_has_zero_quality) ... ok
test_count_contract_rejects_bool_float_and_out_of_range (test_p093.FactoryTests.test_count_contract_rejects_bool_float_and_out_of_range) ... ok
test_decimal_cycle_boundary_does_not_reject_float_rounding (test_p093.FactoryTests.test_decimal_cycle_boundary_does_not_reject_float_rounding) ... ok
test_decimal_planned_boundary_is_bounded_only_within_tolerance (test_p093.FactoryTests.test_decimal_planned_boundary_is_bounded_only_within_tolerance) ... ok
test_demo_reports_two_machines_and_one_rule_signal (test_p093.FactoryTests.test_demo_reports_two_machines_and_one_rule_signal) ... ok
test_empty_plant_has_no_mean (test_p093.FactoryTests.test_empty_plant_has_no_mean) ... ok
test_finite_numeric_fields_reject_nan_inf_bool_and_strings (test_p093.FactoryTests.test_finite_numeric_fields_reject_nan_inf_bool_and_strings) ... ok
test_impossible_cycle_or_zero_runtime_production_rejected (test_p093.FactoryTests.test_impossible_cycle_or_zero_runtime_production_rejected) ... ok
test_known_availability_performance_quality_and_oee (test_p093.FactoryTests.test_known_availability_performance_quality_and_oee) ... ok
test_maintenance_limit_must_be_finite_nonnegative (test_p093.FactoryTests.test_maintenance_limit_must_be_finite_nonnegative) ... ok
test_maintenance_threshold_is_strict (test_p093.FactoryTests.test_maintenance_threshold_is_strict) ... ok
test_mean_oee_is_arithmetic_not_a_weighted_plant_oee (test_p093.FactoryTests.test_mean_oee_is_arithmetic_not_a_weighted_plant_oee) ... ok
test_names_must_be_nonempty_bounded_strings (test_p093.FactoryTests.test_names_must_be_nonempty_bounded_strings) ... ok
test_negative_measurements_rejected (test_p093.FactoryTests.test_negative_measurements_rejected) ... ok
test_perfect_machine_at_upper_bound (test_p093.FactoryTests.test_perfect_machine_at_upper_bound) ... ok
test_plant_keeps_its_own_machine_sequence (test_p093.FactoryTests.test_plant_keeps_its_own_machine_sequence) ... ok
test_plant_rejects_duplicate_machine_names (test_p093.FactoryTests.test_plant_rejects_duplicate_machine_names) ... ok
test_plant_rejects_non_twin_members (test_p093.FactoryTests.test_plant_rejects_non_twin_members) ... ok
test_runtime_cannot_exceed_planned_time (test_p093.FactoryTests.test_runtime_cannot_exceed_planned_time) ... ok
test_runtime_without_production_has_zero_quality_by_convention (test_p093.FactoryTests.test_runtime_without_production_has_zero_quality_by_convention) ... ok
test_stopped_machine_has_zero_components (test_p093.FactoryTests.test_stopped_machine_has_zero_components) ... ok
test_validated_twin_is_immutable (test_p093.FactoryTests.test_validated_twin_is_immutable) ... ok

----------------------------------------------------------------------
Ran 22 tests in 0.002s

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
test_all_scrap_has_zero_quality (test_p093.FactoryTests.test_all_scrap_has_zero_quality) ... ok
test_count_contract_rejects_bool_float_and_out_of_range (test_p093.FactoryTests.test_count_contract_rejects_bool_float_and_out_of_range) ... ok
test_decimal_cycle_boundary_does_not_reject_float_rounding (test_p093.FactoryTests.test_decimal_cycle_boundary_does_not_reject_float_rounding) ... ok
test_decimal_planned_boundary_is_bounded_only_within_tolerance (test_p093.FactoryTests.test_decimal_planned_boundary_is_bounded_only_within_tolerance) ... ok
test_demo_reports_two_machines_and_one_rule_signal (test_p093.FactoryTests.test_demo_reports_two_machines_and_one_rule_signal) ... ok
test_empty_plant_has_no_mean (test_p093.FactoryTests.test_empty_plant_has_no_mean) ... ok
test_finite_numeric_fields_reject_nan_inf_bool_and_strings (test_p093.FactoryTests.test_finite_numeric_fields_reject_nan_inf_bool_and_strings) ... ok
test_impossible_cycle_or_zero_runtime_production_rejected (test_p093.FactoryTests.test_impossible_cycle_or_zero_runtime_production_rejected) ... ok
test_known_availability_performance_quality_and_oee (test_p093.FactoryTests.test_known_availability_performance_quality_and_oee) ... ok
test_maintenance_limit_must_be_finite_nonnegative (test_p093.FactoryTests.test_maintenance_limit_must_be_finite_nonnegative) ... ok
test_maintenance_threshold_is_strict (test_p093.FactoryTests.test_maintenance_threshold_is_strict) ... ok
test_mean_oee_is_arithmetic_not_a_weighted_plant_oee (test_p093.FactoryTests.test_mean_oee_is_arithmetic_not_a_weighted_plant_oee) ... ok
test_names_must_be_nonempty_bounded_strings (test_p093.FactoryTests.test_names_must_be_nonempty_bounded_strings) ... ok
test_negative_measurements_rejected (test_p093.FactoryTests.test_negative_measurements_rejected) ... ok
test_perfect_machine_at_upper_bound (test_p093.FactoryTests.test_perfect_machine_at_upper_bound) ... ok
test_plant_keeps_its_own_machine_sequence (test_p093.FactoryTests.test_plant_keeps_its_own_machine_sequence) ... ok
test_plant_rejects_duplicate_machine_names (test_p093.FactoryTests.test_plant_rejects_duplicate_machine_names) ... ok
test_plant_rejects_non_twin_members (test_p093.FactoryTests.test_plant_rejects_non_twin_members) ... ok
test_runtime_cannot_exceed_planned_time (test_p093.FactoryTests.test_runtime_cannot_exceed_planned_time) ... ok
test_runtime_without_production_has_zero_quality_by_convention (test_p093.FactoryTests.test_runtime_without_production_has_zero_quality_by_convention) ... ok
test_stopped_machine_has_zero_components (test_p093.FactoryTests.test_stopped_machine_has_zero_components) ... ok
test_validated_twin_is_immutable (test_p093.FactoryTests.test_validated_twin_is_immutable) ... ok

----------------------------------------------------------------------
Ran 22 tests in 0.002s

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
test_all_scrap_has_zero_quality (test_p093.FactoryTests.test_all_scrap_has_zero_quality) ... ok
test_count_contract_rejects_bool_float_and_out_of_range (test_p093.FactoryTests.test_count_contract_rejects_bool_float_and_out_of_range) ... ok
test_decimal_cycle_boundary_does_not_reject_float_rounding (test_p093.FactoryTests.test_decimal_cycle_boundary_does_not_reject_float_rounding) ... ok
test_decimal_planned_boundary_is_bounded_only_within_tolerance (test_p093.FactoryTests.test_decimal_planned_boundary_is_bounded_only_within_tolerance) ... ok
test_demo_reports_two_machines_and_one_rule_signal (test_p093.FactoryTests.test_demo_reports_two_machines_and_one_rule_signal) ... ok
test_empty_plant_has_no_mean (test_p093.FactoryTests.test_empty_plant_has_no_mean) ... ok
test_finite_numeric_fields_reject_nan_inf_bool_and_strings (test_p093.FactoryTests.test_finite_numeric_fields_reject_nan_inf_bool_and_strings) ... ok
test_impossible_cycle_or_zero_runtime_production_rejected (test_p093.FactoryTests.test_impossible_cycle_or_zero_runtime_production_rejected) ... ok
test_known_availability_performance_quality_and_oee (test_p093.FactoryTests.test_known_availability_performance_quality_and_oee) ... ok
test_maintenance_limit_must_be_finite_nonnegative (test_p093.FactoryTests.test_maintenance_limit_must_be_finite_nonnegative) ... ok
test_maintenance_threshold_is_strict (test_p093.FactoryTests.test_maintenance_threshold_is_strict) ... ok
test_mean_oee_is_arithmetic_not_a_weighted_plant_oee (test_p093.FactoryTests.test_mean_oee_is_arithmetic_not_a_weighted_plant_oee) ... ok
test_names_must_be_nonempty_bounded_strings (test_p093.FactoryTests.test_names_must_be_nonempty_bounded_strings) ... ok
test_negative_measurements_rejected (test_p093.FactoryTests.test_negative_measurements_rejected) ... ok
test_perfect_machine_at_upper_bound (test_p093.FactoryTests.test_perfect_machine_at_upper_bound) ... ok
test_plant_keeps_its_own_machine_sequence (test_p093.FactoryTests.test_plant_keeps_its_own_machine_sequence) ... ok
test_plant_rejects_duplicate_machine_names (test_p093.FactoryTests.test_plant_rejects_duplicate_machine_names) ... ok
test_plant_rejects_non_twin_members (test_p093.FactoryTests.test_plant_rejects_non_twin_members) ... ok
test_runtime_cannot_exceed_planned_time (test_p093.FactoryTests.test_runtime_cannot_exceed_planned_time) ... ok
test_runtime_without_production_has_zero_quality_by_convention (test_p093.FactoryTests.test_runtime_without_production_has_zero_quality_by_convention) ... ok
test_stopped_machine_has_zero_components (test_p093.FactoryTests.test_stopped_machine_has_zero_components) ... ok
test_validated_twin_is_immutable (test_p093.FactoryTests.test_validated_twin_is_immutable) ... ok

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
test_all_scrap_has_zero_quality (test_p093.FactoryTests.test_all_scrap_has_zero_quality) ... ok
test_count_contract_rejects_bool_float_and_out_of_range (test_p093.FactoryTests.test_count_contract_rejects_bool_float_and_out_of_range) ... ok
test_decimal_cycle_boundary_does_not_reject_float_rounding (test_p093.FactoryTests.test_decimal_cycle_boundary_does_not_reject_float_rounding) ... ok
test_decimal_planned_boundary_is_bounded_only_within_tolerance (test_p093.FactoryTests.test_decimal_planned_boundary_is_bounded_only_within_tolerance) ... ok
test_demo_reports_two_machines_and_one_rule_signal (test_p093.FactoryTests.test_demo_reports_two_machines_and_one_rule_signal) ... ok
test_empty_plant_has_no_mean (test_p093.FactoryTests.test_empty_plant_has_no_mean) ... ok
test_finite_numeric_fields_reject_nan_inf_bool_and_strings (test_p093.FactoryTests.test_finite_numeric_fields_reject_nan_inf_bool_and_strings) ... ok
test_impossible_cycle_or_zero_runtime_production_rejected (test_p093.FactoryTests.test_impossible_cycle_or_zero_runtime_production_rejected) ... ok
test_known_availability_performance_quality_and_oee (test_p093.FactoryTests.test_known_availability_performance_quality_and_oee) ... ok
test_maintenance_limit_must_be_finite_nonnegative (test_p093.FactoryTests.test_maintenance_limit_must_be_finite_nonnegative) ... ok
test_maintenance_threshold_is_strict (test_p093.FactoryTests.test_maintenance_threshold_is_strict) ... ok
test_mean_oee_is_arithmetic_not_a_weighted_plant_oee (test_p093.FactoryTests.test_mean_oee_is_arithmetic_not_a_weighted_plant_oee) ... ok
test_names_must_be_nonempty_bounded_strings (test_p093.FactoryTests.test_names_must_be_nonempty_bounded_strings) ... ok
test_negative_measurements_rejected (test_p093.FactoryTests.test_negative_measurements_rejected) ... ok
test_perfect_machine_at_upper_bound (test_p093.FactoryTests.test_perfect_machine_at_upper_bound) ... ok
test_plant_keeps_its_own_machine_sequence (test_p093.FactoryTests.test_plant_keeps_its_own_machine_sequence) ... ok
test_plant_rejects_duplicate_machine_names (test_p093.FactoryTests.test_plant_rejects_duplicate_machine_names) ... ok
test_plant_rejects_non_twin_members (test_p093.FactoryTests.test_plant_rejects_non_twin_members) ... ok
test_runtime_cannot_exceed_planned_time (test_p093.FactoryTests.test_runtime_cannot_exceed_planned_time) ... ok
test_runtime_without_production_has_zero_quality_by_convention (test_p093.FactoryTests.test_runtime_without_production_has_zero_quality_by_convention) ... ok
test_stopped_machine_has_zero_components (test_p093.FactoryTests.test_stopped_machine_has_zero_components) ... ok
test_validated_twin_is_immutable (test_p093.FactoryTests.test_validated_twin_is_immutable) ... ok

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
