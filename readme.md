# Monitoring App Python

Aplicação Flask de demonstração para praticar monitoramento com Prometheus e Grafana no Kubernetes.

## Arquitetura

```
Flask App (porta 5000)
    │
    └── /metrics ──► Prometheus (kube-prometheus-stack)
                          │
                          └──► Grafana
```

## Estrutura do Repositório

```
monitoring_app_python/
├── my_flask_app/
│   ├── k8s/
│   │   ├── deployment.yaml     # 2 réplicas do Flask
│   │   ├── service.yaml        # ClusterIP na porta 5000
│   │   └── ServiceMonitor.yaml # Configuração de scrape do Prometheus
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── readme.md               # Guia da aplicação Flask
└── readme.md                   # Este arquivo
```

## Pré-requisitos

- Cluster Kubernetes em execução (ex: minikube)
- `kubectl` instalado e configurado
- `Helm` instalado

## Instalação do kube-prometheus-stack

### 1. Adicionar repositório Helm

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
```

### 2. Criar namespace e instalar

```bash
kubectl create namespace monitoring

helm install kube-prometheus-stack prometheus-community/kube-prometheus-stack \
  --namespace monitoring \
  --set prometheus.prometheusSpec.serviceMonitorSelectorNilUsesHelmValues=false
```

> A flag `serviceMonitorSelectorNilUsesHelmValues=false` é necessária para que o Prometheus descubra ServiceMonitors em namespaces fora do `monitoring` (como o `default`, onde a aplicação roda).

### 3. Atualizar instalação existente

Caso o stack já esteja instalado sem a flag acima:

```bash
helm upgrade kube-prometheus-stack prometheus-community/kube-prometheus-stack \
  --namespace monitoring \
  --set prometheus.prometheusSpec.serviceMonitorSelectorNilUsesHelmValues=false
```

### 4. Verificar instalação

```bash
kubectl get pods -n monitoring
```

## Deploy da aplicação Flask

Veja [my_flask_app/readme.md](my_flask_app/readme.md) para instruções completas de build e deploy.
