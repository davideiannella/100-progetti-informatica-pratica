import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))
import json
import churn as m
r = m.run_experiment()
print("primo_caso:", json.dumps({"id": r["test_ids"][0], "probabilita": r["probability"][0], "vero": r["y_true"][0], "predetto": r["prediction"][0]}))
for threshold in [0.3,0.5,0.7]:
    print("soglia:", threshold, json.dumps(m.classification_metrics(r["y_true"],r["probability"],threshold),ensure_ascii=False))
print("uguaglianza_0_5:", m.classification_metrics([1],[0.5])["confusion_matrix"])
print("esercizio:", json.dumps(m.classification_metrics([0,0,1,1],[0.1,0.7,0.4,0.9]),ensure_ascii=False))
