# P076 — output reali dei collaudi

Esito registrato: **PASS**. [Run 39849393701](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701) · [job 120071206449](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701/job/120071206449).

Commit del runner: `44cd421247ca2bfe838baa735cf6180134f80464`. Sorgenti applicativi congelati: `32e201b1fb1258c4e7c77d32af323b966647b908`.

Ambiente registrato: Ubuntu 24.04 x86_64; Python 3.12.15 (main, Oct  1 2026, 02:35:59) [GCC 13.3.0]. Artifact: `p041-p080-core-39849393701-1` (ID `12456886835`); record originale: `P076/results.json`.

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

Rapporto registrato: 112 metodi unittest; failures 0, errors 0, skipped 0; sottocasi dichiarati 0.

**stdout** — [file TXT](streams/001_unittest_project_suite.stdout.txt)

```text
SEED_RESULT {"candidates": 6, "k": 8, "returned": 6, "seed": 0, "top_score": 0.9026260869720649}
SEED_RESULT {"candidates": 6, "k": 4, "returned": 4, "seed": 1, "top_score": 0.9373948219289396}
SEED_RESULT {"candidates": 6, "k": 5, "returned": 5, "seed": 2, "top_score": 0.8831776953091264}
SEED_RESULT {"candidates": 6, "k": 6, "returned": 6, "seed": 3, "top_score": 0.8565762008647633}
SEED_RESULT {"candidates": 6, "k": 8, "returned": 6, "seed": 4, "top_score": 0.9882488537703276}
SEED_RESULT {"candidates": 6, "k": 0, "returned": 0, "seed": 5, "top_score": null}
SEED_RESULT {"candidates": 6, "k": 4, "returned": 4, "seed": 6, "top_score": 0.9735050563110296}
SEED_RESULT {"candidates": 6, "k": 9, "returned": 6, "seed": 7, "top_score": 0.9685799420449641}
SEED_RESULT {"candidates": 6, "k": 1, "returned": 1, "seed": 8, "top_score": 0.9699693098717388}
SEED_RESULT {"candidates": 6, "k": 5, "returned": 5, "seed": 9, "top_score": 0.9700050642818845}
SEED_RESULT {"candidates": 6, "k": 7, "returned": 6, "seed": 10, "top_score": 0.777888192486685}
SEED_RESULT {"candidates": 6, "k": 0, "returned": 0, "seed": 11, "top_score": null}
SEED_RESULT {"candidates": 6, "k": 0, "returned": 0, "seed": 12, "top_score": null}
SEED_RESULT {"candidates": 6, "k": 5, "returned": 5, "seed": 13, "top_score": 0.8829924282785776}
SEED_RESULT {"candidates": 6, "k": 8, "returned": 6, "seed": 14, "top_score": 0.9773368839432057}
SEED_RESULT {"candidates": 6, "k": 7, "returned": 6, "seed": 15, "top_score": 0.9063242551202237}
SEED_RESULT {"candidates": 6, "k": 5, "returned": 5, "seed": 16, "top_score": 0.971449138479239}
SEED_RESULT {"candidates": 6, "k": 7, "returned": 6, "seed": 17, "top_score": 0.9207397989326744}
SEED_RESULT {"candidates": 6, "k": 5, "returned": 5, "seed": 18, "top_score": 0.8611942045384304}
SEED_RESULT {"candidates": 6, "k": 5, "returned": 5, "seed": 19, "top_score": 0.9286508565435034}
SEED_RESULT {"candidates": 6, "k": 2, "returned": 2, "seed": 20, "top_score": 0.8381817235962779}
SEED_RESULT {"candidates": 6, "k": 2, "returned": 2, "seed": 21, "top_score": 0.9551367361757522}
SEED_RESULT {"candidates": 6, "k": 6, "returned": 6, "seed": 22, "top_score": 0.9907641475417281}
SEED_RESULT {"candidates": 6, "k": 0, "returned": 0, "seed": 23, "top_score": null}
SEED_RESULT {"candidates": 6, "k": 5, "returned": 5, "seed": 24, "top_score": 0.9889834603091723}
SEED_RESULT {"candidates": 6, "k": 3, "returned": 3, "seed": 25, "top_score": 0.9378500985081415}
SEED_RESULT {"candidates": 6, "k": 9, "returned": 6, "seed": 26, "top_score": 0.9040816952139784}
SEED_RESULT {"candidates": 6, "k": 6, "returned": 6, "seed": 27, "top_score": 0.9274403054015157}
SEED_RESULT {"candidates": 6, "k": 8, "returned": 6, "seed": 28, "top_score": 0.9054455782953186}
SEED_RESULT {"candidates": 6, "k": 9, "returned": 6, "seed": 29, "top_score": 0.8721933769409513}
SEED_RESULT {"candidates": 6, "k": 2, "returned": 2, "seed": 30, "top_score": 0.9816543377037812}
SEED_RESULT {"candidates": 6, "k": 1, "returned": 1, "seed": 31, "top_score": 0.9389602009248829}
SEED_RESULT {"candidates": 6, "k": 1, "returned": 1, "seed": 32, "top_score": 0.9626322353091622}
SEED_RESULT {"candidates": 6, "k": 6, "returned": 6, "seed": 33, "top_score": 0.9380358934033446}
SEED_RESULT {"candidates": 6, "k": 1, "returned": 1, "seed": 34, "top_score": 0.9231663486565124}
SEED_RESULT {"candidates": 6, "k": 5, "returned": 5, "seed": 35, "top_score": 0.9417812269009875}
SEED_RESULT {"candidates": 6, "k": 9, "returned": 6, "seed": 36, "top_score": 0.8739764604574597}
SEED_RESULT {"candidates": 6, "k": 8, "returned": 6, "seed": 37, "top_score": 0.933920121132214}
SEED_RESULT {"candidates": 6, "k": 8, "returned": 6, "seed": 38, "top_score": 0.9387263701241327}
SEED_RESULT {"candidates": 6, "k": 2, "returned": 2, "seed": 39, "top_score": 0.9805971229438993}
SEED_RESULT {"candidates": 6, "k": 8, "returned": 6, "seed": 40, "top_score": 0.9231316657430816}
SEED_RESULT {"candidates": 6, "k": 6, "returned": 6, "seed": 41, "top_score": 0.9134754972347906}
SEED_RESULT {"candidates": 6, "k": 4, "returned": 4, "seed": 42, "top_score": 0.9914519680790675}
SEED_RESULT {"candidates": 6, "k": 6, "returned": 6, "seed": 43, "top_score": 0.9640624147047331}
SEED_RESULT {"candidates": 6, "k": 3, "returned": 3, "seed": 44, "top_score": 0.7205589565489786}
SEED_RESULT {"candidates": 6, "k": 1, "returned": 1, "seed": 45, "top_score": 0.9819530273793932}
SEED_RESULT {"candidates": 6, "k": 8, "returned": 6, "seed": 46, "top_score": 0.9690604322160116}
SEED_RESULT {"candidates": 6, "k": 2, "returned": 2, "seed": 47, "top_score": 0.9837357843739046}
SEED_RESULT {"candidates": 6, "k": 7, "returned": 6, "seed": 48, "top_score": 0.9580608175736837}
SEED_RESULT {"candidates": 6, "k": 4, "returned": 4, "seed": 49, "top_score": 0.9281849593607419}
SEED_RESULT {"candidates": 6, "k": 4, "returned": 4, "seed": 50, "top_score": 0.9167114998641126}
SEED_RESULT {"candidates": 6, "k": 2, "returned": 2, "seed": 51, "top_score": 0.9242723105560369}
SEED_RESULT {"candidates": 6, "k": 8, "returned": 6, "seed": 52, "top_score": 0.9454584904302211}
SEED_RESULT {"candidates": 6, "k": 6, "returned": 6, "seed": 53, "top_score": 0.9012277922729415}
SEED_RESULT {"candidates": 6, "k": 2, "returned": 2, "seed": 54, "top_score": 0.9225335560883308}
SEED_RESULT {"candidates": 6, "k": 7, "returned": 6, "seed": 55, "top_score": 0.981747660187322}
SEED_RESULT {"candidates": 6, "k": 0, "returned": 0, "seed": 56, "top_score": null}
SEED_RESULT {"candidates": 6, "k": 4, "returned": 4, "seed": 57, "top_score": 0.9255273332551734}
SEED_RESULT {"candidates": 6, "k": 8, "returned": 6, "seed": 58, "top_score": 0.9656989871957143}
SEED_RESULT {"candidates": 6, "k": 9, "returned": 6, "seed": 59, "top_score": 0.9022742489750794}
SEED_RESULT {"candidates": 6, "k": 5, "returned": 5, "seed": 60, "top_score": 0.7809403107662466}
SEED_RESULT {"candidates": 6, "k": 4, "returned": 4, "seed": 61, "top_score": 0.9974481812128662}
SEED_RESULT {"candidates": 6, "k": 4, "returned": 4, "seed": 62, "top_score": 0.9322420054734148}
SEED_RESULT {"candidates": 6, "k": 9, "returned": 6, "seed": 63, "top_score": 0.9925344186214843}
SEED_RESULT {"candidates": 6, "k": 3, "returned": 3, "seed": 64, "top_score": 0.7908801099212472}
SEED_RESULT {"candidates": 6, "k": 0, "returned": 0, "seed": 65, "top_score": null}
SEED_RESULT {"candidates": 6, "k": 0, "returned": 0, "seed": 66, "top_score": null}
SEED_RESULT {"candidates": 6, "k": 9, "returned": 6, "seed": 67, "top_score": 0.8839050033117334}
SEED_RESULT {"candidates": 6, "k": 1, "returned": 1, "seed": 68, "top_score": 0.9531372738861585}
SEED_RESULT {"candidates": 6, "k": 2, "returned": 2, "seed": 69, "top_score": 0.9399241757761553}
SEED_RESULT {"candidates": 6, "k": 6, "returned": 6, "seed": 70, "top_score": 0.9622437404963254}
SEED_RESULT {"candidates": 6, "k": 1, "returned": 1, "seed": 71, "top_score": 0.949365863527048}
SEED_RESULT {"candidates": 6, "k": 5, "returned": 5, "seed": 72, "top_score": 0.8830033683046548}
SEED_RESULT {"candidates": 6, "k": 2, "returned": 2, "seed": 73, "top_score": 0.7783857469679161}
SEED_RESULT {"candidates": 6, "k": 5, "returned": 5, "seed": 74, "top_score": 0.9736921662557304}
SEED_RESULT {"candidates": 6, "k": 8, "returned": 6, "seed": 75, "top_score": 0.9940641587740334}
SEED_RESULT {"candidates": 6, "k": 0, "returned": 0, "seed": 76, "top_score": null}
SEED_RESULT {"candidates": 6, "k": 6, "returned": 6, "seed": 77, "top_score": 0.8952616123675781}
SEED_RESULT {"candidates": 6, "k": 2, "returned": 2, "seed": 78, "top_score": 0.9638658634986221}
SEED_RESULT {"candidates": 6, "k": 0, "returned": 0, "seed": 79, "top_score": null}
SEED_RESULT {"candidates": 6, "k": 9, "returned": 6, "seed": 80, "top_score": 0.8202072051902122}
SEED_RESULT {"candidates": 6, "k": 6, "returned": 6, "seed": 81, "top_score": 0.9779026848527338}
SEED_RESULT {"candidates": 6, "k": 7, "returned": 6, "seed": 82, "top_score": 0.9788782306566062}
SEED_RESULT {"candidates": 6, "k": 7, "returned": 6, "seed": 83, "top_score": 0.9805069269446955}
SEED_RESULT {"candidates": 6, "k": 0, "returned": 0, "seed": 84, "top_score": null}
SEED_RESULT {"candidates": 6, "k": 3, "returned": 3, "seed": 85, "top_score": 0.9446121152148226}
SEED_RESULT {"candidates": 6, "k": 5, "returned": 5, "seed": 86, "top_score": 0.9327341342600669}
SEED_RESULT {"candidates": 6, "k": 3, "returned": 3, "seed": 87, "top_score": 0.8914994847743576}
SEED_RESULT {"candidates": 6, "k": 1, "returned": 1, "seed": 88, "top_score": 0.8265882911281659}
SEED_RESULT {"candidates": 6, "k": 6, "returned": 6, "seed": 89, "top_score": 0.8966213943709433}
SEED_RESULT {"candidates": 6, "k": 3, "returned": 3, "seed": 90, "top_score": 0.8736353188516631}
SEED_RESULT {"candidates": 6, "k": 1, "returned": 1, "seed": 91, "top_score": 0.85601899598563}
SEED_RESULT {"candidates": 6, "k": 9, "returned": 6, "seed": 92, "top_score": 0.9516060327223655}
SEED_RESULT {"candidates": 6, "k": 2, "returned": 2, "seed": 93, "top_score": 0.9699920415548174}
SEED_RESULT {"candidates": 6, "k": 3, "returned": 3, "seed": 94, "top_score": 0.8738568395152049}
SEED_RESULT {"candidates": 6, "k": 2, "returned": 2, "seed": 95, "top_score": 0.9668269320690481}
SEED_RESULT {"candidates": 6, "k": 6, "returned": 6, "seed": 96, "top_score": 0.8596891344173593}
SEED_RESULT {"candidates": 6, "k": 3, "returned": 3, "seed": 97, "top_score": 0.806688244508588}
SEED_RESULT {"candidates": 6, "k": 8, "returned": 6, "seed": 98, "top_score": 0.9503098749938929}
SEED_RESULT {"candidates": 6, "k": 0, "returned": 0, "seed": 99, "top_score": null}
TEST_SUMMARY {"tests_run": 112, "failures": 0, "errors": 0, "skipped": 0, "successful": true}
```

