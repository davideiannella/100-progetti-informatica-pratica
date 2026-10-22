import pathlib, sys, unittest
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))

import random
import numpy as np
import ticket_nlp as m

class TestTicket(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model = m.train_model()

    def test_split_no_shared_ids_or_texts(self):
        tr, te = m.validate_split(m.TRAIN_DATA, m.TEST_DATA)
        self.assertFalse({r[0] for r in tr} & {r[0] for r in te})
        self.assertFalse({r[1] for r in tr} & {r[1] for r in te})
        self.assertEqual((len(tr), len(te)), (24, 12))

    def test_overlap_rejected_even_different_id(self):
        with self.assertRaises(ValueError):
            m.experiment(test=[('new', '  NON RIESCO AD ACCEDERE ACCOUNT PASSWORD ', 'accesso')])

    def test_punctuation_cannot_disguise_train_test_duplicate(self):
        with self.assertRaises(ValueError):
            m.experiment(test=[('new', 'reset, PASSWORD! utente.', 'accesso')])

    def test_holdout_token_never_fitted(self):
        vocab = self.model.named_steps['tfidf'].vocabulary_
        self.assertNotIn('bianca', vocab)
        self.assertNotIn('recupero', vocab)
        before = dict(vocab)
        m.classify(self.model, 'parolasegretaesclusivatest')
        self.assertEqual(vocab, before)

    def test_input_validation(self):
        for value in [None, 12, float('nan'), float('inf'), [], {}, '', ' \n ', '!!!', '123', 'a', 'x'*5001]:
            with self.subTest(value=repr(value)), self.assertRaises(ValueError):
                m.classify(self.model, value)

    def test_bad_training_rows(self):
        for rows in [[], None, [('x','password')], [('x', 'password', 'alieno')], [('x', '', 'accesso')],
                     [('', 'password', 'accesso')], [('x', 'password', [])]]:
            with self.subTest(rows=rows), self.assertRaises(ValueError):
                m.train_model(rows)

    def test_duplicates_rejected(self):
        for extra in [('a01','altra password','accesso'), ('z','RESET   PASSWORD UTENTE','accesso')]:
            with self.subTest(extra=extra), self.assertRaises(ValueError):
                m.train_model(list(m.TRAIN_DATA)+[extra])

    def test_missing_class_rejected(self):
        with self.assertRaises(ValueError):
            m.train_model(m.TRAIN_DATA[:8])

    def test_unseen_terms_abstain(self):
        self.assertIsNone(m.classify(self.model, 'astronave quantistica')['label'])

    def test_known_example(self):
        self.assertEqual(m.classify(self.model, 'ho dimenticato la password')['label'], 'accesso')

    def test_metric_counts_from_predictions(self):
        r=m.experiment()
        manual=[[0]*3 for _ in range(3)]
        for p in r['predictions']:
            manual[m.CLASSES.index(p['truth'])][m.CLASSES.index(p['prediction'])]+=1
        self.assertEqual(manual,r['confusion_matrix'])
        self.assertEqual(sum(map(sum,manual)),12)
        self.assertAlmostEqual(r['accuracy'],sum(manual[i][i] for i in range(3))/12)
        self.assertGreater(r['accuracy'],r['baseline_accuracy'])

    def test_deterministic_fit(self):
        other=m.train_model()
        np.testing.assert_allclose(self.model.named_steps['clf'].coef_,other.named_steps['clf'].coef_,rtol=0,atol=0)

    def test_training_order_does_not_change_labels(self):
        rows=list(m.TRAIN_DATA);random.Random(771).shuffle(rows)
        other=m.train_model(rows)
        for _, text, _ in m.TEST_DATA:
            self.assertEqual(m.classify(self.model,text),m.classify(other,text))

    def test_unicode_normalization(self):
        self.assertEqual(m.normalize_text('ＰＡＳＳＷＯＲＤ\t account'), 'password account')

    def test_probability_finite_and_normalized(self):
        p=self.model.predict_proba([r[1] for r in m.TEST_DATA])
        self.assertTrue(np.isfinite(p).all())
        np.testing.assert_allclose(p.sum(axis=1),1)


def seeded_case(seed):
    def test(self):
        rng=random.Random(seed)
        _,text,label=m.TRAIN_DATA[rng.randrange(len(m.TRAIN_DATA))]
        words=[word.upper() if rng.randrange(2) else word for word in text.split()]
        variant=(' '*rng.randint(1,4)).join(words)+' zzinvisibile'+str(seed)
        self.assertEqual(m.classify(self.model,variant)['label'],label)
        self.assertIsNone(m.classify(self.model,'zzfuorivocabolario'+str(seed))['label'])
    return test
for seed in range(100):
    setattr(TestTicket, f'test_seed_{seed:03d}', seeded_case(seed))

if __name__ == "__main__": unittest.main(verbosity=2)
