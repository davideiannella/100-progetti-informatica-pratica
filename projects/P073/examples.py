import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))
import json
import energy_regression as m
r = m.run_experiment()
print("prima_riga_test:", json.dumps({"id": r["test_ids"][0], "X": r["X_test"][0], "vero": r["y_true"][0], "previsto": r["y_pred"][0], "baseline": r["baseline_predictions"][0]}, ensure_ascii=False))
print("temperature_simmetriche:", m.design_matrix([[10,1,12],[30,1,12]]).tolist())
print("metriche_manuali:", m.regression_metrics([1,3,5], [2,3,3]))
X, y = m.make_data(n=400, noise=0)
model = m.train_model(X[:300], y[:300])
print("senza_rumore:", json.dumps({"intercetta": float(model.intercept_), "coefficienti": model.coef_.tolist(), "metriche_test": m.regression_metrics(y[300:], m.predict(model, X[300:]))}))
print("esercizio:", m.regression_metrics([10,12,14],[12,12,12]))
