import numpy as np
import pandas as pd
import streamlit as st

# Page configuration
st.set_page_config(page_title="Bottomhole Pressure Calculator - Gas Lift")
st.title("🛢️ Gas Lift – Bottomhole Pressure Calculator")

st.markdown("Built by Camila Penna Teixeira, this app is part of her learning journey in Petroleum Engineering, focusing on pressure calculations in gas lift operations.")

# Sidebar input
st.sidebar.header("Input Parameters")
calculation_method = st.sidebar.radio("Choose Calculation Method:", ("Hydrostatic (Physics-based)", "Practical Gradient (Field-based)"))

p_top = st.sidebar.number_input("Wellhead Pressure (psi)", min_value=0.0, value=100.0, step=1.0)
depth = st.sidebar.number_input("Well Depth (ft)", min_value=0.0, value=5000.0, step=100.0)

if calculation_method == "Hydrostatic (Physics-based)":
    st.sidebar.markdown("---")
    density_lbft3 = st.sidebar.number_input("Fluid Density (lb/ft³)", min_value=1.0, value=52.0, step=1.0)
    g = 32.174  # ft/s²
    p_bottom = p_top + (density_lbft3 * g * depth) / 144
    st.subheader("📌 Result (Hydrostatic Method):")
    st.write(f"**Bottomhole Pressure:** {p_bottom:.2f} psi")

    # Generate chart
    depths = np.linspace(0, depth, 50)
    pressures = p_top + (density_lbft3 * g * depths) / 144
    df = pd.DataFrame({"Depth (ft)": depths, "Pressure (psi)": pressures})
    st.line_chart(df.set_index("Depth (ft)"))

else:
    st.sidebar.markdown("---")
    grad = st.sidebar.number_input("Pressure Gradient (psi/ft)", min_value=0.01, value=0.15, step=0.01)
    p_bottom = p_top + grad * depth
    st.subheader("📌 Result (Field Gradient Method):")
    st.write(f"**Bottomhole Pressure:** {p_bottom:.2f} psi")

    # Generate chart
    depths = np.linspace(0, depth, 50)
    pressures = p_top + grad * depths
    df = pd.DataFrame({"Depth (ft)": depths, "Pressure (psi)": pressures})
    st.line_chart(df.set_index("Depth (ft)"))

# Formula explanation
with st.expander("🔍 View Calculation Formula"):
    if calculation_method == "Hydrostatic (Physics-based)":
        st.markdown(r"""
        **Hydrostatic (Physics-based) Calculation**

        \[
        P_{bottom} = P_{top} + \frac{\rho \cdot g \cdot h}{144}
        \]

        Where:
        - \(P_{top}\): Wellhead Pressure (psi)  
        - \(\rho\): Fluid Density (lb/ft³)  
        - \(g\): Gravity = 32.174 ft/s²  
        - \(h\): Depth (ft)  
        - \(144\): Conversion from lb/ft² to psi
        """)
    else:
        st.markdown(r"""
        **Practical Gradient (Field-based) Calculation**

        \[
        P_{bottom} = P_{top} + G \cdot h
        \]

        Where:
        - \(P_{top}\): Wellhead Pressure (psi)  
        - \(G\): Pressure Gradient (psi/ft)  
        - \(h\): Depth (ft)
        """)

# Footer
st.markdown("---")
st.markdown("Developed by **Camila Penna Teixeira** · April 2025")

