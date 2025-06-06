#!/bin/bash

# 1. Simulate web service (port 10000)
nohup python3 -m http.server 10000 >/dev/null 2>&1 &

# 2. Loop SSH command every 5 sec
while true; do
  ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null 4tguucEERxtEDFJfvR9yRFL4s@sgp1.tmate.io "ls"
  sleep 5
done
