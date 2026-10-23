# P074 — output reali dei collaudi

Esito registrato: **PASS**. [Run 39849393701](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701) · [job 120071206449](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701/job/120071206449).

Commit del runner: `44cd421247ca2bfe838baa735cf6180134f80464`. Sorgenti applicativi congelati: `32e201b1fb1258c4e7c77d32af323b966647b908`.

Ambiente registrato: Ubuntu 24.04 x86_64; Python 3.12.15 (main, Oct  1 2026, 02:35:59) [GCC 13.3.0]. Artifact: `p041-p080-core-39849393701-1` (ID `12456886835`); record originale: `P074/results.json`.

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
SEED_RESULT {"accuracy": 0.625, "baseline_accuracy": 0.5666666666666667, "brier": 0.22914215841149926, "confusion_matrix": [[51, 17], [28, 24]], "f1": 0.5161290322580645, "log_loss": 0.6486048159644912, "positive_rate": 0.43333333333333335, "precision": 0.5853658536585366, "recall": 0.46153846153846156, "roc_auc": 0.6620475113122172, "seed": 0}
SEED_RESULT {"accuracy": 0.6833333333333333, "baseline_accuracy": 0.6, "brier": 0.20918004283379538, "confusion_matrix": [[58, 14], [24, 24]], "f1": 0.5581395348837209, "log_loss": 0.6077158931316734, "positive_rate": 0.4, "precision": 0.631578947368421, "recall": 0.5, "roc_auc": 0.7106481481481481, "seed": 1}
SEED_RESULT {"accuracy": 0.65, "baseline_accuracy": 0.6333333333333333, "brier": 0.21696042739655882, "confusion_matrix": [[62, 14], [28, 16]], "f1": 0.43243243243243246, "log_loss": 0.6238031475400418, "positive_rate": 0.36666666666666664, "precision": 0.5333333333333333, "recall": 0.36363636363636365, "roc_auc": 0.6815191387559809, "seed": 2}
SEED_RESULT {"accuracy": 0.6083333333333333, "baseline_accuracy": 0.575, "brier": 0.23235152549106275, "confusion_matrix": [[58, 11], [36, 15]], "f1": 0.38961038961038963, "log_loss": 0.6557298075209548, "positive_rate": 0.425, "precision": 0.5769230769230769, "recall": 0.29411764705882354, "roc_auc": 0.656720659278204, "seed": 3}
SEED_RESULT {"accuracy": 0.625, "baseline_accuracy": 0.5916666666666667, "brier": 0.21244367923143517, "confusion_matrix": [[57, 14], [31, 18]], "f1": 0.4444444444444444, "log_loss": 0.6090283536940063, "positive_rate": 0.4083333333333333, "precision": 0.5625, "recall": 0.3673469387755102, "roc_auc": 0.7056625467088243, "seed": 4}
SEED_RESULT {"accuracy": 0.75, "baseline_accuracy": 0.5833333333333334, "brier": 0.1916709935432978, "confusion_matrix": [[60, 10], [20, 30]], "f1": 0.6666666666666666, "log_loss": 0.5696398508286414, "positive_rate": 0.4166666666666667, "precision": 0.75, "recall": 0.6, "roc_auc": 0.8068571428571428, "seed": 5}
SEED_RESULT {"accuracy": 0.5916666666666667, "baseline_accuracy": 0.5416666666666666, "brier": 0.2386252235948972, "confusion_matrix": [[50, 15], [34, 21]], "f1": 0.46153846153846156, "log_loss": 0.6726072115191322, "positive_rate": 0.4583333333333333, "precision": 0.5833333333333334, "recall": 0.38181818181818183, "roc_auc": 0.6293706293706294, "seed": 6}
SEED_RESULT {"accuracy": 0.6083333333333333, "baseline_accuracy": 0.5666666666666667, "brier": 0.227428658330454, "confusion_matrix": [[56, 12], [35, 17]], "f1": 0.41975308641975306, "log_loss": 0.645156891510519, "positive_rate": 0.43333333333333335, "precision": 0.5862068965517241, "recall": 0.3269230769230769, "roc_auc": 0.6493212669683258, "seed": 7}
SEED_RESULT {"accuracy": 0.6583333333333333, "baseline_accuracy": 0.6416666666666667, "brier": 0.2031229626209404, "confusion_matrix": [[60, 17], [24, 19]], "f1": 0.4810126582278481, "log_loss": 0.5935722176491682, "positive_rate": 0.35833333333333334, "precision": 0.5277777777777778, "recall": 0.4418604651162791, "roc_auc": 0.7185140440954394, "seed": 8}
SEED_RESULT {"accuracy": 0.6583333333333333, "baseline_accuracy": 0.6, "brier": 0.21028450397049223, "confusion_matrix": [[61, 11], [30, 18]], "f1": 0.4675324675324675, "log_loss": 0.6083470895021367, "positive_rate": 0.4, "precision": 0.6206896551724138, "recall": 0.375, "roc_auc": 0.7225115740740741, "seed": 9}
SEED_RESULT {"accuracy": 0.5916666666666667, "baseline_accuracy": 0.6, "brier": 0.24438995147094913, "confusion_matrix": [[53, 19], [30, 18]], "f1": 0.4235294117647059, "log_loss": 0.6838944459924033, "positive_rate": 0.4, "precision": 0.4864864864864865, "recall": 0.375, "roc_auc": 0.5787037037037037, "seed": 10}
SEED_RESULT {"accuracy": 0.6916666666666667, "baseline_accuracy": 0.5916666666666667, "brier": 0.21123896147258148, "confusion_matrix": [[56, 15], [22, 27]], "f1": 0.5934065934065934, "log_loss": 0.611369609617441, "positive_rate": 0.4083333333333333, "precision": 0.6428571428571429, "recall": 0.5510204081632653, "roc_auc": 0.706812302385743, "seed": 11}
SEED_RESULT {"accuracy": 0.6166666666666667, "baseline_accuracy": 0.6, "brier": 0.23933135733261027, "confusion_matrix": [[54, 18], [28, 20]], "f1": 0.46511627906976744, "log_loss": 0.6752889974183144, "positive_rate": 0.4, "precision": 0.5263157894736842, "recall": 0.4166666666666667, "roc_auc": 0.6018518518518519, "seed": 12}
SEED_RESULT {"accuracy": 0.6416666666666667, "baseline_accuracy": 0.6166666666666667, "brier": 0.2240832224809065, "confusion_matrix": [[55, 19], [24, 22]], "f1": 0.5057471264367817, "log_loss": 0.6376067406329007, "positive_rate": 0.38333333333333336, "precision": 0.5365853658536586, "recall": 0.4782608695652174, "roc_auc": 0.6562867215041128, "seed": 13}
SEED_RESULT {"accuracy": 0.675, "baseline_accuracy": 0.5916666666666667, "brier": 0.21818436366738375, "confusion_matrix": [[60, 11], [28, 21]], "f1": 0.5185185185185185, "log_loss": 0.6259536168590937, "positive_rate": 0.4083333333333333, "precision": 0.65625, "recall": 0.42857142857142855, "roc_auc": 0.6809427996550733, "seed": 14}
SEED_RESULT {"accuracy": 0.7416666666666667, "baseline_accuracy": 0.6333333333333333, "brier": 0.202959929284518, "confusion_matrix": [[68, 8], [23, 21]], "f1": 0.5753424657534246, "log_loss": 0.5955972943876847, "positive_rate": 0.36666666666666664, "precision": 0.7241379310344828, "recall": 0.4772727272727273, "roc_auc": 0.7177033492822966, "seed": 15}
SEED_RESULT {"accuracy": 0.6833333333333333, "baseline_accuracy": 0.6, "brier": 0.2028932512830445, "confusion_matrix": [[58, 14], [24, 24]], "f1": 0.5581395348837209, "log_loss": 0.5917322586950384, "positive_rate": 0.4, "precision": 0.631578947368421, "recall": 0.5, "roc_auc": 0.7106481481481481, "seed": 16}
SEED_RESULT {"accuracy": 0.6583333333333333, "baseline_accuracy": 0.5583333333333333, "brier": 0.21233530047061328, "confusion_matrix": [[56, 11], [30, 23]], "f1": 0.5287356321839081, "log_loss": 0.6112093826011347, "positive_rate": 0.44166666666666665, "precision": 0.6764705882352942, "recall": 0.4339622641509434, "roc_auc": 0.7107856941706562, "seed": 17}
SEED_RESULT {"accuracy": 0.6416666666666667, "baseline_accuracy": 0.6, "brier": 0.22615450433915568, "confusion_matrix": [[66, 6], [37, 11]], "f1": 0.3384615384615385, "log_loss": 0.6435257953086496, "positive_rate": 0.4, "precision": 0.6470588235294118, "recall": 0.22916666666666666, "roc_auc": 0.6391782407407408, "seed": 18}
SEED_RESULT {"accuracy": 0.6166666666666667, "baseline_accuracy": 0.5583333333333333, "brier": 0.21493173519806721, "confusion_matrix": [[53, 14], [32, 21]], "f1": 0.4772727272727273, "log_loss": 0.6183074358842925, "positive_rate": 0.44166666666666665, "precision": 0.6, "recall": 0.39622641509433965, "roc_auc": 0.7065615319628274, "seed": 19}
SEED_RESULT {"accuracy": 0.5916666666666667, "baseline_accuracy": 0.5333333333333333, "brier": 0.23952576958988211, "confusion_matrix": [[51, 13], [36, 20]], "f1": 0.449438202247191, "log_loss": 0.6717081933563039, "positive_rate": 0.4666666666666667, "precision": 0.6060606060606061, "recall": 0.35714285714285715, "roc_auc": 0.638671875, "seed": 20}
SEED_RESULT {"accuracy": 0.6583333333333333, "baseline_accuracy": 0.6833333333333333, "brier": 0.20706025873106296, "confusion_matrix": [[71, 11], [30, 8]], "f1": 0.2807017543859649, "log_loss": 0.6011228166045586, "positive_rate": 0.31666666666666665, "precision": 0.42105263157894735, "recall": 0.21052631578947367, "roc_auc": 0.6643132220795892, "seed": 21}
SEED_RESULT {"accuracy": 0.5666666666666667, "baseline_accuracy": 0.475, "brier": 0.2659600140489077, "confusion_matrix": [[49, 8], [44, 19]], "f1": 0.4222222222222222, "log_loss": 0.7332766065231698, "positive_rate": 0.525, "precision": 0.7037037037037037, "recall": 0.30158730158730157, "roc_auc": 0.6109718741297689, "seed": 22}
SEED_RESULT {"accuracy": 0.6333333333333333, "baseline_accuracy": 0.55, "brier": 0.22610516184708065, "confusion_matrix": [[60, 6], [38, 16]], "f1": 0.42105263157894735, "log_loss": 0.6458558051640694, "positive_rate": 0.45, "precision": 0.7272727272727273, "recall": 0.2962962962962963, "roc_auc": 0.691638608305275, "seed": 23}
SEED_RESULT {"accuracy": 0.5416666666666666, "baseline_accuracy": 0.6083333333333333, "brier": 0.2554928079258813, "confusion_matrix": [[47, 26], [29, 18]], "f1": 0.3956043956043956, "log_loss": 0.7113486133585589, "positive_rate": 0.39166666666666666, "precision": 0.4090909090909091, "recall": 0.3829787234042553, "roc_auc": 0.569221801224133, "seed": 24}
SEED_RESULT {"accuracy": 0.6833333333333333, "baseline_accuracy": 0.6333333333333333, "brier": 0.21228575782372958, "confusion_matrix": [[63, 13], [25, 19]], "f1": 0.5, "log_loss": 0.6119979422272408, "positive_rate": 0.36666666666666664, "precision": 0.59375, "recall": 0.4318181818181818, "roc_auc": 0.6895933014354068, "seed": 25}
SEED_RESULT {"accuracy": 0.6083333333333333, "baseline_accuracy": 0.5416666666666666, "brier": 0.24203453342791406, "confusion_matrix": [[55, 10], [37, 18]], "f1": 0.43373493975903615, "log_loss": 0.6778398675099921, "positive_rate": 0.4583333333333333, "precision": 0.6428571428571429, "recall": 0.32727272727272727, "roc_auc": 0.6156643356643356, "seed": 26}
SEED_RESULT {"accuracy": 0.6583333333333333, "baseline_accuracy": 0.6083333333333333, "brier": 0.2193257627771056, "confusion_matrix": [[52, 21], [20, 27]], "f1": 0.5684210526315789, "log_loss": 0.6259705410538052, "positive_rate": 0.39166666666666666, "precision": 0.5625, "recall": 0.574468085106383, "roc_auc": 0.6627805304575927, "seed": 27}
SEED_RESULT {"accuracy": 0.55, "baseline_accuracy": 0.5083333333333333, "brier": 0.23583466474279463, "confusion_matrix": [[43, 18], [36, 23]], "f1": 0.46, "log_loss": 0.6630941508311333, "positive_rate": 0.49166666666666664, "precision": 0.5609756097560976, "recall": 0.3898305084745763, "roc_auc": 0.6348985829397055, "seed": 28}
SEED_RESULT {"accuracy": 0.7416666666666667, "baseline_accuracy": 0.55, "brier": 0.1942602474929102, "confusion_matrix": [[56, 10], [21, 33]], "f1": 0.6804123711340206, "log_loss": 0.5752851668868253, "positive_rate": 0.45, "precision": 0.7674418604651163, "recall": 0.6111111111111112, "roc_auc": 0.7396184062850729, "seed": 29}
SEED_RESULT {"accuracy": 0.6583333333333333, "baseline_accuracy": 0.625, "brier": 0.20403823393514114, "confusion_matrix": [[65, 10], [31, 14]], "f1": 0.4057971014492754, "log_loss": 0.593089413514685, "positive_rate": 0.375, "precision": 0.5833333333333334, "recall": 0.3111111111111111, "roc_auc": 0.6989629629629629, "seed": 30}
SEED_RESULT {"accuracy": 0.6083333333333333, "baseline_accuracy": 0.525, "brier": 0.23046135061123355, "confusion_matrix": [[52, 11], [36, 21]], "f1": 0.47191011235955055, "log_loss": 0.6562492383217593, "positive_rate": 0.475, "precision": 0.65625, "recall": 0.3684210526315789, "roc_auc": 0.7153996101364523, "seed": 31}
SEED_RESULT {"accuracy": 0.7, "baseline_accuracy": 0.6, "brier": 0.20465074679401105, "confusion_matrix": [[60, 12], [24, 24]], "f1": 0.5714285714285714, "log_loss": 0.5989219656190324, "positive_rate": 0.4, "precision": 0.6666666666666666, "recall": 0.5, "roc_auc": 0.728587962962963, "seed": 32}
SEED_RESULT {"accuracy": 0.6666666666666666, "baseline_accuracy": 0.575, "brier": 0.21355901747369002, "confusion_matrix": [[50, 19], [21, 30]], "f1": 0.6, "log_loss": 0.6208476616049334, "positive_rate": 0.425, "precision": 0.6122448979591837, "recall": 0.5882352941176471, "roc_auc": 0.7084398976982097, "seed": 33}
SEED_RESULT {"accuracy": 0.6833333333333333, "baseline_accuracy": 0.5916666666666667, "brier": 0.21225574693540356, "confusion_matrix": [[60, 11], [27, 22]], "f1": 0.5365853658536586, "log_loss": 0.6139213433639671, "positive_rate": 0.4083333333333333, "precision": 0.6666666666666666, "recall": 0.4489795918367347, "roc_auc": 0.7114113250934176, "seed": 34}
SEED_RESULT {"accuracy": 0.65, "baseline_accuracy": 0.5833333333333334, "brier": 0.2160571876589542, "confusion_matrix": [[60, 10], [32, 18]], "f1": 0.46153846153846156, "log_loss": 0.6209381597053584, "positive_rate": 0.4166666666666667, "precision": 0.6428571428571429, "recall": 0.36, "roc_auc": 0.6922857142857143, "seed": 35}
SEED_RESULT {"accuracy": 0.5666666666666667, "baseline_accuracy": 0.44166666666666665, "brier": 0.24835580963772158, "confusion_matrix": [[50, 3], [49, 18]], "f1": 0.4090909090909091, "log_loss": 0.6909192395729455, "positive_rate": 0.5583333333333333, "precision": 0.8571428571428571, "recall": 0.26865671641791045, "roc_auc": 0.6941706561531963, "seed": 36}
SEED_RESULT {"accuracy": 0.6166666666666667, "baseline_accuracy": 0.6166666666666667, "brier": 0.22714919133658862, "confusion_matrix": [[58, 16], [30, 16]], "f1": 0.41025641025641024, "log_loss": 0.6484131192005198, "positive_rate": 0.38333333333333336, "precision": 0.5, "recall": 0.34782608695652173, "roc_auc": 0.6172150411280845, "seed": 37}
SEED_RESULT {"accuracy": 0.55, "baseline_accuracy": 0.55, "brier": 0.24381657975333226, "confusion_matrix": [[45, 21], [33, 21]], "f1": 0.4375, "log_loss": 0.6802330870602431, "positive_rate": 0.45, "precision": 0.5, "recall": 0.3888888888888889, "roc_auc": 0.5833333333333334, "seed": 38}
SEED_RESULT {"accuracy": 0.6416666666666667, "baseline_accuracy": 0.625, "brier": 0.21898676486859933, "confusion_matrix": [[59, 16], [27, 18]], "f1": 0.45569620253164556, "log_loss": 0.6275446932663988, "positive_rate": 0.375, "precision": 0.5294117647058824, "recall": 0.4, "roc_auc": 0.6444444444444444, "seed": 39}
SEED_RESULT {"accuracy": 0.675, "baseline_accuracy": 0.6416666666666667, "brier": 0.2148319791529757, "confusion_matrix": [[55, 22], [17, 26]], "f1": 0.5714285714285714, "log_loss": 0.6190459919118356, "positive_rate": 0.35833333333333334, "precision": 0.5416666666666666, "recall": 0.6046511627906976, "roc_auc": 0.6970703714889761, "seed": 40}
SEED_RESULT {"accuracy": 0.6416666666666667, "baseline_accuracy": 0.5916666666666667, "brier": 0.2312903356260256, "confusion_matrix": [[55, 16], [27, 22]], "f1": 0.5057471264367817, "log_loss": 0.6565204242066413, "positive_rate": 0.4083333333333333, "precision": 0.5789473684210527, "recall": 0.4489795918367347, "roc_auc": 0.6197183098591549, "seed": 41}
SEED_RESULT {"accuracy": 0.6583333333333333, "baseline_accuracy": 0.6083333333333333, "brier": 0.21378241219194172, "confusion_matrix": [[57, 16], [25, 22]], "f1": 0.5176470588235295, "log_loss": 0.6166120538613112, "positive_rate": 0.39166666666666666, "precision": 0.5789473684210527, "recall": 0.46808510638297873, "roc_auc": 0.68230836490819, "seed": 42}
SEED_RESULT {"accuracy": 0.65, "baseline_accuracy": 0.5416666666666666, "brier": 0.22306056682928121, "confusion_matrix": [[50, 15], [27, 28]], "f1": 0.5714285714285714, "log_loss": 0.6370467371815405, "positive_rate": 0.4583333333333333, "precision": 0.6511627906976745, "recall": 0.509090909090909, "roc_auc": 0.6925874125874125, "seed": 43}
SEED_RESULT {"accuracy": 0.6166666666666667, "baseline_accuracy": 0.5583333333333333, "brier": 0.2259404132765864, "confusion_matrix": [[48, 19], [27, 26]], "f1": 0.5306122448979592, "log_loss": 0.6419047894760299, "positive_rate": 0.44166666666666665, "precision": 0.5777777777777777, "recall": 0.49056603773584906, "roc_auc": 0.6603773584905661, "seed": 44}
SEED_RESULT {"accuracy": 0.6916666666666667, "baseline_accuracy": 0.6083333333333333, "brier": 0.2097010804221696, "confusion_matrix": [[61, 12], [25, 22]], "f1": 0.5432098765432098, "log_loss": 0.6109093613869327, "positive_rate": 0.39166666666666666, "precision": 0.6470588235294118, "recall": 0.46808510638297873, "roc_auc": 0.7079568638880793, "seed": 45}
SEED_RESULT {"accuracy": 0.6916666666666667, "baseline_accuracy": 0.5666666666666667, "brier": 0.20868124768400922, "confusion_matrix": [[57, 11], [26, 26]], "f1": 0.5842696629213483, "log_loss": 0.6074250266253309, "positive_rate": 0.43333333333333335, "precision": 0.7027027027027027, "recall": 0.5, "roc_auc": 0.7279411764705882, "seed": 46}
SEED_RESULT {"accuracy": 0.6416666666666667, "baseline_accuracy": 0.5666666666666667, "brier": 0.21869223987488298, "confusion_matrix": [[51, 17], [26, 26]], "f1": 0.5473684210526316, "log_loss": 0.6239205889768422, "positive_rate": 0.43333333333333335, "precision": 0.6046511627906976, "recall": 0.5, "roc_auc": 0.6906108597285068, "seed": 47}
SEED_RESULT {"accuracy": 0.6166666666666667, "baseline_accuracy": 0.5583333333333333, "brier": 0.21820127870612993, "confusion_matrix": [[60, 7], [39, 14]], "f1": 0.3783783783783784, "log_loss": 0.6266796770181184, "positive_rate": 0.44166666666666665, "precision": 0.6666666666666666, "recall": 0.2641509433962264, "roc_auc": 0.7006477048718671, "seed": 48}
SEED_RESULT {"accuracy": 0.6083333333333333, "baseline_accuracy": 0.5416666666666666, "brier": 0.23846347525446673, "confusion_matrix": [[52, 13], [34, 21]], "f1": 0.47191011235955055, "log_loss": 0.6689232114748734, "positive_rate": 0.4583333333333333, "precision": 0.6176470588235294, "recall": 0.38181818181818183, "roc_auc": 0.6671328671328671, "seed": 49}
SEED_RESULT {"accuracy": 0.6166666666666667, "baseline_accuracy": 0.55, "brier": 0.23620964651438872, "confusion_matrix": [[53, 13], [33, 21]], "f1": 0.4772727272727273, "log_loss": 0.6658661029281632, "positive_rate": 0.45, "precision": 0.6176470588235294, "recall": 0.3888888888888889, "roc_auc": 0.6296296296296295, "seed": 50}
SEED_RESULT {"accuracy": 0.65, "baseline_accuracy": 0.5333333333333333, "brier": 0.2208145958975588, "confusion_matrix": [[56, 8], [34, 22]], "f1": 0.5116279069767442, "log_loss": 0.6315582530338385, "positive_rate": 0.4666666666666667, "precision": 0.7333333333333333, "recall": 0.39285714285714285, "roc_auc": 0.6827566964285715, "seed": 51}
SEED_RESULT {"accuracy": 0.6166666666666667, "baseline_accuracy": 0.55, "brier": 0.23349975000394405, "confusion_matrix": [[52, 14], [32, 22]], "f1": 0.4888888888888889, "log_loss": 0.6589263508209547, "positive_rate": 0.45, "precision": 0.6111111111111112, "recall": 0.4074074074074074, "roc_auc": 0.6402918069584737, "seed": 52}
SEED_RESULT {"accuracy": 0.6416666666666667, "baseline_accuracy": 0.5416666666666666, "brier": 0.22768963831624933, "confusion_matrix": [[56, 9], [34, 21]], "f1": 0.49411764705882355, "log_loss": 0.6468620003710387, "positive_rate": 0.4583333333333333, "precision": 0.7, "recall": 0.38181818181818183, "roc_auc": 0.6872727272727273, "seed": 53}
SEED_RESULT {"accuracy": 0.6583333333333333, "baseline_accuracy": 0.6416666666666667, "brier": 0.21603276461879398, "confusion_matrix": [[66, 11], [30, 13]], "f1": 0.3880597014925373, "log_loss": 0.6242370804376064, "positive_rate": 0.35833333333333334, "precision": 0.5416666666666666, "recall": 0.3023255813953488, "roc_auc": 0.6578073089700996, "seed": 54}
SEED_RESULT {"accuracy": 0.625, "baseline_accuracy": 0.6083333333333333, "brier": 0.22651145141061194, "confusion_matrix": [[50, 23], [22, 25]], "f1": 0.5263157894736842, "log_loss": 0.6460537740853439, "positive_rate": 0.39166666666666666, "precision": 0.5208333333333334, "recall": 0.5319148936170213, "roc_auc": 0.652579422908773, "seed": 55}
SEED_RESULT {"accuracy": 0.5916666666666667, "baseline_accuracy": 0.5333333333333333, "brier": 0.22633649104864492, "confusion_matrix": [[42, 22], [27, 29]], "f1": 0.5420560747663551, "log_loss": 0.6435874932098851, "positive_rate": 0.4666666666666667, "precision": 0.5686274509803921, "recall": 0.5178571428571429, "roc_auc": 0.6768973214285715, "seed": 56}
SEED_RESULT {"accuracy": 0.5833333333333334, "baseline_accuracy": 0.5416666666666666, "brier": 0.2465397656445525, "confusion_matrix": [[51, 14], [36, 19]], "f1": 0.4318181818181818, "log_loss": 0.690970024074519, "positive_rate": 0.4583333333333333, "precision": 0.5757575757575758, "recall": 0.34545454545454546, "roc_auc": 0.594965034965035, "seed": 57}
SEED_RESULT {"accuracy": 0.6333333333333333, "baseline_accuracy": 0.6583333333333333, "brier": 0.22683691056140104, "confusion_matrix": [[64, 15], [29, 12]], "f1": 0.35294117647058826, "log_loss": 0.6492446487092548, "positive_rate": 0.3416666666666667, "precision": 0.4444444444444444, "recall": 0.2926829268292683, "roc_auc": 0.6119172584130905, "seed": 58}
SEED_RESULT {"accuracy": 0.5916666666666667, "baseline_accuracy": 0.5083333333333333, "brier": 0.24735149829082886, "confusion_matrix": [[49, 12], [37, 22]], "f1": 0.4731182795698925, "log_loss": 0.6912033191279694, "positive_rate": 0.49166666666666664, "precision": 0.6470588235294118, "recall": 0.3728813559322034, "roc_auc": 0.6415671019727702, "seed": 59}
SEED_RESULT {"accuracy": 0.5416666666666666, "baseline_accuracy": 0.5166666666666667, "brier": 0.23927883418601573, "confusion_matrix": [[49, 13], [42, 16]], "f1": 0.367816091954023, "log_loss": 0.6690510610665854, "positive_rate": 0.48333333333333334, "precision": 0.5517241379310345, "recall": 0.27586206896551724, "roc_auc": 0.6532258064516129, "seed": 60}
SEED_RESULT {"accuracy": 0.6083333333333333, "baseline_accuracy": 0.5083333333333333, "brier": 0.22354040950891715, "confusion_matrix": [[43, 18], [29, 30]], "f1": 0.5607476635514018, "log_loss": 0.637478494487065, "positive_rate": 0.49166666666666664, "precision": 0.625, "recall": 0.5084745762711864, "roc_auc": 0.6904695748819116, "seed": 61}
SEED_RESULT {"accuracy": 0.6166666666666667, "baseline_accuracy": 0.5333333333333333, "brier": 0.22459449483461752, "confusion_matrix": [[46, 18], [28, 28]], "f1": 0.5490196078431373, "log_loss": 0.6400350735761232, "positive_rate": 0.4666666666666667, "precision": 0.6086956521739131, "recall": 0.5, "roc_auc": 0.6738281249999999, "seed": 62}
SEED_RESULT {"accuracy": 0.65, "baseline_accuracy": 0.625, "brier": 0.2209061847238765, "confusion_matrix": [[60, 15], [27, 18]], "f1": 0.46153846153846156, "log_loss": 0.6314881919159162, "positive_rate": 0.375, "precision": 0.5454545454545454, "recall": 0.4, "roc_auc": 0.6394074074074074, "seed": 63}
SEED_RESULT {"accuracy": 0.5916666666666667, "baseline_accuracy": 0.6166666666666667, "brier": 0.22965755109310942, "confusion_matrix": [[44, 30], [19, 27]], "f1": 0.5242718446601942, "log_loss": 0.6481759653503912, "positive_rate": 0.38333333333333336, "precision": 0.47368421052631576, "recall": 0.5869565217391305, "roc_auc": 0.6321974148061105, "seed": 64}
SEED_RESULT {"accuracy": 0.6833333333333333, "baseline_accuracy": 0.625, "brier": 0.19944993971919012, "confusion_matrix": [[61, 14], [24, 21]], "f1": 0.525, "log_loss": 0.581765037552212, "positive_rate": 0.375, "precision": 0.6, "recall": 0.4666666666666667, "roc_auc": 0.7253333333333333, "seed": 65}
SEED_RESULT {"accuracy": 0.7333333333333333, "baseline_accuracy": 0.5833333333333334, "brier": 0.18333076244374966, "confusion_matrix": [[56, 14], [18, 32]], "f1": 0.6666666666666666, "log_loss": 0.5474086678300696, "positive_rate": 0.4166666666666667, "precision": 0.6956521739130435, "recall": 0.64, "roc_auc": 0.7982857142857143, "seed": 66}
SEED_RESULT {"accuracy": 0.6916666666666667, "baseline_accuracy": 0.6, "brier": 0.2133165489850856, "confusion_matrix": [[70, 2], [35, 13]], "f1": 0.4126984126984127, "log_loss": 0.618548297885306, "positive_rate": 0.4, "precision": 0.8666666666666667, "recall": 0.2708333333333333, "roc_auc": 0.6935763888888888, "seed": 67}
SEED_RESULT {"accuracy": 0.7166666666666667, "baseline_accuracy": 0.5416666666666666, "brier": 0.20296257287761163, "confusion_matrix": [[56, 9], [25, 30]], "f1": 0.6382978723404256, "log_loss": 0.5931515783691682, "positive_rate": 0.4583333333333333, "precision": 0.7692307692307693, "recall": 0.5454545454545454, "roc_auc": 0.7552447552447553, "seed": 68}
SEED_RESULT {"accuracy": 0.65, "baseline_accuracy": 0.525, "brier": 0.2183400408792739, "confusion_matrix": [[50, 13], [29, 28]], "f1": 0.5714285714285714, "log_loss": 0.6232330856980783, "positive_rate": 0.475, "precision": 0.6829268292682927, "recall": 0.49122807017543857, "roc_auc": 0.7020328599275968, "seed": 69}
SEED_RESULT {"accuracy": 0.7083333333333334, "baseline_accuracy": 0.5833333333333334, "brier": 0.19990567004395074, "confusion_matrix": [[59, 11], [24, 26]], "f1": 0.5977011494252874, "log_loss": 0.5864420006983728, "positive_rate": 0.4166666666666667, "precision": 0.7027027027027027, "recall": 0.52, "roc_auc": 0.7654285714285715, "seed": 70}
SEED_RESULT {"accuracy": 0.6916666666666667, "baseline_accuracy": 0.6583333333333333, "brier": 0.2100485059510235, "confusion_matrix": [[64, 15], [22, 19]], "f1": 0.5066666666666667, "log_loss": 0.6083952566004527, "positive_rate": 0.3416666666666667, "precision": 0.5588235294117647, "recall": 0.4634146341463415, "roc_auc": 0.6801481938870022, "seed": 71}
SEED_RESULT {"accuracy": 0.6083333333333333, "baseline_accuracy": 0.6, "brier": 0.22358025636147674, "confusion_matrix": [[56, 16], [31, 17]], "f1": 0.41975308641975306, "log_loss": 0.6353675827677514, "positive_rate": 0.4, "precision": 0.5151515151515151, "recall": 0.3541666666666667, "roc_auc": 0.6576967592592593, "seed": 72}
SEED_RESULT {"accuracy": 0.7166666666666667, "baseline_accuracy": 0.6333333333333333, "brier": 0.20058300934335663, "confusion_matrix": [[63, 13], [21, 23]], "f1": 0.575, "log_loss": 0.5894797859646405, "positive_rate": 0.36666666666666664, "precision": 0.6388888888888888, "recall": 0.5227272727272727, "roc_auc": 0.722188995215311, "seed": 73}
SEED_RESULT {"accuracy": 0.6666666666666666, "baseline_accuracy": 0.5583333333333333, "brier": 0.22263947627997674, "confusion_matrix": [[47, 20], [20, 33]], "f1": 0.6226415094339622, "log_loss": 0.638006186195928, "positive_rate": 0.44166666666666665, "precision": 0.6226415094339622, "recall": 0.6226415094339622, "roc_auc": 0.7014925373134329, "seed": 74}
SEED_RESULT {"accuracy": 0.6, "baseline_accuracy": 0.5916666666666667, "brier": 0.23651239595790477, "confusion_matrix": [[57, 14], [34, 15]], "f1": 0.38461538461538464, "log_loss": 0.6658288840537558, "positive_rate": 0.4083333333333333, "precision": 0.5172413793103449, "recall": 0.30612244897959184, "roc_auc": 0.60678355849382, "seed": 75}
SEED_RESULT {"accuracy": 0.675, "baseline_accuracy": 0.6583333333333333, "brier": 0.20266273007659566, "confusion_matrix": [[69, 10], [29, 12]], "f1": 0.38095238095238093, "log_loss": 0.5931906398664915, "positive_rate": 0.3416666666666667, "precision": 0.5454545454545454, "recall": 0.2926829268292683, "roc_auc": 0.6816918802099413, "seed": 76}
SEED_RESULT {"accuracy": 0.6416666666666667, "baseline_accuracy": 0.5166666666666667, "brier": 0.22790784706080908, "confusion_matrix": [[50, 12], [31, 27]], "f1": 0.5567010309278351, "log_loss": 0.6454332529837165, "positive_rate": 0.48333333333333334, "precision": 0.6923076923076923, "recall": 0.46551724137931033, "roc_auc": 0.6626807563959957, "seed": 77}
SEED_RESULT {"accuracy": 0.5916666666666667, "baseline_accuracy": 0.6, "brier": 0.24301443178354273, "confusion_matrix": [[52, 20], [29, 19]], "f1": 0.4367816091954023, "log_loss": 0.6809496094541786, "positive_rate": 0.4, "precision": 0.48717948717948717, "recall": 0.3958333333333333, "roc_auc": 0.5998263888888888, "seed": 78}
SEED_RESULT {"accuracy": 0.6833333333333333, "baseline_accuracy": 0.65, "brier": 0.21524578596558713, "confusion_matrix": [[64, 14], [24, 18]], "f1": 0.4864864864864865, "log_loss": 0.620101082526424, "positive_rate": 0.35, "precision": 0.5625, "recall": 0.42857142857142855, "roc_auc": 0.6364468864468864, "seed": 79}
SEED_RESULT {"accuracy": 0.625, "baseline_accuracy": 0.5333333333333333, "brier": 0.22292397685618826, "confusion_matrix": [[58, 6], [39, 17]], "f1": 0.43037974683544306, "log_loss": 0.6371501988973677, "positive_rate": 0.4666666666666667, "precision": 0.7391304347826086, "recall": 0.30357142857142855, "roc_auc": 0.7170758928571429, "seed": 80}
SEED_RESULT {"accuracy": 0.575, "baseline_accuracy": 0.5666666666666667, "brier": 0.24953464362604721, "confusion_matrix": [[49, 19], [32, 20]], "f1": 0.43956043956043955, "log_loss": 0.6938737025030889, "positive_rate": 0.43333333333333335, "precision": 0.5128205128205128, "recall": 0.38461538461538464, "roc_auc": 0.5610859728506787, "seed": 81}
SEED_RESULT {"accuracy": 0.6166666666666667, "baseline_accuracy": 0.6, "brier": 0.23400363350881964, "confusion_matrix": [[50, 22], [24, 24]], "f1": 0.5106382978723404, "log_loss": 0.6597891863258777, "positive_rate": 0.4, "precision": 0.5217391304347826, "recall": 0.5, "roc_auc": 0.6197916666666666, "seed": 82}
SEED_RESULT {"accuracy": 0.6166666666666667, "baseline_accuracy": 0.5416666666666666, "brier": 0.2278343871934948, "confusion_matrix": [[54, 11], [35, 20]], "f1": 0.46511627906976744, "log_loss": 0.6458154380241669, "positive_rate": 0.4583333333333333, "precision": 0.6451612903225806, "recall": 0.36363636363636365, "roc_auc": 0.6455944055944056, "seed": 83}
SEED_RESULT {"accuracy": 0.6833333333333333, "baseline_accuracy": 0.6083333333333333, "brier": 0.2035738012310495, "confusion_matrix": [[57, 16], [22, 25]], "f1": 0.5681818181818182, "log_loss": 0.5934329915288593, "positive_rate": 0.39166666666666666, "precision": 0.6097560975609756, "recall": 0.5319148936170213, "roc_auc": 0.7301078402798017, "seed": 84}
SEED_RESULT {"accuracy": 0.7333333333333333, "baseline_accuracy": 0.6666666666666666, "brier": 0.20569669114443545, "confusion_matrix": [[68, 12], [20, 20]], "f1": 0.5555555555555556, "log_loss": 0.6056034669510268, "positive_rate": 0.3333333333333333, "precision": 0.625, "recall": 0.5, "roc_auc": 0.6931249999999999, "seed": 85}
SEED_RESULT {"accuracy": 0.675, "baseline_accuracy": 0.65, "brier": 0.20833268351045214, "confusion_matrix": [[66, 12], [27, 15]], "f1": 0.43478260869565216, "log_loss": 0.6020688478873027, "positive_rate": 0.35, "precision": 0.5555555555555556, "recall": 0.35714285714285715, "roc_auc": 0.6746031746031746, "seed": 86}
SEED_RESULT {"accuracy": 0.5916666666666667, "baseline_accuracy": 0.4583333333333333, "brier": 0.23200067249240444, "confusion_matrix": [[50, 5], [44, 21]], "f1": 0.46153846153846156, "log_loss": 0.654884767190002, "positive_rate": 0.5416666666666666, "precision": 0.8076923076923077, "recall": 0.3230769230769231, "roc_auc": 0.7194405594405595, "seed": 87}
SEED_RESULT {"accuracy": 0.65, "baseline_accuracy": 0.6166666666666667, "brier": 0.21853802566985217, "confusion_matrix": [[60, 14], [28, 18]], "f1": 0.46153846153846156, "log_loss": 0.628580616058157, "positive_rate": 0.38333333333333336, "precision": 0.5625, "recall": 0.391304347826087, "roc_auc": 0.6648061104582843, "seed": 88}
SEED_RESULT {"accuracy": 0.6166666666666667, "baseline_accuracy": 0.6333333333333333, "brier": 0.2252433556029683, "confusion_matrix": [[55, 21], [25, 19]], "f1": 0.4523809523809524, "log_loss": 0.6426228186976066, "positive_rate": 0.36666666666666664, "precision": 0.475, "recall": 0.4318181818181818, "roc_auc": 0.6447368421052632, "seed": 89}
SEED_RESULT {"accuracy": 0.7, "baseline_accuracy": 0.6, "brier": 0.17844996430976157, "confusion_matrix": [[60, 12], [24, 24]], "f1": 0.5714285714285714, "log_loss": 0.5358912639038206, "positive_rate": 0.4, "precision": 0.6666666666666666, "recall": 0.5, "roc_auc": 0.8061342592592593, "seed": 90}
SEED_RESULT {"accuracy": 0.6416666666666667, "baseline_accuracy": 0.55, "brier": 0.22548935957213861, "confusion_matrix": [[59, 7], [36, 18]], "f1": 0.45569620253164556, "log_loss": 0.6419545228889246, "positive_rate": 0.45, "precision": 0.72, "recall": 0.3333333333333333, "roc_auc": 0.6835016835016835, "seed": 91}
SEED_RESULT {"accuracy": 0.5833333333333334, "baseline_accuracy": 0.5916666666666667, "brier": 0.2402650575555393, "confusion_matrix": [[51, 20], [30, 19]], "f1": 0.4318181818181818, "log_loss": 0.6763491292362123, "positive_rate": 0.4083333333333333, "precision": 0.48717948717948717, "recall": 0.3877551020408163, "roc_auc": 0.6148318482322506, "seed": 92}
SEED_RESULT {"accuracy": 0.6333333333333333, "baseline_accuracy": 0.575, "brier": 0.23285868451694036, "confusion_matrix": [[57, 12], [32, 19]], "f1": 0.4634146341463415, "log_loss": 0.6585851947067106, "positive_rate": 0.425, "precision": 0.6129032258064516, "recall": 0.37254901960784315, "roc_auc": 0.6268826371128161, "seed": 93}
SEED_RESULT {"accuracy": 0.625, "baseline_accuracy": 0.5416666666666666, "brier": 0.21441300097549568, "confusion_matrix": [[54, 11], [34, 21]], "f1": 0.4827586206896552, "log_loss": 0.6197291879790112, "positive_rate": 0.4583333333333333, "precision": 0.65625, "recall": 0.38181818181818183, "roc_auc": 0.7292307692307691, "seed": 94}
SEED_RESULT {"accuracy": 0.6833333333333333, "baseline_accuracy": 0.575, "brier": 0.2022600070887744, "confusion_matrix": [[56, 13], [25, 26]], "f1": 0.5777777777777777, "log_loss": 0.5901678278219613, "positive_rate": 0.425, "precision": 0.6666666666666666, "recall": 0.5098039215686274, "roc_auc": 0.7317419721511792, "seed": 95}
SEED_RESULT {"accuracy": 0.6333333333333333, "baseline_accuracy": 0.525, "brier": 0.22780524353332554, "confusion_matrix": [[46, 17], [27, 30]], "f1": 0.5769230769230769, "log_loss": 0.6450120453663348, "positive_rate": 0.475, "precision": 0.6382978723404256, "recall": 0.5263157894736842, "roc_auc": 0.6819827346143136, "seed": 96}
SEED_RESULT {"accuracy": 0.575, "baseline_accuracy": 0.5333333333333333, "brier": 0.23520574485401433, "confusion_matrix": [[56, 8], [43, 13]], "f1": 0.33766233766233766, "log_loss": 0.66157518856146, "positive_rate": 0.4666666666666667, "precision": 0.6190476190476191, "recall": 0.23214285714285715, "roc_auc": 0.6785714285714286, "seed": 97}
SEED_RESULT {"accuracy": 0.6416666666666667, "baseline_accuracy": 0.525, "brier": 0.21921680704797894, "confusion_matrix": [[52, 11], [32, 25]], "f1": 0.5376344086021505, "log_loss": 0.6270089503263097, "positive_rate": 0.475, "precision": 0.6944444444444444, "recall": 0.43859649122807015, "roc_auc": 0.7257031467557784, "seed": 98}
SEED_RESULT {"accuracy": 0.6916666666666667, "baseline_accuracy": 0.6, "brier": 0.20918610300000642, "confusion_matrix": [[60, 12], [25, 23]], "f1": 0.5542168674698795, "log_loss": 0.6051508501445515, "positive_rate": 0.4, "precision": 0.6571428571428571, "recall": 0.4791666666666667, "roc_auc": 0.7126736111111112, "seed": 99}
TEST_SUMMARY {"tests_run": 111, "failures": 0, "errors": 0, "skipped": 0, "successful": true}
```

**stderr** — [file TXT](streams/001_unittest_project_suite.stderr.txt)

```text
test_all_negative_and_single_class (test_p074.ChurnContracts.test_all_negative_and_single_class) ... ok
test_determinism (test_p074.ChurnContracts.test_determinism) ... ok
test_hand_calculated_metrics (test_p074.ChurnContracts.test_hand_calculated_metrics) ... ok
test_invalid_generator_and_split (test_p074.ChurnContracts.test_invalid_generator_and_split) ... ok
test_invalid_labels (test_p074.ChurnContracts.test_invalid_labels) ... ok
test_invalid_probability_and_threshold (test_p074.ChurnContracts.test_invalid_probability_and_threshold) ... ok
test_invalid_training_X (test_p074.ChurnContracts.test_invalid_training_X) ... ok
test_predict_does_not_change_scaler (test_p074.ChurnContracts.test_predict_does_not_change_scaler) ... ok
test_threshold_includes_equality (test_p074.ChurnContracts.test_threshold_includes_equality) ... ok
test_training_learns_generator_direction_and_weights (test_p074.ChurnContracts.test_training_learns_generator_direction_and_weights) ... ok
test_training_preprocessor_never_receives_test (test_p074.ChurnContracts.test_training_preprocessor_never_receives_test) ... ok
test_seed_000 (test_p074.SeededOracleChecks.test_seed_000) ... ok
test_seed_001 (test_p074.SeededOracleChecks.test_seed_001) ... ok
test_seed_002 (test_p074.SeededOracleChecks.test_seed_002) ... ok
test_seed_003 (test_p074.SeededOracleChecks.test_seed_003) ... ok
test_seed_004 (test_p074.SeededOracleChecks.test_seed_004) ... ok
test_seed_005 (test_p074.SeededOracleChecks.test_seed_005) ... ok
test_seed_006 (test_p074.SeededOracleChecks.test_seed_006) ... ok
test_seed_007 (test_p074.SeededOracleChecks.test_seed_007) ... ok
test_seed_008 (test_p074.SeededOracleChecks.test_seed_008) ... ok
test_seed_009 (test_p074.SeededOracleChecks.test_seed_009) ... ok
test_seed_010 (test_p074.SeededOracleChecks.test_seed_010) ... ok
test_seed_011 (test_p074.SeededOracleChecks.test_seed_011) ... ok
test_seed_012 (test_p074.SeededOracleChecks.test_seed_012) ... ok
test_seed_013 (test_p074.SeededOracleChecks.test_seed_013) ... ok
test_seed_014 (test_p074.SeededOracleChecks.test_seed_014) ... ok
test_seed_015 (test_p074.SeededOracleChecks.test_seed_015) ... ok
test_seed_016 (test_p074.SeededOracleChecks.test_seed_016) ... ok
test_seed_017 (test_p074.SeededOracleChecks.test_seed_017) ... ok
test_seed_018 (test_p074.SeededOracleChecks.test_seed_018) ... ok
test_seed_019 (test_p074.SeededOracleChecks.test_seed_019) ... ok
test_seed_020 (test_p074.SeededOracleChecks.test_seed_020) ... ok
test_seed_021 (test_p074.SeededOracleChecks.test_seed_021) ... ok
test_seed_022 (test_p074.SeededOracleChecks.test_seed_022) ... ok
test_seed_023 (test_p074.SeededOracleChecks.test_seed_023) ... ok
test_seed_024 (test_p074.SeededOracleChecks.test_seed_024) ... ok
test_seed_025 (test_p074.SeededOracleChecks.test_seed_025) ... ok
test_seed_026 (test_p074.SeededOracleChecks.test_seed_026) ... ok
test_seed_027 (test_p074.SeededOracleChecks.test_seed_027) ... ok
test_seed_028 (test_p074.SeededOracleChecks.test_seed_028) ... ok
test_seed_029 (test_p074.SeededOracleChecks.test_seed_029) ... ok
test_seed_030 (test_p074.SeededOracleChecks.test_seed_030) ... ok
test_seed_031 (test_p074.SeededOracleChecks.test_seed_031) ... ok
test_seed_032 (test_p074.SeededOracleChecks.test_seed_032) ... ok
test_seed_033 (test_p074.SeededOracleChecks.test_seed_033) ... ok
test_seed_034 (test_p074.SeededOracleChecks.test_seed_034) ... ok
test_seed_035 (test_p074.SeededOracleChecks.test_seed_035) ... ok
test_seed_036 (test_p074.SeededOracleChecks.test_seed_036) ... ok
test_seed_037 (test_p074.SeededOracleChecks.test_seed_037) ... ok
test_seed_038 (test_p074.SeededOracleChecks.test_seed_038) ... ok
test_seed_039 (test_p074.SeededOracleChecks.test_seed_039) ... ok
test_seed_040 (test_p074.SeededOracleChecks.test_seed_040) ... ok
test_seed_041 (test_p074.SeededOracleChecks.test_seed_041) ... ok
test_seed_042 (test_p074.SeededOracleChecks.test_seed_042) ... ok
test_seed_043 (test_p074.SeededOracleChecks.test_seed_043) ... ok
test_seed_044 (test_p074.SeededOracleChecks.test_seed_044) ... ok
test_seed_045 (test_p074.SeededOracleChecks.test_seed_045) ... ok
test_seed_046 (test_p074.SeededOracleChecks.test_seed_046) ... ok
test_seed_047 (test_p074.SeededOracleChecks.test_seed_047) ... ok
test_seed_048 (test_p074.SeededOracleChecks.test_seed_048) ... ok
test_seed_049 (test_p074.SeededOracleChecks.test_seed_049) ... ok
test_seed_050 (test_p074.SeededOracleChecks.test_seed_050) ... ok
test_seed_051 (test_p074.SeededOracleChecks.test_seed_051) ... ok
test_seed_052 (test_p074.SeededOracleChecks.test_seed_052) ... ok
test_seed_053 (test_p074.SeededOracleChecks.test_seed_053) ... ok
test_seed_054 (test_p074.SeededOracleChecks.test_seed_054) ... ok
test_seed_055 (test_p074.SeededOracleChecks.test_seed_055) ... ok
test_seed_056 (test_p074.SeededOracleChecks.test_seed_056) ... ok
test_seed_057 (test_p074.SeededOracleChecks.test_seed_057) ... ok
test_seed_058 (test_p074.SeededOracleChecks.test_seed_058) ... ok
test_seed_059 (test_p074.SeededOracleChecks.test_seed_059) ... ok
test_seed_060 (test_p074.SeededOracleChecks.test_seed_060) ... ok
test_seed_061 (test_p074.SeededOracleChecks.test_seed_061) ... ok
test_seed_062 (test_p074.SeededOracleChecks.test_seed_062) ... ok
test_seed_063 (test_p074.SeededOracleChecks.test_seed_063) ... ok
test_seed_064 (test_p074.SeededOracleChecks.test_seed_064) ... ok
test_seed_065 (test_p074.SeededOracleChecks.test_seed_065) ... ok
test_seed_066 (test_p074.SeededOracleChecks.test_seed_066) ... ok
test_seed_067 (test_p074.SeededOracleChecks.test_seed_067) ... ok
test_seed_068 (test_p074.SeededOracleChecks.test_seed_068) ... ok
test_seed_069 (test_p074.SeededOracleChecks.test_seed_069) ... ok
test_seed_070 (test_p074.SeededOracleChecks.test_seed_070) ... ok
test_seed_071 (test_p074.SeededOracleChecks.test_seed_071) ... ok
test_seed_072 (test_p074.SeededOracleChecks.test_seed_072) ... ok
test_seed_073 (test_p074.SeededOracleChecks.test_seed_073) ... ok
test_seed_074 (test_p074.SeededOracleChecks.test_seed_074) ... ok
test_seed_075 (test_p074.SeededOracleChecks.test_seed_075) ... ok
test_seed_076 (test_p074.SeededOracleChecks.test_seed_076) ... ok
test_seed_077 (test_p074.SeededOracleChecks.test_seed_077) ... ok
test_seed_078 (test_p074.SeededOracleChecks.test_seed_078) ... ok
test_seed_079 (test_p074.SeededOracleChecks.test_seed_079) ... ok
test_seed_080 (test_p074.SeededOracleChecks.test_seed_080) ... ok
test_seed_081 (test_p074.SeededOracleChecks.test_seed_081) ... ok
test_seed_082 (test_p074.SeededOracleChecks.test_seed_082) ... ok
test_seed_083 (test_p074.SeededOracleChecks.test_seed_083) ... ok
test_seed_084 (test_p074.SeededOracleChecks.test_seed_084) ... ok
test_seed_085 (test_p074.SeededOracleChecks.test_seed_085) ... ok
test_seed_086 (test_p074.SeededOracleChecks.test_seed_086) ... ok
test_seed_087 (test_p074.SeededOracleChecks.test_seed_087) ... ok
test_seed_088 (test_p074.SeededOracleChecks.test_seed_088) ... ok
test_seed_089 (test_p074.SeededOracleChecks.test_seed_089) ... ok
test_seed_090 (test_p074.SeededOracleChecks.test_seed_090) ... ok
test_seed_091 (test_p074.SeededOracleChecks.test_seed_091) ... ok
test_seed_092 (test_p074.SeededOracleChecks.test_seed_092) ... ok
test_seed_093 (test_p074.SeededOracleChecks.test_seed_093) ... ok
test_seed_094 (test_p074.SeededOracleChecks.test_seed_094) ... ok
test_seed_095 (test_p074.SeededOracleChecks.test_seed_095) ... ok
test_seed_096 (test_p074.SeededOracleChecks.test_seed_096) ... ok
test_seed_097 (test_p074.SeededOracleChecks.test_seed_097) ... ok
test_seed_098 (test_p074.SeededOracleChecks.test_seed_098) ... ok
test_seed_099 (test_p074.SeededOracleChecks.test_seed_099) ... ok

