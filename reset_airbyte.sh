#!/bin/bash

echo "▶ Restarting Airbyte components..."

kubectl --kubeconfig ~/.airbyte/abctl/abctl.kubeconfig -n airbyte-abctl rollout restart deployment airbyte-abctl-server
kubectl --kubeconfig ~/.airbyte/abctl/abctl.kubeconfig -n airbyte-abctl rollout restart deployment airbyte-abctl-worker
kubectl --kubeconfig ~/.airbyte/abctl/abctl.kubeconfig -n airbyte-abctl rollout restart deployment airbyte-abctl-webapp

echo " Waiting for pods to become ready..."
sleep 60

kubectl --kubeconfig ~/.airbyte/abctl/abctl.kubeconfig -n airbyte-abctl get pods

echo " Restart complete. Airbyte should be accessible at http://localhost:8000"
