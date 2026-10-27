# Struttura del repository

[Pagina principale](../README.md) · [Catalogo](CATALOGO.md) · [Collaudi](../collaudo/README.md)

## Percorso di lettura

1. Scegli un laboratorio nel catalogo.
2. Apri `projects/Pnnn/README.md` e prepara l’ambiente indicato.
3. Consulta `collaudo/Pnnn/README.md` per confrontare comandi, esiti e output con le prove documentate.

## Cartelle e responsabilità

| Percorso | Contenuto |
|---|---|
| [projects](../projects/README.md) | Sorgenti, test, dati di esempio e istruzioni dei cento laboratori |
| [collaudo](../collaudo/README.md) | Un solo indice e cento cartelle di risultati, da P001 a P100 |
| [docs](README.md) | Catalogo, ambienti e guida all’organizzazione |
| [tools](../tools/README.md) | Runner dei collaudi e strumenti di verifica |
| [.github/workflows](../.github/workflows) | Automazioni GitHub Actions |

I workflow restano distinti perché usano strumenti e ambienti diversi. I risultati si consultano tutti nella stessa cartella collaudo. I file di log e le impronte dei sorgenti conservano la provenienza delle prove originali.

## File delle dipendenze condivise

Nella cartella principale trovi anche [requirements-p061-p080.txt](../requirements-p061-p080.txt) e [requirements-p081-p100.txt](../requirements-p081-p100.txt). Elencano i pacchetti Python e le versioni usati da più laboratori; il secondo serve anche al collaudo completo P081–P100.

Gli intervalli nei nomi identificano gli ambienti condivisi di questi progetti. Le dieci sezioni tematiche del libro restano quelle del catalogo.

Per svolgere un solo progetto, segui i requisiti del suo README. I comandi comuni sono nella [guida agli ambienti](AMBIENTI.md#dipendenze-python).
