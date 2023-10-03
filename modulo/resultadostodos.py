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
