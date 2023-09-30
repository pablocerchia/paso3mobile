import streamlit as st 

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

c4, c5, c6 = st.columns([0.2, 0.6, 0.2])

with c5:

    iframe_url = "https://www.padron.gob.ar/"
    st.components.v1.iframe(iframe_url, width=1000, height=1200)
