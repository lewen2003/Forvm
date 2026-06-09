import streamlit as st
import urllib.parse

# ─── CONFIGURAZIONE DELLA PAGINA ────────────────────────────────────
st.set_page_config(
    page_title="FORVM — Prodotti Laziali Artigianali · Consegna 48h Roma",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Numero WhatsApp ufficiale del servizio clienti
WHATSAPP_NUMBER = "393000000000"  # Sostituisci con il tuo numero reale se necessario

# ─── DATASET COMPLETO DELLE 10 BOX ──────────────────────────────────
BOXES = [
    {
        "id": "colazione",
        "name": "La Colazione Romana",
        "emoji": "☕",
        "tagline": "Il risveglio autentico della capitale",
        "desc": "Cornetti artigianali, maritozzo con panna freschissima, caffè di torrefazione storica e marmellata locale selezionata.",
        "ingredienti": ["Cornetti artigianali (x2 a persona)", "Maritozzo con panna montata fresca", "Caffè Torrefazione Sant'Eustachio", "Marmellata di agrumi laziali", "Succo di arancia rossa"],
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
        "desc": "Guanciale DOP di Amatrice, Pecorino Romano DOP, rigatoni trafilati al bronzo, uova fresche laziali e pepe nero Tellicherry.",
        "ingredienti": ["Guanciale DOP di Amatrice (100g a persona)", "Pecorino Romano DOP (80g a persona)", "Rigatoni trafilati al bronzo (100g a persona)", "Uova fresche da allevamento laziale", "Pepe nero Tellicherry macinato fresco", "🍷 Frascati DOCG (75cl) incluso"],
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
        "desc": "Guanciale stagionato, pomodori San Marzano DOP, Pecorino della Sabina e bucatini artigianali laziali.",
        "ingredienti": ["Guanciale stagionato di Amatrice (100g a persona)", "Pomodori San Marzano DOP (200g a persona)", "Pecorino Romano DOP (60g a persona)", "Bucatini artigianali (100g a persona)", "🍷 Cesanese DOCG (75cl) incluso"],
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
        "desc": "Pecorino Romano stagionato 24 mesi, pepe nero intero e spaghetti alla chitarra artigianali.",
        "ingredienti": ["Pecorino Romano stagionato 24 mesi (120g a persona)", "Pepe nero Tellicherry in grani", "Spaghetti alla chitarra artigianali (100g a persona)", "🍷 Frascati DOC (75cl) incluso"],
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
        "desc": "Guanciale artigianale, Pecorino Romano DOP e rigatoni di semola dura di piccoli pastifici della provincia di Roma.",
        "ingredienti": ["Guanciale artigianale laziale (110g a persona)", "Pecorino Romano DOP (80g a persona)", "Rigatoni di semola dura laziale (100g a persona)", "🍷 Marino DOC (75cl) incluso"],
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
        "desc": "Pollo ruspante laziale a pezzi, peperoni cornetti dolci rossi e gialli, aglio di Cori e aromi dell'orto.",
        "ingredienti": ["Pollo ruspante del Lazio (300g a persona)", "Peperoni cornetti rossi e gialli locali", "Aglio di Cori e olio EVO Sabina", "Vino bianco laziale per sfumare", "🍷 Frascati DOCG (75cl) incluso"],
        "prezzi": {1: 18, 2: 28, 3: 38},
        "stagione": "Estate · Giu-Set",
        "vino": "Frascati DOCG",
        "badge_color": "#4A7C59",
    },
    {
        "id": "caprese",
        "name": "La Caprese Laziale",
        "emoji": "🌿",
        "tagline": "Freschezza dei Castelli Romani",
        "desc": "Mozzarella di bufala DOP dell'Agro Pontino, pomodori cuore di bue laziali, basilico fresco e olio EVO.",
        "ingredienti": ["Mozzarella di bufala DOP (150g a persona)", "Pomodori cuore di bue laziali (200g a persona)", "Basilico fresco profumato", "Olio EVO dei Colli Sabini DOP", "Sale marino di Cervia"],
        "prezzi": {1: 16, 2: 24, 3: 32},
        "stagione": "Stagionale · Giu-Set",
        "vino": None,
        "badge_color": "#4A7C59",
    },
    {
        "id": "cantina",
        "name": "La Cantina Laziale",
        "emoji": "🍷",
        "tagline": "Un viaggio tra i vigneti del Lazio",
        "desc": "Selezione guidata di due bottiglie DOCG laziali d'eccellenza accompagnate da un tagliere ricco di salumi e formaggi.",
        "ingredienti": ["Frascati Superiore DOCG (75cl)", "Cesanese del Piglio DOCG (75cl)", "Pecorino Romano DOP (80g a persona)", "Guanciale stagionato a fette", "Olive di Gaeta DOP", "Pane artigianale di Lariano"],
        "prezzi": {2: 38, 3: 48, 4: 58},
        "stagione": "Tutto l'anno",
        "vino": "2 Vini DOCG inclusi",
        "badge_color": "#6B2D8B",
    },
    {
        "id": "dolci",
        "name": "I Dolci Romani",
        "emoji": "🍮",
        "tagline": "Il finale perfetto per la serata",
        "desc": "Tiramisù artigianale fatto in giornata, crostata di visciole della tradizione e biscotteria secca laziale.",
        "ingredienti": ["Tiramisù artigianale monoporzione", "Crostata di visciole locale (100g a persona)", "Biscotti artigianali della Sabina", "🍷 Cannellino di Frascati DOCG (37.5cl) incluso"],
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
        "desc": "Un'esperienza di lusso privato: lo chef viene direttamente nel tuo appartamento e cucina un menu romano completo di 4 portate.",
        "ingredienti": ["Menu interamente personalizzato", "Tutti gli ingredienti freschi inclusi", "Servizio a tavola e mise en place", "Abbinamento vini laziali della cantina FORVM"],
        "prezzi": {},
        "stagione": "Tutto l'anno",
        "vino": "Abbinamento incluso",
        "badge_color": "#1B4332",
        "premium": True,
    },
]

# Funzione per generare il link WhatsApp pulito senza conflitti di encoding
def get_whatsapp_url(box_name, n_persons):
    if box_name == "Chef a Domicilio":
        msg = f"Ciao FORVM! 🏛️ Vorrei richiedere informazioni per il servizio Chef a Domicilio per {n_persons} persone."
    else:
        msg = f"Ciao FORVM! 🏛️ Vorrei ordinare la box '{box_name}' per {n_persons} persone. Quali sono i prossimi passi per la consegna a Roma?"
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={urllib.parse.quote(msg)}"

# ─── STILI CSS PREMIUM COMPLETI ──────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;0,700;1,400;1,600&family=DM+Sans:wght@300;400;500;600&display=swap');

*, *::before, *::after { box-sizing: border-box; }

.main .block-container {
    padding: 0 !important;
    max-width: 100% !important;
}

#MainMenu, footer, header { visibility: hidden; }
.stDeployButton { display: none; }
[data-testid="stSidebar"] { display: none; }
[data-testid="collapsedControl"] { display: none; }

body { font-family: 'DM Sans', sans-serif; background-color: #F9F5EE; }
h1, h2, h3 { font-family: 'Cormorant Garamond', serif; }

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
}
.forvm-nav-links {
    display: flex;
    gap: 32px;
}
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
}

