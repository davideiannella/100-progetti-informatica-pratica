# P075: output dei collaudi

[Indice dei collaudi](../README.md) · [Codice e istruzioni](../../projects/P075/README.md)

Esito registrato: **PASS**. [Run 39849393701](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701) · [job 120071206449](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701/job/120071206449).

Commit del runner: `44cd421247ca2bfe838baa735cf6180134f80464`. Sorgenti applicativi congelati: `32e201b1fb1258c4e7c77d32af323b966647b908`.

Ambiente registrato: Ubuntu 24.04 x86_64; Python 3.12.15 (main, Oct  1 2026, 02:35:59) [GCC 13.3.0]. Artifact: `p041-p080-core-39849393701-1` (ID `12456886835`); record originale: `P075/results.json`.

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

Rapporto registrato: 110 metodi unittest; failures 0, errors 0, skipped 0; sottocasi dichiarati 0.

**stdout** — [file TXT](streams/001_unittest_project_suite.stdout.txt)

```text
SEED_RESULT {"alerts": 37, "confusion_matrix": [[93, 7], [0, 30]], "f1": 0.8955223880597015, "false_positive_rate": 0.07, "precision": 0.8108108108108109, "recall": 1.0, "roc_auc": 1.0, "seed": 0}
SEED_RESULT {"alerts": 33, "confusion_matrix": [[97, 3], [0, 30]], "f1": 0.9523809523809523, "false_positive_rate": 0.03, "precision": 0.9090909090909091, "recall": 1.0, "roc_auc": 1.0, "seed": 1}
SEED_RESULT {"alerts": 48, "confusion_matrix": [[82, 18], [0, 30]], "f1": 0.7692307692307693, "false_positive_rate": 0.18, "precision": 0.625, "recall": 1.0, "roc_auc": 1.0, "seed": 2}
SEED_RESULT {"alerts": 40, "confusion_matrix": [[90, 10], [0, 30]], "f1": 0.8571428571428571, "false_positive_rate": 0.1, "precision": 0.75, "recall": 1.0, "roc_auc": 1.0, "seed": 3}
SEED_RESULT {"alerts": 38, "confusion_matrix": [[92, 8], [0, 30]], "f1": 0.8823529411764706, "false_positive_rate": 0.08, "precision": 0.7894736842105263, "recall": 1.0, "roc_auc": 1.0, "seed": 4}
SEED_RESULT {"alerts": 35, "confusion_matrix": [[95, 5], [0, 30]], "f1": 0.9230769230769231, "false_positive_rate": 0.05, "precision": 0.8571428571428571, "recall": 1.0, "roc_auc": 1.0, "seed": 5}
SEED_RESULT {"alerts": 36, "confusion_matrix": [[94, 6], [0, 30]], "f1": 0.9090909090909091, "false_positive_rate": 0.06, "precision": 0.8333333333333334, "recall": 1.0, "roc_auc": 1.0, "seed": 6}
SEED_RESULT {"alerts": 43, "confusion_matrix": [[87, 13], [0, 30]], "f1": 0.821917808219178, "false_positive_rate": 0.13, "precision": 0.6976744186046512, "recall": 1.0, "roc_auc": 1.0, "seed": 7}
SEED_RESULT {"alerts": 37, "confusion_matrix": [[93, 7], [0, 30]], "f1": 0.8955223880597015, "false_positive_rate": 0.07, "precision": 0.8108108108108109, "recall": 1.0, "roc_auc": 1.0, "seed": 8}
SEED_RESULT {"alerts": 37, "confusion_matrix": [[93, 7], [0, 30]], "f1": 0.8955223880597015, "false_positive_rate": 0.07, "precision": 0.8108108108108109, "recall": 1.0, "roc_auc": 1.0, "seed": 9}
SEED_RESULT {"alerts": 42, "confusion_matrix": [[88, 12], [0, 30]], "f1": 0.8333333333333334, "false_positive_rate": 0.12, "precision": 0.7142857142857143, "recall": 1.0, "roc_auc": 1.0, "seed": 10}
SEED_RESULT {"alerts": 37, "confusion_matrix": [[93, 7], [0, 30]], "f1": 0.8955223880597015, "false_positive_rate": 0.07, "precision": 0.8108108108108109, "recall": 1.0, "roc_auc": 1.0, "seed": 11}
SEED_RESULT {"alerts": 39, "confusion_matrix": [[91, 9], [0, 30]], "f1": 0.8695652173913043, "false_positive_rate": 0.09, "precision": 0.7692307692307693, "recall": 1.0, "roc_auc": 1.0, "seed": 12}
SEED_RESULT {"alerts": 35, "confusion_matrix": [[95, 5], [0, 30]], "f1": 0.9230769230769231, "false_positive_rate": 0.05, "precision": 0.8571428571428571, "recall": 1.0, "roc_auc": 1.0, "seed": 13}
SEED_RESULT {"alerts": 43, "confusion_matrix": [[87, 13], [0, 30]], "f1": 0.821917808219178, "false_positive_rate": 0.13, "precision": 0.6976744186046512, "recall": 1.0, "roc_auc": 1.0, "seed": 14}
SEED_RESULT {"alerts": 39, "confusion_matrix": [[91, 9], [0, 30]], "f1": 0.8695652173913043, "false_positive_rate": 0.09, "precision": 0.7692307692307693, "recall": 1.0, "roc_auc": 1.0, "seed": 15}
SEED_RESULT {"alerts": 47, "confusion_matrix": [[83, 17], [0, 30]], "f1": 0.7792207792207793, "false_positive_rate": 0.17, "precision": 0.6382978723404256, "recall": 1.0, "roc_auc": 1.0, "seed": 16}
SEED_RESULT {"alerts": 39, "confusion_matrix": [[91, 9], [0, 30]], "f1": 0.8695652173913043, "false_positive_rate": 0.09, "precision": 0.7692307692307693, "recall": 1.0, "roc_auc": 1.0, "seed": 17}
SEED_RESULT {"alerts": 37, "confusion_matrix": [[93, 7], [0, 30]], "f1": 0.8955223880597015, "false_positive_rate": 0.07, "precision": 0.8108108108108109, "recall": 1.0, "roc_auc": 0.99, "seed": 18}
SEED_RESULT {"alerts": 41, "confusion_matrix": [[89, 11], [0, 30]], "f1": 0.8450704225352113, "false_positive_rate": 0.11, "precision": 0.7317073170731707, "recall": 1.0, "roc_auc": 1.0, "seed": 19}
SEED_RESULT {"alerts": 34, "confusion_matrix": [[96, 4], [0, 30]], "f1": 0.9375, "false_positive_rate": 0.04, "precision": 0.8823529411764706, "recall": 1.0, "roc_auc": 1.0, "seed": 20}
SEED_RESULT {"alerts": 40, "confusion_matrix": [[90, 10], [0, 30]], "f1": 0.8571428571428571, "false_positive_rate": 0.1, "precision": 0.75, "recall": 1.0, "roc_auc": 1.0, "seed": 21}
SEED_RESULT {"alerts": 33, "confusion_matrix": [[97, 3], [0, 30]], "f1": 0.9523809523809523, "false_positive_rate": 0.03, "precision": 0.9090909090909091, "recall": 1.0, "roc_auc": 1.0, "seed": 22}
SEED_RESULT {"alerts": 46, "confusion_matrix": [[84, 16], [0, 30]], "f1": 0.7894736842105263, "false_positive_rate": 0.16, "precision": 0.6521739130434783, "recall": 1.0, "roc_auc": 1.0, "seed": 23}
SEED_RESULT {"alerts": 39, "confusion_matrix": [[91, 9], [0, 30]], "f1": 0.8695652173913043, "false_positive_rate": 0.09, "precision": 0.7692307692307693, "recall": 1.0, "roc_auc": 1.0, "seed": 24}
SEED_RESULT {"alerts": 42, "confusion_matrix": [[88, 12], [0, 30]], "f1": 0.8333333333333334, "false_positive_rate": 0.12, "precision": 0.7142857142857143, "recall": 1.0, "roc_auc": 1.0, "seed": 25}
SEED_RESULT {"alerts": 34, "confusion_matrix": [[96, 4], [0, 30]], "f1": 0.9375, "false_positive_rate": 0.04, "precision": 0.8823529411764706, "recall": 1.0, "roc_auc": 1.0, "seed": 26}
SEED_RESULT {"alerts": 47, "confusion_matrix": [[83, 17], [0, 30]], "f1": 0.7792207792207793, "false_positive_rate": 0.17, "precision": 0.6382978723404256, "recall": 1.0, "roc_auc": 1.0, "seed": 27}
SEED_RESULT {"alerts": 38, "confusion_matrix": [[92, 8], [0, 30]], "f1": 0.8823529411764706, "false_positive_rate": 0.08, "precision": 0.7894736842105263, "recall": 1.0, "roc_auc": 1.0, "seed": 28}
SEED_RESULT {"alerts": 37, "confusion_matrix": [[93, 7], [0, 30]], "f1": 0.8955223880597015, "false_positive_rate": 0.07, "precision": 0.8108108108108109, "recall": 1.0, "roc_auc": 1.0, "seed": 29}
SEED_RESULT {"alerts": 44, "confusion_matrix": [[86, 14], [0, 30]], "f1": 0.8108108108108109, "false_positive_rate": 0.14, "precision": 0.6818181818181818, "recall": 1.0, "roc_auc": 1.0, "seed": 30}
SEED_RESULT {"alerts": 37, "confusion_matrix": [[93, 7], [0, 30]], "f1": 0.8955223880597015, "false_positive_rate": 0.07, "precision": 0.8108108108108109, "recall": 1.0, "roc_auc": 1.0, "seed": 31}
SEED_RESULT {"alerts": 37, "confusion_matrix": [[93, 7], [0, 30]], "f1": 0.8955223880597015, "false_positive_rate": 0.07, "precision": 0.8108108108108109, "recall": 1.0, "roc_auc": 1.0, "seed": 32}
SEED_RESULT {"alerts": 33, "confusion_matrix": [[97, 3], [0, 30]], "f1": 0.9523809523809523, "false_positive_rate": 0.03, "precision": 0.9090909090909091, "recall": 1.0, "roc_auc": 1.0, "seed": 33}
SEED_RESULT {"alerts": 39, "confusion_matrix": [[91, 9], [0, 30]], "f1": 0.8695652173913043, "false_positive_rate": 0.09, "precision": 0.7692307692307693, "recall": 1.0, "roc_auc": 1.0, "seed": 34}
SEED_RESULT {"alerts": 39, "confusion_matrix": [[91, 9], [0, 30]], "f1": 0.8695652173913043, "false_positive_rate": 0.09, "precision": 0.7692307692307693, "recall": 1.0, "roc_auc": 1.0, "seed": 35}
SEED_RESULT {"alerts": 37, "confusion_matrix": [[93, 7], [0, 30]], "f1": 0.8955223880597015, "false_positive_rate": 0.07, "precision": 0.8108108108108109, "recall": 1.0, "roc_auc": 1.0, "seed": 36}
SEED_RESULT {"alerts": 38, "confusion_matrix": [[92, 8], [0, 30]], "f1": 0.8823529411764706, "false_positive_rate": 0.08, "precision": 0.7894736842105263, "recall": 1.0, "roc_auc": 1.0, "seed": 37}
SEED_RESULT {"alerts": 38, "confusion_matrix": [[92, 8], [0, 30]], "f1": 0.8823529411764706, "false_positive_rate": 0.08, "precision": 0.7894736842105263, "recall": 1.0, "roc_auc": 1.0, "seed": 38}
SEED_RESULT {"alerts": 40, "confusion_matrix": [[90, 10], [0, 30]], "f1": 0.8571428571428571, "false_positive_rate": 0.1, "precision": 0.75, "recall": 1.0, "roc_auc": 1.0, "seed": 39}
SEED_RESULT {"alerts": 38, "confusion_matrix": [[92, 8], [0, 30]], "f1": 0.8823529411764706, "false_positive_rate": 0.08, "precision": 0.7894736842105263, "recall": 1.0, "roc_auc": 1.0, "seed": 40}
SEED_RESULT {"alerts": 35, "confusion_matrix": [[95, 5], [0, 30]], "f1": 0.9230769230769231, "false_positive_rate": 0.05, "precision": 0.8571428571428571, "recall": 1.0, "roc_auc": 1.0, "seed": 41}
SEED_RESULT {"alerts": 37, "confusion_matrix": [[93, 7], [0, 30]], "f1": 0.8955223880597015, "false_positive_rate": 0.07, "precision": 0.8108108108108109, "recall": 1.0, "roc_auc": 1.0, "seed": 42}
SEED_RESULT {"alerts": 42, "confusion_matrix": [[88, 12], [0, 30]], "f1": 0.8333333333333334, "false_positive_rate": 0.12, "precision": 0.7142857142857143, "recall": 1.0, "roc_auc": 1.0, "seed": 43}
SEED_RESULT {"alerts": 36, "confusion_matrix": [[94, 6], [0, 30]], "f1": 0.9090909090909091, "false_positive_rate": 0.06, "precision": 0.8333333333333334, "recall": 1.0, "roc_auc": 1.0, "seed": 44}
SEED_RESULT {"alerts": 40, "confusion_matrix": [[90, 10], [0, 30]], "f1": 0.8571428571428571, "false_positive_rate": 0.1, "precision": 0.75, "recall": 1.0, "roc_auc": 1.0, "seed": 45}
SEED_RESULT {"alerts": 40, "confusion_matrix": [[90, 10], [0, 30]], "f1": 0.8571428571428571, "false_positive_rate": 0.1, "precision": 0.75, "recall": 1.0, "roc_auc": 1.0, "seed": 46}
SEED_RESULT {"alerts": 43, "confusion_matrix": [[87, 13], [0, 30]], "f1": 0.821917808219178, "false_positive_rate": 0.13, "precision": 0.6976744186046512, "recall": 1.0, "roc_auc": 1.0, "seed": 47}
SEED_RESULT {"alerts": 37, "confusion_matrix": [[93, 7], [0, 30]], "f1": 0.8955223880597015, "false_positive_rate": 0.07, "precision": 0.8108108108108109, "recall": 1.0, "roc_auc": 1.0, "seed": 48}
SEED_RESULT {"alerts": 36, "confusion_matrix": [[94, 6], [0, 30]], "f1": 0.9090909090909091, "false_positive_rate": 0.06, "precision": 0.8333333333333334, "recall": 1.0, "roc_auc": 1.0, "seed": 49}
SEED_RESULT {"alerts": 39, "confusion_matrix": [[91, 9], [0, 30]], "f1": 0.8695652173913043, "false_positive_rate": 0.09, "precision": 0.7692307692307693, "recall": 1.0, "roc_auc": 1.0, "seed": 50}
SEED_RESULT {"alerts": 38, "confusion_matrix": [[92, 8], [0, 30]], "f1": 0.8823529411764706, "false_positive_rate": 0.08, "precision": 0.7894736842105263, "recall": 1.0, "roc_auc": 1.0, "seed": 51}
SEED_RESULT {"alerts": 39, "confusion_matrix": [[91, 9], [0, 30]], "f1": 0.8695652173913043, "false_positive_rate": 0.09, "precision": 0.7692307692307693, "recall": 1.0, "roc_auc": 1.0, "seed": 52}
SEED_RESULT {"alerts": 37, "confusion_matrix": [[93, 7], [0, 30]], "f1": 0.8955223880597015, "false_positive_rate": 0.07, "precision": 0.8108108108108109, "recall": 1.0, "roc_auc": 1.0, "seed": 53}
SEED_RESULT {"alerts": 36, "confusion_matrix": [[94, 6], [0, 30]], "f1": 0.9090909090909091, "false_positive_rate": 0.06, "precision": 0.8333333333333334, "recall": 1.0, "roc_auc": 1.0, "seed": 54}
SEED_RESULT {"alerts": 40, "confusion_matrix": [[90, 10], [0, 30]], "f1": 0.8571428571428571, "false_positive_rate": 0.1, "precision": 0.75, "recall": 1.0, "roc_auc": 1.0, "seed": 55}
SEED_RESULT {"alerts": 39, "confusion_matrix": [[91, 9], [0, 30]], "f1": 0.8695652173913043, "false_positive_rate": 0.09, "precision": 0.7692307692307693, "recall": 1.0, "roc_auc": 1.0, "seed": 56}
SEED_RESULT {"alerts": 43, "confusion_matrix": [[87, 13], [0, 30]], "f1": 0.821917808219178, "false_positive_rate": 0.13, "precision": 0.6976744186046512, "recall": 1.0, "roc_auc": 1.0, "seed": 57}
SEED_RESULT {"alerts": 37, "confusion_matrix": [[93, 7], [0, 30]], "f1": 0.8955223880597015, "false_positive_rate": 0.07, "precision": 0.8108108108108109, "recall": 1.0, "roc_auc": 1.0, "seed": 58}
SEED_RESULT {"alerts": 39, "confusion_matrix": [[91, 9], [0, 30]], "f1": 0.8695652173913043, "false_positive_rate": 0.09, "precision": 0.7692307692307693, "recall": 1.0, "roc_auc": 1.0, "seed": 59}
SEED_RESULT {"alerts": 45, "confusion_matrix": [[85, 15], [0, 30]], "f1": 0.8, "false_positive_rate": 0.15, "precision": 0.6666666666666666, "recall": 1.0, "roc_auc": 1.0, "seed": 60}
SEED_RESULT {"alerts": 41, "confusion_matrix": [[89, 11], [0, 30]], "f1": 0.8450704225352113, "false_positive_rate": 0.11, "precision": 0.7317073170731707, "recall": 1.0, "roc_auc": 1.0, "seed": 61}
SEED_RESULT {"alerts": 39, "confusion_matrix": [[91, 9], [0, 30]], "f1": 0.8695652173913043, "false_positive_rate": 0.09, "precision": 0.7692307692307693, "recall": 1.0, "roc_auc": 1.0, "seed": 62}
SEED_RESULT {"alerts": 42, "confusion_matrix": [[88, 12], [0, 30]], "f1": 0.8333333333333334, "false_positive_rate": 0.12, "precision": 0.7142857142857143, "recall": 1.0, "roc_auc": 1.0, "seed": 63}
SEED_RESULT {"alerts": 39, "confusion_matrix": [[91, 9], [0, 30]], "f1": 0.8695652173913043, "false_positive_rate": 0.09, "precision": 0.7692307692307693, "recall": 1.0, "roc_auc": 1.0, "seed": 64}
SEED_RESULT {"alerts": 46, "confusion_matrix": [[84, 16], [0, 30]], "f1": 0.7894736842105263, "false_positive_rate": 0.16, "precision": 0.6521739130434783, "recall": 1.0, "roc_auc": 1.0, "seed": 65}
SEED_RESULT {"alerts": 34, "confusion_matrix": [[96, 4], [0, 30]], "f1": 0.9375, "false_positive_rate": 0.04, "precision": 0.8823529411764706, "recall": 1.0, "roc_auc": 1.0, "seed": 66}
SEED_RESULT {"alerts": 39, "confusion_matrix": [[91, 9], [0, 30]], "f1": 0.8695652173913043, "false_positive_rate": 0.09, "precision": 0.7692307692307693, "recall": 1.0, "roc_auc": 1.0, "seed": 67}
SEED_RESULT {"alerts": 41, "confusion_matrix": [[89, 11], [0, 30]], "f1": 0.8450704225352113, "false_positive_rate": 0.11, "precision": 0.7317073170731707, "recall": 1.0, "roc_auc": 1.0, "seed": 68}
SEED_RESULT {"alerts": 38, "confusion_matrix": [[92, 8], [0, 30]], "f1": 0.8823529411764706, "false_positive_rate": 0.08, "precision": 0.7894736842105263, "recall": 1.0, "roc_auc": 1.0, "seed": 69}
SEED_RESULT {"alerts": 40, "confusion_matrix": [[90, 10], [0, 30]], "f1": 0.8571428571428571, "false_positive_rate": 0.1, "precision": 0.75, "recall": 1.0, "roc_auc": 1.0, "seed": 70}
SEED_RESULT {"alerts": 40, "confusion_matrix": [[90, 10], [0, 30]], "f1": 0.8571428571428571, "false_positive_rate": 0.1, "precision": 0.75, "recall": 1.0, "roc_auc": 1.0, "seed": 71}
SEED_RESULT {"alerts": 34, "confusion_matrix": [[96, 4], [0, 30]], "f1": 0.9375, "false_positive_rate": 0.04, "precision": 0.8823529411764706, "recall": 1.0, "roc_auc": 1.0, "seed": 72}
SEED_RESULT {"alerts": 35, "confusion_matrix": [[95, 5], [0, 30]], "f1": 0.9230769230769231, "false_positive_rate": 0.05, "precision": 0.8571428571428571, "recall": 1.0, "roc_auc": 1.0, "seed": 73}
SEED_RESULT {"alerts": 33, "confusion_matrix": [[97, 3], [0, 30]], "f1": 0.9523809523809523, "false_positive_rate": 0.03, "precision": 0.9090909090909091, "recall": 1.0, "roc_auc": 1.0, "seed": 74}
SEED_RESULT {"alerts": 33, "confusion_matrix": [[97, 3], [0, 30]], "f1": 0.9523809523809523, "false_positive_rate": 0.03, "precision": 0.9090909090909091, "recall": 1.0, "roc_auc": 1.0, "seed": 75}
SEED_RESULT {"alerts": 36, "confusion_matrix": [[94, 6], [0, 30]], "f1": 0.9090909090909091, "false_positive_rate": 0.06, "precision": 0.8333333333333334, "recall": 1.0, "roc_auc": 1.0, "seed": 76}
SEED_RESULT {"alerts": 43, "confusion_matrix": [[87, 13], [0, 30]], "f1": 0.821917808219178, "false_positive_rate": 0.13, "precision": 0.6976744186046512, "recall": 1.0, "roc_auc": 1.0, "seed": 77}
SEED_RESULT {"alerts": 36, "confusion_matrix": [[94, 6], [0, 30]], "f1": 0.9090909090909091, "false_positive_rate": 0.06, "precision": 0.8333333333333334, "recall": 1.0, "roc_auc": 1.0, "seed": 78}
SEED_RESULT {"alerts": 38, "confusion_matrix": [[92, 8], [0, 30]], "f1": 0.8823529411764706, "false_positive_rate": 0.08, "precision": 0.7894736842105263, "recall": 1.0, "roc_auc": 1.0, "seed": 79}
SEED_RESULT {"alerts": 34, "confusion_matrix": [[96, 4], [0, 30]], "f1": 0.9375, "false_positive_rate": 0.04, "precision": 0.8823529411764706, "recall": 1.0, "roc_auc": 1.0, "seed": 80}
SEED_RESULT {"alerts": 38, "confusion_matrix": [[92, 8], [0, 30]], "f1": 0.8823529411764706, "false_positive_rate": 0.08, "precision": 0.7894736842105263, "recall": 1.0, "roc_auc": 1.0, "seed": 81}
SEED_RESULT {"alerts": 39, "confusion_matrix": [[91, 9], [0, 30]], "f1": 0.8695652173913043, "false_positive_rate": 0.09, "precision": 0.7692307692307693, "recall": 1.0, "roc_auc": 1.0, "seed": 82}
SEED_RESULT {"alerts": 36, "confusion_matrix": [[94, 6], [0, 30]], "f1": 0.9090909090909091, "false_positive_rate": 0.06, "precision": 0.8333333333333334, "recall": 1.0, "roc_auc": 1.0, "seed": 83}
SEED_RESULT {"alerts": 44, "confusion_matrix": [[86, 14], [0, 30]], "f1": 0.8108108108108109, "false_positive_rate": 0.14, "precision": 0.6818181818181818, "recall": 1.0, "roc_auc": 1.0, "seed": 84}
SEED_RESULT {"alerts": 33, "confusion_matrix": [[97, 3], [0, 30]], "f1": 0.9523809523809523, "false_positive_rate": 0.03, "precision": 0.9090909090909091, "recall": 1.0, "roc_auc": 1.0, "seed": 85}
SEED_RESULT {"alerts": 39, "confusion_matrix": [[91, 9], [0, 30]], "f1": 0.8695652173913043, "false_positive_rate": 0.09, "precision": 0.7692307692307693, "recall": 1.0, "roc_auc": 1.0, "seed": 86}
SEED_RESULT {"alerts": 36, "confusion_matrix": [[94, 6], [0, 30]], "f1": 0.9090909090909091, "false_positive_rate": 0.06, "precision": 0.8333333333333334, "recall": 1.0, "roc_auc": 1.0, "seed": 87}
SEED_RESULT {"alerts": 41, "confusion_matrix": [[89, 11], [0, 30]], "f1": 0.8450704225352113, "false_positive_rate": 0.11, "precision": 0.7317073170731707, "recall": 1.0, "roc_auc": 1.0, "seed": 88}
SEED_RESULT {"alerts": 42, "confusion_matrix": [[88, 12], [0, 30]], "f1": 0.8333333333333334, "false_positive_rate": 0.12, "precision": 0.7142857142857143, "recall": 1.0, "roc_auc": 1.0, "seed": 89}
SEED_RESULT {"alerts": 40, "confusion_matrix": [[90, 10], [0, 30]], "f1": 0.8571428571428571, "false_positive_rate": 0.1, "precision": 0.75, "recall": 1.0, "roc_auc": 1.0, "seed": 90}
SEED_RESULT {"alerts": 37, "confusion_matrix": [[93, 7], [0, 30]], "f1": 0.8955223880597015, "false_positive_rate": 0.07, "precision": 0.8108108108108109, "recall": 1.0, "roc_auc": 1.0, "seed": 91}
SEED_RESULT {"alerts": 33, "confusion_matrix": [[97, 3], [0, 30]], "f1": 0.9523809523809523, "false_positive_rate": 0.03, "precision": 0.9090909090909091, "recall": 1.0, "roc_auc": 1.0, "seed": 92}
SEED_RESULT {"alerts": 39, "confusion_matrix": [[91, 9], [0, 30]], "f1": 0.8695652173913043, "false_positive_rate": 0.09, "precision": 0.7692307692307693, "recall": 1.0, "roc_auc": 1.0, "seed": 93}
SEED_RESULT {"alerts": 38, "confusion_matrix": [[92, 8], [0, 30]], "f1": 0.8823529411764706, "false_positive_rate": 0.08, "precision": 0.7894736842105263, "recall": 1.0, "roc_auc": 1.0, "seed": 94}
SEED_RESULT {"alerts": 38, "confusion_matrix": [[92, 8], [0, 30]], "f1": 0.8823529411764706, "false_positive_rate": 0.08, "precision": 0.7894736842105263, "recall": 1.0, "roc_auc": 1.0, "seed": 95}
SEED_RESULT {"alerts": 40, "confusion_matrix": [[90, 10], [0, 30]], "f1": 0.8571428571428571, "false_positive_rate": 0.1, "precision": 0.75, "recall": 1.0, "roc_auc": 1.0, "seed": 96}
SEED_RESULT {"alerts": 36, "confusion_matrix": [[94, 6], [0, 30]], "f1": 0.9090909090909091, "false_positive_rate": 0.06, "precision": 0.8333333333333334, "recall": 1.0, "roc_auc": 1.0, "seed": 97}
SEED_RESULT {"alerts": 41, "confusion_matrix": [[89, 11], [0, 30]], "f1": 0.8450704225352113, "false_positive_rate": 0.11, "precision": 0.7317073170731707, "recall": 1.0, "roc_auc": 1.0, "seed": 98}
SEED_RESULT {"alerts": 36, "confusion_matrix": [[94, 6], [0, 30]], "f1": 0.9090909090909091, "false_positive_rate": 0.06, "precision": 0.8333333333333334, "recall": 1.0, "roc_auc": 1.0, "seed": 99}
TEST_SUMMARY {"tests_run": 110, "failures": 0, "errors": 0, "skipped": 0, "successful": true}
```

