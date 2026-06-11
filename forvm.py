import streamlit as st
import streamlit.components.v1 as components
import base64
import os

# ─── CONFIGURAZIONE DELLA PAGINA ───────────────────────────────────
st.set_page_config(
    page_title="FORVM — Prodotti Laziali Artigianali · Consegna 48h Roma",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Rimuove i margini di Streamlit e l'interfaccia nativa per un look 100% full-screen
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
        }
        iframe {
            display: block;
            width: 100vw;
            height: 100vh;
            border: none;
        }
    </style>
""", unsafe_allow_html=True)

# ─── HELPER: CONVERSIONE IMMAGINI IN BASE64 ────────────────────────
def img_to_b64(path: str) -> str:
    if os.path.exists(path):
        try:
            with open(path, "rb") as f:
                return base64.b64encode(f.read()).decode()
        except Exception:
            return ""
    return ""

# ─── HELPER: OTTIMIZZAZIONE E LETTURA DEI FILE HTML ────────────────
def get_enhanced_html(file_name: str) -> str:
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            html_content = f.read()
        
        # 1. Iniezione automatica delle immagini locali caricate
        local_images = ["catalogo.jpg", "chisiamo.jpg", "funziona.jpg"]
        for img in local_images:
            if img in html_content:
                b64_str = img_to_b64(img)
                if b64_str:
                    ext = img.split(".")[-1].lower()
                    mime = "image/png" if ext == "png" else "image/jpeg"
                    # Sostituisce i riferimenti src standard con i dati Base64 incorporati
                    html_content = html_content.replace(f'src="{img}"', f'src="data:{mime};base64,{b64_str}"')
                    html_content = html_content.replace(f"src='{img}'", f"src='data:{mime};base64,{b64_str}'")
        
        # 2. Correzione dei Link per la navigazione nell'Iframe di Streamlit
        # Cambiando target="_self" in target="_parent", i link aggiorneranno la scheda principale del browser
        html_content = html_content.replace('target="_self"', 'target="_parent"')
        html_content = html_content.replace("target='_self'", "target='_parent'")
        
        # Se alcuni link non hanno il target impostato, lo forziamo sui parametri di pagina
        html_content = html_content.replace('href="?p=', 'target="_parent" href="?p=')
        html_content = html_content.replace("href='?p=", "target='_parent' href='?p=")
                    
        return html_content
    except FileNotFoundError:
        return f"<h3 style='color:red; padding:20px;'>Errore: Il file monumentale <code>{file_name}</code> non è stato trovato.</h3>"

# ─── ROUTING DI NAVIGAZIONE (QUERY PARAMETERS) ─────────────────────
# Legge il parametro '?p=' dall'URL corrente del browser
query_params = st.query_params
current_page = query_params.get("p", "home")

# Mappa le abbreviazioni dell'URL sui rispettivi file HTML caricati
PAGES_MAP = {
    "home": "forvm_home_page_monumentale_desktop.html",
    "catalogo": "forvm_catalogo_desktop.html",
    "come_funziona": "forvm_come_funziona_desktop.html",
    "chi_siamo": "forvm_chi_siamo_desktop.html",
    "partner": "forvm_host_partner_desktop.html"
}

# Identifica il file corretto o rimanda alla Home come fallback
target_html_file = PAGES_MAP.get(current_page, "forvm_home_page_monumentale_desktop.html")

# Ottiene il codice della pagina ottimizzato e pronto per il rendering
final_html_content = get_enhanced_html(target_html_file)

# ─── RENDERING DELL'INTERFACCIA DENTRO STREAMLIT ───────────────────
# Mostra la pagina HTML. L'altezza è impostata ampia per accomodare le sezioni lunghe delle box
components.html(final_html_content, height=3200, scrolling=True)