import streamlit as st
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import numpy as np
import geopandas as gpd
import folium
from folium.features import GeoJsonTooltip
from streamlit_folium import st_folium
import streamlit.components.v1 as components

partido_ganador_x_prov = pd.read_csv("data/partido_ganador_x_prov.csv")
partidos_x_prov = pd.read_csv("data/partidos_x_prov.csv")
ganadores_listas_prov = pd.read_csv("data/ganadores_listas_prov.csv")
presidencial_x_AP = pd.read_csv("data/resultados_por_partido.csv")
votos_candidatos_totales = pd.read_csv("data/votos_candidatos_totales.csv")
listas_x_prov = pd.read_csv("data/resultados_por_lista_CLEAN.csv") 
geojson_file = "data/Regions geometry.1692055458453.geojson"
geojson = gpd.read_file(geojson_file)
tabla_ganadores_x_prov = geojson.merge(partido_ganador_x_prov, on="Name")
ganadores_listas_prov = geojson.merge(ganadores_listas_prov, on="Name")
tabla_votos = tabla_ganadores_x_prov.merge(partidos_x_prov, on=["Name", 'Partido', 'perc'])


st.title('Resultados presidenciales - Elecciones PASO 2023')

tab_titles2 = [
                "Por agrupacion politica",
                "Por candidato",
]

tabs2 = st.tabs(tab_titles2)

with tabs2[0]:


    c1, c2, c3 = st.columns([0.2,0.6,0.2])

    #st.title('Resultados presidenciales por provincia')
    #tabla_ganadores_x_prov2 = pd.DataFrame(tabla_ganadores_x_prov)

    #tabla_ganadores_x_prov['Color'] = tabla_ganadores_x_prov['Partido'].map(color_dict)
    with c2:

            components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/14732854"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=1500)

            presidencial_x_AP_sorted = presidencial_x_AP.sort_values(by='perc', ascending=False)
            fig_presidencial_AP = px.bar(presidencial_x_AP_sorted, x='perc', y='name', color='name', orientation='h', text='perc',
                                                title=f'Resultados presidenciales', hover_data=["votos"])
            fig_presidencial_AP.update_traces(textposition='outside', textfont_color='black')
                        #fig_partidos_prov.update_yaxes(type='category', ticks="outside", ticklen=5, tickcolor='rgb(195,186,178)', linecolor='rgb(203,193,185)')
                        #fig_partidos_prov.update_xaxes(anchor="free", shift= -10, gridcolor="rgb(228,217,208)")
            fig_presidencial_AP.update_layout(showlegend=False, template='simple_white')  
            fig_presidencial_AP.update_traces(hovertemplate='Agrupacion Politica: %{y}<br>Votos: %{customdata[0]}<br>Porcentaje: %{x}', hoverlabel=dict(namelength=0))
            fig_presidencial_AP.update_xaxes(title="Porcentaje")
            fig_presidencial_AP.update_yaxes(title="")
            st.plotly_chart(fig_presidencial_AP, use_container_width=True)


            provincias = st.selectbox("Filtrar resultados por distrito:",
                                                    partidos_x_prov['Name'].unique()
                                                    )
            df_provincial = partidos_x_prov.query('Name == @provincias')
            df_provincial = df_provincial.sort_values(by='perc', ascending=False)
            fig_partidos_prov = px.bar(df_provincial, x='perc', y='Partido', color='Partido', orientation='h', text='perc',
                                    title=f'Resultados presidenciales en {provincias}')
            fig_partidos_prov.update_traces(textposition='outside', textfont_color='black')
            #fig_partidos_prov.update_yaxes(type='category', ticks="outside", ticklen=5, tickcolor='rgb(195,186,178)', linecolor='rgb(203,193,185)')
            #fig_partidos_prov.update_xaxes(anchor="free", shift= -10, gridcolor="rgb(228,217,208)")
            fig_partidos_prov.update_layout(showlegend=False, template='simple_white')  
            fig_partidos_prov.update_traces(hovertemplate='Partido: %{y} <br>Porcentaje: %{x}', hoverlabel=dict(namelength=0))
            st.plotly_chart(fig_partidos_prov, use_container_width=True)

            def convert_df(dataframe):
                            return dataframe.to_csv(index=False).encode('utf-8')
                            
            csv_tabla_partidos_x_prov = convert_df(partidos_x_prov)
            csv_tabla_listas_x_prov = convert_df(listas_x_prov)


            st.write("Resultados de las agrupaciones politicas por distrito")
            st.dataframe(partidos_x_prov, hide_index=True)

            st.download_button(
                            "Descargar tabla como archivo CSV.",
                            csv_tabla_partidos_x_prov,
                            "csv_tabla_partidos_x_prov.csv",
                            "text/csv",
                            key='download-csv1'
                            )

            st.write("Resultados de las listas por distrito")
            st.dataframe(listas_x_prov, hide_index=True)

            st.download_button(
                            "Descargar tabla como archivo CSV",
                            csv_tabla_listas_x_prov,
                            "csv_tabla_listas_x_prov.csv",
                            "text/csv",
                            key='download-csv2'
                            )
    
with tabs2[1]:

    c4, c5, c6 = st.columns([0.2,0.6,0.2])

    with c5:
        components.html("""<div class="flourish-embed flourish-map" data-src="visualisation/14802009"><script src="https://public.flourish.studio/resources/embed.js"></script></div>""", height=1500)

        presidencial_x_lista_sorted = votos_candidatos_totales.sort_values(by='Percentage', ascending=False)
        fig_presidencial_listas = px.bar(presidencial_x_lista_sorted, x='Percentage', y='Candidatos', color='Candidatos', orientation='h', text='Percentage',
                                            title=f'Resultados presidenciales por candidato', hover_data=['Partido', 'Lista', "Votos"])
        fig_presidencial_listas.update_traces(textposition='outside', textfont_color='black')
                    #fig_partidos_prov.update_yaxes(type='category', ticks="outside", ticklen=5, tickcolor='rgb(195,186,178)', linecolor='rgb(203,193,185)')
                    #fig_partidos_prov.update_xaxes(anchor="free", shift= -10, gridcolor="rgb(228,217,208)")
        fig_presidencial_listas.update_layout(showlegend=False, template='simple_white', height=600)  
        fig_presidencial_listas.update_traces(hovertemplate='Agrupacion Politica: %{customdata[0]}<br>Lista: %{customdata[1]}<br>Votos: %{customdata[2]}', hoverlabel=dict(namelength=0))
        fig_presidencial_listas.update_xaxes(title="Porcentaje")
        fig_presidencial_listas.update_yaxes(title="")
        st.plotly_chart(fig_presidencial_listas, height=600, use_container_width=True)

 