import streamlit as st
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import numpy as np
import streamlit.components.v1 as components
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode, ColumnsAutoSizeMode
import streamlit_antd_components as sac
#from modulo.mesa import mesa


def presidentes():

    tabla_delta_listas = pd.read_csv("data/tabla_delta_listas.csv")
    tabla_delta = pd.read_csv("data/tabla_delta.csv")
    partido_ganador_x_prov = pd.read_csv("data/partido_ganador_x_prov.csv")
    partidos_x_prov = pd.read_csv("data/partidos_x_prov.csv")
    ganadores_listas_prov = pd.read_csv("data/ganadores_listas_prov.csv")
    presidencial_x_AP = pd.read_csv("data/resultados_por_partido.csv")
    votos_candidatos_totales = pd.read_csv("data/votos_candidatos_totales.csv")
    listas_x_prov = pd.read_csv("data/resultados_por_lista_CLEAN.csv")
    fuente_votos = pd.read_csv("data/fuente_votos_partidos.csv")

    c1998, c1997, c1996 = st.columns([0.1,0.8,0.1])

    with c1997:
        st.markdown("<h3 style='text-align: center;'>Qué vas a poder encontrar en esta sección<br></h3>", unsafe_allow_html=True)
        st.markdown(
    """
    <div style="text-align:center; font-size: 1.5em;">Consultá y compará cómo le fue a las agrupaciones y a los candidatos en cada provincia y sección electoral del país. Además, podés comparar en detalle los resultados de las principales agrupaciones y candidatos en Buenos Aires, CABA y el Conurbano Bonaerense. También vas a encontrar datos históricos de comparación con <a href='#comparaci-n-con-elecciones-anteriores'>elecciones anteriores</a>, la evolución del <a href='#alza-del-voto-en-blanco'>voto en blanco</a> y <a href='#baja-participaci-n-en-estas-elecciones'>la participación</a> en las elecciones.</div>
    """,
    unsafe_allow_html=True
)
    sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='1667')
    st.markdown("<h5 style='text-align: center;'><br></h5>", unsafe_allow_html=True)
    tabs = sac.buttons(['Por agrupación','Por candidato'], label=None, index=0, format_func=None, align='center', position='top', size='large', direction='horizontal', shape='round', compact=False, return_index=False)
    tabs_sac = sac.buttons(['Por provincia','Por sección'], label=None, index=0, format_func=None, align='center', position='top', size='default', direction='horizontal', shape='round', compact=True, return_index=False, key=888)

    #tabs2 = st.tabs(tabs_sac)
    st.markdown("""<style>.css-zt5igj svg{display:none}</style>""", unsafe_allow_html=True)


    if tabs == 'Por agrupación':

        if tabs_sac == 'Por provincia':


            c1, c2, c3 = st.columns([0.05,0.9,0.05])

            #st.title('Resultados presidenciales por provincia')
            #tabla_ganadores_x_prov2 = pd.DataFrame(tabla_ganadores_x_prov)
            #tabla_ganadores_x_prov['Color'] = tabla_ganadores_x_prov['Partido'].map(color_dict)
            with c2:

                    #components.html("""<div class="flourish-embed flourish-cards" data-src="visualisation/14837408"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=500)
            
                    cmap, charts =st.columns([0.60,0.4])
                    #st.write("Si posas el mouse sobre la provincia podrás ver los resultados en ese distrito. Si clickeas sobre la provincia podrás ver los resultados de las PASO 2019.")
                    with cmap:
                        #components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/14909169" data-height="800px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=800)
                        components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/14732854" data-height="850px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=850)
                    with charts:
                        components.html("""<div style="min-height:447px"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/KOW6L/embed.js?v=2" charset="utf-8"></script><noscript><img src="https://datawrapper.dwcdn.net/KOW6L/full.png" alt="" /></noscript></div>""",height=465)
                        components.html("""<div style="min-height:364px"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/caVxh/embed.js?v=3" charset="utf-8"></script><noscript><img src="https://datawrapper.dwcdn.net/caVxh/full.png" alt="" /></noscript></div>""",height=385)  
                    sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='1')
                    st.markdown("<h3 style='text-align: center;'>RESULTADOS DE LAS PRINCIPALES AGRUPACIONES EN CADA PROVINCIA<br></h3>", unsafe_allow_html=True)
                    #st.subheader('Así fue el rendimiento individual de las principales fuerzas en cada provincia', anchor=False)
                    #st.write("Mirá dónde se hicieron fuertes y dónde tienen terreno por ganar las principales de agrupaciones de cara a las generales.")
                    st.markdown("<h5 style='text-align: center; font-weight: normal;'>Mirá dónde se hicieron fuertes y dónde tienen terreno por ganar de cara a las generales.<br></h5>", unsafe_allow_html=True)
                    mapa1, mapa2, mapa3 = st.columns([0.33, 0.34, 0.33])
                    with mapa1:
                        components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/14999149" data-height="800px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=800)
                    with mapa2: 
                        components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/14999746" data-height="800px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=800)
                    with mapa3:
                        components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/14999491" data-height="800px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=800)
                    sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='4')
                    # col1, col2, col3,col4 = st.columns(4)
                    
                    # with col1:
                    #     st.markdown("<h3 style='text-align: center;'>Mesas escrutadas<br>97,39%<br><br></h3>", unsafe_allow_html=True)
                    #     #st.metric("Mesas escrutadas", "97,39%")
                    # with col2:
                    #     st.markdown("<h3 style='text-align: center;'>Participación<br>69,62%<br><br></h3>", unsafe_allow_html=True)
                    #     #col2.metric("Participación", "69,62%")
                    # with col3:
                    #     st.markdown("<h3 style='text-align: center;'>Votos totales<br>24.016.776<br><br></h3>", unsafe_allow_html=True)
                    #     #col3.metric("Votos totales", "24.016.776")
                    # with col4:
                    #     st.markdown("<h3 style='text-align: center;'>Votos en blanco<br>4,78%<br><br></h3>", unsafe_allow_html=True) 
                    #     #col4.metric("Votos en blanco", "4,78%")  
                    # sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='2')
                    # st.subheader('Resultados presidenciales a nivel nacional', anchor=False)
                    # presidencial_x_AP_sorted = presidencial_x_AP.sort_values(by='perc', ascending=False)
                    # color_partido = {
                    #     'UNION POR LA PATRIA': '#01b5f0',
                    #     'JUNTOS POR EL CAMBIO': '#fcd201',
                    #     'LA LIBERTAD AVANZA': '#695eb0',
                    #     'FRENTE DE IZQUIERDA Y DE TRABAJADORES - UNIDAD': '#cd4137',
                    #     'FRENTE DE IZQUIERDA Y DE TRABAJADORES': '#cd4137',
                    #     'HACEMOS POR NUESTRO PAIS': '#7ec69b',
                    #     'FRENTE LIBER.AR': '#88e99a',
                    #     'MOVIMIENTO AL SOCIALISMO': '#c11f1f',
                    #     'FRENTE PATRIOTA FEDERAL': '#dc61e5',
                    #     'MOVIMIENTO DE ACCION VECINAL': '#3e3c3c',
                    #     'MOVIMIENTO IZQUIERDA JUVENTUD Y DIGNIDAD': '#909f41',
                    #     'MOVIMIENTO LIBRES DEL SUR': '#d69405',
                    #     'POLITICA OBRERA': '#bc5938',
                    #     'PRINCIPIOS Y VALORES': '#82e8dc',
                    #     'PROYECTO JOVEN': '#25ef3c'
                    # }
                    
                    # config = {'displayModeBar': False}
                    # fig_presidencial_AP = px.bar(presidencial_x_AP_sorted, x='perc', y='name', color='name', color_discrete_map=color_partido, orientation='h', text='perc',
                    #                                     title='', hover_data=["votos"])
                    # fig_presidencial_AP.update_traces(textposition='outside', textfont_color='black')
                    #             #fig_partidos_prov.update_yaxes(type='category', ticks="outside", ticklen=5, tickcolor='rgb(195,186,178)', linecolor='rgb(203,193,185)')
                    #             #fig_partidos_prov.update_xaxes(anchor="free", shift= -10, gridcolor="rgb(228,217,208)")
                    # fig_presidencial_AP.update_layout(showlegend=False, template='simple_white')  
                    # fig_presidencial_AP.update_traces(hovertemplate='Agrupacion Politica: %{y}<br>Votos: %{customdata[0]}<br>Porcentaje: %{x}', hoverlabel=dict(namelength=0))
                    # fig_presidencial_AP.update_xaxes(title="Porcentaje", fixedrange=True)
                    # fig_presidencial_AP.update_yaxes(title="", fixedrange=True)
                    # st.plotly_chart(fig_presidencial_AP, use_container_width=True, config=config)
                    # sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='3')
                    # st.subheader('Cómo le fue a los partidos en cada provincia', anchor=False)
                    # provincias = st.selectbox("Filtrar resultados por distrito:",
                    #                                         partidos_x_prov['Name'].unique()
                    #                                         )
                    # df_provincial = partidos_x_prov.query('Name == @provincias')
                    # df_provincial = df_provincial.sort_values(by='perc', ascending=False)
                    # fig_partidos_prov = px.bar(df_provincial, x='perc', y='Partido', color='Partido', color_discrete_map=color_partido, orientation='h', text='perc',
                    #                         title=f'Resultados presidenciales en {provincias}')
                    # fig_partidos_prov.update_traces(textposition='outside', textfont_color='black')
                    # fig_partidos_prov.update_xaxes(title="Porcentaje", fixedrange=True)
                    # #fig_partidos_prov.update_yaxes(title="", fixedrange=True)
                    # #fig_partidos_prov.update_yaxes(type='category', ticks="outside", ticklen=5, tickcolor='rgb(195,186,178)', linecolor='rgb(203,193,185)')
                    # #fig_partidos_prov.update_xaxes(anchor="free", shift= -10, gridcolor="rgb(228,217,208)")
                    # fig_partidos_prov.update_layout(showlegend=False, template='simple_white')  
                    # fig_partidos_prov.update_traces(hovertemplate='Partido: %{y} <br>Porcentaje: %{x}', hoverlabel=dict(namelength=0))
                    # st.plotly_chart(fig_partidos_prov, use_container_width=True, config=config)

                    # st.subheader("Resultados de las agrupaciones políticas por distrito", anchor=False)
                    # partidos_x_prov_aggrid = partidos_x_prov[['Partido', 'Name','perc', 'votos']]
                    # partidos_x_prov_aggrid.rename(columns={"Partido": "Agrupación Política", "Name": "Distrito",
                    #                                        "perc": "Porcentaje","votos": "Votos",}, inplace=True)
                    # gd = GridOptionsBuilder.from_dataframe(partidos_x_prov_aggrid)
                    # #gd.configure_pagination(enabled=True)
                    # #gd.configure_default_column(
                    # #resizable=True,
                    # #filterable=True,
                    # #sortable=True,
                    # #editable=False,)


                    # cellstyle_jscode = JsCode("""
                    #     function(params){
                    #         if (params.value == 'UNION POR LA PATRIA') {
                    #             return {
                    #                 'color': 'black',
                    #                 'backgroundColor' : '#01b5f0'
                    #         }
                    #         }
                    #         if (params.value == 'JUNTOS POR EL CAMBIO') {
                    #             return{
                    #                 'color'  : 'black',
                    #                 'backgroundColor' : '#fcd201'
                    #             }
                    #         }
                    #         if (params.value == 'LA LIBERTAD AVANZA') {
                    #             return{
                    #                 'color'  : 'black',
                    #                 'backgroundColor' : '#695eb0'
                    #             }
                    #         }
                    #         if (params.value == 'FRENTE DE IZQUIERDA Y DE TRABAJADORES - UNIDAD') {
                    #             return{
                    #                 'color'  : 'black',
                    #                 'backgroundColor' : '#cd4137'
                    #             }
                    #         }
                    #         if (params.value == 'FRENTE DE IZQUIERDA Y DE TRABAJADORES') {
                    #             return{
                    #                 'color'  : 'black',
                    #                 'backgroundColor' : '#cd4137'
                    #             }
                    #         }
                    #         if (params.value == 'HACEMOS POR NUESTRO PAIS') {
                    #             return{
                    #                 'color'  : 'black',
                    #                 'backgroundColor' : '#7ec69b'
                    #             }
                    #         }
                    #         if (params.value == 'FRENTE LIBER.AR') {
                    #             return{
                    #                 'color'  : 'black',
                    #                 'backgroundColor' : '#88e99a'
                    #             }
                    #         }
                    #         if (params.value == 'MOVIMIENTO AL SOCIALISMO') {
                    #             return{
                    #                 'color'  : 'black',
                    #                 'backgroundColor' : '#c11f1f'
                    #             }
                    #         }
                    #         if (params.value == 'FRENTE PATRIOTA FEDERAL') {
                    #             return{
                    #                 'color'  : 'black',
                    #                 'backgroundColor' : '#dc61e5'
                    #             }
                    #         }
                    #         if (params.value == 'MOVIMIENTO DE ACCION VECINAL') {
                    #             return{
                    #                 'color'  : 'black',
                    #                 'backgroundColor' : '#3e3c3c'
                    #             }
                    #         }
                    #         if (params.value == 'MOVIMIENTO IZQUIERDA JUVENTUD Y DIGNIDAD') {
                    #             return{
                    #                 'color'  : 'black',
                    #                 'backgroundColor' : '#909f41'
                    #             }
                    #         }
                    #         if (params.value == 'MOVIMIENTO LIBRES DEL SUR') {
                    #             return{
                    #                 'color'  : 'black',
                    #                 'backgroundColor' : '#d69405'
                    #             }
                    #         }
                    #         if (params.value == 'POLITICA OBRERA') {
                    #             return{
                    #                 'color'  : 'black',
                    #                 'backgroundColor' : '#bc5938'
                    #             }
                    #         }
                    #         if (params.value == 'PRINCIPIOS Y VALORES') {
                    #             return{
                    #                 'color'  : 'black',
                    #                 'backgroundColor' : '#82e8dc'
                    #             }
                    #         }
                    #         if (params.value == 'PROYECTO JOVEN') {
                    #             return{
                    #                 'color'  : 'black',
                    #                 'backgroundColor' : '#25ef3c'
                    #             }
                    #         }                                                                         
                    #         else{
                    #             return{
                    #                 'color': 'black',
                    #                 'backgroundColor': 'lightpink'
                    #             }
                    #         }
                    
                    # };
                    # """)
                    # gd.configure_columns('Agrupación Política', cellStyle=cellstyle_jscode)
                    # gridOptions = gd.build()
                    # grid_table = AgGrid(partidos_x_prov_aggrid,
                    #         gridOptions = gridOptions, 
                    #         enable_enterprise_modules = True,
                    #         fit_columns_on_grid_load = True,
                    #         columns_auto_size_mode=ColumnsAutoSizeMode.FIT_CONTENTS,
                    #         height=400,
                    #         width=750,
                    #         allow_unsafe_jscode=True,
                    #         )
                    #st.dataframe(partidos_x_prov, hide_index=True)
        elif tabs_sac == 'Por sección':


            c1, c2, c3 = st.columns([0.05,0.9,0.05])

            #st.title('Resultados presidenciales por provincia')
            #tabla_ganadores_x_prov2 = pd.DataFrame(tabla_ganadores_x_prov)
            #tabla_ganadores_x_prov['Color'] = tabla_ganadores_x_prov['Partido'].map(color_dict)
            with c2:

                    #components.html("""<div class="flourish-embed flourish-cards" data-src="visualisation/14837408"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=500)
            
                    cmap, charts =st.columns([0.6,0.4])
                    #st.write("Si posas el mouse sobre la provincia podrás ver los resultados en ese distrito. Si clickeas sobre la provincia podrás ver los resultados de las PASO 2019.")
                    with cmap:
                        #components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/14909169" data-height="800px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=800)
                        components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/14921103" data-height="850px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=850)
                    with charts:
                        components.html("""<div style="min-height:447px"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/KOW6L/embed.js?v=2" charset="utf-8"></script><noscript><img src="https://datawrapper.dwcdn.net/KOW6L/full.png" alt="" /></noscript></div>""",height=465)
                        components.html("""<div style="min-height:364px"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/caVxh/embed.js?v=3" charset="utf-8"></script><noscript><img src="https://datawrapper.dwcdn.net/caVxh/full.png" alt="" /></noscript></div>""",height=385) 
                    sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='1')
                    st.markdown("<h3 style='text-align: center;'>RESULTADOS DE LAS PRINCIPALES AGRUPACIONES EN CADA SECCIÓN<br></h3>", unsafe_allow_html=True)
                    st.markdown("<h5 style='text-align: center; font-weight: normal;'>Mirá dónde se hicieron fuertes y dónde tienen terreno por ganar de cara a las generales.<br></h5>", unsafe_allow_html=True)
                    #st.subheader('Así fue el rendimiento individual de las principales fuerzas en cada sección electoral', anchor=False)
                    #st.write("Mirá dónde se hicieron fuertes y dónde tienen terreno por ganar las principales de agrupaciones de cara a las elecciones.")
                    mapa1, mapa2, mapa3 = st.columns([0.33, 0.34, 0.33])
                    with mapa1:
                        components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15011745" data-height="800px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=800)
                    with mapa2: 
                        components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15008412" data-height="800px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=800)
                    with mapa3:
                        components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15008476" data-height="800px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=800)
                    sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='4')
                    # col1, col2, col3,col4 = st.columns(4)
                    
                    # with col1:
                    #     st.markdown("<h3 style='text-align: center;'>Mesas escrutadas<br>97,39%<br><br></h3>", unsafe_allow_html=True)
                    #     #st.metric("Mesas escrutadas", "97,39%")
                    # with col2:
                    #     st.markdown("<h3 style='text-align: center;'>Participación<br>69,62%<br><br></h3>", unsafe_allow_html=True)
                    #     #col2.metric("Participación", "69,62%")
                    # with col3:
                    #     st.markdown("<h3 style='text-align: center;'>Votos totales<br>24.016.776<br><br></h3>", unsafe_allow_html=True)
                    #     #col3.metric("Votos totales", "24.016.776")
                    # with col4:
                    #     st.markdown("<h3 style='text-align: center;'>Votos en blanco<br>4,78%<br><br></h3>", unsafe_allow_html=True) 
                    #     #col4.metric("Votos en blanco", "4,78%")  
                    # sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='2')
        c1, c2, c3 = st.columns([0.05,0.9,0.05])
        with c2:
            # st.subheader('¿Dónde ganaron y dónde perdieron las agrupaciones?', anchor=False)
            # st.write("En el siguiente mapa se visualiza cuántos porcentajes de puntos ganó y perdió cada partido en relación a su resultado a nivel nacional. Así se puede ver claramente adónde le fue mejor a cada agrupación y dónde tiene terreno por ganar.")
            # delta1, delta2 = st.columns([0.57, 0.43])
            # def format_with_plus(value):
            #     if value >= 0:
            #         return f'+{value:.2f}'
            #     else:
            #         return f'{value:.2f}'

            # tabla_delta['Juntos por el Cambio'] = tabla_delta['Juntos por el Cambio'].apply(format_with_plus)
            # tabla_delta['Unión por la Patria'] = tabla_delta['Unión por la Patria'].apply(format_with_plus)
            # tabla_delta['La Libertad Avanza'] = tabla_delta['La Libertad Avanza'].apply(format_with_plus)
            # tabla_delta.at[0, 'La Libertad Avanza'] = '30.04'
            # tabla_delta.at[0, 'Juntos por el Cambio'] = '28.27'
            # tabla_delta.at[0, 'Unión por la Patria'] = '27.27'
            # with delta1:
            #     components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/14805050" data-height="900px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=910)            
            # with delta2:
            #     st.dataframe(tabla_delta, hide_index=True, height=915, use_container_width=True)
            # sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='5')
            st.markdown("<h3 style='text-align: center;'>RESULTADOS DE LAS PRINCIPALES AGRUPACIONES EN BUENOS AIRES<br></h3>", unsafe_allow_html=True)
            #st.subheader('Compará cómo les fue en Buenos Aires', anchor=False)
            #st.write("Mirá dónde se hicieron fuertes y dónde tienen terreno por ganar las principales de agrupaciones en la provincia más poblada del país.")
            st.markdown("<h5 style='text-align: center; font-weight: normal;'>Compará cómo les fue en la provincia más poblada del país.<br></h5>", unsafe_allow_html=True)
            mapa111, mapa222, mapa333 = st.columns([0.33, 0.34, 0.33])
            with mapa111:
                components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15011178" data-height="700px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
            with mapa222: 
                components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15011317" data-height="700px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=700)
            with mapa333:
                components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15011199" data-height="700px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=700)
            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='412') 
            #st.subheader('MIRADA EN DETALLE: Compará cómo les fue en el conurbano a nivel circuito electoral', anchor=False)
            st.markdown("<h3 style='text-align: center;'>MIRADA EN DETALLE: CONURBANO BONAERENSE<br></h3>", unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: center; font-weight: normal;'>En los 24 partidos del Conurbano viven más de 10 millones de personas, lo cual representa <br> el 25% de la población del país y el 64% de la población de Buenos Aires.<br></h5>", unsafe_allow_html=True)
            #st.write("En los 24 partidos del Conurbano Bonaerense viven 10.894.664 personas, lo cual representa el 25% de la población del país y el 64% de la población de la provincia de Buenos Aires.")
            mapa777, mapa77789, mapa636 = st.columns([0.2, 0.6, 0.2])
            with mapa77789:
                components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15079086" data-height="800px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=800)
            #sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='4692')
            #st.markdown("<h3 style='text-align: center;'><br><br>MIRÁ CÓMO LE FUE A CADA AGRUPACIÓN<br></h3>", unsafe_allow_html=True)
            #st.subheader("Rendimiento individual de cada agrupación en el conurbano:")
            mapa1116, mapa2226, mapa3336 = st.columns([0.33, 0.34, 0.33])
            
            with mapa1116:
                components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15099425" data-height="800px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=800)
            with mapa2226: 
                components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15099497" data-height="800px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=800)
            with mapa3336:
                components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15099721" data-height="800px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=800)
            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='4126') 
            #st.subheader('Compará cómo les fue en CABA', anchor=False)
            st.markdown("<h3 style='text-align: center;'>RESULTADOS DE LAS PRINCIPALES AGRUPACIONES EN CABA<br></h3>", unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: center; font-weight: normal;'>Mirá dónde se hicieron fuertes y dónde tienen terreno por ganar en la capital del país.<br></h5>", unsafe_allow_html=True)
            #st.write("Mirá dónde se hicieron fuertes y dónde tienen terreno por ganar en la capital del país.")
            mapa1111, mapa2222, mapa3333 = st.columns([0.33, 0.34, 0.33])
            with mapa1111:
                components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15008285" data-height="800px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=800)
            with mapa2222: 
                components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15011674" data-height="800px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=800)
            with mapa3333:
                components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15011648" data-height="800px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=800)
            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='472') 
            #st.subheader('¿De dónde vinieron los votos de cada agrupación?', anchor=False)
            st.markdown("<h3 style='text-align: center;'>¿DE DÓNDE VINIERON LOS VOTOS DE CADA AGRUPACIÓN?<br></h3>", unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: center; font-weight: normal;'>Otro aspecto para analizar es de dónde vienen -porcentualmente hablando- los votos de cada partido.<br> Abajo podrás ver una tabla donde se indica el peso electoral de cada provincia y el resultado de cada fuerza política en la misma. <br></h5>", unsafe_allow_html=True)
            #st.write("Otro aspecto interesante para analizar es de dónde vienen -porcentualmente hablando- los votos de cada partido. Lo esperable sería que haya una distribución parecida de acuerdo a la cantidad de electores en cada distrito. Por eso en la tabla de abajo se incluye cuántos electores viven en cada distrito, como para tener un dato de referencia.")
            st.dataframe(fuente_votos, hide_index=True, height=500, use_container_width=True)

            # sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='6')
            # st.subheader("Niveles históricos de participación electoral", anchor=False)
            # url = "https://cenital.com/paso-una-eleccion-de-cuatro-cuartos/"
            # st.write("Una de las principales preocupaciones post-elecciones fue el hecho de que sólo el 69,62 porciento de los electores registrados fueron efectivamente a votar. Si bien la cifra suscitó cierto pánico, esta nota del politólogo Facundo Cruz viene a traer cierta calma y contexto a la situación. Accedé a la nota mediante este [link](%s)" % url)
            # components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/14842806"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=600)
            # sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='7')
            # st.subheader("Niveles históricos del voto en blanco", anchor=False)
            # st.write("El descontento del pueblo con la situación económica y social actual parece haber sido canalizado principalmente mediante la victoria de Javier Milei en las PASO 2023. Sin embargo, otras vías de canalización institucionalizada del descontento también puede manifestarse a través del voto en blanco o mediante el ausentismo (el cuál llegó a un 30,38%, convirtiéndose así la elección en una batalla de cuatro cuartos y no tres tercios como planteó hace unos meses la vicepresidenta Cristina Kirchner, si se sigue el marco teórico planteado por la nota de arriba).")
            # components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/14843088"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=600)

            # #sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='8')


    #####  SECCION POR CANDIDATO ######

    elif tabs == 'Por candidato':

        if tabs_sac == 'Por provincia':
            c4, c5, c6 = st.columns([0.05,0.9,0.05])

            with c5:
                #components.html("""<div class="flourish-embed flourish-cards" data-src="visualisation/14806041" data-height="500px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=500)
                
                cmap2, charts2 = st.columns([0.6,0.4])
                with cmap2:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/14802009" data-width="100%" data-height="850px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=850)
                with charts2:
                    components.html("""<div style="min-height:428px"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/tNo0l/embed.js?v=7" charset="utf-8"></script><noscript><img src="https://datawrapper.dwcdn.net/tNo0l/full.png" alt="" /></noscript></div>""",height=500)
                    components.html("""<div style="min-height:364px"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/caVxh/embed.js?v=3" charset="utf-8"></script><noscript><img src="https://datawrapper.dwcdn.net/caVxh/full.png" alt="" /></noscript></div>""",height=365)                                  
                sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='422')  
                #st.subheader('Así fue el rendimiento individual de los principales candidatos en cada provincia', anchor=False)
                st.markdown("<h3 style='text-align: center;'>RESULTADOS DE LOS PRINCIPALES CANDIDATOS EN CADA PROVINCIA<br></h3>", unsafe_allow_html=True)
                st.markdown("<h5 style='text-align: center; font-weight: normal;'>Mirá dónde se hicieron fuertes y dónde tienen terreno por ganar de cara a las generales.<br></h5>", unsafe_allow_html=True)
                #st.write("Mirá dónde se hicieron fuertes y dónde tienen terreno por ganar Milei, Massa y Bullrich de cara a las elecciones generales.")
                mapa1, mapa2, mapa3 = st.columns([0.33, 0.34, 0.33])
                with mapa1:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15008664" data-height="800px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=800)
                with mapa2: 
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15008781" data-height="800px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=800)
                with mapa3:
                    components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15008843" data-height="800px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=800)
                sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='412')    
                # presidencial_x_lista_sorted = votos_candidatos_totales.sort_values(by='Percentage', ascending=False)
                # fig_presidencial_listas = px.bar(presidencial_x_lista_sorted, x='Percentage', y='Candidatos', color='Candidatos', color_discrete_map=color_lista, orientation='h', text='Percentage',
                #                                     title=f'Resultados presidenciales por candidato', hover_data=['Partido', 'Lista', "Votos"])
                # fig_presidencial_listas.update_traces(textposition='outside', textfont_color='black')
                #             #fig_partidos_prov.update_yaxes(type='category', ticks="outside", ticklen=5, tickcolor='rgb(195,186,178)', linecolor='rgb(203,193,185)')
                #             #fig_partidos_prov.update_xaxes(anchor="free", shift= -10, gridcolor="rgb(228,217,208)")
                # fig_presidencial_listas.update_layout(showlegend=False, template='simple_white', height=600)  
                # fig_presidencial_listas.update_traces(hovertemplate='Agrupacion Politica: %{customdata[0]}<br>Lista: %{customdata[1]}<br>Votos: %{customdata[2]}', hoverlabel=dict(namelength=0))
                # fig_presidencial_listas.update_xaxes(title="Porcentaje")
                # fig_presidencial_listas.update_yaxes(title="")
                # st.plotly_chart(fig_presidencial_listas, height=600, use_container_width=True)
        elif tabs_sac == 'Por sección':


            c1, c2, c3 = st.columns([0.05,0.9,0.05])

            #st.title('Resultados presidenciales por provincia')
            #tabla_ganadores_x_prov2 = pd.DataFrame(tabla_ganadores_x_prov)
            #tabla_ganadores_x_prov['Color'] = tabla_ganadores_x_prov['Partido'].map(color_dict)
            with c2:

                    #components.html("""<div class="flourish-embed flourish-cards" data-src="visualisation/14837408"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=500)
            
                    cmap, charts =st.columns([0.6,0.4])
                    #st.write("Si posas el mouse sobre la provincia podrás ver los resultados en ese distrito. Si clickeas sobre la provincia podrás ver los resultados de las PASO 2019.")
                    with cmap:
                        #components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/14909169" data-height="800px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=800)
                        components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/14909169" data-height="850px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=850)
                    with charts:
                        components.html("""<div style="min-height:428px"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/tNo0l/embed.js?v=7" charset="utf-8"></script><noscript><img src="https://datawrapper.dwcdn.net/tNo0l/full.png" alt="" /></noscript></div>""",height=500)
                        components.html("""<div style="min-height:364px"><script type="text/javascript" defer src="https://datawrapper.dwcdn.net/caVxh/embed.js?v=3" charset="utf-8"></script><noscript><img src="https://datawrapper.dwcdn.net/caVxh/full.png" alt="" /></noscript></div>""",height=365)                                   
                    sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='1')

                    #st.subheader('Así fue el rendimiento individual de los principales candidatos en todo el país', anchor=False)
                    st.markdown("<h3 style='text-align: center;'>RESULTADOS DE LOS PRINCIPALES CANDIDATOS EN CADA SECCIÓN<br></h3>", unsafe_allow_html=True)
                    st.markdown("<h5 style='text-align: center; font-weight: normal;'>Mirá dónde se hicieron fuertes y dónde tienen terreno por ganar de cara a las generales.<br></h5>", unsafe_allow_html=True)
                    #st.write("Mirá dónde se hicieron fuertes y dónde tienen terreno por ganar Milei, Massa y Bullrich de cara a las elecciones generales.")
                    mapa1, mapa2, mapa3 = st.columns([0.33, 0.34, 0.33])
                    with mapa1:
                        components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15008939" data-height="800px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=800)
                    with mapa2: 
                        components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15009605" data-height="800px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=800)
                    with mapa3:
                        components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15009788" data-height="800px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=800)
                    sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='412')   
                    # col1, col2, col3,col4 = st.columns(4)
                    
                    # with col1:
                    #     st.markdown("<h3 style='text-align: center;'>Mesas escrutadas<br>97,39%<br><br></h3>", unsafe_allow_html=True)
                    #     #st.metric("Mesas escrutadas", "97,39%")
                    # with col2:
                    #     st.markdown("<h3 style='text-align: center;'>Participación<br>69,62%<br><br></h3>", unsafe_allow_html=True)
                    #     #col2.metric("Participación", "69,62%")
                    # with col3:
                    #     st.markdown("<h3 style='text-align: center;'>Votos totales<br>24.016.776<br><br></h3>", unsafe_allow_html=True)
                    #     #col3.metric("Votos totales", "24.016.776")
                    # with col4:
                    #     st.markdown("<h3 style='text-align: center;'>Votos en blanco<br>4,78%<br><br></h3>", unsafe_allow_html=True) 
                    #     #col4.metric("Votos en blanco", "4,78%")  
                    # sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='2')
        # def format_with_plus(value):
        #             if value >= 0:
        #                 return f'+{value:.2f}'
        #             else:
        #                 return f'{value:.2f}'
        # color_lista = {
        #             'MASSA-ROSSI': '#01b5f0',
        #             'GRABOIS-ABAL MEDINA': '#01b5f0',
        #             'BULLRICH-PETRI': '#fcd201',
        #             'RODRIGUEZ LARRETA-MORALES': '#fcd201',
        #             'MILEI-VILLARRUEL': '#695eb0',
        #             'BREGMAN-DEL CAÑO': '#cd4137',
        #             'SOLANO-RIPOLL': '#cd4137',
        #             'SCHIARETTI-RANDAZZO': '#7ec69b',
        #             'VASENA-LAGONEGRO': '#88e99a',
        #             'ETCHEPARE-LORENZO': '#88e99a',
        #             'BARBARO-PUCHETA': '#88e99a',
        #             'CASTAÑEIRA-RUIZ': '#c11f1f',
        #             'BIONDINI-AVENDAÑO': '#dc61e5',
        #             'ALBARRACIN-PASTORE': '#3e3c3c',
        #             'CÚNEO-BARRANCO': '#909f41',
        #             'CASTELLS-REINOSO': '#909f41',
        #             'ESCOBAR-LEZAMA HID': '#d69405',
        #             'RAMAL-URONES': '#bc5938',
        #             'MORENO-FABRE': '#82e8dc',
        #             'AYERBE-RODRIGUEZ': '#25ef3c',
        #             'GIARDINELLI-SOLERNOU': '#25ef3c',
        #             'IBAÑEZ-IBARRA': '#25ef3c'
        #         }
        
        c1, c2, c3 = st.columns([0.1,0.8,0.1])
        with c2:
            # st.subheader('¿Dónde ganó y dónde perdió puntos cada candidato?', anchor=False)
            # st.write("En el siguiente mapa se visualiza cuántos porcentajes de puntos ganó y perdió cada candidato en relación a su resultado a nivel nacional. Así se puede ver claramente adónde le fue mejor a cada candidato y dónde tiene terreno por ganar.")
            # delta11, delta22 = st.columns([0.57, 0.43])

            # with delta11:
            #     components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/14805178" data-height="900px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=910)
            # with delta22:
            #     tabla_delta_listas.rename(columns={'Name': 'Distrito'}, inplace=True)
            #     tabla_delta_listas['Milei'] = tabla_delta_listas['Milei'].apply(format_with_plus)
            #     tabla_delta_listas['Bullrich'] = tabla_delta_listas['Bullrich'].apply(format_with_plus)
            #     tabla_delta_listas['Massa'] = tabla_delta_listas['Massa'].apply(format_with_plus)
            #     tabla_delta_listas['Larreta'] = tabla_delta_listas['Larreta'].apply(format_with_plus)
            #     tabla_delta_listas.at[0, 'Milei'] = '30.04'
            #     tabla_delta_listas.at[0, 'Bullrich'] = '16.98'
            #     tabla_delta_listas.at[0, 'Massa'] = '21.40'
            #     tabla_delta_listas.at[0, 'Larreta'] = '11.30'

            #     st.dataframe(tabla_delta_listas, hide_index=True, height=915, use_container_width=True)
            st.markdown("<h3 style='text-align: center;'>RESULTADOS DE LOS PRINCIPALES CANDIDATOS EN BUENOS AIRES<br></h3>", unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: center; font-weight: normal;'>Compará cómo les fue en la provincia más poblada del país.<br></h5>", unsafe_allow_html=True)
            mapa1112, mapa2227, mapa3337 = st.columns([0.33, 0.34, 0.33])
            with mapa1112:
                components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15011743" data-height="800px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=800)
            with mapa2227: 
                components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15012335" data-height="800px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=800)
            with mapa3337:
                components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15012374" data-height="800px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=800)
            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='492') 
            st.markdown("<h3 style='text-align: center;'>MIRADA EN DETALLE: CONURBANO BONAERENSE<br></h3>", unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: center; font-weight: normal;'>En los 24 partidos del Conurbano viven más de 10 millones de personas, lo cual representa <br> el 25% de la población del país y el 64% de la población de Buenos Aires.<br></h5>", unsafe_allow_html=True)
            mapa7772, mapa777891, mapa6362 = st.columns([0.2, 0.6, 0.2])
            with mapa777891:
                components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15100118" data-height="800px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=800)
            mapa11164, mapa22264, mapa33364 = st.columns([0.33, 0.34, 0.33])
            
            with mapa11164:
                components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15100553" data-height="800px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=800)
            with mapa22264: 
                components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15119684" data-height="800px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=800)
            with mapa33364:
                components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15121109" data-height="800px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=800)
            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='4126') 
            st.markdown("<h3 style='text-align: center;'>RESULTADOS DE LOS PRINCIPALES CANDIDATOS EN CABA<br></h3>", unsafe_allow_html=True)
            st.markdown("<h5 style='text-align: center; font-weight: normal;'>Mirá dónde se hicieron fuertes y dónde tienen terreno por ganar los principales candidatos en la capital del país.<br></h5>", unsafe_allow_html=True)
            mapa1111, mapa2222, mapa3333 = st.columns([0.33, 0.34, 0.33])
            with mapa1111:
                components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15012544" data-height="800px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=800)
            with mapa2222: 
                components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15012554" data-height="800px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=800)
            with mapa3333:
                components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15012574" data-height="800px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=800)
            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='472') 
            st.markdown("<h3 style='text-align: center;'>CONSULTÁ CÓMO LE FUE A CADA CANDIDATO EN CADA DISTRITO Y EN SU INTERNA<br></h3>", unsafe_allow_html=True)
            #st.subheader("Consultá cómo le fue a cada candidato en cada distrito y en su interna", anchor=False)
            listas_x_prov_aggrid = listas_x_prov[['Partido', 'Lista', 'Candidatos', 'Name', 'percAbs', 'perc_interna', 'Votos']]
            listas_x_prov_aggrid.rename(columns={'Partido': 'Agrupación Política','Name': 'Distrito',
                                                    'percAbs': '% Total','perc_interna': '% En la interna',}, inplace=True)
            gd2 = GridOptionsBuilder.from_dataframe(listas_x_prov_aggrid)
                #gd.configure_pagination(enabled=True)
                #gd.configure_default_column(
                #resizable=True,
                #filterable=True,
                #sortable=True,
                #editable=False,)


            cellstyle_jscode = JsCode("""
            function(params){
                if (params.value == 'UNION POR LA PATRIA') {
                    return {
                        'color': 'black',
                        'backgroundColor' : '#01b5f0'
                }
                }
                if (params.value == 'JUNTOS POR EL CAMBIO') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#fcd201'
                    }
                }
                if (params.value == 'LA LIBERTAD AVANZA') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#695eb0'
                    }
                }
                if (params.value == 'FRENTE DE IZQUIERDA Y DE TRABAJADORES - UNIDAD') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#cd4137'
                    }
                }
                if (params.value == 'FRENTE DE IZQUIERDA Y DE TRABAJADORES') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#cd4137'
                    }
                }
                if (params.value == 'HACEMOS POR NUESTRO PAIS') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#7ec69b'
                    }
                }
                if (params.value == 'FRENTE LIBER.AR') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#88e99a'
                    }
                }
                if (params.value == 'MOVIMIENTO AL SOCIALISMO') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#c11f1f'
                    }
                }
                if (params.value == 'FRENTE PATRIOTA FEDERAL') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#dc61e5'
                    }
                }
                if (params.value == 'MOVIMIENTO DE ACCION VECINAL') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#3e3c3c'
                    }
                }
                if (params.value == 'MOVIMIENTO IZQUIERDA JUVENTUD Y DIGNIDAD') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#909f41'
                    }
                }
                if (params.value == 'MOVIMIENTO LIBRES DEL SUR') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#d69405'
                    }
                }
                if (params.value == 'POLITICA OBRERA') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#bc5938'
                    }
                }
                if (params.value == 'PRINCIPIOS Y VALORES') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#82e8dc'
                    }
                }
                if (params.value == 'PROYECTO JOVEN') {
                    return{
                        'color'  : 'black',
                        'backgroundColor' : '#25ef3c'
                    }
                }                                                                         
                else{
                    return{
                        'color': 'black',
                        'backgroundColor': 'lightpink'
                    }
                }
            
                };
                    """)
            gd2.configure_columns('Agrupación Política', cellStyle=cellstyle_jscode)
            gridOptions2 = gd2.build()
            grid_table = AgGrid(listas_x_prov_aggrid, 
                        gridOptions = gridOptions2, 
                        enable_enterprise_modules = True,
                        fit_columns_on_grid_load = True,
                        columns_auto_size_mode=ColumnsAutoSizeMode.FIT_CONTENTS,
                        height=400,
                        width='100%',
                        allow_unsafe_jscode=True,
                        )

            #st.dataframe(listas_x_prov, hide_index=True)
    c1, c2, c3 = st.columns([0.05,0.9,0.05])
    with c2:
            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='6452')
            st.markdown("<h3 style='text-align: center;'>COMPARACIÓN CON ELECCIONES ANTERIORES<br></h3>", unsafe_allow_html=True)
            mapa11117, mapa2227, mapa33337 = st.columns([0.33, 0.34, 0.33])
            with mapa11117:
                components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/14879048" data-height="800px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=800)
            with mapa2227:
                components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/14845138" data-height="800px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=800)
            with mapa33337:
                components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/15164582" data-height="800px"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=800)



            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='6')
            #st.subheader("Pocas personas fueron a votar", anchor=False)
            st.markdown("<h3 style='text-align: center;'>BAJA PARTICIPACIÓN EN ESTAS ELECCIONES<br></h3>", unsafe_allow_html=True)
            url = "https://cenital.com/paso-una-eleccion-de-cuatro-cuartos/"

            st.markdown(
                        """<h5 style='text-align: center; font-weight: normal;'>
                        Una de las principales preocupaciones post PASO fue el hecho de que sólo el 69,62% de los electores fueron a votar.<br>
                        A continuación podrás ver cómo evolucionó la participación desde el retorno de la democracia. <br></h5>
                        """,unsafe_allow_html=True,
                    )
            #st.write("Una de las principales preocupaciones post-elecciones fue el hecho de que sólo el 69,62 porciento de los electores registrados fueron efectivamente a votar. Si bien la cifra suscitó cierto pánico, esta nota del politólogo Facundo Cruz viene a traer cierta calma y contexto a la situación. Accedé a la nota mediante este [link](%s)" % url)
            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/14842806"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)
            sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='7')
            #st.subheader("Alza del voto en blanco", anchor=False)
            st.markdown("<h3 style='text-align: center;'>ALZA DEL VOTO EN BLANCO<br></h3>", unsafe_allow_html=True)
            st.markdown(
                        """<h5 style='text-align: center; font-weight: normal;'>
                        El descontento del pueblo con la situación económica y social actual parece haber sido canalizado institucionalmente <br> mediante la victoria de Milei, el voto en blanco (el más alto desde 2007) y el ausentismo (el cuál llegó a un 30,38%) <br></h5>
                        """,unsafe_allow_html=True,
                    )
            #st.write("El descontento del pueblo con la situación económica y social actual parece haber sido canalizado principalmente mediante la victoria de Javier Milei en las PASO 2023. Sin embargo, otras vías de canalización institucionalizada del descontento también puede manifestarse a través del voto en blanco o mediante el ausentismo (el cuál llegó a un 30,38%, convirtiéndose así la elección en una batalla de cuatro cuartos y no tres tercios como planteó hace unos meses la vicepresidenta Cristina Kirchner, si se sigue el marco teórico planteado por la nota de arriba).")
            components.html("""<div class="flourish-embed flourish-chart" data-src="visualisation/14843088"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""",height=700)

    # if tabs_generales == 'Diputados':
    #     diputados()
    # if tabs_generales == 'Senadores':
    #     senadores()
