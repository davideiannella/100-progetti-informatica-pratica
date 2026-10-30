# P023: API .NET per attività concorrenti

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P023/README.md) · [Registro del collaudo](../../collaudo/P023/registro.json)

**Sezione:** [Sezione 1: Programmazione, algoritmi e strutture dati](../../docs/CATALOGO.md#sezione-1-programmazione-algoritmi-e-strutture-dati).

**Argomenti:** API web · Concorrenza.

Crei, elenchi e completi attività tramite richieste HTTP a un servizio .NET locale. I test controllano anche richieste simultanee; le attività restano in memoria e si perdono quando il servizio viene riavviato.

Apri un terminale nella cartella `projects/P023` ed esegui da lì i comandi. I blocchi seguenti usano la sintassi di Linux/Bash; per Windows consulta la sezione dedicata.

## Requisiti e versioni

**Tecnologie utilizzate:** C# · .NET · ASP.NET Core · Python.

- Python 3.12.14
- .NET Target net8.0; SDK 8.0.426 documentato per P022/P040

Dipendenze:

- SDK .NET 8 e runtime .NET 8; nessun PackageReference esterno nei .csproj.
- ASP.NET Core tramite Microsoft.NET.Sdk.Web.
- Python con libreria standard e loopback 127.0.0.1 disponibile per la prova HTTP.

## Preparazione

Installa Python 3.12, poi crea e attiva l’ambiente virtuale con i comandi seguenti. Dopo l’attivazione, `python` usa l’interprete dell’ambiente `.venv`. Riattiva l’ambiente ogni volta che apri un nuovo terminale. Le versioni elencate descrivono gli ambienti documentati: non sono necessariamente le versioni minime richieste.

```bash
python3.12 -m venv .venv
. .venv/bin/activate
dotnet build src/P023.csproj
```

## Avvio

```bash
dotnet run --project src/P023.csproj -- --urls http://127.0.0.1:8000
```

Il servizio resta attivo nel terminale. Aprine un altro per eseguire i controlli; per arrestare il servizio, premi `Ctrl+C` nel terminale in cui lo hai avviato.

## Test

Il test avvia il servizio, invia richieste HTTP e controlla anche 100 creazioni concorrenti e 30 richieste di completamento. Stampa `PASS` se i controlli previsti riescono.

```bash
python tests/test_http.py
```

Compila prima il progetto in configurazione Debug, come fa il comando di preparazione. Il test avvia e arresta da solo l’applicazione su una porta locale libera: non devi tenere aperto il servizio dimostrativo per eseguirlo.

## Perimetro del laboratorio

- Il test non compila il progetto: cerca il file `src/bin/Debug/net8.0/P023.dll`. Aver compilato soltanto in configurazione Release non basta.
- Puoi passare al test il percorso di `dotnet` come primo argomento facoltativo. A ogni esecuzione viene riscritto il log `tests/http_test.log`.

## Windows

Il progetto usa .NET 8 e funzioni portabili. Per il test servono anche Python e la comunicazione di loopback, cioè una connessione che resta sullo stesso computer. Il codice non richiede funzioni specifiche di Linux, ma i collaudi documentati in questa pagina non comprendono una prova nativa su Windows.

Per preparare Python su Windows, apri il **Prompt dei comandi (cmd.exe)** nella cartella del progetto ed esegui:

```bat
py -3.12 -m venv .venv
.venv\Scripts\activate.bat
```

Dopo l’attivazione, esegui i comandi `python` di installazione, avvio e test indicati sopra. In alternativa, anche da PowerShell, usa direttamente `.\.venv\Scripts\python.exe` al posto di `python`: non devi attivare script né cambiare le regole di esecuzione di PowerShell. Non copiare in PowerShell il comando di attivazione Bash.

## Collaudi documentati

I materiali conservati documentano un collaudo su Linux con esito positivo per le suite disponibili e le prove aggiuntive. Il riepilogo storico del gruppo P001–P040 non indica una data precisa.

Consulta **Output verificati** e **Registro del collaudo**, all’inizio della pagina, per leggere comandi, ambiente e limiti di ciascuna prova. I risultati documentati descrivono quei collaudi; per verificare la copia che stai usando, esegui i test sul tuo computer.
