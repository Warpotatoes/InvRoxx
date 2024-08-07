import streamlit as st
image_path='images/'

import os

st.write(os.name)

import platform

st.write(platform.system())
st.write(platform.release())

######################
# Pages
######################
pg = st.navigation([
    st.Page("invroxx_page.py", title="InvRoxx", icon=":material/cruelty_free:"),
    st.Page("calcroxx_page.py", title="CalcRoxx", icon=":material/swords:"),
])
pg.run()
