# Índice de Archivos de Fabricación

## 📦 Archivo Principal

**Para fabricación, usa este archivo ZIP:**

```
olivia_v0.2_fabrication_20251021_154253.zip (140 KB)
```

Este ZIP contiene TODOS los archivos necesarios para fabricar la placa.

## 📁 Estructura de Archivos

```
fabrication_output/
│
├── 📦 olivia_v0.2_fabrication_20251021_154253.zip   ← ARCHIVO PRINCIPAL
│
├── 📂 olivia_v0.2_20251021_154253/
│   │
│   ├── 📂 gerber/                (9 archivos Gerber)
│   │   ├── v0.2-F_Cu.gbr         Cobre superior
│   │   ├── v0.2-B_Cu.gbr         Cobre inferior
│   │   ├── v0.2-F_Mask.gbr       Máscara superior
│   │   ├── v0.2-B_Mask.gbr       Máscara inferior
│   │   ├── v0.2-F_SilkS.gbr      Serigrafía superior
│   │   ├── v0.2-B_SilkS.gbr      Serigrafía inferior
│   │   ├── v0.2-F_Paste.gbr      Pasta superior
│   │   ├── v0.2-B_Paste.gbr      Pasta inferior
│   │   └── v0.2-Edge_Cuts.gbr    Contorno
│   │
│   ├── 📂 drill/                 (2 archivos de taladrado)
│   │   ├── v0.2-PTH.drl          Agujeros metalizados
│   │   └── v0.2-NPTH.drl         Agujeros no metalizados
│   │
│   ├── 📄 bom.csv                Lista de materiales (35 partes)
│   ├── 📄 position.csv           Posiciones (51 componentes)
│   └── 📄 FABRICATION_SUMMARY.txt Resumen
│
├── 📖 OLIVIA_FABRICATION_README.md  Documentación completa
└── 📋 INDEX.md                      Este archivo
```

## 🎯 Guía Rápida

### Para Fabricar Solo el PCB

1. Subir: `olivia_v0.2_fabrication_20251021_154253.zip`
2. Configurar: 2 capas, 1.6mm grosor, acabado HASL o ENIG
3. Ordenar

### Para Fabricar + Ensamblar

1. Subir ZIP para el PCB
2. Subir `bom.csv` como lista de materiales
3. Subir `position.csv` como archivo de posiciones
4. Seleccionar componentes disponibles en stock
5. Ordenar PCB + ensamblaje

## 📊 Especificaciones

- **Dimensiones**: 90 x 100 mm
- **Capas**: 2 (doble cara)
- **Componentes**: 51 total, 35 únicos
- **Grosor recomendado**: 1.6mm
- **Acabado**: HASL sin plomo o ENIG

## 🏭 Fabricantes Recomendados

1. **JLCPCB** - Económico, 5 días
   - https://jlcpcb.com/
   - Ensamblaje SMT disponible

2. **PCBWay** - Calidad premium
   - https://www.pcbway.com/
   - Más opciones de acabado

3. **OSH Park** - Alta calidad, USA
   - https://oshpark.com/
   - Acabado ENIG incluido

## ⚠️ Advertencias

Esta placa maneja **220V AC**:
- Verificar aislamiento entre alta y baja tensión
- Usar grosor de cobre adecuado (1 oz mínimo)
- Confirmar clearances con el fabricante
- Componentes críticos: verificar disponibilidad

## 📧 Componentes Principales

| Componente | Descripción | Cantidad |
|------------|-------------|----------|
| ESP32-WROOM-32D | MCU WiFi/BT | 1 |
| HLK-10M05 | Fuente 220V→5V | 1 |
| BTA16-800B | TRIAC 16A | 2 |
| AMS1117-3.3 | Regulador 3.3V | 1 |
| DB107S | Puente rectificador | 1 |

## 🔗 Enlaces Útiles

- **Visor Gerber Online**: https://www.pcbway.com/project/OnlineGerberViewer.html
- **Calculadora de PCB**: https://www.4pcb.com/pcb-trace-width-calculator.html
- **KiCad Docs**: https://docs.kicad.org/

## ✅ Checklist Pre-Fabricación

- [ ] Verificar archivos Gerber (9 archivos)
- [ ] Verificar archivos drill (2 archivos)
- [ ] Visualizar Gerbers en visor
- [ ] Confirmar dimensiones (90x100mm)
- [ ] Revisar BOM - componentes disponibles
- [ ] Verificar clearances 220V
- [ ] Elegir fabricante
- [ ] Configurar especificaciones
- [ ] Hacer pedido

---

**Generado**: 2025-10-21
**Proyecto**: Olivia Control v0.2
**Estado**: ✅ Listo para fabricación
