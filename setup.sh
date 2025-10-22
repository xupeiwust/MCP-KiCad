#!/bin/bash
# Setup script for KiCad MCP Integration

set -e  # Exit on error

echo "======================================================================"
echo "KiCad MCP Integration - Setup Script"
echo "======================================================================"
echo

# Check Python version
echo "Checking Python version..."
python3 --version || {
    echo "Error: Python 3 not found"
    exit 1
}

# Create virtual environment
if [ -d "venv" ]; then
    echo "Virtual environment already exists"
else
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo "✓ Virtual environment created"
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip -q

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt -q
echo "✓ Dependencies installed"

# Create .env if it doesn't exist
if [ -f ".env" ]; then
    echo ".env file already exists"
else
    echo "Creating .env file..."
    cp .env.example .env
    echo "✓ .env file created"
    echo
    echo "⚠ IMPORTANT: Edit .env and add your ANTHROPIC_API_KEY"
    echo "  Get your key from: https://console.anthropic.com/"
fi

# Make scripts executable
echo "Making scripts executable..."
chmod +x kicad_mcp_server.py kicad_mcp_client.py test_server.py check_kicad.py

# Run environment check
echo
echo "======================================================================"
echo "Running environment check..."
echo "======================================================================"
echo
python check_kicad.py

echo
echo "======================================================================"
echo "Setup Complete!"
echo "======================================================================"
echo
echo "Next steps:"
echo
echo "1. Add your API key to .env file:"
echo "   nano .env"
echo
echo "2. Test in mock mode:"
echo "   source venv/bin/activate"
echo "   python test_server.py"
echo
echo "3. Or use with KiCad:"
echo "   - Open a PCB in KiCad PCBNew"
echo "   - Terminal 1: python kicad_mcp_server.py"
echo "   - Terminal 2: python kicad_mcp_client.py kicad_mcp_server.py"
echo
echo "See README.md for full documentation"
echo
