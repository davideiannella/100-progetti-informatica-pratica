# P042: Pagamenti simulati con idempotenza

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../COLLAUDO/P042/README.md) · [Registro del collaudo](../../COLLAUDO/P042/registro.json)

Controlla idempotenza, conflitti e richieste concorrenti in pagamenti simulati.

Tutti i comandi partono dalla cartella `projects/P042`. I blocchi seguenti usano la sintassi di Linux/Bash.

## Requisiti e versioni

Linguaggio: C# / .NET.

- .NET SDK 8.0.426 (collaudo locale storico)
- .NET runtime 8.0.26 (collaudo locale storico)

Dipendenze:

- .NET 8 net8.0 — Librerie di base; nessun PackageReference esterno. Progetto test eseguibile con ProjectReference a src/P042.csproj.

## Preparazione

Comandi per una shell Linux/Bash dalla cartella projects/P042. Installare prima il compilatore o SDK indicato nei requisiti. Le versioni documentate non costituiscono una garanzia per toolchain diverse.

Non sono previsti ulteriori comandi di preparazione oltre all’installazione della toolchain indicata.

## Avvio

Non è presente un’applicazione dimostrativa autonoma: usare i test sotto come punto di ingresso eseguibile.

## Test

```bash
dotnet run --project tests/P042.Tests.csproj
```

## Perimetro del laboratorio

- Il servizio è una libreria in memoria. L’eseguibile dei test dimostra retry, conflitto, input e 100 chiamate concorrenti; non avvia un server HTTP.

## Windows

SDK .NET 8 e progetti SDK-style net8.0 rendono plausibile l’avvio Windows nativo; nessun uso di Bash/POSIX nei file esaminati. Nessun test Windows nativo è attestato da questo README.

## Collaudi documentati

Collaudo storico del 2026-10-16: Test locali registrati; nessun nuovo test eseguito durante questa revisione.

Queste istruzioni sono state ricavate dai file e dai collaudi conservati. La preparazione dei README non ha eseguito nuove suite né modificato il codice.
