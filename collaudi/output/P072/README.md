# P072 — output reali dei collaudi

Esito registrato: **PASS**. [Run 39849393701](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701) · [job 120071206449](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701/job/120071206449).

Commit del runner: `44cd421247ca2bfe838baa735cf6180134f80464`. Sorgenti applicativi congelati: `32e201b1fb1258c4e7c77d32af323b966647b908`.

Ambiente registrato: Ubuntu 24.04 x86_64; Python 3.12.15 (main, Oct  1 2026, 02:35:59) [GCC 13.3.0]. Artifact: `p041-p080-core-39849393701-1` (ID `12456886835`); record originale: `P072/results.json`.

Questa pagina deriva dai risultati CI già acquisiti. Non è stata eseguita una nuova suite per prepararla. I blocchi riportano il testo emesso, dopo le sole sostituzioni di metadati indicate nel manifest. I TXT conservano i terminatori originali; per la lettura Markdown i terminatori sono normalizzati.

`unittest` scrive normalmente il proprio rapporto su **stderr**: la presenza di testo in quel canale non equivale a un errore. Esito e codice di uscita sono riportati separatamente.

I programmi di assert possono stampare soltanto un riepilogo o niente. I sottocasi non nominati dal processo restano non nominati: questa raccolta non ricostruisce nomi, valori o esiti di singoli assert. I rapporti `unittest` compatti a punti non rendono disponibili i nomi dei metodi.

## Suite di test

### 001 · unittest_project_suite

Comando registrato (array degli argomenti; segnaposto dei metadati documentati nel manifest):

```json
["<PYTHON_HOME>/bin/python", "-B", "run_tests.py"]
```

Esito: **PASS** · codice di uscita: `0`.

Rapporto registrato: 111 metodi unittest; failures 0, errors 0, skipped 0; sottocasi dichiarati 0.

**stdout** — [file TXT](streams/001_unittest_project_suite.stdout.txt)

```text
{"errors": 0, "failures": 0, "skipped": 0, "tests_run": 111}
```

**stderr** — [file TXT](streams/001_unittest_project_suite.stderr.txt)

