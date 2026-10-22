import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))
import json
import anomaly as m
r = m.run_experiment()
print("primo_caso:", json.dumps({"id": r["test_ids"][0], "X": r["X_test"][0], "vero": r["y_true"][0], "predetto": r["prediction"][0], "decision_function": r["decision_function"][0], "anomaly_score": r["anomaly_score"][0]}))
s = m.make_splits()
for contamination in [0.01,0.07,0.15]:
    model = m.train_model(s["X_train"], contamination=contamination)
    prediction = m.predict(model,s["X_test"])
    print("contamination:", contamination, json.dumps(m.detection_metrics(s["y_test"],prediction,-model.score_samples(s["X_test"])),ensure_ascii=False))
print("esercizio:", json.dumps(m.detection_metrics([0,0,0,1,1],[0,1,0,1,0]),ensure_ascii=False))
