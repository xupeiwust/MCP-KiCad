# Quick Start Guide

Get started with KiCad MCP integration in 5 minutes.

## Prerequisites Check

```bash
# Check Python version (need 3.10+)
python3 --version

# Check if KiCad is installed
which kicad
```

## Installation

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
# Test the server works
python test_server.py
```

You should see mock component data and successful test results.

## Use With KiCad

### Step 1: Open KiCad Board

```bash
# Open your PCB project
kicad /path/to/your/project.kicad_pcb
```

In KiCad, open the PCB Editor (PCBNew).

### Step 2: Start Server

In one terminal:

```bash
source venv/bin/activate
python kicad_mcp_server.py
```

### Step 3: Start Client

In another terminal:

```bash
source venv/bin/activate
python kicad_mcp_client.py kicad_mcp_server.py
```

### Step 4: Chat!

```
You: List all components on the board
You: Place R1 at 10, 20 mm
You: Give me layout suggestions for an LED circuit
```

## Troubleshooting

### "pcbnew module not available"

The server runs in mock mode. To use real KiCad:

```bash
# Find KiCad's Python
ls /usr/lib/kicad/bin/

# Install deps in KiCad's Python
/usr/lib/kicad/bin/python3 -m pip install mcp anthropic python-dotenv

# Run server with KiCad's Python
/usr/lib/kicad/bin/python3 kicad_mcp_server.py
```

### "ANTHROPIC_API_KEY not found"

Make sure `.env` file exists with:

```
ANTHROPIC_API_KEY=sk-ant-your-key-here
```

Get key from: https://console.anthropic.com/

## Next Steps

- Read [README.md](README.md) for complete documentation
- Check example queries in the README
- Extend the server with more tools
- Try different circuit types in layout prompts

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