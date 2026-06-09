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