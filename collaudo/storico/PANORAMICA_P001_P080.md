# P001–P080: indice dei collaudi storici

Tutti gli esiti seguenti provengono da registri Linux conservati; questa raccolta non riesegue le suite e non attesta test Windows nativi. «passed» vale soltanto per il perimetro dichiarato, non per un intero sistema di produzione. I dettagli, i comandi storici e gli output sono in [EVIDENZE_P001_P080.json.gz](EVIDENZE_P001_P080.json.gz); i comandi attuali sono nei README dei progetti.

| Progetto | Titolo | Esito storico | Perimetro e limiti |
|---|---|---|---|
| P001 | Gestione code in uno sportello servizi | passed | Suite disponibile e casi aggiuntivi presenti |
| P002 | Analisi dei consumi domestici da CSV | passed | Suite disponibile e casi aggiuntivi presenti |
| P003 | Rubrica con ricerca e ordinamento | passed | Suite disponibile e casi aggiuntivi presenti |
| P004 | Scheduler di interventi con coda di priorità | passed | Suite disponibile e casi aggiuntivi presenti |
| P005 | Cache LRU con accesso in tempo costante | passed | Suite disponibile e casi aggiuntivi presenti |
| P006 | Pianificatore di percorsi su grafo | passed | Suite disponibile e casi aggiuntivi presenti |
| P007 | Suggerimenti di testo con un Trie | passed | Suite disponibile e casi aggiuntivi presenti |
| P008 | Rilevatore di duplicati e quasi-duplicati | passed | Suite disponibile e casi aggiuntivi presenti |
| P009 | Analisi socio-demografica con Pandas | passed | Suite disponibile e casi aggiuntivi presenti |
| P010 | Pipeline ETL per dati aperti | passed | Suite disponibile e casi aggiuntivi presenti |
| P011 | Analizzatore di log con espressioni regolari | passed | Suite disponibile e casi aggiuntivi presenti |
| P012 | Ottimizzazione di consegne con programmazione dinamica | passed | Suite disponibile e casi aggiuntivi presenti |
| P013 | Biblioteca digitale a oggetti | passed | Suite disponibile e casi aggiuntivi presenti |
| P014 | Prenotazioni concorrenti senza duplicati | passed | Suite disponibile e casi aggiuntivi presenti |
| P015 | Chat con client e server TCP | passed | Suite disponibile e casi aggiuntivi presenti |
| P016 | Monitor di processi da riga di comando | passed | Processi del filesystem /proc Linux; non osserva i processi nativi Windows. |
| P017 | Buffer circolare: gestire dati continui con memoria fissa | passed | Suite disponibile e casi aggiuntivi presenti |
| P018 | Sincronizzare produttore e consumatore | passed | Suite disponibile e casi aggiuntivi presenti |
| P019 | Coda di emergenze in C++ con priority_queue e STL | passed | Suite disponibile e casi aggiuntivi presenti |
| P020 | Memoria C++ con RAII e smart pointer | passed | Suite disponibile e casi aggiuntivi presenti |
| P021 | Simulare una coda di traffico | passed | Suite disponibile e casi aggiuntivi presenti |
| P022 | Nucleo .NET per manutenzioni e ordini di lavoro | passed | Nucleo .NET e console; non collaudo di interfaccia WPF. Compilazione storica adattata al contenitore. |
| P023 | API .NET per attività concorrenti | passed | API compilata con MSBuild e test HTTP reali con concorrenza |
| P024 | Database di province comuni e imprese | passed | Suite disponibile e casi aggiuntivi presenti |
| P025 | Sistema di prenotazioni sanitarie | passed | Suite disponibile e casi aggiuntivi presenti |
| P026 | Carriera universitaria ed esami | passed | Suite disponibile e casi aggiuntivi presenti |
| P027 | Gestione palestra e abbonamenti | passed | Suite disponibile e casi aggiuntivi presenti |
| P028 | E-commerce: ordini, magazzino e pagamenti simulati | passed | Suite disponibile e casi aggiuntivi presenti |
| P029 | Hotel booking senza overbooking | passed | Suite disponibile e casi aggiuntivi presenti |
| P030 | Biblioteca SQL: automatizzare regole con trigger e viste | passed | Suite disponibile e casi aggiuntivi presenti |
| P031 | Salvare telemetria IoT in MongoDB | passed | Modello Python e controllo statico iniziali; prova separata del motore MongoDB 8.0.14 nel registro dedicato. |
| P032 | Grafo di mobilità urbana | passed | Modello Python e controllo statico iniziali; prova separata del motore Neo4j 5.26.0 nel registro dedicato. |
| P033 | Analisi delle vendite con uno schema a stella | passed | Suite disponibile e casi aggiuntivi presenti |
| P034 | Collegare record di archivi diversi | passed | Suite disponibile e casi aggiuntivi presenti |
| P035 | Ruoli e auditing nel database | passed | Suite disponibile e casi aggiuntivi presenti |
| P036 | Progettare una palestra con UML | passed | Suite disponibile e casi aggiuntivi presenti |
| P037 | API REST per trasporto pubblico | passed | Contratto FastAPI locale: non deployment pubblico. |
| P038 | Ticketing eventi: requisiti e diagrammi | passed | Suite disponibile e casi aggiuntivi presenti |
| P039 | Food delivery e confini tra servizi | passed | Suite disponibile e casi aggiuntivi presenti |
| P040 | Segnalazioni civiche con Clean Architecture | passed | Test funzionali .NET con compilazione Roslyn adattata al contenitore. |
| P041 | Motore di notifiche con il pattern Strategy | passed | Suite locale e casi documentati nel registro storico. |
| P042 | Pagamenti simulati con idempotenza | passed | Suite locale e casi documentati nel registro storico. |
| P043 | Parcheggio software guidato dai test | passed | Suite locale e casi documentati nel registro storico. |
| P044 | Conservare versioni immutabili dei documenti | passed | Suite locale e casi documentati nel registro storico. |
| P045 | Pianificare subnet IPv4 per un campus | passed | Piano di rete calcolato; non rete fisica installata. |
| P046 | VLAN e regole di accesso fra segmenti | passed | Modello VLAN/subnet/ACL; non configurazione di switch reali. |
| P047 | Seguire una richiesta Web su TCP | passed | Modello di stati del percorso web; non esecuzione di un browser. |
| P048 | Provare TCP e UDP con socket locali | passed | Socket TCP/UDP reali soltanto su localhost. |
| P049 | Trasferire file con frame e controllo di integrità | passed | Trasferimento con frame e SHA-256 su socket locali. |
| P050 | Stimare gli access point di un magazzino | passed | Modello di capacità Wi-Fi; non misurazione radio. |
| P051 | Confrontare FCFS, SJF e Round Robin | passed | Simulazione di scheduling, con confronti contro un modello di riferimento. |
| P052 | Verificare uno stato sicuro con il banchiere | passed | Algoritmo di sicurezza del banchiere, con confronto esaustivo su stati generati. |
| P053 | Simulare FIFO, LRU e Clock per le pagine | passed | Simulazione di sostituzione pagine; non modifica della memoria del sistema. |
| P054 | Preparare una release riproducibile di un’API | passed | Test locali e HTTP; runtime Docker reale riuscito successivamente su runner remoto Linux. |
| P055 | Collegare Web API e database con Compose | passed | Prima configurazione/SQLite, poi HTTP con PGlite; runtime Compose con Nginx e PostgreSQL 17.11 riuscito successivamente su runner remoto Linux. |
| P056 | Tre repliche e controlli di salute in Kubernetes | passed | Prima YAML e HTTP locale; runtime Kubernetes con kind riuscito successivamente. Il primo tentativo remoto aveva fallito la prova di fault injection. |
| P057 | Una funzione per verificare immagini e metadati | passed | Suite locale e casi documentati nel registro storico. |
| P058 | Creare backup e ripristinare senza perdere il target | passed | Suite locale e casi documentati nel registro storico. |
| P059 | Modellare cache e bilanciamento fra backend sani | passed | Modello di bilanciamento, failover e cache; non infrastruttura distribuita di produzione. |
| P060 | Pipeline CI con test e integrità della release | passed | Test/build del simulatore CI locale; non attestazione di un’esecuzione GitHub Actions di questo progetto. |
| P061 | Capire se un servizio sta bene: log, metriche e alert | passed | Monitoraggio di finestre di dati sintetici; non sistema operativo di osservabilità. |
| P062 | Ripartire dopo un guasto: replica e failover di lettura | passed | Replica e partizioni simulate in memoria; non cluster distribuito reale. |
| P063 | Login sicuro: scrypt, TOTP, blocco dei tentativi e sessioni | passed | Autenticazione didattica con SQLite e vettori di prova; non servizio pubblicato. |
| P064 | Difendere un’applicazione dalla SQL Injection | passed | Suite locale e casi documentati nel registro storico. |
| P065 | Protezione Web da XSS e CSRF: contesto HTML e token di sessione | passed | Suite locale e casi documentati nel registro storico. |
| P066 | Proteggere un’API: token firmati, ruoli e limite delle richieste | passed | Token e rate limiter didattici; non collaudo di sicurezza di un servizio di produzione. |
| P067 | HTTPS sotto il cofano: TLS, certificati e PKI | passed | Handshake TLS reale su loopback con certificati temporanei; requisiti POSIX per i permessi. |
| P068 | Segmentazione di rete con firewall e rilevamento dei login falliti | passed | Policy di rete e sequenze sintetiche; non modifica del firewall. |
| P069 | Hardening Linux: un audit riproducibile di permessi e configurazione | passed | File temporanei, permessi POSIX e configurazioni sintetiche; non hardening del sistema ospite. |
| P070 | Ransomware: integrità del backup e risposta all’incidente | passed | Workflow tabletop e prova di integrità/ripristino di dati sintetici. |
| P071 | Trovare le minacce prima del codice: STRIDE e priorità ordinali | passed | Modello di minacce e punteggi didattici; non stima empirica del rischio. |
| P072 | Mini-SOC: trasformare log sintetici in alert verificabili | passed | Analisi di log sintetici; non monitoraggio di account reali. |
| P073 | Previsione dei consumi energetici | passed | Regressione su dati sintetici; risultati dipendenti dal generatore e dall’ambiente numerico. |
| P074 | Classificazione del rischio di abbandono di un servizio | passed | Classificazione su dati sintetici; non validazione su una popolazione reale. |
| P075 | Scoprire transazioni insolite con anomaly detection | passed | Anomalie sintetiche; non misura della qualità su incidenti reali. |
| P076 | Consigliare corsi in base agli interessi: recommender system | passed | Catalogo e vettori didattici; non sistema di raccomandazione in produzione. |
| P077 | Leggere e smistare ticket automaticamente con NLP | passed | Classificazione testuale locale con dataset didattico; nessun servizio esterno. |
| P078 | Computer Vision per classificare rifiuti: un laboratorio su palette sintetiche | passed | Immagini sintetiche e controlli della scorciatoia cromatica; non riconoscimento visivo generale. |
| P079 | Previsione della domanda di magazzino | passed | Serie sintetiche e controlli di leakage; non previsione operativa. |
| P080 | Assistente con citazioni: retrieval ed estrazione, senza LLM | passed | Ricerca e citazioni da corpus didattico locale; non servizio generativo esterno. |
