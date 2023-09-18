import streamlit as st 
import pandas as pd
st.image('logo_olimpica.jpg')
st.subheader('Datos de la visita Regional Santa Marta')

negocios = st.selectbox("Negocio", ('STO 1201','STO 1202','STO 1203','STO 1204','STO 1205','STO 1206',
    'STO 1207','STO 1208','STO 1209','SDO 1210','SDO 1211','SAO 1212','STO 1214','STO 1215','STO 1216','STO 1217','STO 1218','STO 1219',
    'STO 1220','STO 1221','STO 1222','STO 1223','STO 1225','STO 1226','STO 1227','STO 1228','STO 1701','STO 1702','STO 1704','SDO 1754' ))
dat = st.date_input('Fecha')

st.markdown('---')
st.header('Aspectos a evaluar')
st.subheader('1. ENTRADA')
ent1= st.selectbox('¿Se encuentra el parqueadero limpio y señalizado? (Incluye parqueadero para discapacitados)',(1,2,3,4,5,'No aplica'))
ent2= st.selectbox('¿Hay horarios publicados? ¿Puertas, ventanas y avisos limpios en la entrada?',(1,2,3,4,5,'No aplica'))
ent3= st.selectbox('¿Vigilantes o ACP saludan al los clientes?',(1,2,3,4,5,'No aplica'))
ent4= st.selectbox('¿Se encuentran carros y canastillas para mercar limpios?',(1,2,3,4,5,'No aplica'))
obs1= st.text_area(height =50,label='Observaciones Entrada')

st.markdown('---')
st.subheader('2. PISO DE VENTAS')
pis1=st.selectbox('¿Hay pisos limpios, pasillos despejados, buena iluminacion y una temperatura agradable?',(1,2,3,4,5,'No aplica'))
pis2=st.selectbox('¿Están los productos señalizados con su respctivo material pop y precio?',(1,2,3,4,5,'No aplica'))
pis3=st.selectbox('¿Existe surtido y señalizacion de acuerdo a la estrategia de precios rojos?',(1,2,3,4,5,'No aplica'))
pis5=st.selectbox('¿Existe un buen saneo y limpieza en frutas y verduras?',(1,2,3,4,5,'No aplica'))
pis6=st.selectbox('¿Existe un completo surtido sin agotados en frutas y verduras?',(1,2,3,4,5,'No aplica'))
pis7=st.selectbox('¿Hay productos porcionados y liquidados en frutas y verduras?',(1,2,3,4,5,'No aplica'))
pis4=st.selectbox('¿Estan los empleados alegres, dispuestos y con buena presentacion personal?',(1,2,3,4,5,'No aplica'))
pis8=st.selectbox('¿La nevera de refrigerados esta limpia, señalizada y bien surtida?',(1,2,3,4,5,'No aplica'))
pis9=st.selectbox('¿Se cumple con el surtido y planometria en la seccion de carnes en general?',(1,2,3,4,5,'No aplica'))
pis10=st.selectbox('¿Esta surtido, señalizado y se está ofreciendo el cajero vendedor?',(1,2,3,4,5,'No aplica'))
pis11=st.selectbox('¿Estan señalizados los eventos tarjeta plata?',(1,2,3,4,5,'No aplica'))
pis12=st.selectbox('¿Existen puestos de pago limpios y se ofrece la bolsa reutilizable?',(1,2,3,4,5,'No aplica'))
pis13=st.selectbox('¿Existe homogenidad en las palomeras, puntas de gondola y exhibiciones?',(1,2,3,4,5,'No aplica'))
obs2 = st.text_area(height =50,label='Observaciones Piso de ventas')

st.markdown('---')
st.subheader('3. INDICADORES')
ind1=st.selectbox('¿Saben los lideres y el director, el presupuesto del dia, presupuesto del mes, cumplimiento y crecimiento?',(1,2,3,4,5,'No aplica'))
ind2=st.selectbox('¿Saben los lideres y el director, en que porcentaje esta la merma? ¿Qué categorias impactan mas?',(1,2,3,4,5,'No aplica'))
ind3=st.selectbox('¿Saben los lideres y el director, cuanto debe ser el consumo diario de energia? ¿Qué plan de accion hay?',(1,2,3,4,5,'No aplica'))
obs3 = st.text_area(height =50,label='Observaciones Indicadores')

st.markdown('---')
st.subheader('4. BAÑOS')
bn1=st.selectbox('¿Existen baños limpios de empleados y clientes, con jabon y papel?',(1,2,3,4,5,'No aplica'))
bn2=st.selectbox('¿Hay novedades de infraestructura pendiente en los baños? Si hay novedad ¿Esta reportada?',(1,2,3,4,5,'No aplica'))
obs4 = st.text_area(height =50,label='Observaciones Baños')

