import streamlit as st
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import numpy as np
import streamlit.components.v1 as components
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode, ColumnsAutoSizeMode
import streamlit_antd_components as sac
from modulo.bancas import diputados, senadores
from modulo.presidentes import presidentes
from modulo.gobernador import gobernadores
from modulo.mesa import mesa

st.set_page_config(page_title='Elecciones 2023 - Página de consulta', layout='wide')
st.write("#")
st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
        </style>
        """, unsafe_allow_html=True)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

def resultados():
    tabs_generales = sac.tabs(['PRESIDENTE','DIPUTADOS','SENADORES', 'GOBERNADOR PBA', 'MESA'], index=0, format_func='upper', height=None, align='center', position='top', shape='default', grow=False, return_index=False)
    if tabs_generales == 'PRESIDENTE':
        presidentes()
    if tabs_generales == 'DIPUTADOS':
        diputados()
    if tabs_generales == 'SENADORES':
        senadores()
    if tabs_generales == 'GOBERNADOR PBA':
        gobernadores()
    if tabs_generales == 'MESA':
        mesa()