**stderr** — [file TXT](streams/001_unittest_project_suite.stderr.txt)

```text
test_absent_class_has_undefined_auc_and_fpr (test_p075.AnomalyContracts.test_absent_class_has_undefined_auc_and_fpr) ... ok
test_determinism (test_p075.AnomalyContracts.test_determinism) ... ok
test_hand_metrics_and_no_alert_baseline (test_p075.AnomalyContracts.test_hand_metrics_and_no_alert_baseline) ... ok
test_independent_generation_and_no_shared_memory (test_p075.AnomalyContracts.test_independent_generation_and_no_shared_memory) ... ok
test_invalid_matrices (test_p075.AnomalyContracts.test_invalid_matrices) ... ok
test_invalid_metrics (test_p075.AnomalyContracts.test_invalid_metrics) ... ok
test_invalid_parameters (test_p075.AnomalyContracts.test_invalid_parameters) ... ok
test_no_test_rows_in_fit (test_p075.AnomalyContracts.test_no_test_rows_in_fit) ... ok
test_offset_is_training_quantile (test_p075.AnomalyContracts.test_offset_is_training_quantile) ... ok
test_prediction_score_direction (test_p075.AnomalyContracts.test_prediction_score_direction) ... ok
test_seed_000 (test_p075.SeededOracleChecks.test_seed_000) ... ok
test_seed_001 (test_p075.SeededOracleChecks.test_seed_001) ... ok
test_seed_002 (test_p075.SeededOracleChecks.test_seed_002) ... ok
test_seed_003 (test_p075.SeededOracleChecks.test_seed_003) ... ok
test_seed_004 (test_p075.SeededOracleChecks.test_seed_004) ... ok
test_seed_005 (test_p075.SeededOracleChecks.test_seed_005) ... ok
test_seed_006 (test_p075.SeededOracleChecks.test_seed_006) ... ok
test_seed_007 (test_p075.SeededOracleChecks.test_seed_007) ... ok
test_seed_008 (test_p075.SeededOracleChecks.test_seed_008) ... ok
test_seed_009 (test_p075.SeededOracleChecks.test_seed_009) ... ok
test_seed_010 (test_p075.SeededOracleChecks.test_seed_010) ... ok
test_seed_011 (test_p075.SeededOracleChecks.test_seed_011) ... ok
test_seed_012 (test_p075.SeededOracleChecks.test_seed_012) ... ok
test_seed_013 (test_p075.SeededOracleChecks.test_seed_013) ... ok
test_seed_014 (test_p075.SeededOracleChecks.test_seed_014) ... ok
test_seed_015 (test_p075.SeededOracleChecks.test_seed_015) ... ok
test_seed_016 (test_p075.SeededOracleChecks.test_seed_016) ... ok
test_seed_017 (test_p075.SeededOracleChecks.test_seed_017) ... ok
test_seed_018 (test_p075.SeededOracleChecks.test_seed_018) ... ok
test_seed_019 (test_p075.SeededOracleChecks.test_seed_019) ... ok
test_seed_020 (test_p075.SeededOracleChecks.test_seed_020) ... ok
test_seed_021 (test_p075.SeededOracleChecks.test_seed_021) ... ok
test_seed_022 (test_p075.SeededOracleChecks.test_seed_022) ... ok
test_seed_023 (test_p075.SeededOracleChecks.test_seed_023) ... ok
test_seed_024 (test_p075.SeededOracleChecks.test_seed_024) ... ok
test_seed_025 (test_p075.SeededOracleChecks.test_seed_025) ... ok
test_seed_026 (test_p075.SeededOracleChecks.test_seed_026) ... ok
test_seed_027 (test_p075.SeededOracleChecks.test_seed_027) ... ok
test_seed_028 (test_p075.SeededOracleChecks.test_seed_028) ... ok
test_seed_029 (test_p075.SeededOracleChecks.test_seed_029) ... ok
test_seed_030 (test_p075.SeededOracleChecks.test_seed_030) ... ok
test_seed_031 (test_p075.SeededOracleChecks.test_seed_031) ... ok
test_seed_032 (test_p075.SeededOracleChecks.test_seed_032) ... ok
test_seed_033 (test_p075.SeededOracleChecks.test_seed_033) ... ok
test_seed_034 (test_p075.SeededOracleChecks.test_seed_034) ... ok
test_seed_035 (test_p075.SeededOracleChecks.test_seed_035) ... ok
test_seed_036 (test_p075.SeededOracleChecks.test_seed_036) ... ok
test_seed_037 (test_p075.SeededOracleChecks.test_seed_037) ... ok
test_seed_038 (test_p075.SeededOracleChecks.test_seed_038) ... ok
test_seed_039 (test_p075.SeededOracleChecks.test_seed_039) ... ok
test_seed_040 (test_p075.SeededOracleChecks.test_seed_040) ... ok
test_seed_041 (test_p075.SeededOracleChecks.test_seed_041) ... ok
test_seed_042 (test_p075.SeededOracleChecks.test_seed_042) ... ok
test_seed_043 (test_p075.SeededOracleChecks.test_seed_043) ... ok
test_seed_044 (test_p075.SeededOracleChecks.test_seed_044) ... ok
test_seed_045 (test_p075.SeededOracleChecks.test_seed_045) ... ok
test_seed_046 (test_p075.SeededOracleChecks.test_seed_046) ... ok
test_seed_047 (test_p075.SeededOracleChecks.test_seed_047) ... ok
test_seed_048 (test_p075.SeededOracleChecks.test_seed_048) ... ok
test_seed_049 (test_p075.SeededOracleChecks.test_seed_049) ... ok
test_seed_050 (test_p075.SeededOracleChecks.test_seed_050) ... ok
test_seed_051 (test_p075.SeededOracleChecks.test_seed_051) ... ok
test_seed_052 (test_p075.SeededOracleChecks.test_seed_052) ... ok
test_seed_053 (test_p075.SeededOracleChecks.test_seed_053) ... ok
test_seed_054 (test_p075.SeededOracleChecks.test_seed_054) ... ok
test_seed_055 (test_p075.SeededOracleChecks.test_seed_055) ... ok
test_seed_056 (test_p075.SeededOracleChecks.test_seed_056) ... ok
test_seed_057 (test_p075.SeededOracleChecks.test_seed_057) ... ok
test_seed_058 (test_p075.SeededOracleChecks.test_seed_058) ... ok
test_seed_059 (test_p075.SeededOracleChecks.test_seed_059) ... ok
test_seed_060 (test_p075.SeededOracleChecks.test_seed_060) ... ok
test_seed_061 (test_p075.SeededOracleChecks.test_seed_061) ... ok
test_seed_062 (test_p075.SeededOracleChecks.test_seed_062) ... ok
test_seed_063 (test_p075.SeededOracleChecks.test_seed_063) ... ok
test_seed_064 (test_p075.SeededOracleChecks.test_seed_064) ... ok
test_seed_065 (test_p075.SeededOracleChecks.test_seed_065) ... ok
test_seed_066 (test_p075.SeededOracleChecks.test_seed_066) ... ok
test_seed_067 (test_p075.SeededOracleChecks.test_seed_067) ... ok
test_seed_068 (test_p075.SeededOracleChecks.test_seed_068) ... ok
test_seed_069 (test_p075.SeededOracleChecks.test_seed_069) ... ok
test_seed_070 (test_p075.SeededOracleChecks.test_seed_070) ... ok
test_seed_071 (test_p075.SeededOracleChecks.test_seed_071) ... ok
test_seed_072 (test_p075.SeededOracleChecks.test_seed_072) ... ok
test_seed_073 (test_p075.SeededOracleChecks.test_seed_073) ... ok
test_seed_074 (test_p075.SeededOracleChecks.test_seed_074) ... ok
test_seed_075 (test_p075.SeededOracleChecks.test_seed_075) ... ok
test_seed_076 (test_p075.SeededOracleChecks.test_seed_076) ... ok
test_seed_077 (test_p075.SeededOracleChecks.test_seed_077) ... ok
test_seed_078 (test_p075.SeededOracleChecks.test_seed_078) ... ok
test_seed_079 (test_p075.SeededOracleChecks.test_seed_079) ... ok
test_seed_080 (test_p075.SeededOracleChecks.test_seed_080) ... ok
test_seed_081 (test_p075.SeededOracleChecks.test_seed_081) ... ok
test_seed_082 (test_p075.SeededOracleChecks.test_seed_082) ... ok
test_seed_083 (test_p075.SeededOracleChecks.test_seed_083) ... ok
test_seed_084 (test_p075.SeededOracleChecks.test_seed_084) ... ok
test_seed_085 (test_p075.SeededOracleChecks.test_seed_085) ... ok
test_seed_086 (test_p075.SeededOracleChecks.test_seed_086) ... ok
test_seed_087 (test_p075.SeededOracleChecks.test_seed_087) ... ok
test_seed_088 (test_p075.SeededOracleChecks.test_seed_088) ... ok
test_seed_089 (test_p075.SeededOracleChecks.test_seed_089) ... ok
test_seed_090 (test_p075.SeededOracleChecks.test_seed_090) ... ok
test_seed_091 (test_p075.SeededOracleChecks.test_seed_091) ... ok
test_seed_092 (test_p075.SeededOracleChecks.test_seed_092) ... ok
test_seed_093 (test_p075.SeededOracleChecks.test_seed_093) ... ok
test_seed_094 (test_p075.SeededOracleChecks.test_seed_094) ... ok
test_seed_095 (test_p075.SeededOracleChecks.test_seed_095) ... ok
test_seed_096 (test_p075.SeededOracleChecks.test_seed_096) ... ok
test_seed_097 (test_p075.SeededOracleChecks.test_seed_097) ... ok
test_seed_098 (test_p075.SeededOracleChecks.test_seed_098) ... ok
test_seed_099 (test_p075.SeededOracleChecks.test_seed_099) ... ok

----------------------------------------------------------------------
Ran 110 tests in 7.378s

OK
```

