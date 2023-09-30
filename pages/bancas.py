import streamlit as st
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import numpy as np
import datetime
import streamlit.components.v1 as components

### DIPUTADOS 
lista_DIPUTADOS = pd.read_csv("data/bancas/TABLA_LIMPIA_DIPUTADOS257.csv")
finalizan_mandato_DIPUTADOS = pd.read_csv("data/bancas/terminan_mandato_diputados.csv")
finalizan_mandato_BLOQUE_DIPUTADOS = pd.read_csv("data/bancas/renovacion_x_bloque.csv")
finalizan_mandato_INTERBLOQUE_DIPUTADOS = pd.read_csv('data/bancas/renovacion_interbloque.csv')
lista_DIPUTADOS = lista_DIPUTADOS[['Apellido', 'Nombre', 'Distrito', 'Bloque', 'INTERBLOQUE','IniciaMandato', 'FinalizaMandato']]
finalizan_mandato_DIPUTADOS = finalizan_mandato_DIPUTADOS[['Apellido', 'Nombre', 'Distrito', 'Bloque', 'INTERBLOQUE','IniciaMandato', 'FinalizaMandato']]

### SENADORES
lista_senadores = pd.read_csv("data/bancas/lista_senadores_CLEAN.csv")
finalizan_mandato = pd.read_csv("data/bancas/terminan_mandato_SENADORES.csv")
finalizan_mandato_bloque = pd.read_csv("data/bancas/terminan_mandato_SENADORES_BLOQUE.csv")
finalizan_mandato = finalizan_mandato[['BLOQUE', 'APELLIDO', 'NOMBRE', 'PROVINCIA']]
finalizan_mandato_bloque = finalizan_mandato_bloque[['Bloque', 'Cantidad']]
lista_senadores = lista_senadores[['BLOQUE', 'APELLIDO', 'NOMBRE', 'PROVINCIA','Inicia_Mandato', 'Finaliza_Mandato']]
lista_senadores2 = lista_senadores.copy()

st.markdown("<h1 style='text-align: center;'>Composición y proyección de las Cámaras de Diputados y Senadores</h1>", unsafe_allow_html=True)

tab_titles2 = [
                "Diputados",
                "Senadores",
]

tab_titles_dip = [
                "Por interbloque",
                "Por bloque",
]



tabs2 = st.tabs(tab_titles2)


