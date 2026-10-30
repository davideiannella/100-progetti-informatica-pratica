# P042: Pagamenti simulati con idempotenza

[Catalogo](../../docs/CATALOGO.md) · [Output verificati](../../collaudo/P042/README.md) · [Registro del collaudo](../../collaudo/P042/registro.json)

**Sezione:** [Sezione 3: Ingegneria e progettazione del software](../../docs/CATALOGO.md#sezione-3-ingegneria-e-progettazione-del-software).

**Argomenti:** Affidabilità del software · Idempotenza · Concorrenza.

Ripeti una richiesta di pagamento simulato senza crearne una seconda identica. Il servizio conserva in memoria il risultato associato alla chiave e rifiuta la stessa chiave se viene riusata con un importo diverso.

Apri un terminale nella cartella `projects/P042` ed esegui da lì tutti i comandi. Gli esempi usano Linux e Bash; per Windows, segui anche la sezione dedicata.

## Requisiti e versioni

**Tecnologie utilizzate:** C# · .NET.

- .NET SDK 8.0.426 (collaudo locale storico)
- .NET runtime 8.0.26 (collaudo locale storico)

Dipendenze:

- .NET 8 net8.0 — Librerie di base; nessun PackageReference esterno. Progetto test eseguibile con ProjectReference a src/P042.csproj.

## Preparazione

Installa l’SDK .NET 8 indicato nei requisiti: è il pacchetto di strumenti necessario per compilare il progetto. Le versioni elencate sono quelle dei collaudi documentati; con strumenti diversi occorre ripetere le verifiche.

Dopo l’installazione dell’SDK non servono altri comandi di preparazione.

## Avvio

Esegui i comandi della sezione Test per provare il laboratorio. I test richiamano il codice e verificano i risultati; non c’è un’applicazione dimostrativa separata.

## Test

I test ripetono le richieste, provano chiavi in conflitto e input non validi ed eseguono 100 chiamate concorrenti. Se i controlli passano, stampano un messaggio `PASS`.

```bash
dotnet run --project tests/P042.Tests.csproj
```

## Perimetro del laboratorio

- Il servizio conserva i risultati soltanto in memoria. I test provano il reinvio della stessa richiesta (retry), i conflitti, gli input e 100 chiamate concorrenti; non avviano un server HTTP.

## Windows

Per provare il progetto direttamente su Windows serve l’SDK .NET 8. Il progetto usa il formato SDK-style con destinazione net8.0 e non richiede Bash o strumenti POSIX. L’esecuzione nativa su Windows non è stata collaudata nelle prove documentate.

## Collaudi documentati

**Ultimo collaudo: 31 ottobre 2026 — superato.** Le verifiche del progetto sono riuscite su Ubuntu 24.04 nel [collaudo pubblico P001–P080](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/41142475728), eseguito sul commit `c8303920c4f4`.

### Prove precedenti

Collaudo storico del 2026-10-16: Test locali registrati.

Queste istruzioni sono state ricavate dai file e dai collaudi conservati.
