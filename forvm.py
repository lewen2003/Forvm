import streamlit as st
import base64
from pathlib import Path

# ─── Page Config ───────────────────────────────────────────────────
st.set_page_config(
    page_title="FORVM — Prodotti Laziali Artigianali · Consegna 48h Roma",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── Query Params & Session State Sync ──────────────────────────────
# Gestione elegante della navigazione tramite URL Query Params
if "page" in st.query_params:
    st.session_state.page = st.query_params["page"]
else:
    st.query_params["page"] = "home"
    st.session_state.page = "home"

if "persons" not in st.session_state:
    st.session_state.persons = 2

# ─── Helper: load image as base64 ──────────────────────────────────
def img_to_b64(path: str) -> str:
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except Exception:
        return ""

LOGO_B64 = img_to_b64("logo.jpeg")
BOX_B64  = img_to_b64("box_product.jpeg")

WHATSAPP_NUMBER = "393000000000"  # Placeholder — sostituire col numero reale

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
        "tagline": "La tradition di Amatrice in una box",
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
        "ingredienti": ["Pollo ruspante laziale (300g a persona)", "Peperoni cornetti rossi e gialli", "Aglio di Cori", "Vino bianco laziale per cottura", "Rosmarino e alloro freschi", "🍷 Frascati DOCG (75cl)"],
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

# ─── Helper: Calcolo del Totale Dinamico ed Estrapolazione Prezzi ────
def get_box_price_block(box, persons):
    if not box["prezzi"]:
        return '<div class="box-price-na">Prezzo su richiesta &mdash; scrivici su WhatsApp</div>'
    
    if persons in box["prezzi"]:
        total_price = box["prezzi"][persons]
    else:
        max_key = max(box["prezzi"].keys())
        min_key = min(box["prezzi"].keys())
        if persons > max_key:
            # Calcola la quota addizionale basata sull'ultimo incremento noto
            if max_key > 1:
                extra_cost = box["prezzi"][max_key] - box["prezzi"][max_key - 1]
            else:
                extra_cost = box["prezzi"][max_key]
            total_price = box["prezzi"][max_key] + (persons - max_key) * extra_cost
        else:
            total_price = box["prezzi"][min_key]
            
    price_per_person = total_price / persons
    return f'<div class="box-price">Prezzo Totale: &euro; {total_price} <span style="font-size: 14px; font-weight: 400; color: #888; font-family: \'DM Sans\', sans-serif;">(&euro; {price_per_person:.2f} / persona)</span></div>'

def get_whatsapp_url(box_name: str, n_persons: int) -> str:
    if box_name == "Chef a Domicilio":
        msg = f"Ciao FORVM! 🏛️ Vorrei prenotare il servizio Chef a Domicilio. Persone: {n_persons} · Data preferita: [da completare] · Indirizzo: [da completare]"
    else:
        msg = f"Ciao FORVM! 🏛️ Vorrei ordinare {box_name} per {n_persons} person{'a' if n_persons == 1 else 'e'}. Indirizzo: [da completare]. Quando potete consegnare?"
    import urllib.parse
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={urllib.parse.quote(msg)}"

# ─── CSS ───────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400;1,600&family=DM+Sans:wght@300;400;500;600&display=swap');

/* Reset & Base */
*, *::before, *::after { box-sizing: border-box; }

.main .block-container {
    padding: 0 !important;
    max-width: 100% !important;
}

/* Hide Streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.stDeployButton { display: none; }
[data-testid="stSidebar"] { display: none; }
[data-testid="collapsedControl"] { display: none; }

/* Typography */
body { font-family: 'DM Sans', sans-serif; }
h1, h2, h3 { font-family: 'Cormorant Garamond', serif; }

/* ── NAV ── */
.forvm-nav {
    position: sticky;
    top: 0;
    z-index: 1000;
    background: #1B4332;
    padding: 0 40px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    height: 64px;
    border-bottom: 1px solid rgba(181,135,58,0.3);
}
.forvm-nav-logo {
    font-family: 'Cormorant Garamond', serif;
    font-size: 26px;
    font-weight: 700;
    color: #B5873A;
    letter-spacing: 4px;
    text-decoration: none;
    cursor: pointer;
}
.forvm-nav-links {
    display: flex;
    align-items: center;
    gap: 32px;
}
.forvm-nav-links a {
    font-family: 'DM Sans', sans-serif;
    font-size: 13px;
    font-weight: 600;
    color: #F9F5EE;
    text-decoration: none;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    opacity: 0.85;
    transition: opacity 0.2s, color 0.2s;
}
.forvm-nav-links a:hover { opacity: 1; color: #B5873A; }
.nav-wa-btn {
    background: #25D366 !important;
    color: white !important;
    padding: 8px 18px !important;
    border-radius: 24px !important;
    font-size: 13px !important;
    font-weight: 600 !important;
    text-decoration: none !important;
    display: flex !important;
    align-items: center !important;
    gap: 6px !important;
    opacity: 1 !important;
}
.nav-wa-btn:hover { background: #1fb855 !important; }

/* ── HERO ── */
.hero-section {
    position: relative;
    width: 100%;
    min-height: 88vh;
    background: linear-gradient(155deg, #0d2b1f 0%, #1B4332 45%, #2d5a44 100%);
    display: flex;
    align-items: center;
    overflow: hidden;
}
.hero-pattern {
    position: absolute;
    inset: 0;
    opacity: 0.04;
    background-image: repeating-linear-gradient(45deg, #B5873A 0px, #B5873A 1px, transparent 0px, transparent 50%);
    background-size: 20px 20px;
}
.hero-arch {
    position: absolute;
    right: 5%;
    top: 50%;
    transform: translateY(-50%);
    opacity: 0.12;
    font-size: 320px;
    line-height: 1;
    color: #B5873A;
    pointer-events: none;
    select: none;
    font-family: 'Cormorant Garamond', serif;
}
.hero-content {
    position: relative;
    z-index: 2;
    padding: 80px 80px 80px 80px;
    max-width: 680px;
}
.hero-eyebrow {
    font-family: 'DM Sans', sans-serif;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #B5873A;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    gap: 12px;
}
.hero-eyebrow::after {
    content: '';
    display: block;
    width: 40px;
    height: 1px;
    background: #B5873A;
}
.hero-h1 {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(48px, 6vw, 82px);
    font-weight: 600;
    line-height: 1.08;
    color: #F9F5EE;
    margin: 0 0 8px 0;
}
.hero-h1 em {
    font-style: italic;
    color: #B5873A;
}
.hero-subtitle {
    font-family: 'DM Sans', sans-serif;
    font-size: 17px;
    font-weight: 300;
    line-height: 1.7;
    color: rgba(249,245,238,0.8);
    margin: 24px 0 44px 0;
    max-width: 480px;
}
.hero-ctas {
    display: flex;
    gap: 16px;
    flex-wrap: wrap;
}
.btn-primary {
    display: inline-block;
    background: #B5873A;
    color: #1B4332;
    font-family: 'DM Sans', sans-serif;
    font-size: 14px;
    font-weight: 600;
    letter-spacing: 1px;
    text-transform: uppercase;
    padding: 16px 32px;
    text-decoration: none;
    transition: all 0.25s;
    border: 2px solid #B5873A;
}
.btn-primary:hover { background: #c9973f; border-color: #c9973f; }

.btn-whatsapp {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    background: transparent;
    color: #F9F5EE;
    font-family: 'DM Sans', sans-serif;
    font-size: 14px;
    font-weight: 500;
    padding: 16px 32px;
    text-decoration: none;
    border: 2px solid rgba(249,245,238,0.3);
    transition: all 0.25s;
}
.btn-whatsapp:hover { border-color: #25D366; color: #25D366; }
.btn-whatsapp .wa-dot { color: #25D366; font-size: 18px; }

/* ── SECTION SHELL ── */
.section {
    padding: 80px 80px;
    width: 100%;
}
.section-alt { background: #F9F5EE; }
.section-dark { background: #1B4332; }

.section-label {
    font-family: 'DM Sans', sans-serif;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #B5873A;
    margin-bottom: 12px;
}
.section-h2 {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(34px, 4vw, 54px);
    font-weight: 600;
    line-height: 1.12;
    color: #1B4332;
    margin: 0 0 16px 0;
}
.section-h2.light { color: #F9F5EE; }
.section-sub {
    font-family: 'DM Sans', sans-serif;
    font-size: 16px;
    font-weight: 300;
    line-height: 1.7;
    color: #4a4a4a;
    max-width: 560px;
}
.section-sub.light { color: rgba(249,245,238,0.75); }

/* ── THREE VALUES ── */
.values-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 0;
    margin-top: 0;
    border-top: 1px solid rgba(181,135,58,0.25);
    border-left: 1px solid rgba(181,135,58,0.25);
}
.value-card {
    padding: 40px 36px;
    border-right: 1px solid rgba(181,135,58,0.25);
    border-bottom: 1px solid rgba(181,135,58,0.25);
    background: #F9F5EE;
    transition: background 0.25s;
}
.value-card:hover { background: #f2ece1; }
.value-icon {
    font-size: 32px;
    margin-bottom: 16px;
    display: block;
}
.value-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 22px;
    font-weight: 600;
    color: #1B4332;
    margin-bottom: 8px;
}
.value-text {
    font-family: 'DM Sans', sans-serif;
    font-size: 14px;
    font-weight: 300;
    line-height: 1.65;
    color: #5a5a5a;
}

/* ── BOX CARDS ── */
.person-selector {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 40px;
}
.person-selector-label {
    font-family: 'DM Sans', sans-serif;
    font-size: 13px;
    font-weight: 500;
    color: #1B4332;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-right: 8px;
}

.boxes-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 2px;
    background: rgba(181,135,58,0.15);
}
.box-card {
    background: #fff;
    padding: 36px;
    display: flex;
    flex-direction: column;
    gap: 0;
    transition: background 0.2s;
}
.box-card:hover { background: #fdfaf5; }
.box-number {
    font-family: 'DM Sans', sans-serif;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 2px;
    color: #B5873A;
    margin-bottom: 10px;
    text-transform: uppercase;
}
.box-header {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    margin-bottom: 8px;
}
.box-name {
    font-family: 'Cormorant Garamond', serif;
    font-size: 26px;
    font-weight: 600;
    color: #1B4332;
    line-height: 1.2;
}
.box-emoji { font-size: 28px; }
.box-stagione {
    display: inline-block;
    font-family: 'DM Sans', sans-serif;
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 1px;
    padding: 3px 10px;
    border-radius: 2px;
    margin-bottom: 12px;
}
.stagione-estate { background: #fff3cd; color: #856404; }
.stagione-tutto { background: rgba(27,67,50,0.08); color: #1B4332; }
.stagione-stagionale { background: #d1ecf1; color: #0c5460; }
.stagione-premium { background: #1B4332; color: #B5873A; }

.box-desc {
    font-family: 'DM Sans', sans-serif;
    font-size: 14px;
    font-weight: 300;
    line-height: 1.65;
    color: #5a5a5a;
    margin-bottom: 16px;
    flex: 1;
}
.box-vino {
    font-family: 'DM Sans', sans-serif;
    font-size: 12px;
    font-weight: 500;
    color: #6B2D8B;
    margin-bottom: 12px;
}
.box-price {
    font-family: 'Cormorant Garamond', serif;
    font-size: 22px;
    font-weight: 600;
    color: #1B4332;
    margin-bottom: 4px;
}
.box-price span { font-size: 15px; font-weight: 400; color: #888; font-family: 'DM Sans', sans-serif; }
.box-price-na {
    font-family: 'DM Sans', sans-serif;
    font-size: 14px;
    font-weight: 400;
    color: #B5873A;
    font-style: italic;
    margin-bottom: 4px;
}
.box-btn {
    display: inline-block;
    width: 100%;
    text-align: center;
    background: #1B4332;
    color: #F9F5EE;
    font-family: 'DM Sans', sans-serif;
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 1px;
    text-transform: uppercase;
    padding: 14px 20px;
    text-decoration: none;
    margin-top: 16px;
    border: 2px solid #1B4332;
    transition: all 0.22s;
}
.box-btn:hover { background: transparent; color: #1B4332; }
.box-btn.gold { background: #B5873A; border-color: #B5873A; color: #fff; }
.box-btn.gold:hover { background: #1B4332; border-color: #1B4332; }

/* Accordion Ingredienti Estetico */
.ing-details { margin: 14px 0 10px 0; }
.ing-summary {
    font-family: 'DM Sans', sans-serif;
    font-size: 13px;
    font-weight: 500;
    color: #B5873A;
    cursor: pointer;
    user-select: none;
    margin-bottom: 4px;
    text-decoration: underline;
    text-underline-offset: 4px;
}
.ing-list {
    margin: 8px 0 0 0;
    padding-left: 18px;
    font-family: 'DM Sans', sans-serif;
    font-size: 13px;
    color: #5a5a5a;
    line-height: 1.7;
}

/* ── HOW IT WORKS ── */
.steps-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 0;
    margin-top: 48px;
    position: relative;
}
.step-item {
    padding: 0 32px 0 0;
    position: relative;
}
.step-item:not(:last-child)::after {
    content: '→';
    position: absolute;
    right: 8px;
    top: 16px;
    font-size: 20px;
    color: rgba(181,135,58,0.4);
}
.step-num {
    font-family: 'Cormorant Garamond', serif;
    font-size: 56px;
    font-weight: 400;
    color: #B5873A;
    line-height: 1;
    margin-bottom: 8px;
}
.step-icon { font-size: 28px; margin-bottom: 12px; display: block; }
.step-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 22px;
    font-weight: 600;
    color: #F9F5EE;
    margin-bottom: 8px;
}
.step-text {
    font-family: 'DM Sans', sans-serif;
    font-size: 14px;
    font-weight: 300;
    line-height: 1.65;
    color: rgba(249,245,238,0.7);
}

/* ── FAQ ── */
.faq-item {
    border-bottom: 1px solid rgba(27,67,50,0.12);
    padding: 20px 0;
}
.faq-q {
    font-family: 'Cormorant Garamond', serif;
    font-size: 20px;
    font-weight: 600;
    color: #1B4332;
    margin-bottom: 10px;
}
.faq-a {
    font-family: 'DM Sans', sans-serif;
    font-size: 14px;
    font-weight: 300;
    line-height: 1.7;
    color: #5a5a5a;
}

/* ── CHI SIAMO ── */
.chef-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 80px;
    align-items: center;
    margin-top: 48px;
}
.chef-text p {
    font-family: 'DM Sans', sans-serif;
    font-size: 16px;
    font-weight: 300;
    line-height: 1.8;
    color: #4a4a4a;
    margin-bottom: 20px;
}
.chef-quote {
    font-family: 'Cormorant Garamond', serif;
    font-size: 24px;
    font-style: italic;
    color: #1B4332;
    border-left: 3px solid #B5873A;
    padding-left: 20px;
    margin: 28px 0;
    line-height: 1.5;
}
.chef-img-wrap {
    position: relative;
}
.chef-img-wrap::before {
    content: '';
    position: absolute;
    top: 16px;
    left: 16px;
    right: -16px;
    bottom: -16px;
    border: 2px solid rgba(181,135,58,0.3);
    z-index: 0;
}
.chef-img-wrap img {
    position: relative;
    z-index: 1;
    width: 100%;
    display: block;
}

/* ── PARTNERSHIP ── */
.partner-benefits {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 2px;
    background: rgba(181,135,58,0.15);
    margin: 48px 0;
}
.partner-benefit {
    background: #F9F5EE;
    padding: 36px;
    text-align: center;
}
.partner-benefit-icon { font-size: 36px; margin-bottom: 16px; display: block; }
.partner-benefit-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 22px;
    font-weight: 600;
    color: #1B4332;
    margin-bottom: 8px;
}
.partner-benefit-text {
    font-family: 'DM Sans', sans-serif;
    font-size: 14px;
    font-weight: 300;
    color: #5a5a5a;
    line-height: 1.6;
}

/* ── FOOTER ── */
.forvm-footer {
    background: #0d2b1f;
    color: #F9F5EE;
    padding: 56px 80px 32px;
    border-top: 1px solid rgba(181,135,58,0.2);
}
.footer-top {
    display: grid;
    grid-template-columns: 2fr 1fr 1fr;
    gap: 48px;
    margin-bottom: 40px;
}
.footer-logo {
    font-family: 'Cormorant Garamond', serif;
    font-size: 32px;
    font-weight: 700;
    color: #B5873A;
    letter-spacing: 4px;
    margin-bottom: 12px;
}
.footer-tagline {
    font-family: 'DM Sans', sans-serif;
    font-size: 13px;
    font-weight: 300;
    color: rgba(249,245,238,0.6);
    line-height: 1.6;
}
.footer-col-title {
    font-family: 'DM Sans', sans-serif;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #B5873A;
    margin-bottom: 16px;
}
.footer-links {
    display: flex;
    flex-direction: column;
    gap: 10px;
}
.footer-links a {
    font-family: 'DM Sans', sans-serif;
    font-size: 13px;
    font-weight: 300;
    color: rgba(249,245,238,0.7);
    text-decoration: none;
    transition: color 0.2s;
}
.footer-links a:hover { color: #B5873A; }
.footer-bottom {
    border-top: 1px solid rgba(249,245,238,0.08);
    padding-top: 24px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.footer-copy {
    font-family: 'DM Sans', sans-serif;
    font-size: 12px;
    color: rgba(249,245,238,0.35);
}

/* ── FLOATING WA BUTTON ── */
.wa-float {
    position: fixed;
    bottom: 28px;
    right: 28px;
    z-index: 9999;
    background: #25D366;
    color: white;
    padding: 14px 22px 14px 18px;
    border-radius: 50px;
    font-family: 'DM Sans', sans-serif;
    font-size: 14px;
    font-weight: 600;
    text-decoration: none;
    display: flex;
    align-items: center;
    gap: 10px;
    box-shadow: 0 4px 20px rgba(37,211,102,0.4);
    transition: all 0.25s;
    animation: pulse-wa 3s infinite;
}
.wa-float:hover { background: #1db553; box-shadow: 0 6px 28px rgba(37,211,102,0.5); transform: translateY(-2px); }
@keyframes pulse-wa {
    0%, 100% { box-shadow: 0 4px 20px rgba(37,211,102,0.4); }
    50% { box-shadow: 0 4px 28px rgba(37,211,102,0.65); }
}
.wa-icon { font-size: 20px; }

/* Streamlit widgets hide overrides */
.stSelectbox, .stRadio { display: none !important; }
div[data-testid="stHorizontalBlock"] { gap: 0 !important; }

/* mobile */
@media (max-width: 768px) {
    .section { padding: 48px 20px; }
    .hero-content { padding: 56px 24px; }
    .boxes-grid { grid-template-columns: 1fr; }
    .values-grid { grid-template-columns: 1fr; }
    .steps-grid { grid-template-columns: 1fr 1fr; }
    .chef-grid { grid-template-columns: 1fr; }
    .partner-benefits { grid-template-columns: 1fr; }
    .footer-top { grid-template-columns: 1fr; gap: 32px; }
    .forvm-nav { padding: 0 20px; }
    .forvm-nav-links { display: none; }
    .hero-h1 { font-size: 42px; }
}
</style>
""", unsafe_allow_html=True)

# ─── Navigation Bar Elegant (HTML + Query Params Native Links) ───
wa_general = f"https://wa.me/{WHATSAPP_NUMBER}?text=Ciao%20FORVM!%20%F0%9F%9B%8F%EF%B8%8F%20Vorrei%20ordinare%20una%20box%20laziale%20%E2%80%94%20potete%20aiutarmi%3F"

st.markdown(f"""
<nav class="forvm-nav">
    <a href="/?page=home" target="_self" class="forvm-nav-logo">FORVM</a>
    <div class="forvm-nav-links">
        <a href="/?page=home" target="_self">Home</a>
        <a href="/?page=catalogo" target="_self">Catalogo</a>
        <a href="/?page=come_funziona" target="_self">Come Funziona</a>
        <a href="/?page=chi_siamo" target="_self">Chi Siamo</a>
        <a href="/?page=partner" target="_self">Per gli Host</a>
        <a href="{wa_general}" target="_blank" class="nav-wa-btn">
            <span>📱</span> Ordina su WhatsApp
        </a>
    </div>
</nav>
""", unsafe_allow_html=True)

current_page = st.session_state.page

# ══════════════════════════════════════════════════════════════════
# PAGE: HOME
# ══════════════════════════════════════════════════════════════════
if current_page == "home":

    # Hero
    st.markdown(f"""
    <div class="hero-section">
        <div class="hero-pattern"></div>
        <div class="hero-arch">🏛</div>
        <div class="hero-content">
            <div class="hero-eyebrow">Roma · Lazio · Artigianale</div>
            <h1 class="hero-h1"><em>Il mercato di Roma.</em><br>2000 anni dopo.</h1>
            <p class="hero-subtitle">
                Prodotti laziali artigianali selezionati dallo chef, consegnati nel tuo appartamento entro 48 ore.
                Carbonara, Amatriciana, Cacio e Pepe — kit completi per cucinare come un romano.
            </p>
            <div class="hero-ctas">
                <a href="/?page=catalogo" target="_self" class="btn-primary">Scopri le Box</a>
                <a href="{wa_general}" target="_blank" class="btn-whatsapp">
                    <span class="wa-dot">●</span> Ordina su WhatsApp
                </a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Three Values
    st.markdown("""
    <div style="padding: 0 80px; background: #F9F5EE;">
        <div class="values-grid">
            <div class="value-card">
                <span class="value-icon">🏛️</span>
                <div class="value-title">Selezionato dallo chef</div>
                <div class="value-text">Ogni prodotto scelto personalmente tra i migliori produttori laziali — nessun catalogo generico, nessun compromesso.</div>
            </div>
            <div class="value-card">
                <span class="value-icon">📦</span>
                <div class="value-title">Consegna in 48 ore</div>
                <div class="value-text">Direttamente nel tuo appartamento Airbnb — senza uscire, senza cercare, senza deludere.</div>
            </div>
            <div class="value-card">
                <span class="value-icon">🍷</span>
                <div class="value-title">Ingrediente laziale</div>
                <div class="value-text">Produttori locali, botteghe storiche, il territorio romano in ogni box — abbinato al vino della stessa terra.</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Preview Boxes (top 4)
    st.markdown("""
    <div class="section section-alt" style="padding-top: 64px;">
        <div class="section-label">Le Box in Evidenza</div>
        <h2 class="section-h2">A tavola con Roma</h2>
        <p class="section-sub">Le box più amate dai nostri ospiti. Ingredienti artigianali, ricetta dello chef, vino laziale abbinato.</p>
    </div>
    """, unsafe_allow_html=True)

    persons = st.session_state.persons
    preview_boxes = BOXES[:4]

    left_prev = ""
    right_prev = ""
    for i, box in enumerate(preview_boxes):
        price_block = get_box_price_block(box, persons)
        vino_badge = f'<div class="box-vino">&#127863; {box["vino"]} incluso</div>' if box["vino"] else ""
        stage_cls = "stagione-estate" if "Estate" in box["stagione"] or "Stagionale" in box["stagione"] else "stagione-tutto"
        if box.get("premium"):
            stage_cls = "stagione-premium"
        wa_url = get_whatsapp_url(box["name"], persons)
        
        # Gestione ingredienti a tendina anche per la Home
        ing_items = "".join(f"<li>{ing}</li>" for ing in box["ingredienti"])
        ingredienti_block = (
            f'<details class="ing-details">'
            f'<summary class="ing-summary">&#9660; Vedi ingredienti kit</summary>'
            f'<ul class="ing-list">{ing_items}</ul>'
            f'</details>'
        )

        card = (
            f'<div class="box-card" style="min-height:360px;">'
            f'<div class="box-header">'
            f'<div><div class="box-number">Box {str(i+1).zfill(2)}</div>'
            f'<div class="box-name">{box["name"]}</div></div>'
            f'<span class="box-emoji">{box["emoji"]}</span>'
            f'</div>'
            f'<span class="box-stagione {stage_cls}">{box["stagione"]}</span>'
            f'<p class="box-desc">{box["desc"]}</p>'
            f'{vino_badge}'
            f'{ingredienti_block}'
            f'{price_block}'
            f'<a href="{wa_url}" target="_blank" class="box-btn">Ordina su WhatsApp &rarr;</a>'
            f'</div>'
        )
        if i % 2 == 0:
            left_prev += card
        else:
            right_prev += card

    st.markdown(f"""
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:2px;background:rgba(181,135,58,0.15);padding:0 80px 0;">
        <div>{left_prev}</div>
        <div>{right_prev}</div>
    </div>
    <div style="padding:32px 80px;background:#F9F5EE;text-align:center;">
        <a href="/?page=catalogo" target="_self"
           style="font-family:'DM Sans',sans-serif;font-size:14px;font-weight:600;color:#1B4332;
                  text-decoration:none;border-bottom:2px solid #B5873A;padding-bottom:3px;">
            &rarr; Vedi tutte le 10 box del catalogo
        </a>
    </div>
    """, unsafe_allow_html=True)

    # How it works mini
    st.markdown(f"""
    <div class="section section-dark">
        <div class="section-label" style="color: rgba(181,135,58,0.8);">Come funziona</div>
        <h2 class="section-h2 light">Tre passi verso Roma</h2>
        <div class="steps-grid">
            <div class="step-item">
                <div class="step-num">01</div>
                <span class="step-icon">📋</span>
                <div class="step-title">Scegli la box</div>
                <div class="step-text">Sfoglia il catalogo e scegli il tuo momento romano — colazione, pranzo, cena o dolce.</div>
            </div>
            <div class="step-item">
                <div class="step-num">02</div>
                <span class="step-icon">📱</span>
                <div class="step-title">Ordina su WhatsApp</div>
                <div class="step-text">Premi il bottone — il messaggio è già precompilato. Aggiungi solo l'indirizzo.</div>
            </div>
            <div class="step-item">
                <div class="step-num">03</div>
                <span class="step-icon">📅</span>
                <div class="step-title">Confermiamo</div>
                <div class="step-text">Ti rispondiamo entro 30 minuti. Scegli la fascia oraria: mattina 9-12 o pomeriggio 15-18.</div>
            </div>
            <div class="step-item" style="padding-right: 0;">
                <div class="step-num">04</div>
                <span class="step-icon">🎁</span>
                <div class="step-title">Ricevi la tua box</div>
                <div class="step-text">Entro 48 ore — prodotti artigianali, scheda ricetta dello chef, vino laziale abbinato.</div>
            </div>
        </div>
        <div style="margin-top: 40px; text-align: center;">
            <a href="{wa_general}" target="_blank" class="btn-primary" style="display: inline-block;">Ordina ora →</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Chef section
    if BOX_B64:
        st.markdown(f"""
        <div class="section">
            <div class="chef-grid">
                <div class="chef-text">
                    <div class="section-label">Chi seleziona</div>
                    <h2 class="section-h2">La filosofia FORVM</h2>
                    <p>FORVM nasce da un'ossessione: trovare i migliori prodotti del Lazio — non i più famosi, i migliori. Guanciale di chi alleva i maiali nei monti di Amatrice. Pecorino Romano stagionato in grotte naturali dei Castelli. Rigatoni trafilati al bronzo in piccoli pastifici di famiglia.</p>
                    <div class="chef-quote">"Non vendo prodotti laziali. Racconto il territorio romano attraverso ogni ingrediente."</div>
                    <p>Ogni stagione la selezione viene aggiornata con l'arrivo dei migliori prodotti frescos. Non troverai mai lo stesso catalogo per 12 mesi.</p>
                    <a href="{wa_general}" target="_blank" class="btn-primary" style="display: inline-block; margin-top: 8px;">Ordina su WhatsApp →</a>
                </div>
                <div class="chef-img-wrap">
                    <img src="data:image/jpeg;base64,{BOX_B64}" alt="Box FORVM" style="border-radius: 2px;" />
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════
# PAGE: CATALOGO
# ══════════════════════════════════════════════════════════════════
elif current_page == "catalogo":
    st.markdown("""
    <div class="section section-alt" style="padding-bottom: 32px;">
        <div class="section-label">Catalogo Completo</div>
        <h2 class="section-h2">Le Box FORVM — A Tavola con Roma</h2>
        <p class="section-sub">Scegli il tuo momento romano. Ordina su WhatsApp. Consegniamo entro 48 ore.</p>
    </div>
    """, unsafe_allow_html=True)

    # Person selector
    st.markdown("<div style='padding: 0 80px; background: #F9F5EE;'><div class='person-selector'><span class='person-selector-label'>👥 Per quante persone?</span></div></div>", unsafe_allow_html=True)

    cols_p = st.columns([1,1,1,1,1,8])
    for n in range(1, 6):
        with cols_p[n-1]:
            label = f"{'✓ ' if st.session_state.persons == n else ''}{n} pers."
            if st.button(label, key=f"p_{n}", use_container_width=True):
                st.session_state.persons = n
                st.rerun()

    persons = st.session_state.persons

    # All boxes grid
    st.markdown("<div style='padding: 32px 80px 0; background: #F9F5EE;'>", unsafe_allow_html=True)

    left_html = ""
    right_html = ""

    for i, box in enumerate(BOXES):
        vino_badge = f'<div class="box-vino">&#127863; Vino laziale incluso &mdash; {box["vino"]}</div>' if box["vino"] else ""

        stage_cls = "stagione-estate" if "Estate" in box["stagione"] else (
            "stagione-stagionale" if "Stagionale" in box["stagione"] else (
                "stagione-premium" if box.get("premium") else "stagione-tutto"
            )
        )

        wa_url = get_whatsapp_url(box["name"], persons)
        btn_cls = "box-btn gold" if box.get("premium") else "box-btn"

        # Ingredienti a tendina con details/summary HTML
        ing_items = "".join(f"<li>{ing}</li>" for ing in box["ingredienti"])
        ingredienti_block = (
            f'<details class="ing-details">'
            f'<summary class="ing-summary">&#9660; Vedi ingredienti kit</summary>'
            f'<ul class="ing-list">{ing_items}</ul>'
            f'</details>'
        )

        # Calcolo prezzo dinamico totale strutturato
        price_block = get_box_price_block(box, persons)

        emoji_safe = box["emoji"]
        card = (
            f'<div class="box-card" id="{box["id"]}">'
            f'<div class="box-header">'
            f'<div>'
            f'<div class="box-number">Box {str(i+1).zfill(2)}</div>'
            f'<div class="box-name">{box["name"]}</div>'
            f'<div style="font-family:DM Sans,sans-serif;font-size:13px;color:#888;margin-top:3px;font-style:italic;">{box["tagline"]}</div>'
            f'</div>'
            f'<span class="box-emoji">{emoji_safe}</span>'
            f'</div>'
            f'<span class="box-stagione {stage_cls}">{box["stagione"]}</span>'
            f'<p class="box-desc">{box["desc"]}</p>'
            f'{vino_badge}'
            f'{ingredienti_block}'
            f'{price_block}'
            f'<a href="{wa_url}" target="_blank" class="{btn_cls}">Ordina su WhatsApp &rarr;</a>'
            f'</div>'
        )

        if i % 2 == 0:
            left_html += card
        else:
            right_html += card

    st.markdown(f"""
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:2px;background:rgba(181,135,58,0.15);padding:0 80px 80px;">
        <div>{left_html}</div>
        <div>{right_html}</div>
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════
# PAGE: COME FUNZIONA
# ══════════════════════════════════════════════════════════════════
elif current_page == "come_funziona":
    st.markdown(f"""
    <div class="section section-dark" style="min-height: 50vh;">
        <div class="section-label" style="color: rgba(181,135,58,0.8);">Il processo</div>
        <h2 class="section-h2 light">Come funziona FORVM</h2>
        <p class="section-sub light">Quattro passi — dall'ordine al tuo tavolo romano.</p>
        <div class="steps-grid">
            <div class="step-item">
                <div class="step-num">01</div>
                <span class="step-icon">📋</span>
                <div class="step-title">Scegli la box</div>
                <div class="step-text">Sfoglia il catalogo e scegli la box per il tuo momento romano — colazione, pranzo, cena, aperitivo o dolce.</div>
            </div>
            <div class="step-item">
                <div class="step-num">02</div>
                <span class="step-icon">📱</span>
                <div class="step-title">Ordina su WhatsApp</div>
                <div class="step-text">Premi il bottone WhatsApp — trovi già il messaggio precompilato con la box scelta. Aggiungi solo il tuo indirizzo.</div>
            </div>
            <div class="step-item">
                <div class="step-num">03</div>
                <span class="step-icon">📅</span>
                <div class="step-title">Confermiamo la consegna</div>
                <div class="step-text">Ti rispondiamo entro 30 minuti. Scegli la fascia oraria — mattina 9-12 o pomeriggio 15-18. Se hai una safe box consegniamo direttamente lì.</div>
            </div>
            <div class="step-item" style="padding-right: 0;">
                <div class="step-num">04</div>
                <span class="step-icon">🎁</span>
                <div class="step-title">Ricevi la tua box</div>
                <div class="step-text">La tua box FORVM arriva entro 48 ore — prodotti artigianali, scheda ricetta dello chef, vino laziale abbinato. Apri e inizia.</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Info boxes
    st.markdown("""
    <div class="section" style="background: #F9F5EE;">
        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 24px; margin-bottom: 56px;">
            <div style="background: white; padding: 28px; border-left: 3px solid #B5873A;">
                <div style="font-size: 24px; margin-bottom: 8px;">💳</div>
                <div style="font-family: 'Cormorant Garamond', serif; font-size: 20px; font-weight: 600; color: #1B4332; margin-bottom: 8px;">Come si paga</div>
                <div style="font-family: 'DM Sans', sans-serif; font-size: 14px; color: #5a5a5a; line-height: 1.65;">Satispay o PayPal prima della consegna. Pagamento anticipato obbligatorio.</div>
            </div>
            <div style="background: white; padding: 28px; border-left: 3px solid #B5873A;">
                <div style="font-size: 24px; margin-bottom: 8px;">🌍</div>
                <div style="font-family: 'Cormorant Garamond', serif; font-size: 20px; font-weight: 600; color: #1B4332; margin-bottom: 8px;">Parliamo la tua lingua</div>
                <div style="font-family: 'DM Sans', sans-serif; font-size: 14px; color: #5a5a5a; line-height: 1.65;">Gestiamo le comunicazioni in italiano e inglese. Non serve parlare italiano per ordinare.</div>
            </div>
            <div style="background: white; padding: 28px; border-left: 3px solid #25D366;">
                <div style="font-size: 24px; margin-bottom: 8px;">⚡</div>
                <div style="font-family: 'Cormorant Garamond', serif; font-size: 20px; font-weight: 600; color: #1B4332; margin-bottom: 8px;">Garanzia rimborso</div>
                <div style="font-family: 'DM Sans', sans-serif; font-size: 14px; color: #5a5a5a; line-height: 1.65;">Se qualcosa non va — rimborso immediato senza discussioni. Scrivici su WhatsApp.</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # FAQ
    st.markdown("""
        <div class="section-label">Domande frequenti</div>
        <h2 class="section-h2">FAQ</h2>
    """, unsafe_allow_html=True)

    faqs = [
        ("Devo essere in casa quando consegnate?", "Sì, se non hai una safe box. Ti chiediamo una fascia oraria di 2 ore — la sera prima ti confermiamo con un messaggio WhatsApp."),
        ("Qual è il tempo minimo di preavviso?", "24 ore. Per consegne urgenti scrivici su WhatsApp e vediamo cosa possiamo fare — a volte riusciamo ad accelerare."),
        ("Posso ordinare più box insieme?", "Sì — una sola consegna per tutti gli ordini dello stesso giorno."),
        ("Posso ordinare se non parlo italiano?", "Sì. Gestiamo le comunicazioni in italiano e inglese."),
        ("Come pago?", "Satispay o PayPal prima della consegna. Pagamento anticipato obbligatorio."),
        ("Cosa succede se qualcosa non va?", "Rimborso immediato senza discussioni. Scrivici su WhatsApp — è il nostro canale diretto per tutto."),
    ]

    for q, a in faqs:
        st.markdown(f"""
        <div class="faq-item">
            <div class="faq-q">❓ {q}</div>
            <div class="faq-a">{a}</div>
        </div>
        """, unsafe_allow_html=True)

    wa_url = f"https://wa.me/{WHATSAPP_NUMBER}?text=Ciao%20FORVM!%20Ho%20una%20domanda%20prima%20di%20ordinare."
    st.markdown(f"""
        <div style="margin-top: 48px; text-align: center;">
            <a href="{wa_url}" target="_blank" class="btn-primary" style="display: inline-block;">Parla con lo chef →</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════
# PAGE: CHI SIAMO
# ══════════════════════════════════════════════════════════════════
elif current_page == "chi_siamo":
    wa_url = f"https://wa.me/{WHATSAPP_NUMBER}?text=Ciao%20FORVM!%20%F0%9F%9B%8F%EF%B8%8F%20Vorrei%20ordinare%20una%20box%20laziale."
    st.markdown(f"""
    <div class="section">
        <div class="section-label">Chi seleziona</div>
        <h2 class="section-h2">La persona dietro FORVM</h2>
        <div class="chef-grid">
            <div class="chef-text">
                <p>FORVM nasce da un'ossessione professionale: trovare i prodotti laziali davvero eccezionali. Non i più famosi o i più promossi — i migliori, quelli che meritano di essere portati sulla tavola di chi visita Roma per la prima volta o per la centesima.</p>
                <div class="chef-quote">"Il Forum Romano era il mercato di Roma. 2000 anni fa, tutto il Lazio confluiva lì. FORVM riporta quel concetto nel 2026 — il meglio del territorio laziale, consegnato dove sei."</div>
                <p>Ogni prodotto nella nostra selezione è scelto personalmente — visitando i produttori nei Castelli Romani, nei monti di Amatrice, nelle colline della Ciociaria. Non utilizziamo grossisti o cataloghi generici.</p>
                <p>La selezione cambia ogni stagione, seguendo i ritmi del territorio. L'estate porta la Caprese Laziale con i pomodori di Fondi. L'autunno porta i funghi porcini dei Simbruini. Il Natale porta i vini passiti dei Colli Lanuvini.</p>
                <a href="{wa_url}" target="_blank" class="btn-primary" style="display: inline-block; margin-top: 8px;">Ordina su WhatsApp →</a>
            </div>
            <div class="chef-img-wrap">
    """, unsafe_allow_html=True)

    if BOX_B64:
        st.markdown(f'<img src="data:image/jpeg;base64,{BOX_B64}" alt="Box FORVM" />', unsafe_allow_html=True)

    st.markdown("""
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Produttori section
    st.markdown("""
    <div class="section section-alt">
        <div class="section-label">I nostri produttori</div>
        <h2 class="section-h2">Le radici del territorio</h2>
        <p class="section-sub">Non selezioniamo brand — selezioniamo persone. Questi sono alcuni dei produttori con cui lavoriamo.</p>
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 2px; background: rgba(181,135,58,0.15); margin-top: 40px;">
    """, unsafe_allow_html=True)

    produttori = [
        ("🥩", "Norcineria Jacovone", "Amatrice (RI)", "Guanciale, salumi stagionati"),
        ("🧀", "Caseificio Bernardi", "Castelli Romani (RM)", "Pecorino Romano DOP, ricotta"),
        ("🍷", "Cantina Casale del Giglio", "Aprilia (LT)", "Vini laziali DOCG e DOC"),
        ("🫒", "Oleificio Colli Sabini", "Sabina (RI)", "Olio EVO DOP, olive da mensa"),
    ]

    for icon, name, place, prod in produttori:
        st.markdown(f"""
        <div style="background: white; padding: 28px; text-align: center;">
            <div style="font-size: 36px; margin-bottom: 12px;">{icon}</div>
            <div style="font-family: 'Cormorant Garamond', serif; font-size: 20px; font-weight: 600; color: #1B4332; margin-bottom: 4px;">{name}</div>
            <div style="font-family: 'DM Sans', sans-serif; font-size: 12px; font-weight: 600; letter-spacing: 1px; color: #B5873A; text-transform: uppercase; margin-bottom: 8px;">{place}</div>
            <div style="font-family: 'DM Sans', sans-serif; font-size: 13px; color: #777; line-height: 1.5;">{prod}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div></div>", unsafe_allow_html=True)

    # Chef stagionale
    st.markdown("""
    <div class="section section-dark">
        <div class="section-label" style="color: rgba(181,135,58,0.8);">Chef stagionale</div>
        <h2 class="section-h2 light">La selezione di questa stagione</h2>
        <div style="display: flex; align-items: flex-start; gap: 48px; margin-top: 32px;">
            <div style="flex: 1;">
                <div style="font-family: 'Cormorant Garamond', serif; font-size: 26px; font-weight: 600; color: #F9F5EE; margin-bottom: 4px;">Estate 2026</div>
                <div style="font-family: 'DM Sans', sans-serif; font-size: 14px; color: rgba(249,245,238,0.6); font-style: italic; margin-bottom: 20px;">Selezione in aggiornamento — il nome dello chef verrà comunicato presto</div>
                <p style="font-family: 'DM Sans', sans-serif; font-size: 15px; font-weight: 300; line-height: 1.75; color: rgba(249,245,238,0.75);">Ogni stagione FORVM collabora con uno chef laziale per aggiornare la selezione con i prodotti freschi del momento. L'estate 2026 porta nuovi produttori della costa laziale e delle colline pontine.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════
# PAGE: PARTNERSHIP HOST
# ══════════════════════════════════════════════════════════════════
elif current_page == "partner":
    wa_host = f"https://wa.me/{WHATSAPP_NUMBER}?text=Ciao%20FORVM!%20Sono%20un%20host%20Airbnb%20e%20vorrei%20diventare%20partner.%20Possiamo%20parlarne%3F"

    st.markdown(f"""
    <div class="hero-section" style="min-height: 50vh;">
        <div class="hero-pattern"></div>
        <div class="hero-content">
            <div class="hero-eyebrow">Per gli host Airbnb</div>
            <h1 class="hero-h1">Porta Roma sulla tavola<br>dei tuoi ospiti.<br><em>Guadagni senza fare nulla.</em></h1>
            <p class="hero-subtitle">Commissione automatica del 10% su ogni ordine generato dai tuoi ospiti. Zero gestione da parte tua.</p>
            <div class="hero-ctas">
                <a href="{wa_host}" target="_blank" class="btn-primary">Diventa partner →</a>
                <a href="mailto:info@forvm.roma" class="btn-whatsapp">
                    <span class="wa-dot" style="color: #B5873A;">●</span> Scrivi a info@forvm.roma
                </a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Benefits
    st.markdown("""
    <div class="section section-alt" style="padding-bottom: 0;">
        <div class="section-label">Perché conviene</div>
        <h2 class="section-h2">Tre buone ragioni</h2>
        <div class="partner-benefits">
            <div class="partner-benefit">
                <span class="partner-benefit-icon">💰</span>
                <div class="partner-benefit-title">Commissione 10%</div>
                <div class="partner-benefit-text">Ogni volta che un tuo ospite ordina, ricevi il 10% automaticamente. Su una Carbonara da €28, guadagni €2.80 senza fare nulla.</div>
            </div>
            <div class="partner-benefit">
                <span class="partner-benefit-icon">🛋️</span>
                <div class="partner-benefit-title">Zero gestione</div>
                <div class="partner-benefit-text">Tu metti il biglietto nell'appartamento. Noi facciamo tutto il resto — ordini, pagamenti, consegne, problemi.</div>
            </div>
            <div class="partner-benefit">
                <span class="partner-benefit-icon">⭐</span>
                <div class="partner-benefit-title">Ospiti più soddisfatti</div>
                <div class="partner-benefit-text">Un ospite che cucina la Carbonara con i prodotti giusti parla bene dell'appartamento. La tua recensione cresce.</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # How it works for hosts
    st.markdown("""
    <div class="section">
        <div class="section-label">Come funziona</div>
        <h2 class="section-h2">Quattro passi per l'host</h2>
        <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; margin-top: 40px;">
    """, unsafe_allow_html=True)

    host_steps = [
        ("📞", "Ti contatti con noi", "Scrivici su WhatsApp o via email — parliamo del tuo appartamento e del tipo di ospiti che ricevi."),
        ("🃏", "Ricevi il biglietto", "Ti mandiamo il biglietto fisico FORVM da lasciare in appartamento — con QR code e link personalizzato."),
        ("📦", "I tuoi ospiti ordinano", "L'ospite scansiona il QR, visita il sito, sceglie la box. Ordina su WhatsApp — tu non tocchi nulla."),
        ("💶", "Ricevi la commissione", "A fine mese ti inviamo il riepilogo degli ordini e la tua commissione del 10%."),
    ]

    for icon, title, text in host_steps:
        st.markdown(f"""
        <div style="background: #F9F5EE; padding: 28px; border-left: 3px solid rgba(181,135,58,0.4);">
            <div style="font-size: 28px; margin-bottom: 12px;">{icon}</div>
            <div style="font-family: 'Cormorant Garamond', serif; font-size: 20px; font-weight: 600; color: #1B4332; margin-bottom: 8px;">{title}</div>
            <div style="font-family: 'DM Sans', sans-serif; font-size: 14px; color: #5a5a5a; line-height: 1.65;">{text}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div></div>", unsafe_allow_html=True)

    # Commission table
    st.markdown("""
    <div class="section section-alt">
        <div class="section-label">Commissioni</div>
        <h2 class="section-h2">Quanto guadagni</h2>
        <p class="section-sub">10% su ogni ordine generato dai tuoi ospiti — calcolato automaticamente.</p>
        <div style="margin-top: 32px; overflow-x: auto;">
        <table style="width: 100%; border-collapse: collapse; font-family: 'DM Sans', sans-serif; font-size: 14px;">
            <thead>
                <tr style="background: #1B4332; color: #F9F5EE;">
                    <th style="padding: 14px 20px; text-align: left; font-weight: 500;">Box</th>
                    <th style="padding: 14px 20px; text-align: center;">1 persona</th>
                    <th style="padding: 14px 20px; text-align: center;">2 persone</th>
                    <th style="padding: 14px 20px; text-align: center;">3 persone</th>
                    <th style="padding: 14px 20px; text-align: center; color: #B5873A; font-weight: 600;">Tua commissione (2p)</th>
                </tr>
            </thead>
            <tbody>
    """, unsafe_allow_html=True)

    for i, box in enumerate(BOXES[:9]):
        bg = "#fff" if i % 2 == 0 else "#f8f5f0"
        p1 = f"€ {box['prezzi'].get(1, '—')}"
        p2 = f"€ {box['prezzi'].get(2, '—')}"
        p3 = f"€ {box['prezzi'].get(3, '—')}"
        comm = box['prezzi'].get(2, 0)
        comm_str = f"<span style='color: #25D366; font-weight: 600;'>€ {comm * 0.1:.1f}</span>" if comm else "—"
        st.markdown(f"""
        <tr style="background: {bg}; border-bottom: 1px solid rgba(181,135,58,0.1);">
            <td style="padding: 12px 20px; font-weight: 500; color: #1B4332;">{box['emoji']} {box['name']}</td>
            <td style="padding: 12px 20px; text-align: center; color: #4a4a4a;">{p1}</td>
            <td style="padding: 12px 20px; text-align: center; color: #4a4a4a;">{p2}</td>
            <td style="padding: 12px 20px; text-align: center; color: #4a4a4a;">{p3}</td>
            <td style="padding: 12px 20px; text-align: center;">{comm_str}</td>
        </tr>
        """, unsafe_allow_html=True)

    st.markdown(f"""
            </tbody>
        </table>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Contact form
    st.markdown("""
    <div class="section section-dark">
        <div class="section-label" style="color: rgba(181,135,58,0.8);">Inizia ora</div>
        <h2 class="section-h2 light">Diventare partner è semplice</h2>
        <p class="section-sub light">Compila il form oppure scrivici direttamente su WhatsApp — ti rispondiamo entro un'ora.</p>
    </div>
    """, unsafe_allow_html=True)

    with st.form("partner_form", clear_on_submit=True):
        col_a, col_b = st.columns(2)
        with col_a:
            nome = st.text_input("Nome e Cognome *")
            whatsapp_num = st.text_input("WhatsApp *")
        with col_b:
            n_app = st.number_input("N° di appartamenti", min_value=1, max_value=50, value=1)
            zona = st.text_input("Zona di Roma")
        messaggio = st.text_area("Messaggio (opzionale)", height=80)
        submitted = st.form_submit_button("Invia richiesta di partnership →", use_container_width=True)
        if submitted:
            if nome and whatsapp_num:
                st.success(f"✅ Grazie {nome}! Ti contatteremo al numero {whatsapp_num} entro 24 ore.")
            else:
                st.error("Inserisci nome e WhatsApp per continuare.")

    st.markdown(f"""
    <div class="section" style="text-align: center; padding-top: 32px;">
        <p style="font-family: 'DM Sans', sans-serif; font-size: 16px; color: #5a5a5a; margin-bottom: 20px;">Preferisci scrivere direttamente?</p>
        <a href="{wa_host}" target="_blank" class="btn-primary" style="display: inline-block;">📱 Scrivimi su WhatsApp →</a>
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════
# FOOTER (all pages)
# ══════════════════════════════════════════════════════════════════
wa_footer = f"https://wa.me/{WHATSAPP_NUMBER}?text=Ciao%20FORVM!%20%F0%9F%9B%8F%EF%B8%8F%20Vorrei%20ordinare%20una%20box%20laziale%20%E2%80%94%20potete%20aiutarmi%3F"

st.markdown(f"""
<footer class="forvm-footer">
    <div class="footer-top">
        <div>
            <div class="footer-logo">FORVM</div>
            <div class="footer-tagline">Il mercato di Roma. 2000 anni dopo.<br>Prodotti laziali artigianali selezionati dallo chef,<br>consegnati nel tuo appartamento entro 48 ore.</div>
        </div>
        <div>
            <div class="footer-col-title">Pagine</div>
            <div class="footer-links">
                <a href="/?page=home" target="_self">Home</a>
                <a href="/?page=catalogo" target="_self">Catalogo Box</a>
                <a href="/?page=come_funziona" target="_self">Come Funziona</a>
                <a href="/?page=chi_siamo" target="_self">Chi Siamo</a>
                <a href="/?page=partner" target="_self">Partnership Host</a>
            </div>
        </div>
        <div>
            <div class="footer-col-title">Contatti</div>
            <div class="footer-links">
                <a href="{wa_footer}" target="_blank">📱 WhatsApp</a>
                <a href="https://instagram.com/forvm.roma" target="_blank">📸 @forvm.roma</a>
                <a href="mailto:info@forvm.roma">✉️ info@forvm.roma</a>
                <a href="#">Privacy Policy</a>
                <a href="#">Cookie Policy</a>
            </div>
        </div>
    </div>
    <div class="footer-bottom">
        <div class="footer-copy">© 2026 FORVM · P.IVA [in aggiornamento] · forvm.roma</div>
        <div class="footer-copy">Selezionato dallo chef · Consegnato a casa tua · Roma</div>
    </div>
</footer>

<a href="{wa_footer}" target="_blank" class="wa-float">
    <span class="wa-icon">💬</span>
    <span>Ordina ora</span>
</a>
""", unsafe_allow_html=True)