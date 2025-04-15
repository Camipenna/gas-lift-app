import numpy as np
import pandas as pd
import streamlit as st

# Page configuration
st.set_page_config(page_title="Bottomhole Pressure Calculator - Gas Lift")
st.title("🛢️ Gas Lift – Bottomhole Pressure Calculator")

st.markdown("This application was developed by **Camila Penna Teixeira** to demonstrate technical knowledge in Petroleum Engineering, focusing on bottomhole pressure calculations in gas lift systems.")

# Sidebar input
st.sidebar.header("Input Parameters")
p_top = st.sidebar.number_input("Wellhead Pressure (psi)", min_value=0.0, value=100.0, step=1.0)
density = st.sidebar.number_input("Fluid Density (lb/gal)", min_value=0.0, value=9.5, step=0.1)
depth = st.sidebar.number_input("Well Depth (ft)", min_value=0.0, value=5000.0, step=100.0)

# Constant for hydrostatic pressure (psi/ft)
CONVERSION_FACTOR = 0.433

# Bottomhole pressure calculation
p_bottom = p_top + (CONVERSION_FACTOR * density * depth)

# Result
st.subheader("📌 Result:")
st.write(f"**Bottomhole Pressure:** {p_bottom:.2f} psi")

# Optimized chart using Streamlit
st.subheader("📈 Pressure vs. Depth Chart")
depths = np.linspace(0, depth, 50)
pressures = p_top + CONVERSION_FACTOR * density * depths

df = pd.DataFrame({
    'Depth (ft)': depths,
    'Pressure (psi)': pressures
})

st.line_chart(df.set_index('Depth (ft)'))

# Formula explanation
with st.expander("🔍 View Calculation Formula"):
    st.markdown(r"""
    The formula used is:

    \[
    P_{bottom} = P_{top} + 0.433 \times \rho \times h
    \]

    Where:
    - \(P_{top}\): Wellhead Pressure (psi)
    - \(\rho\): Fluid Density (lb/gal)
    - \(h\): Depth (ft)
    - 0.433: Conversion factor for psi/ft
    """)

# Footer
st.markdown("---")
st.markdown("Developed by **Camila Penna Teixeira** · April 2025")

