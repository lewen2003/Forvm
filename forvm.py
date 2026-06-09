import streamlit as st
import base64
import urllib.parse
from pathlib import Path

# ─── Page Config ───────────────────────────────────────────────────
st.set_page_config(
    page_title="FORVM — Prodotti Laziali Artigianali · Consegna 48h Roma",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── Helper: load image as base64 ──────────────────────────────────
def img_to_b64(path: str) -> str:
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except Exception:
        return ""

LOGO_B64 = img_to_b64("logo.jpeg")
BOX_B64  = img_to_b64("box_product.jpeg")

WHATSAPP_NUMBER = "393000000000"  # Sostituire col numero reale

# ─── Box Catalogue Data ────────────────────────────────────────────
BOXES = [
    {
        "id": "colazione",
        "name": "La Colazione Romana",
        "emoji": "☕",
        "tagline": "Il risveglio autentico della capitale",
        "desc": "Cornetti artigianali, maritozzo con panna, caffè di torrefazione storica, marmellata locale.",
        "ingredienti": ["Cornetti artigianali (x2 a persona)", "Maritozzo con panna", "Caffè Torrefazione Sant'Eustachio", "Marmellata di agrumi laziali", "Succo di arancia rossa Siciliana"],
        "prezzi": {1: 16, 2: 26, 3: 35},
        "stagione": "Tutto l'anno",
        "vino": None,
        "badge_color": "#8B5E3C",
    },
    {
        "id": "carbonara",
        "name": "La Carbonara",
        "emoji": "🍝",
        "tagline": "Kit completo per la ricetta originale",
        "desc": "Guanciale DOP, Pecorino Romano DOP, rigatoni trafilati al bronzo, uova fresche laziali, vino Frascati DOCG.",
        "ingredienti": ["Guanciale DOP di Amatrice (100g a persona)", "Pecorino Romano DOP (80g a persona)", "Rigatoni trafilati al bronzo (100g a persona)", "Uova fresche laziali (2 a persona)", "Pepe nero intero macinato fresco", "🍷 Frascati DOCG (75cl)"],
        "prezzi": {1: 18, 2: 28, 3: 38},
        "stagione": "Tutto l'anno",
        "vino": "Frascati DOCG",
        "badge_color": "#B5873A",
    },
    {
        "id": "amatriciana",
        "name": "La Amatriciana",
        "emoji": "🍅",
        "tagline": "La tradizione di Amatrice in una box",
        "desc": "Guanciale stagionato, pomodori San Marzano, Pecorino Romano, bucatini artigianali, Cesanese DOCG.",
        "ingredienti": ["Guanciale stagionato di Amatrice (100g a persona)", "Pomodori San Marzano DOP (200g a persona)", "Pecorino Romano DOP (60g a persona)", "Bucatini artigianali (100g a persona)", "🍷 Cesanese DOCG (75cl)"],
        "prezzi": {1: 17, 2: 27, 3: 37},
        "stagione": "Tutto l'anno",
        "vino": "Cesanese DOCG",
        "badge_color": "#B5873A",
    },
    {
        "id": "cacio",
        "name": "La Cacio e Pepe",
        "emoji": "🧀",
        "tagline": "Due ingredienti, una filosofia",
        "desc": "Pecorino Romano stagionato, pepe nero Tellicherry, spaghetti alla chitarra artigianali, Frascati DOC.",
        "ingredienti": ["Pecorino Romano stagionato 24 mesi (120g a persona)", "Pepe nero Tellicherry intero", "Spaghetti alla chitarra artigianali (100g a persona)", "🍷 Frascati DOC (75cl)"],
        "prezzi": {1: 16, 2: 26, 3: 36},
        "stagione": "Tutto l'anno",
        "vino": "Frascati DOC",
        "badge_color": "#B5873A",
    },
    {
        "id": "gricia",
        "name": "La Gricia",
        "emoji": "🥩",
        "tagline": "La madre di tutte le paste romane",
        "desc": "Guanciale artigianale, Pecorino Romano DOP, rigatoni di semola dura laziale, Marino DOC.",
        "ingredienti": ["Guanciale artigianale (110g a persona)", "Pecorino Romano DOP (80g a persona)", "Rigatoni di semola dura laziale (100g a persona)", "🍷 Marino DOC (75cl)"],
        "prezzi": {1: 17, 2: 27, 3: 37},
        "stagione": "Tutto l'anno",
        "vino": "Marino DOC",
        "badge_color": "#B5873A",
    },
    {
        "id": "pollo",
        "name": "Il Pollo con i Peperoni",
        "emoji": "🫑",
        "tagline": "Il secondo della domenica romana",
        "desc": "Pollo ruspante laziale, peperoni cornetti, aglio di Cori, vino bianco laziale, Frascati DOCG.",
        "ingredienti": ["Pollo ruspante laziale (300g a persona)", "Peperoni cornetti rossi e gialli", "Aglio di Cori", "Vino bianco laziale per cottura", "Rosmarino e alloro frescos", "🍷 Frascati DOCG (75cl)"],
        "prezzi": {1: 18, 2: 28, 3: 38},
        "stagione": "Estate · giu-set",
        "vino": "Frascati DOCG",
        "badge_color": "#4A7C59",
    },
    {
        "id": "caprese",
        "name": "La Caprese Laziale",
        "emoji": "🌿",
        "tagline": "Freschezza dei Castelli Romani",
        "desc": "Mozzarella di bufala DOP, pomodori cuore di bue laziali, basilico fresco, olio EVO dei Colli Sabini.",
        "ingredienti": ["Mozzarella di bufala DOP (150g a persona)", "Pomodori cuore di bue laziali (200g a persona)", "Basilico fresco del Lazio", "Olio EVO dei Colli Sabini DOP", "Sale marino di Cervia"],
        "prezzi": {1: 16, 2: 24, 3: 32},
        "stagione": "Stagionale · giu-set",
        "vino": None,
        "badge_color": "#4A7C59",
    },
    {
        "id": "cantina",
        "name": "La Cantina Laziale",
        "emoji": "🍷",
        "tagline": "Un viaggio tra i vigneti del Lazio",
        "desc": "Selezione di 2 vini DOCG laziali con tagliere di formaggi e salumi tipici. Minimo 2 persone.",
        "ingredienti": ["Frascati Superiore DOCG (75cl)", "Cesanese del Piglio DOCG (75cl)", "Pecorino Romano DOP (80g a persona)", "Guanciale stagionato (60g a persona)", "Olive di Gaeta DOP (50g a persona)", "Pane di Lariano (200g)"],
        "prezzi": {2: 38, 3: 48},
        "stagione": "Tutto l'anno",
        "vino": "2 vini DOCG",
        "badge_color": "#6B2D8B",
    },
    {
        "id": "dolci",
        "name": "I Dolci Romani",
        "emoji": "🍮",
        "tagline": "Il finale perfetto per una serata romana",
        "desc": "Tiramisù artigianale, crostata di visciole, biscotti del Lazio, Cannellino DOCG.",
        "ingredienti": ["Tiramisù artigianale (porzione a persona)", "Crostata di visciole laziale (100g a persona)", "Biscotti 'brutti ma buoni'", "Cioccolato fondente di artigiano romano", "🍷 Cannellino di Frascati DOCG (37.5cl)"],
        "prezzi": {1: 22, 2: 32, 3: 42},
        "stagione": "Tutto l'anno",
        "vino": "Cannellino DOCG",
        "badge_color": "#B5873A",
    },
    {
        "id": "chef",
        "name": "Chef a Domicilio",
        "emoji": "👨‍🍳",
        "tagline": "Roma in cucina, a casa tua",
        "desc": "Lo chef viene nel tuo appartamento e cucina un menu romano completo. Prenotazione obbligatoria con 48h di anticipo.",
        "ingredienti": ["Menu personalizzato dallo chef", "Tutti gli ingredienti inclusi", "Mise en place e servizio", "Abbinamento vini laziali", "Ricette originali da portare a casa"],
        "prezzi": {},
        "stagione": "Tutto l'anno",
        "vino": None,
        "badge_color": "#1B4332",
        "premium": True,
    },
]

def get_whatsapp_url(box_name: str, n_persons: int) -> str:
    if box_name == "Chef a Domicilio":
        msg = f"Ciao FORVM! 🏛️ Vorrei prenotare il servizio Chef a Domicilio. Persone: {n_persons} · Data preferita: [da completare] · Indirizzo: [da completare]"
    else:
        msg = f"Ciao FORVM! 🏛️ Vorrei ordinare {box_name} per {n_persons} person{'a' if n_persons == 1 else 'e'}. Indirizzo: [da completare]. Quando potete consegnare?"
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={urllib.parse.quote(msg)}"

# ─── CSS (Stili ad Alto Contrasto e Oro Acceso) ──────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400;1,600&family=DM+Sans:wght@300;400;500;600;700&display=swap');

/* Reset & Base */
*, *::before, *::after { box-sizing: border-box; }

.main .block-container {
    padding: 0 !important;
    max-width: 100% !important;
}

/* Nasconde elementi Streamlit */
#MainMenu, footer, header { visibility: hidden; }
.stDeployButton { display: none; }
[data-testid="stSidebar"] { display: none; }
[data-testid="collapsedControl"] { display: none; }

body { font-family: 'DM Sans', sans-serif; background-color: #FFFFFF !important; color: #111111 !important; }
h1, h2, h3 { font-family: 'Cormorant Garamond', serif; }

/* Testi Generici per Forzare la Leggibilità */
p, li, span, label, div {
    font-family: 'DM Sans', sans-serif;
}

/* ── NAV BAR ── */
.forvm-nav {
    position: sticky;
    top: 0;
    z-index: 1000;
    background: #0A2318 !important; /* Verde scurissimo per massimo contrasto */
    padding