# P070 — output reali dei collaudi

Esito registrato: **PASS**. [Run 39849393701](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701) · [job 120071206449](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701/job/120071206449).

Commit del runner: `44cd421247ca2bfe838baa735cf6180134f80464`. Sorgenti applicativi congelati: `32e201b1fb1258c4e7c77d32af323b966647b908`.

Ambiente registrato: Ubuntu 24.04 x86_64; Python 3.12.15 (main, Oct  1 2026, 02:35:59) [GCC 13.3.0]. Artifact: `p041-p080-core-39849393701-1` (ID `12456886835`); record originale: `P070/results.json`.

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

Rapporto registrato: 108 metodi unittest; failures 0, errors 0, skipped 0; sottocasi dichiarati 0.

**stdout** — [file TXT](streams/001_unittest_project_suite.stdout.txt)

```text
{"errors": 0, "failures": 0, "skipped": 0, "tests_run": 108}
```

**stderr** — [file TXT](streams/001_unittest_project_suite.stderr.txt)

```text
test_backup_digest_contract (test_p070.IncidentTests.test_backup_digest_contract) ... ok
test_bad_assets_rejected (test_p070.IncidentTests.test_bad_assets_rejected) ... ok
test_complete_workflow_and_audit (test_p070.IncidentTests.test_complete_workflow_and_audit) ... ok
test_empty_actions_and_early_evidence_rejected (test_p070.IncidentTests.test_empty_actions_and_early_evidence_rejected) ... ok
test_malformed_evidence_rejected (test_p070.IncidentTests.test_malformed_evidence_rejected) ... ok
test_priority_order_ties_and_copies (test_p070.IncidentTests.test_priority_order_ties_and_copies) ... ok
test_recover_requires_evidence_and_rejections_do_not_change_state (test_p070.IncidentTests.test_recover_requires_evidence_and_rejections_do_not_change_state) ... ok
test_seeded_integrity_and_priority_000 (test_p070.IncidentTests.test_seeded_integrity_and_priority_000) ... ok
test_seeded_integrity_and_priority_001 (test_p070.IncidentTests.test_seeded_integrity_and_priority_001) ... ok
test_seeded_integrity_and_priority_002 (test_p070.IncidentTests.test_seeded_integrity_and_priority_002) ... ok
test_seeded_integrity_and_priority_003 (test_p070.IncidentTests.test_seeded_integrity_and_priority_003) ... ok
test_seeded_integrity_and_priority_004 (test_p070.IncidentTests.test_seeded_integrity_and_priority_004) ... ok
test_seeded_integrity_and_priority_005 (test_p070.IncidentTests.test_seeded_integrity_and_priority_005) ... ok
test_seeded_integrity_and_priority_006 (test_p070.IncidentTests.test_seeded_integrity_and_priority_006) ... ok
test_seeded_integrity_and_priority_007 (test_p070.IncidentTests.test_seeded_integrity_and_priority_007) ... ok
test_seeded_integrity_and_priority_008 (test_p070.IncidentTests.test_seeded_integrity_and_priority_008) ... ok
test_seeded_integrity_and_priority_009 (test_p070.IncidentTests.test_seeded_integrity_and_priority_009) ... ok
test_seeded_integrity_and_priority_010 (test_p070.IncidentTests.test_seeded_integrity_and_priority_010) ... ok
test_seeded_integrity_and_priority_011 (test_p070.IncidentTests.test_seeded_integrity_and_priority_011) ... ok
test_seeded_integrity_and_priority_012 (test_p070.IncidentTests.test_seeded_integrity_and_priority_012) ... ok
test_seeded_integrity_and_priority_013 (test_p070.IncidentTests.test_seeded_integrity_and_priority_013) ... ok
test_seeded_integrity_and_priority_014 (test_p070.IncidentTests.test_seeded_integrity_and_priority_014) ... ok
test_seeded_integrity_and_priority_015 (test_p070.IncidentTests.test_seeded_integrity_and_priority_015) ... ok
test_seeded_integrity_and_priority_016 (test_p070.IncidentTests.test_seeded_integrity_and_priority_016) ... ok
test_seeded_integrity_and_priority_017 (test_p070.IncidentTests.test_seeded_integrity_and_priority_017) ... ok
test_seeded_integrity_and_priority_018 (test_p070.IncidentTests.test_seeded_integrity_and_priority_018) ... ok
test_seeded_integrity_and_priority_019 (test_p070.IncidentTests.test_seeded_integrity_and_priority_019) ... ok
test_seeded_integrity_and_priority_020 (test_p070.IncidentTests.test_seeded_integrity_and_priority_020) ... ok
test_seeded_integrity_and_priority_021 (test_p070.IncidentTests.test_seeded_integrity_and_priority_021) ... ok
test_seeded_integrity_and_priority_022 (test_p070.IncidentTests.test_seeded_integrity_and_priority_022) ... ok
test_seeded_integrity_and_priority_023 (test_p070.IncidentTests.test_seeded_integrity_and_priority_023) ... ok
test_seeded_integrity_and_priority_024 (test_p070.IncidentTests.test_seeded_integrity_and_priority_024) ... ok
test_seeded_integrity_and_priority_025 (test_p070.IncidentTests.test_seeded_integrity_and_priority_025) ... ok
test_seeded_integrity_and_priority_026 (test_p070.IncidentTests.test_seeded_integrity_and_priority_026) ... ok
test_seeded_integrity_and_priority_027 (test_p070.IncidentTests.test_seeded_integrity_and_priority_027) ... ok
test_seeded_integrity_and_priority_028 (test_p070.IncidentTests.test_seeded_integrity_and_priority_028) ... ok
test_seeded_integrity_and_priority_029 (test_p070.IncidentTests.test_seeded_integrity_and_priority_029) ... ok
test_seeded_integrity_and_priority_030 (test_p070.IncidentTests.test_seeded_integrity_and_priority_030) ... ok
test_seeded_integrity_and_priority_031 (test_p070.IncidentTests.test_seeded_integrity_and_priority_031) ... ok
test_seeded_integrity_and_priority_032 (test_p070.IncidentTests.test_seeded_integrity_and_priority_032) ... ok
test_seeded_integrity_and_priority_033 (test_p070.IncidentTests.test_seeded_integrity_and_priority_033) ... ok
test_seeded_integrity_and_priority_034 (test_p070.IncidentTests.test_seeded_integrity_and_priority_034) ... ok
test_seeded_integrity_and_priority_035 (test_p070.IncidentTests.test_seeded_integrity_and_priority_035) ... ok
test_seeded_integrity_and_priority_036 (test_p070.IncidentTests.test_seeded_integrity_and_priority_036) ... ok
test_seeded_integrity_and_priority_037 (test_p070.IncidentTests.test_seeded_integrity_and_priority_037) ... ok
test_seeded_integrity_and_priority_038 (test_p070.IncidentTests.test_seeded_integrity_and_priority_038) ... ok
test_seeded_integrity_and_priority_039 (test_p070.IncidentTests.test_seeded_integrity_and_priority_039) ... ok
test_seeded_integrity_and_priority_040 (test_p070.IncidentTests.test_seeded_integrity_and_priority_040) ... ok
test_seeded_integrity_and_priority_041 (test_p070.IncidentTests.test_seeded_integrity_and_priority_041) ... ok
test_seeded_integrity_and_priority_042 (test_p070.IncidentTests.test_seeded_integrity_and_priority_042) ... ok
test_seeded_integrity_and_priority_043 (test_p070.IncidentTests.test_seeded_integrity_and_priority_043) ... ok
test_seeded_integrity_and_priority_044 (test_p070.IncidentTests.test_seeded_integrity_and_priority_044) ... ok
test_seeded_integrity_and_priority_045 (test_p070.IncidentTests.test_seeded_integrity_and_priority_045) ... ok
test_seeded_integrity_and_priority_046 (test_p070.IncidentTests.test_seeded_integrity_and_priority_046) ... ok
test_seeded_integrity_and_priority_047 (test_p070.IncidentTests.test_seeded_integrity_and_priority_047) ... ok
test_seeded_integrity_and_priority_048 (test_p070.IncidentTests.test_seeded_integrity_and_priority_048) ... ok
test_seeded_integrity_and_priority_049 (test_p070.IncidentTests.test_seeded_integrity_and_priority_049) ... ok
test_seeded_integrity_and_priority_050 (test_p070.IncidentTests.test_seeded_integrity_and_priority_050) ... ok
test_seeded_integrity_and_priority_051 (test_p070.IncidentTests.test_seeded_integrity_and_priority_051) ... ok
test_seeded_integrity_and_priority_052 (test_p070.IncidentTests.test_seeded_integrity_and_priority_052) ... ok
test_seeded_integrity_and_priority_053 (test_p070.IncidentTests.test_seeded_integrity_and_priority_053) ... ok
test_seeded_integrity_and_priority_054 (test_p070.IncidentTests.test_seeded_integrity_and_priority_054) ... ok
test_seeded_integrity_and_priority_055 (test_p070.IncidentTests.test_seeded_integrity_and_priority_055) ... ok
test_seeded_integrity_and_priority_056 (test_p070.IncidentTests.test_seeded_integrity_and_priority_056) ... ok
test_seeded_integrity_and_priority_057 (test_p070.IncidentTests.test_seeded_integrity_and_priority_057) ... ok
test_seeded_integrity_and_priority_058 (test_p070.IncidentTests.test_seeded_integrity_and_priority_058) ... ok
test_seeded_integrity_and_priority_059 (test_p070.IncidentTests.test_seeded_integrity_and_priority_059) ... ok
test_seeded_integrity_and_priority_060 (test_p070.IncidentTests.test_seeded_integrity_and_priority_060) ... ok
test_seeded_integrity_and_priority_061 (test_p070.IncidentTests.test_seeded_integrity_and_priority_061) ... ok
test_seeded_integrity_and_priority_062 (test_p070.IncidentTests.test_seeded_integrity_and_priority_062) ... ok
test_seeded_integrity_and_priority_063 (test_p070.IncidentTests.test_seeded_integrity_and_priority_063) ... ok
test_seeded_integrity_and_priority_064 (test_p070.IncidentTests.test_seeded_integrity_and_priority_064) ... ok
test_seeded_integrity_and_priority_065 (test_p070.IncidentTests.test_seeded_integrity_and_priority_065) ... ok
test_seeded_integrity_and_priority_066 (test_p070.IncidentTests.test_seeded_integrity_and_priority_066) ... ok
test_seeded_integrity_and_priority_067 (test_p070.IncidentTests.test_seeded_integrity_and_priority_067) ... ok
test_seeded_integrity_and_priority_068 (test_p070.IncidentTests.test_seeded_integrity_and_priority_068) ... ok
test_seeded_integrity_and_priority_069 (test_p070.IncidentTests.test_seeded_integrity_and_priority_069) ... ok
test_seeded_integrity_and_priority_070 (test_p070.IncidentTests.test_seeded_integrity_and_priority_070) ... ok
test_seeded_integrity_and_priority_071 (test_p070.IncidentTests.test_seeded_integrity_and_priority_071) ... ok
test_seeded_integrity_and_priority_072 (test_p070.IncidentTests.test_seeded_integrity_and_priority_072) ... ok
test_seeded_integrity_and_priority_073 (test_p070.IncidentTests.test_seeded_integrity_and_priority_073) ... ok
test_seeded_integrity_and_priority_074 (test_p070.IncidentTests.test_seeded_integrity_and_priority_074) ... ok
test_seeded_integrity_and_priority_075 (test_p070.IncidentTests.test_seeded_integrity_and_priority_075) ... ok
test_seeded_integrity_and_priority_076 (test_p070.IncidentTests.test_seeded_integrity_and_priority_076) ... ok
test_seeded_integrity_and_priority_077 (test_p070.IncidentTests.test_seeded_integrity_and_priority_077) ... ok
test_seeded_integrity_and_priority_078 (test_p070.IncidentTests.test_seeded_integrity_and_priority_078) ... ok
test_seeded_integrity_and_priority_079 (test_p070.IncidentTests.test_seeded_integrity_and_priority_079) ... ok
test_seeded_integrity_and_priority_080 (test_p070.IncidentTests.test_seeded_integrity_and_priority_080) ... ok
test_seeded_integrity_and_priority_081 (test_p070.IncidentTests.test_seeded_integrity_and_priority_081) ... ok
test_seeded_integrity_and_priority_082 (test_p070.IncidentTests.test_seeded_integrity_and_priority_082) ... ok
test_seeded_integrity_and_priority_083 (test_p070.IncidentTests.test_seeded_integrity_and_priority_083) ... ok
test_seeded_integrity_and_priority_084 (test_p070.IncidentTests.test_seeded_integrity_and_priority_084) ... ok
test_seeded_integrity_and_priority_085 (test_p070.IncidentTests.test_seeded_integrity_and_priority_085) ... ok
test_seeded_integrity_and_priority_086 (test_p070.IncidentTests.test_seeded_integrity_and_priority_086) ... ok
test_seeded_integrity_and_priority_087 (test_p070.IncidentTests.test_seeded_integrity_and_priority_087) ... ok
test_seeded_integrity_and_priority_088 (test_p070.IncidentTests.test_seeded_integrity_and_priority_088) ... ok
test_seeded_integrity_and_priority_089 (test_p070.IncidentTests.test_seeded_integrity_and_priority_089) ... ok
test_seeded_integrity_and_priority_090 (test_p070.IncidentTests.test_seeded_integrity_and_priority_090) ... ok
test_seeded_integrity_and_priority_091 (test_p070.IncidentTests.test_seeded_integrity_and_priority_091) ... ok
test_seeded_integrity_and_priority_092 (test_p070.IncidentTests.test_seeded_integrity_and_priority_092) ... ok
test_seeded_integrity_and_priority_093 (test_p070.IncidentTests.test_seeded_integrity_and_priority_093) ... ok
test_seeded_integrity_and_priority_094 (test_p070.IncidentTests.test_seeded_integrity_and_priority_094) ... ok
test_seeded_integrity_and_priority_095 (test_p070.IncidentTests.test_seeded_integrity_and_priority_095) ... ok
test_seeded_integrity_and_priority_096 (test_p070.IncidentTests.test_seeded_integrity_and_priority_096) ... ok
test_seeded_integrity_and_priority_097 (test_p070.IncidentTests.test_seeded_integrity_and_priority_097) ... ok
test_seeded_integrity_and_priority_098 (test_p070.IncidentTests.test_seeded_integrity_and_priority_098) ... ok
test_seeded_integrity_and_priority_099 (test_p070.IncidentTests.test_seeded_integrity_and_priority_099) ... ok
test_terminal_state_rejected (test_p070.IncidentTests.test_terminal_state_rejected) ... ok

----------------------------------------------------------------------
Ran 108 tests in 0.013s

OK
```

## Demo — processi separati dalle suite

Questi output provengono dalle demo eseguite dal runner. Non costituiscono nuovi metodi unittest.

### 002 · demo_incident_response

Comando registrato (array degli argomenti; segnaposto dei metadati documentati nel manifest):

```json
["<PYTHON_HOME>/bin/python", "-B", "src/incident_response.py"]
```

Esito: **PASS** · codice di uscita: `0`.

**stdout** — [file TXT](streams/002_demo_incident_response.stdout.txt)

```text
DETECTED
CONTAINED
ERADICATED
RECOVERED
LESSONS_LEARNED
Byte ripristinati: 10
Backup alterato: RIFIUTATO
```

**stderr** — [file TXT](streams/002_demo_incident_response.stderr.txt)

Il processo non ha emesso byte su stderr. Il file collegato è vuoto (0 byte).

## Controlli runtime

Il record di questo progetto non contiene controlli classificati come `runtime_check`. L’assenza non aggiunge una verifica runtime alle suite del progetto.

## Verifica e provenienza

[Registro strutturato](registro.json) · [Hash e trasformazioni](MANIFEST.json) · [Policy](../AUDIT.md) · [Indice](../README.md)
