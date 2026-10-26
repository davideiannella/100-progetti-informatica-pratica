# P022: Nucleo .NET per manutenzioni e ordini di lavoro

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P022/README.md) · [Registro del collaudo](../../collaudo/P022/registro.json)

Modella manutenzioni e ordini di lavoro con un programma .NET locale.

Tutti i comandi partono dalla cartella `projects/P022`. I blocchi seguenti usano la sintassi di Linux/Bash.

## Requisiti e versioni

Linguaggio: C#.

- .NET Target net8.0; SDK 8.0.426 documentato per P022/P040

Dipendenze:

- SDK .NET 8 e runtime .NET 8; nessun PackageReference esterno nei .csproj.

## Preparazione

Comandi per una shell Linux/Bash dalla cartella projects/P022. Installare prima il compilatore o SDK indicato nei requisiti. Le versioni documentate non costituiscono una garanzia per toolchain diverse.

Non sono previsti ulteriori comandi di preparazione oltre all’installazione della toolchain indicata.

## Avvio

```bash
dotnet run --project src/P022.csproj
```

## Test

```bash
dotnet run --project tests/P022.Tests.csproj
```

## Windows

Progetti SDK .NET 8 con API portabili; nessun requisito Bash/POSIX. P023 richiede anche Python e loopback. Nessun test Windows documentato. Nessun test Windows nativo è attestato da questo README.

## Collaudi documentati

Collaudo storico su Linux: le suite disponibili e i casi aggiuntivi risultano superati. Il riepilogo del gruppo P001–P040 non riporta una data puntuale; questi risultati non sono stati rieseguiti per preparare il README.

Queste istruzioni sono state ricavate dai file e dai collaudi conservati. La preparazione dei README non ha eseguito nuove suite né modificato il codice.