.hero-section {
    position: relative;
    width: 100%;
    min-height: 60vh;
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
    font-size: 280px;
    line-height: 1;
    color: #B5873A;
    pointer-events: none;
    font-family: 'Cormorant Garamond', serif;
}
.hero-content {
    position: relative;
    z-index: 2;
    padding: 60px 80px;
    max-width: 750px;
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
    font-size: clamp(42px, 5vw, 72px);
    font-weight: 600;
    line-height: 1.1;
    color: #F9F5EE;
    margin: 0;
}
.hero-h1 em { font-style: italic; color: #B5873A; }
.hero-subtitle {
    font-family: 'DM Sans', sans-serif;
    font-size: 17px;
    font-weight: 300;
    line-height: 1.7;
    color: rgba(249,245,238,0.8);
    margin: 20px 0 0 0;
}

.section { padding: 60px 80px; width: 100%; }
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
    font-size: clamp(32px, 4vw, 48px);
    font-weight: 600;
    line-height: 1.15;
    color: #1B4332;
    margin: 0 0 16px;
}
.section-h2.light { color: #F9F5EE; }
.section-sub {
    font-family: 'DM Sans', sans-serif;
    font-size: 16px;
    font-weight: 300;
    line-height: 1.7;
    color: #4a4a4a;
    max-width: 600px;
}
.section-sub.light { color: rgba(249,245,238,0.75); }

.values-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    border-top: 1px solid rgba(181,135,58,0.25);
    border-left: 1px solid rgba(181,135,58,0.25);
    margin-top: 32px;
}
.value-card {
    padding: 40px 36px;
    border-right: 1px solid rgba(181,135,58,0.25);
    border-bottom: 1px solid rgba(181,135,58,0.25);
    background: #F9F5EE;
}
.value-icon { font-size: 32px; margin-bottom: 16px; display: block; }
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