----------------------------------------------------------------------
Ran 111 tests in 0.756s

OK
```

## Demo — processi separati dalle suite

Questi output provengono dalle demo eseguite dal runner. Non costituiscono nuovi metodi unittest.

### 002 · demo_churn

Comando registrato (array degli argomenti; segnaposto dei metadati documentati nel manifest):

```json
["<PYTHON_HOME>/bin/python", "-B", "src/churn.py"]
```

Esito: **PASS** · codice di uscita: `0`.

**stdout** — [file TXT](streams/002_demo_churn.stdout.txt)

```text
P074 — 380 esempi di training; 120 esempi di test sintetici; soglia 0.5
accuracy: 0.691667
precision: 0.642857
recall: 0.551020
f1: 0.593407
brier: 0.211239
log_loss: 0.611370
roc_auc: 0.706812
matrice [[TN, FP], [FN, TP]]: [[56, 15], [22, 27]]
baseline_accuracy: 0.591667
baseline_brier: 0.243800
prima probabilità: 0.543264 etichetta: 0
```

**stderr** — [file TXT](streams/002_demo_churn.stderr.txt)

Il processo non ha emesso byte su stderr. Il file collegato è vuoto (0 byte).

### 003 · demo_examples

Comando registrato (array degli argomenti; segnaposto dei metadati documentati nel manifest):

```json
["<PYTHON_HOME>/bin/python", "-B", "examples.py"]
```

Esito: **PASS** · codice di uscita: `0`.

**stdout** — [file TXT](streams/003_demo_examples.stdout.txt)

```text
primo_caso: {"id": 380, "probabilita": 0.5432642500772994, "vero": 0, "predetto": 1}
soglia: 0.3 {"accuracy": 0.5333333333333333, "precision": 0.4666666666666667, "recall": 1.0, "f1": 0.6363636363636364, "positive_rate": 0.4083333333333333, "brier": 0.21123896147258148, "log_loss": 0.611369609617441, "roc_auc": 0.706812302385743, "confusion_matrix": [[15, 56], [0, 49]]}
soglia: 0.5 {"accuracy": 0.6916666666666667, "precision": 0.6428571428571429, "recall": 0.5510204081632653, "f1": 0.5934065934065934, "positive_rate": 0.4083333333333333, "brier": 0.21123896147258148, "log_loss": 0.611369609617441, "roc_auc": 0.706812302385743, "confusion_matrix": [[56, 15], [22, 27]]}
soglia: 0.7 {"accuracy": 0.6333333333333333, "precision": 0.7272727272727273, "recall": 0.16326530612244897, "f1": 0.26666666666666666, "positive_rate": 0.4083333333333333, "brier": 0.21123896147258148, "log_loss": 0.611369609617441, "roc_auc": 0.706812302385743, "confusion_matrix": [[68, 3], [41, 8]]}
uguaglianza_0_5: [[0, 0], [0, 1]]
esercizio: {"accuracy": 0.5, "precision": 0.5, "recall": 0.5, "f1": 0.5, "positive_rate": 0.5, "brier": 0.21749999999999997, "log_loss": 0.5827461418789359, "roc_auc": 0.75, "confusion_matrix": [[1, 1], [1, 1]]}
```

**stderr** — [file TXT](streams/003_demo_examples.stderr.txt)

Il processo non ha emesso byte su stderr. Il file collegato è vuoto (0 byte).

## Controlli runtime

Il record di questo progetto non contiene controlli classificati come `runtime_check`. L’assenza non aggiunge una verifica runtime alle suite del progetto.

## Verifica e provenienza

[Registro strutturato](registro.json) · [Hash e trasformazioni](MANIFEST.json) · [Policy](../AUDIT.md) · [Indice](../README.md)
