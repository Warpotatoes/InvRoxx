import streamlit as st
image_path='images/'

import os

os.system("./webdriver/chromedriver")

######################
# Pages
######################
pg = st.navigation([
    st.Page("invroxx_page.py", title="InvRoxx", icon=":material/cruelty_free:"),
    st.Page("calcroxx_page.py", title="CalcRoxx", icon=":material/swords:"),
])
pg.run()
