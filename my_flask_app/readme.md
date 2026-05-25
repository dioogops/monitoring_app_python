# Flask App com Métricas Prometheus

Aplicação Flask simples que expõe métricas para o Prometheus via `/metrics` e possui rotas que retornam diferentes códigos HTTP — útil para testar alertas, dashboards e regras de monitoramento.

## Endpoints

| Rota            | Status | Descrição               |
|-----------------|--------|-------------------------|
| `/`             | 200    | Página inicial          |
| `/success`      | 200    | Simulação de resposta OK |
| `/client-error` | 400    | Simulação de erro 4xx   |
| `/server-error` | 500    | Simulação de erro 5xx   |
| `/metrics`      | 200    | Métricas do Prometheus  |

## Estrutura

```
my_flask_app/
├── k8s/
│   ├── deployment.yaml     # 2 réplicas
│   ├── service.yaml        # ClusterIP na porta 5000
│   └── ServiceMonitor.yaml # Configuração de scrape do Prometheus
├── app.py
├── Dockerfile
└── requirements.txt
```

## Desenvolvimento local (sem Docker)

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Acesse em: `http://localhost:5000`

## Build e deploy no minikube

```bash
minikube start

# Aponta o Docker para o daemon do minikube (necessário para o kubectl encontrar a imagem)
eval $(minikube docker-env)

docker build -t my-flask-app .
kubectl apply -f k8s/
```

## Verificação após deploy

```bash
# Checar se os pods estão rodando
kubectl get pods -l app=flask-app

# Expor o serviço localmente e testar os endpoints
kubectl port-forward svc/flask-app 5000:5000
curl http://localhost:5000/success
curl http://localhost:5000/client-error
curl http://localhost:5000/server-error
curl http://localhost:5000/metrics

# Confirmar que o ServiceMonitor foi criado
kubectl get servicemonitor flask-app-monitor -n default
```

## Nota sobre o ServiceMonitor

O `ServiceMonitor` reside no namespace `default` — o mesmo namespace da aplicação, não do Prometheus. Para que o Prometheus (instalado no namespace `monitoring`) descubra esse ServiceMonitor, o kube-prometheus-stack precisa da flag:

```
--set prometheus.prometheusSpec.serviceMonitorSelectorNilUsesHelmValues=false
```

Veja o [readme raiz](../readme.md) para o comando completo de instalação.
