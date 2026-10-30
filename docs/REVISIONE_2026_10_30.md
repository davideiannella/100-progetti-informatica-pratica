# Revisione dei progetti del 30 ottobre 2026

[Pagina principale](../README.md) · [Catalogo](CATALOGO.md) · [Registri dei collaudi](../collaudo/README.md)

Questa revisione corregge alcuni casi limite e rende più precisi i test. Il controllo ha confrontato i cento progetti con i capitoli corrispondenti del Kindle, dividendo il lavoro fra cinque revisioni di venti progetti ciascuna.

## Correzioni al codice

| Progetto | Comportamento corretto |
|---|---|
| [P050 — Piano Wi-Fi](../projects/P050/README.md) | Il numero di dispositivi e l'obiettivo per access point devono essere interi positivi. Valori decimali, booleani e non finiti sono rifiutati con un messaggio chiaro. |
| [P058 — Backup](../projects/P058/README.md) | La dimostrazione di un backup corrotto termina con un errore se il ripristino non lo rifiuta. Prima poteva terminare senza segnalare questo difetto. |
| [P077 — Classificazione dei ticket](../projects/P077/README.md) | Il numero di ticket nella descrizione si aggiorna quando il lettore amplia il dataset. Con 24 ticket di training e 21 di test indica 45 ticket. |
| [P094 — Indicatori di una città](../projects/P094/README.md) | La media usa `statistics.mean`: gestisce valori molto grandi e molto piccoli e non genera un falso allarme con undici valori uguali a `0.1` e soglia `0.1`. |

P094 può mostrare una diversa ultima cifra decimale rispetto ai vecchi output. Per i valori dimostrativi 20, 40 e 50, il risultato corrente è `36.666666666666664`. I log delle prove precedenti conservano il risultato ottenuto dal codice di allora.

## Test resi più precisi

| Progetto | Verifica aggiunta o rafforzata |
|---|---|
| [P026](../projects/P026/tests/test_p026.py) | Voti fuori intervallo, voti frazionari, lode, iscrizione e risultati duplicati sono verificati separatamente. Una chiave duplicata non può più nascondere un controllo mancante sul voto. |
| [P029](../projects/P029/tests/test_p029.py) | I tentativi di inserire e aggiornare prenotazioni sovrapposte raggiungono realmente il database. Sono verificati anche intervalli adiacenti e camere diverse. |
| [P030](../projects/P030/tests/test_p030.py) | Le date non valide sono provate senza provocare contemporaneamente un conflitto con l'unicità del prestito attivo. Sono controllati anche aggiornamento e restituzione. |
| [P041](../projects/P041/tests/NotificationsTest.java) | La notifica deve conservare canale, destinatario e messaggio, non soltanto il prefisso del canale. |
| [P045](../projects/P045/tests/test_network_plan.py) | Il validatore deve rifiutare sottoreti esterne, capienza insufficiente e sovrapposizioni. |
| [P050](../projects/P050/tests/test_p050.py) | Sono provati entrambi i parametri non validi e il passaggio da uno a due access point. |
| [P077](../projects/P077/tests/test_p077.py) | L'esercizio con nove ticket aggiuntivi deve aggiornare il totale a 45, mantenendo separati training e test. La suite passa da 115 a 116 metodi. |
| [P094](../projects/P094/tests/test_p094.py) | Le medie sono confrontate con un riferimento razionale esatto; sono inclusi valori estremi e il comportamento sulla soglia. |
| [P100](../projects/P100/tests/test_smart_waste_platform.py) | Un dispositivo sconosciuto deve essere rifiutato per quell'identità. Una firma già errata non può più nascondere il mancato controllo del dispositivo. |

I test modificati sono stati eseguiti. In copie temporanee sono stati introdotti anche errori mirati, per controllare che le verifiche fallissero quando dovevano. Queste copie difettose non fanno parte dei progetti distribuiti.

## Ambiente del collaudo automatico

Il primo nuovo collaudo ha rilevato una discordanza nella preparazione di .NET: il workflow installava l’ultima versione 8.0 disponibile, mentre la procedura richiedeva esattamente l’SDK 8.0.426. L’installazione è ora allineata alla versione richiesta, prima di avviare i test di P022, P023 e P040. Il tentativo precedente rimane consultabile nei log di GitHub Actions.

## Istruzioni e testo

Sono state chiarite le istruzioni Java su Windows e documentate le dimostrazioni già presenti in P041 e P044. Il titolo P067 è ora uniforme nel catalogo e nel README. Le note sui collaudi conservano date e ambienti, evitando riferimenti ambigui a «questa revisione».

Nel Kindle sono state allineate le spiegazioni interessate dalle correzioni. Le descrizioni di P028, P029, P031 e P097 distinguono ciò che dimostrano i log storici da ciò che il lettore verifica nell'esercizio. I riquadri, le figure e la copertina restano quelli dell'edizione approvata.

## Controllare la versione e gli esiti

Il manifest [SOURCE_SHA256.json](../SOURCE_SHA256.json) riporta le impronte dei file aggiornati. I workflow eseguono di nuovo tutti i progetti quando cambia il codice o il manifest:

- [P001–P080 su Ubuntu](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/workflows/collaudo-p001-p080.yml): linguaggi diversi, database e container secondo il laboratorio.
- [P081–P100 su Ubuntu e Windows](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/workflows/collaudo-p081-p100.yml): Python 3.12 e 3.13.

Apri l'esecuzione associata al commit che stai usando e controlla job, esiti e log. Gli output già presenti nella cartella `collaudo` rimangono registri datati delle prove precedenti; non vengono riscritti per farli apparire nuovi. Le nuove esecuzioni conservano i propri output negli artifact di GitHub Actions.

I test verificano i casi e gli ambienti descritti. Il controllo di tutti i progetti non equivale a una prova matematica dell'assenza di ogni possibile errore, né a un collaudo nativo Windows dei progetti provati soltanto su Ubuntu.

## Esito dei collaudi del 30 ottobre 2026

- [P001–P080](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/41134634700): cinque job riusciti sul commit `35b49f130493ddd03e3c16d00f373d7bfe4237a7`, inclusi i controlli dei database e dei container.
- [P081–P100](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/41133691301): quattro job riusciti sul commit `4741cc45e376c39bcddcc63d519bd579efc31c19`, su Ubuntu e Windows con Python 3.12 e 3.13.

Fra queste versioni e l’aggiornamento delle date nei README, i sorgenti, i test e il manifest restano identici. È cambiata la documentazione e, per il secondo collaudo P001–P080, la selezione dell’SDK .NET. Le date nei README sono quelle delle esecuzioni effettive; le prove storiche restano distinte.

## Riferimenti tecnici

- [SQLite: vincoli delle tabelle](https://www.sqlite.org/lang_createtable.html).
- [SQLite: trigger su inserimento e aggiornamento](https://www.sqlite.org/lang_createtrigger.html).
- [Python 3.12: media aritmetica con `statistics.mean`](https://docs.python.org/3.12/library/statistics.html#statistics.mean).

Le fonti descrivono il comportamento degli strumenti. Le prove eseguite sul progetto verificano che il codice li utilizzi nel modo previsto.