**stderr** — [file TXT](streams/001_unittest_project_suite.stderr.txt)

```text
test_determinism (test_p076.RecommenderContracts.test_determinism) ... ok
test_exclusions_and_empty_catalog (test_p076.RecommenderContracts.test_exclusions_and_empty_catalog) ... ok
test_extreme_finite_scaling (test_p076.RecommenderContracts.test_extreme_finite_scaling) ... ok
test_inputs_are_not_modified (test_p076.RecommenderContracts.test_inputs_are_not_modified) ... ok
test_invalid_catalog (test_p076.RecommenderContracts.test_invalid_catalog) ... ok
test_invalid_exclude (test_p076.RecommenderContracts.test_invalid_exclude) ... ok
test_invalid_k (test_p076.RecommenderContracts.test_invalid_k) ... ok
test_invalid_profile (test_p076.RecommenderContracts.test_invalid_profile) ... ok
test_k_zero_and_larger_than_catalog (test_p076.RecommenderContracts.test_k_zero_and_larger_than_catalog) ... ok
test_orthogonal_vectors (test_p076.RecommenderContracts.test_orthogonal_vectors) ... ok
test_reference_ranking (test_p076.RecommenderContracts.test_reference_ranking) ... ok
test_ties_ignore_catalog_insertion_order (test_p076.RecommenderContracts.test_ties_ignore_catalog_insertion_order) ... ok
test_seed_000 (test_p076.SeededOracleChecks.test_seed_000) ... ok
test_seed_001 (test_p076.SeededOracleChecks.test_seed_001) ... ok
test_seed_002 (test_p076.SeededOracleChecks.test_seed_002) ... ok
test_seed_003 (test_p076.SeededOracleChecks.test_seed_003) ... ok
test_seed_004 (test_p076.SeededOracleChecks.test_seed_004) ... ok
test_seed_005 (test_p076.SeededOracleChecks.test_seed_005) ... ok
test_seed_006 (test_p076.SeededOracleChecks.test_seed_006) ... ok
test_seed_007 (test_p076.SeededOracleChecks.test_seed_007) ... ok
test_seed_008 (test_p076.SeededOracleChecks.test_seed_008) ... ok
test_seed_009 (test_p076.SeededOracleChecks.test_seed_009) ... ok
test_seed_010 (test_p076.SeededOracleChecks.test_seed_010) ... ok
test_seed_011 (test_p076.SeededOracleChecks.test_seed_011) ... ok
test_seed_012 (test_p076.SeededOracleChecks.test_seed_012) ... ok
test_seed_013 (test_p076.SeededOracleChecks.test_seed_013) ... ok
test_seed_014 (test_p076.SeededOracleChecks.test_seed_014) ... ok
test_seed_015 (test_p076.SeededOracleChecks.test_seed_015) ... ok
test_seed_016 (test_p076.SeededOracleChecks.test_seed_016) ... ok
test_seed_017 (test_p076.SeededOracleChecks.test_seed_017) ... ok
test_seed_018 (test_p076.SeededOracleChecks.test_seed_018) ... ok
test_seed_019 (test_p076.SeededOracleChecks.test_seed_019) ... ok
test_seed_020 (test_p076.SeededOracleChecks.test_seed_020) ... ok
test_seed_021 (test_p076.SeededOracleChecks.test_seed_021) ... ok
test_seed_022 (test_p076.SeededOracleChecks.test_seed_022) ... ok
test_seed_023 (test_p076.SeededOracleChecks.test_seed_023) ... ok
test_seed_024 (test_p076.SeededOracleChecks.test_seed_024) ... ok
test_seed_025 (test_p076.SeededOracleChecks.test_seed_025) ... ok
test_seed_026 (test_p076.SeededOracleChecks.test_seed_026) ... ok
test_seed_027 (test_p076.SeededOracleChecks.test_seed_027) ... ok
test_seed_028 (test_p076.SeededOracleChecks.test_seed_028) ... ok
test_seed_029 (test_p076.SeededOracleChecks.test_seed_029) ... ok
test_seed_030 (test_p076.SeededOracleChecks.test_seed_030) ... ok
test_seed_031 (test_p076.SeededOracleChecks.test_seed_031) ... ok
test_seed_032 (test_p076.SeededOracleChecks.test_seed_032) ... ok
test_seed_033 (test_p076.SeededOracleChecks.test_seed_033) ... ok
test_seed_034 (test_p076.SeededOracleChecks.test_seed_034) ... ok
test_seed_035 (test_p076.SeededOracleChecks.test_seed_035) ... ok
test_seed_036 (test_p076.SeededOracleChecks.test_seed_036) ... ok
test_seed_037 (test_p076.SeededOracleChecks.test_seed_037) ... ok
test_seed_038 (test_p076.SeededOracleChecks.test_seed_038) ... ok
test_seed_039 (test_p076.SeededOracleChecks.test_seed_039) ... ok
test_seed_040 (test_p076.SeededOracleChecks.test_seed_040) ... ok
test_seed_041 (test_p076.SeededOracleChecks.test_seed_041) ... ok
test_seed_042 (test_p076.SeededOracleChecks.test_seed_042) ... ok
test_seed_043 (test_p076.SeededOracleChecks.test_seed_043) ... ok
test_seed_044 (test_p076.SeededOracleChecks.test_seed_044) ... ok
test_seed_045 (test_p076.SeededOracleChecks.test_seed_045) ... ok
test_seed_046 (test_p076.SeededOracleChecks.test_seed_046) ... ok
test_seed_047 (test_p076.SeededOracleChecks.test_seed_047) ... ok
test_seed_048 (test_p076.SeededOracleChecks.test_seed_048) ... ok
test_seed_049 (test_p076.SeededOracleChecks.test_seed_049) ... ok
test_seed_050 (test_p076.SeededOracleChecks.test_seed_050) ... ok
test_seed_051 (test_p076.SeededOracleChecks.test_seed_051) ... ok
test_seed_052 (test_p076.SeededOracleChecks.test_seed_052) ... ok
test_seed_053 (test_p076.SeededOracleChecks.test_seed_053) ... ok
test_seed_054 (test_p076.SeededOracleChecks.test_seed_054) ... ok
test_seed_055 (test_p076.SeededOracleChecks.test_seed_055) ... ok
test_seed_056 (test_p076.SeededOracleChecks.test_seed_056) ... ok
test_seed_057 (test_p076.SeededOracleChecks.test_seed_057) ... ok
test_seed_058 (test_p076.SeededOracleChecks.test_seed_058) ... ok
test_seed_059 (test_p076.SeededOracleChecks.test_seed_059) ... ok
test_seed_060 (test_p076.SeededOracleChecks.test_seed_060) ... ok
test_seed_061 (test_p076.SeededOracleChecks.test_seed_061) ... ok
test_seed_062 (test_p076.SeededOracleChecks.test_seed_062) ... ok
test_seed_063 (test_p076.SeededOracleChecks.test_seed_063) ... ok
test_seed_064 (test_p076.SeededOracleChecks.test_seed_064) ... ok
test_seed_065 (test_p076.SeededOracleChecks.test_seed_065) ... ok
test_seed_066 (test_p076.SeededOracleChecks.test_seed_066) ... ok
test_seed_067 (test_p076.SeededOracleChecks.test_seed_067) ... ok
test_seed_068 (test_p076.SeededOracleChecks.test_seed_068) ... ok
test_seed_069 (test_p076.SeededOracleChecks.test_seed_069) ... ok
test_seed_070 (test_p076.SeededOracleChecks.test_seed_070) ... ok
test_seed_071 (test_p076.SeededOracleChecks.test_seed_071) ... ok
test_seed_072 (test_p076.SeededOracleChecks.test_seed_072) ... ok
test_seed_073 (test_p076.SeededOracleChecks.test_seed_073) ... ok
test_seed_074 (test_p076.SeededOracleChecks.test_seed_074) ... ok
test_seed_075 (test_p076.SeededOracleChecks.test_seed_075) ... ok
test_seed_076 (test_p076.SeededOracleChecks.test_seed_076) ... ok
test_seed_077 (test_p076.SeededOracleChecks.test_seed_077) ... ok
test_seed_078 (test_p076.SeededOracleChecks.test_seed_078) ... ok
test_seed_079 (test_p076.SeededOracleChecks.test_seed_079) ... ok
test_seed_080 (test_p076.SeededOracleChecks.test_seed_080) ... ok
test_seed_081 (test_p076.SeededOracleChecks.test_seed_081) ... ok
test_seed_082 (test_p076.SeededOracleChecks.test_seed_082) ... ok
test_seed_083 (test_p076.SeededOracleChecks.test_seed_083) ... ok
test_seed_084 (test_p076.SeededOracleChecks.test_seed_084) ... ok
test_seed_085 (test_p076.SeededOracleChecks.test_seed_085) ... ok
test_seed_086 (test_p076.SeededOracleChecks.test_seed_086) ... ok
test_seed_087 (test_p076.SeededOracleChecks.test_seed_087) ... ok
test_seed_088 (test_p076.SeededOracleChecks.test_seed_088) ... ok
test_seed_089 (test_p076.SeededOracleChecks.test_seed_089) ... ok
test_seed_090 (test_p076.SeededOracleChecks.test_seed_090) ... ok
test_seed_091 (test_p076.SeededOracleChecks.test_seed_091) ... ok
test_seed_092 (test_p076.SeededOracleChecks.test_seed_092) ... ok
test_seed_093 (test_p076.SeededOracleChecks.test_seed_093) ... ok
test_seed_094 (test_p076.SeededOracleChecks.test_seed_094) ... ok
test_seed_095 (test_p076.SeededOracleChecks.test_seed_095) ... ok
test_seed_096 (test_p076.SeededOracleChecks.test_seed_096) ... ok
test_seed_097 (test_p076.SeededOracleChecks.test_seed_097) ... ok
test_seed_098 (test_p076.SeededOracleChecks.test_seed_098) ... ok
test_seed_099 (test_p076.SeededOracleChecks.test_seed_099) ... ok

----------------------------------------------------------------------
Ran 112 tests in 0.057s

OK
```

