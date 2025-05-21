import streamlit as st
import matplotlib.pyplot as plt
import math

st.title("Simulador de Generador Eléctrico Lineal")

# Inputs
N = st.slider("Vueltas por bobina (N)", 100, 2000, 400)
B = st.slider("Campo magnético (T)", 0.1, 1.5, 1.0, 0.1)
r_mm = st.slider("Radio de la bobina (mm)", 5, 50, 12)
t_ms = st.slider("Tiempo de cruce (ms)", 1, 1000, 50)


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

# Parámetro: número de pares de imanes
n_pares = st.slider("Cantidad de pares de imanes/bobinas", 1, 20, 10)

# Crear dibujo
fig, ax = plt.subplots(figsize=(5, 1))
for i in range(n_pares):
    # Dibujar imán
    x_imanes = i * 22
    ax.add_patch(plt.Rectangle((x_imanes, 0.5), 10, 1, color='red'))  # polo N
    # Dibujar bobina
    ax.add_patch(plt.Circle((x_imanes + 8, 0.5), 2.5, color='orange', fill=False, linewidth=1))
    ax.add_patch(plt.Circle((x_imanes + 9, 0.5), 2.5, color='orange', fill=False, linewidth=1))
    ax.add_patch(plt.Circle((x_imanes + 10, 0.5), 2.5, color='orange', fill=False, linewidth=1))
    ax.add_patch(plt.Circle((x_imanes + 11, 0.5), 2.5, color='orange', fill=False, linewidth=1))
    ax.add_patch(plt.Circle((x_imanes + 12, 0.5), 2.5, color='orange', fill=False, linewidth=1))
    
    ax.add_patch(plt.Rectangle((x_imanes + 10, 0.5), 10, 1, color='blue'))  # polo S

ax.set_xlim(0, n_pares * 22)
ax.set_ylim(-3, 3)
ax.axis('off')
st.pyplot(fig)

nv = n_pares * emf_rms

st.markdown(f"**Voltaje RMS multiplicado con n pares de imanes/bobinas** {nv:.2f} V")
