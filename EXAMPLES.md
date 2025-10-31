# Usage Examples

Complete examples showing how to use KiCad MCP Integration for PCB design and fabrication.

## Basic Usage Examples

### Example 1: Listing Components

**User Query:**
```
You: List all components on the board
```

**AI Response:**
```
Calling tool: list_components
Arguments: {}

Result: Found 42 components on the board:

Reference | Value      | Footprint               | Position (mm)  | Rotation | Layer
----------|------------|-------------------------|----------------|----------|------
R1        | 10k        | R_0805_2012Metric       | (50.8, 30.5)  | 0°       | Top
R2        | 10k        | R_0805_2012Metric       | (55.9, 30.5)  | 0°       | Top
C1        | 100nF      | C_0805_2012Metric       | (60.2, 35.1)  | 90°      | Top
U1        | ATmega328P | TQFP-32_7x7mm           | (70.0, 45.0)  | 45°      | Top
...
```

### Example 2: Placing Components

**User Query:**
```
You: Place resistor R1 at position 50, 30 mm
```

**AI Response:**
```
Calling tool: place_component
Arguments: {
  "reference": "R1",
  "x_mm": 50.0,
  "y_mm": 30.0
}

Result: Component R1 moved to (50.0, 30.0) mm
```

**User Query:**
```
You: Move capacitor C1 to 60, 35 mm with 90 degree rotation
```

**AI Response:**
```
Calling tool: place_component
Arguments: {
  "reference": "C1",
  "x_mm": 60.0,
  "y_mm": 35.0,
  "rotation_deg": 90.0
}

Result: Component C1 moved to (60.0, 35.0) mm, rotated to 90°
```

### Example 3: Board Information

**User Query:**
```
You: What's the board size and how many layers does it have?
```

**AI Response:**
```
Calling tool: get_board_info
Arguments: {}

Result:
Board: myproject.kicad_pcb
Size: 100.0 x 75.0 mm
Layers: 2 (F.Cu, B.Cu)
Components: 42
Tracks: 156
Vias: 28
```

### Example 4: Netlist Information

**User Query:**
```
You: Show me the netlist for the power supply section
```

**AI Response:**
```
Calling tool: read_netlist
Arguments: {}

Result: Found 23 nets:

Net Name    | Net Code | Pads
------------|----------|-----
GND         | 0        | 45
VCC         | 1        | 32
VOUT        | 2        | 8
/LED1       | 3        | 2
/RESET      | 4        | 3
...
```

## Fabrication Examples (Extended Server)

### Example 5: Export Gerber Files

**User Query:**
```
You: Export Gerber files for manufacturing
```

**AI Response:**
```
Calling tool: export_gerber
Arguments: {
  "output_dir": "./fabrication/gerber"
}

Result: Exported 9 Gerber files to ./fabrication/gerber:
- myproject-F.Cu.gbr (Front Copper)
- myproject-B.Cu.gbr (Back Copper)
- myproject-F.Mask.gbr (Front Solder Mask)
- myproject-B.Mask.gbr (Back Solder Mask)
- myproject-F.SilkS.gbr (Front Silkscreen)
- myproject-B.SilkS.gbr (Back Silkscreen)
- myproject-F.Paste.gbr (Front Paste)
- myproject-B.Paste.gbr (Back Paste)
- myproject-Edge.Cuts.gbr (Board Outline)
- myproject-job.gbrjob (Gerber Job File)

Files are ready for manufacturing!
```

### Example 6: Generate Drill Files

**User Query:**
```
You: Create drill files with PTH and NPTH separated
```

**AI Response:**
```
Calling tool: export_drill_files
Arguments: {
  "output_dir": "./fabrication/drill",
  "merge_pth_npth": false
}

Result: Exported drill files to ./fabrication/drill:
- myproject.drl (48 PTH holes)
- myproject-NPTH.drl (4 NPTH holes)

Total holes: 52 (48 plated, 4 non-plated)
```

### Example 7: Complete Fabrication Package

**User Query:**
```
You: Prepare a complete fabrication package for JLCPCB
```

