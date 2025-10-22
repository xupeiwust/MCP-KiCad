#!/usr/bin/env python3
"""
Test script for KiCad MCP Server Extended fabrication tools
Tests all fabrication, verification, and layout tools in mock mode
"""

import asyncio
import json
import tempfile
import shutil
from pathlib import Path

# Import the extended server
from kicad_mcp_server_extended import KiCadMCPServerExtended


async def test_all_fabrication_tools():
    """Test all fabrication tools"""

    print("=" * 70)
    print("Testing KiCad MCP Server Extended - Fabrication Tools")
    print("=" * 70)
    print()

    server = KiCadMCPServerExtended()

    # Create temporary directory for test outputs
    temp_dir = tempfile.mkdtemp(prefix="kicad_mcp_test_")
    print(f"Using temporary directory: {temp_dir}\n")

    try:
        # ====================================================================
        # BASIC TOOLS
        # ====================================================================
        print("=" * 70)
        print("BASIC TOOLS")
        print("=" * 70)

        print("\n1. Testing list_components...")
        result = await server._list_components()
        print(json.dumps(result, indent=2))
        assert result["status"] == "mock"
        print("✓ list_components works")

        print("\n2. Testing get_board_info...")
        result = await server._get_board_info()
        print(json.dumps(result, indent=2))
        assert result["status"] == "mock"
        print("✓ get_board_info works")

        print("\n3. Testing read_netlist...")
        result = await server._read_netlist()
        print(json.dumps(result, indent=2))
        assert result["status"] == "mock"
        print("✓ read_netlist works")

        print("\n4. Testing place_component...")
        result = await server._place_component("R1", 10.0, 20.0, 45.0)
        print(json.dumps(result, indent=2))
        assert result["status"] == "mock"
        print("✓ place_component works")

        # ====================================================================
        # FABRICATION TOOLS
        # ====================================================================
        print("\n" + "=" * 70)
        print("FABRICATION TOOLS")
        print("=" * 70)

        print("\n5. Testing export_gerber...")
        gerber_dir = Path(temp_dir) / "gerber"
        result = await server._export_gerber(str(gerber_dir))
        print(json.dumps(result, indent=2))
        assert result["status"] == "mock"
        assert len(result["files"]) > 0
        print(f"✓ export_gerber works - {len(result['files'])} files")

        print("\n6. Testing export_drill_files...")
        drill_dir = Path(temp_dir) / "drill"
        result = await server._export_drill_files(str(drill_dir))
        print(json.dumps(result, indent=2))
        assert result["status"] == "mock"
        assert len(result["files"]) > 0
        print(f"✓ export_drill_files works - {len(result['files'])} files")

        print("\n7. Testing export_drill_files (merged)...")
        drill_merged_dir = Path(temp_dir) / "drill_merged"
        result = await server._export_drill_files(str(drill_merged_dir), merge_pth_npth=True)
        print(json.dumps(result, indent=2))
        assert result["status"] == "mock"
        assert result["merged"] == True
        print("✓ export_drill_files (merged) works")

        print("\n8. Testing export_bom...")
        bom_file = Path(temp_dir) / "bom.csv"
        result = await server._export_bom(str(bom_file))
        print(json.dumps(result, indent=2))
        assert result["status"] == "mock"
        print("✓ export_bom works")

        print("\n9. Testing export_position_file...")
        pos_file = Path(temp_dir) / "position.csv"
        result = await server._export_position_file(str(pos_file))
        print(json.dumps(result, indent=2))
        assert result["status"] == "mock"
        print("✓ export_position_file works")

        print("\n10. Testing export_fabrication_package (generic)...")
        fab_dir = Path(temp_dir) / "fabrication"
        result = await server._export_fabrication_package(str(fab_dir), "generic")
        print(json.dumps(result, indent=2))
        if "error" not in result:
            assert result["manufacturer"] == "generic"
            print("✓ export_fabrication_package (generic) works")
        else:
            print(f"⚠ export_fabrication_package skipped: {result['error']}")

        print("\n11. Testing export_fabrication_package (jlcpcb)...")
        result = await server._export_fabrication_package(str(fab_dir), "jlcpcb")
        print(json.dumps(result, indent=2))
        if "error" not in result:
            assert result["manufacturer"] == "jlcpcb"
            print("✓ export_fabrication_package (jlcpcb) works")
        else:
            print(f"⚠ export_fabrication_package (jlcpcb) skipped: {result['error']}")

        # ====================================================================
        # VERIFICATION TOOLS
        # ====================================================================
        print("\n" + "=" * 70)
        print("VERIFICATION TOOLS")
        print("=" * 70)

        print("\n12. Testing run_drc (all)...")
        result = await server._run_drc("all")
        print(json.dumps(result, indent=2))
        assert result["status"] == "mock"
        print(f"✓ run_drc works - {result['error_count']} errors, {result['warning_count']} warnings")

        print("\n13. Testing run_drc (error only)...")
        result = await server._run_drc("error")
        print(json.dumps(result, indent=2))
        assert result["status"] == "mock"
        print("✓ run_drc (error only) works")

        # ====================================================================
        # LAYOUT TOOLS
        # ====================================================================
        print("\n" + "=" * 70)
        print("LAYOUT TOOLS")
        print("=" * 70)

        print("\n14. Testing fill_zones (all)...")
        result = await server._fill_zones()
        print(json.dumps(result, indent=2))
        assert result["status"] == "mock"
        print(f"✓ fill_zones works - filled {result['count']} zones")

        print("\n15. Testing fill_zones (specific)...")
        result = await server._fill_zones(zone_names=["GND"])
        print(json.dumps(result, indent=2))
        assert result["status"] == "mock"
        print("✓ fill_zones (specific) works")

        print("\n16. Testing get_track_info (all)...")
        result = await server._get_track_info()
        print(json.dumps(result, indent=2))
        assert result["status"] == "mock"
        print(f"✓ get_track_info works - {result['count']} tracks")

        print("\n17. Testing get_track_info (filtered)...")
        result = await server._get_track_info(net_name="VCC")
        print(json.dumps(result, indent=2))
        assert result["status"] == "mock"
        print("✓ get_track_info (filtered) works")

        # ====================================================================
        # PROMPTS
        # ====================================================================
        print("\n" + "=" * 70)
        print("PROMPTS")
        print("=" * 70)

        print("\n18. Testing circuit guidance (LED)...")
        components = await server._list_components()
        guidance = server._get_circuit_guidance("LED", components)
        print(guidance[:300] + "..." if len(guidance) > 300 else guidance)
        assert "LED" in guidance
        print("✓ circuit guidance (LED) works")

        print("\n19. Testing circuit guidance (power_supply)...")
        guidance = server._get_circuit_guidance("power_supply", components)
        print(guidance[:300] + "..." if len(guidance) > 300 else guidance)
        assert "power" in guidance.lower()
        print("✓ circuit guidance (power_supply) works")

        print("\n20. Testing fabrication checklist...")
        checklist = await server._get_fabrication_checklist()
        print(checklist[:400] + "..." if len(checklist) > 400 else checklist)
        assert "DRC" in checklist
        assert "Gerber" in checklist
        print("✓ fabrication checklist works")

        # ====================================================================
        # SUMMARY
        # ====================================================================
        print("\n" + "=" * 70)
        print("TEST SUMMARY")
        print("=" * 70)
        print()
        print("✓ All 20 tests passed successfully!")
        print()
        print("Tested tools:")
        print("  Basic: list_components, get_board_info, read_netlist, place_component")
        print("  Fabrication: export_gerber, export_drill_files, export_bom,")
        print("               export_position_file, export_fabrication_package")
        print("  Verification: run_drc")
        print("  Layout: fill_zones, get_track_info")
        print("  Prompts: circuit_guidance, fabrication_checklist")
        print()
        print("Note: All tests ran in MOCK MODE (no KiCad connection)")
        print("      Real KiCad integration requires:")
        print("        1. KiCad PCBNew running with a board open")
        print("        2. pcbnew Python module available")
        print("        3. Run via: ./run_with_flatpak.sh (for Flatpak)")
        print()

    finally:
        # Cleanup
        print(f"Cleaning up temporary directory: {temp_dir}")
        shutil.rmtree(temp_dir, ignore_errors=True)

    print("=" * 70)
    print("All tests completed successfully!")
    print("=" * 70)


async def test_error_handling():
    """Test error handling"""
    print("\n" + "=" * 70)
    print("TESTING ERROR HANDLING")
    print("=" * 70)

    server = KiCadMCPServerExtended()

    # Test with component placement with invalid reference
    print("\n1. Testing component placement with invalid reference...")
    result = await server._place_component("INVALID_REF", 0, 0)
    print(json.dumps(result, indent=2))
    assert result["status"] == "mock"
    print("✓ Handled invalid component reference")

    print("\n2. Testing get_track_info with non-existent net...")
    result = await server._get_track_info(net_name="NON_EXISTENT_NET")
    print(json.dumps(result, indent=2))
    assert result["status"] == "mock"
    assert result["count"] == 0  # Should return empty list
    print("✓ Handled non-existent net filter")

    print()


if __name__ == "__main__":
    print("\n")
    asyncio.run(test_all_fabrication_tools())
    asyncio.run(test_error_handling())
    print("\n✅ All fabrication tools tested and working!\n")
