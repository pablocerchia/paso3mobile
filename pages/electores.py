import streamlit as st
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import numpy as np
import geopandas as gpd
import folium
from folium.features import GeoJsonTooltip
from streamlit_folium import st_folium

st.title('Electores por provincia')
st.write("Aqui se podra encontrar informacion sobre los electores y como estan distribuidos por genero por provincia.")
st.write("A su vez se puede consultar cuantas mesas, secciones electorales y circuitos electorales hay por provincia.")

# Load CSV file into GeoDataFrame
tabla_csv = pd.read_csv("data/tabla_electores.csv")
geojson_file = "data/Regions geometry.1692055458453.geojson"
geojson = gpd.read_file(geojson_file)
tabla_electores = geojson.merge(tabla_csv, on="Name")
electores_anio = pd.read_csv("data/electores_anio.csv")
electores_grupo_etario = pd.read_csv("data/electores_grupo_etario.csv")

c1, c2 = st.columns(2)

with c1:
    mapa_electores = folium.Map(location=[-35.913226, -65.175537], zoom_start=4.5, tiles=None)
    folium.Choropleth(
                geo_data=r'data/Regions geometry.1692055458453.geojson',
                data=tabla_electores,
                columns=['Name', 'Porcentaje'],  #Here we tell folium to get the county fips and plot new_cases_7days metric for each county
                key_on='feature.properties.Name',
                fill_color='YlOrRd',
                nan_fill_color="White", #Use white color if there is no data available for the county
                fill_opacity=0.9,
                line_opacity=0.4,
                legend_name='Porcentaje', #title of the legend
                highlight=True,
                line_color='black').add_to(mapa_electores) 
    folium.features.GeoJson(tabla_electores,
                        name='Name',
                        smooth_factor=2,
                        style_function=lambda x: {'color':'black','fillColor':'transparent','weight':0.5},
                        tooltip=folium.features.GeoJsonTooltip(
                            fields=['Name',
                                    'Porcentaje',
                                    'Electores',
                                    'Femenino',
                                    'Masculino',
                                    'NoBinario',
                                    'Mesas',
                                    'Secciones',
                                    'Circuitos'
                                ],
                            aliases=["Distrito:",
                                    "Porcentaje (%):",
                                    "Electores:",
                                    "Femenino:",
                                    "Masculino:",
                                    "No Binario:",
                                    "Mesas:",
                                    "Secciones:",
                                    "Circuitos:"],
                            localize=True,
                            sticky=False,
                            labels=True,
                            style="""
                                background-color: #F0EFEF;
                                border: 2px solid black;
                                border-radius: 3px;
                                box-shadow: 3px;
                            """,
                            max_width=800,),
                                highlight_function=lambda x: {'weight':3,'fillColor':'grey'},
                            ).add_to(mapa_electores)

    st_folium(mapa_electores,height=1000, width=800)