**AI Response:**
```
I'll create a complete fabrication package with Gerber files, drill files, BOM, and position file.

Calling tool: fill_zones
Arguments: {}
Result: Filled 2 copper zones (GND, VCC)

Calling tool: run_drc
Arguments: {}
Result: DRC passed - 0 errors, 2 warnings

Calling tool: export_fabrication_package
Arguments: {
  "output_path": "./fabrication/myproject_fabrication.zip"
}

Result: Created fabrication package: ./fabrication/myproject_fabrication.zip
Contents:
- 9 Gerber files
- 2 Drill files
- bom.csv (25 unique parts, 42 components)
- position.csv (42 component positions)
- README.txt (manufacturing notes)

Package size: 145 KB
Ready to upload to JLCPCB!
```

### Example 8: Export Bill of Materials

**User Query:**
```
You: Generate a BOM in CSV format
```

**AI Response:**
```
Calling tool: export_bom
Arguments: {
  "output_path": "./fabrication/bom.csv",
  "include_dnp": false
}

Result: Exported BOM to ./fabrication/bom.csv
- 25 unique component types
- 42 total components
- Excludes DNP (Do Not Populate) components

Sample entries:
Reference       | Value  | Footprint             | Qty
----------------|--------|-----------------------|----
R1,R2,R3        | 10k    | R_0805_2012Metric    | 3
C1,C2           | 100nF  | C_0805_2012Metric    | 2
U1              | ATmega | TQFP-32_7x7mm        | 1
```

### Example 9: Pick-and-Place Position File

**User Query:**
```
You: Create a pick-and-place file for automated assembly
```

**AI Response:**
```
Calling tool: export_position_file
Arguments: {
  "output_path": "./fabrication/position.csv",
  "side": "both"
}

Result: Exported position file to ./fabrication/position.csv
- 38 top-side components
- 4 bottom-side components
- Total: 42 components

Format: CSV with columns:
Ref, Val, Package, PosX, PosY, Rot, Side

Compatible with: JLCPCB, PCBWay, Macrofab
```

## Verification Examples

### Example 10: Design Rule Check

**User Query:**
```
You: Run a design rule check on my board
```

**AI Response:**
```
Calling tool: run_drc
Arguments: {
  "report_path": "./drc_report.txt"
}

Result: DRC Check Complete
Errors: 0
Warnings: 3

Warnings:
1. Track width 0.15mm is close to minimum (0.127mm) - Net: /USB_D+
2. Clearance 0.21mm is close to minimum (0.2mm) - Between R12 and C5
3. Silkscreen over pad - Component: U1

Report saved to: ./drc_report.txt
```

### Example 11: Fill Copper Zones

**User Query:**
```
You: Fill all copper zones before generating fabrication files
```

**AI Response:**
```
Calling tool: fill_zones
Arguments: {}

Result: Filled 2 copper zones:
- Zone 1: GND (connected to 45 pads)
- Zone 2: VCC (connected to 32 pads)

Zones updated successfully. Refresh KiCad to see changes.
```

### Example 12: Track Information

**User Query:**
```
You: Show me information about tracks on the VCC net
```

**AI Response:**
```
Calling tool: get_track_info
Arguments: {
  "net_name": "VCC"
}

Result: Track information for net 'VCC':
Tracks: 24
Total length: 156.8 mm
Average width: 0.4 mm

Layer distribution:
- F.Cu: 18 tracks (102.3 mm)
- B.Cu: 6 tracks (54.5 mm)

Width distribution:
- 0.3mm: 8 tracks
- 0.4mm: 12 tracks
- 0.5mm: 4 tracks
```

## Multi-Step Workflow Examples

### Example 13: Complete Pre-Fabrication Workflow

**User Query:**
```
You: Prepare my board for fabrication at JLCPCB. Make sure everything is ready.
```