with tabs2[0]:

    c4, c5, c6 = st.columns([0.2, 0.6, 0.2])

    with c5:
        #st.title('Cámara de Senadores')
        st.markdown("<h1 style='text-align: center;'>Cámara de Diputados</h1>", unsafe_allow_html=True)
        # SENADORES
        components.html("""<div class="flourish-embed flourish-parliament" data-src="visualisation/14778887"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=1000)
        
        st.subheader('¿Cómo se compone la Cámara?')
        st.write("La cámara está integrada por 257 diputados nacionales quienes representan directamente al pueblo de la Nación. Tienen mandatos de cuatro años y pueden ser reelegidos. Son elegidos utilizando el sistema de representación proporcional D'Hondt en cada uno de los 24 distritos autónomos que integran la federación (23 provincias y la Ciudad Autónoma de Buenos Aires). Cada dos años la Cámara renueva la mitad de sus miembros. Para dar quórum se necesitan 129 diputados. ", unsafe_allow_html=True)
        
        st.subheader('¿Qué es un bloque y un interbloque?')
        st.write("Un bloque es un conjunto de legisladores constituido de un modo formal generalmente a partir de afinidades políticas y/o partidarias. Mientras que un interbloque es una asociación de un conjunto de diversos bloques a partir de afinidades políticas y/o partidarias. No están definidos en el reglamento, pero refieren a grupos de bloques unidos por afinidades o frentes de coalición.")

        st.subheader('¿Quiénes terminan su mandato en 2023?')
        st.write("Los siguientes diputados son quienes finalizan su mandato. A su vez, se puede observar cuantas bancas renueva cada bloque.")

        st.dataframe(finalizan_mandato_DIPUTADOS, hide_index=True, use_container_width=True)

        tabs_dip = st.tabs(tab_titles_dip)

        with tabs_dip[0]:
            fig_bloques_dip2 = px.bar(finalizan_mandato_INTERBLOQUE_DIPUTADOS, x='cantidad', y='Interbloque', color='Interbloque', orientation='h', text='cantidad',
                                        title=f'Renovación bancas por interbloque')
            fig_bloques_dip2.update_traces(textposition='outside', textfont_color='black')
                #fig_partidos_prov.update_yaxes(type='category', ticks="outside", ticklen=5, tickcolor='rgb(195,186,178)', linecolor='rgb(203,193,185)')
                #fig_partidos_prov.update_xaxes(anchor="free", shift= -10, gridcolor="rgb(228,217,208)")
            fig_bloques_dip2.update_layout(showlegend=False, template='simple_white')  
            fig_bloques_dip2.update_traces(hovertemplate='Interbloque: %{y}<br>Bancas a renovar: %{x}<br>', hoverlabel=dict(namelength=0))
            fig_bloques_dip2.update_yaxes(title="")
            fig_bloques_dip2.update_xaxes(title="")
            st.plotly_chart(fig_bloques_dip2, use_container_width=True)

        with tabs_dip[1]:
             
                fig_bloques_dip = px.bar(finalizan_mandato_BLOQUE_DIPUTADOS, x='cantidad', y='Bloque', color='Bloque', orientation='h', text='cantidad',
                                            title=f'Renovación bancas por bloque')
                fig_bloques_dip.update_traces(textposition='outside', textfont_color='black')
                    #fig_partidos_prov.update_yaxes(type='category', ticks="outside", ticklen=5, tickcolor='rgb(195,186,178)', linecolor='rgb(203,193,185)')
                    #fig_partidos_prov.update_xaxes(anchor="free", shift= -10, gridcolor="rgb(228,217,208)")
                fig_bloques_dip.update_layout(showlegend=False, template='simple_white')  
                fig_bloques_dip.update_traces(hovertemplate='Bloque: %{y}<br>Bancas a renovar: %{x}<br>', hoverlabel=dict(namelength=0))
                fig_bloques_dip.update_yaxes(title="")
                fig_bloques_dip.update_xaxes(title="")
                st.plotly_chart(fig_bloques_dip, use_container_width=True)

        st.subheader('¿Quiénes componen actualmente la Cámara de Diputados?')
        st.write("Esta es una tabla que contiene a todos los diputados actuales. Más abajo podrás filtrar la tabla para ver la distribución por provincia, interbloque, etc.")

        st.dataframe(lista_DIPUTADOS, hide_index=True, use_container_width=True)
        @st.cache_data
        def convert_df(df_presi2):
                    return df_presi2.to_csv(index=False).encode('utf-8')
                
        csv2 = convert_df(lista_DIPUTADOS)

        st.download_button(
                "Descargar tabla como archivo CSV",
                csv2,
                "lista_diputados.csv",
                "text/csv",
                key='download-csv44'
                )       
        
        sb10, sb12= st.columns(2)
        lista_DIPUTADOS = lista_DIPUTADOS.sort_values(by='Distrito')
        with sb10:
            provincia_diputado = st.selectbox('Provincia', lista_DIPUTADOS['Distrito'].unique())
            df11 = lista_DIPUTADOS.query('Distrito == @provincia_diputado')
            df11 = df11.sort_values(by='INTERBLOQUE')
        with sb12:
            interbloque_diputado = st.multiselect('Interbloque', df11['INTERBLOQUE'].unique(), default=df11['INTERBLOQUE'].unique())
            lista_diputados_final = df11.query('INTERBLOQUE == @interbloque_diputado')
        lista_diputados_final = lista_diputados_final[['Apellido', 'Nombre', 'Distrito', 'Bloque', 'INTERBLOQUE','IniciaMandato', 'FinalizaMandato']]
        st.dataframe(lista_diputados_final, hide_index=True, use_container_width=True)

        st.subheader('Proyectá cuántas bancas va a ganar cada partido según la provincia!')
        with st.expander("**Qué es el sistema de representación proporcional D'Hondt**"):
             st.write("<br>Es una fórmula mediante la cual se determinan cuántas bancas se le asignará a cada partido político en cada distrito.", unsafe_allow_html=True)
             st.video('https://www.youtube.com/watch?v=kXbUXugLnlc')

        def formula_dhont(cant_bancas, votos):
            total_votes = sum(votos.values())
            votos_porcentaje = {partido: total_votes * (porcentaje / 100) for partido, porcentaje in votos.items()}
            
            lista = []
            for partido, votos_partido in votos_porcentaje.items():
                for bancas in range(1, cant_bancas + 1):
                    lista.append((votos_partido / bancas, partido))

            lista.sort(reverse=True)
            lista_final = lista[:cant_bancas]

            results = {}

            for l in lista_final:
                partido = l[1]
                results[partido] = results.get(partido, 0) + 1

            return results

        with st.expander("**Calculadora de distribución de bancas según fórmula D'Hondt**"):

            st.write("<br> **Hace tu propia proyección! Editá el nombre de los partidos y los porcentajes que podría sacar cada uno para calcular así cuántas bancas a diputados obtendría cada partido en las elecciones generales** <br>", unsafe_allow_html=True)
        
            states_seats = {"Buenos Aires": 35, "Capital Federal": 12,
                "Catamarca": 2,
                "Chaco": 3,
                "Chubut": 3,
                "Córdoba": 9,
                "Corrientes": 4,
                "Entre Ríos": 4,
                "Formosa": 3,
                "Jujuy": 3,
                "La Pampa": 2,
                "La Rioja": 3,
                "Mendoza": 2,
                "Misiones": 4,
                "Neuquén": 2,
                "Río Negro": 3,
                "Salta": 4,
                "San Juan": 3,
                "Santa Cruz": 2,
                "San Luis": 2,
                "Santiago del Estero": 4,
                "Santa Fe": 10,
                "Tierra del Fuego": 3,
                "Tucumán": 5,
                
            }
            
            selected_state = st.selectbox("Seleccione una provincia", list(states_seats.keys()))
            cant_bancas = states_seats[selected_state]
            
            num_parties = st.number_input("Cantidad de partidos", min_value=1, max_value=10, value=3)
            
            votos = {}
            total_percentage = 0  # Initialize total_percentage
            
            for i in range(1, num_parties + 1):
                partido = st.text_input(f"Partido {i}", f"Partido {chr(64+i)}", help='Podés editar el nombre del partido y el porcentaje')
                porcentaje = st.number_input(f"Porcentaje de votos para {partido}", min_value=0.1, max_value=100.0, value=30.0)
                
                # Update total_percentage
                total_percentage += porcentaje
                
                votos[partido] = porcentaje
            
            if total_percentage > 100:
                st.warning("El total de los porcentajes supera el 100%. Por favor corregir.")
            
            if st.button("Calcular"):
                results = formula_dhont(cant_bancas, votos)
                
                st.write("Distribución de Bancas:")
                for partido, bancas in results.items():
                    if bancas == 1:
                        st.write(f"{partido} obtendría {bancas} banca.")
                    elif bancas == 0:
                        st.write(f"{partido} no obtendría bancas.")
                    else:
                        st.write(f"{partido} obtendría {bancas} bancas.")

        st.subheader('Si querés saber más sobre la Cámara de Diputados...')

        with st.expander('**Qué es el Congreso. Diferencia entre Diputados y Senadores**'):
            st.write("El Congreso de la Nación Argentina es el órgano en el cual se ejerce uno de los tres poderes del Estado, el Poder Legislativo, engranaje de nuestro sistema de gobierno representativo, republicano y federal. Dicho Poder está integrado por dos cámaras: la Cámara de Diputados y la Cámara de Senadores, que tienen su sede en el edificio del Palacio del Congreso Nacional. Se trata de un cuerpo deliberativo. Los integrantes de cada una de las Cámaras son elegidos por el voto popular en sufragio universal, secreto y obligatorio.<br><br> **Integrantes:** de la Cámara de Diputados en la actualidad son 257 y representan a los ciudadanos en cuanto a atender y defender sus intereses, son elegidos utilizando el sistema de representación proporcional D'Hondt. A la Cámara de Diputados se la denomina coloquialmente como “la casa del pueblo” “Cámara Baja”. Mientras que a la Cámara de Senadores se la denomina “Cámara Alta”, y los senadores actualmente 72, representan los intereses de las provincias. Son elegidos 3 senadores por provincia y 3 por la Ciudad Autónoma de Buenos Aires.<br><br> **Requisitos:** Para ser diputado un ciudadano debe haber cumplido la edad de veinticinco años, tener cuatro años de ciudadanía en ejercicio, y ser natural de la provincia que lo elija, o con dos años de residencia inmediata en ella. Para ser Senador debe tener la edad de treinta años, haber sido seis años ciudadano de la Nación, y ser natural de la provincia que lo elija, o con dos años de residencia inmediata en ella.<br><br> **Mandato y Renovación de Cámara:** cuatro son los años de mandato de un diputado y la Cámara se renueva por mitad cada dos años, mientras que la Cámara de Senadores se renueva por tercios cada dos años y los senadores tienen un mandato de 6 años. Presidencias de las Cámaras; en la Cámara de Diputados el Presidente/a es un Diputado/a que a propuesta de los Bloques Parlamentarios es elegido por el voto de la mayoría en Sesión Preparatoria, los usos y costumbres dan la Presidencia de la Cámara al partido oficialista. Mientras que la Cámara de Senadores la preside el/la Vicepresidente/a de la Nación.", unsafe_allow_html=True)
        with st.expander('**Funciones**'):
             st.write("Conforme a lo dispuesto en la Constitución Nacional, son competencias específicas de la Cámara de Diputados:<br><br>- Recibir los proyectos de Ley presentados por iniciativa popular (CN Art.39)<br><br>- Iniciar el proceso de consulta popular para un proyecto de ley (CN Art. 40)<br><br>- Iniciar las leyes sobre contribuciones y reclutamiento de tropas (CN Art. 52)<br><br>- Acusar ante el Senado, en juicio político, al presidente y vicepresidente de la Nación, al jefe de Gabinete de ministros, a ministros del Poder Ejecutivo y a miembros de la Corte Suprema (CN Art. 53)", unsafe_allow_html=True)
        with st.expander('**Qué hace un diputado**'):
             st.write("La función específica de un Diputado es legislar, representando los intereses del pueblo que lo llevó a ocupar una banca en el Congreso de la Nación, velar por sus intereses, y adecuar la legislación vigente o proponer nuevas alternativas. Para cumplir su cometido debe asesorarse, investigar, comparar legislaciones, asistir a las reuniones de comisión y ser partícipe de las Sesiones del pleno. Como así también comprometerse con su voto conforme a sus convicciones.", unsafe_allow_html=True)
        with st.expander('**Bloques e interbloques**'):
            st.write("El reglamento de la Cámara de Diputados en su artículo 55 define: “Los grupos de tres o más diputados podrán organizarse en bloques de acuerdo con sus afinidades políticas. Cuando un partido político existente con anterioridad a la elección de los diputados tenga sólo uno o dos diputados en la Cámara, podrán ellos asimismo actuar como bloque.”<br><br>Los bloques tienen un Presidente, que es un diputado/a que los representa ante el pleno y es nexo con la presidencia de la Cámara, también cuentan con un Vicepresidente y un Secretario todos ellos legisladores, internamente cuentan con un Secretario Parlamentario de bloque, y uno Administrativo estos últimos no legisladores.<br><br>Hace unos años estos Bloques políticos se comenzaron a agrupar en Interbloques, siguiendo el criterio de afinidad política, lo que no está reglamentado al día de la fecha.", unsafe_allow_html=True)
        with st.expander('**Comisiones**'):
             st.write("Las comisiones legislativas son órganos de asesoramiento existentes en ambas Cámaras del Congreso de la Nación. Estan integradas por legísladores, asesores y personal de planta. Su funcion es estudiar los proyectos de ley y producir dictámenes sobre los mismos. Pueden ser permanentes o especiales.", unsafe_allow_html=True)
        with st.expander('**Sesiones**'):
            st.write("Se denomina sesión a la reunión del pleno de los diputados o senadores en recinto. Ambas Cámaras del Congreso inician su Período Parlamentario el 1 de marzo con la Asamblea Legislativa (reunión de Diputados y Senadores) en la que el Presidente de la Nación brinda al pleno el informe de gestión, y finaliza el 30 de noviembre, a este período se lo denomina de Sesiones Ordinarias, dentro del mismo las sesiones pueden ser “de tablas” o “especiales”. Fuera del período descripto, el presidente de la Nación tiene la facultad de convocar a Sesiones Extraordinarias, lo hace por decreto especificando el período de duración de las mismas y el temario a considerar, como así también puede prorrogar el período de sesiones ordinarias aquí las Cámaras continúan su normal funcionamiento.", unsafe_allow_html=True)
with tabs2[1]:

    c1, c2, c3 = st.columns([0.2, 0.6, 0.2])

    with c2:
        #st.title('Cámara de Senadores')
        st.markdown("<h1 style='text-align: center;'>Cámara de Senadores</h1>", unsafe_allow_html=True)
        # SENADORES
        components.html("""<div class="flourish-embed flourish-parliament" data-src="visualisation/14777971"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=700)
        
        st.subheader('¿Cómo se compone la Cámara?')
        st.write("La Cámara de Senadores se compone de 72 integrantes, los cuales tienen un mandato de seis años. tres por cada provincia y tres por la Ciudad Autónoma de Buenos Aires. Todos los distritos tienen igual representación. Corresponden dos bancas al partido mayoritario y una al que le sigue en cantidad de votos obtenidos. Cada dos años se renueva un tercio de la cámara, es decir, se renuevan 24 bancas. Formalmente los senadores están organizados por bloques, los cuales a su vez pueden formar alianzas entre sí (en el gráfico de arriba se visualizan las alianzas pero a continuación se tratará a cada bloque por separado). Para dar quórum se necesitan 37 senadores.")
        
        st.subheader('¿Quiénes terminan su mandato en 2023?')
        st.write("Los siguientes senadores son quienes finalizan su mandato. A su vez, se puede observar cuantas bancas renueva cada bloque.")

        st.dataframe(finalizan_mandato, hide_index=True, use_container_width=True)

        fig_bloques = px.bar(finalizan_mandato_bloque, x='Cantidad', y='Bloque', color='Bloque', orientation='h', text='Cantidad',
                                    title=f'Renovación bancas por bloque')
        fig_bloques.update_traces(textposition='outside', textfont_color='black')
            #fig_partidos_prov.update_yaxes(type='category', ticks="outside", ticklen=5, tickcolor='rgb(195,186,178)', linecolor='rgb(203,193,185)')
            #fig_partidos_prov.update_xaxes(anchor="free", shift= -10, gridcolor="rgb(228,217,208)")
        fig_bloques.update_layout(showlegend=False, template='simple_white')  
        fig_bloques.update_traces(hovertemplate='Bloque: %{y}<br>Bancas a renovar: %{x}<br>', hoverlabel=dict(namelength=0))
        st.plotly_chart(fig_bloques, use_container_width=True)

        st.subheader('¿Quiénes componen actualmente el Senado?')
        st.write("Esta es una tabla que contiene a todos los senadores actuales. Más abajo podrás filtrar la tabla para ver la distribución por provincia, bloque, etc.")

        st.dataframe(lista_senadores2, hide_index=True, use_container_width=True)
        @st.cache_data
        def convert_df(df_presi2):
                    return df_presi2.to_csv(index=False).encode('utf-8')
                
        csv = convert_df(lista_senadores2)

        st.download_button(
                "Descargar tabla como archivo CSV",
                csv,
                "lista_senadores.csv",
                "text/csv",
                key='download-csv4'
                )       
        
        sb, sb2= st.columns(2)
        lista_senadores2 = lista_senadores2.sort_values(by='PROVINCIA')
        with sb:
            provincia_senador = st.selectbox('Provincia', lista_senadores2['PROVINCIA'].unique())
            df1 = lista_senadores2.query('PROVINCIA == @provincia_senador')
            df1 = df1.sort_values(by='BLOQUE')
        with sb2:
            bloque_senador = st.multiselect('Bloque', df1['BLOQUE'].unique(), default=df1['BLOQUE'].unique())
            lista_senadores_final = df1.query('BLOQUE == @bloque_senador')
        st.dataframe(lista_senadores_final, hide_index=True, use_container_width=True)

        st.subheader('Si querés saber más sobre la Cámara de Senadores...')

        with st.expander('**Funciones**'):
             st.write("El Poder Legislativo es ejercido en la República Argentina por el Congreso Nacional, que está compuesto por dos cámaras: la de Diputados y la de Senadores. **Su tarea primordial es deliberar y sancionar leyes. Además de legislar, otra de las funciones esenciales del Congreso es ejercer el control de gobierno.** Esta actividad se lleva a cabo al evaluar el cumplimiento de los planes o programas previamente elaborados, para lo cual el Congreso tiene las facultades de investigar, requerir informes y realizar tareas de campo. La publicidad de sus actos es otra de sus tareas clave ya que, en tanto fuente de información, permite también a la ciudadanía evaluar el cumplimiento del mandato conferido.")
        with st.expander('**Conformación**'):
            st.write("Los senadores y senadoras cumplen un mandato de seis años y pueden ser reelectos indefinidamente. Sin embargo, no se eligen todos en simultáneo: la Cámara se renueva en un tercio cada dos años, en elecciones nacionales. Cabe recordar que la reforma constitucional de 1994 consagró la elección directa de los senadores y senadoras y la designación de un tercer senador o senadora por la minoría en cada distrito. Para el período 1995-2001, ese tercer senador o senadora fue electo por cada legislatura provincial. La reforma constitucional también acortó la duración del mandato de nueve a seis años y estableció la renovación parcial de la Cámara, un tercio de los distritos cada dos años. <br><br> La reforma constitucional dispuso en una cláusula transitoria que la totalidad de los integrantes del Senado serían elegidos de forma directa en el año 2001. Pero como la reforma también disponía la renovación parcial del Cuerpo por tercios cada dos años, fue necesario disponer la división de los distritos en tres grupos y decidir por la suerte qué senadores y senadoras cumplirían mandatos de dos, cuatro y seis años. Los grupos quedaron conformados de la siguiente manera:<br><br>**Grupo I:** Catamarca, Córdoba, Corrientes, Chubut, La Pampa, Mendoza, Santa Fe y Tucumán.<br><br>**Grupo II:** Buenos Aires, Formosa, Jujuy, La Rioja, Misiones, San Juan, San Luis y Santa Cruz.<br><br>**Grupo III:** Ciudad de Buenos Aires, Chaco, Entre Ríos, Neuquén, Río Negro, Salta, Santiago del Estero y Tierra del Fuego.<br><br>Estos grupos siguen vigentes hasta hoy y determinan qué distritos renuevan sus bancas cada dos años.", unsafe_allow_html=True)
        with st.expander('**Autoridades**'):
             st.write("El presidente natural del Senado de la Nación es el vicepresidente o vicepresidenta de la Nación . En el orden parlamentario preside las sesiones pero no participa de los debates ni vota, salvo en caso de empate. Además, es titular de todas las atribuciones administrativas que hacen al funcionamiento del Cuerpo.<br><br>En lo que respecta al resto de sus autoridades, el Senado designa cada año entre sus miembros a un presidente o presidenta provisional, un vicepresidente o vicepresidenta, un vicepresidente o vicepresidenta primero y un vicepresidente o vicepresidenta segundo . Esta mesa de autoridades es asistida por dos secretarios o secretarias y tres prosecretarios o prosecretarias que no son legisladores y cumplen funciones parlamentarias, administrativas y de coordinación. El mandato de los miembros de la mesa de autoridades dura un período, que vence el último día del mes de febrero del año siguiente a su designación.<br><br>Con respecto al presidente provisional del Senado, cabe señalar que deberá reemplazar a quien preside el Cuerpo en caso de su ausencia o vacancia. Además, de acuerdo con la Ley de Acefalía, será llamado a suceder al presidente o presidenta de la República en tercer término ante el supuesto de renuncia, muerte o incapacidad del presidente o presidenta y de su sucesor natural, el vicepresidente o vicepresidenta de la Nación.",unsafe_allow_html=True)
        with st.expander('**Comisiones**'):
             st.write("Los senadores y senadoras debaten en el marco de comisiones permanentes que abordan diferentes áreas temáticas específicas y están facultadas para dictaminar sobre los proyectos sometidos a decisión. Se trata de instancias de investigación, análisis y discusión que permiten una especialización y un mejor conocimiento de los temas que son objeto de tratamiento legislativo.<br><br>Los senadores y senadoras que integran las comisiones recogen información, escuchan a los diferentes actores involucrados, piden asesoramiento y contemplan la opinión pública y los intereses de la comunidad.<br><br>A partir de la labor de las comisiones, se obtiene información técnica precisa y simplificada, que constituye el soporte elemental para todo el proceso de decisión de los legisladores y legisladoras.",unsafe_allow_html=True)
        with st.expander('**Bloques parlamentarios**'):
             st.write('Los bloques parlamentarios reúnen legisladores y legisladoras por afinidades políticas e intereses comunes.<br><br>El objetivo principal de los bloques es mantener un criterio y delinear estrategias políticas coherentes frente a los diversos problemas e iniciativas que se plantean. La complejidad de la tarea legislativa hace que el trabajo deba dividirse para no dispersar esfuerzos, siendo los bloques los encargados de determinar y coordinar esta tarea.<br><br>Los bloques cuentan con un presidente o presidenta, que es elegido entre sus miembros y suele funcionar como nexo con las autoridades del Cuerpo y con las autoridades nacionales. Los presidentes y presidentas de los bloques, junto con el presidente o presidenta del Senado, forman el Plenario de Labor Parlamentaria, que se ocupa de proyectar el orden del día que se seguirá en las sesiones, informarse acerca del estado de los asuntos en las comisiones y promover medidas prácticas para agilizar los debates y mejorar el funcionamiento del Senado, entre otras funciones.', unsafe_allow_html=True)