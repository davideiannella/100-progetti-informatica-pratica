import pathlib, sys, unittest
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))

import numpy as np
import waste_cv as m

class TestVision(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result=m.experiment()

    def test_known_rgb_statistics(self):
        im=np.array([[[0,255,0],[255,0,255]]],dtype=np.uint8)
        np.testing.assert_allclose(m.features(im),[.5,.5,.5,.5,.5,.5])

    def test_shape_validation(self):
        for shape in [(24,24),(0,2,3),(2,0,3),(2,2,4),(2,2,1),(3,),()]:
            with self.subTest(shape=shape),self.assertRaises(ValueError):
                m.features(np.zeros(shape,dtype=np.uint8))

    def test_dtype_and_nonfinite_validation(self):
        for value in [0.0,float('nan'),float('inf'),-1,256,'pixel',True]:
            with self.subTest(value=value),self.assertRaises(ValueError):
                m.features(np.full((2,2,3),value))

    def test_parameters_validation(self):
        for bad in [-1,1.5,True,float('nan'),None]:
            with self.subTest(bad=bad),self.assertRaises(ValueError):
                m.make_image('carta',bad)
        for bad in [0,1,257,False]:
            with self.subTest(size=bad),self.assertRaises(ValueError):
                m.make_image('carta',0,size=bad)
        with self.assertRaises(ValueError):m.make_image('metallo',0)

    def test_dataset_parameters(self):
        for split,n in [('bad',4),('train',0),('test',1001),('train',True)]:
            with self.subTest(split=split,n=n),self.assertRaises(ValueError):m.dataset(split,n)

    def test_ids_and_image_hashes_independent(self):
        tr=m.dataset('train',60);te=m.dataset('test',25)
        self.assertFalse(set(tr[2])&set(te[2]))
        self.assertFalse(set(tr[3])&set(te[3]))
        self.assertEqual(len(set(tr[3])),240)
        self.assertEqual(len(set(te[3])),100)

    def test_holdout_beats_constant_baseline(self):
        self.assertGreater(self.result['accuracy'],self.result['baseline_accuracy'])
        self.assertGreaterEqual(self.result['accuracy'],.8)

    def test_shift_reveals_palette_shortcut(self):
        self.assertLess(self.result['shifted_palette']['accuracy'],self.result['accuracy'])

    def test_shuffled_label_control(self):
        self.assertLess(self.result['shuffled_labels']['accuracy'],self.result['accuracy'])

    def test_matrix_from_predictions(self):
        manual=[[0]*4 for _ in range(4)]
        for p in self.result['predictions']:
            manual[m.CLASSES.index(p['truth'])][m.CLASSES.index(p['prediction'])]+=1
        self.assertEqual(manual,self.result['confusion_matrix'])
        self.assertEqual([sum(row) for row in manual],[25]*4)

    def test_scaler_fits_training_only(self):
        X,y,_,_=m.dataset('train',60)
        model=m.train_model(X,y)
        np.testing.assert_allclose(model.named_steps['standardscaler'].mean_,X.mean(axis=0))
        test,_,_,_=m.dataset('test',25)
        self.assertFalse(np.allclose(X.mean(axis=0),np.vstack([X,test]).mean(axis=0),rtol=0,atol=1e-10))

    def test_model_input_validation(self):
        X,y,_,_=m.dataset('train',2)
        for bad in [np.empty((0,6)),np.ones((8,5)),np.full((8,6),np.nan),np.full((8,6),np.inf),np.full((8,6),-1),np.full((8,6),2)]:
            with self.subTest(shape=bad.shape),self.assertRaises(ValueError):m.train_model(bad,y)
        with self.assertRaises(ValueError):m.train_model(X,y[:-1])

    def test_fit_is_deterministic(self):
        X,y,_,_=m.dataset('train',5)
        np.testing.assert_array_equal(m.train_model(X,y).predict(X),m.train_model(X,y).predict(X))


def seeded_case(seed):
    def test(self):
        rng=np.random.default_rng(seed)
        label=m.CLASSES[int(rng.integers(4))];size=int(rng.integers(2,49))
        a=m.make_image(label,seed,size=size);b=m.make_image(label,seed,size=size)
        np.testing.assert_array_equal(a,b)
        self.assertFalse(np.array_equal(a,m.make_image(label,seed+1000,size=size)))
        f=m.features(a)
        self.assertEqual(f.shape,(6,));self.assertTrue(np.isfinite(f).all())
        np.testing.assert_allclose(f[:3],a.reshape(-1,3).mean(axis=0)/255)
        np.testing.assert_allclose(f[3:],a.reshape(-1,3).std(axis=0)/255,atol=1e-14)
    return test
for seed in range(100):
    setattr(TestVision,f'test_seed_{seed:03d}',seeded_case(seed))

if __name__ == "__main__": unittest.main(verbosity=2)
