#!/bin/bash
# Wrapper to run KiCad MCP Server inside Flatpak container
# This allows the server to access pcbnew module

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FLATPAK_ID="org.kicad.KiCad"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "======================================================================"
echo "KiCad MCP Server - Flatpak Launcher"
echo "======================================================================"
echo

# Check if Flatpak KiCad is installed
if ! flatpak list | grep -q "$FLATPAK_ID"; then
    echo -e "${RED}Error: KiCad Flatpak not found${NC}"
    echo "Install with: flatpak install flathub org.kicad.KiCad"
    exit 1
fi

# Check which server script to use
if [ -f "$SCRIPT_DIR/kicad_mcp_server_extended.py" ]; then
    SERVER_SCRIPT="kicad_mcp_server_extended.py"
    echo -e "${GREEN}Using extended server with fabrication tools${NC}"
elif [ -f "$SCRIPT_DIR/kicad_mcp_server.py" ]; then
    SERVER_SCRIPT="kicad_mcp_server.py"
    echo -e "${YELLOW}Using basic server (no fabrication tools)${NC}"
else
    echo -e "${RED}Error: No server script found${NC}"
    exit 1
fi

# Check if dependencies are installed in Flatpak
echo "Checking dependencies in Flatpak..."
if ! flatpak run --command=python3 "$FLATPAK_ID" -c "import mcp" 2>/dev/null; then
    echo -e "${YELLOW}MCP dependencies not installed in Flatpak${NC}"
    echo "Run: ./kicad_flatpak_setup.sh"
    echo
    read -p "Install now? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        ./kicad_flatpak_setup.sh
    else
        exit 1
    fi
fi

echo -e "${GREEN}All checks passed${NC}"
echo
echo "Starting MCP server inside Flatpak container..."
echo "Server script: $SERVER_SCRIPT"
echo
echo "Note: Make sure you have a PCB open in KiCad PCBNew"
echo "Press Ctrl+C to stop the server"
echo
echo "======================================================================"

# Run the server inside Flatpak with filesystem access
# --filesystem=host gives access to the entire host filesystem
# This allows the server to write output files
flatpak run \
    --command=python3 \
    --filesystem=host \
    --share=network \
    --env=PYTHONUNBUFFERED=1 \
    "$FLATPAK_ID" \
    "$SCRIPT_DIR/$SERVER_SCRIPT"
