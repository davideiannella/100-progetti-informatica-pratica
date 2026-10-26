# P080: output dei collaudi

[Indice dei collaudi](../README.md) · [Codice e istruzioni](../../projects/P080/README.md)

Esito registrato: **PASS**. [Run 39849393701](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701) · [job 120071206449](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701/job/120071206449).

Commit del runner: `44cd421247ca2bfe838baa735cf6180134f80464`. Sorgenti applicativi congelati: `32e201b1fb1258c4e7c77d32af323b966647b908`.

Ambiente registrato: Ubuntu 24.04 x86_64; Python 3.12.15 (main, Oct  1 2026, 02:35:59) [GCC 13.3.0]. Artifact: `p041-p080-core-39849393701-1` (ID `12456886835`); record originale: `P080/results.json`.

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

Rapporto registrato: 114 metodi unittest; failures 0, errors 0, skipped 0.

**stdout** — [file TXT](streams/001_unittest_project_suite.stdout.txt)

```text
{
  "project": "P080",
  "tests_run": 114,
  "failures": 0,
  "errors": 0,
  "skipped": 0,
  "seeded_cases": 100,
  "passed": true,
  "seconds": 0.055290297999988525
}
```

**stderr** — [file TXT](streams/001_unittest_project_suite.stderr.txt)

