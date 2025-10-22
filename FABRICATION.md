# Fabrication Tools Documentation

Complete guide for using KiCad MCP Server Extended fabrication tools.

## Overview

The extended MCP server (`kicad_mcp_server_extended.py`) provides AI-powered tools for generating PCB fabrication files, running design verification, and managing board layout.

## Quick Start

### Using Extended Server

```bash
# With Flatpak
./run_with_flatpak.sh

# Native installation
python kicad_mcp_server_extended.py
```

The client automatically detects which server is running.

## Fabrication Tools

### export_gerber

Export Gerber files for PCB fabrication (RS-274X format).

**Usage:**
```
AI: Export Gerber files to ./output/gerber
```

**Parameters:**
- `output_dir` (required): Output directory path
- `layers` (optional): List of layers to export (default: all standard layers)
- `create_job_file` (optional): Create `.gbrjob` file (default: true)

**Default Layers Exported:**
- `F.Cu` - Front copper
- `B.Cu` - Back copper
- `F.Mask` - Front solder mask
- `B.Mask` - Back solder mask
- `F.SilkS` - Front silkscreen
- `B.SilkS` - Back silkscreen
- `F.Paste` - Front paste (for stencils)
- `B.Paste` - Back paste
- `Edge.Cuts` - Board outline

**Example Output:**
```
output/gerber/
├── project-F_Cu.gbr
├── project-B_Cu.gbr
├── project-F_Mask.gbr
├── project-B_Mask.gbr
├── project-F_SilkS.gbr
├── project-B_SilkS.gbr
├── project-F_Paste.gbr
├── project-B_Paste.gbr
├── project-Edge_Cuts.gbr
└── project-job.gbrjob
```

### export_drill_files

Export drill files in Excellon format for PCB drilling.

**Usage:**
```
AI: Export drill files to ./output/drill
```

**Parameters:**
- `output_dir` (required): Output directory
- `merge_pth_npth` (optional): Merge plated and non-plated holes (default: false)

**Output Files:**
- `project-PTH.drl` - Plated through-holes
- `project-NPTH.drl` - Non-plated through-holes
- Or `project.drl` if merged

**Example:**
```
User: "Export drill files, keep PTH and NPTH separate"

AI calls: export_drill_files(
    output_dir="./fabrication/drill",
    merge_pth_npth=false
)
```

### export_fabrication_package

Create a complete fabrication package as a ZIP file, ready to send to manufacturers.

**Usage:**
```
AI: Create fabrication package for JLCPCB
```

**Parameters:**
- `output_dir` (required): Output directory for ZIP file
- `manufacturer_preset` (optional): Manufacturer preset
  - `jlcpcb` - JLCPCB format
  - `pcbway` - PCBWay format
  - `oshpark` - OSH Park format
  - `generic` - Generic format (default)

**Package Contents:**
```
fabrication_jlcpcb_20250121_143052.zip
├── gerber/
│   ├── *.gbr files (all layers)
│   └── *.gbrjob
├── drill/
│   ├── *-PTH.drl
│   └── *-NPTH.drl
├── bom.csv
└── position.csv
```

**Example:**
```
User: "Prepare everything for fabrication at JLCPCB"

AI calls: export_fabrication_package(
    output_dir="./output",
    manufacturer_preset="jlcpcb"
)
```

This is the **recommended** way to export - creates everything in one step!

### export_bom

Export Bill of Materials as CSV file.

**Usage:**
```
AI: Export BOM to ./output/bom.csv
```

**Parameters:**
- `output_file` (required): Output CSV file path

**CSV Format:**
```csv
Reference,Value,Footprint,Quantity
"R1 R2 R3","10k","Resistor_SMD:R_0805",3
"C1 C2","100nF","Capacitor_SMD:C_0805",2
"U1","LM358","Package_SO:SOIC-8",1
```

**Example:**
```
User: "Generate a bill of materials"

AI calls: export_bom(output_file="./fabrication/bom.csv")
```

### export_position_file

Export component position file for automated assembly (pick-and-place).

**Usage:**
```
AI: Export position file for SMT assembly
```

**Parameters:**
- `output_file` (required): Output CSV file path

**CSV Format:**
```csv
Designator,Val,Package,Mid X,Mid Y,Rotation,Layer
"R1","10k","R_0805",25.4000,30.5000,0.00,Top
"C1","100nF","C_0805",35.2000,30.5000,90.00,Top
"U1","LM358","SOIC-8",50.0000,40.0000,0.00,Top
```

**Coordinates:** In millimeters, relative to board origin

**Example:**
```
User: "I need component positions for the assembly house"

AI calls: export_position_file(output_file="./fab/positions.csv")
```

