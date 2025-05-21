import streamlit as st
import math

st.title("Simulador de Generador Eléctrico Lineal")

# Inputs
N = st.slider("Vueltas por bobina (N)", 100, 2000, 400)
B = st.slider("Campo magnético (T)", 0.1, 1.5, 1.0, 0.1)
r_mm = st.slider("Radio de la bobina (mm)", 5, 30, 12)
t_ms = st.slider("Tiempo de cruce (ms)", 1, 100, 50)

# Convertir unidades
r = r_mm / 1000
t = t_ms / 1000

# Cálculo
A = math.pi * r**2
phi = B * A
emf_peak = N * (phi / t)
emf_rms = emf_peak / math.sqrt(2)

# Resultados
st.markdown(f"**Área de la bobina:** {A:.6f} m²")
st.markdown(f"**Flujo magnético (Φ):** {phi:.6e} Wb")
st.markdown(f"**Voltaje pico inducido:** {emf_peak:.2f} V")
st.markdown(f"**Voltaje RMS (asumiendo onda senoidal):** {emf_rms:.2f} V")
