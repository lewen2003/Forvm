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

# Rimuove i margini di Streamlit per consentire una visualizzazione a schermo intero
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

# ─── HELPER: OTTIMIZZAZIONE HTML E REWRITING DEI LINK ──────────────
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
                    html_content = html_content.replace(f'src="{img}"', f'src="data:{mime};base64,{b64_str}"')
                    html_content = html_content.replace(f"src='{img}'", f"src='data:{mime};base64,{b64_str}'")
        
        # 2. RISOLUZIONE DEL PROBLEMA DI NAVIGAZIONE
        # Mappiamo i nomi dei file HTML reali sui parametri di navigazione di Streamlit
        PAGES_MAP = {
            "forvm_home_page_monumentale_desktop.html": "home",
            "forvm_catalogo_desktop.html": "catalogo",
            "forvm_come_funziona_desktop.html": "come_funziona",
            "forvm_chi_siamo_desktop.html": "chi_siamo",
            "forvm_host_partner_desktop.html": "partner"
        }
        
        # Sostituiamo i collegamenti ipertestuali statici dei file con le query di Streamlit
        # L'aggiunta di target="_parent" è FONDAMENTALE: dice al browser di rompere l'Iframe e aggiornare la barra degli indirizzi principale
        for html_file, page_slug in PAGES_MAP.items():
            html_content = html_content.replace(f'href="{html_file}"', f'href="?p={page_slug}" target="_parent"')
            html_content = html_content.replace(f"href='{html_file}'", f"href='?p={page_slug}' target='_parent'")
            
            # Riconosce e sistema anche varianti di link che usano percorsi parziali o relativi
            html_content = html_content.replace(f'href="./{html_file}"', f'href="?p={page_slug}" target="_parent"')
            html_content = html_content.replace(f"href='./{html_file}'", f"href='?p={page_slug}' target='_parent'")

        # Uniforma eventuali link nativi già scritti come parametri query aggiungendo il target corretto
        for page_slug in PAGES_MAP.values():
            if f'href="?p={page_slug}"' in html_content and 'target="_parent"' not in html_content:
                html_content = html_content.replace(f'href="?p={page_slug}"', f'href="?p={page_slug}" target="_parent"')
            if f"href='?p={page_slug}'" in html_content and "target='_parent'" not in html_content:
                html_content = html_content.replace(f"href='?p={page_slug}'", f"href='?p={page_slug}' target='_parent'")
                    
        return html_content
    except FileNotFoundError:
        return f"<h3 style='color:red; padding:20px;'>Errore: Il file monumentale <code>{file_name}</code> non è stato trovato.</h3>"

# ─── ROUTING DI NAVIGAZIONE (QUERY PARAMETERS) ─────────────────────
query_params = st.query_params
current_page = query_params.get("p", "home")

FILE_ROUTING = {
    "home": "forvm_home_page_monumentale_desktop.html",
    "catalogo": "forvm_catalogo_desktop.html",
    "come_funziona": "forvm_come_funziona_desktop.html",
    "chi_siamo": "forvm_chi_siamo_desktop.html",
    "partner": "forvm_host_partner_desktop.html"
}

# Identifica il file corrente da caricare
target_html_file = FILE_ROUTING.get(current_page, "forvm_home_page_monumentale_desktop.html")

# Genera l'HTML finale modificato con i link corretti
final_html_content = get_enhanced_html(target_html_file)

# ─── RENDERING ─────────────────────────────────────────────────────
# L'altezza è impostata per contenere agevolmente le pagine lunghe
components.html(final_html_content, height=3500, scrolling=True)