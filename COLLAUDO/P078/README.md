# P078: output dei collaudi

[Indice dei collaudi](../README.md) · [Codice e istruzioni](../../projects/P078/README.md)

Esito registrato: **PASS**. [Run 39849393701](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701) · [job 120071206449](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701/job/120071206449).

Commit del runner: `44cd421247ca2bfe838baa735cf6180134f80464`. Sorgenti applicativi congelati: `32e201b1fb1258c4e7c77d32af323b966647b908`.

Ambiente registrato: Ubuntu 24.04 x86_64; Python 3.12.15 (main, Oct  1 2026, 02:35:59) [GCC 13.3.0]. Artifact: `p041-p080-core-39849393701-1` (ID `12456886835`); record originale: `P078/results.json`.

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

Rapporto registrato: 113 metodi unittest; failures 0, errors 0, skipped 0.

**stdout** — [file TXT](streams/001_unittest_project_suite.stdout.txt)

```text
{
  "project": "P078",
  "tests_run": 113,
  "failures": 0,
  "errors": 0,
  "skipped": 0,
  "seeded_cases": 100,
  "passed": true,
  "seconds": 0.13403038299998116
}
```

**stderr** — [file TXT](streams/001_unittest_project_suite.stderr.txt)

```text
test_dataset_parameters (test_p078.TestVision.test_dataset_parameters) ... ok
test_dtype_and_nonfinite_validation (test_p078.TestVision.test_dtype_and_nonfinite_validation) ... ok
test_fit_is_deterministic (test_p078.TestVision.test_fit_is_deterministic) ... ok
test_holdout_beats_constant_baseline (test_p078.TestVision.test_holdout_beats_constant_baseline) ... ok
test_ids_and_image_hashes_independent (test_p078.TestVision.test_ids_and_image_hashes_independent) ... ok
test_known_rgb_statistics (test_p078.TestVision.test_known_rgb_statistics) ... ok
test_matrix_from_predictions (test_p078.TestVision.test_matrix_from_predictions) ... ok
test_model_input_validation (test_p078.TestVision.test_model_input_validation) ... ok
test_parameters_validation (test_p078.TestVision.test_parameters_validation) ... ok
test_scaler_fits_training_only (test_p078.TestVision.test_scaler_fits_training_only) ... ok
test_seed_000 (test_p078.TestVision.test_seed_000) ... ok
test_seed_001 (test_p078.TestVision.test_seed_001) ... ok
test_seed_002 (test_p078.TestVision.test_seed_002) ... ok
test_seed_003 (test_p078.TestVision.test_seed_003) ... ok
test_seed_004 (test_p078.TestVision.test_seed_004) ... ok
test_seed_005 (test_p078.TestVision.test_seed_005) ... ok
test_seed_006 (test_p078.TestVision.test_seed_006) ... ok
test_seed_007 (test_p078.TestVision.test_seed_007) ... ok
test_seed_008 (test_p078.TestVision.test_seed_008) ... ok
test_seed_009 (test_p078.TestVision.test_seed_009) ... ok
test_seed_010 (test_p078.TestVision.test_seed_010) ... ok
test_seed_011 (test_p078.TestVision.test_seed_011) ... ok
test_seed_012 (test_p078.TestVision.test_seed_012) ... ok
test_seed_013 (test_p078.TestVision.test_seed_013) ... ok
test_seed_014 (test_p078.TestVision.test_seed_014) ... ok
test_seed_015 (test_p078.TestVision.test_seed_015) ... ok
test_seed_016 (test_p078.TestVision.test_seed_016) ... ok
test_seed_017 (test_p078.TestVision.test_seed_017) ... ok
test_seed_018 (test_p078.TestVision.test_seed_018) ... ok
test_seed_019 (test_p078.TestVision.test_seed_019) ... ok
test_seed_020 (test_p078.TestVision.test_seed_020) ... ok
test_seed_021 (test_p078.TestVision.test_seed_021) ... ok
test_seed_022 (test_p078.TestVision.test_seed_022) ... ok
test_seed_023 (test_p078.TestVision.test_seed_023) ... ok
test_seed_024 (test_p078.TestVision.test_seed_024) ... ok
test_seed_025 (test_p078.TestVision.test_seed_025) ... ok
test_seed_026 (test_p078.TestVision.test_seed_026) ... ok
test_seed_027 (test_p078.TestVision.test_seed_027) ... ok
test_seed_028 (test_p078.TestVision.test_seed_028) ... ok
test_seed_029 (test_p078.TestVision.test_seed_029) ... ok
test_seed_030 (test_p078.TestVision.test_seed_030) ... ok
test_seed_031 (test_p078.TestVision.test_seed_031) ... ok
test_seed_032 (test_p078.TestVision.test_seed_032) ... ok
test_seed_033 (test_p078.TestVision.test_seed_033) ... ok
test_seed_034 (test_p078.TestVision.test_seed_034) ... ok
test_seed_035 (test_p078.TestVision.test_seed_035) ... ok
test_seed_036 (test_p078.TestVision.test_seed_036) ... ok
test_seed_037 (test_p078.TestVision.test_seed_037) ... ok
test_seed_038 (test_p078.TestVision.test_seed_038) ... ok
test_seed_039 (test_p078.TestVision.test_seed_039) ... ok
test_seed_040 (test_p078.TestVision.test_seed_040) ... ok
test_seed_041 (test_p078.TestVision.test_seed_041) ... ok
test_seed_042 (test_p078.TestVision.test_seed_042) ... ok
test_seed_043 (test_p078.TestVision.test_seed_043) ... ok
test_seed_044 (test_p078.TestVision.test_seed_044) ... ok
test_seed_045 (test_p078.TestVision.test_seed_045) ... ok
test_seed_046 (test_p078.TestVision.test_seed_046) ... ok
test_seed_047 (test_p078.TestVision.test_seed_047) ... ok
test_seed_048 (test_p078.TestVision.test_seed_048) ... ok
test_seed_049 (test_p078.TestVision.test_seed_049) ... ok
test_seed_050 (test_p078.TestVision.test_seed_050) ... ok
test_seed_051 (test_p078.TestVision.test_seed_051) ... ok
test_seed_052 (test_p078.TestVision.test_seed_052) ... ok
test_seed_053 (test_p078.TestVision.test_seed_053) ... ok
test_seed_054 (test_p078.TestVision.test_seed_054) ... ok
test_seed_055 (test_p078.TestVision.test_seed_055) ... ok
test_seed_056 (test_p078.TestVision.test_seed_056) ... ok
test_seed_057 (test_p078.TestVision.test_seed_057) ... ok
test_seed_058 (test_p078.TestVision.test_seed_058) ... ok
test_seed_059 (test_p078.TestVision.test_seed_059) ... ok
test_seed_060 (test_p078.TestVision.test_seed_060) ... ok
test_seed_061 (test_p078.TestVision.test_seed_061) ... ok
test_seed_062 (test_p078.TestVision.test_seed_062) ... ok
test_seed_063 (test_p078.TestVision.test_seed_063) ... ok
test_seed_064 (test_p078.TestVision.test_seed_064) ... ok
test_seed_065 (test_p078.TestVision.test_seed_065) ... ok
test_seed_066 (test_p078.TestVision.test_seed_066) ... ok
test_seed_067 (test_p078.TestVision.test_seed_067) ... ok
test_seed_068 (test_p078.TestVision.test_seed_068) ... ok
test_seed_069 (test_p078.TestVision.test_seed_069) ... ok
test_seed_070 (test_p078.TestVision.test_seed_070) ... ok
test_seed_071 (test_p078.TestVision.test_seed_071) ... ok
test_seed_072 (test_p078.TestVision.test_seed_072) ... ok
test_seed_073 (test_p078.TestVision.test_seed_073) ... ok
test_seed_074 (test_p078.TestVision.test_seed_074) ... ok
test_seed_075 (test_p078.TestVision.test_seed_075) ... ok
test_seed_076 (test_p078.TestVision.test_seed_076) ... ok
test_seed_077 (test_p078.TestVision.test_seed_077) ... ok
test_seed_078 (test_p078.TestVision.test_seed_078) ... ok
test_seed_079 (test_p078.TestVision.test_seed_079) ... ok
test_seed_080 (test_p078.TestVision.test_seed_080) ... ok
test_seed_081 (test_p078.TestVision.test_seed_081) ... ok
test_seed_082 (test_p078.TestVision.test_seed_082) ... ok
test_seed_083 (test_p078.TestVision.test_seed_083) ... ok
test_seed_084 (test_p078.TestVision.test_seed_084) ... ok
test_seed_085 (test_p078.TestVision.test_seed_085) ... ok
test_seed_086 (test_p078.TestVision.test_seed_086) ... ok
test_seed_087 (test_p078.TestVision.test_seed_087) ... ok
test_seed_088 (test_p078.TestVision.test_seed_088) ... ok
test_seed_089 (test_p078.TestVision.test_seed_089) ... ok
test_seed_090 (test_p078.TestVision.test_seed_090) ... ok
test_seed_091 (test_p078.TestVision.test_seed_091) ... ok
test_seed_092 (test_p078.TestVision.test_seed_092) ... ok
test_seed_093 (test_p078.TestVision.test_seed_093) ... ok
test_seed_094 (test_p078.TestVision.test_seed_094) ... ok
test_seed_095 (test_p078.TestVision.test_seed_095) ... ok
test_seed_096 (test_p078.TestVision.test_seed_096) ... ok
test_seed_097 (test_p078.TestVision.test_seed_097) ... ok
test_seed_098 (test_p078.TestVision.test_seed_098) ... ok
test_seed_099 (test_p078.TestVision.test_seed_099) ... ok
test_shape_validation (test_p078.TestVision.test_shape_validation) ... ok
test_shift_reveals_palette_shortcut (test_p078.TestVision.test_shift_reveals_palette_shortcut) ... ok
test_shuffled_label_control (test_p078.TestVision.test_shuffled_label_control) ... ok

----------------------------------------------------------------------
Ran 113 tests in 0.134s

OK
```

