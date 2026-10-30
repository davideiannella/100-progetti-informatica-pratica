# P040: Segnalazioni civiche con Clean Architecture

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P040/README.md) · [Registro del collaudo](../../collaudo/P040/registro.json)

**Sezione:** [Sezione 3: Ingegneria e progettazione del software](../../docs/CATALOGO.md#sezione-3-ingegneria-e-progettazione-del-software).

**Argomenti:** Architettura software · Gestione delle dipendenze.

Crei segnalazioni civiche e separi i controlli sui dati dal modo in cui vengono conservati. Il repository di esempio è un archivio in memoria, utile per provare le regole senza avviare un database.

Apri un terminale nella cartella `projects/P040` ed esegui da lì i comandi. I blocchi seguenti usano la sintassi di Linux/Bash; per Windows consulta la sezione dedicata.

## Requisiti e versioni

**Tecnologie utilizzate:** C# · .NET.

- .NET Target net8.0; SDK 8.0.426 documentato per P022/P040

Dipendenze:

- SDK .NET 8 e runtime .NET 8; nessun PackageReference esterno nei .csproj.

## Preparazione

Installa il compilatore o il kit di sviluppo (SDK) indicato nei requisiti. Le versioni documentate descrivono gli strumenti usati nei collaudi; con strumenti diversi, verifica il risultato eseguendo i test.

Dopo l’installazione degli strumenti richiesti, puoi passare ai comandi seguenti.

## Avvio

Per provare il laboratorio, esegui i test della sezione seguente: creano i dati di esempio e chiamano le operazioni previste. Non è presente un’applicazione dimostrativa separata.

## Test

Il test controlla creazione, dati non validi, duplicati e accesso al repository. Se le verifiche riescono, stampa `PASS`. Nel suo messaggio, «persistenza» indica che il dato resta recuperabile durante la stessa esecuzione: non viene salvato su disco.

```bash
dotnet run --project tests/P040.Tests.csproj
```

## Windows

Il progetto usa .NET 8 e funzioni portabili, senza richiedere Bash o funzioni specifiche di Linux. Con .NET 8 installato, puoi usare i comandi `dotnet` anche su Windows. I collaudi documentati in questa pagina non comprendono una prova nativa su Windows.

## Collaudi documentati

**Ultimo collaudo: 30 ottobre 2026 — superato.** Le verifiche del progetto sono riuscite su Ubuntu 24.04 nel [collaudo pubblico P001–P080](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/41134634700), eseguito sul commit `35b49f130493`.

### Prove precedenti

Nel [collaudo del 22 ottobre 2026](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701), le verifiche della versione di allora sono riuscite su Ubuntu 24.04.

Consulta **Output verificati** e **Registro del collaudo**, all’inizio della pagina, per leggere comandi, ambiente e limiti di ciascuna prova. I risultati documentati descrivono quei collaudi; per verificare la copia che stai usando, esegui i test sul tuo computer.
