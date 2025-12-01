import streamlit as st
#Titulo de la aplicación
st.title("Aplicación de Saludo")

# Solicitar el nombre del usuario
nombre = st.text_input("Ingresa tu nombre:")
# Mostrar el saludo
if nombre:
    st.write(f"¡Hola, {nombre}! Bienvenido a Streamlit.")