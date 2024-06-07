#!/bin/bash

# chmod +x update.sh && ./update.sh

# Function to log messages
log() {
    echo "[$(date +'%Y-%m-%dT%H:%M:%S%z')]: $*"
}

# Exit the script if any command fails
set -e

# Set the project URL
PROJECT_URL="https://github.com/lizzypokerface/ipynb-proj-setup"

# Ensure we are on the main branch
log "Checking out the main branch..."
if git checkout main; then
    log "Checked out to main branch."
else
    log "Failed to check out to main branch."
    exit 1
fi

# Fetch changes from the remote repository
log "Fetching changes from the remote repository..."
if git fetch origin; then
    log "Fetched changes successfully."
else
    log "Failed to fetch changes from the remote repository."
    exit 1
fi

# Pull changes from the remote main branch
log "Pulling changes from the remote main branch..."
if git pull origin main; then
    log "Pulled changes from the remote main branch successfully."
else
    log "Failed to pull changes from the remote main branch."
    exit 1
fi

# Final message
log "Your local main branch is up to date."

exit 0