## Demo — processi separati dalle suite

Questi output provengono dalle demo eseguite dal runner. Non costituiscono nuovi metodi unittest.

### 002 · demo_waste_cv

Comando registrato (array degli argomenti; segnaposto dei metadati documentati nel manifest):

```json
["<PYTHON_HOME>/bin/python", "-B", "src/waste_cv.py"]
```

Esito: **PASS** · codice di uscita: `0`.

**stdout** — [file TXT](streams/002_demo_waste_cv.stdout.txt)

```text
{
  "dataset": "Immagini RGB 24x24 da quattro palette; nessuna fotografia di rifiuti",
  "seed": 78,
  "classes": [
    "carta",
    "plastica",
    "vetro",
    "organico"
  ],
  "split": {
    "train": 240,
    "test": 100,
    "hash_overlap": 0,
    "train_ids": [
      "train-carta-0000",
      "train-carta-0001",
      "train-carta-0002",
      "train-carta-0003",
      "train-carta-0004",
      "train-carta-0005",
      "train-carta-0006",
      "train-carta-0007",
      "train-carta-0008",
      "train-carta-0009",
      "train-carta-0010",
      "train-carta-0011",
      "train-carta-0012",
      "train-carta-0013",
      "train-carta-0014",
      "train-carta-0015",
      "train-carta-0016",
      "train-carta-0017",
      "train-carta-0018",
      "train-carta-0019",
      "train-carta-0020",
      "train-carta-0021",
      "train-carta-0022",
      "train-carta-0023",
      "train-carta-0024",
      "train-carta-0025",
      "train-carta-0026",
      "train-carta-0027",
      "train-carta-0028",
      "train-carta-0029",
      "train-carta-0030",
      "train-carta-0031",
      "train-carta-0032",
      "train-carta-0033",
      "train-carta-0034",
      "train-carta-0035",
      "train-carta-0036",
      "train-carta-0037",
      "train-carta-0038",
      "train-carta-0039",
      "train-carta-0040",
      "train-carta-0041",
      "train-carta-0042",
      "train-carta-0043",
      "train-carta-0044",
      "train-carta-0045",
      "train-carta-0046",
      "train-carta-0047",
      "train-carta-0048",
      "train-carta-0049",
      "train-carta-0050",
      "train-carta-0051",
      "train-carta-0052",
      "train-carta-0053",
      "train-carta-0054",
      "train-carta-0055",
      "train-carta-0056",
      "train-carta-0057",
      "train-carta-0058",
      "train-carta-0059",
      "train-plastica-0000",
      "train-plastica-0001",
      "train-plastica-0002",
      "train-plastica-0003",
      "train-plastica-0004",
      "train-plastica-0005",
      "train-plastica-0006",
      "train-plastica-0007",
      "train-plastica-0008",
      "train-plastica-0009",
      "train-plastica-0010",
      "train-plastica-0011",
      "train-plastica-0012",
      "train-plastica-0013",
      "train-plastica-0014",
      "train-plastica-0015",
      "train-plastica-0016",
      "train-plastica-0017",
      "train-plastica-0018",
      "train-plastica-0019",
      "train-plastica-0020",
      "train-plastica-0021",
      "train-plastica-0022",
      "train-plastica-0023",
      "train-plastica-0024",
      "train-plastica-0025",
      "train-plastica-0026",
      "train-plastica-0027",
      "train-plastica-0028",
      "train-plastica-0029",
      "train-plastica-0030",
      "train-plastica-0031",
      "train-plastica-0032",
      "train-plastica-0033",
      "train-plastica-0034",
      "train-plastica-0035",
      "train-plastica-0036",
      "train-plastica-0037",
      "train-plastica-0038",
      "train-plastica-0039",
      "train-plastica-0040",
      "train-plastica-0041",
      "train-plastica-0042",
      "train-plastica-0043",
      "train-plastica-0044",
      "train-plastica-0045",
      "train-plastica-0046",
      "train-plastica-0047",
      "train-plastica-0048",
      "train-plastica-0049",
      "train-plastica-0050",
      "train-plastica-0051",
      "train-plastica-0052",
      "train-plastica-0053",
      "train-plastica-0054",
      "train-plastica-0055",
      "train-plastica-0056",
      "train-plastica-0057",
      "train-plastica-0058",
      "train-plastica-0059",
      "train-vetro-0000",
      "train-vetro-0001",
      "train-vetro-0002",
      "train-vetro-0003",
      "train-vetro-0004",
      "train-vetro-0005",
      "train-vetro-0006",
      "train-vetro-0007",
      "train-vetro-0008",
      "train-vetro-0009",
      "train-vetro-0010",
      "train-vetro-0011",
      "train-vetro-0012",
      "train-vetro-0013",
      "train-vetro-0014",
      "train-vetro-0015",
      "train-vetro-0016",
      "train-vetro-0017",
      "train-vetro-0018",
      "train-vetro-0019",
      "train-vetro-0020",
      "train-vetro-0021",
      "train-vetro-0022",
      "train-vetro-0023",
      "train-vetro-0024",
      "train-vetro-0025",
      "train-vetro-0026",
      "train-vetro-0027",
      "train-vetro-0028",
      "train-vetro-0029",
      "train-vetro-0030",
      "train-vetro-0031",
      "train-vetro-0032",
      "train-vetro-0033",
      "train-vetro-0034",
      "train-vetro-0035",
      "train-vetro-0036",
      "train-vetro-0037",
      "train-vetro-0038",
      "train-vetro-0039",
      "train-vetro-0040",
      "train-vetro-0041",
      "train-vetro-0042",
      "train-vetro-0043",
      "train-vetro-0044",
      "train-vetro-0045",
      "train-vetro-0046",
      "train-vetro-0047",
      "train-vetro-0048",
      "train-vetro-0049",
      "train-vetro-0050",
      "train-vetro-0051",
      "train-vetro-0052",
      "train-vetro-0053",
      "train-vetro-0054",
      "train-vetro-0055",
      "train-vetro-0056",
      "train-vetro-0057",
      "train-vetro-0058",
      "train-vetro-0059",
      "train-organico-0000",
      "train-organico-0001",
      "train-organico-0002",
      "train-organico-0003",
      "train-organico-0004",
      "train-organico-0005",
      "train-organico-0006",
      "train-organico-0007",
      "train-organico-0008",
      "train-organico-0009",
      "train-organico-0010",
      "train-organico-0011",
      "train-organico-0012",
      "train-organico-0013",
      "train-organico-0014",
      "train-organico-0015",
      "train-organico-0016",
      "train-organico-0017",
      "train-organico-0018",
      "train-organico-0019",
      "train-organico-0020",
      "train-organico-0021",
      "train-organico-0022",
      "train-organico-0023",
      "train-organico-0024",
      "train-organico-0025",
      "train-organico-0026",
      "train-organico-0027",
      "train-organico-0028",
      "train-organico-0029",
      "train-organico-0030",
      "train-organico-0031",
      "train-organico-0032",
      "train-organico-0033",
      "train-organico-0034",
      "train-organico-0035",
      "train-organico-0036",
      "train-organico-0037",
      "train-organico-0038",
      "train-organico-0039",
      "train-organico-0040",
      "train-organico-0041",
      "train-organico-0042",
      "train-organico-0043",
      "train-organico-0044",
      "train-organico-0045",
      "train-organico-0046",
      "train-organico-0047",
      "train-organico-0048",
      "train-organico-0049",
      "train-organico-0050",
      "train-organico-0051",
      "train-organico-0052",
      "train-organico-0053",
      "train-organico-0054",
      "train-organico-0055",
      "train-organico-0056",
      "train-organico-0057",
      "train-organico-0058",
      "train-organico-0059"
    ],
    "test_ids": [
      "test-carta-0000",
      "test-carta-0001",
      "test-carta-0002",
      "test-carta-0003",
      "test-carta-0004",
      "test-carta-0005",
      "test-carta-0006",
      "test-carta-0007",
      "test-carta-0008",
      "test-carta-0009",
      "test-carta-0010",
      "test-carta-0011",
      "test-carta-0012",
      "test-carta-0013",
      "test-carta-0014",
      "test-carta-0015",
      "test-carta-0016",
      "test-carta-0017",
      "test-carta-0018",
      "test-carta-0019",
      "test-carta-0020",
      "test-carta-0021",
      "test-carta-0022",
      "test-carta-0023",
      "test-carta-0024",
      "test-plastica-0000",
      "test-plastica-0001",
      "test-plastica-0002",
      "test-plastica-0003",
      "test-plastica-0004",
      "test-plastica-0005",
      "test-plastica-0006",
      "test-plastica-0007",
      "test-plastica-0008",
      "test-plastica-0009",
      "test-plastica-0010",
      "test-plastica-0011",
      "test-plastica-0012",
      "test-plastica-0013",
      "test-plastica-0014",
      "test-plastica-0015",
      "test-plastica-0016",
      "test-plastica-0017",
      "test-plastica-0018",
      "test-plastica-0019",
      "test-plastica-0020",
      "test-plastica-0021",
      "test-plastica-0022",
      "test-plastica-0023",
      "test-plastica-0024",
      "test-vetro-0000",
      "test-vetro-0001",
      "test-vetro-0002",
      "test-vetro-0003",
      "test-vetro-0004",
      "test-vetro-0005",
      "test-vetro-0006",
      "test-vetro-0007",
      "test-vetro-0008",
      "test-vetro-0009",
      "test-vetro-0010",
      "test-vetro-0011",
      "test-vetro-0012",
      "test-vetro-0013",
      "test-vetro-0014",
      "test-vetro-0015",
      "test-vetro-0016",
      "test-vetro-0017",
      "test-vetro-0018",
      "test-vetro-0019",
      "test-vetro-0020",
      "test-vetro-0021",
      "test-vetro-0022",
      "test-vetro-0023",
      "test-vetro-0024",
      "test-organico-0000",
      "test-organico-0001",
      "test-organico-0002",
      "test-organico-0003",
      "test-organico-0004",
      "test-organico-0005",
      "test-organico-0006",
      "test-organico-0007",
      "test-organico-0008",
      "test-organico-0009",
      "test-organico-0010",
      "test-organico-0011",
      "test-organico-0012",
      "test-organico-0013",
      "test-organico-0014",
      "test-organico-0015",
      "test-organico-0016",
      "test-organico-0017",
      "test-organico-0018",
      "test-organico-0019",
      "test-organico-0020",
      "test-organico-0021",
      "test-organico-0022",
      "test-organico-0023",
      "test-organico-0024"
    ]
  },
  "accuracy": 1.0,
  "f1_macro": 1.0,
  "confusion_matrix": [
    [
      25,
      0,
      0,
      0
    ],
    [
      0,
      25,
      0,
      0
    ],
    [
      0,
      0,
      25,
      0
    ],
    [
      0,
      0,
      0,
      25
    ]
  ],
  "baseline_accuracy": 0.25,
  "shifted_palette": {
    "accuracy": 0.0,
    "f1_macro": 0.0,
    "confusion_matrix": [
      [
        0,
        25,
        0,
        0
      ],
      [
        0,
        0,
        25,
        0
      ],
      [
        0,
        0,
        0,
        25
      ],
      [
        25,
        0,
        0,
        0
      ]
    ]
  },
  "shuffled_labels": {
    "accuracy": 0.33,
    "f1_macro": 0.3005302170520641,
    "confusion_matrix": [
      [
        7,
        9,
        4,
        5
      ],
      [
        11,
        2,
        2,
        10
      ],
      [
        1,
        0,
        23,
        1
      ],
      [
        9,
        12,
        3,
        1
      ]
    ]
  },
  "predictions": [
    {
      "id": "test-carta-0000",
      "truth": "carta",
      "prediction": "carta"
    },
    {
      "id": "test-carta-0001",
      "truth": "carta",
      "prediction": "carta"
    },
    {
      "id": "test-carta-0002",
      "truth": "carta",
      "prediction": "carta"
    },
    {
      "id": "test-carta-0003",
      "truth": "carta",
      "prediction": "carta"
    },
    {
      "id": "test-carta-0004",
      "truth": "carta",
      "prediction": "carta"
    },
    {
      "id": "test-carta-0005",
      "truth": "carta",
      "prediction": "carta"
    },
    {
      "id": "test-carta-0006",
      "truth": "carta",
      "prediction": "carta"
    },
    {
      "id": "test-carta-0007",
      "truth": "carta",
      "prediction": "carta"
    },
    {
      "id": "test-carta-0008",
      "truth": "carta",
      "prediction": "carta"
    },
    {
      "id": "test-carta-0009",
      "truth": "carta",
      "prediction": "carta"
    },
    {
      "id": "test-carta-0010",
      "truth": "carta",
      "prediction": "carta"
    },
    {
      "id": "test-carta-0011",
      "truth": "carta",
      "prediction": "carta"
    },
    {
      "id": "test-carta-0012",
      "truth": "carta",
      "prediction": "carta"
    },
    {
      "id": "test-carta-0013",
      "truth": "carta",
      "prediction": "carta"
    },
    {
      "id": "test-carta-0014",
      "truth": "carta",
      "prediction": "carta"
    },
    {
      "id": "test-carta-0015",
      "truth": "carta",
      "prediction": "carta"
    },
    {
      "id": "test-carta-0016",
      "truth": "carta",
      "prediction": "carta"
    },
    {
      "id": "test-carta-0017",
      "truth": "carta",
      "prediction": "carta"
    },
    {
      "id": "test-carta-0018",
      "truth": "carta",
      "prediction": "carta"
    },
    {
      "id": "test-carta-0019",
      "truth": "carta",
      "prediction": "carta"
    },
    {
      "id": "test-carta-0020",
      "truth": "carta",
      "prediction": "carta"
    },
    {
      "id": "test-carta-0021",
      "truth": "carta",
      "prediction": "carta"
    },
    {
      "id": "test-carta-0022",
      "truth": "carta",
      "prediction": "carta"
    },
    {
      "id": "test-carta-0023",
      "truth": "carta",
      "prediction": "carta"
    },
    {
      "id": "test-carta-0024",
      "truth": "carta",
      "prediction": "carta"
    },
    {
      "id": "test-plastica-0000",
      "truth": "plastica",
      "prediction": "plastica"
    },
    {
      "id": "test-plastica-0001",
      "truth": "plastica",
      "prediction": "plastica"
    },
    {
      "id": "test-plastica-0002",
      "truth": "plastica",
      "prediction": "plastica"
    },
    {
      "id": "test-plastica-0003",
      "truth": "plastica",
      "prediction": "plastica"
    },
    {
      "id": "test-plastica-0004",
      "truth": "plastica",
      "prediction": "plastica"
    },
    {
      "id": "test-plastica-0005",
      "truth": "plastica",
      "prediction": "plastica"
    },
    {
      "id": "test-plastica-0006",
      "truth": "plastica",
      "prediction": "plastica"
    },
    {
      "id": "test-plastica-0007",
      "truth": "plastica",
      "prediction": "plastica"
    },
    {
      "id": "test-plastica-0008",
      "truth": "plastica",
      "prediction": "plastica"
    },
    {
      "id": "test-plastica-0009",
      "truth": "plastica",
      "prediction": "plastica"
    },
    {
      "id": "test-plastica-0010",
      "truth": "plastica",
      "prediction": "plastica"
    },
    {
      "id": "test-plastica-0011",
      "truth": "plastica",
      "prediction": "plastica"
    },
    {
      "id": "test-plastica-0012",
      "truth": "plastica",
      "prediction": "plastica"
    },
    {
      "id": "test-plastica-0013",
      "truth": "plastica",
      "prediction": "plastica"
    },
    {
      "id": "test-plastica-0014",
      "truth": "plastica",
      "prediction": "plastica"
    },
    {
      "id": "test-plastica-0015",
      "truth": "plastica",
      "prediction": "plastica"
    },
    {
      "id": "test-plastica-0016",
      "truth": "plastica",
      "prediction": "plastica"
    },
    {
      "id": "test-plastica-0017",
      "truth": "plastica",
      "prediction": "plastica"
    },
    {
      "id": "test-plastica-0018",
      "truth": "plastica",
      "prediction": "plastica"
    },
    {
      "id": "test-plastica-0019",
      "truth": "plastica",
      "prediction": "plastica"
    },
    {
      "id": "test-plastica-0020",
      "truth": "plastica",
      "prediction": "plastica"
    },
    {
      "id": "test-plastica-0021",
      "truth": "plastica",
      "prediction": "plastica"
    },
    {
      "id": "test-plastica-0022",
      "truth": "plastica",
      "prediction": "plastica"
    },
    {
      "id": "test-plastica-0023",
      "truth": "plastica",
      "prediction": "plastica"
    },
    {
      "id": "test-plastica-0024",
      "truth": "plastica",
      "prediction": "plastica"
    },
    {
      "id": "test-vetro-0000",
      "truth": "vetro",
      "prediction": "vetro"
    },
    {
      "id": "test-vetro-0001",
      "truth": "vetro",
      "prediction": "vetro"
    },
    {
      "id": "test-vetro-0002",
      "truth": "vetro",
      "prediction": "vetro"
    },
    {
      "id": "test-vetro-0003",
      "truth": "vetro",
      "prediction": "vetro"
    },
    {
      "id": "test-vetro-0004",
      "truth": "vetro",
      "prediction": "vetro"
    },
    {
      "id": "test-vetro-0005",
      "truth": "vetro",
      "prediction": "vetro"
    },
    {
      "id": "test-vetro-0006",
      "truth": "vetro",
      "prediction": "vetro"
    },
    {
      "id": "test-vetro-0007",
      "truth": "vetro",
      "prediction": "vetro"
    },
    {
      "id": "test-vetro-0008",
      "truth": "vetro",
      "prediction": "vetro"
    },
    {
      "id": "test-vetro-0009",
      "truth": "vetro",
      "prediction": "vetro"
    },
    {
      "id": "test-vetro-0010",
      "truth": "vetro",
      "prediction": "vetro"
    },
    {
      "id": "test-vetro-0011",
      "truth": "vetro",
      "prediction": "vetro"
    },
    {
      "id": "test-vetro-0012",
      "truth": "vetro",
      "prediction": "vetro"
    },
    {
      "id": "test-vetro-0013",
      "truth": "vetro",
      "prediction": "vetro"
    },
    {
      "id": "test-vetro-0014",
      "truth": "vetro",
      "prediction": "vetro"
    },
    {
      "id": "test-vetro-0015",
      "truth": "vetro",
      "prediction": "vetro"
    },
    {
      "id": "test-vetro-0016",
      "truth": "vetro",
      "prediction": "vetro"
    },
    {
      "id": "test-vetro-0017",
      "truth": "vetro",
      "prediction": "vetro"
    },
    {
      "id": "test-vetro-0018",
      "truth": "vetro",
      "prediction": "vetro"
    },
    {
      "id": "test-vetro-0019",
      "truth": "vetro",
      "prediction": "vetro"
    },
    {
      "id": "test-vetro-0020",
      "truth": "vetro",
      "prediction": "vetro"
    },
    {
      "id": "test-vetro-0021",
      "truth": "vetro",
      "prediction": "vetro"
    },
    {
      "id": "test-vetro-0022",
      "truth": "vetro",
      "prediction": "vetro"
    },
    {
      "id": "test-vetro-0023",
      "truth": "vetro",
      "prediction": "vetro"
    },
    {
      "id": "test-vetro-0024",
      "truth": "vetro",
      "prediction": "vetro"
    },
    {
      "id": "test-organico-0000",
      "truth": "organico",
      "prediction": "organico"
    },
    {
      "id": "test-organico-0001",
      "truth": "organico",
      "prediction": "organico"
    },
    {
      "id": "test-organico-0002",
      "truth": "organico",
      "prediction": "organico"
    },
    {
      "id": "test-organico-0003",
      "truth": "organico",
      "prediction": "organico"
    },
    {
      "id": "test-organico-0004",
      "truth": "organico",
      "prediction": "organico"
    },
    {
      "id": "test-organico-0005",
      "truth": "organico",
      "prediction": "organico"
    },
    {
      "id": "test-organico-0006",
      "truth": "organico",
      "prediction": "organico"
    },
    {
      "id": "test-organico-0007",
      "truth": "organico",
      "prediction": "organico"
    },
    {
      "id": "test-organico-0008",
      "truth": "organico",
      "prediction": "organico"
    },
    {
      "id": "test-organico-0009",
      "truth": "organico",
      "prediction": "organico"
    },
    {
      "id": "test-organico-0010",
      "truth": "organico",
      "prediction": "organico"
    },
    {
      "id": "test-organico-0011",
      "truth": "organico",
      "prediction": "organico"
    },
    {
      "id": "test-organico-0012",
      "truth": "organico",
      "prediction": "organico"
    },
    {
      "id": "test-organico-0013",
      "truth": "organico",
      "prediction": "organico"
    },
    {
      "id": "test-organico-0014",
      "truth": "organico",
      "prediction": "organico"
    },
    {
      "id": "test-organico-0015",
      "truth": "organico",
      "prediction": "organico"
    },
    {
      "id": "test-organico-0016",
      "truth": "organico",
      "prediction": "organico"
    },
    {
      "id": "test-organico-0017",
      "truth": "organico",
      "prediction": "organico"
    },
    {
      "id": "test-organico-0018",
      "truth": "organico",
      "prediction": "organico"
    },
    {
      "id": "test-organico-0019",
      "truth": "organico",
      "prediction": "organico"
    },
    {
      "id": "test-organico-0020",
      "truth": "organico",
      "prediction": "organico"
    },
    {
      "id": "test-organico-0021",
      "truth": "organico",
      "prediction": "organico"
    },
    {
      "id": "test-organico-0022",
      "truth": "organico",
      "prediction": "organico"
    },
    {
      "id": "test-organico-0023",
      "truth": "organico",
      "prediction": "organico"
    },
    {
      "id": "test-organico-0024",
      "truth": "organico",
      "prediction": "organico"
    }
  ],
  "feature_names": [
    "media_R",
    "media_G",
    "media_B",
    "std_R",
    "std_G",
    "std_B"
  ],
  "sample_features": [
    0.8764705882352931,
    0.8367510893246167,
    0.8240059912854014,
    0.02336087058910005,
    0.022727397289173532,
    0.023505282798509733
  ]
}
```

**stderr** — [file TXT](streams/002_demo_waste_cv.stderr.txt)

Il processo non ha emesso byte su stderr. Il file collegato è vuoto (0 byte).

## Controlli runtime

Il record di questo progetto non contiene controlli classificati come `runtime_check`. L’assenza non aggiunge una verifica runtime alle suite del progetto.

## Verifica e provenienza

[Registro strutturato](registro.json) · [Hash e trasformazioni](MANIFEST.json) · [Policy](../AUDIT.md) · [Indice](../README.md)
