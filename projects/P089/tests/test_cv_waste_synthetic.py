from pathlib import Path
import sys
import unittest
from unittest.mock import patch
import numpy as np
from PIL import Image
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from cv_waste_synthetic import (CLASSES, FEATURE_NAMES, synthetic_image, features,
                                build_dataset, train_evaluate, classify_probabilities)
from sklearn.ensemble import RandomForestClassifier


class SyntheticCVTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fit_inputs = []
        original_fit = RandomForestClassifier.fit
        def recording_fit(model, X, y, *args, **kwargs):
            cls.fit_inputs.append((X.copy(), y.copy()))
            return original_fit(model, X, y, *args, **kwargs)
        with patch.object(RandomForestClassifier, "fit", recording_fit):
            cls.result = train_evaluate()
        cls.X, cls.y = build_dataset()

    def test_all_classes_generate_rgb_images(self):
        rng = np.random.default_rng(1)
        for label in CLASSES:
            with self.subTest(label=label):
                image = synthetic_image(label, rng)
                self.assertEqual((image.size, image.mode), ((64, 64), "RGB"))

    def test_generation_is_deterministic(self):
        a = synthetic_image("carta", np.random.default_rng(5))
        b = synthetic_image("carta", np.random.default_rng(5))
        c = synthetic_image("carta", np.random.default_rng(6))
        self.assertEqual(a.tobytes(), b.tobytes())
        self.assertNotEqual(a.tobytes(), c.tobytes())

    def test_generator_rejects_unknown_class_and_rng(self):
        for label in ("organico", "", None, True, []):
            with self.subTest(label=label), self.assertRaises(ValueError):
                synthetic_image(label, np.random.default_rng(1))
        with self.assertRaises(ValueError):
            synthetic_image("carta", 123)

    def test_image_size_constraints(self):
        self.assertEqual(synthetic_image("vetro", np.random.default_rng(1), 256).size, (256, 256))
        for size in (0, 63, 257, True, 64.0, float("nan"), "64"):
            with self.subTest(size=size), self.assertRaises(ValueError):
                synthetic_image("vetro", np.random.default_rng(1), size)

    def test_features_have_known_order_and_dimension(self):
        f = features(Image.new("RGB", (4, 4), (255, 0, 0)))
        self.assertEqual(len(FEATURE_NAMES), 14)
        np.testing.assert_allclose(f, [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0])

    def test_features_are_finite_and_bounded(self):
        self.assertEqual(self.X.shape, (320, 14))
        self.assertTrue(np.isfinite(self.X).all())
        self.assertTrue(((self.X >= 0) & (self.X <= 1)).all())

    def test_features_reject_unsupported_images(self):
        for image in (None, np.zeros((64, 64, 3)), Image.new("L", (4, 4)), Image.new("RGB", (1, 64))):
            with self.subTest(image=type(image).__name__), self.assertRaises(ValueError):
                features(image)

    def test_dataset_count_seed_and_bounds(self):
        X, y = build_dataset(samples_per_class=1, seed=0)
        self.assertEqual((X.shape, len(y)), ((4, 14), 4))
        for value in (0, -1, True, 1.5, float("nan"), 1001, "4"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                build_dataset(samples_per_class=value)
        for seed in (-1, 2**32, True, float("nan"), "1"):
            with self.subTest(seed=seed), self.assertRaises(ValueError):
                build_dataset(seed=seed)

    def test_training_requires_enough_samples_for_stratification(self):
        for count in (1, 2, 3):
            with self.subTest(count=count), self.assertRaises(ValueError):
                train_evaluate(samples_per_class=count)

    def test_split_is_disjoint_complete_and_balanced(self):
        train, test = self.result["train_indices"], self.result["test_indices"]
        self.assertEqual((len(train), len(test)), (240, 80))
        self.assertFalse(set(train) & set(test))
        self.assertEqual(set(train) | set(test), set(range(320)))
        for label in CLASSES:
            self.assertEqual(int((self.y[train] == label).sum()), 60)
            self.assertEqual(int((self.y[test] == label).sum()), 20)
        self.assertEqual(len({row.tobytes() for row in self.X}), 320)

    def test_fit_receives_only_training_rows(self):
        self.assertEqual(len(self.fit_inputs), 1)
        X, y = self.fit_inputs[0]
        train = self.result["train_indices"]
        np.testing.assert_array_equal(X, self.X[train])
        np.testing.assert_array_equal(y, self.y[train])

    def test_metrics_match_confusion_matrix_and_baseline(self):
        r = self.result
        cm = np.asarray(r["confusion_matrix"])
        self.assertEqual(cm.sum(), 80)
        self.assertAlmostEqual(r["accuracy"], np.trace(cm) / cm.sum())
        self.assertEqual(r["baseline"]["class"], "carta")
        self.assertEqual(r["baseline"]["accuracy"], 0.25)
        self.assertAlmostEqual(r["baseline"]["f1_macro"], 0.1)
        self.assertGreater(r["f1_macro"], r["baseline"]["f1_macro"])

    def test_pipeline_is_reproducible(self):
        second = train_evaluate()
        self.assertEqual({k: v for k, v in self.result.items() if k != "model"},
                         {k: v for k, v in second.items() if k != "model"})

    def test_review_threshold_is_inclusive(self):
        at = classify_probabilities([0.75, 0.25, 0, 0])
        below = classify_probabilities([0.749, 0.251, 0, 0])
        self.assertEqual((at["label"], at["decision"]), ("carta", "automatico"))
        self.assertEqual(below["decision"], "revisione")
        self.assertEqual(classify_probabilities([0.25] * 4)["decision"], "revisione")

    def test_probability_labels_and_ties_are_explicit(self):
        labels = ("metallo", "vetro", "plastica", "carta")
        self.assertEqual(classify_probabilities([1, 0, 0, 0], labels)["label"], "metallo")
        self.assertEqual(classify_probabilities([0.5, 0.5, 0, 0], labels)["label"], "metallo")
        for invalid in (("carta",) * 4, list(CLASSES[:3]), [1, 2, 3, 4], "carta"):
            with self.subTest(labels=invalid), self.assertRaises(ValueError):
                classify_probabilities([1, 0, 0, 0], invalid)

    def test_invalid_probability_vectors(self):
        for probabilities in ([1, 0, 0], [[1, 0, 0, 0]], [True, False, False, False],
                              [True, 0, 0, 0], [1.0, np.bool_(False), 0.0, 0.0],
                              [float("nan"), 0, 0, 0], [float("inf"), 0, 0, 0],
                              [-0.1, 1.1, 0, 0], [0, 0, 0, 0], ["1", "0", "0", "0"]):
            with self.subTest(probabilities=probabilities), self.assertRaises(ValueError):
                classify_probabilities(probabilities)

    def test_invalid_review_thresholds(self):
        for threshold in (True, None, "0.75", -0.1, 1.1, float("nan"), float("inf"), 10**1000):
            with self.subTest(threshold=type(threshold).__name__), self.assertRaises(ValueError):
                classify_probabilities([1, 0, 0, 0], min_confidence=threshold)

    def test_review_counts_cover_the_test_set(self):
        r = self.result
        self.assertEqual(r["automatic_samples"] + r["review_samples"], r["test_samples"])
        self.assertEqual((r["automatic_samples"], r["review_samples"]), (80, 0))
        self.assertEqual(r["min_test_confidence"], 1)


if __name__ == "__main__":
    unittest.main()
