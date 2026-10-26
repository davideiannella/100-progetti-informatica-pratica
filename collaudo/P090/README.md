# P090: output dei collaudi

[Indice dei collaudi](../README.md) · [Codice e istruzioni](../../projects/P090/README.md)

Esito registrato: **PASS in tutte le quattro combinazioni**. [Run 39893701054](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39893701054) · commit `3ab7bdfedb20a443bd71fe4e4ffe3c1dd67bd707`.

Comando effettivo del [runner a quel commit](https://github.com/davideiannella/100-progetti-informatica-pratica/blob/3ab7bdfedb20a443bd71fe4e4ffe3c1dd67bd707/tools/collaudo_p081_p100.py): `[sys.executable, "-B", "run_tests.py"]`, con directory di lavoro `projects/P090`. `sys.executable` indica l’interprete della combinazione riportata sotto; il suo percorso host assoluto non è registrato nella summary.

I quattro rapporti sono output CI preesistenti, non nuove esecuzioni preparate per questa pagina. Ogni ambiente ha verificato gli hash dei 299 sorgenti, compilato 60 file Python e completato 20 suite per 377 metodi complessivi.

`unittest` scrive normalmente il rapporto dettagliato su **stderr**: questo non equivale a un errore. I nomi e gli esiti sotto provengono dalle righe effettivamente emesse; non sono stati ricostruiti dal codice. I TXT mantengono i byte e i terminatori originali, compreso CRLF su Windows; i blocchi Markdown normalizzano soltanto i terminatori.

## Suite — quattro ambienti CI

### ubuntu-latest-python-3.12

Artifact: `output-p081-p100-ubuntu-latest-python-3.12` (ID `12476170749`). [Summary originale](../ambienti/ubuntu-latest-python-3.12.summary.json).

OS: `Linux` · piattaforma: `Linux-6.17.0-1022-azure-x86_64-with-glibc2.39` · Python: `3.12.15 (main, Oct  1 2026, 02:35:59) [GCC 13.3.0]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **19** · skipped: `0`.

**stdout** — [file TXT](streams/ubuntu-latest-python-3.12.stdout.txt)

Il processo non ha emesso byte su stdout. Il file collegato è vuoto (0 byte).

**stderr** — [file TXT](streams/ubuntu-latest-python-3.12.stderr.txt)

```text
test_baseline_and_missed_anomalies_are_visible (test_p090.MaintenanceTests.test_baseline_and_missed_anomalies_are_visible) ... ok
test_confusion_matrix_reconstructs_metrics (test_p090.MaintenanceTests.test_confusion_matrix_reconstructs_metrics) ... ok
test_constant_signal_has_no_ac_component (test_p090.MaintenanceTests.test_constant_signal_has_no_ac_component) ... ok
test_experiment_is_reproducible (test_p090.MaintenanceTests.test_experiment_is_reproducible) ... ok
test_feature_constraints_on_generated_signals (test_p090.MaintenanceTests.test_feature_constraints_on_generated_signals) ... ok
test_frequency_cutoff_includes_40_hz (test_p090.MaintenanceTests.test_frequency_cutoff_includes_40_hz) ... ok
test_generator_rejects_invalid_label_and_rng (test_p090.MaintenanceTests.test_generator_rejects_invalid_label_and_rng) ... ok
test_generator_seed_is_reproducible (test_p090.MaintenanceTests.test_generator_seed_is_reproducible) ... ok
test_invalid_attention_threshold (test_p090.MaintenanceTests.test_invalid_attention_threshold) ... ok
test_invalid_sample_rates (test_p090.MaintenanceTests.test_invalid_sample_rates) ... ok
test_invalid_seeds (test_p090.MaintenanceTests.test_invalid_seeds) ... ok
test_invalid_signal_shapes_and_types (test_p090.MaintenanceTests.test_invalid_signal_shapes_and_types) ... ok
test_large_finite_amplitudes_do_not_overflow (test_p090.MaintenanceTests.test_large_finite_amplitudes_do_not_overflow) ... ok
test_nonfinite_signal_values (test_p090.MaintenanceTests.test_nonfinite_signal_values) ... ok
test_odd_length_spectral_weights (test_p090.MaintenanceTests.test_odd_length_spectral_weights) ... ok
test_scaler_is_fitted_only_on_training (test_p090.MaintenanceTests.test_scaler_is_fitted_only_on_training) ... ok
test_sine_rms_and_frequency_ratio (test_p090.MaintenanceTests.test_sine_rms_and_frequency_ratio) ... ok
test_split_is_disjoint_and_stratified (test_p090.MaintenanceTests.test_split_is_disjoint_and_stratified) ... ok
test_zero_signal (test_p090.MaintenanceTests.test_zero_signal) ... ok

----------------------------------------------------------------------
Ran 19 tests in 0.192s

OK
```

### ubuntu-latest-python-3.13

Artifact: `output-p081-p100-ubuntu-latest-python-3.13` (ID `12476095990`). [Summary originale](../ambienti/ubuntu-latest-python-3.13.summary.json).

OS: `Linux` · piattaforma: `Linux-6.17.0-1022-azure-x86_64-with-glibc2.39` · Python: `3.13.16 (main, Oct  1 2026, 02:37:54) [GCC 13.3.0]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **19** · skipped: `0`.

**stdout** — [file TXT](streams/ubuntu-latest-python-3.13.stdout.txt)

Il processo non ha emesso byte su stdout. Il file collegato è vuoto (0 byte).

**stderr** — [file TXT](streams/ubuntu-latest-python-3.13.stderr.txt)

```text
test_baseline_and_missed_anomalies_are_visible (test_p090.MaintenanceTests.test_baseline_and_missed_anomalies_are_visible) ... ok
test_confusion_matrix_reconstructs_metrics (test_p090.MaintenanceTests.test_confusion_matrix_reconstructs_metrics) ... ok
test_constant_signal_has_no_ac_component (test_p090.MaintenanceTests.test_constant_signal_has_no_ac_component) ... ok
test_experiment_is_reproducible (test_p090.MaintenanceTests.test_experiment_is_reproducible) ... ok
test_feature_constraints_on_generated_signals (test_p090.MaintenanceTests.test_feature_constraints_on_generated_signals) ... ok
test_frequency_cutoff_includes_40_hz (test_p090.MaintenanceTests.test_frequency_cutoff_includes_40_hz) ... ok
test_generator_rejects_invalid_label_and_rng (test_p090.MaintenanceTests.test_generator_rejects_invalid_label_and_rng) ... ok
test_generator_seed_is_reproducible (test_p090.MaintenanceTests.test_generator_seed_is_reproducible) ... ok
test_invalid_attention_threshold (test_p090.MaintenanceTests.test_invalid_attention_threshold) ... ok
test_invalid_sample_rates (test_p090.MaintenanceTests.test_invalid_sample_rates) ... ok
test_invalid_seeds (test_p090.MaintenanceTests.test_invalid_seeds) ... ok
test_invalid_signal_shapes_and_types (test_p090.MaintenanceTests.test_invalid_signal_shapes_and_types) ... ok
test_large_finite_amplitudes_do_not_overflow (test_p090.MaintenanceTests.test_large_finite_amplitudes_do_not_overflow) ... ok
test_nonfinite_signal_values (test_p090.MaintenanceTests.test_nonfinite_signal_values) ... ok
test_odd_length_spectral_weights (test_p090.MaintenanceTests.test_odd_length_spectral_weights) ... ok
test_scaler_is_fitted_only_on_training (test_p090.MaintenanceTests.test_scaler_is_fitted_only_on_training) ... ok
test_sine_rms_and_frequency_ratio (test_p090.MaintenanceTests.test_sine_rms_and_frequency_ratio) ... ok
test_split_is_disjoint_and_stratified (test_p090.MaintenanceTests.test_split_is_disjoint_and_stratified) ... ok
test_zero_signal (test_p090.MaintenanceTests.test_zero_signal) ... ok

----------------------------------------------------------------------
Ran 19 tests in 0.186s

OK
```

### windows-latest-python-3.12

Artifact: `output-p081-p100-windows-latest-python-3.12` (ID `12475927047`). [Summary originale](../ambienti/windows-latest-python-3.12.summary.json).

OS: `Windows` · piattaforma: `Windows-2025Server-10.0.26100-SP0` · Python: `3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **19** · skipped: `0`.

**stdout** — [file TXT](streams/windows-latest-python-3.12.stdout.txt)

Il processo non ha emesso byte su stdout. Il file collegato è vuoto (0 byte).

**stderr** — [file TXT](streams/windows-latest-python-3.12.stderr.txt)

```text
test_baseline_and_missed_anomalies_are_visible (test_p090.MaintenanceTests.test_baseline_and_missed_anomalies_are_visible) ... ok
test_confusion_matrix_reconstructs_metrics (test_p090.MaintenanceTests.test_confusion_matrix_reconstructs_metrics) ... ok
test_constant_signal_has_no_ac_component (test_p090.MaintenanceTests.test_constant_signal_has_no_ac_component) ... ok
test_experiment_is_reproducible (test_p090.MaintenanceTests.test_experiment_is_reproducible) ... ok
test_feature_constraints_on_generated_signals (test_p090.MaintenanceTests.test_feature_constraints_on_generated_signals) ... ok
test_frequency_cutoff_includes_40_hz (test_p090.MaintenanceTests.test_frequency_cutoff_includes_40_hz) ... ok
test_generator_rejects_invalid_label_and_rng (test_p090.MaintenanceTests.test_generator_rejects_invalid_label_and_rng) ... ok
test_generator_seed_is_reproducible (test_p090.MaintenanceTests.test_generator_seed_is_reproducible) ... ok
test_invalid_attention_threshold (test_p090.MaintenanceTests.test_invalid_attention_threshold) ... ok
test_invalid_sample_rates (test_p090.MaintenanceTests.test_invalid_sample_rates) ... ok
test_invalid_seeds (test_p090.MaintenanceTests.test_invalid_seeds) ... ok
test_invalid_signal_shapes_and_types (test_p090.MaintenanceTests.test_invalid_signal_shapes_and_types) ... ok
test_large_finite_amplitudes_do_not_overflow (test_p090.MaintenanceTests.test_large_finite_amplitudes_do_not_overflow) ... ok
test_nonfinite_signal_values (test_p090.MaintenanceTests.test_nonfinite_signal_values) ... ok
test_odd_length_spectral_weights (test_p090.MaintenanceTests.test_odd_length_spectral_weights) ... ok
test_scaler_is_fitted_only_on_training (test_p090.MaintenanceTests.test_scaler_is_fitted_only_on_training) ... ok
test_sine_rms_and_frequency_ratio (test_p090.MaintenanceTests.test_sine_rms_and_frequency_ratio) ... ok
test_split_is_disjoint_and_stratified (test_p090.MaintenanceTests.test_split_is_disjoint_and_stratified) ... ok
test_zero_signal (test_p090.MaintenanceTests.test_zero_signal) ... ok

----------------------------------------------------------------------
Ran 19 tests in 0.101s

OK
```

### windows-latest-python-3.13

Artifact: `output-p081-p100-windows-latest-python-3.13` (ID `12475826902`). [Summary originale](../ambienti/windows-latest-python-3.13.summary.json).

OS: `Windows` · piattaforma: `Windows-2025Server-10.0.26100-SP0` · Python: `3.13.16 (tags/v3.13.16:cbc944f, Sep 30 2026, 19:17:50) [MSC v.1944 64 bit (AMD64)]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **19** · skipped: `0`.

**stdout** — [file TXT](streams/windows-latest-python-3.13.stdout.txt)

Il processo non ha emesso byte su stdout. Il file collegato è vuoto (0 byte).

**stderr** — [file TXT](streams/windows-latest-python-3.13.stderr.txt)

```text
test_baseline_and_missed_anomalies_are_visible (test_p090.MaintenanceTests.test_baseline_and_missed_anomalies_are_visible) ... ok
test_confusion_matrix_reconstructs_metrics (test_p090.MaintenanceTests.test_confusion_matrix_reconstructs_metrics) ... ok
test_constant_signal_has_no_ac_component (test_p090.MaintenanceTests.test_constant_signal_has_no_ac_component) ... ok
test_experiment_is_reproducible (test_p090.MaintenanceTests.test_experiment_is_reproducible) ... ok
test_feature_constraints_on_generated_signals (test_p090.MaintenanceTests.test_feature_constraints_on_generated_signals) ... ok
test_frequency_cutoff_includes_40_hz (test_p090.MaintenanceTests.test_frequency_cutoff_includes_40_hz) ... ok
test_generator_rejects_invalid_label_and_rng (test_p090.MaintenanceTests.test_generator_rejects_invalid_label_and_rng) ... ok
test_generator_seed_is_reproducible (test_p090.MaintenanceTests.test_generator_seed_is_reproducible) ... ok
test_invalid_attention_threshold (test_p090.MaintenanceTests.test_invalid_attention_threshold) ... ok
test_invalid_sample_rates (test_p090.MaintenanceTests.test_invalid_sample_rates) ... ok
test_invalid_seeds (test_p090.MaintenanceTests.test_invalid_seeds) ... ok
test_invalid_signal_shapes_and_types (test_p090.MaintenanceTests.test_invalid_signal_shapes_and_types) ... ok
test_large_finite_amplitudes_do_not_overflow (test_p090.MaintenanceTests.test_large_finite_amplitudes_do_not_overflow) ... ok
test_nonfinite_signal_values (test_p090.MaintenanceTests.test_nonfinite_signal_values) ... ok
test_odd_length_spectral_weights (test_p090.MaintenanceTests.test_odd_length_spectral_weights) ... ok
test_scaler_is_fitted_only_on_training (test_p090.MaintenanceTests.test_scaler_is_fitted_only_on_training) ... ok
test_sine_rms_and_frequency_ratio (test_p090.MaintenanceTests.test_sine_rms_and_frequency_ratio) ... ok
test_split_is_disjoint_and_stratified (test_p090.MaintenanceTests.test_split_is_disjoint_and_stratified) ... ok
test_zero_signal (test_p090.MaintenanceTests.test_zero_signal) ... ok

----------------------------------------------------------------------
Ran 19 tests in 0.102s

OK
```

## Demo e controlli runtime

Questa matrice esegue le suite `run_tests.py`. Le summary non classificano processi separati come demo o controlli runtime: non sono aggiunti output o esiti di tali categorie.

## Verifica e provenienza

[Registro strutturato](registro.json) · [Hash e trasformazioni](MANIFEST.json) · [Policy](../AUDIT.md) · [Indice](../README.md)
