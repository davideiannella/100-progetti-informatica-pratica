# P077 — output reali dei collaudi

Esito registrato: **PASS**. [Run 39849393701](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701) · [job 120071206449](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701/job/120071206449).

Commit del runner: `44cd421247ca2bfe838baa735cf6180134f80464`. Sorgenti applicativi congelati: `32e201b1fb1258c4e7c77d32af323b966647b908`.

Ambiente registrato: Ubuntu 24.04 x86_64; Python 3.12.15 (main, Oct  1 2026, 02:35:59) [GCC 13.3.0]. Artifact: `p041-p080-core-39849393701-1` (ID `12456886835`); record originale: `P077/results.json`.

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

Rapporto registrato: 115 metodi unittest; failures 0, errors 0, skipped 0.

**stdout** — [file TXT](streams/001_unittest_project_suite.stdout.txt)

```text
{
  "project": "P077",
  "tests_run": 115,
  "failures": 0,
  "errors": 0,
  "skipped": 0,
  "seeded_cases": 100,
  "passed": true,
  "seconds": 0.0656933459999891
}
```

**stderr** — [file TXT](streams/001_unittest_project_suite.stderr.txt)

```text
test_bad_training_rows (test_p077.TestTicket.test_bad_training_rows) ... ok
test_deterministic_fit (test_p077.TestTicket.test_deterministic_fit) ... ok
test_duplicates_rejected (test_p077.TestTicket.test_duplicates_rejected) ... ok
test_holdout_token_never_fitted (test_p077.TestTicket.test_holdout_token_never_fitted) ... ok
test_input_validation (test_p077.TestTicket.test_input_validation) ... ok
test_known_example (test_p077.TestTicket.test_known_example) ... ok
test_metric_counts_from_predictions (test_p077.TestTicket.test_metric_counts_from_predictions) ... ok
test_missing_class_rejected (test_p077.TestTicket.test_missing_class_rejected) ... ok
test_overlap_rejected_even_different_id (test_p077.TestTicket.test_overlap_rejected_even_different_id) ... ok
test_probability_finite_and_normalized (test_p077.TestTicket.test_probability_finite_and_normalized) ... ok
test_punctuation_cannot_disguise_train_test_duplicate (test_p077.TestTicket.test_punctuation_cannot_disguise_train_test_duplicate) ... ok
test_seed_000 (test_p077.TestTicket.test_seed_000) ... ok
test_seed_001 (test_p077.TestTicket.test_seed_001) ... ok
test_seed_002 (test_p077.TestTicket.test_seed_002) ... ok
test_seed_003 (test_p077.TestTicket.test_seed_003) ... ok
test_seed_004 (test_p077.TestTicket.test_seed_004) ... ok
test_seed_005 (test_p077.TestTicket.test_seed_005) ... ok
test_seed_006 (test_p077.TestTicket.test_seed_006) ... ok
test_seed_007 (test_p077.TestTicket.test_seed_007) ... ok
test_seed_008 (test_p077.TestTicket.test_seed_008) ... ok
test_seed_009 (test_p077.TestTicket.test_seed_009) ... ok
test_seed_010 (test_p077.TestTicket.test_seed_010) ... ok
test_seed_011 (test_p077.TestTicket.test_seed_011) ... ok
test_seed_012 (test_p077.TestTicket.test_seed_012) ... ok
test_seed_013 (test_p077.TestTicket.test_seed_013) ... ok
test_seed_014 (test_p077.TestTicket.test_seed_014) ... ok
test_seed_015 (test_p077.TestTicket.test_seed_015) ... ok
test_seed_016 (test_p077.TestTicket.test_seed_016) ... ok
test_seed_017 (test_p077.TestTicket.test_seed_017) ... ok
test_seed_018 (test_p077.TestTicket.test_seed_018) ... ok
test_seed_019 (test_p077.TestTicket.test_seed_019) ... ok
test_seed_020 (test_p077.TestTicket.test_seed_020) ... ok
test_seed_021 (test_p077.TestTicket.test_seed_021) ... ok
test_seed_022 (test_p077.TestTicket.test_seed_022) ... ok
test_seed_023 (test_p077.TestTicket.test_seed_023) ... ok
test_seed_024 (test_p077.TestTicket.test_seed_024) ... ok
test_seed_025 (test_p077.TestTicket.test_seed_025) ... ok
test_seed_026 (test_p077.TestTicket.test_seed_026) ... ok
test_seed_027 (test_p077.TestTicket.test_seed_027) ... ok
test_seed_028 (test_p077.TestTicket.test_seed_028) ... ok
test_seed_029 (test_p077.TestTicket.test_seed_029) ... ok
test_seed_030 (test_p077.TestTicket.test_seed_030) ... ok
test_seed_031 (test_p077.TestTicket.test_seed_031) ... ok
test_seed_032 (test_p077.TestTicket.test_seed_032) ... ok
test_seed_033 (test_p077.TestTicket.test_seed_033) ... ok
test_seed_034 (test_p077.TestTicket.test_seed_034) ... ok
test_seed_035 (test_p077.TestTicket.test_seed_035) ... ok
test_seed_036 (test_p077.TestTicket.test_seed_036) ... ok
test_seed_037 (test_p077.TestTicket.test_seed_037) ... ok
test_seed_038 (test_p077.TestTicket.test_seed_038) ... ok
test_seed_039 (test_p077.TestTicket.test_seed_039) ... ok
test_seed_040 (test_p077.TestTicket.test_seed_040) ... ok
test_seed_041 (test_p077.TestTicket.test_seed_041) ... ok
test_seed_042 (test_p077.TestTicket.test_seed_042) ... ok
test_seed_043 (test_p077.TestTicket.test_seed_043) ... ok
test_seed_044 (test_p077.TestTicket.test_seed_044) ... ok
test_seed_045 (test_p077.TestTicket.test_seed_045) ... ok
test_seed_046 (test_p077.TestTicket.test_seed_046) ... ok
test_seed_047 (test_p077.TestTicket.test_seed_047) ... ok
test_seed_048 (test_p077.TestTicket.test_seed_048) ... ok
test_seed_049 (test_p077.TestTicket.test_seed_049) ... ok
test_seed_050 (test_p077.TestTicket.test_seed_050) ... ok
test_seed_051 (test_p077.TestTicket.test_seed_051) ... ok
test_seed_052 (test_p077.TestTicket.test_seed_052) ... ok
test_seed_053 (test_p077.TestTicket.test_seed_053) ... ok
test_seed_054 (test_p077.TestTicket.test_seed_054) ... ok
test_seed_055 (test_p077.TestTicket.test_seed_055) ... ok
test_seed_056 (test_p077.TestTicket.test_seed_056) ... ok
test_seed_057 (test_p077.TestTicket.test_seed_057) ... ok
test_seed_058 (test_p077.TestTicket.test_seed_058) ... ok
test_seed_059 (test_p077.TestTicket.test_seed_059) ... ok
test_seed_060 (test_p077.TestTicket.test_seed_060) ... ok
test_seed_061 (test_p077.TestTicket.test_seed_061) ... ok
test_seed_062 (test_p077.TestTicket.test_seed_062) ... ok
test_seed_063 (test_p077.TestTicket.test_seed_063) ... ok
test_seed_064 (test_p077.TestTicket.test_seed_064) ... ok
test_seed_065 (test_p077.TestTicket.test_seed_065) ... ok
test_seed_066 (test_p077.TestTicket.test_seed_066) ... ok
test_seed_067 (test_p077.TestTicket.test_seed_067) ... ok
test_seed_068 (test_p077.TestTicket.test_seed_068) ... ok
test_seed_069 (test_p077.TestTicket.test_seed_069) ... ok
test_seed_070 (test_p077.TestTicket.test_seed_070) ... ok
test_seed_071 (test_p077.TestTicket.test_seed_071) ... ok
test_seed_072 (test_p077.TestTicket.test_seed_072) ... ok
test_seed_073 (test_p077.TestTicket.test_seed_073) ... ok
test_seed_074 (test_p077.TestTicket.test_seed_074) ... ok
test_seed_075 (test_p077.TestTicket.test_seed_075) ... ok
test_seed_076 (test_p077.TestTicket.test_seed_076) ... ok
test_seed_077 (test_p077.TestTicket.test_seed_077) ... ok
test_seed_078 (test_p077.TestTicket.test_seed_078) ... ok
test_seed_079 (test_p077.TestTicket.test_seed_079) ... ok
test_seed_080 (test_p077.TestTicket.test_seed_080) ... ok
test_seed_081 (test_p077.TestTicket.test_seed_081) ... ok
test_seed_082 (test_p077.TestTicket.test_seed_082) ... ok
test_seed_083 (test_p077.TestTicket.test_seed_083) ... ok
test_seed_084 (test_p077.TestTicket.test_seed_084) ... ok
test_seed_085 (test_p077.TestTicket.test_seed_085) ... ok
test_seed_086 (test_p077.TestTicket.test_seed_086) ... ok
test_seed_087 (test_p077.TestTicket.test_seed_087) ... ok
test_seed_088 (test_p077.TestTicket.test_seed_088) ... ok
test_seed_089 (test_p077.TestTicket.test_seed_089) ... ok
test_seed_090 (test_p077.TestTicket.test_seed_090) ... ok
test_seed_091 (test_p077.TestTicket.test_seed_091) ... ok
test_seed_092 (test_p077.TestTicket.test_seed_092) ... ok
test_seed_093 (test_p077.TestTicket.test_seed_093) ... ok
test_seed_094 (test_p077.TestTicket.test_seed_094) ... ok
test_seed_095 (test_p077.TestTicket.test_seed_095) ... ok
test_seed_096 (test_p077.TestTicket.test_seed_096) ... ok
test_seed_097 (test_p077.TestTicket.test_seed_097) ... ok
test_seed_098 (test_p077.TestTicket.test_seed_098) ... ok
test_seed_099 (test_p077.TestTicket.test_seed_099) ... ok
test_split_no_shared_ids_or_texts (test_p077.TestTicket.test_split_no_shared_ids_or_texts) ... ok
test_training_order_does_not_change_labels (test_p077.TestTicket.test_training_order_does_not_change_labels) ... ok
test_unicode_normalization (test_p077.TestTicket.test_unicode_normalization) ... ok
test_unseen_terms_abstain (test_p077.TestTicket.test_unseen_terms_abstain) ... ok

----------------------------------------------------------------------
Ran 115 tests in 0.066s

OK
```