## Verification Tools

### run_drc

Run Design Rule Check to find errors and violations.

**Usage:**
```
AI: Run DRC and show any errors
```

**Parameters:**
- `severity_level` (optional): Minimum severity to report
  - `error` - Errors only
  - `warning` - Warnings and errors
  - `all` - Everything (default)

**Returns:**
- List of violations with type, severity, description
- Error and warning counts

**Example:**
```
User: "Check my board for design rule violations"

AI calls: run_drc(severity_level="all")

Result:
{
  "violations": [
    {
      "type": "clearance",
      "severity": "error",
      "description": "Clearance between Track and Pad"
    }
  ],
  "error_count": 1,
  "warning_count": 0
}
```

**Note:** Full DRC support requires KiCad 7+ with proper API access. Currently returns basic information.

## Layout Tools

### fill_zones

Fill copper zones (ground planes, power planes, etc.).

**Usage:**
```
AI: Fill all copper zones
AI: Fill the GND zone only
```

**Parameters:**
- `zone_names` (optional): List of specific zone net names to fill

**Example:**
```
User: "Fill all the copper pours"

AI calls: fill_zones()

User: "Just fill the GND zone"

AI calls: fill_zones(zone_names=["GND"])
```

**Note:** Board will refresh automatically after filling.

### get_track_info

Get information about traces/tracks on the board.

**Usage:**
```
AI: Show me all tracks on the VCC net
AI: Get track information
```

**Parameters:**
- `net_name` (optional): Filter by specific net name

**Returns:**
- Track width, length, layer, net name

**Example:**
```
User: "What's the total length of the VCC traces?"

AI calls: get_track_info(net_name="VCC")

Result:
{
  "tracks": [
    {"net": "VCC", "width_mm": 0.5, "length_mm": 25.4, "layer": "F.Cu"},
    {"net": "VCC", "width_mm": 0.5, "length_mm": 18.2, "layer": "F.Cu"}
  ],
  "count": 2
}
```

## AI Prompts

### fabrication_checklist

Get a comprehensive pre-fabrication checklist.

**Usage:**
```
AI: Give me the fabrication checklist
AI: What should I check before ordering PCBs?
```

**Returns:** Complete checklist covering:
- Design verification (DRC, footprints, values)
- Manufacturing files (Gerber, drill, BOM, position)
- Manufacturer specifications
- Final review steps

**Example:**
```
User: "I'm ready to order PCBs, what should I check?"

AI invokes: fabrication_checklist prompt

AI: "Here's your pre-fabrication checklist:
- Run DRC (no errors)
- All components have footprints
- Export Gerber files
- ..."
```

## Complete Workflow Examples

### Example 1: Quick Fabrication Export

```
User: "I need to send this board to JLCPCB for fabrication"

AI: "I'll create a complete fabrication package for JLCPCB..."

[Calls export_fabrication_package with jlcpcb preset]

AI: "Done! Created fabrication_jlcpcb_20250121_143052.zip with:
- 9 Gerber files (all layers)
- Drill files (PTH and NPTH)
- BOM (25 unique parts)
- Position file (42 components)

The ZIP file is ready to upload to JLCPCB!"
```

### Example 2: Step-by-Step Export

```
User: "Export Gerber files"

AI: [Calls export_gerber]
"Exported 9 Gerber files to ./gerber/"

User: "Now export drill files"

AI: [Calls export_drill_files]
"Exported drill files (PTH and NPTH separated)"

User: "Create a BOM too"

AI: [Calls export_bom]
"BOM exported with 25 unique parts, 42 total components"
```

### Example 3: Pre-Fabrication Verification

```
User: "Check if my board is ready for fabrication"

AI: "Let me verify your design..."

[Calls run_drc]

AI: "DRC check found 2 errors:
1. Clearance violation between tracks
2. Track width below minimum

Please fix these before fabricating."

User: "I fixed them, check again"

AI: [Calls run_drc again]
"Perfect! No DRC errors. Your board is ready for fabrication."

[Calls fabrication_checklist]

AI: "Here's your pre-fabrication checklist..."
```

### Example 4: Assembly Package

```
User: "Prepare files for PCB assembly"

AI: "I'll create a complete package for assembly..."

[Calls export_fabrication_package]
[Calls export_bom]
[Calls export_position_file]

AI: "Assembly package ready:
- Gerber files for PCB fabrication
- Drill files
- BOM with 25 parts
- Position file for pick-and-place machine
- Everything packaged in fabrication_generic_20250121.zip

Your board has 42 components total, all on the top layer."
```

## Manufacturer-Specific Notes

### JLCPCB

```
User: "Export for JLCPCB"
```