.boxes-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; }
.box-card { background: #fff; padding: 36px; display: flex; flex-direction: column; border-radius: 4px; box-shadow: 0 4px 15px rgba(0,0,0,0.03); }
.box-number {
    font-family: 'DM Sans', sans-serif;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 2px;
    color: #B5873A;
    margin-bottom: 10px;
    text-transform: uppercase;
}
.box-header { display: flex; align-items: flex-start; justify-content: space-between; margin-bottom: 8px; }
.box-name { font-family: 'Cormorant Garamond', serif; font-size: 26px; font-weight: 600; color: #1B4332; }
.box-emoji { font-size: 28px; }
.box-stagione { display: inline-block; font-family: 'DM Sans', sans-serif; font-size: 11px; font-weight: 500; letter-spacing: 1px; padding: 3px 10px; border-radius: 2px; margin-bottom: 12px; max-width: fit-content; }
.stagione-estate { background: #fff3cd; color: #856404; }
.stagione-tutto { background: rgba(27,67,50,0.08); color: #1B4332; }
.stagione-premium { background: #1B4332; color: #B5873A; }

.box-desc { font-family: 'DM Sans', sans-serif; font-size: 14px; font-weight: 300; line-height: 1.65; color: #5a5a5a; margin-bottom: 16px; flex: 1; }
.box-vino { font-family: 'DM Sans', sans-serif; font-size: 12px; font-weight: 500; color: #6B2D8B; margin-bottom: 12px; }
.box-price { font-family: 'Cormorant Garamond', serif; font-size: 28px; font-weight: 600; color: #1B4332; margin-bottom: 4px; }
.box-price span { font-size: 14px; font-weight: 400; color: #888; font-family: 'DM Sans', sans-serif; }
.box-price-na { font-family: 'DM Sans', sans-serif; font-size: 14px; font-weight: 400; color: #B5873A; font-style: italic; margin-bottom: 4px; }
.box-btn { display: inline-block; width: 100%; text-align: center; background: #1B4332; color: #F9F5EE; font-family: 'DM Sans', sans-serif; font-size: 13px; font-weight: 600; letter-spacing: 1px; text-transform: uppercase; padding: 14px 20px; text-decoration: none; margin-top: 16px; border: 2px solid #1B4332; border-radius: 4px; transition: all 0.2s; }
.box-btn:hover { background: #2d5a44; border-color: #2d5a44; }
.box-btn.gold { background: #B5873A; border-color: #B5873A; color: white; }
.box-btn.gold:hover { background: #a47629; border-color: #a47629; }

.steps-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; margin-top: 48px; }
.step-item { padding: 0 10px 0 0; position: relative; }
.step-num { font-family: 'Cormorant Garamond', serif; font-size: 56px; font-weight: 400; color: #B5873A; line-height: 1; margin-bottom: 8px; }
.step-icon { font-size: 28px; margin-bottom: 12px; display: block; }
.step-title { font-family: 'Cormorant Garamond', serif; font-size: 22px; font-weight: 600; color: #F9F5EE; margin-bottom: 8px; }
.step-text { font-family: 'DM Sans', sans-serif; font-size: 14px; font-weight: 300; line-height: 1.65; color: rgba(249,245,238,0.7); }

.chef-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 40px; align-items: center; margin-top: 32px; }
.chef-text p { font-family: 'DM Sans', sans-serif; font-size: 16px; font-weight: 300; line-height: 1.8; color: #4a4a4a; margin-bottom: 20px; }
.chef-quote { font-family: 'Cormorant Garamond', serif; font-size: 24px; font-style: italic; color: #1B4332; border-left: 3px solid #B5873A; padding-left: 20px; margin: 28px 0; }

.partner-benefits { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin: 32px 0; }
.partner-benefit { background: white; padding: 36px; text-align: center; border-radius: 4px; box-shadow: 0 4px 15px rgba(0,0,0,0.02); }
.partner-benefit-icon { font-size: 36px; margin-bottom: 16px; display: block; }
.partner-benefit-title { font-family: 'Cormorant Garamond', serif; font-size: 22px; font-weight: 600; color: #1B4332; margin-bottom: 8px; }
.partner-benefit-text { font-family: 'DM Sans', sans-serif; font-size: 14px; font-weight: 300; color: #5a5a5a; line-height: 1.6; }

.forvm-footer { background: #0d2b1f; color: #F9F5EE; padding: 60px 80px 40px; border-top: 1px solid rgba(181,135,58,0.2); margin-top: 60px; }
.footer-top { display: grid; grid-template-columns: 2fr 1fr 1fr; gap: 48px; margin-bottom: 40px; }
.footer-logo { font-family: 'Cormorant Garamond', serif; font-size: 32px; font-weight: 700; color: #B5873A; letter-spacing: 4px; margin-bottom: 12px; }
.footer-tagline { font-family: 'DM Sans', sans-serif; font-size: 13px; font-weight: 300; color: rgba(249,245,238,0.6); line-height: 1.6; }
.footer-col-title { font-family: 'DM Sans', sans-serif; font-size: 11px; font-weight: 600; letter-spacing: 2px; text-transform: uppercase; color: #B5873A; margin-bottom: 16px; }
.footer-links { display: flex; flex-direction: column; gap: 10px; }
.footer-links a { font-family: 'DM Sans', sans-serif; font-size: 13px; font-weight: 300; color: rgba(249,245,238,0.7); text-decoration: none; }
.footer-links a:hover { color: #B5873A; }
.footer-bottom { border-top: 1px solid rgba(249,245,238,0.08); padding-top: 24px; display: flex; justify-content: space-between; align-items: center; }
.footer-copy { font-family: 'DM Sans', sans-serif; font-size: 12px; color: rgba(249,245,238,0.35); }

.wa-float { position: fixed; bottom: 28px; right: 28px; z-index: 9999; background: #25D366; color: white; padding: 14px 22px; border-radius: 50px; font-family: 'DM Sans', sans-serif; font-size: 14px; font-weight: 600; text-decoration: none; display: flex; align-items: center; gap: 10px; box-shadow: 0 4px 20px rgba(37,211,102,0.4); }

@media (max-width: 768px) {
    .section { padding: 48px 20px; }
    .hero-content { padding: 40px 20px; }
    .boxes-grid { grid-template-columns: 1fr; }
    .values-grid { grid-template-columns: 1fr; }
    .steps-grid { grid-template-columns: 1fr; gap: 32px; }
    .chef-grid { grid-template-columns: 1fr; gap: 32px; }
    .partner-benefits { grid-template-columns: 1fr; }
    .footer-top { grid-template-columns: 1fr; gap: 32px; }
    .forvm-nav { padding: 0 20px; }
    .forvm-nav-links { display: none; }
}
</style>
""", unsafe_allow_html=True)

# ─── STATO DELLA SESSIONE (NAVIGAZIONE NATIVA) ────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "home"
if "persons" not in st.session_state:
    st.session_state.persons = 2

def nav_to(page_name):
    st.session_state.page = page_name
    st.rerun()

# ─── HEADER & MENU DI NAVIGAZIONE ───────────────────────────────────
wa_general = get_whatsapp_url("Informazioni Generali", st.session_state.persons)

st.markdown(f"""
<nav class="forvm-nav">
    <span class="forvm-nav-logo">FORVM</span>
    <div class="forvm-nav-links">
        <span style="color:#B5873A; font-size:11px; letter-spacing:1px; font-family:'DM Sans'; text-transform:uppercase;">Naviga tra le sezioni con i pulsanti qui sotto</span>
    </div>
    <a href="{wa_general}" target="_blank" class="nav-wa-btn">💬 Ordina su WhatsApp</a>
</nav>
""", unsafe_allow_html=True)

# Pulsanti di navigazione nativi Streamlit ad alto impatto estetico
cols_nav = st.columns([1, 1.2, 1.3, 1.1, 1.1, 4])
pages = ["home", "catalogo", "come_funziona", "chi_siamo", "partner"]
labels = ["🏠 Home", "📦 Catalogo Box", "❓ Come Funziona", "👨‍🍳 Chi Siamo", "🤝 Per gli Host"]

for col, pg, lb in zip(cols_nav, pages, labels):
    with col:
        is_active = st.session_state.page == pg
        btn_label = f"✨ {lb}" if is_active else lb
        if st.button(btn_label, key=f"nav_btn_{pg}", use_container_width=True):
            nav_to(pg)

# Gestione della pagina corrente
current_page = st.session_state.page

# ══════════════════════════════════════════════════════════════════════
# PAGINA: HOME
# ═══════════════════════════════════════════════════════════════════
if current_page == "home":
    st.markdown("""
    <div class="hero-section">
        <div class="hero-pattern"></div>
        <div class="hero-arch">🏛️</div>
        <div class="hero-content">
            <div class="hero-eyebrow">Roma · Lazio · Artigianale</div>
            <h1 class="hero-h1"><em>Il mercato di Roma.</em><br>2000 anni dopo.</h1>
            <p class="hero-subtitle">Prodotti laziali d'eccellenza artigianale selezionati dallo chef e consegnati direttamente nel tuo appartamento o casa vacanze a Roma entro 48 ore. Ricette leggendarie in kit pronti da assemblare.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Pulsanti di azione rapida sotto Hero
    c1, c2, _ = st.columns([2, 2, 4])
    with c1:
        if st.button("🛒 SCOPRI IL CATALOGO COMPLETO", key="hero_to_cat", use_container_width=True):
            nav_to("catalogo")
    with c2:
        st.markdown(f'<a href="{wa_general}" target="_blank" style="text-decoration:none;"><div style="background:#25D366; color:white; text-align:center; padding:10px; font-family:\'DM Sans\'; font-weight:600; font-size:14px; border-radius:4px; letter-spacing:1px; border:2px solid #25D366;">💬 PARLA SU WHATSAPP</div></a>', unsafe_allow_html=True)

    st.markdown("""
    <div class="section section-alt">
        <div class="section-label">L'Esclusività</div>
        <h2 class="section-h2">Perché scegliere le nostre Box</h2>
        <div class="values-grid">
            <div class="value-card">
                <span class="value-icon">👨‍🍳</span>
                <div class="value-title">Nessun Grossista</div>
                <div class="value-text">Lo chef seleziona sul campo solo aziende agricole familiari e piccole norcinerie storiche del territorio laziale. Più autentico di così è impossibile.</div>
            </div>
            <div class="value-card">
                <span class="value-icon">📦</span>
                <div class="value-title">Dosi ed Ingredienti Esatti</div>
                <div class="value-text">Ricevi tutto ciò che serve, dal Pecorino Romano DOP grattugiato fresco alle uova biologiche di giornata, con schede ricetta immediate.</div>
            </div>
            <div class="value-card">
                <span class="value-icon">⚡</span>
                <div class="value-title">Consegna Personalizzata</div>
                <div class="value-text">Siamo specializzati nel rifornire chi alloggia in case vacanza o Airbnb a Roma. Concordiamo la fascia oraria precisa su WhatsApp.</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Anteprima delle prime 4 Box nella Home
    st.markdown("""
    <div class="section" style="padding-bottom:10px;">
        <div class="section-label">Un Assaggio del Territorio</div>
        <h2 class="section-h2">Le Box Più Richieste</h2>
    </div>
    """, unsafe_allow_html=True)
    
    persons = st.session_state.persons
    preview_boxes = BOXES[:4]
    
    left_prev = ""
    right_prev = ""
    for i, box in enumerate(preview_boxes):
        price = box["prezzi"].get(persons, 28)
        price_str = f"&euro; {price}"
        persons_str = f"per {persons} person{'a' if persons == 1 else 'e'}"
        vino_badge = f'<div class="box-vino">&#127863; {box["vino"]} incluso</div>' if box["vino"] else ""
        stage_cls = "stagione-estate" if "Estate" in box["stagione"] or "Stagionale" in box["stagione"] else "stagione-tutto"
        wa_url = get_whatsapp_url(box["name"], persons)
        
        card = (
            f'<div class="box-card" style="min-height:340px; margin-bottom:20px; border:1px solid rgba(181,135,58,0.15);">'
            f'<div class="box-header">'
            f'<div><div class="box-number">Box {str(i+1).zfill(2)}</div>'
            f'<div class="box-name">{box["name"]}</div></div>'
            f'<span class="box-emoji">{box["emoji"]}</span>'
            f'</div>'
            f'<span class="box-stagione {stage_cls}">{box["stagione"]}</span>'
            f'<p class="box-desc">{box["desc"]}</p>'
            f'{vino_badge}'
            f'<div class="box-price">{price_str}<span> {persons_str}</span></div>'
            f'<a href="{wa_url}" target="_blank" class="box-btn" style="text-decoration:none;">Ordina su WhatsApp &rarr;</a>'
            f'</div>'
        )
        if i % 2 == 0:
            left_prev += card
        else:
            right_prev += card

    st.markdown(f"""
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;padding:0 80px 40px;">
        <div>{left_prev}</div>
        <div>{right_prev}</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div style='text-align:center; padding-bottom:60px;'>", unsafe_allow_html=True)
    if st.button("✨ ESPLORA TUTTE LE 10 BOX DISPONIBILI →", key="home_to_cat_bottom"):
        nav_to("catalogo")
    st.markdown("</div>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════
# PAGINA: CATALOGO
# ═══════════════════════════════════════════════════════════════════
elif current_page == "catalogo":
    st.markdown("""
    <div class="section section-alt" style="padding-bottom: 24px;">
        <div class="section-label">Catalogo Completo</div>
        <h2 class="section-h2">Le Box di FORVM</h2>
        <p class="section-sub">Seleziona il numero di ospiti per aggiornare all'istante le porzioni e le tariffe delle Box.</p>
    </div>
    """, unsafe_allow_html=True)

    # Selettore persone nativo integrato con stile
    st.markdown("<div style='padding: 0 80px; background: #F9F5EE; font-family:\'DM Sans\'; font-weight:600; color:#1B4332; margin-bottom:12px;'>👥 SELEZIONA IL NUMERO DI PERSONE:</div>", unsafe_allow_html=True)
    cols_p = st.columns([1,1,1,1,1,8])
    for n in range(1, 6):
        with cols_p[n-1]:
            is_selected = st.session_state.persons == n
            label = f"✓ {n} Pers." if is_selected else f"{n} Pers."
            if st.button(label, key=f"p_select_{n}", use_container_width=True):
                st.session_state.persons = n
                st.rerun()
                
    persons = st.session_state.persons

    left_html = ""
    right_html = ""
    
    for i, box in enumerate(BOXES):
        price = box["prezzi"].get(persons)
        if price is None and box["prezzi"]:
            price = list(box["prezzi"].values())[0]
            
        price_str = f"&euro; {price}" if price else "Su richiesta"
        persons_str = f"per {persons} person{'a' if persons == 1 else 'e'}" if price else ""
        vino_badge = f'<div class="box-vino">&#127863; {box["vino"]} incluso</div>' if box["vino"] else ""
        stage_cls = "stagione-estate" if "Estate" in box["stagione"] or "Stagionale" in box["stagione"] else "stagione-tutto"
        if box.get("premium"):
            stage_cls = "stagione-premium"
            
        wa_url = get_whatsapp_url(box["name"], persons)
        
        # Elenco ingredienti
        ing_items = "".join([f"<li>{ing}</li>" for ing in box["ingredienti"]])
        ingredienti_block = f'<div style="margin-bottom:16px;"><span style="font-size:12px; font-weight:600; color:#B5873A; font-family:\'DM Sans\';">Cosa include questo kit:</span><ul style="margin:4px 0; padding-left:16px; font-family:\'DM Sans\'; font-size:13px; color:#5a5a5a; line-height:1.5;">{ing_items}</ul></div>'
        
        price_block = f'<div class="box-price">{price_str}<span> {persons_str}</span></div>' if price else '<div class="box-price-na">Prezzo su richiesta</div>'
        btn_cls = "box-btn gold" if box.get("premium") else "box-btn"
        
        card = (
            f'<div class="box-card" id="{box["id"]}" style="margin-bottom:24px; border:1px solid rgba(181,135,58,0.15);">'
            f'<div class="box-header">'
            f'<div>'
            f'<div class="box-number">Box {str(i+1).zfill(2)}</div>'
            f'<div class="box-name">{box["name"]}</div>'
            f'<div style="font-family:\'DM Sans\';font-size:13px;color:#888;margin-top:3px;font-style:italic;">{box["tagline"]}</div>'
            f'</div>'
            f'<span class="box-emoji">{box["emoji"]}</span>'
            f'</div>'
            f'<span class="box-stagione {stage_cls}">{box["stagione"]}</span>'
            f'<p class="box-desc">{box["desc"]}</p>'
            f'{vino_badge}'
            f'{ingredienti_block}'
            f'{price_block}'
            f'<a href="{wa_url}" target="_blank" class="{btn_cls}" style="text-decoration:none;">Ordina su WhatsApp &rarr;</a>'
            f'</div>'
        )
        if i % 2 == 0:
            left_html += card
        else:
            right_html += card

    st.markdown(f"""
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:24px;padding:32px 80px 80px; background:#F9F5EE;">
        <div>{left_html}</div>
        <div>{right_html}</div>
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════
# PAGINA: COME FUNZIONA
# ═══════════════════════════════════════════════════════════════════
elif current_page == "come_funziona":
    st.markdown("""
    <div class="section section-dark" style="min-height: 40vh;">
        <div class="section-label" style="color: rgba(181,135,58,0.8);">Il Processo</div>
        <h2 class="section-h2 light">Semplice ed Immediato</h2>
        <p class="section-sub light">Riforniamo il tuo appartamento a Roma azzerando ogni complicazione logistica.</p>
        
        <div class="steps-grid">
            <div class="step-item">
                <div class="step-num">01</div>
                <span class="step-icon">📱</span>
                <div class="step-title">Seleziona la Box</div>
                <div class="step-text">Esplora le ricette e scegli il kit perfetto per il tuo pranzo o cena.</div>
            </div>
            <div class="step-item">
                <div class="step-num">02</div>
                <span class="step-icon">💬</span>
                <div class="step-title">Invia su WhatsApp</div>
                <div class="step-text">Cliccando verrai reindirizzato ad una chat precompilata con il nostro account ufficiale.</div>
            </div>
            <div class="step-item">
                <div class="step-num">03</div>
                <span class="step-icon">🗓️</span>
                <div class="step-title">Fissa la Consegna</div>
                <div class="step-text">Pianifichiamo insieme il giorno e lo slot di 2 ore più comodo per la tua giornata.</div>
            </div>
            <div class="step-item">
                <div class="step-num">04</div>
                <span class="step-icon">🍝</span>
                <div class="step-title">Cucina e Goditi</div>
                <div class="step-text">Trovi ingredienti freschi pronti e dosati. Pochi minuti sul fuoco e la cena è servita.</div>
            </div>
        </div>
    </div>
    
    <div class="section section-alt">
        <div class="section-label">Trasparenza</div>
        <h2 class="section-h2">Le Nostre Garanzie Fondamentali</h2>
        <div style="display:grid; grid-template-columns: repeat(3, 1fr); gap:20px; margin-top:32px;">
            <div style="background: white; padding: 28px; border-left: 3px solid #B5873A; box-shadow:0 2px 10px rgba(0,0,0,0.03);">
                <div style="font-size: 24px; margin-bottom: 8px;">💳</div>
                <div style="font-family: 'Cormorant Garamond', serif; font-size: 20px; font-weight: 600; color: #1B4332; margin-bottom: 8px;">Pagamenti Digitali</div>
                <div style="font-family: 'DM Sans', sans-serif; font-size: 14px; color: #5a5a5a; line-height: 1.65;">Transazioni istantanee sicure tramite PayPal, Satispay o link di pagamento prima della consegna.</div>
            </div>
            <div style="background: white; padding: 28px; border-left: 3px solid #B5873A; box-shadow:0 2px 10px rgba(0,0,0,0.03);">
                <div style="font-size: 24px; margin-bottom: 8px;">🌍</div>
                <div style="font-family: 'Cormorant Garamond', serif; font-size: 20px; font-weight: 600; color: #1B4332; margin-bottom: 8px;">Assistenza Internazionale</div>
                <div style="font-family: 'DM Sans', sans-serif; font-size: 14px; color: #5a5a5a; line-height: 1.65;">Parliamo correntemente italiano e inglese per guidare al meglio turisti e viaggiatori da tutto il mondo.</div>
            </div>
            <div style="background: white; padding: 28px; border-left: 3px solid #25D366; box-shadow:0 2px 10px rgba(0,0,0,0.03);">
                <div style="font-size: 24px; margin-bottom: 8px;">⚡</div>
                <div style="font-family: 'Cormorant Garamond', serif; font-size: 20px; font-weight: 600; color: #1B4332; margin-bottom: 8px;">Rimborso Qualità</div>
                <div style="font-family: 'DM Sans', sans-serif; font-size: 14px; color: #5a5a5a; line-height: 1.65;">Se un ingrediente non corrisponde ai massimi standard freschi attesi, provvediamo alla sostituzione immediata.</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════
# PAGINA: CHI SIAMO
# ═══════════════════════════════════════════════════════════════════
elif current_page == "chi_siamo":
    st.markdown("""
    <div class="section section-alt">
        <div class="section-label">La Filosofia</div>
        <h2 class="section-h2">Il Mercato di Roma, 2000 Anni Dopo</h2>
        <div class="chef-grid">
            <div class="chef-text">
                <p>Nell'antica Roma il Foro era il fulcro commerciale in cui i migliori artigiani del cibo della regione confluivano per vendere le proprie prelibatezze. FORVM ricrea questo identico ecosistema in chiave moderna.</p>
                <div class="chef-quote">"Il nostro obiettivo è eliminare la grande distribuzione. Vogliamo che tu possa assaporare il Lazio vero, lo stesso che i romani veraci scelgono per la propria tavola familiare."</div>
                <p>Ogni produttore partner viene selezionato dopo rigide sessioni di assaggio in loco. Sosteniamo lo slow-food e il lavoro rurale locale.</p>
            </div>
            <div class="chef-text" style="background:white; padding:40px; border:1px solid rgba(181,135,58,0.2); border-radius:4px;">
                <h3 style="font-family:'Cormorant Garamond'; font-size:28px; color:#1B4332; margin-bottom:16px;">La Nostra Rete Territoriale</h3>
                <ul style="font-family:'DM Sans'; font-size:15px; color:#5a5a5a; line-height:2; padding-left:20px;">
                    <li><strong>🥩 Norcineria Jacovone (Amatrice)</strong> - Fornitore esclusivo del guanciale laziale</li>
                    <li><strong>🧀 Caseificio Bernardi (Castelli Romani)</strong> - Pecorino Romano a salatura controllata</li>
                    <li><strong>🍷 Casale del Giglio</strong> - Selezione vitivinicola ufficiale DOCG</li>
                    <li><strong>🫒 Oleificio Colli Sabini</strong> - Olio EVO spremuto a freddo di categoria superiore</li>
                </ul>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════
# PAGINA: PER GLI HOST
# ═══════════════════════════════════════════════════════════════════
elif current_page == "partner":
    wa_host = f"https://wa.me/{WHATSAPP_NUMBER}?text=Ciao%20FORVM!%20Sono%20un%20host%20Airbnb%20e%20vorrei%20maggiori%20informazioni%20sulla%20partnership."
    st.markdown(f"""
    <div class="hero-section" style="min-height: 45vh;">
        <div class="hero-pattern"></div>
        <div class="hero-content">
            <div class="hero-eyebrow">Programma Partner Esclusivo</div>
            <h1 class="hero-h1">Porta il Gusto di Roma ai tuoi Ospiti.<br><em>E guadagna una rendita passiva.</em></h1>
            <p class="hero-subtitle">Offri ai turisti che soggiornano nella tua struttura un servizio gastronomico d'eccellenza. Ricevi una commissione automatica del 10% su ogni ordine completato, senza muovere un dito.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div style='padding: 24px 80px 0; background:#F9F5EE;'>", unsafe_allow_html=True)
    st.markdown(f'<a href="{wa_host}" target="_blank" style="text-decoration:none;"><div style="background:#1B4332; color:white; text-align:center; padding:14px; font-family:\'DM Sans\'; font-weight:600; font-size:14px; border-radius:4px; max-width:320px; letter-spacing:1px;">🤝 ATTIVA LA PARTNERSHIP VIA WHATSAPP</div></a>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="section section-alt">
        <div class="section-label">I Vantaggi</div>
        <h2 class="section-h2">Perché Conviene Collaborare con FORVM</h2>
        <div class="partner-benefits">
            <div class="partner-benefit">
                <span class="partner-benefit-icon">💰</span>
                <div class="partner-benefit-title">Guadagno Automatico</div>
                <div class="partner-benefit-text">Generi il 10% netto su ogni box ordinata tramite il codice QR univoco assegnato al tuo appartamento. Accrediti mensili immediati.</div>
            </div>
            <div class="partner-benefit">
                <span class="partner-benefit-icon">🛋️</span>
                <div class="partner-benefit-title">Zero Operatività</div>
                <div class="partner-benefit-text">Ti forniamo un elegante flyer o un espositore da tavolo. Gestiamo noi l'intera transazione, la preparazione del cibo e la consegna a domicilio.</div>
            </div>
            <div class="partner-benefit">
                <span class="partner-benefit-icon">⭐</span>
                <div class="partner-benefit-title">Recensioni a 5 Stelle</div>
                <div class="partner-benefit-text">I tuoi ospiti eviteranno i ristoranti-trappola del centro, vivendo una vera esperienza culinaria d'élite direttamente nel tuo alloggio.</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ─── FOOTER GLOBALE DI TUTTE LE PAGINE ────────────────────────────────
st.markdown(f"""
<footer class="forvm-footer">
    <div class="footer-top">
        <div>
            <div class="footer-logo">FORVM</div>
            <div class="footer-tagline">Il mercato di Roma. 2000 anni dopo.<br>Prodotti laziali artigianali selezionati e consegnati nel tuo alloggio entro 48 ore.</div>
        </div>
        <div>
            <div class="footer-col-title">Contatti ed Assistenza</div>
            <div class="footer-links">
                <a href="{wa_general}" target="_blank">📱 Supporto WhatsApp Clienti</a>
                <a href="mailto:info@forvm.roma">✉️ info@forvm.roma</a>
                <a href="https://instagram.com/forvm.roma" target="_blank">📸 Instagram: @forvm.roma</a>
            </div>
        </div>
        <div>
            <div class="footer-col-title">Trasparenza</div>
            <div class="footer-links">
                <a href="#">Privacy Policy</a>
                <a href="#">Cookie Policy</a>
                <span style="font-size:12px; color:rgba(249,245,238,0.4);">Partita IVA [In aggiornamento]</span>
            </div>
        </div>
    </div>
    <div class="footer-bottom">
        <div class="footer-copy">© 2026 FORVM · Tutti i diritti riservati.</div>
        <div class="footer-copy">Selezionato accuratamente · Consegnato a Roma</div>
    </div>
</footer>

<a href="{wa_general}" target="_blank" class="wa-float" style="text-decoration:none;">
    <span>💬 WhatsApp Ordini</span>
</a>
""", unsafe_allow_html=True)