## Demo — processi separati dalle suite

Questi output provengono dalle demo eseguite dal runner. Non costituiscono nuovi metodi unittest.

### 002 · demo_anomaly

Comando registrato (array degli argomenti; segnaposto dei metadati documentati nel manifest):

```json
["<PYTHON_HOME>/bin/python", "-B", "src/anomaly.py"]
```

Esito: **PASS** · codice di uscita: `0`.

**stdout** — [file TXT](streams/002_demo_anomaly.stdout.txt)

```text
P075 — 300 normali in training; test indipendente: 100 normali e 30 anomalie
precision: 0.750000
recall: 1.000000
f1: 0.857143
false_positive_rate: 0.100000
roc_auc: 1.000000
alerts: 40
matrice [[TN, FP], [FN, TP]]: [[90, 10], [0, 30]]
offset appreso: -0.559153
baseline senza allarmi: recall 0.000000; f1 0.000000
```

**stderr** — [file TXT](streams/002_demo_anomaly.stderr.txt)

Il processo non ha emesso byte su stderr. Il file collegato è vuoto (0 byte).

### 003 · demo_examples

Comando registrato (array degli argomenti; segnaposto dei metadati documentati nel manifest):

```json
["<PYTHON_HOME>/bin/python", "-B", "examples.py"]
```