- Use `manufacturer_preset="jlcpcb"`
- JLCPCB accepts standard Gerber RS-274X
- BOM should use LCSC part numbers if using assembly
- Position file in CSV format is accepted

### PCBWay

```
User: "Prepare files for PCBWay"
```

- Use `manufacturer_preset="pcbway"`
- Supports extended Gerber (RS-274X)
- Include Gerber job file (.gbrjob)

### OSH Park

```
User: "Export for OSH Park"
```

- Use `manufacturer_preset="oshpark"`
- Simpler requirements
- Can upload individual Gerber files

### Generic

```
User: "Export fabrication files"
```

- Use `manufacturer_preset="generic"` (default)
- Standard Gerber RS-274X format
- Works with most manufacturers

## File Naming Conventions

The server automatically names files according to KiCad standards:

**Gerber files:**
- `project-F_Cu.gbr` - Front copper
- `project-B_Cu.gbr` - Back copper
- `project-F_Mask.gbr` - Front solder mask
- etc.

**Drill files:**
- `project-PTH.drl` - Plated holes
- `project-NPTH.drl` - Non-plated holes

**Other files:**
- `bom.csv` - Bill of Materials
- `position.csv` - Component positions

## Troubleshooting

### "No PCB board is open"

**Solution:** Open a `.kicad_pcb` file in KiCad PCBNew before running the server.

### Empty Gerber files

**Solution:**
- Ensure board has traces/copper on the layers
- Check that board outline (Edge.Cuts) is defined
- Verify components are placed

### Missing drill files

**Solution:**
- Ensure footprints have through-hole pads
- Check that holes are properly defined in footprints

### BOM missing values

**Solution:**
- Assign values to all components in schematic
- Update PCB from schematic (Tools → Update PCB from Schematic)

### Position file has wrong origin

**Solution:**
- Set auxiliary origin in PCBNew if needed (Place → Drill and Place Offset)
- Or use default origin (bottom-left of board)

## Best Practices

1. **Always run DRC first**
   ```
   User: "Run DRC before I export"
   ```

2. **Use the checklist**
   ```
   User: "Show me the fabrication checklist"
   ```

3. **Use the all-in-one export**
   ```
   User: "Create complete fabrication package"
   ```
   This ensures nothing is forgotten!

4. **Verify files with Gerber viewer**
   - Use KiCad's Gerber Viewer (Tools → Gerber Viewer)
   - Or online tools like https://www.pcbway.com/project/OnlineGerberViewer.html

5. **Keep fabrication files organized**
   ```
   output/
   ├── fabrication_20250121/
   │   ├── gerber/
   │   ├── drill/
   │   ├── bom.csv
   │   └── position.csv
   └── fabrication_20250121.zip
   ```

6. **Document your stackup**
   - Include layer stackup information
   - Specify material (FR4, etc.)
   - Specify finish (HASL, ENIG, etc.)

## Advanced Tips

### Custom layer selection

```
User: "Export only copper layers"

AI calls: export_gerber(
    output_dir="./copper_only",
    layers=["F.Cu", "B.Cu"]
)
```

### Multiple manufacturer packages

```
User: "Create packages for both JLCPCB and PCBWay"

AI creates two separate packages:
- fabrication_jlcpcb_TIMESTAMP.zip
- fabrication_pcbway_TIMESTAMP.zip
```

### Batch processing

```
User: "Fill zones, run DRC, then export if no errors"

AI: [Fills zones] → [Runs DRC] → checks result → [Exports if clean]
```

## Integration with AI Workflows

The AI can chain multiple tools together intelligently:

```
User: "Prepare my board for manufacturing"

AI workflow:
1. Get board info → understand project
2. Run DRC → check for errors
3. Fill zones → ensure copper pours are current
4. Run DRC again → verify no new errors
5. Export fabrication package → create all files
6. Show checklist → final verification

AI: "Your board is ready! Here's what I did:
- Filled all copper zones (GND, VCC)
- Ran DRC: 0 errors, 0 warnings ✓
- Exported complete fabrication package
- 25 unique parts, 42 components total
- Ready to send to manufacturer"
```

## See Also

- [README.md](README.md) - Main documentation
- [QUICKSTART.md](QUICKSTART.md) - Getting started guide
- [EXAMPLES.md](EXAMPLES.md) - Usage examples
- [KiCad Documentation](https://docs.kicad.org/) - Official KiCad docs

## Support

For issues with fabrication tools, check:
1. KiCad PCBNew is open with a board loaded
2. Server is running in correct mode (not mock)
3. Output directories exist and are writable
4. Board has necessary elements (traces, components, etc.)

Happy fabricating! 🎉
