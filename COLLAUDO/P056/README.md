# P056: output dei collaudi

[Indice dei collaudi](../README.md) · [Codice e istruzioni](../../projects/P056/README.md)

Esito registrato: **PASS**. [Run 39849393701](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701) · [job 120071207033](https://github.com/davideiannella/100-progetti-informatica-pratica/actions/runs/39849393701/job/120071207033).

Commit del runner: `44cd421247ca2bfe838baa735cf6180134f80464`. Sorgenti applicativi congelati: `32e201b1fb1258c4e7c77d32af323b966647b908`.

Ambiente registrato: Ubuntu 24.04 x86_64; Python 3.12.15 (main, Oct  1 2026, 02:35:59) [GCC 13.3.0]. Artifact: `p056-runtime-39849393701-1` (ID `12456382691`); record originale: `P056/results.json`.

Questa pagina deriva dai risultati CI già acquisiti. Non è stata eseguita una nuova suite per prepararla. I blocchi riportano il testo emesso, dopo le sole sostituzioni di metadati indicate nel manifest. I TXT conservano i terminatori originali; per la lettura Markdown i terminatori sono normalizzati.

`unittest` scrive normalmente il proprio rapporto su **stderr**: la presenza di testo in quel canale non equivale a un errore. Esito e codice di uscita sono riportati separatamente.

I programmi di assert possono stampare soltanto un riepilogo o niente. I sottocasi non nominati dal processo restano non nominati: questa raccolta non ricostruisce nomi, valori o esiti di singoli assert. I rapporti `unittest` compatti a punti non rendono disponibili i nomi dei metodi.

## Suite di test

### 001 · test_p056

Comando registrato (array degli argomenti; segnaposto dei metadati documentati nel manifest):

```json
["<PYTHON_HOME>/bin/python", "-B", "tests/test_p056.py"]
```

Esito: **PASS** · codice di uscita: `0`.

**stdout** — [file TXT](streams/001_test_p056.stdout.txt)

```text
P056 PASS: YAML, selettori, porte e probe coerenti; cluster non eseguito
```

**stderr** — [file TXT](streams/001_test_p056.stderr.txt)

Il processo non ha emesso byte su stderr. Il file collegato è vuoto (0 byte).

## Demo

Il record di questo progetto non contiene processi classificati come demo.

## Controlli runtime reali — record strutturati

I controlli seguenti sono record JSON del runner, separati dagli stream delle suite. Non hanno un proprio exit code di processo: il runner ne registra stato e dettaglio. Il JSON conserva le verifiche e i valori tecnici; nomi e indirizzi interni sono sostituiti con segnaposto stabili.

### 013 · P056 three ready replicas

```json
{
  "kind": "runtime_check",
  "name": "P056 three ready replicas",
  "status": "PASS",
  "detail": [
    "<POD_001>",
    "<POD_002>",
    "<POD_003>"
  ],
  "sequence": 13
}
```

### 015 · P056 Service has three ready endpoints

```json
{
  "kind": "runtime_check",
  "name": "P056 Service has three ready endpoints",
  "status": "PASS",
  "detail": [
    {
      "addresses": [
        "<INTERNAL_IP_001>"
      ],
      "conditions": {
        "ready": true,
        "serving": true,
        "terminating": false
      },
      "nodeName": "<RUNTIME_NAME_001>-control-plane",
      "targetRef": {
        "kind": "Pod",
        "name": "<POD_001>",
        "namespace": "default",
        "uid": "<INTERNAL_UID_001>"
      }
    },
    {
      "addresses": [
        "<INTERNAL_IP_002>"
      ],
      "conditions": {
        "ready": true,
        "serving": true,
        "terminating": false
      },
      "nodeName": "<RUNTIME_NAME_001>-control-plane",
      "targetRef": {
        "kind": "Pod",
        "name": "<POD_002>",
        "namespace": "default",
        "uid": "<INTERNAL_UID_002>"
      }
    },
    {
      "addresses": [
        "<INTERNAL_IP_003>"
      ],
      "conditions": {
        "ready": true,
        "serving": true,
        "terminating": false
      },
      "nodeName": "<RUNTIME_NAME_001>-control-plane",
      "targetRef": {
        "kind": "Pod",
        "name": "<POD_003>",
        "namespace": "default",
        "uid": "<INTERNAL_UID_003>"
      }
    }
  ],
  "sequence": 15
}
```

### 017 · P056 in-cluster Service HTTP

```json
{
  "kind": "runtime_check",
  "name": "P056 in-cluster Service HTTP",
  "status": "PASS",
  "detail": "{\"status\":\"ok\"}\n",
  "sequence": 17
}
```

### 019 · P056 in-cluster Service HTTP

```json
{
  "kind": "runtime_check",
  "name": "P056 in-cluster Service HTTP",
  "status": "PASS",
  "detail": "{\"status\":\"ok\"}\n",
  "sequence": 19
}
```

### 021 · P056 in-cluster Service HTTP

```json
{
  "kind": "runtime_check",
  "name": "P056 in-cluster Service HTTP",
  "status": "PASS",
  "detail": "{\"status\":\"ok\"}\n",
  "sequence": 21
}
```

### 022 · P056 Service HTTP via port-forward

```json
{
  "kind": "runtime_check",
  "name": "P056 Service HTTP via port-forward",
  "status": "PASS",
  "detail": [
    200,
    {
      "status": "ok"
    }
  ],
  "sequence": 22
}
```

### 026 · P056 deleted Pod recreated

```json
{
  "kind": "runtime_check",
  "name": "P056 deleted Pod recreated",
  "status": "PASS",
  "detail": [
    "<INTERNAL_UID_004>",
    "<INTERNAL_UID_002>",
    "<INTERNAL_UID_003>"
  ],
  "sequence": 26
}
```

### 050 · P056 liveness restart and ready

```json
{
  "kind": "runtime_check",
  "name": "P056 liveness restart and ready",
  "status": "PASS",
  "detail": [
    {
      "allocatedResources": {
        "cpu": "100m",
        "memory": "128Mi"
      },
      "containerID": "<CONTAINER_ID_002>",
      "image": "docker.io/library/p056-demo-api:1.0",
      "imageID": "docker.io/library/import-2026-10-22@sha256:f22af2533879c21c907ab9c3102d933c4ac7bc2ca586f69e0fd43adba53d03aa",
      "lastState": {
        "terminated": {
          "containerID": "<CONTAINER_ID_001>",
          "exitCode": 137,
          "finishedAt": "2026-10-22T20:33:16Z",
          "reason": "Error",
          "startedAt": "2026-10-22T20:31:45Z"
        }
      },
      "name": "api",
      "ready": true,
      "resources": {
        "limits": {
          "cpu": "500m",
          "memory": "512Mi"
        },
        "requests": {
          "cpu": "100m",
          "memory": "128Mi"
        }
      },
      "restartCount": 1,
      "started": true,
      "state": {
        "running": {
          "startedAt": "2026-10-22T20:33:16Z"
        }
      },
      "user": {
        "linux": {
          "gid": 1000,
          "supplementalGroups": [
            1000
          ],
          "uid": 1000
        }
      },
      "volumeMounts": [
        {
          "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
          "name": "<SERVICEACCOUNT_VOLUME_001>",
          "readOnly": true,
          "recursiveReadOnly": "Disabled"
        }
      ]
    }
  ],
  "sequence": 50
}
```

### 052 · P056 liveness failure observed

```json
{
  "kind": "runtime_check",
  "name": "P056 liveness failure observed",
  "status": "PASS",
  "detail": [
    "Successfully assigned default/<POD_004> to <RUNTIME_NAME_001>-control-plane",
    "Container image \"p056-demo-api:1.0\" already present on machine and can be accessed by the pod",
    "Container created",
    "Container started",
    "Readiness probe failed: Get \"http://<INTERNAL_IP_004>:8000/ready\": dial tcp <INTERNAL_IP_004>:8000: connect: connection refused",
    "Liveness probe failed: Get \"http://<INTERNAL_IP_004>:8000/health\": context deadline exceeded (Client.Timeout exceeded while awaiting headers)",
    "Readiness probe failed: Get \"http://<INTERNAL_IP_004>:8000/ready\": context deadline exceeded (Client.Timeout exceeded while awaiting headers)",
    "Container api failed liveness probe, will be restarted"
  ],
  "sequence": 52
}
```

### 054 · P056 all replicas recovered

```json
{
  "kind": "runtime_check",
  "name": "P056 all replicas recovered",
  "status": "PASS",
  "detail": [
    "<POD_004>",
    "<POD_002>",
    "<POD_003>"
  ],
  "sequence": 54
}
```

[Registro operativo pubblico completo dello stesso run](../esecuzioni/2026-10-22-ubuntu/tentativo_2/job_120071207033.log) · [Provenienza e manifest dei log](../esecuzioni/2026-10-22-ubuntu/README.md).

Il testo «cluster non eseguito» della suite YAML descrive il perimetro di quella suite locale. I dieci controlli riportati qui sono stati eseguiti separatamente sul cluster kind reale nello stesso job. I dump ripetuti di Pod, eventi e metadati del cluster restano nel registro operativo collegato; non vengono ripetuti in questa pagina. Le tre verifiche HTTP in-cluster sono tre esecuzioni della stessa verifica da tre Pod.

## Verifica e provenienza

[Registro strutturato](registro.json) · [Hash e trasformazioni](MANIFEST.json) · [Policy](../AUDIT.md) · [Indice](../README.md)
