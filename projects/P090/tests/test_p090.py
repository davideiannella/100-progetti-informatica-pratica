from pathlib import Path
import sys
import unittest
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from maintenance_ml import (features, generate_signal, build_signals, experiment,
                            SAMPLE_RATE_HZ, WINDOW_SAMPLES)


class MaintenanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = experiment()
        cls.signals, cls.y = build_signals()
        cls.X = np.stack([features(signal) for signal in cls.signals])

    def test_zero_signal(self):
        np.testing.assert_array_equal(features(np.zeros(256)), np.zeros(4))

    def test_constant_signal_has_no_ac_component(self):
        np.testing.assert_allclose(features(np.full(256, 2.0)), [2, 2, 1, 0])

    def test_sine_rms_and_frequency_ratio(self):
        t = np.arange(256) / 256
        low = features(np.sin(2 * np.pi * 16 * t))
        high = features(np.sin(2 * np.pi * 64 * t))
        self.assertAlmostEqual(low[0], 1 / np.sqrt(2))
        self.assertAlmostEqual(low[2], np.sqrt(2))
        self.assertAlmostEqual(low[3], 0)
        self.assertAlmostEqual(high[3], 1)

    def test_frequency_cutoff_includes_40_hz(self):
        t = np.arange(256) / 256
        self.assertAlmostEqual(features(np.sin(2 * np.pi * 40 * t))[3], 1)
        self.assertAlmostEqual(features(np.sin(2 * np.pi * 39 * t))[3], 0)

    def test_odd_length_spectral_weights(self):
        n = 255
        t = np.arange(n) / 255
        self.assertAlmostEqual(features(np.sin(2 * np.pi * 60 * t), 255)[3], 1)

    def test_large_finite_amplitudes_do_not_overflow(self):
        f = features(np.full(256, 1e300))
        self.assertTrue(np.isfinite(f).all())
        self.assertEqual(f[0], 1e300)
        self.assertEqual(f[3], 0)
        with self.assertRaises(ValueError):
            features([float.fromhex("0x0.0000000000001p-1022")] + [0] * 255)

    def test_feature_constraints_on_generated_signals(self):
        self.assertEqual(self.X.shape, (240, 4))
        self.assertTrue(np.isfinite(self.X).all())
        self.assertTrue((self.X[:, 0] <= self.X[:, 1]).all())
        self.assertTrue((self.X[:, 2] >= 1).all())
        self.assertTrue(((self.X[:, 3] >= 0) & (self.X[:, 3] <= 1)).all())

    def test_invalid_signal_shapes_and_types(self):
        for signal in (None, 1.0, [], [1] * 7, [[1] * 8], [True] * 8, [True] + [0] * 255,
                       [np.bool_(False)] + [1.0] * 255,
                       ["1"] * 8, [complex(1, 1)] * 8, [[1], [1, 2]]):
            with self.subTest(signal=type(signal).__name__), self.assertRaises(ValueError):
                features(signal)

    def test_nonfinite_signal_values(self):
        for value in (float("nan"), float("inf"), -float("inf")):
            with self.subTest(value=value), self.assertRaises(ValueError):
                features([0] * 7 + [value])

    def test_invalid_sample_rates(self):
        for rate in (0, 80, -1, True, "256", None, float("nan"), float("inf"), 10**1000):
            with self.subTest(rate=type(rate).__name__), self.assertRaises(ValueError):
                features([1] * 8, rate)

    def test_generator_seed_is_reproducible(self):
        a = generate_signal(1, np.random.default_rng(0))
        b = generate_signal(1, np.random.default_rng(0))
        c = generate_signal(1, np.random.default_rng(1))
        np.testing.assert_array_equal(a, b)
        self.assertFalse(np.array_equal(a, c))
        self.assertEqual(len(a), WINDOW_SAMPLES)
        self.assertEqual(WINDOW_SAMPLES / SAMPLE_RATE_HZ, 1)

    def test_generator_rejects_invalid_label_and_rng(self):
        for label in (-1, 2, True, 0.0, "0", None):
            with self.subTest(label=label), self.assertRaises(ValueError):
                generate_signal(label, np.random.default_rng(0))
        with self.assertRaises(ValueError):
            generate_signal(0, 9)

    def test_invalid_seeds(self):
        for seed in (-1, 2**32, True, 9.0, "9", None, float("nan")):
            with self.subTest(seed=seed), self.assertRaises(ValueError):
                build_signals(seed)

    def test_split_is_disjoint_and_stratified(self):
        r = self.result
        train, test = set(r["train_indices"]), set(r["test_indices"])
        self.assertFalse(train & test)
        self.assertEqual(train | test, set(range(240)))
        self.assertEqual(r["train_class_counts"], [135, 45])
        self.assertEqual(r["test_class_counts"], [45, 15])
        self.assertEqual(len(set(r["signal_sha256"])), 240)
        hashes = r["signal_sha256"]
        self.assertFalse({hashes[i] for i in train} & {hashes[i] for i in test})

    def test_scaler_is_fitted_only_on_training(self):
        train = self.result["train_indices"]
        scaler = self.result["model"].named_steps["standardscaler"]
        np.testing.assert_allclose(scaler.mean_, self.X[train].mean(axis=0), rtol=1e-13)
        self.assertEqual(scaler.n_samples_seen_, 180)
        self.assertFalse(np.allclose(scaler.mean_, self.X.mean(axis=0), rtol=1e-8, atol=0))

    def test_confusion_matrix_reconstructs_metrics(self):
        r = self.result
        (tn, fp), (fn, tp) = r["confusion_matrix"]
        self.assertEqual(tn + fp + fn + tp, 60)
        self.assertAlmostEqual(r["precision"], tp / (tp + fp))
        self.assertAlmostEqual(r["recall"], tp / (tp + fn))
        self.assertAlmostEqual(r["f1"], 2 * tp / (2 * tp + fp + fn))
        self.assertAlmostEqual(r["accuracy"], (tn + tp) / 60)

    def test_baseline_and_missed_anomalies_are_visible(self):
        r = self.result
        self.assertEqual(r["baseline"]["accuracy"], 0.75)
        self.assertEqual(r["baseline"]["f1"], 0)
        self.assertGreater(r["f1"], r["baseline"]["f1"])
        self.assertGreater(r["confusion_matrix"][1][0], 0)
        self.assertGreater(r["confusion_matrix"][0][1], 0)

    def test_experiment_is_reproducible(self):
        second = experiment()
        self.assertEqual({k: v for k, v in self.result.items() if k != "model"},
                         {k: v for k, v in second.items() if k != "model"})

    def test_invalid_attention_threshold(self):
        for threshold in (0, -1, 1.1, True, "0.5", None, float("nan"), float("inf"), 10**1000):
            with self.subTest(threshold=type(threshold).__name__), self.assertRaises(ValueError):
                experiment(attention_threshold=threshold)


if __name__ == "__main__":
    unittest.main()