Esito: **PASS** · codice di uscita: `0`.

**stdout** — [file TXT](streams/003_demo_examples.stdout.txt)

```text
primo_caso: {"id": 409, "X": [143.21620913529793, 19.514969927440923], "vero": 1, "predetto": 1, "decision_function": -0.18891914892981665, "anomaly_score": 0.7480723888402291}
contamination: 0.01 {"precision": 1.0, "recall": 1.0, "f1": 1.0, "false_positive_rate": 0.0, "alerts": 30, "confusion_matrix": [[100, 0], [0, 30]], "roc_auc": 1.0}
contamination: 0.07 {"precision": 0.75, "recall": 1.0, "f1": 0.8571428571428571, "false_positive_rate": 0.1, "alerts": 40, "confusion_matrix": [[90, 10], [0, 30]], "roc_auc": 1.0}
contamination: 0.15 {"precision": 0.6122448979591837, "recall": 1.0, "f1": 0.759493670886076, "false_positive_rate": 0.19, "alerts": 49, "confusion_matrix": [[81, 19], [0, 30]], "roc_auc": 1.0}
esercizio: {"precision": 0.5, "recall": 0.5, "f1": 0.5, "false_positive_rate": 0.3333333333333333, "alerts": 2, "confusion_matrix": [[2, 1], [1, 1]], "roc_auc": null}
```

**stderr** — [file TXT](streams/003_demo_examples.stderr.txt)

Il processo non ha emesso byte su stderr. Il file collegato è vuoto (0 byte).

## Controlli runtime

Il record di questo progetto non contiene controlli classificati come `runtime_check`. L’assenza non aggiunge una verifica runtime alle suite del progetto.

## Verifica e provenienza

[Registro strutturato](registro.json) · [Hash e trasformazioni](MANIFEST.json) · [Policy](../AUDIT.md) · [Indice](../README.md)
