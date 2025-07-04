#!/bin/bash

# Check if running as root (sudo)
if [ "$EUID" -ne 0 ]; then
  echo "Please run this script with sudo or as root."
  exit 1
fi

# Detect OS type
OS=$(grep ID= /etc/os-release | cut -d= -f2 | tr -d '"')

echo "Detected OS: $OS"

# Install Python and pip based on OS
case "$OS" in
  ubuntu|debian)
    echo "Installing Python and pip for Debian/Ubuntu..."
    apt update && apt install -y python3 python3-pip python3-venv
    ;;
  alpine)
    echo "Installing Python and pip for Alpine Linux..."
    apk update
    apk add python3 py3-pip
    ;;
  centos|fedora|rhel)
    echo "Installing Python and pip for CentOS/Fedora/RHEL..."
    dnf install -y python3 pip
    ;;
  *)
    echo "Unsupported OS: $OS"
    exit 1
    ;;
esac

# Verify installation
if ! command -v python3 &> /dev/null; then
  echo "Python3 not found after installation. Aborting."
  exit 1
fi

if ! command -v pip3 &> /dev/null; then
  echo "pip3 not found after installation. Aborting."
  exit 1
fi

# Create symlink for python and pip (optional)
ln -sf /usr/bin/python3 /usr/bin/python || true
ln -sf /usr/bin/pip3 /usr/bin/pip || true

# Create project directory and cd into it
mkdir -p ~/myproject && cd ~/myproject

# Create a virtual environment
python -m venv env

# Activate the virtual environment
source env/bin/activate

# Update PATH to use virtual environment
export PATH="$PWD/env/bin:$PATH"

# Optional: Install numpy as a test package
pip install numpy

# Final check
python -c "import numpy; print('NumPy version:', numpy.__version__)" && echo "✅ Setup completed successfully!" || echo "❌ Something went wrong."
