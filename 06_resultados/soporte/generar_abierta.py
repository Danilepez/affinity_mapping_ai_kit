from pathlib import Path
import json,collections,re
R=Path('06_resultados'); sources={p.name[:3]:p for p in Path('02_entrevistas').glob('E*.md')}
data='''E01|Un Excel.|usa hoja de cálculo|comportamiento|baja
E01|más o menos se estima en lo que hemos gastado y lo que hemos podido tener de ingreso.|estima resultado de caja|comportamiento|baja
E01|Entre 30 a 45 minutos más o menos.|dedica tiempo al cierre|contexto|baja
E01|damos crédito a empresas, ¿no? Entonces ellos llevan y después nos cancelan en 30 días más o menos.|otorga crédito empresarial|comportamiento|baja
E01|Ah, sí. Ha habido, ha habido.|reporta impago previo|dolor|baja
E01|ya se ha descontinuado, ya no corre con el Windows 10|pierde herramienta anterior|dolor|media
E01|no sabe usar ni un celular, entonces ahí eso nos detiene|frena adopción familiar|dolor|media
E02|cada operador hace su cierre de caja.|controla por operador|comportamiento|baja
E02|Cada producto que sale de la tienda sale con códigos de barra|escanea ventas|comportamiento|baja
E02|en un Excel que lo hemos diseñado nosotros como tienda.|complementa con Excel|workaround|baja
E02|no trabajamos con fiados de ningún tipo|rechaza fiado|comportamiento|baja
E02|he contratado una empresa para que me diseñe un sistema que tenga todo lo que yo requiero.|contrata desarrollo propio|comportamiento|media
E02|me acomodo a lo que TuGerente tiene|adapta operación al software|dolor|media
E02|como que no es su prioridad|percibe soporte insuficiente|frustración|media
E03|manejamos el cuaderno de anotaciones. Y el flujo se registra en las noches|registra al cerrar|comportamiento|baja
E03|No tenemos sistema, no estamos tan grandes|ajusta control al tamaño|creencia|baja
E03|tiempo para registrar, todo eso, que te genera más gasto.|anticipa costo de registro|creencia|media
E03|no vienen y no te pagan, ¿no? Y pierdes el cliente y pierdes el producto.|reporta impago previo|dolor|media
E03|No, no trabajamos con el fiado porque es pérdida.|rechaza fiado|comportamiento|media
E03|tenemos los precios, toda la tienda organizada|organiza para atender|comportamiento|baja
E03|atender rápido a la gente para no perjudicarla|prioriza rapidez de atención|motivación|media
E04|Hago mis cuentas diario, diario.|registra al cerrar|comportamiento|baja
E04|las cosas han bajado, digámosle, la venta.|reporta caída de ventas|dolor|media
E04|como es la tienda pequeña, entonces se puede hacer.|ajusta control al tamaño|creencia|baja
E04|yo soy la dueña|atiende como propietaria|contexto|baja
E04|se presta son botellas, pero se deja cambio|exige garantía|comportamiento|baja
E04|el inventario yo lo hago anual.|cuenta inventario anualmente|comportamiento|baja
E04|es muy problemático sacar por meses, por fechas las facturas.|dificulta ordenar comprobantes|dolor|media
E04|siempre les he presentado lo que tengo: apuntes por día anotados|presenta registro manual|comportamiento|baja
E05|en cuaderno, en cuentas de lo que entra y sale.|registra en cuaderno|comportamiento|baja
E05|primero el cuaderno, luego se pasa a la computadora y listo, y todo tranquilo ya.|duplica registro sin molestia|comportamiento|baja
E05|Ah, aquí fiados no. No existe.|rechaza fiado|comportamiento|baja
E05|en negocios mucho más grandes ya es un poco más complicado.|ajusta control al tamaño|creencia|baja
E05|las aplicaciones o todo lo que hay es como para negocios más grandes|percibe software sobredimensionado|creencia|media
E06|el cierre de caja lo hacemos por día.|registra al cerrar|comportamiento|baja
E06|unos 8.000, 10.000 bolivianos, hemos hecho instalar.|paga instalación de sistema|comportamiento|baja
E06|No, ya nada.|evita mensualidad posterior|contexto|baja
E06|No, fiados no.|rechaza fiado|comportamiento|baja
E06|trabajamos entre tres a cuatro personas|comparte atención|contexto|baja
E06|agarramos el sistema y vemos qué se ha vendido y ya para considerar también cuánto se gana.|consulta ventas del personal|comportamiento|baja
E06|se lentea, no deja meter más productos.|sufre límite de carga|dolor|media
E07|en cuadernos más que todo.|registra en cuaderno|comportamiento|baja
E07|Económicos del país, eso.|prioriza contexto económico|dolor|baja
E07|Cada semana o cada tres días|repone periódicamente|comportamiento|baja
E07|Excel algunas cosas, otros son reabastecimiento, otros es cuadernos y facturas.|combina registros|comportamiento|baja
E07|precios no|descarta precio como barrera|creencia|baja
E07|tener un conteo de cuántos productos, más que todo eso.|señala conteo ambiguo|contexto|baja
E07|personas que, como caseros, que no vuelven|reporta pérdida de clientes|dolor|media
E07|productos que no tenemos.|señala faltantes|contexto|baja
E08|no, ya hace años que lo hacemos. Se anotan las salidas y las entradas.|acepta registro actual|creencia|baja
E08|Pero no a tal detalle|limita detalle de registro|contexto|baja
E08|alguna excepción por horas|restringe fiado|comportamiento|baja
E08|algún rato presto pero con una buena garantía.|exige garantía|comportamiento|baja
E08|Por la señal también a veces que baja y todo eso es difícil.|sufre señal irregular|dolor|media
E08|Estamos queriendo meternos a eso, pero está costando.|dificulta adopción digital|dolor|media
E08|Mi esposa me ayuda.|comparte atención|contexto|baja
E08|te muestran una cantidad y no es la cantidad|desconfía comprobantes QR|dolor|media
E08|esperamos que llegue la cantidad digamos, recién les damos el producto|espera confirmación QR|comportamiento|media
E09|ahora ya es innecesario porque los pedidos que hacemos nosotros son muy mínimos|ajusta control al tamaño|creencia|baja
E09|se puede controlar todo mentalmente.|controla de memoria|comportamiento|baja
E09|yo empiezo a atender a las 9 y me quedo hasta medianoche.|extiende horario de atención|comportamiento|media
E09|hemos tenido que guardar nuestras bebidas para Carnavales.|inmoviliza stock estacional|dolor|media
E09|hemos empezado a graduar la cantidad de bebidas que teníamos.|ajusta compras por experiencia|comportamiento|baja
E09|ahora pago 220.|reduce gasto eléctrico|comportamiento|baja
E09|estamos horneando nosotros.|diversifica producción|workaround|baja
E09|Yo apenas logro pagar mi alquiler|reporta presión económica|dolor|alta
E10|cuento todo lo que me queda y lo voy anotando en este cuaderno.|registra al cerrar|comportamiento|baja
E10|entran tres, cuatro personas, entonces hay una venta que se salta.|omite registro con afluencia|dolor|media
E10|dos, tres personas que son de mucha confianza|restringe fiado|comportamiento|baja
E10|me dicen "he llevado esto" y a mí se me pasa.|recupera registro con cliente|workaround|media
E10|es una aplicación de teléfono. Entonces todavía sigue siendo incómodo y no es tan rápido.|sufre lentitud móvil|dolor|media
E10|mi plan a futuro es habilitar una computadora|prefiere computadora futura|motivación|media
E10|con tal de no empeorar la calidad del servicio, no lo uso el teléfono.|abandona registro móvil|comportamiento|media
E10|era algo de 50 pesos mensuales|reporta precio de alternativa|contexto|baja
E10|fechas de caducidad, igual me avisaba. El inventario igual se iba descontando constantemente.|reconoce funciones útiles|creencia|baja
E10|algún código de barras brilla, entonces tarda en enfocarlo.|sufre enfoque de cámara|dolor|media
E10|Fechas de caducidad es lo que más me lleva.|prioriza control de fechas|dolor|media
E10|en esos 10 días a veces se quedan esos dos.|reporta rotación variable|contexto|media
E11|Yo no llevo ninguna contabilidad de nada|opera sin registro|comportamiento|baja
E11|veo cuando en las estanterías faltan cosas y las vuelvo a pedir.|repone a ojo|comportamiento|baja
E11|es dinero que está en las repisas durmiendo|evita capital inmovilizado|motivación|media
E11|estoy pagando entre 400 y 500 al mes de luz.|reporta gasto eléctrico|dolor|media
E11|He tenido que tirarme como cuatro días con un reloj|ajusta consumo eléctrico|workaround|media
E11|Al principio registraba, y la verdad que era mejor, pero ahora en este momento no estoy registrando ya.|abandona registro previo|comportamiento|baja
E11|una estantería no está produciendo, pues mira, reemplazo con alguna cosa que sí se venda.|busca mejorar surtido|motivación|media
E11|son como a lo mejor un 35%, un 40% la ganancia.|estima margen de comida|contexto|baja
E11|hay muchas cosas que hay que llevar con la cabeza, no se puede.|sobrecarga control mental|dolor|media
E11|checo los precios, a veces suben, entonces hay que aumentarle un poco más|actualiza precios de venta|comportamiento|baja
E11|al final me ha quedado debiendo un montón de plata.|reporta impago previo|dolor|media
E11|fiar prácticamente nada.|restringe fiado|comportamiento|baja
E11|incluso me han amenazado y nunca he cerrado|resiste interrupciones externas|dolor|alta
E12|No, no, no hay venta.|reporta caída de ventas|dolor|alta
E12|estoy a veces solita, no está mi hija, entonces pasan ladrones.|percibe riesgo de robo|dolor|media
E12|un poco más para distraernos.|busca actividad cotidiana|motivación|baja
E12|No, porque no hay mucha platita. Muy poquito vendo, muy poquito.|prescinde registro por volumen|comportamiento|baja
E12|Ellos me ayudan a pagar luz, agüita.|recibe apoyo familiar|contexto|baja
E13|cuánto se ha pagado, cuánto se ha vendido, si se ha llegado al objetivo o no.|controla metas diarias|comportamiento|baja
E13|se saca un porcentaje del 8%. Esa es la ganancia.|estima margen fijo|comportamiento|baja
E13|se abre 07:00 y se cierra 19:00.|mantiene horario extenso|contexto|baja
E13|Es mucho ítem, mucho guara-guara es.|percibe software sobredimensionado|creencia|media
E13|para una persona sola no da.|anticipa costo de registro|creencia|media
E13|si contratara a otra persona, ah, tal vez ya optaría por ese sistema.|condiciona adopción a personal|creencia|baja
E13|verifico, pago y lo lleno en el cuaderno|registra en cuaderno|comportamiento|baja
E13|llego a los objetivos.|acepta registro actual|creencia|baja
E14|se lleva un registro manual de las ventas, del inventario de acá.|registra manualmente inventario|comportamiento|baja
E14|he intentado probar distintos software|prueba alternativas|comportamiento|baja
E14|son muy genéricos.|percibe software genérico|frustración|media
E14|he tratado digamos de contactarme con un desarrollador|busca desarrollo propio|comportamiento|media
E14|ver las mermas, la caducidad, renovar el inventario|busca control de perecederos|necesidad|media
E14|únicamente voy digamos yo atendiéndola.|atiende sin apoyo|contexto|baja
E14|No es incómodo, pero tampoco es digamos lo que necesito|acepta hábito insuficiente|creencia|media
E14|si hay conflictos o bloqueos, eso me limita digamos de aquí el inventario.|sufre interrupción de abastecimiento|dolor|media
E14|Para evitar pérdidas vamos nomás yendo según lo que va presentándose coyunturalmente.|evita comprometer oferta|comportamiento|media
E15|Tenemos nuestro propio sistema instalado en la computadora.|usa sistema de escritorio|comportamiento|baja
E15|todo lo que se vende se pasa por el lector.|escanea ventas|comportamiento|baja
E15|Nos sale 700 bolivianos al mes.|paga mensualidad existente|comportamiento|baja
E15|Nos dan soporte y nos actualizan el sistema si algo falla.|recibe soporte|contexto|baja
E15|Estamos muy a gusto con el sistema.|acepta registro actual|creencia|media
E15|No, aquí no damos fiado. A nadie.|rechaza fiado|comportamiento|media
E15|no me llega la confirmación rápido.|espera confirmación QR|dolor|media
E15|la fila se me tranca un poco por esperar que pase el pago.|retiene fila por pago|dolor|media
E16|La verdad no sé exactamente cuál es el que más se vende.|desconoce mayor rotación|contexto|baja
E16|la soda, el pan y la leche.|identifica productos esenciales|contexto|baja
E16|hay varios productos que se vencen bastante rápido|reporta vencimientos|dolor|media
E16|no llevamos ningún control de las fechas.|omite control de fechas|comportamiento|baja
E16|Anotamos todo en un cuaderno.|registra en cuaderno|comportamiento|baja
E16|La verdad no lo siento como un problema, así nomás funciona.|acepta registro actual|creencia|baja
E16|no siempre me acuerdo de cuánto cuesta cada cosa.|dificulta recordar precios|dolor|media
E16|solo a personas muy conocidas del barrio|restringe fiado|comportamiento|baja
E16|solo yo lo hago, porque mis papás no saben usarlo muy bien.|concentra cobro QR|comportamiento|baja'''
rows=[]; counts=collections.Counter()
for line in data.splitlines():
 e,q,c,t,i=line.split('|'); counts[e]+=1
 assert q in sources[e].read_text(encoding='utf-8-sig'),(e,q)
 rows.append(dict(ref=f'{e}-F{counts[e]:02}',entrevista=e,cita=q,codigo=c,tipo=t,intensidad=i))
