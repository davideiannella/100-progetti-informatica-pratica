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
