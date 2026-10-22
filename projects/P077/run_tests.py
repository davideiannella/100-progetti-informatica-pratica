"""Esegue i test veri e stampa un riepilogo JSON; exit code nonzero sui fallimenti."""
import argparse,json,pathlib,sys,time,unittest
ROOT=pathlib.Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'src'))
class Result(unittest.TextTestResult):
    seeded=0
    def startTest(self,test):
        super().startTest(test)
        if '.test_seed_' in test.id(): self.seeded+=1
def main():
    parser=argparse.ArgumentParser();parser.add_argument('--json',type=pathlib.Path);args=parser.parse_args()
    suite=unittest.defaultTestLoader.discover(str(ROOT/'tests'))
    start=time.monotonic();result=unittest.TextTestRunner(verbosity=2,resultclass=Result).run(suite)
    report={'project':ROOT.name,'tests_run':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),'skipped':len(result.skipped),'seeded_cases':result.seeded,'passed':result.wasSuccessful(),'seconds':time.monotonic()-start}
    serialized=json.dumps(report,indent=2);print(serialized)
    if args.json:args.json.write_text(serialized+'\n',encoding='utf-8')
    return 0 if result.wasSuccessful() else 1
if __name__=='__main__':raise SystemExit(main())
