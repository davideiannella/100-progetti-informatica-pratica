from pathlib import Path
import yaml
root = Path(__file__).parents[1]
deployment, service = list(yaml.safe_load_all((root/'k8s/deployment.yaml').read_text()))
assert deployment['kind'] == 'Deployment' and deployment['spec']['replicas'] == 3
spec = deployment['spec']['template']
assert deployment['spec']['selector']['matchLabels'] == spec['metadata']['labels']
assert service['spec']['selector'] == spec['metadata']['labels']
c = spec['spec']['containers'][0]
assert c['image'] == 'p056-demo-api:1.0' and c['imagePullPolicy'] == 'Never'
assert c['readinessProbe']['httpGet']['path'] == '/ready'
assert c['livenessProbe']['httpGet']['path'] == '/health'
assert c['resources']['requests'] and c['resources']['limits']
assert service['spec']['ports'][0]['targetPort'] == c['ports'][0]['containerPort']
assert (root/'Dockerfile').is_file() and (root/'src/app.py').is_file()
print('P056 PASS: YAML, selettori, porte e probe coerenti; cluster non eseguito')