with c2: 
            melted_df = pd.melt(tabla_csv, id_vars=['Name'], value_vars=['Femenino', 'Masculino', 'NoBinario'],
                    var_name='Genero', value_name='Cant_genero')
            melted_df2 = pd.melt(tabla_csv, id_vars=['Name'], value_vars=['M_Percentage', 'F_Percentage', 'X_Percentage'],
                    var_name='Porc_genero', value_name='Cant_porc_genero')
            #result = pd.merge(melted_df, melted_df2, on=['Name'])

            prov_select_electores = st.selectbox("Filtrar resultados por distrito:",
                                                    melted_df['Name'].unique()
                                                    )
            df_provincial = melted_df.query('Name == @prov_select_electores')
            df_provincial = df_provincial.sort_values(by='Cant_genero', ascending=False)
            df_provincial2 = melted_df2.query('Name == @prov_select_electores')
            df_provincial2 = df_provincial2.sort_values(by='Cant_porc_genero', ascending=False)

            fig_partidos_prov = px.bar(df_provincial, x='Cant_genero', y='Genero', color='Genero', orientation='h', text='Cant_genero',
                                    title=f'Distribucion por genero de electores en {prov_select_electores}')
            fig_partidos_prov.update_traces(textposition='outside', textfont_color='black', texttemplate='%{text:,.2s}')
            #fig_partidos_prov.update_yaxes(type='category', ticks="outside", ticklen=5, tickcolor='rgb(195,186,178)', linecolor='rgb(203,193,185)')
            #fig_partidos_prov.update_xaxes(anchor="free", shift= -10, gridcolor="rgb(228,217,208)")
            fig_partidos_prov.update_layout(showlegend=False, template='simple_white')  
            fig_partidos_prov.update_traces(hovertemplate='Genero: %{y}<br>Electores: %{x}<br>', hoverlabel=dict(namelength=0))
            #st.plotly_chart(fig_partidos_prov, use_container_width=True)

            fig_partidos_prov_porc = px.bar(df_provincial2, x='Cant_porc_genero', y='Porc_genero', color='Porc_genero', orientation='h', text='Cant_porc_genero',
                                    title=f'Distribucion por genero de electores en {prov_select_electores}')
            fig_partidos_prov_porc.update_traces(textposition='outside', textfont_color='black')
            #fig_partidos_prov.update_yaxes(type='category', ticks="outside", ticklen=5, tickcolor='rgb(195,186,178)', linecolor='rgb(203,193,185)')
            #fig_partidos_prov.update_xaxes(anchor="free", shift= -10, gridcolor="rgb(228,217,208)")
            fig_partidos_prov_porc.update_layout(showlegend=False, template='simple_white')  
            fig_partidos_prov_porc.update_traces(hovertemplate='Genero: %{y}<br>Porcentaje: %{x}<br>', hoverlabel=dict(namelength=0))
            #st.plotly_chart(fig_partidos_prov_porc, use_container_width=True)

            boton_productos2 = st.radio(
            "Elegir tipo de distribucion",
            ('Por totales', 'Por porcentaje'), horizontal=True,label_visibility='collapsed')

            if boton_productos2 == 'Por totales':
                st.plotly_chart(fig_partidos_prov, use_container_width=True)
            else:
                st.plotly_chart(fig_partidos_prov_porc, use_container_width=True)

            prov_select_electores2 = st.selectbox("Filtrar resultados por distrito:",
                                                    electores_anio['DISTRITO'].unique()
                                                    )
            df_anios = electores_anio.query('DISTRITO == @prov_select_electores2')
            df_grupo_etario = electores_grupo_etario.query('DISTRITO == @prov_select_electores2')           

            boton_productos3 = st.radio(
            "Elegir tipo de distribuciosadaasn",
            ('Por año', 'Por grupo etario'), horizontal=True,label_visibility='collapsed')

            fig_electores_anio = px.histogram(df_anios, x='CLASE', y='ELECTORES', title='Distribución de los electores por año')
            fig_electores_grupo_etario = px.bar(df_grupo_etario, x='GRUPO', y='ELECTORES', 
                                                      title='Distribución de los electores por grupo etario', text='Percentage')
            fig_electores_grupo_etario.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
            if boton_productos3 == 'Por año':
                st.plotly_chart(fig_electores_anio, use_container_width=True)
            else:
                st.plotly_chart(fig_electores_grupo_etario, use_container_width=True)

tabla_csv.rename(columns={"Num_dist": "ID Distrito", "Name": "Distrito","Porcentaje": "Porcentaje Electores","NoBinario": "No Binario",
                          "M_Percentage": "M_Porcentaje", "F_Percentage": "F_Porcentaje", "X_Percentage": "NB_Porcentaje"}, inplace=True)
tabla_csv2=tabla_csv[['ID Distrito', 'Distrito', 'Electores', 'Porcentaje Electores', 'Mesas', 'Secciones', 'Circuitos', 'Femenino', 'Masculino',
                      'No Binario', 'F_Porcentaje', 'M_Porcentaje', 'NB_Porcentaje']]

st.dataframe(tabla_csv2, hide_index=True, use_container_width=True)
def convert_df(tabla_csv2):
                return tabla_csv2.to_csv(index=False).encode('utf-8')
                
csv2 = convert_df(tabla_csv2)

st.download_button(
                "Descargar tabla como archivo CSV",
                csv2,
                "tabla_electores.csv",
                "text/csv",
                key='download-csv'
                )