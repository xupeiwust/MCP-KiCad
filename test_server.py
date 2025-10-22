#!/usr/bin/env python3
"""
Quick test script to verify the MCP server works in mock mode
"""

import asyncio
import json
from kicad_mcp_server import KiCadMCPServer


async def test_tools():
    """Test the server tools directly"""

    print("Testing KiCad MCP Server in Mock Mode")
    print("=" * 50)

    server = KiCadMCPServer()

    # Test 1: List components
    print("\n1. Testing list_components...")
    result = await server._list_components()
    print(json.dumps(result, indent=2))

    # Test 2: Get board info
    print("\n2. Testing get_board_info...")
    result = await server._get_board_info()
    print(json.dumps(result, indent=2))

    # Test 3: Read netlist
    print("\n3. Testing read_netlist...")
    result = await server._read_netlist()
    print(json.dumps(result, indent=2))

    # Test 4: Place component
    print("\n4. Testing place_component...")
    result = await server._place_component("R1", 10.0, 20.0, 45.0)
    print(json.dumps(result, indent=2))

    # Test 5: Get circuit guidance
    print("\n5. Testing circuit guidance...")
    components = await server._list_components()
    guidance = server._get_circuit_guidance("LED", components)
    print(guidance[:200] + "...")

    print("\n" + "=" * 50)
    print("All tests completed successfully!")
    print("\nNote: This is mock mode. Real KiCad integration requires:")
    print("  1. KiCad PCBNew running with a board open")
    print("  2. pcbnew Python module available")


if __name__ == "__main__":
    asyncio.run(test_tools())
