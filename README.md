# 100 progetti di informatica pratica

Sorgenti e test dei cento laboratori del libro di **Davide Iannella**. Il percorso è pensato per studenti e autodidatti con basi di programmazione e per professionisti junior che desiderano esercitarsi su problemi concreti.

Ogni cartella `projects/P001` … `projects/P100` contiene il codice del laboratorio, i suoi test e un README con ambiente, dipendenze e comandi. I capitoli, la copertina e i file editoriali del libro sono distribuiti separatamente.

## Iniziare

Scarica il repository con **Code → Download ZIP**, estrailo in un percorso breve (per esempio `C:\ip` oppure `~/ip`) e apri il README del progetto scelto. Esegui i comandi dalla sua cartella, salvo indicazione diversa. Puoi anche usare Git:

```text
git clone https://github.com/davideiannella/100-progetti-informatica-pratica.git
cd 100-progetti-informatica-pratica
```

Per Python crea un ambiente virtuale dedicato e installa soltanto i requisiti del laboratorio. Esempio da Linux, dalla radice del repository:

```sh
python3.12 -m venv .venv
. .venv/bin/activate
```

Da Windows, con il Prompt dei comandi:

```bat
py -3.12 -m venv .venv
.venv\Scripts\activate.bat
```

Da PowerShell puoi invocare direttamente `.venv\Scripts\python.exe`, senza cambiare i criteri di esecuzione del sistema. Nei comandi dei README `python` indica l’interprete dell’ambiente virtuale attivo. Verificalo con `python --version`.

Python 3.12 e 3.13 sono i riferimenti dei laboratori P061–P100; i requisiti condivisi sono `requirements-p061-p080.txt` e `requirements-p081-p100.txt`. I progetti precedenti comprendono anche Java 17, C/C++, .NET 8 e database: consulta sempre il README specifico. I laboratori che richiedono POSIX o `/proc` si eseguono su Linux; da Windows usa WSL e conserva i file nel filesystem Linux. Docker e Kubernetes richiedono i rispettivi strumenti, con container Linux.

## Verifiche

Il workflow [Collaudo pubblico P081 P100 Linux e Windows](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/workflows/collaudo-p081-p100.yml) esegue le venti suite P081–P100 su Ubuntu e Windows, con Python 3.12 e 3.13. Controlla lo stato e i log della singola esecuzione: la presenza del workflow non significa che sia già terminato con successo.

Ogni job verifica il manifest `SOURCE_SHA256.json`, compila i sessanta file Python P081–P100 e richiede **377 metodi di test senza skip**. Per ripetere questa verifica, dopo aver installato `requirements-p081-p100.txt`:

```text
python -B tools/collaudo_p081_p100.py
```

Gli esiti locali vengono scritti in `test-results`. I test verificano i casi e gli ambienti documentati. Le simulazioni locali non certificano dispositivi, impianti, infrastrutture cloud o sistemi di produzione. Per gli altri ottanta laboratori segui i test nel relativo README; questo workflow non li esegue.

## Versioni e segnalazioni

Per accompagnare un’edizione del libro conserva l’identificativo del commit usato. Il ramo `main` può ricevere correzioni successive. Una segnalazione utile indica progetto, commit, sistema operativo, versioni, comando eseguito, risultato atteso e messaggio completo di errore, senza dati personali o segreti.

## Licenza

Il codice originale e la documentazione tecnica presenti in questo repository sono disponibili con [licenza MIT](LICENSE), gratuitamente, anche per uso commerciale, nel rispetto delle sue condizioni. Il libro, le copertine e gli altri materiali editoriali non sono concessi con questa licenza. Le dipendenze di terzi mantengono le rispettive licenze.
