import sys
from pathlib import Path
from datetime import datetime
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from telemetry_model import Telemetry
for value in [None,True,'20',float('nan'),float('inf')]:
    try: Telemetry('A',datetime(2026,10,1),value,50).to_document()
    except ValueError: pass
    else: raise AssertionError('Metrica non valida accettata')
for device in [None,'',' ']:
    try:Telemetry(device,datetime(2026,10,1),20,50).to_document()
    except ValueError:pass
    else:raise AssertionError('Identificativo non valido accettato')
print('P031: tipi, finitezza e identificativi PASS')