st.markdown('---')
st.subheader('5. TRASTIENDA')
trs1=st.selectbox('¿los  cuartos Rack, Retorno, Subestacion y Planta electrica limpios y ordenados?',(1,2,3,4,5,'No aplica'))
trs2=st.selectbox('¿Existe cuarto de Basura y Carton  limpio y ordenado?',(1,2,3,4,5,'No aplica'))
trs3=st.selectbox('¿El area de recibo y trastienda en general esta limpia, ordenada y libre de material de desuso?',(1,2,3,4,5,'No aplica'))
obs5 = st.text_area(height =50,label='Observaciones Trastienda')

st.markdown('---')
st.subheader('6. BODEGAS')
bg1=st.selectbox('¿Está la bodega limpia y organizada?',(1,2,3,4,5,'No aplica'))
bg2=st.selectbox('¿Está la mercancia sectorizada y con su respectiva señalizacion en la estanteria?',(1,2,3,4,5,'No aplica'))
bg3=st.selectbox('¿La mercancia en bodega se encuentra rotulada con el sticker correspondiente al mes de ingreso?',(1,2,3,4,5,'No aplica'))
bg4=st.selectbox('¿Esta la bodega libre de averias?',(1,2,3,4,5,'No aplica'))
bg5=st.selectbox('¿Está el area de devoluciones señalizada y la mercancia ubicada según el estado de la devolucion?',(1,2,3,4,5,'No aplica'))
obs6 = st.text_area(height =50,label='Observaciones Bodegas')

st.markdown('---')
st.subheader('7. CUARTOS FRIOS')
cf1=st.selectbox('¿Estan los cuartos frios limpios y organizados?',(1,2,3,4,5,'No aplica'))
cf2=st.selectbox('¿La mercancia esta ubicada acorde a la categoria y con señalizacion?',(1,2,3,4,5,'No aplica'))
cf3=st.selectbox('¿La mercancia esta en optimas condiciones para su comercializacion?',(1,2,3,4,5,'No aplica'))
cf4=st.selectbox('¿Las devoluciones estan en su sitio y con su respectivo documento?',(1,2,3,4,5,'No aplica'))
obs7 = st.text_area(height =50,label='Observaciones Cuartos frios')

st.markdown('---')
st.subheader('8. SALAS DE PROCESOS')
sp1=st.selectbox('¿Están las salas de proceso (Carnes, Panaderia y Cafeteria)  limpias y organizadas?',(1,2,3,4,5,'No aplica'))
sp2=st.selectbox('¿Existe rotulacion en las materias primas con su fecha de apertura, lote y fecha de vencimiento?',(1,2,3,4,5,'No aplica'))
sp3=st.selectbox('¿Se encuentran productos vencidos o en mal estado?',(1,2,3,4,5,'No aplica'))
obs8 = st.text_area(height =50,label='Observaciones Salas de procesos')

st.markdown('---')
st.subheader('RESULTADOS')
res = st.button('Generar resultados')
if res: 
	var = [ent1,ent2,ent3,ent4,pis1,pis2,pis3,pis4,pis5,pis6,pis7,pis8,pis9,pis10,pis11,pis12,pis13,ind1,ind2,ind3,bn1,bn2,trs1,trs2,trs3,bg1,bg2,bg3,bg4,bg5,cf1,cf2,cf3,cf4,sp1,sp2,sp3]
	var_num = []
	total = 0
	for i in var:
		if isinstance(i, (int, float)):
			var_num.append(i)
			total += i
	cal = round(((total/(5*len(var_num)))*100),3)
	if cal < 69.99:
		st.error('CALIFICACIÓN DE LA VISITA: CRITICO')
		st.error(cal)
		st.write('SUMA PUNTOS TOTALES:',total)
	elif (cal >= 70 and cal <= 79.99):
		st.warning('CALIFICACIÓN DE LA VISITA: REGULAR')
		st.warning(cal)
		st.write('SUMA PUNTOS TOTALES:',total)
	elif (cal >= 80 and cal <= 89.99):
		st.warning('CALIFICACIÓN DE LA VISITA: ACEPTABLE')
		st.warning(cal)
		st.write('SUMA PUNTOS TOTALES:',total)
	elif (cal >= 90 and cal <= 96.9):
		st.success('CALIFICACIÓN DE LA VISITA: BUENO')
		st.success(cal)
		st.write('SUMA PUNTOS TOTALES:',total)
	elif (cal >= 97 and cal >= 100):
		st.success('CALIFICACIÓN DE LA VISITA: EXCELENTE')
		st.success(cal)
		st.write('SUMA PUNTOS TOTALES:',total)
		

#st.subheader('GENERAR ARCHIVO')
#arch = st.button('Generar archivo')
#if arch:
    # Crear el archivo Excel
 #   df.to_excel("datos.xlsx", index=False)
    # Mostrar un mensaje de éxito
  #  st.success("Archivo Excel generado exitosamente.")












