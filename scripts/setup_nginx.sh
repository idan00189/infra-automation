#!/bin/bash
# scripts/setup_nginx.sh

LOG_FILE="../logs/provisioning.log"

echo "Starting Nginx installation..." | tee -a "$LOG_FILE"

# Check if Nginx is installed
if command -v nginx > /dev/null 2>&1; then
    echo "Nginx is already installed." | tee -a "$LOG_FILE"
else
    echo "Installing Nginx..." | tee -a "$LOG_FILE"
    # For simulation, we use sleep to mimic an installation process.
    sleep 2
    # Uncomment the following line for an actual install on Ubuntu:
    # sudo apt-get update && sudo apt-get install -y nginx
    echo "Nginx installation simulated successfully." | tee -a "$LOG_FILE"
fi

echo "Nginx setup completed." | tee -a "$LOG_FILE"