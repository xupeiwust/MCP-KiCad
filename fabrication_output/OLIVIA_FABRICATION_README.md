# Olivia Control v0.2 - Archivos de Fabricación

Archivos de fabricación generados para la placa Olivia Control v0.2

## Información del Proyecto

- **Proyecto**: Olivia Control v0.2 - Sistema de Control de Incubadora
- **Origen**: `/home/pablo/repos/Proyecto-Incubadora/HardWare/Electro/Olivia_control/v0.2/`
- **Generado**: 2025-10-21 15:42:54
- **Herramienta**: KiCad MCP Fabrication Tools

## Especificaciones de la Placa

- **Tamaño**: 90.0 x 100.0 mm
- **Capas**: 2 capas (doble cara)
- **Componentes**: 51 total (35 únicos)
- **Tipo**: PCB para control de incubadora con ESP32

## Archivos Incluidos

### Paquete ZIP Principal
📦 **`olivia_v0.2_fabrication_20251021_154253.zip`** (140 KB)

Contiene TODOS los archivos necesarios para fabricación:

### 1. Archivos Gerber (9 archivos)
Formato: RS-274X estándar

- **v0.2-F_Cu.gbr** (152 KB) - Capa de cobre superior
- **v0.2-B_Cu.gbr** (176 KB) - Capa de cobre inferior
- **v0.2-F_Mask.gbr** (11 KB) - Máscara de soldadura superior
- **v0.2-B_Mask.gbr** (11 KB) - Máscara de soldadura inferior
- **v0.2-F_SilkS.gbr** (79 KB) - Serigrafía superior
- **v0.2-B_SilkS.gbr** (177 KB) - Serigrafía inferior
- **v0.2-F_Paste.gbr** (5.5 KB) - Pasta de soldadura superior
- **v0.2-B_Paste.gbr** (5.8 KB) - Pasta de soldadura inferior
- **v0.2-Edge_Cuts.gbr** (2.6 KB) - Contorno de la placa

### 2. Archivos de Taladrado (2 archivos)
Formato: Excellon

- **v0.2-PTH.drl** (2.6 KB) - Agujeros pasantes metalizados
- **v0.2-NPTH.drl** (265 B) - Agujeros pasantes no metalizados

### 3. Lista de Materiales (BOM)
**bom.csv** (2 KB)

Lista completa de componentes con:
- Referencias
- Valores
- Footprints
- Cantidades

**Componentes principales**:
- ESP32-WROOM-32D (microcontrolador)
- HLK-10M05 (fuente AC-DC)
- BTA16-800B (2x TRIACs para control de potencia)
- AMS1117-3.3 (regulador de voltaje)
- DB107S (puente rectificador)
- Resistencias, capacitores, conectores, etc.

### 4. Archivo de Posiciones
**position.csv** (4.3 KB)

Coordenadas de todos los componentes para máquina pick-and-place:
- Designador
- Valor
- Paquete
- Posición X, Y (mm)
- Rotación (grados)
- Capa (Top/Bottom)

### 5. Resumen de Fabricación
**FABRICATION_SUMMARY.txt**

Resumen completo de especificaciones y archivos incluidos.

## Fabricantes Compatibles

Este paquete es compatible con:

