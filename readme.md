# Setup do Prometheus com kube-prometheus-stack

Este documento fornece um guia passo a passo para configurar o Prometheus no Kubernetes usando o kube-prometheus-stack.

## Pré-requisitos

- Um cluster Kubernetes em execução.
- `kubectl` instalado e configurado para se conectar ao seu cluster.
- `Helm` instalado.

## Passo 1: Adicionar o repositório do Helm

Adicione o repositório do Helm para o kube-prometheus-stack:

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts

helm repo update

kubectl create namespace monitoring

helm install kube-prometheus-stack prometheus-community/

kube-prometheus-stack --namespace monitoring
```