```text
test_admin_allowed_unusual_and_missing_are_distinct (test_p072.SOCTests.test_admin_allowed_unusual_and_missing_are_distinct) ... ok
test_bad_event_not_counted_and_order_rejected (test_p072.SOCTests.test_bad_event_not_counted_and_order_rejected) ... ok
test_bad_parser_input (test_p072.SOCTests.test_bad_parser_input) ... ok
test_capacity_is_explicit_and_expiry_recovers (test_p072.SOCTests.test_capacity_is_explicit_and_expiry_recovers) ... ok
test_duplicate_timestamps_count_as_separate_records (test_p072.SOCTests.test_duplicate_timestamps_count_as_separate_records) ... ok
test_inclusive_boundary_expiry_and_source_isolation (test_p072.SOCTests.test_inclusive_boundary_expiry_and_source_isolation) ... ok
test_invalid_settings (test_p072.SOCTests.test_invalid_settings) ... ok
test_no_alert_for_success_and_no_automatic_reset (test_p072.SOCTests.test_no_alert_for_success_and_no_automatic_reset) ... ok
test_normalize_validation (test_p072.SOCTests.test_normalize_validation) ... ok
test_parse_quoted_values_and_equals (test_p072.SOCTests.test_parse_quoted_values_and_equals) ... ok
test_seeded_correlation_oracle_000 (test_p072.SOCTests.test_seeded_correlation_oracle_000) ... ok
test_seeded_correlation_oracle_001 (test_p072.SOCTests.test_seeded_correlation_oracle_001) ... ok
test_seeded_correlation_oracle_002 (test_p072.SOCTests.test_seeded_correlation_oracle_002) ... ok
test_seeded_correlation_oracle_003 (test_p072.SOCTests.test_seeded_correlation_oracle_003) ... ok
test_seeded_correlation_oracle_004 (test_p072.SOCTests.test_seeded_correlation_oracle_004) ... ok
test_seeded_correlation_oracle_005 (test_p072.SOCTests.test_seeded_correlation_oracle_005) ... ok
test_seeded_correlation_oracle_006 (test_p072.SOCTests.test_seeded_correlation_oracle_006) ... ok
test_seeded_correlation_oracle_007 (test_p072.SOCTests.test_seeded_correlation_oracle_007) ... ok
test_seeded_correlation_oracle_008 (test_p072.SOCTests.test_seeded_correlation_oracle_008) ... ok
test_seeded_correlation_oracle_009 (test_p072.SOCTests.test_seeded_correlation_oracle_009) ... ok
test_seeded_correlation_oracle_010 (test_p072.SOCTests.test_seeded_correlation_oracle_010) ... ok
test_seeded_correlation_oracle_011 (test_p072.SOCTests.test_seeded_correlation_oracle_011) ... ok
test_seeded_correlation_oracle_012 (test_p072.SOCTests.test_seeded_correlation_oracle_012) ... ok
test_seeded_correlation_oracle_013 (test_p072.SOCTests.test_seeded_correlation_oracle_013) ... ok
test_seeded_correlation_oracle_014 (test_p072.SOCTests.test_seeded_correlation_oracle_014) ... ok
test_seeded_correlation_oracle_015 (test_p072.SOCTests.test_seeded_correlation_oracle_015) ... ok
test_seeded_correlation_oracle_016 (test_p072.SOCTests.test_seeded_correlation_oracle_016) ... ok
test_seeded_correlation_oracle_017 (test_p072.SOCTests.test_seeded_correlation_oracle_017) ... ok
test_seeded_correlation_oracle_018 (test_p072.SOCTests.test_seeded_correlation_oracle_018) ... ok
test_seeded_correlation_oracle_019 (test_p072.SOCTests.test_seeded_correlation_oracle_019) ... ok
test_seeded_correlation_oracle_020 (test_p072.SOCTests.test_seeded_correlation_oracle_020) ... ok
test_seeded_correlation_oracle_021 (test_p072.SOCTests.test_seeded_correlation_oracle_021) ... ok
test_seeded_correlation_oracle_022 (test_p072.SOCTests.test_seeded_correlation_oracle_022) ... ok
test_seeded_correlation_oracle_023 (test_p072.SOCTests.test_seeded_correlation_oracle_023) ... ok
test_seeded_correlation_oracle_024 (test_p072.SOCTests.test_seeded_correlation_oracle_024) ... ok
test_seeded_correlation_oracle_025 (test_p072.SOCTests.test_seeded_correlation_oracle_025) ... ok
test_seeded_correlation_oracle_026 (test_p072.SOCTests.test_seeded_correlation_oracle_026) ... ok
test_seeded_correlation_oracle_027 (test_p072.SOCTests.test_seeded_correlation_oracle_027) ... ok
test_seeded_correlation_oracle_028 (test_p072.SOCTests.test_seeded_correlation_oracle_028) ... ok
test_seeded_correlation_oracle_029 (test_p072.SOCTests.test_seeded_correlation_oracle_029) ... ok
test_seeded_correlation_oracle_030 (test_p072.SOCTests.test_seeded_correlation_oracle_030) ... ok
test_seeded_correlation_oracle_031 (test_p072.SOCTests.test_seeded_correlation_oracle_031) ... ok
test_seeded_correlation_oracle_032 (test_p072.SOCTests.test_seeded_correlation_oracle_032) ... ok
test_seeded_correlation_oracle_033 (test_p072.SOCTests.test_seeded_correlation_oracle_033) ... ok
test_seeded_correlation_oracle_034 (test_p072.SOCTests.test_seeded_correlation_oracle_034) ... ok
test_seeded_correlation_oracle_035 (test_p072.SOCTests.test_seeded_correlation_oracle_035) ... ok
test_seeded_correlation_oracle_036 (test_p072.SOCTests.test_seeded_correlation_oracle_036) ... ok
test_seeded_correlation_oracle_037 (test_p072.SOCTests.test_seeded_correlation_oracle_037) ... ok
test_seeded_correlation_oracle_038 (test_p072.SOCTests.test_seeded_correlation_oracle_038) ... ok
test_seeded_correlation_oracle_039 (test_p072.SOCTests.test_seeded_correlation_oracle_039) ... ok
test_seeded_correlation_oracle_040 (test_p072.SOCTests.test_seeded_correlation_oracle_040) ... ok
test_seeded_correlation_oracle_041 (test_p072.SOCTests.test_seeded_correlation_oracle_041) ... ok
test_seeded_correlation_oracle_042 (test_p072.SOCTests.test_seeded_correlation_oracle_042) ... ok
test_seeded_correlation_oracle_043 (test_p072.SOCTests.test_seeded_correlation_oracle_043) ... ok
test_seeded_correlation_oracle_044 (test_p072.SOCTests.test_seeded_correlation_oracle_044) ... ok
test_seeded_correlation_oracle_045 (test_p072.SOCTests.test_seeded_correlation_oracle_045) ... ok
test_seeded_correlation_oracle_046 (test_p072.SOCTests.test_seeded_correlation_oracle_046) ... ok
test_seeded_correlation_oracle_047 (test_p072.SOCTests.test_seeded_correlation_oracle_047) ... ok
test_seeded_correlation_oracle_048 (test_p072.SOCTests.test_seeded_correlation_oracle_048) ... ok
test_seeded_correlation_oracle_049 (test_p072.SOCTests.test_seeded_correlation_oracle_049) ... ok
test_seeded_correlation_oracle_050 (test_p072.SOCTests.test_seeded_correlation_oracle_050) ... ok
test_seeded_correlation_oracle_051 (test_p072.SOCTests.test_seeded_correlation_oracle_051) ... ok
test_seeded_correlation_oracle_052 (test_p072.SOCTests.test_seeded_correlation_oracle_052) ... ok
test_seeded_correlation_oracle_053 (test_p072.SOCTests.test_seeded_correlation_oracle_053) ... ok
test_seeded_correlation_oracle_054 (test_p072.SOCTests.test_seeded_correlation_oracle_054) ... ok
test_seeded_correlation_oracle_055 (test_p072.SOCTests.test_seeded_correlation_oracle_055) ... ok
test_seeded_correlation_oracle_056 (test_p072.SOCTests.test_seeded_correlation_oracle_056) ... ok
test_seeded_correlation_oracle_057 (test_p072.SOCTests.test_seeded_correlation_oracle_057) ... ok
test_seeded_correlation_oracle_058 (test_p072.SOCTests.test_seeded_correlation_oracle_058) ... ok
test_seeded_correlation_oracle_059 (test_p072.SOCTests.test_seeded_correlation_oracle_059) ... ok
test_seeded_correlation_oracle_060 (test_p072.SOCTests.test_seeded_correlation_oracle_060) ... ok
test_seeded_correlation_oracle_061 (test_p072.SOCTests.test_seeded_correlation_oracle_061) ... ok
test_seeded_correlation_oracle_062 (test_p072.SOCTests.test_seeded_correlation_oracle_062) ... ok
test_seeded_correlation_oracle_063 (test_p072.SOCTests.test_seeded_correlation_oracle_063) ... ok
test_seeded_correlation_oracle_064 (test_p072.SOCTests.test_seeded_correlation_oracle_064) ... ok
test_seeded_correlation_oracle_065 (test_p072.SOCTests.test_seeded_correlation_oracle_065) ... ok
test_seeded_correlation_oracle_066 (test_p072.SOCTests.test_seeded_correlation_oracle_066) ... ok
test_seeded_correlation_oracle_067 (test_p072.SOCTests.test_seeded_correlation_oracle_067) ... ok
test_seeded_correlation_oracle_068 (test_p072.SOCTests.test_seeded_correlation_oracle_068) ... ok
test_seeded_correlation_oracle_069 (test_p072.SOCTests.test_seeded_correlation_oracle_069) ... ok
test_seeded_correlation_oracle_070 (test_p072.SOCTests.test_seeded_correlation_oracle_070) ... ok
test_seeded_correlation_oracle_071 (test_p072.SOCTests.test_seeded_correlation_oracle_071) ... ok
test_seeded_correlation_oracle_072 (test_p072.SOCTests.test_seeded_correlation_oracle_072) ... ok
test_seeded_correlation_oracle_073 (test_p072.SOCTests.test_seeded_correlation_oracle_073) ... ok
test_seeded_correlation_oracle_074 (test_p072.SOCTests.test_seeded_correlation_oracle_074) ... ok
test_seeded_correlation_oracle_075 (test_p072.SOCTests.test_seeded_correlation_oracle_075) ... ok
test_seeded_correlation_oracle_076 (test_p072.SOCTests.test_seeded_correlation_oracle_076) ... ok
test_seeded_correlation_oracle_077 (test_p072.SOCTests.test_seeded_correlation_oracle_077) ... ok
test_seeded_correlation_oracle_078 (test_p072.SOCTests.test_seeded_correlation_oracle_078) ... ok
test_seeded_correlation_oracle_079 (test_p072.SOCTests.test_seeded_correlation_oracle_079) ... ok
test_seeded_correlation_oracle_080 (test_p072.SOCTests.test_seeded_correlation_oracle_080) ... ok
test_seeded_correlation_oracle_081 (test_p072.SOCTests.test_seeded_correlation_oracle_081) ... ok
test_seeded_correlation_oracle_082 (test_p072.SOCTests.test_seeded_correlation_oracle_082) ... ok
test_seeded_correlation_oracle_083 (test_p072.SOCTests.test_seeded_correlation_oracle_083) ... ok
test_seeded_correlation_oracle_084 (test_p072.SOCTests.test_seeded_correlation_oracle_084) ... ok
test_seeded_correlation_oracle_085 (test_p072.SOCTests.test_seeded_correlation_oracle_085) ... ok
test_seeded_correlation_oracle_086 (test_p072.SOCTests.test_seeded_correlation_oracle_086) ... ok
test_seeded_correlation_oracle_087 (test_p072.SOCTests.test_seeded_correlation_oracle_087) ... ok
test_seeded_correlation_oracle_088 (test_p072.SOCTests.test_seeded_correlation_oracle_088) ... ok
test_seeded_correlation_oracle_089 (test_p072.SOCTests.test_seeded_correlation_oracle_089) ... ok
test_seeded_correlation_oracle_090 (test_p072.SOCTests.test_seeded_correlation_oracle_090) ... ok
test_seeded_correlation_oracle_091 (test_p072.SOCTests.test_seeded_correlation_oracle_091) ... ok
test_seeded_correlation_oracle_092 (test_p072.SOCTests.test_seeded_correlation_oracle_092) ... ok
test_seeded_correlation_oracle_093 (test_p072.SOCTests.test_seeded_correlation_oracle_093) ... ok
test_seeded_correlation_oracle_094 (test_p072.SOCTests.test_seeded_correlation_oracle_094) ... ok
test_seeded_correlation_oracle_095 (test_p072.SOCTests.test_seeded_correlation_oracle_095) ... ok
test_seeded_correlation_oracle_096 (test_p072.SOCTests.test_seeded_correlation_oracle_096) ... ok
test_seeded_correlation_oracle_097 (test_p072.SOCTests.test_seeded_correlation_oracle_097) ... ok
test_seeded_correlation_oracle_098 (test_p072.SOCTests.test_seeded_correlation_oracle_098) ... ok
test_seeded_correlation_oracle_099 (test_p072.SOCTests.test_seeded_correlation_oracle_099) ... ok
test_stream_keeps_rejection_evidence_and_continues (test_p072.SOCTests.test_stream_keeps_rejection_evidence_and_continues) ... ok

----------------------------------------------------------------------
Ran 111 tests in 0.194s

OK
```

## Demo — processi separati dalle suite

Questi output provengono dalle demo eseguite dal runner. Non costituiscono nuovi metodi unittest.

### 002 · demo_mini_soc

Comando registrato (array degli argomenti; segnaposto dei metadati documentati nel manifest):

```json
["<PYTHON_HOME>/bin/python", "-B", "src/mini_soc.py"]
```

Esito: **PASS** · codice di uscita: `0`.

**stdout** — [file TXT](streams/002_demo_mini_soc.stdout.txt)

```text
riga 1: []
riga 2: []
riga 3: ['repeated_login_failures']
riga 4: ['admin_login_unusual_country']
riga 5: ['missing_country']
riga 6: ['invalid_event']
```

**stderr** — [file TXT](streams/002_demo_mini_soc.stderr.txt)

Il processo non ha emesso byte su stderr. Il file collegato è vuoto (0 byte).

## Controlli runtime

Il record di questo progetto non contiene controlli classificati come `runtime_check`. L’assenza non aggiunge una verifica runtime alle suite del progetto.

## Verifica e provenienza

[Registro strutturato](registro.json) · [Hash e trasformazioni](MANIFEST.json) · [Policy](../AUDIT.md) · [Indice](../README.md)
