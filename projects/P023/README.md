# P023 — API .NET per attività concorrenti

Espone un’API .NET locale e verifica richieste HTTP concorrenti.

Tutti i comandi partono dalla cartella `projects/P023`. I blocchi seguenti usano la sintassi di Linux/Bash.

## Requisiti e versioni

Linguaggio: C# / Python per il test HTTP.

- Python 3.12.14
- .NET Target net8.0; SDK 8.0.426 documentato per P022/P040

Dipendenze:

- SDK .NET 8 e runtime .NET 8; nessun PackageReference esterno nei .csproj.
- ASP.NET Core tramite Microsoft.NET.Sdk.Web.
- Python con libreria standard e loopback 127.0.0.1 disponibile per la prova HTTP.

## Preparazione

Comandi per una shell Linux/Bash dalla cartella projects/P023. Installare Python 3.12 prima della preparazione; dopo l’attivazione, python indica l’interprete dell’ambiente virtuale .venv. Riattivare l’ambiente in ogni nuovo terminale. Le versioni indicate descrivono gli ambienti documentati, non un minimo universale.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
dotnet build src/P023.csproj
```

## Avvio

```bash
dotnet run --project src/P023.csproj -- --urls http://127.0.0.1:8000
```

L’avvio del servizio resta in primo piano. Usare un altro terminale per i controlli oppure interrompere con `Ctrl+C`.

## Test

```bash
python tests/test_http.py
```

Il build iniziale deve essere in configurazione Debug. Il test avvia e arresta autonomamente l’applicazione su una porta locale libera.

## Perimetro del laboratorio

- Il test non compila: cerca src/bin/Debug/net8.0/P023.dll. Un solo build Release non basta.
- Il test accetta il percorso dotnet come primo argomento facoltativo e riscrive tests/http_test.log.

## Windows

Progetti SDK .NET 8 con API portabili; nessun requisito Bash/POSIX. P023 richiede anche Python e loopback. Nessun test Windows documentato. Nessun test Windows nativo è attestato da questo README.

Per la parte Python nativa, dal **Prompt dei comandi (cmd.exe)**, nella cartella del progetto:

```bat
py -3.12 -m venv .venv
.venv\Scripts\activate.bat
```

Dopo l’attivazione, usare i comandi `python` di installazione, avvio e test indicati sopra. In alternativa, anche da PowerShell, invocare direttamente `.\.venv\Scripts\python.exe` al posto di `python`: non serve attivare script né cambiare la policy di esecuzione. Il comando di attivazione Bash non va copiato in PowerShell.

## Collaudi documentati

Collaudo storico su Linux: le suite disponibili e i casi aggiuntivi risultano superati. Il riepilogo del gruppo P001–P040 non riporta una data puntuale; questi risultati non sono stati rieseguiti per preparare il README.

Queste istruzioni sono state ricavate dai file e dai collaudi conservati. La preparazione dei README non ha eseguito nuove suite né modificato il codice.
