import streamlit as st
image_path='images/'

######################
# Pages
######################
pg = st.navigation([
    st.Page("accueil.py", title="Accueil", icon=":material/home:"),
    st.Page("page_invo.py", title="Invocations", icon=":material/cruelty_free:"),
    st.Page("page_sorts.py", title="Sorts", icon=":material/sword_rose:"),
    st.Page("page_dopou.py", title="Dopou", icon=":material/directions_alt:"),

])
pg.run()
