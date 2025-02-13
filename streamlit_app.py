import streamlit as st

st.title("☕ Esta es mi nueva aplicación☕")
st.write(
    "un café"
)
st.header("Cabecera")
cantidad=st.slider("Elija un valor:  ")
for i in range(cantidad):
    st.button(f'Botón {i}')

