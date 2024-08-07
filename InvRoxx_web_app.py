import streamlit as st
image_path='images/'

import subprocess

subprocess.run(["python", "script.py"])

######################
# Pages
######################
def page2():
    st.write("patate sauvage")
pg = st.navigation([
    st.Page("invroxx_page.py", title="InvRoxx", icon=":material/cruelty_free:"),
    st.Page("calcroxx_page.py", title="CalcRoxx", icon=":material/swords:"),
])
pg.run()
