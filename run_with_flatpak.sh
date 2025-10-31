#!/bin/bash
#
# Launch KiCad MCP Server inside Flatpak
#
# This script runs the MCP server using KiCad's Python environment
# inside the Flatpak container. It provides filesystem access to your
# home directory so the server can read/write PCB files.
#
# Usage:
#   ./run_with_flatpak.sh [server_script]
#
# Examples:
#   ./run_with_flatpak.sh                           # Uses extended server by default
#   ./run_with_flatpak.sh kicad_mcp_server.py      # Use basic server
#   ./run_with_flatpak.sh kicad_mcp_server_extended.py  # Use extended server
#

set -e  # Exit on error

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Determine which server to run
SERVER_SCRIPT="${1:-kicad_mcp_server_extended.py}"

# Check if the server script exists
if [ ! -f "$SCRIPT_DIR/$SERVER_SCRIPT" ]; then
    echo "Error: Server script not found: $SCRIPT_DIR/$SERVER_SCRIPT"
    echo ""
    echo "Available servers:"
    echo "  - kicad_mcp_server.py (basic - 4 tools)"
    echo "  - kicad_mcp_server_extended.py (extended - 12 tools, recommended)"
    exit 1
fi

# Check if Flatpak KiCad is installed
if ! flatpak list | grep -q org.kicad.KiCad; then
    echo "Error: KiCad Flatpak not found"
    echo ""
    echo "Install KiCad Flatpak with:"
    echo "  flatpak install flathub org.kicad.KiCad"
    exit 1
fi

# Check if dependencies are installed in Flatpak
echo "Checking Flatpak dependencies..."
if ! flatpak run --command=python3 org.kicad.KiCad -c "import mcp" 2>/dev/null; then
    echo ""
    echo "Warning: MCP dependencies not installed in Flatpak"
    echo "Run: ./kicad_flatpak_setup.sh"
    echo ""
    read -p "Continue anyway? (y/N) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

echo "=========================================="
echo "KiCad MCP Server - Flatpak Mode"
echo "=========================================="
echo "Server: $SERVER_SCRIPT"
echo "Working directory: $SCRIPT_DIR"
echo ""
echo "Starting server..."
echo ""

# Run the MCP server inside Flatpak with filesystem access
flatpak run \
    --command=python3 \
    --filesystem=home \
    org.kicad.KiCad \
    "$SCRIPT_DIR/$SERVER_SCRIPT"
