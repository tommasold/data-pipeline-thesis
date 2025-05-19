#!/bin/bash

echo " Avvio port-forwarding verso i servizi PostgreSQL..."

# Primo DB (grezzo)
kubectl --kubeconfig ~/.airbyte/abctl/abctl.kubeconfig \
  -n airbyte-abctl port-forward svc/postgres-service 55432:5432 > /tmp/portforward_grezzo.log 2>&1 &

# Secondo DB (pulito)
kubectl --kubeconfig ~/.airbyte/abctl/abctl.kubeconfig \
  -n airbyte-abctl port-forward svc/postgres-clean-service 55433:5432 > /tmp/portforward_pulito.log 2>&1 &

echo "Port-forwarding attivato:"
echo " - DB grezzo:     localhost:55432"
echo " - DB pulito:     localhost:55433"
echo
echo " Lascia questo terminale aperto oppure monitora i log con:"
echo "   tail -f /tmp/portforward_grezzo.log"
echo "   tail -f /tmp/portforward_pulito.log"
