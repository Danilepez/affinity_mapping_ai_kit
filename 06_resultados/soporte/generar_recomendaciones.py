from pathlib import Path
import json
R=Path('06_resultados'); rows=json.loads((R/'soporte/fragmentos.json').read_text(encoding='utf-8'))
verdicts=[
('HU','Sin evidencia suficiente','E09 declara 70 años; E06-F05 indica 3–4 personas; E14 es florería; E16 es hijo. Perfil propuesto no describe toda la muestra.','Confundir entrevistas heterogéneas con 16 compradores objetivo.'),
('HP','Respaldada parcialmente; no generalizable','E10-F02 y E10-F04: omisiones con afluencia; E11-F09: sobrecarga. E13-F01 y E15-F05 son contraejemplos de suficiencia. Ganancias y saldos no auditados.','Extender el mecanismo de E10 a toda tienda manual.'),
('HUrg','Sin evidencia suficiente','E01-F03 aporta 30–45 minutos de cierre; E02-F05 contrata desarrollo; E14-F04 busca desarrollador. No hay compromiso/pago de Qhatu ni medición uniforme.','Equiparar problema, intención y compromiso comercial.'),
('S1','Contradicha como descripción universal','E02-F02, E06-F06 y E15-F01: sistemas; E05-F02: práctica mixta. Manualidad no acredita falta de confiabilidad.','Seleccionar solo casos sin software.'),
('S2','Sin evidencia suficiente para la hipótesis mensual','E01-F05, E03-F04 y E11-F11 relatan impagos pasados. Ninguno acredita simultáneamente último mes, frecuencia semanal y monto mensual de al menos Bs 100.','Transformar deuda histórica o préstamo en pérdida mensual por mala anotación.'),
('S3','Sin evidencia suficiente','E15-F03: Bs 700 mensuales por otra solución; E06-F02/F03: instalación de Bs 8.000–10.000 sin mensualidad; E10-F08: precio recordado Bs 50. Cero preventas de Qhatu documentadas.','Inferir precio aceptable de Qhatu desde alternativas distintas.'),
('S4','Contradicha en E10 como promesa general; umbral pendiente','E10-F07 deja el teléfono; E10-F10 explica enfoque lento. No se probó la condición de menos de 10 segundos ni el piloto 4/5.','Confundir escaneo de computadora con móvil y funciones disponibles con uso sostenido.'),
('S5','Sin evidencia suficiente','E02-F02/E15-F02 usan lector; no se contó proporción de ventas o surtido con códigos.','Tomar existencia del lector como cobertura mayoritaria.'),
('S6','Sin evidencia suficiente','No hay inventario de Android/cámara funcional por entrevistado. E01-F07 además describe barrera de uso.','Suponer dispositivo y autonomía por cobrar QR.'),
('S7','Respaldada parcialmente','E08-F05 relata señal irregular al operar pedidos digitales. E15 describe internet del cliente o banco; no equivale a señal de tienda. No hay prueba offline.','Prometer que modo sin internet resolverá pagos bancarios.'),
('S8','Respaldada parcialmente','E11-F07 desea mejorar surtido y E11-F09 expresa carga mental; E06-F06 usa ventas para control. E16-F01 por sí solo no acredita deseo.','Confundir desconocer ranking con pedir reportes.'),
('S9','Respaldada parcialmente y con contraejemplos','E05-F05/E14-F03: desajuste; E06-F07: límite; E15-F05 satisfecho y E10-F09 funciones útiles. Precio en E07-F05 descartado; cobertura de fiado no evaluada.','Generalizar que todo software es caro, complejo o no incluye crédito.'),
('S10','Sin evidencia suficiente','E04-F04 confirma dueña operadora; E16-F09 familiar usuario; compras y autoridad no comprobadas en conjunto.','Confundir encargado con decisor económico.'),
('S11','Sin evidencia suficiente','No hay entrevistas a clientes sobre registro o envío de saldos. E10-F04 solo muestra ayuda recordando consumo.','Inferir consentimiento del cliente a partir del tendero.'),
('S12','Sin evidencia suficiente','E07-F06 conteo ambiguo; E06-F07 límite de sistema, no prueba de alta inicial de 100 productos ni abandono del usuario.','Confundir rendimiento técnico con disposición a cargar inventario.'),
('S13','Sin evidencia suficiente','La pregunta en E05 sugiere perder hojas; respuesta E05-F02 dice que todo tranquilo. No expresa temor a pérdida.','Codificar la pregunta como necesidad del entrevistado.'),
('S14','Respaldada parcialmente','E08-F08/F09, E15-F07/F08 y E16-F09: QR utilizado, con fricciones y dependencia. No hay serie temporal de crecimiento.','Convertir presencia de QR en dominio digital del dueño.'),
('S15','Respaldada parcialmente; heterogénea','E08-F07 pareja, E14-F06 único y E13-F05 sobrecarga anticipada; E06-F05 tres o cuatro. Tiempo administrativo no medido uniformemente.','Suponer mismo tamaño y falta de tiempo en todos.')]
table='| Hipótesis | Veredicto | Evidencia clave | Riesgo de sesgo de confirmación |\n|---|---|---|---|\n'+'\n'.join('| '+' | '.join(r)+' |' for r in verdicts)
p='''# Tensiones y recomendaciones de Qhatu

Actualización al 25 de noviembre de 2026. Corpus de 16 entrevistas; las antiguas E01/E02 son ahora E15/E16. No hay pilotos, ofertas ni cobros nuevos realizados durante este análisis.

## 1. Tensiones y contradicciones detectadas

### Funciones útiles que no sostienen el uso

E10 reconoce alertas y descuento automático de inventario (E10-F09), pero deja el teléfono para no empeorar el servicio (E10-F07) y relata demora de enfoque (E10-F10). Es una tensión real dentro del mismo relato, no prueba observada de rendimiento. Qhatu necesita validar captura durante la atención, además de utilidad del reporte.

### Registro manual aceptado con necesidad puntual

E04 justifica su método por tamaño (E04-F03), pero ordenar facturas por fechas le resulta problemático (E04-F07). E16 acepta el cuaderno (E16-F06), sin control de fechas (E16-F04). E14 está habituado y no satisfecho con el alcance (E14-F07). Aceptación no equivale a exactitud, pero tampoco debe reinterpretarse como dolor oculto obligatorio.

### El fiado puede ser un problema de cobro y política

E01/E03/E11 relatan impago pasado (E01-F05, E03-F04, E11-F11); E03 y E11 limitan exposición (E03-F05, E11-F12). En E10 el cliente recuerda consumos omitidos (E10-F04). Son mecanismos distintos: una mejor anotación puede ayudar a olvidar menos, sin asegurar que el deudor pague. Crédito empresarial en E01-F04 no es equivalente a fiado vecinal.

### Quien quiere digitalizar no siempre puede operarlo solo

E01 describe que un integrante frena la adopción (E01-F07); E16 concentra QR (E16-F09). E06 sí utiliza software para conocer ventas del personal (E06-F06), y E13 consideraría sistema al contratar (E13-F06). El usuario y comprador no pueden asumirse como una sola persona ni como un operador único.

### Precio y complejidad no explican todas las decisiones

E07 rechaza que el precio sea la barrera (E07-F05). E15 paga mensualmente y está satisfecho (E15-F03, E15-F05); E06 paga instalación pero reporta límite de carga (E06-F02, E06-F07). E02 contrata un desarrollo (E02-F05). La competencia debe analizarse por tarea, continuidad y servicio, no solo por precio nominal.

### El dolor principal puede quedar fuera del producto

E09 apenas paga alquiler (E09-F08), E12 describe mínima venta y función de distracción (E12-F01, E12-F03), y E14 limita abastecimiento por bloqueos (E14-F08). Esto contrasta con el supuesto del equipo de que el registro explica las pérdidas. Son relatos de contexto, no verificación económica ni legal. Evitar atribuir a una app la solución de factores externos.

### El muestreo y el guion pueden moldear las conclusiones

E07 introduce situación económica y el entrevistador redirige hacia stock; E10 corrige la suposición de que nunca usó software. En E04 se sugieren omisiones y necesidad de optimización, y en E14 se propone la palabra caducidad. Conservar esas intervenciones en la lectura impide confundir respuestas inducidas con necesidades espontáneas. E09/E12 aportan límites del segmento y no deben descartarse solo por falta de urgencia digital.

## 2. Contraste con hipótesis del equipo

Los veredictos son locales a este corpus. Respaldo parcial no significa cumplimiento del umbral. “Sin evidencia suficiente” tampoco significa que el fenómeno no exista.

'''+table+'''

### Estado de las métricas del Taller 3

- Hay 16 transcripciones, pero una florería y otros perfiles fuera del segmento supuesto. No afirmar que ya hay 16/20 entrevistas elegibles para todas las hipótesis.
- S2 conserva 12/20 con fiado semanal y caso del último mes, y 8/20 con pérdida mensual de al menos Bs 100. Hay tres relatos de impago pasado; cero casos documentan todos los atributos requeridos. Es cero documentación calificable, no cero pérdidas reales.
- HU y HP requieren datos de perfil y demostración de registros que no se recogieron uniformemente. No se pueden computar tasas válidas a partir de silencios.
- HUrg: E01 declara tiempo de cierre compatible con la condición temporal, pero no hay compromisos ni base homogénea para concluir 10/20 y 5/20.
- S4 y S3 necesitan piloto y pago real. No hay datos nuevos que permitan evaluar 4/5 con cobertura sostenida ni 3/5 preventas. Se conservan los denominadores originales.

## 3. Recomendaciones estratégicas

### Qué investigar más

1. **Captura y rapidez — C1:** observar un periodo de afluencia en E10 y casos similares. Contar transacciones reales, omitidas y registradas; medir tiempo, errores y espera. Comparar cámara, búsqueda y flujo habitual. Preguntar por el último abandono, no “¿usaría nuestra app?”.
2. **Fechas y compras — C2:** reconstruir último producto vencido o inmovilizado, unidades, costo, devolución y fecha de recepción. Separar demanda variable de falta de seguimiento. E10 y E16 son casos de abarrotes; E14 requiere otra prueba.
3. **Operadores — C4:** probar la misma tarea con quien decide, quien atiende y quien cubre ausencias. Identificar permisos, ayuda requerida y aceptación del registro por turno. No excluir por edad ni presuponer competencia digital.
4. **Alternativas — C3:** pedir a E02 una lista de tareas concretas que motivaron contratación, a E06 reproducir límite de carga y a E01 aclarar transición de sistema. Verificar cuándo E10 pagó o solo probó la app; no usar Bs 50 como transacción confirmada.
5. **Fiado — C7:** en quienes aún fían, reconstruir último caso con fecha y saldo; diferenciar mala captura, disputa y falta de pago. Preguntar a quienes dejaron de fiar qué cambió, sin sugerir que volver a fiar es deseable.
6. **QR — C6:** observar comprobación de abono y entrega. Diferenciar demora bancaria, señal de tienda, internet de cliente y manejo familiar. No usar una captura de pantalla como verificación de cobro ni prometer confirmación sin conexión.
7. **Precio, inventario y documentos:** E16-F07 justifica explorar consulta de precios, pero sigue siendo un solo caso explícito de olvido. E04-F07 indica una tarea documental; E07-F06 exige aclaración antes de tratarlo como barrera de carga.

### Qué hipótesis validar y experimentos sugeridos

Los umbrales siguientes son propuestas de investigación, no resultados ni compromisos del equipo. Fijarlos antes de probar; registrar también fallos y abandonos.

| Hipótesis | Experimento | Medida y criterio propuesto |
|---|---|---|
| HV1 La captura puede mantenerse sin perjudicar atención (C1) | Cinco tiendas con dolor de omisión; línea base y dos semanas con prototipo de captura | Conservar criterio original de 4/5 con al menos 70% de ventas en 10/14 días. Medir tiempo menor de 10 segundos por tarea y espera del cliente frente a línea base, sin aumentar errores. Contar ventas reales; importe de caja no es número de transacciones |
| HV2 Fechas visibles cambian decisiones de reposición o rotación (C2) | Cinco tiendas de abarrotes con perecederos, lote limitado; registrar línea base y seguimiento de cuatro semanas | Propuesta: 3/5 mantienen fechas en al menos 80% del lote y toman una decisión documentada. Medir descarte/devolución por unidad y costo; no atribuir ahorro causal sin controlar cambios de demanda |
| HV3 Todos los operadores pueden sostener captura (C4) | Incluir dueño, familiar y reemplazo de cada tienda piloto, con dispositivo habitual | Propuesta: cada operador completa 4/5 tareas representativas sin ayuda tras capacitación breve y no deja huecos sistemáticos por turno. Registrar tiempo de formación y dificultades |
| HV4 Una solución acotada supera la alternativa relevante (C3/C5) | Comparar la tarea prioritaria con el método actual; incluir un caso satisfecho como contraste | Propuesta: 3/5 tiendas muestran mejora medible y repiten uso voluntario en tres días distintos. Beneficio y uso antes de precio; no forzar migración de quien ya está satisfecho |
| S2 El fiado genera pérdida mensual por el problema supuesto (C7) | Completar entrevistas elegibles y volver a casos faltantes con registro o reconstrucción de último mes | Mantener 12/20 con caso y fiado semanal, 8/20 con al menos Bs 100; reportar por perfil. No sobrerrepresentar fiadores y vender el resultado como prevalencia general |
| S3 El comprador paga por continuar | Tras uso útil, oferta con condiciones claras al decisor | Mantener 3/5 pagos de Bs 20 por primer mes. Registrar pagos, rechazos y motivos; precio de competidor no cuenta como preventa |

### Qué segmentos priorizar

- **Primer piloto de captura e inventario:** tiendas de abarrotes con omisiones o seguimiento de fechas explícitos y responsable dispuesto a probar una tarea. E10 es el caso más informativo; E16 requiere confirmar dolor y decisión con el dueño. E11 ofrece señal sobre carga mental, pero combina bodega y comida preparada.
- **Prueba de adopción familiar:** perfiles como E01/E08, con operador adicional y fricción digital. E01 puede aportar cierre largo, aunque su crédito empresarial merece análisis separado.
- **Comparación de alternativas:** E02/E06/E15 sirven para comprender control por operador, soporte y límites, sin asumir que un micro-POS reemplazará sistemas más complejos.
- **Florería:** conservar E14 como línea adyacente de perecederos; no usarla para validar mercado de abarrotes.
- **Baja actividad y método suficiente:** E09/E12 y casos satisfechos aportan criterios de exclusión del primer piloto, por ausencia de necesidad abordable demostrada, no por edad ni por usar papel. E13 permite aprender de una práctica manual organizada.

### Tres problemas prioritarios para el siguiente ciclo

1. **Omisiones y abandono al capturar durante atención — C1, 10/12.** Riesgo directo para el diseño móvil; mecanismo concreto en E10, aún no generalizable.
2. **Rotación y fechas con información insuficiente — C2, 10/12.** Probar una tarea específica en abarrotes, cuantificando consecuencias. No agrupar indiscriminadamente precios, documentos, stock y caducidad en un MVP.
3. **Operación desigual entre integrantes de la tienda — C4, 10/12.** Validar con todo el equipo que atiende; el uso de un único entusiasta no asegura datos completos.

C3 también obtiene 10/12 y funciona como criterio transversal de elección de herramienta. C7 obtiene 10/12 por frecuencia de políticas y centralidad de la hipótesis, pero requiere investigar el mecanismo antes de construir fiado; no demuestra pérdidas mensuales. Los desempates priorizan riesgo del diseño y tareas comprobables, no tamaño de mercado.

### Qué cambia frente al análisis de dos entrevistas

El problema de precios queda como hallazgo puntual de E16; fechas gana apoyo con E10 y un caso adyacente E14. Se añade evidencia conductual fuerte de abandono móvil E10, dificultades familiares E01/E08 y búsqueda de soluciones a medida E02/E14. El fiado pasa de no tener relatos de pérdida a tres relatos históricos, sin alcanzar su métrica mensual. La satisfacción con alternativas y el hábito manual siguen siendo contraejemplos importantes. La numeración antigua se conserva únicamente en el archivo histórico.

## 4. Insumo para el problem statement

Algunas tiendas de abarrotes con varios productos o atención compartida tienen dificultades para mantener registros y controlar rotación y fechas sin interrumpir el servicio: la afluencia, la captura lenta y las habilidades desiguales de quienes atienden pueden dejar información incompleta o provocar abandono de herramientas. Qhatu necesita comprobar en ese segmento qué tarea produce una mejora medible, manteniendo rapidez y uso por todos los operadores, antes de generalizar urgencia o disposición a pagar.
'''
(R/'04_tensiones_y_recomendaciones.md').write_text(p,encoding='utf-8')
with (R/'02_codificacion_axial.md').open('a',encoding='utf-8') as f: f.write('\n## Contraste preliminar con hipótesis\n\n'+table+'\n\nRelación axial: HU/S10/S15 con A3; HP/HUrg/S1/S4 con A1–A2; S2/S11 con A6; S3/S5/S9/S12 con A4; S6/S7/S14 con A3/A7; S8 con A5; S13 sin respaldo específico.\n')
# Completar definiciones operativas con el alcance literal, evitando definiciones genéricas.
p=R/'01_codificacion_abierta.md'; s=p.read_text(encoding='utf-8')
for c in sorted({r['codigo'] for r in rows}):
 rr=[r for r in rows if r['codigo']==c]
 s=s.replace('| '+c+' | Etiqueta descriptiva del fragmento; alcance literal, sin atribuir causa o frecuencia adicional |','| '+c+' | Se aplica al relato de '+c+'; ejemplo delimitador: “'+rr[0]['cita']+'” |')
p.write_text(s,encoding='utf-8')
# Consolidado tras la cadena, no ejecución rápida para n=16.
a=(R/'01_codificacion_abierta.md').read_text(encoding='utf-8').split('## Libro de códigos',1)[1].split('## Observaciones de calidad',1)[0]
body='# Análisis completo de Qhatu con 16 entrevistas\n\n25 de noviembre de 2026. Resultado consolidado de la cadena 01–04, con las secciones del prompt 00. Se usa la cadena por el tamaño del corpus; el consolidado no es un segundo análisis independiente. Las antiguas E01/E02 ahora son E15/E16. Una florería se identifica como segmento adyacente.\n\n## Libro de códigos resumido\n'+a
for name in ['02_codificacion_axial.md','03_affinity_map.md','04_tensiones_y_recomendaciones.md']:
 body+='\n'+(R/name).read_text(encoding='utf-8').replace('# ','## ',1)
(R/'00_analisis_completo.md').write_text(body,encoding='utf-8')
print('Recomendaciones y consolidado guardados')