(R/'soporte/fragmentos.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
parts=['# Codificación abierta de Qhatu con 16 entrevistas\n\nActualización: 25 de noviembre de 2026. Identificadores según los nombres actuales E01–E16. Antiguas E01/E02 corresponden a E15/E16. Citas literales de las transcripciones aportadas; no cotejadas con audio. Conductas autorreportadas, no observaciones independientes. Intensidad interpretada desde el texto.\n']
for e,p in sorted(sources.items()):
 parts += [f'## {e} '+p.read_text(encoding='utf-8-sig').splitlines()[0].split(' ',2)[2], '\n| Ref | Fragmento (cita textual) | Código | Tipo | Intensidad |\n|---|---|---|---|---|']
 for r in rows:
  if r['entrevista']==e: parts.append('| '+' | '.join([r['ref'],'“'+r['cita']+'”',r['codigo'],r['tipo'],r['intensidad']])+' |')
parts+=['\n## Libro de códigos\n\n| Código | Definición breve | Nº de fragmentos | Entrevistas donde aparece |\n|---|---|---|---|']
for c in sorted({r['codigo'] for r in rows}):
 rr=[r for r in rows if r['codigo']==c]; parts.append(f'| {c} | '+ {'reporta impago previo':'Relata falta de pago pasada, sin acreditar mes ni monto comparable','acepta registro actual':'Declara suficiencia o satisfacción; no prueba exactitud','anticipa costo de registro':'Percibe que registrar consume tiempo o recursos, sin medición','restringe fiado':'Admite crédito solo excepcionalmente o a conocidos','ajusta control al tamaño':'Justifica método actual por escala o bajo movimiento'}.get(c,'Etiqueta descriptiva del fragmento; alcance literal, sin atribuir causa o frecuencia adicional')+f' | {len(rr)} | '+', '.join(sorted({r['entrevista'] for r in rr}))+' |')
parts+=['''\n## Observaciones de calidad

- E01: “Ha habido” responde a impago; carece de fecha y monto. El fallo de Odisea es una explicación del participante, no verificación técnica. Los 30–45 minutos son estimados.
- E02/E06: micromarket y supermercado, no equivalentes a dueño único con celular. E06 aclara pago único frente a la pregunta inicial mensual.
- E03/E04/E05/E08/E13: no interpretar manualidad como dolor. E04 recibe preguntas que sugieren omisiones, optimización y dificultades de crédito.
- E07: el entrevistador descarta inicialmente la preocupación económica y sugiere “¿Precios?”; el participante la rechaza. El conteo como barrera es ambiguo; no prueba abandono del alta inicial.
- E08: sospechas de comprobantes y lentitud QR no prueban fraude consumado ni monto perdido.
- E09: contiene extensa digresión personal ajena al negocio, excluida de códigos. Sus afirmaciones generales sobre sociedad, leyes y economía no se toman como hechos externos. El ahorro eléctrico es autorreportado; no se atribuye a una única intervención.
- E10: la pregunta presupone que nunca digitalizó y el usuario la corrige. La app incluía funciones útiles, pero la dejó por atención, enfoque y percepción del cliente. Bs 50 es precio recordado, sin comprobante de pago.
- E11: referencia a ofertas de Bs 1.000–1.500 aparece junto a TikTok; no se puede atribuir inequívocamente a software POS. Márgenes, caja y electricidad son estimaciones. Los programadores eléctricos son conducta relatada, no recomendación operativa. Se excluye retórica política y personal sin utilidad para el problema.
- E12: entrevista breve con baja actividad y función de distracción; no convertir ausencia de registro en urgencia digital. Se excluyen detalles sensibles de salud y duelo del análisis comercial.
- E13: el 8% es su cálculo declarado, no rentabilidad auditada. No haber probado y haber visto apps son compatibles.
- E14: florería, segmento adyacente. “Caducidad” fue sugerida por el entrevistador; búsqueda previa de software/desarrollador sí es conducta relatada. No transferir sus necesidades a abarrotes automáticamente.
- E15/E16: preservadas de la primera ronda bajo nuevos identificadores; E16 es familiar, no comprador confirmado. Se corrigieron solo título y campo Código.
- No se conocen reclutamiento ni atributos completos de todos los casos. Preguntas sobre fiado, tiempo, uso o pago no se hicieron uniformemente: silencio no equivale a respuesta negativa. No hay saturación ni representatividad demostradas.
''']
(R/'01_codificacion_abierta.md').write_text('\n'.join(parts),encoding='utf-8')
print(len(rows),'fragmentos',len({r['codigo'] for r in rows}),'códigos',dict(counts))