```text
test_below_threshold_abstains (test_p080.TestRetrieval.test_below_threshold_abstains) ... ok
test_corpus_copied_not_aliased (test_p080.TestRetrieval.test_corpus_copied_not_aliased) ... ok
test_corpus_validation (test_p080.TestRetrieval.test_corpus_validation) ... ok
test_evaluation_queries_are_not_document_copies (test_p080.TestRetrieval.test_evaluation_queries_are_not_document_copies) ... ok
test_instructions_in_query_do_not_execute (test_p080.TestRetrieval.test_instructions_in_query_do_not_execute) ... ok
test_k_validation (test_p080.TestRetrieval.test_k_validation) ... ok
test_query_never_changes_index (test_p080.TestRetrieval.test_query_never_changes_index) ... ok
test_query_types_and_limit (test_p080.TestRetrieval.test_query_types_and_limit) ... ok
test_rank_order_and_positive_scores (test_p080.TestRetrieval.test_rank_order_and_positive_scores) ... ok
test_seed_000 (test_p080.TestRetrieval.test_seed_000) ... ok
test_seed_001 (test_p080.TestRetrieval.test_seed_001) ... ok
test_seed_002 (test_p080.TestRetrieval.test_seed_002) ... ok
test_seed_003 (test_p080.TestRetrieval.test_seed_003) ... ok
test_seed_004 (test_p080.TestRetrieval.test_seed_004) ... ok
test_seed_005 (test_p080.TestRetrieval.test_seed_005) ... ok
test_seed_006 (test_p080.TestRetrieval.test_seed_006) ... ok
test_seed_007 (test_p080.TestRetrieval.test_seed_007) ... ok
test_seed_008 (test_p080.TestRetrieval.test_seed_008) ... ok
test_seed_009 (test_p080.TestRetrieval.test_seed_009) ... ok
test_seed_010 (test_p080.TestRetrieval.test_seed_010) ... ok
test_seed_011 (test_p080.TestRetrieval.test_seed_011) ... ok
test_seed_012 (test_p080.TestRetrieval.test_seed_012) ... ok
test_seed_013 (test_p080.TestRetrieval.test_seed_013) ... ok
test_seed_014 (test_p080.TestRetrieval.test_seed_014) ... ok
test_seed_015 (test_p080.TestRetrieval.test_seed_015) ... ok
test_seed_016 (test_p080.TestRetrieval.test_seed_016) ... ok
test_seed_017 (test_p080.TestRetrieval.test_seed_017) ... ok
test_seed_018 (test_p080.TestRetrieval.test_seed_018) ... ok
test_seed_019 (test_p080.TestRetrieval.test_seed_019) ... ok
test_seed_020 (test_p080.TestRetrieval.test_seed_020) ... ok
test_seed_021 (test_p080.TestRetrieval.test_seed_021) ... ok
test_seed_022 (test_p080.TestRetrieval.test_seed_022) ... ok
test_seed_023 (test_p080.TestRetrieval.test_seed_023) ... ok
test_seed_024 (test_p080.TestRetrieval.test_seed_024) ... ok
test_seed_025 (test_p080.TestRetrieval.test_seed_025) ... ok
test_seed_026 (test_p080.TestRetrieval.test_seed_026) ... ok
test_seed_027 (test_p080.TestRetrieval.test_seed_027) ... ok
test_seed_028 (test_p080.TestRetrieval.test_seed_028) ... ok
test_seed_029 (test_p080.TestRetrieval.test_seed_029) ... ok
test_seed_030 (test_p080.TestRetrieval.test_seed_030) ... ok
test_seed_031 (test_p080.TestRetrieval.test_seed_031) ... ok
test_seed_032 (test_p080.TestRetrieval.test_seed_032) ... ok
test_seed_033 (test_p080.TestRetrieval.test_seed_033) ... ok
test_seed_034 (test_p080.TestRetrieval.test_seed_034) ... ok
test_seed_035 (test_p080.TestRetrieval.test_seed_035) ... ok
test_seed_036 (test_p080.TestRetrieval.test_seed_036) ... ok
test_seed_037 (test_p080.TestRetrieval.test_seed_037) ... ok
test_seed_038 (test_p080.TestRetrieval.test_seed_038) ... ok
test_seed_039 (test_p080.TestRetrieval.test_seed_039) ... ok
test_seed_040 (test_p080.TestRetrieval.test_seed_040) ... ok
test_seed_041 (test_p080.TestRetrieval.test_seed_041) ... ok
test_seed_042 (test_p080.TestRetrieval.test_seed_042) ... ok
test_seed_043 (test_p080.TestRetrieval.test_seed_043) ... ok
test_seed_044 (test_p080.TestRetrieval.test_seed_044) ... ok
test_seed_045 (test_p080.TestRetrieval.test_seed_045) ... ok
test_seed_046 (test_p080.TestRetrieval.test_seed_046) ... ok
test_seed_047 (test_p080.TestRetrieval.test_seed_047) ... ok
test_seed_048 (test_p080.TestRetrieval.test_seed_048) ... ok
test_seed_049 (test_p080.TestRetrieval.test_seed_049) ... ok
test_seed_050 (test_p080.TestRetrieval.test_seed_050) ... ok
test_seed_051 (test_p080.TestRetrieval.test_seed_051) ... ok
test_seed_052 (test_p080.TestRetrieval.test_seed_052) ... ok
test_seed_053 (test_p080.TestRetrieval.test_seed_053) ... ok
test_seed_054 (test_p080.TestRetrieval.test_seed_054) ... ok
test_seed_055 (test_p080.TestRetrieval.test_seed_055) ... ok
test_seed_056 (test_p080.TestRetrieval.test_seed_056) ... ok
test_seed_057 (test_p080.TestRetrieval.test_seed_057) ... ok
test_seed_058 (test_p080.TestRetrieval.test_seed_058) ... ok
test_seed_059 (test_p080.TestRetrieval.test_seed_059) ... ok
test_seed_060 (test_p080.TestRetrieval.test_seed_060) ... ok
test_seed_061 (test_p080.TestRetrieval.test_seed_061) ... ok
test_seed_062 (test_p080.TestRetrieval.test_seed_062) ... ok
test_seed_063 (test_p080.TestRetrieval.test_seed_063) ... ok
test_seed_064 (test_p080.TestRetrieval.test_seed_064) ... ok
test_seed_065 (test_p080.TestRetrieval.test_seed_065) ... ok
test_seed_066 (test_p080.TestRetrieval.test_seed_066) ... ok
test_seed_067 (test_p080.TestRetrieval.test_seed_067) ... ok
test_seed_068 (test_p080.TestRetrieval.test_seed_068) ... ok
test_seed_069 (test_p080.TestRetrieval.test_seed_069) ... ok
test_seed_070 (test_p080.TestRetrieval.test_seed_070) ... ok
test_seed_071 (test_p080.TestRetrieval.test_seed_071) ... ok
test_seed_072 (test_p080.TestRetrieval.test_seed_072) ... ok
test_seed_073 (test_p080.TestRetrieval.test_seed_073) ... ok
test_seed_074 (test_p080.TestRetrieval.test_seed_074) ... ok
test_seed_075 (test_p080.TestRetrieval.test_seed_075) ... ok
test_seed_076 (test_p080.TestRetrieval.test_seed_076) ... ok
test_seed_077 (test_p080.TestRetrieval.test_seed_077) ... ok
test_seed_078 (test_p080.TestRetrieval.test_seed_078) ... ok
test_seed_079 (test_p080.TestRetrieval.test_seed_079) ... ok
test_seed_080 (test_p080.TestRetrieval.test_seed_080) ... ok
test_seed_081 (test_p080.TestRetrieval.test_seed_081) ... ok
test_seed_082 (test_p080.TestRetrieval.test_seed_082) ... ok
test_seed_083 (test_p080.TestRetrieval.test_seed_083) ... ok
test_seed_084 (test_p080.TestRetrieval.test_seed_084) ... ok
test_seed_085 (test_p080.TestRetrieval.test_seed_085) ... ok
test_seed_086 (test_p080.TestRetrieval.test_seed_086) ... ok
test_seed_087 (test_p080.TestRetrieval.test_seed_087) ... ok
test_seed_088 (test_p080.TestRetrieval.test_seed_088) ... ok
test_seed_089 (test_p080.TestRetrieval.test_seed_089) ... ok
test_seed_090 (test_p080.TestRetrieval.test_seed_090) ... ok
test_seed_091 (test_p080.TestRetrieval.test_seed_091) ... ok
test_seed_092 (test_p080.TestRetrieval.test_seed_092) ... ok
test_seed_093 (test_p080.TestRetrieval.test_seed_093) ... ok
test_seed_094 (test_p080.TestRetrieval.test_seed_094) ... ok
test_seed_095 (test_p080.TestRetrieval.test_seed_095) ... ok
test_seed_096 (test_p080.TestRetrieval.test_seed_096) ... ok
test_seed_097 (test_p080.TestRetrieval.test_seed_097) ... ok
test_seed_098 (test_p080.TestRetrieval.test_seed_098) ... ok
test_seed_099 (test_p080.TestRetrieval.test_seed_099) ... ok
test_supported_queries_and_exact_citations (test_p080.TestRetrieval.test_supported_queries_and_exact_citations) ... ok
test_threshold_validation (test_p080.TestRetrieval.test_threshold_validation) ... ok
test_tie_is_stable_and_abstains (test_p080.TestRetrieval.test_tie_is_stable_and_abstains) ... ok
test_unknown_empty_stopword_query_abstains (test_p080.TestRetrieval.test_unknown_empty_stopword_query_abstains) ... ok
test_untrusted_document_can_be_quoted_no_security_claim (test_p080.TestRetrieval.test_untrusted_document_can_be_quoted_no_security_claim) ... ok

----------------------------------------------------------------------
Ran 114 tests in 0.055s

OK
```

