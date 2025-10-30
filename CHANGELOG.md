# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Auto-routing support
- Web UI for visual interaction
- Component database integration (Octopart, LCSC)
- Multi-board project support
- Enhanced DRC with custom rules
- 3D model management

## [1.0.0] - 2025-10-21

### Added

#### Core Features
- Complete MCP server implementation for KiCad PCB design
- AI client using Claude 3.5 Sonnet for natural language interaction
- 12 comprehensive tools for PCB design and fabrication
- Async/await architecture throughout
- Mock mode for testing without KiCad

#### Fabrication Tools
- `export_gerber`: Export Gerber files (RS-274X format, all standard layers)
- `export_drill_files`: Export drill files (Excellon format, PTH/NPTH)
- `export_fabrication_package`: Complete fabrication package as ZIP
- `export_bom`: Bill of Materials export (CSV format)
- `export_position_file`: Pick-and-place positions (CSV format)

#### Verification & Layout Tools
- `run_drc`: Design Rule Check integration
- `fill_zones`: Copper zone management
- `get_track_info`: Track/trace information

#### Basic Tools
- `place_component`: Precise component placement
- `list_components`: Component enumeration with positions
- `read_netlist`: Netlist information
- `get_board_info`: Board specifications

#### Flatpak Integration
- Full KiCad 9.0.5 Flatpak support
- `run_with_flatpak.sh`: Launcher script with filesystem access
- `kicad_flatpak_setup.sh`: Automatic dependency installer
- `check_kicad.py`: Environment checker with auto-detection

#### Testing
- 20 comprehensive tests covering all tools
- `test_server.py`: Basic server tests
- `test_fabrication.py`: Extended fabrication tests
- 100% test pass rate

#### Documentation
- `README.md` (11KB): Complete user guide
- `FABRICATION.md` (13KB): Fabrication tools documentation
- `QUICKSTART.md`: 5-minute setup guide
- `PROJECT_STATUS.md`: Implementation summary
- `SUMMARY.md`: Technical overview
- `CONTRIBUTING.md`: Development guidelines

#### Example Project
- Olivia Control v0.2 fabrication files included
- Complete Gerber set, drill files, BOM, and position file
- Ready-to-manufacture ZIP package

### Technical Details
- **Compatibility**: KiCad 9.0.5, Python 3.10+
- **AI Model**: Claude 3.5 Sonnet
- **Protocol**: Model Context Protocol (MCP) 1.0+
- **Platforms**: Linux (primary), macOS/Windows (untested)

### Known Limitations
- DRC integration is basic (requires KiCad 7+ API for full support)
- Auto-routing not yet implemented
- Single board per session
- No direct 3D model management

---

## Version History

### Release Notes - v1.0.0

First stable release of KiCad MCP Integration.

**Highlights:**
- Production-ready AI-assisted PCB design
- Complete fabrication workflow
- Flatpak support for KiCad 9.0.5
- Comprehensive documentation
- 20/20 tests passing

**Use Cases:**
- AI-assisted PCB design and layout
- Automated fabrication file generation
- Manufacturing preparation
- Component placement optimization
- PCB design education

**Tested With:**
- Olivia Control v0.2 (51 components, 90x100mm, 2-layer board)
- KiCad 9.0.5 Flatpak on Linux Mint 22.2
- Fabrication compatibility: JLCPCB, PCBWay, OSH Park

---

## Links

- **Repository**: https://github.com/Pablomonte/MCP-KiCad
- **Issues**: https://github.com/Pablomonte/MCP-KiCad/issues
- **Releases**: https://github.com/Pablomonte/MCP-KiCad/releases

[Unreleased]: https://github.com/Pablomonte/MCP-KiCad/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/Pablomonte/MCP-KiCad/releases/tag/v1.0.0
