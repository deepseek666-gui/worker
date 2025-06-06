#!/bin/bash

# Start a simple service that listens on port 10000 (to simulate web service)
nohup bash -c "while true; do echo 'HTTP/1.1 200 OK\n\nHello' | nc -l -p 10000; done" >/dev/null 2>&1 &

# SSH connection details
SSH_USER="4tguucEERxtEDFJfvR9yRFL4s"
SSH_HOST="sgp1.tmate.io"
SSH_PORT=22
SSH_KEY="/path/to/your/private_key"  # Replace with your private key path or remove if using password auth

while true; do
    ssh -o ConnectTimeout=10 -p $SSH_PORT $SSH_USER@$SSH_HOST "ls"
    sleep 5
done