## Demo — processi separati dalle suite

Questi output provengono dalle demo eseguite dal runner. Non costituiscono nuovi metodi unittest.

### 002 · demo_rag

Comando registrato (array degli argomenti; segnaposto dei metadati documentati nel manifest):

```json
["<PYTHON_HOME>/bin/python", "-B", "src/rag.py"]
```

Esito: **PASS** · codice di uscita: `0`.

**stdout** — [file TXT](streams/002_demo_rag.stdout.txt)

```text
{
  "dataset": "Quattro documenti tecnici originali; dodici query manuali distinte dai testi",
  "mode": "retrieval_estrattivo_senza_LLM",
  "documents": 4,
  "thresholds": {
    "min_score": 0.15,
    "min_margin": 0.05,
    "selection": "costanti didattiche fissate prima della valutazione; non calibrate"
  },
  "queries": [
    {
      "query": "a cosa serve DNS?",
      "expected_citation": "reti",
      "answer": "DNS traduce nomi di dominio in indirizzi IP.",
      "citation": "reti",
      "score": 0.4082482904638631,
      "abstained": false,
      "reason": "estratto_letterale",
      "ranking": [
        {
          "source": "reti",
          "score": 0.4082482904638631
        }
      ],
      "correct": true
    },
    {
      "query": "nomi di dominio e indirizzi IP",
      "expected_citation": "reti",
      "answer": "DNS traduce nomi di dominio in indirizzi IP.",
      "citation": "reti",
      "score": 0.8164965809277261,
      "abstained": false,
      "reason": "estratto_letterale",
      "ranking": [
        {
          "source": "reti",
          "score": 0.8164965809277261
        }
      ],
      "correct": true
    },
    {
      "query": "che cosa collega una chiave esterna?",
      "expected_citation": "db",
      "answer": "Una chiave esterna collega una riga a una chiave di un’altra relazione.",
      "citation": "db",
      "score": 0.7698003589195009,
      "abstained": false,
      "reason": "estratto_letterale",
      "ranking": [
        {
          "source": "db",
          "score": 0.7698003589195009
        }
      ],
      "correct": true
    },
    {
      "query": "collegare una riga a una relazione",
      "expected_citation": "db",
      "answer": "Una chiave esterna collega una riga a una chiave di un’altra relazione.",
      "citation": "db",
      "score": 0.4714045207910317,
      "abstained": false,
      "reason": "estratto_letterale",
      "ranking": [
        {
          "source": "db",
          "score": 0.4714045207910317
        }
      ],
      "correct": true
    },
    {
      "query": "come evitare SQL injection con query e parametri?",
      "expected_citation": "security",
      "answer": "Le query parametrizzate separano il codice SQL dai dati dell’utente.",
      "citation": "security",
      "score": 0.5000000000000001,
      "abstained": false,
      "reason": "estratto_letterale",
      "ranking": [
        {
          "source": "security",
          "score": 0.5000000000000001
        }
      ],
      "correct": true
    },
    {
      "query": "query parametrizzate e dati utente",
      "expected_citation": "security",
      "answer": "Le query parametrizzate separano il codice SQL dai dati dell’utente.",
      "citation": "security",
      "score": 0.7071067811865476,
      "abstained": false,
      "reason": "estratto_letterale",
      "ranking": [
        {
          "source": "security",
          "score": 0.7071067811865476
        }
      ],
      "correct": true
    },
    {
      "query": "health check istanza disponibile",
      "expected_citation": "cloud",
      "answer": "Un health check consente di valutare se un’istanza è disponibile per ricevere traffico.",
      "citation": "cloud",
      "score": 0.7071067811865476,
      "abstained": false,
      "reason": "estratto_letterale",
      "ranking": [
        {
          "source": "cloud",
          "score": 0.7071067811865476
        }
      ],
      "correct": true
    },
    {
      "query": "ricevere traffico e valutare istanza",
      "expected_citation": "cloud",
      "answer": "Un health check consente di valutare se un’istanza è disponibile per ricevere traffico.",
      "citation": "cloud",
      "score": 0.7071067811865476,
      "abstained": false,
      "reason": "estratto_letterale",
      "ranking": [
        {
          "source": "cloud",
          "score": 0.7071067811865476
        }
      ],
      "correct": true
    },
    {
      "query": "unicorno galattico",
      "expected_citation": null,
      "answer": "Non ho una fonte sufficientemente pertinente e univoca nel corpus.",
      "citation": null,
      "score": 0.0,
      "abstained": true,
      "reason": "nessun_termine_noto",
      "ranking": [],
      "correct": true
    },
    {
      "query": "ricetta risotto funghi",
      "expected_citation": null,
      "answer": "Non ho una fonte sufficientemente pertinente e univoca nel corpus.",
      "citation": null,
      "score": 0.0,
      "abstained": true,
      "reason": "nessun_termine_noto",
      "ranking": [],
      "correct": true
    },
    {
      "query": "",
      "expected_citation": null,
      "answer": "Non ho una fonte sufficientemente pertinente e univoca nel corpus.",
      "citation": null,
      "score": 0.0,
      "abstained": true,
      "reason": "nessun_termine_noto",
      "ranking": [],
      "correct": true
    },
    {
      "query": "e la di un per",
      "expected_citation": null,
      "answer": "Non ho una fonte sufficientemente pertinente e univoca nel corpus.",
      "citation": null,
      "score": 0.0,
      "abstained": true,
      "reason": "nessun_termine_noto",
      "ranking": [],
      "correct": true
    }
  ],
  "correct": 12,
  "total": 12,
  "abstentions": 4,
  "ambiguous_example": {
    "answer": "Non ho una fonte sufficientemente pertinente e univoca nel corpus.",
    "citation": null,
    "score": 0.7071067811865476,
    "abstained": true,
    "reason": "fonti_ambigue",
    "ranking": [
      {
        "source": "a",
        "score": 0.7071067811865476
      },
      {
        "source": "b",
        "score": 0.7071067811865476
      }
    ]
  }
}
```

**stderr** — [file TXT](streams/002_demo_rag.stderr.txt)

Il processo non ha emesso byte su stderr. Il file collegato è vuoto (0 byte).

## Controlli runtime

Il record di questo progetto non contiene controlli classificati come `runtime_check`. L’assenza non aggiunge una verifica runtime alle suite del progetto.

## Verifica e provenienza

[Registro strutturato](registro.json) · [Hash e trasformazioni](MANIFEST.json) · [Policy](../AUDIT.md) · [Indice](../README.md)