**AI Response:**
```
I'll run a complete pre-fabrication workflow for you.

Step 1: Filling copper zones...
Calling tool: fill_zones
Result: ✓ Filled 2 zones (GND, VCC)

Step 2: Running Design Rule Check...
Calling tool: run_drc
Result: ✓ DRC passed - 0 errors, 2 warnings (minor clearance warnings)

Step 3: Exporting Gerber files...
Calling tool: export_gerber
Arguments: {"output_dir": "./fabrication/gerber"}
Result: ✓ Exported 9 Gerber files

Step 4: Exporting drill files...
Calling tool: export_drill_files
Arguments: {"output_dir": "./fabrication/drill", "merge_pth_npth": false}
Result: ✓ Exported 2 drill files (PTH and NPTH)

Step 5: Generating BOM...
Calling tool: export_bom
Arguments: {"output_path": "./fabrication/bom.csv"}
Result: ✓ BOM created (25 unique parts, 42 components)

Step 6: Generating position file...
Calling tool: export_position_file
Arguments: {"output_path": "./fabrication/position.csv", "side": "both"}
Result: ✓ Position file created (42 components)

Step 7: Creating ZIP package...
Calling tool: export_fabrication_package
Arguments: {"output_path": "./fabrication/myproject_jlcpcb.zip"}
Result: ✓ Package created (145 KB)

✓ COMPLETE! Your board is ready for JLCPCB.

Next steps:
1. Upload ./fabrication/myproject_jlcpcb.zip to JLCPCB
2. Review the BOM and select components
3. Verify the board preview
4. Place your order

Notes:
- 2 minor DRC warnings (clearances are acceptable)
- All files generated successfully
- Total cost estimate: Check JLCPCB for current pricing
```

### Example 14: Iterative Design Workflow

**User Query:**
```
You: I need to place decoupling capacitors near the microcontroller. Can you help?
```

**AI Response:**
```
Let me help you place decoupling capacitors near the microcontroller.

First, let me find the microcontroller:

Calling tool: list_components
Result: Found U1 (ATmega328P) at position (70.0, 45.0) mm

Now, let me identify decoupling capacitors:
- C1: 100nF (currently at 60.2, 35.1 mm)
- C2: 100nF (currently at 55.0, 38.0 mm)

I'll place them near U1 for optimal performance:

Calling tool: place_component
Arguments: {"reference": "C1", "x_mm": 68.0, "y_mm": 42.0}
Result: ✓ C1 moved to (68.0, 42.0) mm - 3.6mm from U1

Calling tool: place_component
Arguments: {"reference": "C2", "x_mm": 72.0, "y_mm": 42.0}
Result: ✓ C2 moved to (72.0, 42.0) mm - 4.2mm from U1

Decoupling capacitors placed!
- Both are now < 5mm from U1 (ideal for high-frequency decoupling)
- Positioned symmetrically on either side
- Refresh your KiCad view (F5) to see the changes

Would you like me to:
1. Check the VCC net connections?
2. Verify power trace widths?
3. Run a DRC check?
```

## Real Project Example: Olivia Control v0.2

### Example 15: Actual Fabrication Generation

This is a real example from the Olivia Control v0.2 project (51 components, 90x100mm, 2-layer board):

**Command:**
```bash
flatpak run --command=python3 --filesystem=home org.kicad.KiCad generate_olivia_fabrication.py
```

**Output:**
```
Reading PCB: /home/pablo/repos/Proyecto-Incubadora/HardWare/Electro/Olivia_control/v0.2/Olivia_control.kicad_pcb
Board: Olivia_control.kicad_pcb
Size: 90.0 x 100.0 mm
Layers: 2
Components: 51

Generating Gerber files...
✓ F.Cu (Front Copper)
✓ B.Cu (Back Copper)
✓ F.Mask (Front Solder Mask)
✓ B.Mask (Back Solder Mask)
✓ F.SilkS (Front Silkscreen)
✓ B.SilkS (Back Silkscreen)
✓ F.Paste (Front Paste)
✓ B.Paste (Back Paste)
✓ Edge.Cuts (Board Outline)

Generating drill files...
✓ PTH: 124 holes
✓ NPTH: 4 holes

Generating BOM...
✓ 35 unique parts
✓ 51 total components

Generating position file...
✓ 51 component positions

Creating fabrication package...
✓ ZIP created: olivia_v0.2_fabrication_20251021_154253.zip (140 KB)

FABRICATION COMPLETE!

Output directory: /home/pablo/repos/MCP-KiCad/fabrication_output/olivia_v0.2_20251021_154253

Ready for manufacturing at:
- JLCPCB ✓
- PCBWay ✓
- OSH Park ✓
```

