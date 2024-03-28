import streamlit as st
    


    ######################
    #Craqueleur
    ######################

    st.write("## Craqueleur")

    craq_chance_base=300

    craq_chance=craq_chance_base+stats_perso["Chance"]/2
    craq_do=stats_perso["Doeau"]/2

    ecrasement_min=(28*(100+craq_chance)/100+craq_do)//1
    ecrasement_max=(33*(100+craq_chance)/100+craq_do)//1

    frappe_etourdissante_min=(33*(100+craq_chance)/100+craq_do)//1
    frappe_etourdissante_max=(37*(100+craq_chance)/100+craq_do)//1


    tab_vita_craq="""
| Vitalité |
| ----------- |
"""
    tab_vita_drag+="| "+str(int(calcul_vita(265,0.25)))+" |\n"

    st.write(tab_vita_drag)
    st.text("")

    tab_drag="""
| Sort | Valeur min | Valeur max |
| ----------- | ----------- | ----------- |
"""
    tab_drag+="| Ecrasement | "+str(int(ecrasement_min))+" | "+str(int(ecrasement_max))+" |\n"
    tab_drag+="| Frappe étourdissante (rall pa) | "+str(int(frappe_etourdissante_min))+" | "+str(int(frappe_etourdissante_max))+" |\n"
    
    st.write(tab_drag)

    st.text("")