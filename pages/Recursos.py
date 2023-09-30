import streamlit as st
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import numpy as np
import streamlit.components.v1 as components

st.markdown("""<style>.css-zt5igj svg{display:none}</style>""", unsafe_allow_html=True)
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
st.markdown("<h1 style='text-align: center;'>Recursos</h1>", unsafe_allow_html=True)

st.write("Acá vas a poder encontrar todos las tablas y recursos utilizados para poder hacer los gráficos en esta página para que puedas trabajarlos o seguir investigando y analizando por tu cuenta. Van a estar organizados de acuerdo a cada sección")

with st.expander("Electores"):
    st.write("")