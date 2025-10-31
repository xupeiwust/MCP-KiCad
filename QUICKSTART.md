# Quick Start Guide

Get started with KiCad MCP integration in 5 minutes.

## Prerequisites Check

```bash
# Check Python version (need 3.10+)
python3 --version

# Check if KiCad Flatpak is installed (recommended)
flatpak list | grep kicad

# If not installed:
flatpak install flathub org.kicad.KiCad
```

## Installation

### Method 1: Flatpak (Recommended - 5 minutes)

```bash
# 1. Navigate to project
cd ~/repos/MCP-KiCad

# 2. Install dependencies in Flatpak
./kicad_flatpak_setup.sh

# 3. Configure API key
cp .env.example .env
nano .env  # Add your ANTHROPIC_API_KEY
```

That's it! You're ready to go with Flatpak.

### Method 2: Native Python (Advanced)

```bash
# 1. Navigate to project
cd ~/repos/MCP-KiCad

# 2. Create virtual environment
python3 -m venv venv

# 3. Activate it
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Configure API key
cp .env.example .env
nano .env  # Add your ANTHROPIC_API_KEY
```

## Test Without KiCad (Mock Mode)

```bash
# Test basic server (4 tools)
python test_server.py

# Test extended server with fabrication tools (12 tools)
python test_fabrication.py
```

You should see 20/20 tests passing with mock component data.

## Test With Real Board

Test all 12 tools with a real KiCad board (no GUI needed):

```bash
# Test 1: Basic board loading
flatpak run --command=python3 --filesystem=home \
  org.kicad.KiCad test_real_board.py

# Test 2: Full MCP server functionality
flatpak run --command=python3 --filesystem=home \
  org.kicad.KiCad test_server_real.py
```

**What's tested:**
- Loading real `.kicad_pcb` files
- Reading components, nets, board info
- Exporting Gerber, drill, BOM, position files
- Creating fabrication packages
- All 12 MCP tools

**Expected output:**
- ✅ All tests pass
- ⚠️ Some KiCad 9.x via width warnings (expected, not errors)
- See [FABRICATION.md](FABRICATION.md#testing) for details

**Requirements:**
- KiCad 9.0+ Flatpak installed
- A `.kicad_pcb` board file
- Edit `BOARD_PATH` in test scripts to point to your board

## Use With KiCad

### Step 1: Open KiCad Board

```bash
# Open your PCB project
kicad /path/to/your/project.kicad_pcb
```

In KiCad, open the PCB Editor (PCBNew).

### Step 2: Start Server

In one terminal:

**With Flatpak (Recommended):**

```bash
# Extended server with fabrication tools (12 tools)
./run_with_flatpak.sh

# Or basic server only (4 tools)
./run_with_flatpak.sh kicad_mcp_server.py
```

**With Native Python:**

```bash
source venv/bin/activate
python kicad_mcp_server_extended.py  # or kicad_mcp_server.py for basic
```

### Step 3: Start Client

In another terminal:

```bash
source venv/bin/activate
python kicad_mcp_client.py kicad_mcp_server.py
```

### Step 4: Chat!

**Basic operations:**
```
You: List all components on the board
You: Place R1 at 10, 20 mm
You: Give me layout suggestions for an LED circuit
```

**Fabrication operations (Extended server):**
```
You: Export Gerber files
You: Create a BOM
You: Generate fabrication package for JLCPCB
You: Run Design Rule Check
```

## Troubleshooting

### "pcbnew module not available"

The server runs in mock mode. To use real KiCad:

**With Flatpak (Easy):**
```bash
# Just use the wrapper script
./run_with_flatpak.sh
```

**With Native KiCad:**
```bash
# Find KiCad's Python
ls /usr/lib/kicad/bin/

# Install deps in KiCad's Python
/usr/lib/kicad/bin/python3 -m pip install mcp anthropic python-dotenv

# Run server with KiCad's Python
/usr/lib/kicad/bin/python3 kicad_mcp_server_extended.py
```

### "ANTHROPIC_API_KEY not found"

Make sure `.env` file exists with:

```
ANTHROPIC_API_KEY=sk-ant-your-key-here
```

Get key from: https://console.anthropic.com/

## Next Steps

- Read [README.md](README.md) for complete documentation with all 12 tools
- Check [FABRICATION.md](FABRICATION.md) for fabrication workflow guide
- See [STANDALONE_FABRICATION.md](STANDALONE_FABRICATION.md) for direct script usage
- Try the Olivia v0.2 example in `fabrication_output/`
- Extend the server with more tools

## Example Session

```
$ python kicad_mcp_client.py kicad_mcp_server.py

Connected to KiCad MCP Server
Available tools: place_component, read_netlist, list_components, get_board_info

You: List all components

Calling tool: list_components
Arguments: {}
Result: {
  "status": "success",
  "count": 12,
  "components": [...]
}