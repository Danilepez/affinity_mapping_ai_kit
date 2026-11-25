from pathlib import Path
import json,re,hashlib,collections
R=Path('06_resultados'); rows=json.loads((R/'soporte/fragmentos.json').read_text(encoding='utf-8')); by={r['ref']:r for r in rows}; cats=json.loads((R/'soporte/categorias.json').read_text(encoding='utf-8')); clusters=json.loads((R/'soporte/clusters.json').read_text(encoding='utf-8'))
assert len(by)==len(rows)==130
sources={p.name[:3]:p for p in Path('02_entrevistas').glob('E*.md')}; assert len(sources)==16
for e,p in sources.items(): assert f'Código: {e}' in p.read_text(encoding='utf-8-sig')
for r in rows: assert r['cita'] in sources[r['entrevista']].read_text(encoding='utf-8-sig')
covered={ref for c in cats for ref in c['refs']}; print('Fragmentos sin categoría:',sorted(set(by)-covered))
for p in R.glob('0*.md'):
 s=p.read_text(encoding='utf-8').replace('no nueve casos insatisfechos','no ocho casos insatisfechos')
 for ref in re.findall(r'E\d{2}-F\d{2}',s): assert ref in by,(p,ref)
 p.write_text(s,encoding='utf-8')
for c in clusters:
 n=len({by[ref]['entrevista'] for ref in c['refs']}); assert c['puntajes'][0]==(1 if n<=2 else 2 if n<=8 else 3)
# Jerarquía coherente en el consolidado: una raíz y tres bloques con subsecciones subordinadas.
p=R/'00_analisis_completo.md'; s=p.read_text(encoding='utf-8'); lines=s.splitlines(); level=False; result=[]
for l in lines:
 if l.startswith('## Codificación axial') or l.startswith('## Affinity map') or l.startswith('## Tensiones y recomendaciones'):
  level=True; result.append(l)
 elif level and l.startswith('#'): result.append('#'+l)
 else: result.append(l)
p.write_text('\n'.join(result)+'\n',encoding='utf-8')
audit=['# Trazabilidad de la actualización\n\n25 de noviembre de 2026. 16 archivos, 130 fragmentos, 102 códigos, ocho categorías axiales y ocho clusters. Citas cotejadas literalmente contra Markdown; audio original no revisado.\n\n## Identificadores\n\nAntigua E01 (sistema de escritorio) → E15. Antigua E02 (hijo del dueño) → E16. Se ajustaron título y Código de esos dos archivos, sin editar respuestas. Los identificadores de fragmento fueron reconstruidos: no usar los antiguos F como correspondencia automática. La versión de dos entrevistas está en `historico/analisis_2_entrevistas`.\n\n## Corpus verificado\n\n| Código | Archivo | Fragmentos | SHA256 del archivo |\n|---|---|---|---|']
for e,p in sorted(sources.items()): audit.append(f'| {e} | {p.name} | {sum(r["entrevista"]==e for r in rows)} | {hashlib.sha256(p.read_bytes()).hexdigest()} |')
audit+=['\n## Verificaciones\n\n- Dieciséis códigos de entrevista únicos, consistentes con sus encabezados.\n- 130 citas exactas en las fuentes actuales; tipos e intensidad registrados.\n- Referencias completas en resultados existentes en la codificación abierta.\n- Frecuencia por cluster calculada por entrevistas distintas, no por fragmentos.\n- Contraste de HU, HP, HUrg y S1–S15; denominadores originales del taller conservados.\n- Resultados anteriores archivados; ejemplo de ahorro excluido.\n- Sin búsquedas web: las afirmaciones técnicas, económicas o legales de participantes se tratan como relatos, no hechos comprobados.\n']
(R/'05_trazabilidad_y_revision.md').write_text('\n'.join(audit),encoding='utf-8')
(R/'README.md').write_text('''# Resultados actualizados de Qhatu

Actualización del 25 de noviembre de 2026: 16 entrevistas, 130 fragmentos textuales verificados, 102 códigos, ocho categorías y ocho clusters.

## Documentos

- [Análisis completo](00_analisis_completo.md): consolidado de la cadena, con las secciones del prompt 00.
- [Codificación abierta](01_codificacion_abierta.md): una tabla por entrevista y libro de códigos.
- [Codificación axial](02_codificacion_axial.md): relaciones y contraste preliminar.
- [Affinity map](03_affinity_map.md): patrones, frecuencias y priorización.
- [Tensiones y recomendaciones](04_tensiones_y_recomendaciones.md): hipótesis, pruebas propuestas y problem statement.
- [Trazabilidad y revisión](05_trazabilidad_y_revision.md): correspondencia de identificadores y corpus verificado.

## Lectura de los resultados

Registrar sin frenar atención, controlar rotación/fechas y habilitar a todos los operadores son prioridades de prueba. Persisten casos que consideran suficiente su método. Los impagos históricos no validan pérdidas mensuales y el pago por alternativas no valida pago por Qhatu.

Las entrevistas anteriores son ahora E15/E16. La versión previa se conserva en [histórico](historico/analisis_2_entrevistas/README.md). Los archivos de contexto se actualizaron al corpus actual; hipótesis y metas originales se mantienen. E14 es florería, E02/E06 tienen estructuras más complejas y E12 muy baja actividad: no tratar los 16 como un segmento homogéneo.

Se ejecutó la cadena 01–04 y luego se consolidó el resultado. El prompt 00 es una alternativa rápida; aquí sus secciones se completaron con la cadena revisada. Los experimentos son propuestas, no actividades realizadas.

Los datos estructurados y auxiliares de generación están en `soporte`. Las transcripciones en `02_entrevistas` son la fuente de citas; no se cotejó audio original.
''',encoding='utf-8')
print('Verificación final: 16 fuentes, 130 citas, referencias y frecuencias correctas.')