## Demo — processi separati dalle suite

Questi output provengono dalle demo eseguite dal runner. Non costituiscono nuovi metodi unittest.

### 002 · demo_recommender

Comando registrato (array degli argomenti; segnaposto dei metadati documentati nel manifest):

```json
["<PYTHON_HOME>/bin/python", "-B", "src/recommender.py"]
```

Esito: **PASS** · codice di uscita: `0`.

**stdout** — [file TXT](streams/002_demo_recommender.stdout.txt)

```text
P076 — profilo [1, 0, 1, 1]; ranking completo
ml: 1.000000
python: 0.816497
sql: 0.816497
java: 0.408248
reti: 0.408248
Escludendo ml: python, sql, java
```

**stderr** — [file TXT](streams/002_demo_recommender.stderr.txt)

Il processo non ha emesso byte su stderr. Il file collegato è vuoto (0 byte).

### 003 · demo_examples

Comando registrato (array degli argomenti; segnaposto dei metadati documentati nel manifest):

```json
["<PYTHON_HOME>/bin/python", "-B", "examples.py"]
```

Esito: **PASS** · codice di uscita: `0`.

**stdout** — [file TXT](streams/003_demo_examples.stdout.txt)

```text
profilo_sistemi_pratica: [["reti", 0.9999999999999998], ["java", 0.4999999999999999], ["python", 0.4999999999999999], ["sql", 0.4999999999999999], ["ml", 0.408248290463863]]
profilo_scalato: [["ml", 1.0], ["python", 0.816496580927726], ["sql", 0.816496580927726], ["java", 0.408248290463863], ["reti", 0.408248290463863]]
parita_alfabetica: [["alfa", 1.0], ["zeta", 1.0]]
catalogo_vuoto: []
k_zero: []
esercizio: [["java", 0.4999999999999999], ["python", 0.4999999999999999], ["sql", 0.4999999999999999], ["ml", 0.408248290463863]]
```

**stderr** — [file TXT](streams/003_demo_examples.stderr.txt)

Il processo non ha emesso byte su stderr. Il file collegato è vuoto (0 byte).

## Controlli runtime

Il record di questo progetto non contiene controlli classificati come `runtime_check`. L’assenza non aggiunge una verifica runtime alle suite del progetto.

## Verifica e provenienza

[Registro strutturato](registro.json) · [Hash e trasformazioni](MANIFEST.json) · [Policy](../AUDIT.md) · [Indice](../README.md)