**Files Generated:**
```
fabrication_output/olivia_v0.2_20251021_154253/
├── gerber/
│   ├── Olivia_control-F.Cu.gbr (36 KB)
│   ├── Olivia_control-B.Cu.gbr (28 KB)
│   ├── Olivia_control-F.Mask.gbr (12 KB)
│   ├── Olivia_control-B.Mask.gbr (10 KB)
│   ├── Olivia_control-F.SilkS.gbr (8 KB)
│   ├── Olivia_control-B.SilkS.gbr (4 KB)
│   ├── Olivia_control-F.Paste.gbr (6 KB)
│   ├── Olivia_control-B.Paste.gbr (5 KB)
│   └── Olivia_control-Edge.Cuts.gbr (2 KB)
├── drill/
│   ├── Olivia_control.drl (4 KB)
│   └── Olivia_control-NPTH.drl (1 KB)
├── bom.csv (2 KB)
├── position.csv (3 KB)
├── INDEX.md
└── OLIVIA_FABRICATION_README.md
```

**Manufacturing Result:**
- ✅ Successfully uploaded to JLCPCB
- ✅ No Gerber errors
- ✅ Automatic quote: $5.00 for 5 boards (2-day shipping)
- ✅ Production-ready on first attempt

## Command Reference

### Starting the Server

```bash
# Flatpak (recommended)
./run_with_flatpak.sh

# Native Python
python kicad_mcp_server_extended.py
```

### Starting the Client

```bash
source venv/bin/activate
python kicad_mcp_client.py kicad_mcp_server_extended.py
```

### Running Tests

```bash
# Basic server tests
python test_server.py

# Extended server tests (20 tests)
python test_fabrication.py
```

### Standalone Fabrication

```bash
# Edit paths in generate_olivia_fabrication.py first
flatpak run --command=python3 --filesystem=home org.kicad.KiCad generate_olivia_fabrication.py
```

## Tips and Best Practices

### 1. Always Fill Zones Before Export

```
You: Fill all copper zones before exporting Gerber files
```

This ensures proper ground/power plane connectivity.

### 2. Run DRC Before Fabrication

```
You: Run DRC check and save report
```

Catches errors before sending to manufacturer.

### 3. Use Complete Fabrication Package

```
You: Create complete fabrication package
```

Ensures all files (Gerber + Drill + BOM + Position) are included.

### 4. Verify Component Positions

```
You: List all components and show their positions
```

Double-check placement before finalizing.

### 5. Test in Mock Mode First

```bash
python test_fabrication.py
```

Verify everything works without opening KiCad.

## Troubleshooting Examples

### Error: "Component not found"

**User Query:**
```
You: Place R99 at 50, 30 mm
```

**AI Response:**
```
Error: Component 'R99' not found on the board.

Would you like me to list all resistors? Or list all components?
```

**Solution:**
```
You: List all resistors
AI: Found resistors: R1, R2, R3, R4, R5
```

### Error: "pcbnew not available"

**System Message:**
```
Warning: pcbnew module not available. Running in MOCK MODE.
```

**Solution:**
Use the Flatpak wrapper:
```bash
./run_with_flatpak.sh
```

### Error: "Board not open in KiCad"

**AI Response:**
```
Error: No PCB board is currently open in KiCad.
Please open a .kicad_pcb file in KiCad PCBNew before starting the server.
```

**Solution:**
```bash
# Open your board first
kicad /path/to/project.kicad_pcb

# Then start the server
./run_with_flatpak.sh
```

## Related Documentation

- [README.md](README.md) - Complete setup and tool reference
- [FABRICATION.md](FABRICATION.md) - Detailed fabrication tool documentation
- [QUICKSTART.md](QUICKSTART.md) - 5-minute setup guide
- [STANDALONE_FABRICATION.md](STANDALONE_FABRICATION.md) - Direct script usage

---

**Need More Help?**

- Review tool documentation in [README.md](README.md#available-tools)
- Check [FABRICATION.md](FABRICATION.md) for detailed fabrication workflows
- See [STANDALONE_FABRICATION.md](STANDALONE_FABRICATION.md) for non-AI approach
- Open an issue: https://github.com/Pablomonte/MCP-KiCad/issues
