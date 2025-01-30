import streamlit as st
image_path='images/'




######################
# Page Title
######################

st.set_page_config(page_title="CalcOfus",page_icon=image_path+"logo_InvRoxx_tab.png",layout="wide")

import os
current_os=os.name
st.write(current_os)

import platform
st.write(platform.platform())
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
        Sur cette page vous pouvez retrouver les différents outils que j'ai créé pour vous aider dans votre théorycraft.
        </div>""")
st.html("""
        <div style='text-align: center; 
                    font-size:20px'>
Utilisez la barre sur la gauche pour naviguer entre les outils, ou bien cliquer sur les noms ci-dessous.
        </div>""")

##############
# Outils
##############
col1, col2,col3 = st.columns((1,1,1))
with col1:
    with st.container(border=True):
        st.page_link("page_invo.py",label='**CalcInvo**',icon=":material/cruelty_free:", use_container_width=True)
        st.write("""Calculateur de dégats des invocations
- importation des stats depuis dofusbook possible
- ou entrée des stats custom dans la sidebar""")
with col2:
    with st.container(border=True):
        st.page_link("page_sorts.py",label='**CalcSorts**',icon=":material/sword_rose:", use_container_width=True)
        st.write("Calculateur de ligne de dégats de sort")
with col3:
    with st.container(border=True):
        st.page_link("page_dopou.py",label='**CalcOpou**',icon=":material/directions_alt:", use_container_width=True)
        st.write("Calculateur de dégats de poussée")

st.html("""
        <div style='text-align: center; 
                    font-size:20px'>
Si vous le voulez vous pouvez aussi suivre mes différents projets :
        </div>""")
##############
# Réseaux
##############
twitch, youtube,warpBot = st.columns((1,1,1))
with twitch:
    with st.container(border=True):    
        st.page_link("https://www.twitch.tv/warp_is_fine",label='**Twitch**',icon="👾", use_container_width=True)
        st.write("Viens suivre avec moi les meilleurs tournois de dofus touch ❤️")
        st.link_button("Follow la chaîne pour être prévenu quand je lance un stream", "https://www.twitch.tv/warp_is_fine", help=None, type="secondary", icon="🎙️", disabled=False, use_container_width=True)

with youtube:
    with st.container(border=True):
        st.page_link("https://www.youtube.com/channel/UCVMa-curO2R2fJNQALwB2tQ",label='**Youtube**',icon="🔴", use_container_width=True)
        st.write("Ma chaîne youtube est remplie de matchs de tournois commentés, de retransmission de mes participations et plus encore")
        st.link_button("Abonne toi pour ne rien manquer", "https://www.youtube.com/channel/UCVMa-curO2R2fJNQALwB2tQ", help=None, type="secondary", icon="🎥", disabled=False, use_container_width=True)

with warpBot:
    with st.container(border=True):
        st.page_link("https://discord.com/oauth2/authorize?client_id=1288167324586872842",label='**WarpBot**',icon="🤖")
        st.write("Ce bot discord sert à vous recommander les meilleurs stuff pvp actuellement, donnez lui un élément et ils vous rendra une liste de liens dofusbook de qualité incomparable 🤩")
        st.link_button("Ajoute le sur discord 🤖", "https://discord.com/oauth2/authorize?client_id=1288167324586872842", help=None, type="secondary", icon="🤖", disabled=False, use_container_width=True)


dofusbook, vide1,vide2 = st.columns((1,1,1))
with dofusbook:
    with st.container(border=True):    
        st.page_link("https://d-bk.net/fr/tl/11eJ",label='**Biblio DofusBook**',icon="📚", use_container_width=True)
        st.write("Tu peux y retrouver plus de 500 stuffs faits mains !")
        st.link_button("C'est par ici les stuffs!", "https://d-bk.net/fr/tl/11eJ", help=None, type="secondary", icon="🥋", disabled=False, use_container_width=True)
with vide1:
    with st.container(border=True):
        pass
with vide2:
    with st.container(border=True):
        pass