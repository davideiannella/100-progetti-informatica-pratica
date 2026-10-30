# P022: Gestire manutenzioni e ordini di lavoro con .NET

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P022/README.md) · [Registro del collaudo](../../collaudo/P022/registro.json)

**Sezione:** [Sezione 1: Programmazione, algoritmi e strutture dati](../../docs/CATALOGO.md#sezione-1-programmazione-algoritmi-e-strutture-dati).

**Argomenti:** Programmazione a oggetti · Software gestionale · Test.

Registri i beni da mantenere, apri e chiudi ordini di lavoro e conti quelli ancora aperti. Il programma .NET conserva i dati in memoria durante l’esecuzione.

Apri un terminale nella cartella `projects/P022` ed esegui da lì i comandi. I blocchi seguenti usano la sintassi di Linux/Bash; per Windows consulta la sezione dedicata.

## Requisiti e versioni

**Tecnologie utilizzate:** C# · .NET.

- .NET Target net8.0; SDK 8.0.426 documentato per P022/P040

Dipendenze:

- SDK .NET 8 e runtime .NET 8; nessun PackageReference esterno nei .csproj.

## Preparazione

Installa il compilatore o il kit di sviluppo (SDK) indicato nei requisiti. Le versioni documentate descrivono gli strumenti usati nei collaudi; con strumenti diversi, verifica il risultato eseguendo i test.

Dopo l’installazione degli strumenti richiesti, puoi passare ai comandi seguenti.

## Avvio

```bash
dotnet run --project src/P022.csproj
```

## Test

Il test controlla apertura e chiusura degli ordini, conteggi, duplicati, beni inesistenti e descrizioni vuote. Se tutti i controlli riescono, stampa `PASS`.

```bash
dotnet run --project tests/P022.Tests.csproj
```

## Windows

Il progetto usa .NET 8 e funzioni portabili, senza richiedere Bash o funzioni specifiche di Linux. Con .NET 8 installato, puoi usare i comandi `dotnet` anche su Windows. I collaudi documentati in questa pagina non comprendono una prova nativa su Windows.

## Collaudi documentati

I materiali conservati documentano un collaudo su Linux con esito positivo per le suite disponibili e le prove aggiuntive. Il riepilogo storico del gruppo P001–P040 non indica una data precisa.

Consulta **Output verificati** e **Registro del collaudo**, all’inizio della pagina, per leggere comandi, ambiente e limiti di ciascuna prova. I risultati documentati descrivono quei collaudi; per verificare la copia che stai usando, esegui i test sul tuo computer.