## Demo — processi separati dalle suite

Questi output provengono dalle demo eseguite dal runner. Non costituiscono nuovi metodi unittest.

### 002 · demo_ticket_nlp

Comando registrato (array degli argomenti; segnaposto dei metadati documentati nel manifest):

```json
["<PYTHON_HOME>/bin/python", "-B", "src/ticket_nlp.py"]
```

Esito: **PASS** · codice di uscita: `0`.

**stdout** — [file TXT](streams/002_demo_ticket_nlp.stdout.txt)

```text
{
  "dataset": "36 ticket inventati manualmente; nessun dato cliente",
  "split": {
    "train": 24,
    "test": 12,
    "text_overlap": 0,
    "train_ids": [
      "a01",
      "a02",
      "a03",
      "a04",
      "a05",
      "a06",
      "a07",
      "a08",
      "f01",
      "f02",
      "f03",
      "f04",
      "f05",
      "f06",
      "f07",
      "f08",
      "t01",
      "t02",
      "t03",
      "t04",
      "t05",
      "t06",
      "t07",
      "t08"
    ],
    "test_ids": [
      "ha01",
      "ha02",
      "ha03",
      "ha04",
      "hf01",
      "hf02",
      "hf03",
      "hf04",
      "ht01",
      "ht02",
      "ht03",
      "ht04"
    ]
  },
  "classes": [
    "accesso",
    "fatturazione",
    "tecnico"
  ],
  "accuracy": 1.0,
  "f1_macro": 1.0,
  "baseline_accuracy": 0.3333333333333333,
  "confusion_matrix": [
    [
      4,
      0,
      0
    ],
    [
      0,
      4,
      0
    ],
    [
      0,
      0,
      4
    ]
  ],
  "predictions": [
    {
      "id": "ha01",
      "text": "ho dimenticato la password del mio account",
      "truth": "accesso",
      "prediction": "accesso"
    },
    {
      "id": "ha02",
      "text": "non arriva il codice per autenticazione",
      "truth": "accesso",
      "prediction": "accesso"
    },
    {
      "id": "ha03",
      "text": "le credenziali impediscono il login",
      "truth": "accesso",
      "prediction": "accesso"
    },
    {
      "id": "ha04",
      "text": "devo entrare ma account sospeso",
      "truth": "accesso",
      "prediction": "accesso"
    },
    {
      "id": "hf01",
      "text": "il pagamento ha un importo diverso dalla fattura",
      "truth": "fatturazione",
      "prediction": "fatturazione"
    },
    {
      "id": "hf02",
      "text": "vorrei rimborso per addebito doppio",
      "truth": "fatturazione",
      "prediction": "fatturazione"
    },
    {
      "id": "hf03",
      "text": "dove recupero la ricevuta del pagamento",
      "truth": "fatturazione",
      "prediction": "fatturazione"
    },
    {
      "id": "hf04",
      "text": "correggere indirizzo sulla fattura",
      "truth": "fatturazione",
      "prediction": "fatturazione"
    },
    {
      "id": "ht01",
      "text": "il server risponde lentamente durante salvataggio",
      "truth": "tecnico",
      "prediction": "tecnico"
    },
    {
      "id": "ht02",
      "text": "dopo aggiornamento vedo schermata bianca",
      "truth": "tecnico",
      "prediction": "tecnico"
    },
    {
      "id": "ht03",
      "text": "la connessione cade e la pagina non carica",
      "truth": "tecnico",
      "prediction": "tecnico"
    },
    {
      "id": "ht04",
      "text": "crash durante esportazione del documento",
      "truth": "tecnico",
      "prediction": "tecnico"
    }
  ],
  "example": {
    "input": "ho dimenticato la password",
    "label": "accesso",
    "reason": "classificato"
  },
  "oov_example": {
    "label": null,
    "reason": "nessun_termine_noto"
  }
}
```

**stderr** — [file TXT](streams/002_demo_ticket_nlp.stderr.txt)

Il processo non ha emesso byte su stderr. Il file collegato è vuoto (0 byte).

## Controlli runtime

Il record di questo progetto non contiene controlli classificati come `runtime_check`. L’assenza non aggiunge una verifica runtime alle suite del progetto.

## Verifica e provenienza

[Registro strutturato](registro.json) · [Hash e trasformazioni](MANIFEST.json) · [Policy](../AUDIT.md) · [Indice](../README.md)
