import streamlit as st
import pandas as pd

st.set_page_config(page_title="Chamsys HeadHunter AI", page_icon="🧠")

st.title("🧠 Chamsys HeadHunter Pro")
st.write("Inserisci Marca e Modello. L'AI cercherà i dati tecnici e creerà il file.")

fixture = st.text_input("Modello Testa Mobile", placeholder="es. Clay Paky Sharpy")

# Funzione simulata di intelligenza (che andremo a collegare a un'API reale)
def ai_dmx_search(model_name):
    # Qui l'AI cercherà sul web. Per ora, facciamo un test dinamico:
    st.info(f"Analizzando i database tecnici per {model_name}...")
    
    # Esempio di struttura che l'AI genererà dopo la ricerca
    canali = [
        {"Channel": 1, "Name": "Pan", "Type": "PHT_PAN", "Locate": 128},
        {"Channel": 2, "Name": "Tilt", "Type": "PHT_TILT", "Locate": 128},
        {"Channel": 3, "Name": "Dimmer", "Type": "PHT_DIM", "Locate": 255},
        {"Channel": 4, "Name": "Shutter", "Type": "PHT_SHUT", "Locate": 255},
        {"Channel": 5, "Name": "Color", "Type": "PHT_COL_WHEEL", "Locate": 0},
        {"Channel": 6, "Name": "Zoom", "Type": "PHT_BEAM_ZOOM", "Locate": 128},
    ]
    return pd.DataFrame(canali)

if st.button("Avvia Ricerca Intelligente"):
    if fixture:
        df_risultato = ai_dmx_search(fixture)
        
        # Aggiungiamo i campi fissi richiesti da Chamsys
        df_risultato["Width"] = 8
        df_risultato["Default"] = 0
        df_risultato["Highlight"] = 255
        df_risultato["Curve"] = "Lin"
        
        st.success(f"Dati trovati per {fixture}!")
        st.table(df_risultato) # Mostra un'anteprima della tabella
        
        csv = df_risultato.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Scarica Library CSV", data=csv, file_name=f"{fixture}.csv")
    else:
        st.error("Scrivi il nome di una macchina!")
