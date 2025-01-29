import streamlit as st
image_path='images/'



######################
# Page Title
######################

st.set_page_config(page_title="CalcOfus",page_icon=image_path+"logo_InvRoxx_tab.png",layout="wide")

######################
#SIDEBAR
######################

with st.sidebar:
    st.image(image_path+"logo_nom_transp.png" )
    # st.page_link("https://d-bk.net/fr/tl/11eJ",label='**Biblio DofusBook**',icon="📚")

##############
# Présentation
##############

st.html('<div style="text-align: center; font-size: 50px;font-weight: bold"> Calcofus </div>')
st.html("""
        <div style='text-align: center; 
                    font-size:20px'>
        Sur cette page vous pouvez retrouver les différents outils que j'ai créé pour vous aider dans votre théorycraft, ainsi que les différents endroits où vous pouvez retrouver mon contenu.
        </div>""")
st.html("""
        <div style='text-align: center; 
                    font-size:20px'>
Vous pouvez utiliser la barre sur la gauche pour naviguer entre les outils, ou bien cliquer sur les noms en dessous.        </div>""")

##############
# Outils
##############
col1, col2,col3 = st.columns((1,1,1))
with col1:
    with st.container(border=True):
        st.page_link("page_invo.py",label='**CalcInvo**',icon=":material/cruelty_free:")
        st.write("""Calculateur de dégats des invocations
- importation des stats depuis dofusbook possible
- ou entrée des stats custom dans la sidebar""")
with col2:
    with st.container(border=True):
        st.page_link("page_sorts.py",label='**CalcSorts**',icon=":material/sword_rose:")
        st.write("Calculateur de ligne de dégats de sort")
with col3:
    with st.container(border=True):
        st.page_link("page_dopou.py",label='**CalcOpou**',icon=":material/directions_alt:")
        st.write("Calculateur de dégats de poussée")

##############
# Réseaux
##############
twitch, youtube,dofusbook = st.columns((1,1,1))
with twitch:
    with st.container(border=True):    
        st.page_link("https://www.twitch.tv/warp_is_fine",label='**Twitch**',icon="👾")
        st.write("Viens suivre avec moi les meilleurs tournois de dofus touch ❤️")
with youtube:
    with st.container(border=True):
        st.page_link("https://www.youtube.com/channel/UCVMa-curO2R2fJNQALwB2tQ",label='**Youtube**',icon="🔴")
        st.write("Ma chaîne youtube est remplie de matchs de tournois commentés, de retransmission de mes participations et plus encore")
with dofusbook:
    with st.container(border=True):
        st.page_link("https://d-bk.net/fr/tl/11eJ ",label='**Biblio DofusBook**',icon="📚")
        st.write("Tu peux y retrouver plus de 500 stuffs faits mains !")