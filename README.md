# 100 progetti di informatica pratica

[![P001–P080 su Ubuntu](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/workflows/collaudo-p001-p080.yml/badge.svg?branch=main)](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/workflows/collaudo-p001-p080.yml)
[![P081–P100 su Linux e Windows](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/workflows/collaudo-p081-p100.yml/badge.svg?branch=main)](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/workflows/collaudo-p081-p100.yml)

Codice, test e istruzioni dei cento laboratori del libro di **Davide Iannella**. Per studenti, autodidatti con basi di programmazione e professionisti junior: programmazione, dati, reti, sistemi, sicurezza e intelligenza artificiale, con modelli ed esempi locali riproducibili.

## Iniziare

1. Scarica **Code → Download ZIP** ed estrai l’archivio, oppure clona il repository:

   ```text
   git clone https://github.com/davideiannella/100-progetti-informatica-pratica.git
   cd 100-progetti-informatica-pratica
   ```

2. Scegli un laboratorio nel [catalogo dei 100 progetti](docs/CATALOGO.md). Per un primo esercizio Python puoi partire da [P001](projects/P001/README.md).
3. Prepara l’[ambiente Linux, Windows o WSL](docs/AMBIENTI.md) e segui **Requisiti**, **Preparazione** e **Test** nel README del progetto. Esegui i comandi dalla cartella indicata: i linguaggi e le dipendenze cambiano fra i laboratori.

Alcuni progetti espongono solo funzioni e classi: il loro punto di ingresso eseguibile è la suite di test. Ogni README distingue l’avvio dimostrativo dalle verifiche.

## Dove trovare i materiali

| Percorso | Contenuto |
|---|---|
| [projects](projects) | Cento cartelle autonome, da `P001` a `P100`, con README, sorgenti e test |
| [Catalogo](docs/CATALOGO.md) | Titoli, linguaggi e collegamenti ai singoli laboratori |
| [Ambienti](docs/AMBIENTI.md) | Interpreti, compilatori, dipendenze e differenze fra sistemi |
| [collaudi](collaudi/README.md) | Esiti, log, versioni, provenienza e limiti delle prove |
| [tools](tools) | Script che coordinano i collaudi del repository |
| [SOURCE_SHA256.json](SOURCE_SHA256.json) | Impronte dei file sorgenti per controllarne l’integrità |

## Verifiche automatiche

| Workflow | Ambiente e perimetro |
|---|---|
| [P001–P080](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/workflows/collaudo-p001-p080.yml) | Ubuntu; strumenti e servizi distinti per gruppo di progetti |
| [P081–P100](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/workflows/collaudo-p081-p100.yml) | Ubuntu e Windows, ciascuno con Python 3.12 e 3.13 |

I badge mostrano lo stato del workflow. Per verificare una versione, apri il relativo run e controlla **commit, job e log**. La matrice P081–P100 ripete gli stessi 377 test distinti in quattro ambienti. Le prove Ubuntu di P001–P080 non attestano una verifica nativa Windows; simulazioni e dati sintetici restano entro il perimetro descritto nei README e nei [registri](collaudi/README.md).

## Versioni e segnalazioni

Conserva il commit associato alla copia che usi: `main` può cambiare. Per segnalare un problema indica progetto, commit, sistema operativo, versioni, comando e messaggio completo di errore, rimuovendo dati personali e credenziali.

## Licenza e libro

Il codice originale e la documentazione tecnica del repository sono **gratuiti**, con [licenza MIT](LICENSE), anche per uso commerciale nel rispetto delle sue condizioni. Le dipendenze conservano le proprie licenze. **Libro, copertine e altri materiali editoriali hanno diritti separati** e non sono concessi dalla licenza MIT del repository.
