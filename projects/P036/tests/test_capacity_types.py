from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from gym_domain import GymService,Instructor,Course
s=GymService();s.register_instructor(Instructor('I','Istruttore'))
for capacity in [0,-1,.5,True,'2']:
    try:s.add_course(Course('C','Corso','I',capacity))
    except ValueError:pass
    else:raise AssertionError('Capienza non intera o non positiva accettata')
assert not s.courses
s.add_course(Course('C','Corso','I',1))
assert s.courses['C'].capacity==1
print('P036: capienza intera positiva, rifiuto booleani e frazioni PASS')
