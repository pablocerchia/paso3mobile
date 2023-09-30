
        
import streamlit as st
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import numpy as np
import datetime
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode, ColumnsAutoSizeMode, ExcelExportMode
import streamlit_antd_components as sac

df = pd.read_csv('data/PRECANDIDATOS.csv')
encabezan = pd.read_csv('data/encabeza_precandidatos.csv')


####################### LIMPIEZA Y ORDEN DEL DATAFRAME ####################### 

df2023 = df.copy()

####################### CONFIGURACION DE LA PÁGINA PRINCIPAL ####################### 

st.set_page_config(page_title = 'Elecciones 2023 - Sitio de consulta',
                    layout='wide', initial_sidebar_state='collapsed')
st.markdown(
        """
       <style>
       [data-testid="stSidebar"][aria-expanded="true"]{
           min-width: 200px;
           max-width: 200px;
       }
       """,
        unsafe_allow_html=True,
    )
st.markdown(
    """
    <style>
    [data-testid="collapsedControl"] svg {
        height: 3rem;
        width: 3rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown("""<style>.css-zt5igj svg{display:none}</style>""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>Precandidatos de las elecciones PASO 2023<br><br></h1>", unsafe_allow_html=True)


tab_titles = [
                "Búsqueda de candidato",
                "Edad y género de los candidatos",
]
#tabs = st.tabs(tab_titles)



#tabs = st.tabs(tab_titles)
#with tabs[0]:

madre4, madre5, madre6 = st.columns([0.1,0.8,0.1])



with madre5:

    st.subheader("Informate sobre los precandidatos de cada agrupación", anchor=False)
    st.write("A continuación podrás buscar a los precandidatos de cada espacio político de acuerdo al filtro que selecciones.", help="La tabla también es interactiva. Haciendo click derecho en una columna se puede seleccionar si filtrarla, moverla, achicarla, etc.")
    c4, c5, c6= st.columns(3)
    ######################################
    ####################### DROPDOWNS DE LA PRIMERA OPCION ####################### 
    st.markdown("""<style>.css-zt5igj svg{display:none}</style>""", unsafe_allow_html=True)
    df2023 = df2023.loc[~((df2023['Cargo'] == 'PRESIDENTE Y VICEPRESIDENTE') & (df2023['Distrito'] == 'CATAMARCA'))]
    df2023.loc[df2023['Cargo'] == 'PRESIDENTE Y VICEPRESIDENTE', 'Distrito'] = 'NACION'
    df_recortado = df2023[['AP', 'Nombre_lista', 'Distrito', 'Cargo', 'Subcategoria Cargo', 'Precandidatura', 'Posicion']]
    df_recortado.rename(columns={"AP": "Agrupación Política", "Nombre_lista": "Lista", "Subcategoria Cargo": "Subcategoría Cargo",
                                "Posicion": "Posición", "Precandidatura": "Precandidato"}, inplace=True)
    with c4: 
        cargo = st.selectbox("Seleccione el cargo:",
                                            df_recortado['Cargo'].unique()
                                            )
        df_cargo = df_recortado.query('Cargo == @cargo')

    with c5: 
        distrito = st.selectbox("Seleccione distrito:",
                                            df_cargo['Distrito'].unique()
                                            )
        df_distrito = df_cargo.query("Distrito == @distrito")

    with c6: 
        agrupacion = st.multiselect("Seleccione la agrupación política:",
                                            df_distrito['Agrupación Política'].unique(), ['UNION POR LA PATRIA', 'JUNTOS POR EL CAMBIO']
                                            )
        all_options = st.checkbox("Seleccionar todas las agrupaciones políticas")

        if all_options:
            agrupacion = df_distrito['Agrupación Política']
        df_agrupacion = df_distrito.query("`Agrupación Política` == @agrupacion")



    gd = GridOptionsBuilder.from_dataframe(df_agrupacion)
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
            if (params.value == 'FRENTE DE IZQUIERDA Y DE TRABAJADORES-UNIDAD') {
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
            if (params.value == 'LIBER.AR') {
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
            if (params.value == 'MOVIMIENTO IZQUIERDA JUVENTUD DIGNIDAD') {
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
            if (params.value == 'POLíTICA OBRERA') {
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
    gd.configure_columns('Agrupación Política', cellStyle=cellstyle_jscode)
    gridOptions = gd.build()
    grid_table = AgGrid(df_agrupacion, 
            gridOptions = gridOptions, 
            enable_enterprise_modules = True,
            fit_columns_on_grid_load = True,
            height=400,
            width='100%',
            allow_unsafe_jscode=True,
            )

    #AgGrid(df_agrupacion, height=400)
    sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='1')
    st.markdown("<h2 style='text-align: center;'><br>Distribución por edad y/o género de los candidatos<br><br></h2>", unsafe_allow_html=True)
    c1, c2, c3,c7= st.columns(4)

    df2023_v2 = df2023
    num_bins=10
    bin_width = (df2023_v2['Edad'].max() - df2023_v2['Edad'].min()) / num_bins
    bin_edges = [df2023_v2['Edad'].min() + i * bin_width for i in range(num_bins + 1)]
    df2023_v2['Age_Bin'] = pd.cut(df2023_v2['Edad'], bins=bin_edges, labels=False)

    df2023_v2.loc[df2023_v2['Precandidatura'] == 'ADRIANA ELIZABETH REINOSO', 'Age_Bin'] = 1
    df2023_v2.loc[df2023_v2['Precandidatura'] == 'REINA XIOMARA IBAÑEZ', 'Age_Bin'] = 1
    df2023_v2.loc[df2023_v2['Precandidatura'] == 'OLGA VANESA PAOLA LEIVA', 'Age_Bin'] = 1
    df2023_v2['Age_Bin'] = df2023_v2['Age_Bin'].astype('int8')
    df2023_v2['Age_Range'] = df2023_v2['Age_Bin'].apply(lambda bin_label: f'{bin_edges[bin_label]:.0f}-{bin_edges[bin_label + 1]:.0f}')

    with c1:
        cargos = st.selectbox("Seleccionar cargo:",
                                                df2023_v2['Cargo'].unique()
                                                )
        df_cargos = df2023_v2.query('Cargo == @cargos')
    with c2:
        agrupaciones = st.selectbox("Seleccionar la agrupación política:",
                                            df_cargos['AP'].unique()
                                            )
        df_agrupaciones = df_cargos.query('AP == @agrupaciones')
    with c3: 
        distritos = st.selectbox("Seleccionar distrito:",
                                            df_agrupaciones['Distrito'].unique()
                                            )
        df_distritos = df_agrupaciones.query("Distrito == @distrito")
    with c7: 
        lista = st.selectbox("Seleccionar lista:",
                                            df_distritos['Nombre_lista'].unique()
                                            )
        df_lista = df_distritos.query("Nombre_lista == @lista")

        colores_genero = {
        'Masculino': '#0f203a',
        'Femenino': '#f39a58'
    }
        colores_genero2 = {
        'Femenino': '#0f203a',
        'Masculino': '#0f203a'
    }

    #age_range_gender_counts = df_agrupaciones.groupby(['Age_Range', 'Genero']).size().unstack().reset_index()
    df_lista['Totales'] = 1
    df_lista['Genero'] = df['Genero'].replace({'M': 'Masculino', 'F': 'Femenino'})
    age_range_gender_counts = df_lista.groupby(['Age_Range', 'Genero'])['Totales'].sum().reset_index()
    age_range_gender_counts2 = df_lista.groupby(['Age_Range'])['Totales'].sum().reset_index()
    gender_counts = df_lista.groupby(['Genero'])['Totales'].sum().reset_index()
    barras, pie = st.columns(2)

    tabs_gen = [
                "Por edad y género",
                "Por edad",
                "Por género"]
    tabs_gen2 = [
                "Por edad y género",
                "Por edad","Por género"]


    fig = px.bar(age_range_gender_counts, x='Age_Range', y='Totales', color=age_range_gender_counts['Genero'], color_discrete_map=colores_genero, text=age_range_gender_counts['Totales'])
    fig.update_traces(textposition='outside', textfont_color='black')
    fig.update_xaxes(type='category', ticks="outside", ticklen=5, tickcolor='rgb(195,186,178)', linecolor='rgb(203,193,185)', title='Grupo etario')
    fig.update_yaxes(anchor="free", shift= -10, gridcolor="rgb(228,217,208)", title='Cantidad')
    fig.update_yaxes(dtick=1)
    fig.update_layout(barmode='group', template='simple_white',            
            title=f"<b>DISTRIBUCIÓN {cargos} DE {agrupaciones} EN {distritos}</b><br><sup>Lista: {lista} - Elecciones PASO 2023</sup>")
        
    fig_edad = px.bar(age_range_gender_counts2, x='Age_Range', y='Totales', text=age_range_gender_counts2['Totales'])
    fig_edad.update_traces(textposition='outside', textfont_color='black', marker=dict(color='#254f8f'))
    fig_edad.update_xaxes(type='category', ticks="outside", ticklen=5, tickcolor='rgb(195,186,178)', linecolor='rgb(203,193,185)', title='Grupo etario')
    fig_edad.update_yaxes(anchor="free", shift= -10, gridcolor="rgb(228,217,208)", title='Cantidad')
    fig_edad.update_layout(barmode='group', template='simple_white',            
            title=f"<b>{cargos} DE {agrupaciones} EN {distritos}</b><br><sup>Lista: {lista} - Elecciones PASO 2023</sup>")
        
    tabs1, tabs2, tabs3 = st.tabs(tabs_gen)

        #boton_productos = st.radio(
            #"Elegir tipo de gráfico",
            #('Por edad y genero', 'Por edad'), horizontal=True,label_visibility='collapsed')

    with tabs1:
            st.plotly_chart(fig, use_container_width=True)
    with tabs2:
            st.plotly_chart(fig_edad, use_container_width=True)
    with tabs3:
        fig3 = px.bar(gender_counts, x='Genero', y='Totales', color=gender_counts['Genero'], color_discrete_map=colores_genero, text=gender_counts['Totales'])
        fig3.update_traces(textposition='outside', textfont_color='black')
        #fig_totales_genero.update_xaxes(type='category', ticks="outside", ticklen=5, tickcolor='rgb(195,186,178)', linecolor='rgb(203,193,185)', title='Grupo etario')
        #fig_totales_genero.update_yaxes(anchor="free", shift= -10, gridcolor="rgb(228,217,208)", title='Cantidad')
        #fig_totales_genero.update_xaxes(tickmode='array',tickvals=[0.5, 1], ticktext=gender_counts2['Genero'])
        fig3.update_layout(barmode='stack', template='simple_white',            
        title=f'GÉNERO {cargos} DE {agrupaciones} EN {distritos}<br><sup>Lista: {lista} - Elecciones PASO 2023</sup>')
        st.plotly_chart(fig3, use_container_width=True)

    totales_candidatos = df2023_v2 
    totales_candidatos['Totales'] = 1
    totales_candidatos['Genero'] = totales_candidatos['Genero'].replace({'M': 'Masculino', 'F': 'Femenino'})
    totales_gen_edad = totales_candidatos.groupby(['Age_Range', 'Genero'])['Totales'].sum().reset_index()
    totales_edad = totales_candidatos.groupby(['Age_Range'])['Totales'].sum().reset_index()
    gender_counts2 = totales_candidatos.groupby(['Genero'])['Totales'].sum().reset_index()
    sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='2')
    st.subheader("Distribución total", help='Cómo se distribuye la suma de todos los precandidatos para todos los cargos en las PASO 2023', anchor=False)



    fig_totales_gen_edad = px.bar(totales_gen_edad, x='Age_Range', y='Totales', color=totales_gen_edad['Genero'], color_discrete_map=colores_genero, text=totales_gen_edad['Totales'])
    fig_totales_gen_edad.update_traces(textposition='outside', textfont_color='black')
    fig_totales_gen_edad.update_xaxes(type='category', ticks="outside", ticklen=5, tickcolor='rgb(195,186,178)', linecolor='rgb(203,193,185)', title='Grupo etario')
    fig_totales_gen_edad.update_yaxes(anchor="free", shift= -10, gridcolor="rgb(228,217,208)", title='Cantidad')
    fig_totales_gen_edad.update_layout(barmode='group', template='simple_white',            
        title=f"<b>DISTRIBUCIÓN TOTAL POR EDAD Y GÉNERO DE LOS PRECANDIDATOS</b><br><sup>Elecciones PASO 2023</sup>")

    fig_totales_edad = px.bar(totales_edad, x='Age_Range', y='Totales', text=totales_edad['Totales'])
    fig_totales_edad.update_traces(textposition='outside', textfont_color='black', marker=dict(color='#254f8f'))
    fig_totales_edad.update_xaxes(type='category', ticks="outside", ticklen=5, tickcolor='rgb(195,186,178)', linecolor='rgb(203,193,185)', title='Grupo etario')
    fig_totales_edad.update_yaxes(anchor="free", shift= -10, gridcolor="rgb(228,217,208)", title='Cantidad')
    fig_totales_edad.update_layout(barmode='group', template='simple_white',            
                title=f"<b>DISTRIBUCIÓN TOTAL POR EDAD DE LOS PRECANDIDATOS</b><br><sup>Elecciones PASO 2023</sup>")
            
    tabs4, tabs5, tabs6 = st.tabs(tabs_gen2)

    with tabs4:
                st.plotly_chart(fig_totales_gen_edad, use_container_width=True)
    with tabs5:
                st.plotly_chart(fig_totales_edad, use_container_width=True)     
    with tabs6: 
        fig_totales_genero = px.bar(gender_counts2, x='Genero', y='Totales', color=gender_counts2['Genero'], color_discrete_map=colores_genero, text=gender_counts2['Totales'])
        fig_totales_genero.update_traces(textposition='outside', textfont_color='black')
        #fig_totales_genero.update_xaxes(type='category', ticks="outside", ticklen=5, tickcolor='rgb(195,186,178)', linecolor='rgb(203,193,185)', title='Grupo etario')
        #fig_totales_genero.update_yaxes(anchor="free", shift= -10, gridcolor="rgb(228,217,208)", title='Cantidad')
        #fig_totales_genero.update_xaxes(tickmode='array',tickvals=[0.5, 1], ticktext=gender_counts2['Genero'])
        fig_totales_genero.update_layout(barmode='stack', template='simple_white',            
        title=f"<b>DISTRIBUCIÓN TOTAL GÉNERO DE LOS PRECANDIDATOS</b><br><sup>Elecciones PASO 2023</sup>")
        st.plotly_chart(fig_totales_genero, use_container_width=True)
    sac.divider(label='', icon=None, align='center', direction='horizontal', dashed=False, bold=True, key='3')
    st.subheader("¿Quién encabeza más las listas en cada agrupación?", anchor=False)
    st.write("Si bien según la Ley de Paridad de Género en Ámbitos de Representación Política (Ley 27.412) es obligatorio ubicar de manera intercalada mujeres y varones desde el/la primer/a candidato/a hasta el/la último/a candidato/a suplente, la disparidad de género sigue siendo posible porque las listas pueden estar predominantemente encabezadas por varones de manera legal. En listas como la de Senadores, donde sólo puede llegar 1 o máximo 2 al cargo de Senador, esto es particularmente relevante.")

    enc1, enc2 = st.columns(2)
    custom_order = ['UNION POR LA PATRIA', 'JUNTOS POR EL CAMBIO', 'LA LIBERTAD AVANZA', 'HACEMOS POR NUESTRO PAIS']
    custom_order2 = ['DIPUTADOS NACIONALES', 'SENADORES NACIONALES']
    encabezan = encabezan.sort_values(by=['Agrupación Política'], key=lambda x: x.map({v: i for i, v in enumerate(custom_order)}))

    with enc1:
        ap_encabeza = st.selectbox('Seleccionar agrupación política:', encabezan['Agrupación Política'].unique())
        encabezan_sliced = encabezan.query('`Agrupación Política`== @ap_encabeza')
        encabezan_sliced = encabezan_sliced.sort_values(by=['Cargo'], key=lambda x: x.map({v: i for i, v in enumerate(custom_order2)}))
    with enc2:
        cargo_sliced = st.selectbox('Seleccionar cargo:', encabezan_sliced['Cargo'].unique())
        encabezan_final = encabezan_sliced.query('Cargo == @cargo_sliced')


    encabezan_final['Contador'] = 1
    encabezan_final_plot = encabezan_final.groupby(['Genero'])['Contador'].sum().reset_index()

    fig_encabezan = px.bar(encabezan_final_plot, x='Genero', y='Contador', color=encabezan_final_plot['Genero'], color_discrete_map=colores_genero, text=encabezan_final_plot['Contador'])
    fig_encabezan.update_traces(textposition='outside', textfont_color='black')
    fig_encabezan.update_xaxes(type='category', ticks="outside", ticklen=5, tickcolor='rgb(195,186,178)', linecolor='rgb(203,193,185)', title='Grupo etario')
    fig_encabezan.update_yaxes(anchor="free", shift= -10, gridcolor="rgb(228,217,208)", title='Cantidad')
    fig_encabezan.update_layout(barmode='stack', template='simple_white',            
            title=f"<b>DISTRIBUCIÓN DE GÉNERO PARA {ap_encabeza} EN LAS LISTAS DE {cargo_sliced} </b><br><sup>Según qué género las encabeza - Elecciones PASO 2023</sup>")
    st.plotly_chart(fig_encabezan, use_container_width=True)