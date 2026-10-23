# P097 — output reali dei collaudi

Esito registrato: **PASS in tutte le quattro combinazioni**. [Run 39893701054](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39893701054) · commit `3ab7bdfedb20a443bd71fe4e4ffe3c1dd67bd707`.

Comando effettivo del [runner a quel commit](https://github.com/davideiannella/100-progetti-informatica-pratica/blob/3ab7bdfedb20a443bd71fe4e4ffe3c1dd67bd707/tools/collaudo_p081_p100.py): `[sys.executable, "-B", "run_tests.py"]`, con directory di lavoro `projects/P097`. `sys.executable` indica l’interprete della combinazione riportata sotto; il suo percorso host assoluto non è registrato nella summary.

I quattro rapporti sono output CI preesistenti, non nuove esecuzioni preparate per questa pagina. Ogni ambiente ha verificato gli hash dei 299 sorgenti, compilato 60 file Python e completato 20 suite per 377 metodi complessivi.

`unittest` scrive normalmente il rapporto dettagliato su **stderr**: questo non equivale a un errore. I nomi e gli esiti sotto provengono dalle righe effettivamente emesse; non sono stati ricostruiti dal codice. I TXT mantengono i byte e i terminatori originali, compreso CRLF su Windows; i blocchi Markdown normalizzano soltanto i terminatori.

## Suite — quattro ambienti CI

### ubuntu-latest-python-3.12

Artifact: `output-p081-p100-ubuntu-latest-python-3.12` (ID `12476170749`). [Summary originale](../ambienti/ubuntu-latest-python-3.12.summary.json).

OS: `Linux` · piattaforma: `Linux-6.17.0-1022-azure-x86_64-with-glibc2.39` · Python: `3.12.15 (main, Oct  1 2026, 02:35:59) [GCC 13.3.0]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **14** · skipped: `0`.

**stdout** — [file TXT](streams/ubuntu-latest-python-3.12.stdout.txt)

```text
test_methods=14; executed=14; failures=0; errors=0
```

**stderr** — [file TXT](streams/ubuntu-latest-python-3.12.stderr.txt)

```text
test_alarm_is_virtual_and_independent_from_hvac (test_p097.BuildingTests.test_alarm_is_virtual_and_independent_from_hvac) ... ok
test_boundaries_are_off (test_p097.BuildingTests.test_boundaries_are_off) ... ok
test_cooling_uses_distinct_rate (test_p097.BuildingTests.test_cooling_uses_distinct_rate) ... ok
test_deadband_has_no_memory_hysteresis (test_p097.BuildingTests.test_deadband_has_no_memory_hysteresis) ... ok
test_demo_numbers (test_p097.BuildingTests.test_demo_numbers) ... ok
test_energy_sums_power_times_duration (test_p097.BuildingTests.test_energy_sums_power_times_duration) ... ok
test_heating_cooling_and_off (test_p097.BuildingTests.test_heating_cooling_and_off) ... ok
test_invalid_alarm_adds_nothing (test_p097.BuildingTests.test_invalid_alarm_adds_nothing) ... ok
test_invalid_control_does_not_change_hvac (test_p097.BuildingTests.test_invalid_control_does_not_change_hvac) ... ok
test_invalid_duration_does_not_change_energy (test_p097.BuildingTests.test_invalid_duration_does_not_change_energy) ... ok
test_invalid_names_and_duplicate_zones (test_p097.BuildingTests.test_invalid_names_and_duplicate_zones) ... ok
test_invalid_temperatures_leave_previous_state (test_p097.BuildingTests.test_invalid_temperatures_leave_previous_state) ... ok
test_occupied_requires_boolean (test_p097.BuildingTests.test_occupied_requires_boolean) ... ok
test_unoccupied_is_eco_even_when_cold (test_p097.BuildingTests.test_unoccupied_is_eco_even_when_cold) ... ok

----------------------------------------------------------------------
Ran 14 tests in 0.002s

OK
```

### ubuntu-latest-python-3.13

Artifact: `output-p081-p100-ubuntu-latest-python-3.13` (ID `12476095990`). [Summary originale](../ambienti/ubuntu-latest-python-3.13.summary.json).

OS: `Linux` · piattaforma: `Linux-6.17.0-1022-azure-x86_64-with-glibc2.39` · Python: `3.13.16 (main, Oct  1 2026, 02:37:54) [GCC 13.3.0]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **14** · skipped: `0`.

**stdout** — [file TXT](streams/ubuntu-latest-python-3.13.stdout.txt)

```text
test_methods=14; executed=14; failures=0; errors=0
```

**stderr** — [file TXT](streams/ubuntu-latest-python-3.13.stderr.txt)

```text
test_alarm_is_virtual_and_independent_from_hvac (test_p097.BuildingTests.test_alarm_is_virtual_and_independent_from_hvac) ... ok
test_boundaries_are_off (test_p097.BuildingTests.test_boundaries_are_off) ... ok
test_cooling_uses_distinct_rate (test_p097.BuildingTests.test_cooling_uses_distinct_rate) ... ok
test_deadband_has_no_memory_hysteresis (test_p097.BuildingTests.test_deadband_has_no_memory_hysteresis) ... ok
test_demo_numbers (test_p097.BuildingTests.test_demo_numbers) ... ok
test_energy_sums_power_times_duration (test_p097.BuildingTests.test_energy_sums_power_times_duration) ... ok
test_heating_cooling_and_off (test_p097.BuildingTests.test_heating_cooling_and_off) ... ok
test_invalid_alarm_adds_nothing (test_p097.BuildingTests.test_invalid_alarm_adds_nothing) ... ok
test_invalid_control_does_not_change_hvac (test_p097.BuildingTests.test_invalid_control_does_not_change_hvac) ... ok
test_invalid_duration_does_not_change_energy (test_p097.BuildingTests.test_invalid_duration_does_not_change_energy) ... ok
test_invalid_names_and_duplicate_zones (test_p097.BuildingTests.test_invalid_names_and_duplicate_zones) ... ok
test_invalid_temperatures_leave_previous_state (test_p097.BuildingTests.test_invalid_temperatures_leave_previous_state) ... ok
test_occupied_requires_boolean (test_p097.BuildingTests.test_occupied_requires_boolean) ... ok
test_unoccupied_is_eco_even_when_cold (test_p097.BuildingTests.test_unoccupied_is_eco_even_when_cold) ... ok

----------------------------------------------------------------------
Ran 14 tests in 0.001s

OK
```

### windows-latest-python-3.12

Artifact: `output-p081-p100-windows-latest-python-3.12` (ID `12475927047`). [Summary originale](../ambienti/windows-latest-python-3.12.summary.json).

OS: `Windows` · piattaforma: `Windows-2025Server-10.0.26100-SP0` · Python: `3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **14** · skipped: `0`.

**stdout** — [file TXT](streams/windows-latest-python-3.12.stdout.txt)

```text
test_methods=14; executed=14; failures=0; errors=0
```

**stderr** — [file TXT](streams/windows-latest-python-3.12.stderr.txt)

```text
test_alarm_is_virtual_and_independent_from_hvac (test_p097.BuildingTests.test_alarm_is_virtual_and_independent_from_hvac) ... ok
test_boundaries_are_off (test_p097.BuildingTests.test_boundaries_are_off) ... ok
test_cooling_uses_distinct_rate (test_p097.BuildingTests.test_cooling_uses_distinct_rate) ... ok
test_deadband_has_no_memory_hysteresis (test_p097.BuildingTests.test_deadband_has_no_memory_hysteresis) ... ok
test_demo_numbers (test_p097.BuildingTests.test_demo_numbers) ... ok
test_energy_sums_power_times_duration (test_p097.BuildingTests.test_energy_sums_power_times_duration) ... ok
test_heating_cooling_and_off (test_p097.BuildingTests.test_heating_cooling_and_off) ... ok
test_invalid_alarm_adds_nothing (test_p097.BuildingTests.test_invalid_alarm_adds_nothing) ... ok
test_invalid_control_does_not_change_hvac (test_p097.BuildingTests.test_invalid_control_does_not_change_hvac) ... ok
test_invalid_duration_does_not_change_energy (test_p097.BuildingTests.test_invalid_duration_does_not_change_energy) ... ok
test_invalid_names_and_duplicate_zones (test_p097.BuildingTests.test_invalid_names_and_duplicate_zones) ... ok
test_invalid_temperatures_leave_previous_state (test_p097.BuildingTests.test_invalid_temperatures_leave_previous_state) ... ok
test_occupied_requires_boolean (test_p097.BuildingTests.test_occupied_requires_boolean) ... ok
test_unoccupied_is_eco_even_when_cold (test_p097.BuildingTests.test_unoccupied_is_eco_even_when_cold) ... ok

----------------------------------------------------------------------
Ran 14 tests in 0.001s

OK
```

### windows-latest-python-3.13

Artifact: `output-p081-p100-windows-latest-python-3.13` (ID `12475826902`). [Summary originale](../ambienti/windows-latest-python-3.13.summary.json).

OS: `Windows` · piattaforma: `Windows-2025Server-10.0.26100-SP0` · Python: `3.13.16 (tags/v3.13.16:cbc944f, Sep 30 2026, 19:17:50) [MSC v.1944 64 bit (AMD64)]`.

Esito: **PASS** · codice di uscita: `0` · metodi eseguiti: **14** · skipped: `0`.

**stdout** — [file TXT](streams/windows-latest-python-3.13.stdout.txt)

```text
test_methods=14; executed=14; failures=0; errors=0
```

**stderr** — [file TXT](streams/windows-latest-python-3.13.stderr.txt)

```text
test_alarm_is_virtual_and_independent_from_hvac (test_p097.BuildingTests.test_alarm_is_virtual_and_independent_from_hvac) ... ok
test_boundaries_are_off (test_p097.BuildingTests.test_boundaries_are_off) ... ok
test_cooling_uses_distinct_rate (test_p097.BuildingTests.test_cooling_uses_distinct_rate) ... ok
test_deadband_has_no_memory_hysteresis (test_p097.BuildingTests.test_deadband_has_no_memory_hysteresis) ... ok
test_demo_numbers (test_p097.BuildingTests.test_demo_numbers) ... ok
test_energy_sums_power_times_duration (test_p097.BuildingTests.test_energy_sums_power_times_duration) ... ok
test_heating_cooling_and_off (test_p097.BuildingTests.test_heating_cooling_and_off) ... ok
test_invalid_alarm_adds_nothing (test_p097.BuildingTests.test_invalid_alarm_adds_nothing) ... ok
test_invalid_control_does_not_change_hvac (test_p097.BuildingTests.test_invalid_control_does_not_change_hvac) ... ok
test_invalid_duration_does_not_change_energy (test_p097.BuildingTests.test_invalid_duration_does_not_change_energy) ... ok
test_invalid_names_and_duplicate_zones (test_p097.BuildingTests.test_invalid_names_and_duplicate_zones) ... ok
test_invalid_temperatures_leave_previous_state (test_p097.BuildingTests.test_invalid_temperatures_leave_previous_state) ... ok
test_occupied_requires_boolean (test_p097.BuildingTests.test_occupied_requires_boolean) ... ok
test_unoccupied_is_eco_even_when_cold (test_p097.BuildingTests.test_unoccupied_is_eco_even_when_cold) ... ok

----------------------------------------------------------------------
Ran 14 tests in 0.001s

OK
```

## Demo e controlli runtime

Questa matrice esegue le suite `run_tests.py`. Le summary non classificano processi separati come demo o controlli runtime: non sono aggiunti output o esiti di tali categorie.

## Verifica e provenienza

[Registro strutturato](registro.json) · [Hash e trasformazioni](MANIFEST.json) · [Policy](../AUDIT.md) · [Indice](../README.md)