- ✅ **JLCPCB** (https://jlcpcb.com/)
- ✅ **PCBWay** (https://www.pcbway.com/)
- ✅ **OSH Park** (https://oshpark.com/)
- ✅ **Cualquier fabricante que acepte Gerber RS-274X**

## Instrucciones de Pedido

### Para JLCPCB

1. Ir a https://jlcpcb.com/quote
2. Subir el archivo ZIP: `olivia_v0.2_fabrication_20251021_154253.zip`
3. Configurar especificaciones:
   - **PCB Qty**: Cantidad deseada (mínimo 5)
   - **Layers**: 2
   - **PCB Thickness**: 1.6mm (estándar)
   - **Surface Finish**: HASL (económico) o ENIG (mejor calidad)
   - **Copper Weight**: 1 oz (estándar)
4. Si deseas ensamblaje SMT:
   - Activar "SMT Assembly"
   - Subir `bom.csv` como BOM
   - Subir `position.csv` como CPL (Component Placement List)
   - Seleccionar componentes disponibles en stock de JLCPCB

### Para PCBWay

1. Ir a https://www.pcbway.com/orderonline.aspx
2. Subir el archivo ZIP
3. PCBWay detectará automáticamente las especificaciones
4. Revisar y confirmar:
   - Dimensiones: 90 x 100 mm
   - Capas: 2
   - Acabado superficial: según preferencia

### Para OSH Park

1. Ir a https://oshpark.com/
2. Subir los archivos Gerber individualmente o el ZIP
3. Especificaciones se detectan automáticamente
4. Nota: OSH Park produce placas de 2 capas con acabado ENIG

## Verificación Pre-Fabricación

Antes de enviar a fabricar, verificar:

- ✅ Todos los archivos Gerber están incluidos (9 archivos)
- ✅ Archivos de taladrado presentes (PTH y NPTH)
- ✅ Dimensiones correctas (90 x 100 mm)
- ✅ Número de capas correcto (2)
- ✅ BOM completa y actualizada
- ✅ Posiciones de componentes correctas

**Recomendación**: Visualizar los Gerber con el visor del fabricante o con:
- KiCad Gerber Viewer
- Gerbv (https://gerbv.github.io/)
- Online: https://www.pcbway.com/project/OnlineGerberViewer.html

## Especificaciones Recomendadas

Para fabricación estándar:

```
Dimensiones: 90 x 100 mm
Capas: 2
Grosor: 1.6 mm
Material: FR-4
Acabado: HASL sin plomo o ENIG
Peso del cobre: 1 oz (35 µm)
Máscara de soldadura: Verde (estándar)
Serigrafía: Blanca
Agujeros mínimos: Según Excellon (verificar con fabricante)
Separación mínima: 0.15 mm (verificar)
```

## Consideraciones Especiales

### Control de Potencia AC
La placa incluye:
- TRIACs BTA16-800B para control de cargas 220V AC
- Diseño con aislamiento adecuado entre alta y baja tensión
- ⚠️ **IMPORTANTE**: Revisar separaciones y clearances según normativa local

### Fuente de Alimentación
- Módulo HLK-10M05 (AC-DC 220V → 5V)
- Entrada directa de 220V AC
- Protección con fusible 500mA

### Componentes Críticos
- Verificar disponibilidad de HLK-10M05, ESP32-WROOM-32D
- Los TRIACs y puente rectificador deben soportar las especificaciones

## Contenido del Directorio

```
fabrication_output/
├── olivia_v0.2_20251021_154253/
│   ├── gerber/
│   │   └── 9 archivos .gbr
│   ├── drill/
│   │   └── 2 archivos .drl
│   ├── bom.csv
│   ├── position.csv
│   └── FABRICATION_SUMMARY.txt
├── olivia_v0.2_fabrication_20251021_154253.zip
└── OLIVIA_FABRICATION_README.md (este archivo)
```

## Generación

Estos archivos fueron generados automáticamente usando:
- **KiCad** 9.0.5 (Flatpak)
- **MCP KiCad Integration** - Fabrication Tools
- **Script**: `generate_olivia_fabrication.py`

El script lee el archivo `.kicad_pcb` del proyecto Olivia y genera todos los archivos de fabricación sin modificar el proyecto original.

## Soporte

Para preguntas sobre:
- **Archivos de fabricación**: Revisar documentación de KiCad
- **Proyecto Olivia**: Ver repositorio Proyecto-Incubadora
- **Fabricantes**: Contactar soporte del fabricante elegido

## Licencia

Los archivos de fabricación están sujetos a la licencia del proyecto Olivia Control.

---

**Generado el**: 2025-10-21
**Versión del PCB**: v0.2
**Estado**: ✅ Listo para fabricación

🎉 **¡Listo para enviar a fabricar!**
