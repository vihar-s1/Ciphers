#!/usr/bin/env bash

VENV_DIR=""

log() {
    local level=$1
    local color=$2
    shift 2
    printf "\e[${color}m[%s] [%s] %s\e[0m\n" "$(date '+%Y-%m-%d %H:%M:%S')" "${level}" "$*"
}

log_info() {
    log "INFO" "32" "$@"
}

log_warn() {
    log "WARN" "33" "$@"
}

log_error() {
    log "ERROR" "31" "$@"
}

activate_venv() {
    if [ -x ".venv" ]; then
        VENV_DIR=".venv"
        log_info "Found existing virtual environment directory: .venv"
    elif [ -x "venv" ]; then
        VENV_DIR="venv"
        log_info "Found existing virtual environment directory: venv"
    fi

    # Create a virtual environment
    if [ -z "${VENV_DIR}" ]; then
        if [ -x "*.iml" ] || [ -d ".idea" ]; then
            # IntelliJ system so use "venv"
            VENV_DIR="venv"
            log_info "IntelliJ system detected, setting virtual environment directory to: venv"
        else
            VENV_DIR=".venv"
            log_info "Setting virtual environment directory to: .venv"
        fi
        log_info "Creating virtual environment in directory: ${VENV_DIR}"
        python3 -m venv "${VENV_DIR}"
    fi

    # Activate the virtual environment if inactive
    # VIRTUAL_ENV will be set if virtual env is active
    if [ -z "${VIRTUAL_ENV}" ]; then
        log_info "Activating virtual environment..."
        source "${VENV_DIR}/bin/activate"
    else
        log_info "Active virtual environment found: ${VIRTUAL_ENV}"
    fi
}

### MAIN SCRIPT ###

activate_venv

# Check if pip is outdated and upgrade if necessary
log_info "Checking if pip is up to date..."
current_version=$(pip --version | awk '{print $2}')
latest_version=$(pip install --upgrade pip --dry-run | grep -oe '(.*)')

if [ "(${current_version})" != "$latest_version" ]; then
    log_warn "pip is outdated (current: $current_version, latest: $latest_version). Upgrading pip..."
    pip install --upgrade pip -q
else
    log_info "pip is up to date (version: $current_version)."
fi

# Install the required packages
if [ -f "requirements.txt" ]; then
    log_info "Installing required packages from requirements.txt..."
    pip3 install -r requirements.txt -q
else
    log_warn "requirements.txt not found. Skipping package installation."
fi

# Install the package in editable mode
log_info "Installing the package in editable mode..."
pip3 install -e . -q
# remove any extra files generated
rm -rf ./*.egg-info

# Run the tests
log_info "Running the tests..."
if command -v pytest &> /dev/null; then
    if pytest; then
        log_info "Tests ran successfully."
    else
        log_error "Tests failed."
    fi
else
    log_warn "pytest command not found. Skipping tests."
fi

# Deactivate the virtual environment
log_info "Deactivating the virtual environment..."
deactivate

log_info "Project setup complete"

echo -e "\nRun following Command to activate the virtual environment if not already...\nsource ${VENV_DIR}/bin/activate"