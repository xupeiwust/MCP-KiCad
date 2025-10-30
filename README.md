# KiCad MCP Integration

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![KiCad 9.0+](https://img.shields.io/badge/KiCad-9.0+-blue.svg)](https://www.kicad.org/)
[![Version](https://img.shields.io/badge/version-1.0.0-green.svg)](https://github.com/Pablomonte/MCP-KiCad/releases/tag/v1.0.0)
[![Tests](https://img.shields.io/badge/tests-20%2F20%20passing-brightgreen.svg)](#testing)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

AI-assisted KiCad PCB design using Model Context Protocol (MCP) and Anthropic Claude.

## Overview

This project provides an MCP server that exposes KiCad PCB design tools to AI assistants, enabling natural language interaction with your PCB designs. You can ask an AI to place components, read netlists, and get layout suggestions.

## Features

- **Natural Language PCB Design**: Interact with KiCad using plain English
- **Component Placement**: Ask AI to place components at specific coordinates
- **Board Analysis**: Query component lists, netlists, and board information
- **Layout Guidance**: Get AI-powered layout suggestions for common circuit types
- **Real-time Updates**: Changes are immediately reflected in KiCad

## Architecture

```
┌─────────────┐         ┌─────────────┐         ┌──────────┐
│   You       │ ───────▶│  AI Client  │ ───────▶│  Claude  │
│  (User)     │  Chat   │  (Python)   │   API   │   AI     │
└─────────────┘         └─────────────┘         └──────────┘
                              │
                              │ MCP Protocol
                              ▼
                        ┌─────────────┐         ┌──────────┐
                        │ MCP Server  │ ───────▶│  KiCad   │
                        │  (Python)   │ pcbnew  │ PCBNew   │
                        └─────────────┘         └──────────┘
```

## Prerequisites

1. **KiCad 7.0+** with Python scripting support
2. **Python 3.10+**
3. **Anthropic API Key** (or xAI API key for Grok)

## Installation

### 1. Clone or Download

```bash
cd ~/repos
git clone <repository-url> MCP-KiCad
cd MCP-KiCad
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Linux/Mac
# or
venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API Key

Copy the example environment file and add your API key:

```bash
cp .env.example .env
nano .env  # or your preferred editor
```

Edit `.env` and add your Anthropic API key:

```
ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxxxxxxxxxx
```

Get your API key from: https://console.anthropic.com/

### 5. Setup KiCad Python Environment

The MCP server needs access to KiCad's `pcbnew` module. There are two approaches:

#### Option A: Use KiCad's Python (Recommended)

Find KiCad's Python installation:

```bash
# Linux
which kicad-python
# or
ls /usr/lib/kicad/bin/

# Mac
/Applications/KiCad/KiCad.app/Contents/Frameworks/Python.framework/Versions/Current/bin/python3

# Windows
C:\Program Files\KiCad\7.0\bin\python.exe
```

Install dependencies in KiCad's Python:

```bash
/path/to/kicad-python -m pip install mcp anthropic python-dotenv
```

#### Option B: Link pcbnew to Your Virtual Environment

```bash
# Linux example
ln -s /usr/lib/python3/dist-packages/pcbnew.py venv/lib/python3.*/site-packages/
ln -s /usr/lib/python3/dist-packages/_pcbnew.so venv/lib/python3.*/site-packages/
```

**Note**: The exact paths vary by system. Check your KiCad installation.

## Usage

### 1. Open KiCad PCBNew

First, open your PCB project in KiCad PCBNew:

```bash
kicad path/to/your/project.kicad_pcb
```

Make sure the PCB editor (PCBNew) is open, not just the project manager.

### 2. Run the MCP Server

In a terminal, with your virtual environment activated:

```bash
python kicad_mcp_server.py
```

The server will connect to the currently open KiCad board and wait for MCP requests.

**Note**: If pcbnew is not available, the server runs in **mock mode** for testing.

### 3. Run the Client

In another terminal (with virtual environment activated):

```bash
python kicad_mcp_client.py kicad_mcp_server.py
```

You should see:

```
Connected to KiCad MCP Server
Available tools: place_component, read_netlist, list_components, get_board_info

======================================================================
KiCad AI Assistant
======================================================================

You can ask me to help with your PCB design!
...

You:
```

### 4. Interact with Your Board

Try these example queries:

```
You: List all components on the board
You: Place R1 at position 10, 20 mm
You: Move capacitor C1 to 15, 25 mm with 90 degree rotation
You: Show me the netlist
You: What's the board size?
You: Give me layout suggestions for an LED circuit
```

The AI will:
1. Understand your natural language request
2. Call the appropriate KiCad tools via MCP
3. Execute changes on your PCB
4. Provide feedback on what was done

### 5. Verify Changes in KiCad

After the AI makes changes, refresh your KiCad view to see the updates:
- Click on the PCB canvas
- Press `F5` or use View → Refresh

## Available Tools

The MCP server provides these tools to the AI:

### place_component
Move a component to a specific position on the PCB.

**Parameters**:
- `reference` (string): Component reference (e.g., "R1", "U1")
- `x_mm` (number): X position in millimeters
- `y_mm` (number): Y position in millimeters
- `rotation_deg` (number, optional): Rotation angle in degrees

### list_components
List all components on the PCB with their current positions.

**Returns**: JSON array of components with reference, value, position, rotation, layer

### read_netlist
Read netlist information from the board.

**Returns**: JSON array of nets with names and net codes

### get_board_info
Get general information about the PCB.

**Returns**: Board size, layer count, component count, filename

## Available Resources

### board://schematic
JSON list of all components from the board schematic

### board://info
General PCB board information and settings

## Available Prompts

### simple_circuit
Get AI-powered layout guidance for simple circuits.

**Parameters**:
- `type` (string): Circuit type - "LED", "power_supply", "amplifier", etc.

**Returns**: Layout guidelines and best practices for the specified circuit type

## Project Structure

```
MCP-KiCad/
├── kicad_mcp_server.py      # MCP server exposing KiCad tools
├── kicad_mcp_client.py      # AI client using Claude
├── requirements.txt          # Python dependencies
├── .env.example             # Example environment configuration
├── .env                     # Your API keys (not in git)
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

## Troubleshooting

### "pcbnew module not available"

The server will run in mock mode. To fix:
- Make sure KiCad is installed
- Use KiCad's Python interpreter (see Installation step 5)
- Or link pcbnew to your virtual environment

### "No PCB board is currently open in KiCad"

- Open a PCB file in KiCad PCBNew before running the server
- Make sure you're in the PCB editor, not just the project manager

### "ANTHROPIC_API_KEY not found"

- Create `.env` file from `.env.example`
- Add your API key: `ANTHROPIC_API_KEY=sk-ant-...`
- Make sure `.env` is in the same directory as the scripts

### Component not found error

- List all components first: "List all components"
- Use exact reference designator (case-sensitive)
- Make sure components are on the PCB (not just schematic)

### Changes don't appear in KiCad

- Refresh the view in KiCad (F5)
- Check the console for error messages
- Verify the server is running and connected

## Advanced Usage

### Using with xAI Grok (Alternative to Claude)

To use Grok instead of Claude:

1. Get an xAI API key from https://x.ai/
2. Modify `kicad_mcp_client.py`:

```python
# Replace Anthropic client with xAI client
from openai import OpenAI  # xAI uses OpenAI-compatible API

client = OpenAI(
    api_key=os.getenv("XAI_API_KEY"),
    base_url="https://api.x.ai/v1"
)
```

3. Update API calls to use xAI's model name (e.g., "grok-beta")

### Running Server Standalone

The MCP server can be used by any MCP-compatible client:

```bash
python kicad_mcp_server.py
```

Then connect with any MCP client using stdio transport.

### Extending with More Tools

Add new tools by:

1. Define tool in `list_tools()` handler
2. Implement tool function (e.g., `_route_traces()`)
3. Add tool call handler in `call_tool()`

Example tools to add:
- Route traces between components
- Apply design rules
- Generate copper pours
- Export Gerber files
- Import component footprints

## Security Considerations

- **API Keys**: Never commit `.env` file to version control
- **Auto-execution**: AI can modify your PCB directly - review changes carefully
- **Backups**: Always keep backups of your KiCad projects
- **Logging**: Tool calls are logged to console for transparency

## Development

### Testing in Mock Mode

Test without KiCad by running in mock mode:

```bash
python kicad_mcp_server.py  # pcbnew not available → mock mode
python kicad_mcp_client.py kicad_mcp_server.py
```

Mock mode returns simulated data for testing.

### Adding Logging

Add detailed logging for debugging:

```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
```

### Code Style

- Follow PEP 8 style guide
- Use type hints for all functions
- Document functions with docstrings
- Handle errors gracefully

## Contributing

Contributions welcome! Areas for improvement:

- Support for more KiCad features (routing, DRC, etc.)
- Better error handling and recovery
- Unit tests and integration tests
- Support for other AI models
- Web-based UI
- Multi-board projects

## License

This project is free and open source. Use it however you like.

## Resources

- **KiCad**: https://www.kicad.org/
- **KiCad Python API**: https://docs.kicad.org/doxygen-python/namespacepcbnew.html
- **MCP Protocol**: https://modelcontextprotocol.io/
- **Anthropic Claude**: https://www.anthropic.com/
- **xAI Grok**: https://x.ai/

## Support

For issues, questions, or suggestions:
- Check existing issues in the repository
- Read the Troubleshooting section above
- Review KiCad Python API documentation

## Acknowledgments

Built using:
- KiCad Python API (pcbnew)
- Anthropic's Model Context Protocol
- Claude 3.5 Sonnet
- Python asyncio

---

**Happy PCB Designing with AI!** 🤖🔌
