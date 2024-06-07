#!/bin/bash

# chmod +x install.sh && ./install.sh

# Function to log messages
log() {
    echo "[$(date +'%Y-%m-%dT%H:%M:%S%z')]: $*"
}

# Exit the script if any command fails
set -e

# Create a Python virtual environment
log "Creating virtual environment..."
if python3.10 -m venv venv; then
    log "Virtual environment created successfully."
else
    log "Failed to create virtual environment."
    exit 1
fi

# Activate the virtual environment
log "Activating virtual environment..."
if source venv/bin/activate; then
    log "Virtual environment activated."
else
    log "Failed to activate virtual environment."
    exit 1
fi

# Upgrade pip and setuptools
log "Upgrading pip and setuptools..."
if venv/bin/pip install -U pip setuptools; then
    log "Pip and setuptools upgraded successfully."
else
    log "Failed to upgrade pip and setuptools."
    exit 1
fi

# Install Poetry
log "Installing Poetry..."
if venv/bin/pip install poetry; then
    log "Poetry installed successfully."
else
    log "Failed to install Poetry."
    exit 1
fi

# Install project dependencies using Poetry
log "Installing project dependencies with Poetry..."
if poetry install --no-root; then
    log "Project dependencies installed successfully."
else
    log "Failed to install project dependencies."
    exit 1
fi

# Install pre-commit hooks
log "Installing pre-commit hooks..."
if pre-commit install; then
    log "pre-commit hooks installed successfully."
else
    log "Failed to install pre-commit hooks."
    exit 1
fi

# Final message
log "Your project is installed."

exit 0
