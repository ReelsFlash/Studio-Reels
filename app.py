import streamlit as st
import os
from PIL import Image
from generator_scenarii import genereaza_scenariu_pro

st.set_page_config(page_title="Studio Reels Pro", layout="wide", page_icon="🎬")

st.title("🎬 Studio Reels - Panou de Control Unic")
st.caption("Aplicație mobilă și desktop pentru producție video originală!")

for f in ["assets/personaj", "scenarii", "output_clips"]:
    os.makedirs(f, exist_ok=True)

tab1, tab2, tab3 = st.tabs(["🔥 Scenarii Originale", "🎙️ Gestiune Voce & Audio", "🖼️ Personaj & Elemente"])

with tab1:
    st.subheader("Generator de Scenarii Unice")
    tema = st.text_input("Despre ce vrei să fie următorul clip?", "Secretele istoriei uitate")
    
    if st.button("🚀 Generează Scenariul și Indicațiile"):
        if tema:
            rezultat = genereaza_scenariu_pro(tema)
            st.success("Scenariul a fost creat cu succes!")
            st.text_area("Script complet + Indicații grafice:", rezultat, height=350)
        else:
            st.warning("Te rog introdu o temă validă.")

with tab2:
    st.subheader("Gestiune Audio / Voce")
    st.markdown("Încarcă sau înregistrează vocea ta direct de pe telefon:")
    audio_file = st.file_uploader("Alege fișierul audio (mp3, wav, m4a):", type=["mp3", "wav", "m4a"])
    
    if audio_file:
        st.audio(audio_file)
        st.success("Fișierul audio a fost încărcat în sistem!")

with tab3:
    st.subheader("Magazia cu Elemente Vizuale")
    st.markdown("Urcă poze noi pentru animații și fundaluri:")
    
    poza = st.file_uploader("Adaugă o imagine nouă:", type=["png", "jpg", "jpeg"])
    if poza:
        img = Image.open(poza)
        cale_salvare = os.path.join("assets/personaj", poza.name)
        img.save(cale_salvare)
        st.success(f"Am salvat imaginea: {poza.name}")

    st.markdown("---")
    st.subheader("Imagini active în sistem:")
    dir_assets = "assets/personaj"
    if os.path.exists(dir_assets):
        fisiere_poze = os.listdir(dir_assets)
        if fisiere_poze:
            cols = st.columns(3)
            for idx, p in enumerate(fisiere_poze):
                with cols[idx % 3]:
                    st.image(os.path.join(dir_assets, p), caption=p, width=110)
        else:
            st.info("Nicio imagine urcată momentan.")
