#!/bin/sh

set -e  # Exit on error

echo "🔍 Detecting Linux distribution..."

# Detect Linux flavor
if [ -f /etc/os-release ]; then
    . /etc/os-release
    LINUX_DIST=$ID
elif command -v lsb_release >/dev/null 2>&1; then
    LINUX_DIST=$(lsb_release -si | tr '[:upper:]' '[:lower:]')
else
    echo "⚠️ Unable to detect Linux distribution."
    exit 1
fi

echo "🐧 Detected Linux Distribution: $LINUX_DIST"

# Update package list and install Python/pip accordingly
case "$LINUX_DIST" in
    ubuntu|debian)
        echo "APT-based system detected (Debian/Ubuntu)"
        sudo apt update -y
        sudo apt install -y python3 python3-pip python3-venv
        ;;
    fedora|centos|rhel)
        echo "DNF/YUM-based system detected (Fedora/CentOS/RHEL)"
        if command -v dnf >/dev/null 2>&1; then
            sudo dnf install -y python3 python3-pip
        else
            sudo yum install -y python3 python3-pip
        fi
        ;;
    arch|manjaro)
        echo "Pacman-based system detected (Arch/Manjaro)"
        sudo pacman -Syu --noconfirm python python-pip
        ;;
    alpine)
        echo " Alpine Linux detected"
        apk update
        apk add --no-cache python3 py3-pip python3-virtualenv
        ;;
    *)
        echo "❌ Unsupported Linux distribution: $LINUX_DIST"
        echo "Please install Python manually or extend this script."
        exit 1
        ;;
esac

# Validate Python and pip installation
echo "🧪 Validating Python and pip versions..."
python3 --version || { echo "Python not installed properly."; exit 1; }
pip3 --version || { echo "pip not installed properly."; exit 1; }

# Setup Virtual Environment
echo "🧰 Creating Python virtual environment..."
python3 -m venv venv
source venv/bin/activate
echo "🔌 Virtual environment activated."

# Install numpy and pandas
echo "🧠 Installing numpy and pandas..."
pip install --upgrade pip
pip install numpy pandas

# Create and run test script
echo "🧪 Creating test script for numpy and pandas..."
cat > test_numpy_pandas.py <<EOF
import numpy as np
import pandas as pd

print("✅ NumPy version:", np.__version__)
print("✅ Pandas version:", pd.__version__)

# Test NumPy
arr = np.array([1, 2, 3])
print("NumPy array:", arr)

# Test Pandas
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Score': [90, 85, 92]
})
print("\nPandas DataFrame:")
print(df)
EOF

echo "🏃 Running test script..."
python test_numpy_pandas.py

echo "🎉 Setup complete! Python, pip, virtualenv, numpy, and pandas are working."