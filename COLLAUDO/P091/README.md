# P091: output dei collaudi

[Indice dei collaudi](../README.md) · [Codice e istruzioni](../../projects/P091/README.md)

Esito registrato: **PASS in tutte le quattro combinazioni**. [Run 39893701054](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39893701054) · commit `3ab7bdfedb20a443bd71fe4e4ffe3c1dd67bd707`.

Comando effettivo del [runner a quel commit](https://github.com/davideiannella/100-progetti-informatica-pratica/blob/3ab7bdfedb20a443bd71fe4e4ffe3c1dd67bd707/tools/collaudo_p081_p100.py): `[sys.executable, "-B", "run_tests.py"]`, con directory di lavoro `projects/P091`. `sys.executable` indica l’interprete della combinazione riportata sotto; il suo percorso host assoluto non è registrato nella summary.

I quattro rapporti sono output CI preesistenti, non nuove esecuzioni preparate per questa pagina. Ogni ambiente ha verificato gli hash dei 299 sorgenti, compilato 60 file Python e completato 20 suite per 377 metodi complessivi.

`unittest` scrive normalmente il rapporto dettagliato su **stderr**: questo non equivale a un errore. I nomi e gli esiti sotto provengono dalle righe effettivamente emesse; non sono stati ricostruiti dal codice. I TXT mantengono i byte e i terminatori originali, compreso CRLF su Windows; i blocchi Markdown normalizzano soltanto i terminatori.

## Suite — quattro ambienti CI

### ubuntu-latest-python-3.12

Artifact: `output-p081-p100-ubuntu-latest-python-3.12` (ID `12476170749`). [Summary originale](../ambienti/ubuntu-latest-python-3.12.summary.json).

OS: `Linux` · piattaforma: `Linux-6.17.0-1022-azure-x86_64-with-glibc2.39` · Python: `3.12.15 (main, Oct  1 2026, 02:35:59) [GCC 13.3.0]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **13** · skipped: `0`.

**stdout** — [file TXT](streams/ubuntu-latest-python-3.12.stdout.txt)

```text
test_both_prioritizes_state_without_losing_water_action (test_p091.SafetyTests.test_both_prioritizes_state_without_losing_water_action) ... ok
test_demo_has_six_samples_and_four_transitions (test_p091.SafetyTests.test_demo_has_six_samples_and_four_transitions) ... ok
test_fire_to_water_transition (test_p091.SafetyTests.test_fire_to_water_transition) ... ok
test_instances_do_not_share_state (test_p091.SafetyTests.test_instances_do_not_share_state) ... ok
test_invalid_booleans_rejected_without_mutation (test_p091.SafetyTests.test_invalid_booleans_rejected_without_mutation) ... ok
test_normal_has_no_actions_or_transition (test_p091.SafetyTests.test_normal_has_no_actions_or_transition) ... ok
test_offline_decision_and_ordered_single_flush (test_p091.SafetyTests.test_offline_decision_and_ordered_single_flush) ... ok
test_repeated_sample_does_not_duplicate_notification (test_p091.SafetyTests.test_repeated_sample_does_not_duplicate_notification) ... ok
test_return_to_normal_is_automatic_in_this_simulation (test_p091.SafetyTests.test_return_to_normal_is_automatic_in_this_simulation) ... ok
test_returned_lists_do_not_modify_controller (test_p091.SafetyTests.test_returned_lists_do_not_modify_controller) ... ok
test_same_state_different_hazard_is_recorded (test_p091.SafetyTests.test_same_state_different_hazard_is_recorded) ... ok
test_smoke_requests_two_local_actions (test_p091.SafetyTests.test_smoke_requests_two_local_actions) ... ok
test_water_requests_valve (test_p091.SafetyTests.test_water_requests_valve) ... ok

----------------------------------------------------------------------
Ran 13 tests in 0.002s

OK
```

**stderr** — [file TXT](streams/ubuntu-latest-python-3.12.stderr.txt)

Il processo non ha emesso byte su stderr. Il file collegato è vuoto (0 byte).

### ubuntu-latest-python-3.13

Artifact: `output-p081-p100-ubuntu-latest-python-3.13` (ID `12476095990`). [Summary originale](../ambienti/ubuntu-latest-python-3.13.summary.json).

OS: `Linux` · piattaforma: `Linux-6.17.0-1022-azure-x86_64-with-glibc2.39` · Python: `3.13.16 (main, Oct  1 2026, 02:37:54) [GCC 13.3.0]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **13** · skipped: `0`.

**stdout** — [file TXT](streams/ubuntu-latest-python-3.13.stdout.txt)

```text
test_both_prioritizes_state_without_losing_water_action (test_p091.SafetyTests.test_both_prioritizes_state_without_losing_water_action) ... ok
test_demo_has_six_samples_and_four_transitions (test_p091.SafetyTests.test_demo_has_six_samples_and_four_transitions) ... ok
test_fire_to_water_transition (test_p091.SafetyTests.test_fire_to_water_transition) ... ok
test_instances_do_not_share_state (test_p091.SafetyTests.test_instances_do_not_share_state) ... ok
test_invalid_booleans_rejected_without_mutation (test_p091.SafetyTests.test_invalid_booleans_rejected_without_mutation) ... ok
test_normal_has_no_actions_or_transition (test_p091.SafetyTests.test_normal_has_no_actions_or_transition) ... ok
test_offline_decision_and_ordered_single_flush (test_p091.SafetyTests.test_offline_decision_and_ordered_single_flush) ... ok
test_repeated_sample_does_not_duplicate_notification (test_p091.SafetyTests.test_repeated_sample_does_not_duplicate_notification) ... ok
test_return_to_normal_is_automatic_in_this_simulation (test_p091.SafetyTests.test_return_to_normal_is_automatic_in_this_simulation) ... ok
test_returned_lists_do_not_modify_controller (test_p091.SafetyTests.test_returned_lists_do_not_modify_controller) ... ok
test_same_state_different_hazard_is_recorded (test_p091.SafetyTests.test_same_state_different_hazard_is_recorded) ... ok
test_smoke_requests_two_local_actions (test_p091.SafetyTests.test_smoke_requests_two_local_actions) ... ok
test_water_requests_valve (test_p091.SafetyTests.test_water_requests_valve) ... ok

----------------------------------------------------------------------
Ran 13 tests in 0.002s

OK
```

**stderr** — [file TXT](streams/ubuntu-latest-python-3.13.stderr.txt)

Il processo non ha emesso byte su stderr. Il file collegato è vuoto (0 byte).

### windows-latest-python-3.12

Artifact: `output-p081-p100-windows-latest-python-3.12` (ID `12475927047`). [Summary originale](../ambienti/windows-latest-python-3.12.summary.json).

OS: `Windows` · piattaforma: `Windows-2025Server-10.0.26100-SP0` · Python: `3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **13** · skipped: `0`.

**stdout** — [file TXT](streams/windows-latest-python-3.12.stdout.txt)

```text
test_both_prioritizes_state_without_losing_water_action (test_p091.SafetyTests.test_both_prioritizes_state_without_losing_water_action) ... ok
test_demo_has_six_samples_and_four_transitions (test_p091.SafetyTests.test_demo_has_six_samples_and_four_transitions) ... ok
test_fire_to_water_transition (test_p091.SafetyTests.test_fire_to_water_transition) ... ok
test_instances_do_not_share_state (test_p091.SafetyTests.test_instances_do_not_share_state) ... ok
test_invalid_booleans_rejected_without_mutation (test_p091.SafetyTests.test_invalid_booleans_rejected_without_mutation) ... ok
test_normal_has_no_actions_or_transition (test_p091.SafetyTests.test_normal_has_no_actions_or_transition) ... ok
test_offline_decision_and_ordered_single_flush (test_p091.SafetyTests.test_offline_decision_and_ordered_single_flush) ... ok
test_repeated_sample_does_not_duplicate_notification (test_p091.SafetyTests.test_repeated_sample_does_not_duplicate_notification) ... ok
test_return_to_normal_is_automatic_in_this_simulation (test_p091.SafetyTests.test_return_to_normal_is_automatic_in_this_simulation) ... ok
test_returned_lists_do_not_modify_controller (test_p091.SafetyTests.test_returned_lists_do_not_modify_controller) ... ok
test_same_state_different_hazard_is_recorded (test_p091.SafetyTests.test_same_state_different_hazard_is_recorded) ... ok
test_smoke_requests_two_local_actions (test_p091.SafetyTests.test_smoke_requests_two_local_actions) ... ok
test_water_requests_valve (test_p091.SafetyTests.test_water_requests_valve) ... ok

----------------------------------------------------------------------
Ran 13 tests in 0.002s

OK
```

**stderr** — [file TXT](streams/windows-latest-python-3.12.stderr.txt)

Il processo non ha emesso byte su stderr. Il file collegato è vuoto (0 byte).

### windows-latest-python-3.13

Artifact: `output-p081-p100-windows-latest-python-3.13` (ID `12475826902`). [Summary originale](../ambienti/windows-latest-python-3.13.summary.json).

OS: `Windows` · piattaforma: `Windows-2025Server-10.0.26100-SP0` · Python: `3.13.16 (tags/v3.13.16:cbc944f, Sep 30 2026, 19:17:50) [MSC v.1944 64 bit (AMD64)]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **13** · skipped: `0`.

**stdout** — [file TXT](streams/windows-latest-python-3.13.stdout.txt)

```text
test_both_prioritizes_state_without_losing_water_action (test_p091.SafetyTests.test_both_prioritizes_state_without_losing_water_action) ... ok
test_demo_has_six_samples_and_four_transitions (test_p091.SafetyTests.test_demo_has_six_samples_and_four_transitions) ... ok
test_fire_to_water_transition (test_p091.SafetyTests.test_fire_to_water_transition) ... ok
test_instances_do_not_share_state (test_p091.SafetyTests.test_instances_do_not_share_state) ... ok
test_invalid_booleans_rejected_without_mutation (test_p091.SafetyTests.test_invalid_booleans_rejected_without_mutation) ... ok
test_normal_has_no_actions_or_transition (test_p091.SafetyTests.test_normal_has_no_actions_or_transition) ... ok
test_offline_decision_and_ordered_single_flush (test_p091.SafetyTests.test_offline_decision_and_ordered_single_flush) ... ok
test_repeated_sample_does_not_duplicate_notification (test_p091.SafetyTests.test_repeated_sample_does_not_duplicate_notification) ... ok
test_return_to_normal_is_automatic_in_this_simulation (test_p091.SafetyTests.test_return_to_normal_is_automatic_in_this_simulation) ... ok
test_returned_lists_do_not_modify_controller (test_p091.SafetyTests.test_returned_lists_do_not_modify_controller) ... ok
test_same_state_different_hazard_is_recorded (test_p091.SafetyTests.test_same_state_different_hazard_is_recorded) ... ok
test_smoke_requests_two_local_actions (test_p091.SafetyTests.test_smoke_requests_two_local_actions) ... ok
test_water_requests_valve (test_p091.SafetyTests.test_water_requests_valve) ... ok

----------------------------------------------------------------------
Ran 13 tests in 0.001s

OK
```

**stderr** — [file TXT](streams/windows-latest-python-3.13.stderr.txt)

Il processo non ha emesso byte su stderr. Il file collegato è vuoto (0 byte).

## Demo e controlli runtime

Questa matrice esegue le suite `run_tests.py`. Le summary non classificano processi separati come demo o controlli runtime: non sono aggiunti output o esiti di tali categorie.

## Verifica e provenienza

[Registro strutturato](registro.json) · [Hash e trasformazioni](MANIFEST.json) · [Policy](../AUDIT.md) · [Indice](../README.md)
