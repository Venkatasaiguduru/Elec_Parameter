import streamlit as st

# st.sidebar.title("HACKATHON")

st.title("2305A21L54-PS1")

def Elec_Para(V,R,T):
    I = V/R
    P = I**2*R
    H = I**2*R*T
    return I,P,H

st.write("This application is useful for calculating current through a load,power drawn by the load,and heat energy generated")

col1,col2 = st.columns(2)
with col1:
    with st.container(border=True):
        V = st.number_input("Input voltage:V",min_value=0)
        R = st.number_input("Load resistance:R",min_value=0)
        T = st.number_input("Time in hours:T",min_value=0)

    compute = st.button("Compute")

with col2:
    with st.container(border=True):
        if compute:
            I,P,H = Elec_Para(V,R,T)
            st.write(f'load current = {I} A')
            st.write(f'Load power = {P} W')
            st.write(f'Heat Energy = {H} Wh')

