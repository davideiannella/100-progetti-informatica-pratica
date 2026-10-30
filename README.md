# 100 progetti di informatica pratica

[![P001–P080 su Ubuntu](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/workflows/collaudo-p001-p080.yml/badge.svg?branch=main)](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/workflows/collaudo-p001-p080.yml)
[![P081–P100 su Linux e Windows](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/workflows/collaudo-p081-p100.yml/badge.svg?branch=main)](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/workflows/collaudo-p081-p100.yml)

Codice, test e istruzioni dei cento laboratori del libro di **Davide Iannella**. Per studenti, autodidatti con basi di programmazione e professionisti junior: algoritmi, dati, progettazione del software, reti, sistemi operativi, cloud, sicurezza, intelligenza artificiale e IoT, con modelli ed esempi locali riproducibili.

## Scegli una sezione

I progetti seguono le stesse **dieci sezioni tematiche del libro**. Puoi procedere nell’ordine proposto oppure scegliere l’argomento che ti interessa. Il [catalogo completo](docs/CATALOGO.md) riporta ambiente e argomenti di ogni progetto; nei README trovi anche le combinazioni fra più discipline.

| Sezione | Progetti | Argomento principale |
|---|---|---|
| 1 | P001–P023 | [Programmazione, algoritmi e strutture dati](docs/CATALOGO.md#sezione-1-programmazione-algoritmi-e-strutture-dati) |
| 2 | P024–P035 | [Database e gestione dei dati](docs/CATALOGO.md#sezione-2-database-e-gestione-dei-dati) |
| 3 | P036–P044 | [Ingegneria e progettazione del software](docs/CATALOGO.md#sezione-3-ingegneria-e-progettazione-del-software) |
| 4 | P045–P050 | [Reti di calcolatori](docs/CATALOGO.md#sezione-4-reti-di-calcolatori) |
| 5 | P051–P053 | [Sistemi operativi](docs/CATALOGO.md#sezione-5-sistemi-operativi) |
| 6 | P054–P062 | [Cloud e affidabilità dei servizi](docs/CATALOGO.md#sezione-6-cloud-e-affidabilità-dei-servizi) |
| 7 | P063–P072 | [Sicurezza informatica](docs/CATALOGO.md#sezione-7-sicurezza-informatica) |
| 8 | P073–P082 | [Intelligenza artificiale e analisi dei dati](docs/CATALOGO.md#sezione-8-intelligenza-artificiale-e-analisi-dei-dati) |
| 9 | P083–P094 | [IoT e simulazione di sistemi](docs/CATALOGO.md#sezione-9-iot-e-simulazione-di-sistemi) |
| 10 | P095–P100 | [Progetti integrati](docs/CATALOGO.md#sezione-10-progetti-integrati) |

La sezione Cloud comprende container, rilascio e affidabilità dei servizi; diversi laboratori usano modelli locali. La sezione IoT comprende simulazioni e dati sintetici. Ogni progetto descrive il proprio perimetro e le eventuali estensioni.

## Iniziare

1. Scarica **Code → Download ZIP** ed estrai l’archivio, oppure clona il repository:

   ```text
   git clone https://github.com/davideiannella/100-progetti-informatica-pratica.git
   cd 100-progetti-informatica-pratica
   ```

2. Scegli un laboratorio nel [catalogo dei 100 progetti](docs/CATALOGO.md). Per un primo esercizio Python puoi partire da [P001](projects/P001/README.md).
3. Prepara l’[ambiente Linux, Windows o WSL](docs/AMBIENTI.md) e segui **Requisiti**, **Preparazione** e **Test** nel README del progetto. Esegui i comandi dalla cartella indicata: i linguaggi e le dipendenze cambiano fra i laboratori.

Alcuni progetti contengono funzioni e classi da provare attraverso i test. Una suite è un insieme di test eseguiti insieme: controlla che il programma rispetti le regole previste. Il README di ogni progetto indica come avviare la dimostrazione, quando presente, e come eseguire le verifiche.

## Dove trovare i materiali

I **sorgenti** sono i file con il codice da leggere ed eseguire. La cartella **projects** li raccoglie; **collaudo** raccoglie i risultati documentati di P001–P100. Per orientarti consulta la [guida alla struttura](docs/STRUTTURA.md).

| Percorso | Contenuto |
|---|---|
| [projects](projects/README.md) | Cento cartelle autonome, da `P001` a `P100`, con README, sorgenti e test |
| [Catalogo](docs/CATALOGO.md) | Dieci sezioni, argomenti, ambienti e collegamenti ai singoli laboratori |
| [Ambienti](docs/AMBIENTI.md) | Interpreti, compilatori, dipendenze e differenze fra sistemi |
| [collaudo](collaudo/README.md) | Esiti, log, versioni, provenienza e limiti delle prove |
| [tools](tools/README.md) | Script che coordinano i collaudi del repository |
| [SOURCE_SHA256.json](SOURCE_SHA256.json) | Impronte dei file sorgenti per controllarne l’integrità |

## Verifiche automatiche

GitHub Actions esegue automaticamente i controlli seguendo procedure chiamate **workflow**. Ogni esecuzione, indicata come **run**, è divisa in attività chiamate **job**.

Gli [output dei collaudi per tutti i 100 progetti](collaudo/README.md) riportano i comandi, gli esiti e i testi effettivamente acquisiti. Per i test `unittest`, il normale resoconto con i nomi dei test si trova nel canale stderr.

| Workflow | Ambiente e perimetro |
|---|---|
| [P001–P080](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/workflows/collaudo-p001-p080.yml) | Ubuntu; strumenti e servizi distinti per gruppo di progetti |
| [P081–P100](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/workflows/collaudo-p081-p100.yml) | Ubuntu e Windows, ciascuno con Python 3.12 e 3.13 |

I badge mostrano lo stato del workflow. Per verificare una versione, apri il relativo run e controlla **commit, job e log**. La matrice P081–P100 ripete gli stessi 377 test distinti in quattro ambienti. Le prove Ubuntu di P001–P080 non attestano una verifica nativa Windows; simulazioni e dati sintetici restano entro il perimetro descritto nei README e nei [registri](collaudo/PROVENIENZA.md).

Le [correzioni del 30 ottobre 2026](docs/REVISIONE_2026_10_30.md) descrivono i casi limite risolti, i test rafforzati e il rapporto con gli output storici.

## Versioni e segnalazioni

Conserva il commit associato alla copia che usi: `main` può cambiare. Per segnalare un problema indica progetto, commit, sistema operativo, versioni, comando e messaggio completo di errore, rimuovendo dati personali e credenziali.

## Licenza e libro

Il codice originale e la documentazione tecnica del repository sono **gratuiti**, con [licenza MIT](LICENSE), anche per uso commerciale nel rispetto delle sue condizioni. Le dipendenze conservano le proprie licenze. **Libro, copertine e altri materiali editoriali hanno diritti separati** e non sono concessi dalla licenza MIT del repository.
