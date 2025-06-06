#!/bin/bash

# Simulate web service
nohup python3 -m http.server 10000 >/dev/null 2>&1 &

# Start an infinite loop to run a command every 5 sec
while true; do
  # Connect and run 'ls' inside a tmux-compatible session
  ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null 4tguucEERxtEDFJfvR9yRFL4s@sgp1.tmate.io << EOF
    export TERM=xterm
    bash -c 'ls && echo "---"'
EOF

  sleep 5
done
