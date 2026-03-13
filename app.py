import streamlit as st
import random

st.set_page_config(page_title="Generador de Ideas de Negocio", page_icon="💡")

st.title("💡 Generador de Ideas de Negocio")
st.write("Escribe un sector y genera una idea simple para emprender.")

industria = st.text_input("Escribe un sector (ejemplo: comida, tecnología, salud)")

ideas = [
    "Plataforma que conecta pequeños productores con compradores locales",
    "Aplicación que organiza eventos comunitarios",
    "Servicio de suscripción de productos ecológicos",
    "Marketplace para vender productos hechos a mano",
    "App que conecta personas con entrenadores especializados",
    "Servicio digital para ayudar a pequeños negocios a conseguir clientes",
    "Plataforma para vender cursos rápidos por internet",
    "Aplicación que recomienda ideas de negocio según tus habilidades"
]

if st.button("Generar idea"):
    if industria.strip() == "":
        st.warning("Escribe primero un sector.")
    else:
        idea = random.choice(ideas)
        st.subheader("Idea de negocio:")
        st.write(f"Sector elegido: {industria}")
        st.write(idea) 
