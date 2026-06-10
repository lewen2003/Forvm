import streamlit as st
import base64
import urllib.parse

st.set_page_config(
    page_title="FORVM — Prodotti Laziali Artigianali · Consegna 48h Roma",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

def img_to_b64(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

LOGO_B64 = img_to_b64("logo.jpeg")
BOX_B64  = img_to_b64("box_product.jpeg")
WHATSAPP_NUMBER = "393000000000"

BOXES = [
    {"id":"colazione","name":"La Colazione Romana","emoji":"☕","tagline":"Il risveglio autentico della capitale","desc":"Cornetti artigianali, maritozzo con panna, caffè di torrefazione storica, marmellata locale.","ingredienti":["Cornetti artigianali (x2 a persona)","Maritozzo con panna","Caffè Torrefazione Sant'Eustachio","Marmellata di agrumi laziali","Succo di arancia rossa Siciliana"],"prezzi":{1:16,2:26,3:35},"stagione":"Tutto l'anno","vino":None},
    {"id":"carbonara","name":"La Carbonara","emoji":"🍝","tagline":"Kit completo per la ricetta originale","desc":"Guanciale DOP, Pecorino Romano DOP, rigatoni trafilati al bronzo, uova fresche laziali, vino Frascati DOCG.","ingredienti":["Guanciale DOP di Amatrice (100g a persona)","Pecorino Romano DOP (80g a persona)","Rigatoni trafilati al bronzo (100g a persona)","Uova fresche laziali (2 a persona)","Pepe nero intero macinato fresco","Frascati DOCG (75cl)"],"prezzi":{1:18,2:28,3:38},"stagione":"Tutto l'anno","vino":"Frascati DOCG"},
    {"id":"amatriciana","name":"La Amatriciana","emoji":"🍅","tagline":"La tradizione di Amatrice in una box","desc":"Guanciale stagionato, pomodori San Marzano, Pecorino Romano, bucatini artigianali, Cesanese DOCG.","ingredienti":["Guanciale stagionato di Amatrice (100g a persona)","Pomodori San Marzano DOP (200g a persona)","Pecorino Romano DOP (60g a persona)","Bucatini artigianali (100g a persona)","Cesanese DOCG (75cl)"],"prezzi":{1:17,2:27,3:37},"stagione":"Tutto l'anno","vino":"Cesanese DOCG"},
    {"id":"cacio","name":"La Cacio e Pepe","emoji":"🧀","tagline":"Due ingredienti, una filosofia","desc":"Pecorino Romano stagionato, pepe nero Tellicherry, spaghetti alla chitarra artigianali, Frascati DOC.","ingredienti":["Pecorino Romano stagionato 24 mesi (120g a persona)","Pepe nero Tellicherry intero","Spaghetti alla chitarra artigianali (100g a persona)","Frascati DOC (75cl)"],"prezzi":{1:16,2:26,3:36},"stagione":"Tutto l'anno","vino":"Frascati DOC"},
    {"id":"gricia","name":"La Gricia","emoji":"🥩","tagline":"La madre di tutte le paste romane","desc":"Guanciale artigianale, Pecorino Romano DOP, rigatoni di semola dura laziale, Marino DOC.","ingredienti":["Guanciale artigianale (110g a persona)","Pecorino Romano DOP (80g a persona)","Rigatoni di semola dura laziale (100g a persona)","Marino DOC (75cl)"],"prezzi":{1:17,2:27,3:37},"stagione":"Tutto l'anno","vino":"Marino DOC"},
    {"id":"pollo","name":"Il Pollo con i Peperoni","emoji":"🫑","tagline":"Il secondo della domenica romana","desc":"Pollo ruspante laziale, peperoni cornetti, aglio di Cori, vino bianco laziale, Frascati DOCG.","ingredienti":["Pollo ruspante laziale (300g a persona)","Peperoni cornetti rossi e gialli","Aglio di Cori","Vino bianco laziale per cottura","Rosmarino e alloro freschi","Frascati DOCG (75cl)"],"prezzi":{1:18,2:28,3:38},"stagione":"Estate · giu-set","vino":"Frascati DOCG"},
    {"id":"caprese","name":"La Caprese Laziale","emoji":"🌿","tagline":"Freschezza dei Castelli Romani","desc":"Mozzarella di bufala DOP, pomodori cuore di bue laziali, basilico fresco, olio EVO dei Colli Sabini.","ingredienti":["Mozzarella di bufala DOP (150g a persona)","Pomodori cuore di bue laziali (200g a persona)","Basilico fresco del Lazio","Olio EVO dei Colli Sabini DOP","Sale marino di Cervia"],"prezzi":{1:16,2:24,3:32},"stagione":"Stagionale · giu-set","vino":None},
    {"id":"cantina","name":"La Cantina Laziale","emoji":"🍷","tagline":"Un viaggio tra i vigneti del Lazio","desc":"Selezione di 2 vini DOCG laziali con tagliere di formaggi e salumi tipici. Minimo 2 persone.","ingredienti":["Frascati Superiore DOCG (75cl)","Cesanese del Piglio DOCG (75cl)","Pecorino Romano DOP (80g a persona)","Guanciale stagionato (60g a persona)","Olive di Gaeta DOP (50g a persona)","Pane di Lariano (200g)"],"prezzi":{2:38,3:48},"stagione":"Tutto l'anno","vino":"2 vini DOCG"},
    {"id":"dolci","name":"I Dolci Romani","emoji":"🍮","tagline":"Il finale perfetto per una serata romana","desc":"Tiramisù artigianale, crostata di visciole, biscotti del Lazio, Cannellino DOCG.","ingredienti":["Tiramisù artigianale (porzione a persona)","Crostata di visciole laziale (100g a persona)","Biscotti brutti ma buoni","Cioccolato fondente di artigiano romano","Cannellino di Frascati DOCG (37.5cl)"],"prezzi":{1:22,2:32,3:42},"stagione":"Tutto l'anno","vino":"Cannellino DOCG"},
    {"id":"chef","name":"Chef a Domicilio","emoji":"👨‍🍳","tagline":"Roma in cucina, a casa tua","desc":"Lo chef viene nel tuo appartamento e cucina un menu romano completo. Prenotazione con 48h di anticipo.","ingredienti":["Menu personalizzato dallo chef","Tutti gli ingredienti inclusi","Mise en place e servizio","Abbinamento vini laziali","Ricette originali da portare a casa"],"prezzi":{},"stagione":"Tutto l'anno","vino":None,"premium":True},
]

def wa_url(box_name, n):
    if box_name == "Chef a Domicilio":
        msg = f"Ciao FORVM! Vorrei prenotare Chef a Domicilio. Persone: {n} · Data: [da completare] · Indirizzo: [da completare]"
    else:
        msg = f"Ciao FORVM! Vorrei ordinare {box_name} per {n} person{'a' if n==1 else 'e'}. Indirizzo: [da completare]. Quando consegnate?"
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={urllib.parse.quote(msg)}"

params       = st.query_params
current_page = params.get("p", "home")
persons      = int(params.get("pers", "2"))
wa_gen       = f"https://wa.me/{WHATSAPP_NUMBER}?text=Ciao%20FORVM!%20Vorrei%20ordinare%20una%20box%20laziale."

def nav_active(pg):
    return 'nav-active' if current_page == pg else ''

# ══════════════════════════════════════════════════════════════════
# GLOBAL CSS — Marble · Travertine · Roman Lapidary
# ══════════════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;0,700;1,300;1,400;1,600&family=Cinzel:wght@400;600;700&family=DM+Sans:wght@300;400;500&display=swap');

*,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}

/* ── Streamlit chrome reset ── */
.main .block-container{padding:0!important;max-width:100%!important;}
#MainMenu,footer,header,.stDeployButton{display:none!important;visibility:hidden!important;}
[data-testid="stSidebar"],[data-testid="collapsedControl"]{display:none!important;}
section[data-testid="stMain"]>div{padding:0!important;}

/* ── Root tokens ── */
:root{
  --marble:     #F4F0E8;
  --marble-mid: #EDE7D9;
  --marble-dk:  #E0D8C8;
  --travertine: #D4C9B0;
  --stone:      #A89880;
  --stone-dk:   #7A6B5A;
  --aurum:      #B8933F;
  --aurum-lt:   #D4AB5A;
  --aurum-dk:   #8B6B28;
  --obsidian:   #1A1612;
  --ink:        #2C2419;
  --ink-mid:    #4A3F32;
  --ink-lt:     #6B5C4A;
  --wa:         #25D366;
  --wa-dk:      #1aab52;
}

body{font-family:'DM Sans',sans-serif;background:var(--marble);color:var(--ink);}
h1,h2,h3,h4{font-family:'Cormorant Garamond',serif;}

/* ══════════════════════════════════════
   NAVBAR
══════════════════════════════════════ */
.forvm-nav{
  position:sticky;top:0;z-index:1000;
  background:var(--obsidian);
  border-bottom:1px solid var(--aurum-dk);
  padding:0 60px;
  display:flex;align-items:center;justify-content:space-between;
  height:68px;
}
.nav-logo{
  font-family:'Cinzel',serif;
  font-size:22px;font-weight:700;
  letter-spacing:8px;
  color:var(--aurum);
  text-decoration:none;
}
.nav-links{display:flex;align-items:center;gap:36px;}
.nav-links a{
  font-family:'Cinzel',serif;
  font-size:10px;font-weight:400;
  letter-spacing:3px;text-transform:uppercase;
  color:var(--marble);opacity:.7;
  text-decoration:none;
  transition:opacity .2s,color .2s;
  padding-bottom:2px;
  border-bottom:1px solid transparent;
}
.nav-links a:hover{opacity:1;color:var(--aurum-lt);}
.nav-links a.nav-active{opacity:1;color:var(--aurum);border-bottom-color:var(--aurum);}
.nav-wa{
  background:var(--wa)!important;
  color:#fff!important;
  font-family:'DM Sans',sans-serif!important;
  font-size:12px!important;font-weight:500!important;
  letter-spacing:.5px!important;
  padding:9px 20px!important;
  border-radius:0!important;
  border:none!important;
  opacity:1!important;
}
.nav-wa:hover{background:var(--wa-dk)!important;}

/* ══════════════════════════════════════
   HERO — Colonnato
══════════════════════════════════════ */
.hero{
  position:relative;
  width:100%;min-height:92vh;
  background:var(--obsidian);
  display:flex;align-items:center;
  overflow:hidden;
}
/* Marble texture overlay */
.hero::before{
  content:'';position:absolute;inset:0;
  background:
    repeating-linear-gradient(
      92deg,
      transparent 0,transparent 120px,
      rgba(180,150,90,.03) 120px,rgba(180,150,90,.03) 121px
    ),
    repeating-linear-gradient(
      0deg,
      transparent 0,transparent 80px,
      rgba(180,150,90,.02) 80px,rgba(180,150,90,.02) 81px
    );
  z-index:0;
}
/* Column silhouettes */
.hero-columns{
  position:absolute;right:0;top:0;bottom:0;width:55%;
  display:flex;align-items:flex-end;justify-content:flex-end;
  z-index:1;overflow:hidden;
}
.col-svg{width:100%;height:100%;opacity:.13;}

.hero-content{
  position:relative;z-index:2;
  padding:0 0 0 80px;
  max-width:660px;
}
.hero-era{
  font-family:'Cinzel',serif;
  font-size:10px;font-weight:400;letter-spacing:5px;
  color:var(--aurum);
  margin-bottom:28px;
  display:flex;align-items:center;gap:16px;
}
.hero-era::after{content:'';display:block;width:48px;height:1px;background:var(--aurum);opacity:.5;}

.hero-h1{
  font-family:'Cormorant Garamond',serif;
  font-size:clamp(54px,6.5vw,96px);
  font-weight:300;line-height:1.0;
  color:var(--marble);
  margin-bottom:8px;
  letter-spacing:-1px;
}
.hero-h1 em{font-style:italic;color:var(--aurum-lt);}
.hero-h1 strong{font-weight:600;display:block;}

.hero-rule{
  width:60px;height:1px;
  background:linear-gradient(90deg,var(--aurum),transparent);
  margin:28px 0;
}
.hero-sub{
  font-family:'DM Sans',sans-serif;
  font-size:16px;font-weight:300;line-height:1.75;
  color:rgba(244,240,232,.65);
  max-width:460px;
  margin-bottom:44px;
}
.hero-ctas{display:flex;gap:16px;flex-wrap:wrap;}
.btn-aurum{
  display:inline-block;
  background:var(--aurum);color:var(--obsidian);
  font-family:'Cinzel',serif;font-size:11px;font-weight:600;letter-spacing:3px;
  text-transform:uppercase;
  padding:16px 36px;text-decoration:none;
  border:1px solid var(--aurum);
  transition:all .25s;
}
.btn-aurum:hover{background:var(--aurum-lt);border-color:var(--aurum-lt);}
.btn-ghost{
  display:inline-flex;align-items:center;gap:10px;
  background:transparent;color:var(--marble);
  font-family:'DM Sans',sans-serif;font-size:13px;font-weight:300;letter-spacing:1px;
  padding:15px 28px;text-decoration:none;
  border:1px solid rgba(244,240,232,.2);
  transition:all .25s;
}
.btn-ghost:hover{border-color:var(--wa);color:var(--wa);}
.btn-ghost .dot{color:var(--wa);}

/* ══════════════════════════════════════
   THREE PILLARS (values)
══════════════════════════════════════ */
.pillars{
  display:grid;grid-template-columns:repeat(3,1fr);
  background:var(--obsidian);
  border-top:1px solid rgba(184,147,63,.2);
}
.pillar{
  padding:44px 40px;
  border-right:1px solid rgba(184,147,63,.15);
  position:relative;
}
.pillar:last-child{border-right:none;}
.pillar-num{
  font-family:'Cinzel',serif;
  font-size:11px;letter-spacing:3px;
  color:var(--aurum-dk);
  margin-bottom:20px;display:block;
}
.pillar-icon{font-size:26px;margin-bottom:14px;display:block;}
.pillar-title{
  font-family:'Cormorant Garamond',serif;
  font-size:22px;font-weight:600;
  color:var(--marble);margin-bottom:10px;
}
.pillar-text{
  font-family:'DM Sans',sans-serif;
  font-size:13px;font-weight:300;line-height:1.7;
  color:rgba(244,240,232,.55);
}

/* ══════════════════════════════════════
   SECTION HEADERS
══════════════════════════════════════ */
.sec-wrap{padding:72px 80px;}
.sec-wrap.bg-marble{background:var(--marble);}
.sec-wrap.bg-stone{background:var(--marble-mid);}
.sec-wrap.bg-dark{background:var(--ink);}
.sec-wrap.bg-obsidian{background:var(--obsidian);}

.sec-label{
  font-family:'Cinzel',serif;
  font-size:9px;font-weight:400;letter-spacing:4px;text-transform:uppercase;
  color:var(--aurum);margin-bottom:12px;
  display:flex;align-items:center;gap:12px;
}
.sec-label::before{content:'';display:block;width:24px;height:1px;background:var(--aurum);}

.sec-h2{
  font-family:'Cormorant Garamond',serif;
  font-size:clamp(36px,4vw,56px);font-weight:300;line-height:1.1;
  color:var(--ink);margin-bottom:16px;letter-spacing:-.5px;
}
.sec-h2.light{color:var(--marble);}
.sec-h2 em{font-style:italic;color:var(--aurum);}

.sec-sub{
  font-family:'DM Sans',sans-serif;
  font-size:15px;font-weight:300;line-height:1.75;
  color:var(--ink-lt);max-width:520px;
}
.sec-sub.light{color:rgba(244,240,232,.55);}

/* ══════════════════════════════════════
   BOX CARDS — Lapidary style
══════════════════════════════════════ */
.cards-grid{
  display:grid;grid-template-columns:1fr 1fr;
  gap:1px;background:var(--travertine);
  margin-top:40px;
}
.card{
  background:var(--marble);
  padding:36px 36px 28px;
  display:flex;flex-direction:column;
  transition:background .2s;
  position:relative;
}
.card:hover{background:#FFFDF7;}
.card::before{
  content:'';
  position:absolute;top:0;left:0;right:0;
  height:2px;
  background:linear-gradient(90deg,var(--aurum) 0,transparent 60%);
  opacity:0;transition:opacity .25s;
}
.card:hover::before{opacity:1;}

.card-num{
  font-family:'Cinzel',serif;
  font-size:9px;letter-spacing:3px;
  color:var(--stone);margin-bottom:16px;
}
.card-head{
  display:flex;justify-content:space-between;align-items:flex-start;
  margin-bottom:6px;
}
.card-name{
  font-family:'Cormorant Garamond',serif;
  font-size:27px;font-weight:600;line-height:1.15;
  color:var(--ink);
}
.card-emoji{font-size:26px;line-height:1;}
.card-tagline{
  font-family:'Cormorant Garamond',serif;
  font-size:14px;font-style:italic;
  color:var(--stone-dk);margin-bottom:14px;
}

/* Season badge — chiseled look */
.badge{
  display:inline-block;
  font-family:'Cinzel',serif;
  font-size:8px;letter-spacing:2px;text-transform:uppercase;
  padding:3px 10px;margin-bottom:14px;
}
.badge-always{background:var(--marble-dk);color:var(--ink-lt);}
.badge-estate{background:#FFF4D6;color:#7A5800;}
.badge-stagionale{background:#E8F4F0;color:#1A4A3A;}
.badge-premium{background:var(--ink);color:var(--aurum);}

.card-desc{
  font-family:'DM Sans',sans-serif;
  font-size:13px;font-weight:300;line-height:1.7;
  color:var(--ink-mid);margin-bottom:14px;flex:1;
}

/* Thin rule before price */
.card-rule{
  width:100%;height:1px;
  background:var(--travertine);
  margin:14px 0;
}

.card-vino{
  font-family:'Cinzel',serif;
  font-size:8px;letter-spacing:2px;
  color:#7A4A8A;margin-bottom:10px;
}
.card-price{
  font-family:'Cormorant Garamond',serif;
  font-size:32px;font-weight:600;
  color:var(--ink);line-height:1;
  margin-bottom:4px;
}
.card-price span{
  font-family:'DM Sans',sans-serif;
  font-size:12px;font-weight:300;
  color:var(--stone);
}
.card-price-na{
  font-family:'Cormorant Garamond',serif;
  font-size:16px;font-style:italic;
  color:var(--aurum-dk);margin-bottom:4px;
}

/* CTA inside card */
.card-cta{
  display:block;width:100%;text-align:center;
  background:var(--ink);color:var(--marble);
  font-family:'Cinzel',serif;font-size:9px;
  letter-spacing:3px;text-transform:uppercase;
  padding:14px 20px;text-decoration:none;
  margin-top:20px;
  border:1px solid var(--ink);
  transition:all .22s;
}
.card-cta:hover{background:transparent;color:var(--ink);}
.card-cta.premium-cta{
  background:var(--aurum);color:var(--obsidian);
  border-color:var(--aurum);
}
.card-cta.premium-cta:hover{background:var(--aurum-lt);border-color:var(--aurum-lt);}

/* Ingredient accordion */
.ing-wrap{margin:0 0 10px;}
.ing-details summary{
  font-family:'Cinzel',serif;
  font-size:8px;letter-spacing:2px;text-transform:uppercase;
  color:var(--aurum-dk);cursor:pointer;
  list-style:none;padding:6px 0;
  border-top:1px solid var(--travertine);
}
.ing-details summary::-webkit-details-marker{display:none;}
.ing-details summary::marker{display:none;}
.ing-list{
  list-style:none;padding:10px 0 4px;
  display:grid;gap:5px;
}
.ing-list li{
  font-family:'DM Sans',sans-serif;
  font-size:12px;font-weight:300;color:var(--ink-mid);
  padding-left:14px;position:relative;line-height:1.5;
}
.ing-list li::before{
  content:'·';position:absolute;left:0;
  color:var(--aurum);font-size:16px;line-height:1;top:-1px;
}

/* ══════════════════════════════════════
   PERSON SELECTOR
══════════════════════════════════════ */
.pers-bar{
  display:flex;align-items:center;gap:0;
  margin:32px 0 0;
  border:1px solid var(--travertine);
  width:fit-content;
}
.pers-bar-label{
  font-family:'Cinzel',serif;
  font-size:9px;letter-spacing:3px;
  color:var(--stone-dk);
  padding:11px 20px;
  border-right:1px solid var(--travertine);
  white-space:nowrap;
}
.pers-btn{
  font-family:'Cinzel',serif;
  font-size:10px;letter-spacing:2px;
  padding:11px 18px;
  text-decoration:none;
  color:var(--ink-mid);
  border-right:1px solid var(--travertine);
  transition:all .15s;
}
.pers-btn:last-child{border-right:none;}
.pers-btn:hover{background:var(--marble-mid);color:var(--ink);}
.pers-btn.active{background:var(--ink);color:var(--marble);}

/* ══════════════════════════════════════
   HOW IT WORKS — arch steps
══════════════════════════════════════ */
.steps{
  display:grid;grid-template-columns:repeat(4,1fr);
  gap:0;margin-top:52px;
  border-top:1px solid rgba(184,147,63,.25);
}
.step{
  padding:36px 32px 36px 0;
  position:relative;
}
.step:not(:last-child)::after{
  content:'';
  position:absolute;right:0;top:36px;
  width:1px;height:50%;
  background:rgba(184,147,63,.2);
}
.step-n{
  font-family:'Cinzel',serif;
  font-size:40px;font-weight:400;
  color:var(--aurum);opacity:.9;
  line-height:1;margin-bottom:16px;
  display:block;
}
.step-title{
  font-family:'Cormorant Garamond',serif;
  font-size:22px;font-weight:600;
  color:var(--marble);margin-bottom:8px;
}
.step-text{
  font-family:'DM Sans',sans-serif;
  font-size:13px;font-weight:300;line-height:1.7;
  color:rgba(244,240,232,.55);
}

/* ══════════════════════════════════════
   QUOTE / MANIFESTO
══════════════════════════════════════ */
.manifesto{
  padding:80px;
  text-align:center;
  position:relative;
  overflow:hidden;
}
.manifesto::before,.manifesto::after{
  content:'"';
  font-family:'Cormorant Garamond',serif;
  font-size:200px;font-weight:700;
  color:var(--aurum);opacity:.06;
  position:absolute;line-height:1;
}
.manifesto::before{top:-20px;left:40px;}
.manifesto::after{content:'"';bottom:-60px;right:40px;}
.manifesto-text{
  font-family:'Cormorant Garamond',serif;
  font-size:clamp(28px,3vw,44px);
  font-weight:300;font-style:italic;
  line-height:1.4;
  color:var(--ink);
  max-width:800px;margin:0 auto 28px;
  position:relative;z-index:1;
}
.manifesto-attr{
  font-family:'Cinzel',serif;
  font-size:9px;letter-spacing:4px;
  color:var(--aurum-dk);
  position:relative;z-index:1;
}

/* ══════════════════════════════════════
   PRODUCER CARDS
══════════════════════════════════════ */
.producers{
  display:grid;grid-template-columns:repeat(4,1fr);
  gap:1px;background:var(--travertine);
  margin-top:40px;
}
.producer{
  background:var(--marble);
  padding:32px;
  text-align:center;
}
.producer-icon{font-size:32px;margin-bottom:12px;display:block;}
.producer-name{
  font-family:'Cormorant Garamond',serif;
  font-size:19px;font-weight:600;color:var(--ink);
  margin-bottom:4px;
}
.producer-loc{
  font-family:'Cinzel',serif;
  font-size:8px;letter-spacing:2px;
  color:var(--aurum-dk);
  margin-bottom:8px;display:block;
}
.producer-prod{
  font-family:'DM Sans',sans-serif;
  font-size:12px;font-weight:300;
  color:var(--ink-lt);line-height:1.5;
}

/* ══════════════════════════════════════
   PARTNER BENEFITS
══════════════════════════════════════ */
.benefits{
  display:grid;grid-template-columns:repeat(3,1fr);
  gap:1px;background:var(--travertine);
  margin-top:40px;
}
.benefit{
  background:var(--marble);
  padding:40px 36px;
  text-align:center;
}
.benefit-icon{font-size:36px;margin-bottom:16px;display:block;}
.benefit-title{
  font-family:'Cormorant Garamond',serif;
  font-size:23px;font-weight:600;
  color:var(--ink);margin-bottom:10px;
}
.benefit-text{
  font-family:'DM Sans',sans-serif;
  font-size:13px;font-weight:300;
  color:var(--ink-lt);line-height:1.65;
}

/* ══════════════════════════════════════
   FAQ
══════════════════════════════════════ */
.faq-item{
  border-bottom:1px solid var(--travertine);
  padding:22px 0;
}
.faq-q{
  font-family:'Cormorant Garamond',serif;
  font-size:21px;font-weight:600;
  color:var(--ink);margin-bottom:10px;
}
.faq-a{
  font-family:'DM Sans',sans-serif;
  font-size:14px;font-weight:300;
  line-height:1.75;color:var(--ink-lt);
}

/* ══════════════════════════════════════
   INFO TILES
══════════════════════════════════════ */
.info-tiles{
  display:grid;grid-template-columns:repeat(3,1fr);
  gap:1px;background:var(--travertine);
  margin:40px 0;
}
.info-tile{
  background:var(--marble);
  padding:32px;
  border-top:3px solid var(--aurum-dk);
}
.info-tile-icon{font-size:24px;margin-bottom:12px;display:block;}
.info-tile-title{
  font-family:'Cormorant Garamond',serif;
  font-size:21px;font-weight:600;
  color:var(--ink);margin-bottom:8px;
}
.info-tile-text{
  font-family:'DM Sans',sans-serif;
  font-size:13px;font-weight:300;
  color:var(--ink-lt);line-height:1.65;
}

/* ══════════════════════════════════════
   PARTNER TABLE
══════════════════════════════════════ */
.partner-table{
  width:100%;border-collapse:collapse;
  font-family:'DM Sans',sans-serif;font-size:13px;
  margin-top:32px;
}
.partner-table thead tr{
  background:var(--ink);color:var(--marble);
}
.partner-table th{
  padding:14px 18px;font-weight:400;
  font-family:'Cinzel',serif;font-size:9px;letter-spacing:2px;
  text-align:center;
}
.partner-table th:first-child{text-align:left;}
.partner-table td{
  padding:12px 18px;text-align:center;
  color:var(--ink-mid);
  border-bottom:1px solid var(--marble-dk);
}
.partner-table td:first-child{
  text-align:left;font-weight:500;color:var(--ink);
}
.partner-table tr:nth-child(odd) td{background:#FDFAF4;}
.partner-table tr:nth-child(even) td{background:var(--marble);}
.comm-val{color:#1A7A3A;font-weight:500;}

/* ══════════════════════════════════════
   CHEF SECTION
══════════════════════════════════════ */
.chef-grid{
  display:grid;grid-template-columns:1fr 1fr;
  gap:72px;align-items:center;margin-top:40px;
}
.chef-text p{
  font-family:'DM Sans',sans-serif;
  font-size:15px;font-weight:300;line-height:1.8;
  color:var(--ink-mid);margin-bottom:18px;
}
.chef-quote{
  font-family:'Cormorant Garamond',serif;
  font-size:23px;font-style:italic;
  color:var(--ink);line-height:1.55;
  border-left:2px solid var(--aurum);
  padding:4px 0 4px 20px;
  margin:24px 0;
}
.chef-img{
  position:relative;
}
.chef-img::after{
  content:'';position:absolute;
  bottom:-12px;right:-12px;
  width:70%;height:70%;
  border:1px solid rgba(184,147,63,.3);
  z-index:0;pointer-events:none;
}
.chef-img img{
  width:100%;display:block;
  position:relative;z-index:1;
}

/* ══════════════════════════════════════
   FOOTER
══════════════════════════════════════ */
.forvm-footer{
  background:var(--obsidian);
  padding:60px 80px 36px;
  border-top:1px solid rgba(184,147,63,.15);
}
.footer-grid{
  display:grid;grid-template-columns:2fr 1fr 1fr;
  gap:48px;margin-bottom:48px;
}
.footer-brand{
  font-family:'Cinzel',serif;
  font-size:24px;font-weight:700;letter-spacing:8px;
  color:var(--aurum);margin-bottom:14px;
}
.footer-tagline{
  font-family:'Cormorant Garamond',serif;
  font-size:15px;font-style:italic;
  color:rgba(244,240,232,.4);line-height:1.6;
}
.footer-col-title{
  font-family:'Cinzel',serif;
  font-size:9px;letter-spacing:3px;
  color:var(--aurum-dk);margin-bottom:18px;
}
.footer-links{display:flex;flex-direction:column;gap:12px;}
.footer-links a{
  font-family:'DM Sans',sans-serif;
  font-size:13px;font-weight:300;
  color:rgba(244,240,232,.5);text-decoration:none;
  transition:color .2s;
}
.footer-links a:hover{color:var(--aurum-lt);}
.footer-rule{
  border:none;border-top:1px solid rgba(244,240,232,.06);
  margin-bottom:24px;
}
.footer-copy{
  display:flex;justify-content:space-between;align-items:center;
  font-family:'DM Sans',sans-serif;font-size:11px;
  color:rgba(244,240,232,.2);
}

/* ══════════════════════════════════════
   FLOATING WA
══════════════════════════════════════ */
.wa-float{
  position:fixed;bottom:28px;right:28px;z-index:9999;
  background:var(--wa);color:#fff;
  padding:13px 24px 13px 18px;
  font-family:'DM Sans',sans-serif;font-size:13px;font-weight:500;
  text-decoration:none;
  display:flex;align-items:center;gap:10px;
  box-shadow:0 4px 24px rgba(37,211,102,.35);
  transition:all .25s;
  border-left:3px solid var(--wa-dk);
}
.wa-float:hover{background:var(--wa-dk);transform:translateY(-2px);box-shadow:0 8px 32px rgba(37,211,102,.45);}
.wa-float-icon{font-size:18px;}

/* ══════════════════════════════════════
   RESPONSIVE
══════════════════════════════════════ */
@media(max-width:768px){
  .forvm-nav{padding:0 20px;}
  .nav-links{display:none;}
  .sec-wrap{padding:48px 20px;}
  .hero-content{padding:0 24px;}
  .cards-grid,.benefits,.producers,.info-tiles{grid-template-columns:1fr;}
  .steps{grid-template-columns:1fr 1fr;}
  .chef-grid{grid-template-columns:1fr;}
  .footer-grid{grid-template-columns:1fr;gap:32px;}
  .manifesto{padding:48px 24px;}
  .pillars{grid-template-columns:1fr;}
}
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════
# NAVBAR
# ══════════════════════════════════════════════════════════════════
st.markdown(f"""
<nav class="forvm-nav">
  <a href="?p=home" class="nav-logo">FORVM</a>
  <div class="nav-links">
    <a href="?p=home" class="{nav_active('home')}">Home</a>
    <a href="?p=catalogo" class="{nav_active('catalogo')}">Catalogo</a>
    <a href="?p=come_funziona" class="{nav_active('come_funziona')}">Come Funziona</a>
    <a href="?p=chi_siamo" class="{nav_active('chi_siamo')}">Chi Siamo</a>
    <a href="?p=partner" class="{nav_active('partner')}">Per gli Host</a>
    <a href="{wa_gen}" target="_blank" class="nav-wa">&#128241; Ordina su WhatsApp</a>
  </div>
</nav>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════
# HOME
# ══════════════════════════════════════════════════════════════════
if current_page == "home":

    # — Hero — column SVG drawn in pure markup
    st.markdown(f"""
    <div class="hero">
      <div class="hero-columns">
        <svg class="col-svg" viewBox="0 0 900 900" preserveAspectRatio="xMaxYMax meet" fill="none" xmlns="http://www.w3.org/2000/svg">
          <!-- Left column -->
          <rect x="120" y="120" width="52" height="700" fill="#B8933F"/>
          <rect x="110" y="105" width="72" height="22" fill="#B8933F"/>
          <rect x="105" y="92" width="82" height="16" fill="#B8933F"/>
          <rect x="110" y="808" width="72" height="22" fill="#B8933F"/>
          <rect x="105" y="828" width="82" height="18" fill="#B8933F"/>
          <!-- Right column -->
          <rect x="580" y="120" width="52" height="700" fill="#B8933F"/>
          <rect x="570" y="105" width="72" height="22" fill="#B8933F"/>
          <rect x="565" y="92" width="82" height="16" fill="#B8933F"/>
          <rect x="570" y="808" width="72" height="22" fill="#B8933F"/>
          <rect x="565" y="828" width="82" height="18" fill="#B8933F"/>
          <!-- Far right column -->
          <rect x="790" y="200" width="40" height="620" fill="#B8933F"/>
          <rect x="782" y="188" width="56" height="16" fill="#B8933F"/>
          <rect x="782" y="808" width="56" height="16" fill="#B8933F"/>
          <!-- Entablature top -->
          <rect x="100" y="76" width="500" height="10" fill="#B8933F"/>
          <rect x="95" y="66" width="510" height="12" fill="#B8933F"/>
          <!-- Arch -->
          <path d="M172 120 Q292 0 412 120" stroke="#B8933F" stroke-width="8" fill="none"/>
          <path d="M178 120 Q292 14 406 120" stroke="#B8933F" stroke-width="3" fill="none" opacity="0.4"/>
          <!-- Ground line -->
          <rect x="80" y="840" width="760" height="6" fill="#B8933F"/>
          <rect x="60" y="854" width="800" height="4" fill="#B8933F" opacity="0.5"/>
          <!-- Star in arch -->
          <polygon points="292,52 296,64 308,64 298,72 302,84 292,76 282,84 286,72 276,64 288,64" fill="#B8933F" opacity="0.8"/>
          <!-- Fluting lines on left column -->
          <line x1="132" y1="130" x2="132" y2="800" stroke="#D4AB5A" stroke-width="0.8" opacity="0.3"/>
          <line x1="140" y1="130" x2="140" y2="800" stroke="#D4AB5A" stroke-width="0.8" opacity="0.3"/>
          <line x1="148" y1="130" x2="148" y2="800" stroke="#D4AB5A" stroke-width="0.8" opacity="0.3"/>
          <line x1="156" y1="130" x2="156" y2="800" stroke="#D4AB5A" stroke-width="0.8" opacity="0.3"/>
          <!-- Fluting right column -->
          <line x1="592" y1="130" x2="592" y2="800" stroke="#D4AB5A" stroke-width="0.8" opacity="0.3"/>
          <line x1="600" y1="130" x2="600" y2="800" stroke="#D4AB5A" stroke-width="0.8" opacity="0.3"/>
          <line x1="608" y1="130" x2="608" y2="800" stroke="#D4AB5A" stroke-width="0.8" opacity="0.3"/>
          <line x1="616" y1="130" x2="616" y2="800" stroke="#D4AB5A" stroke-width="0.8" opacity="0.3"/>
        </svg>
      </div>
      <div class="hero-content">
        <div class="hero-era">Roma · Lazio · MMXXVI</div>
        <h1 class="hero-h1">
          <em>Il mercato di Roma.</em>
          <strong>2000 anni dopo.</strong>
        </h1>
        <div class="hero-rule"></div>
        <p class="hero-sub">Prodotti laziali artigianali selezionati dallo chef, consegnati nel tuo appartamento entro 48 ore. Carbonara, Amatriciana, Cacio e Pepe — kit completi per cucinare come un romano.</p>
        <div class="hero-ctas">
          <a href="?p=catalogo" class="btn-aurum">Scopri le Box</a>
          <a href="{wa_gen}" target="_blank" class="btn-ghost"><span class="dot">&#9679;</span> Ordina su WhatsApp</a>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # — Three Pillars —
    st.markdown("""
    <div class="pillars">
      <div class="pillar">
        <span class="pillar-num">I · SELEZIONE</span>
        <span class="pillar-icon">&#127963;&#65039;</span>
        <div class="pillar-title">Selezionato dallo chef</div>
        <div class="pillar-text">Ogni prodotto scelto personalmente tra i migliori produttori laziali — nessun catalogo generico, nessun compromesso.</div>
      </div>
      <div class="pillar">
        <span class="pillar-num">II · CONSEGNA</span>
        <span class="pillar-icon">&#128230;</span>
        <div class="pillar-title">Consegna in 48 ore</div>
        <div class="pillar-text">Direttamente nel tuo appartamento Airbnb — senza uscire, senza cercare, senza deludere.</div>
      </div>
      <div class="pillar">
        <span class="pillar-num">III · TERRITORIO</span>
        <span class="pillar-icon">&#127863;</span>
        <div class="pillar-title">Ingrediente laziale</div>
        <div class="pillar-text">Produttori locali, botteghe storiche, il territorio romano in ogni box — abbinato al vino della stessa terra.</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # — Preview 4 box —
    st.markdown("""
    <div class="sec-wrap bg-marble">
      <div class="sec-label">Le Box in Evidenza</div>
      <h2 class="sec-h2">A tavola con <em>Roma</em></h2>
      <p class="sec-sub">Le box più amate dai nostri ospiti. Ingredienti artigianali, ricetta dello chef, vino laziale abbinato.</p>
    </div>
    """, unsafe_allow_html=True)

    left_html = ""
    right_html = ""
    for i, box in enumerate(BOXES[:4]):
        price = box["prezzi"].get(persons) or (list(box["prezzi"].values())[0] if box["prezzi"] else None)
        ps = f"per {persons} person{'a' if persons==1 else 'e'}"
        stage_cls = "badge-estate" if "Estate" in box["stagione"] or "Stagionale" in box["stagione"] else "badge-always"
        vino_h = f'<div class="card-vino">&#8674; VINO ABBINATO &mdash; {box["vino"]}</div>' if box["vino"] else ""
        price_h = (f'<div class="card-price">&euro; {price}<span> {ps}</span></div>' if price
                   else '<div class="card-price-na">Prezzo su richiesta</div>')
        card = (
            f'<div class="card">'
            f'<div class="card-num">BOX {str(i+1).zfill(2)}</div>'
            f'<div class="card-head"><div class="card-name">{box["name"]}</div>'
            f'<span class="card-emoji">{box["emoji"]}</span></div>'
            f'<div class="card-tagline">{box["tagline"]}</div>'
            f'<span class="badge {stage_cls}">{box["stagione"]}</span>'
            f'<div class="card-desc">{box["desc"]}</div>'
            f'{vino_h}'
            f'<div class="card-rule"></div>'
            f'{price_h}'
            f'<a href="{wa_url(box["name"],persons)}" target="_blank" class="card-cta">Ordina su WhatsApp</a>'
            f'</div>'
        )
        if i % 2 == 0: left_html += card
        else: right_html += card

    st.markdown(f"""
    <div style="padding:0 80px;background:var(--marble,#F4F0E8);">
      <div class="cards-grid">
        <div>{left_html}</div>
        <div>{right_html}</div>
      </div>
      <div style="text-align:center;padding:36px 0 0;">
        <a href="?p=catalogo" style="font-family:'Cinzel',serif;font-size:10px;letter-spacing:3px;
           color:var(--ink,#2C2419);text-decoration:none;
           border-bottom:1px solid var(--aurum,#B8933F);padding-bottom:4px;">
          VEDI TUTTE LE 10 BOX &rarr;
        </a>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # — Manifesto —
    st.markdown("""
    <div class="manifesto bg-stone" style="background:#EDE7D9;">
      <p class="manifesto-text">Il Forum Romano era il mercato di Roma. 2000 anni fa, tutto il Lazio confluiva lì. FORVM riporta quel concetto nel 2026.</p>
      <div class="manifesto-attr">FORVM &mdash; Roma &middot; MMXXVI</div>
    </div>
    """, unsafe_allow_html=True)

    # — How it works —
    st.markdown(f"""
    <div class="sec-wrap bg-obsidian">
      <div class="sec-label" style="color:rgba(184,147,63,.7);">Il processo</div>
      <h2 class="sec-h2 light">Quattro passi verso <em>Roma</em></h2>
      <div class="steps">
        <div class="step">
          <span class="step-n">I</span>
          <div class="step-title">Scegli la box</div>
          <div class="step-text">Sfoglia il catalogo e scegli il tuo momento romano — colazione, pranzo, cena o dolce.</div>
        </div>
        <div class="step">
          <span class="step-n">II</span>
          <div class="step-title">Ordina su WhatsApp</div>
          <div class="step-text">Premi il bottone — il messaggio è già precompilato. Aggiungi solo l'indirizzo.</div>
        </div>
        <div class="step">
          <span class="step-n">III</span>
          <div class="step-title">Confermiamo</div>
          <div class="step-text">Ti rispondiamo entro 30 minuti. Scegli la fascia oraria: mattina 9-12 o pomeriggio 15-18.</div>
        </div>
        <div class="step" style="padding-right:0;">
          <span class="step-n">IV</span>
          <div class="step-title">Ricevi la box</div>
          <div class="step-text">Entro 48 ore — prodotti artigianali, ricetta dello chef, vino laziale abbinato.</div>
        </div>
      </div>
      <div style="margin-top:52px;text-align:center;">
        <a href="{wa_gen}" target="_blank" class="btn-aurum" style="display:inline-block;">Ordina Ora</a>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # — Box product image section —
    if BOX_B64:
        st.markdown(f"""
        <div class="sec-wrap bg-marble">
          <div class="chef-grid">
            <div class="chef-text">
              <div class="sec-label">La filosofia</div>
              <h2 class="sec-h2">Il meglio del <em>Lazio</em>, a casa tua</h2>
              <p>FORVM nasce da un'ossessione: trovare i prodotti laziali davvero eccezionali. Non i più famosi — i migliori. Guanciale di chi alleva i maiali nei monti di Amatrice. Pecorino Romano stagionato nei Castelli. Rigatoni trafilati al bronzo in piccoli pastifici di famiglia.</p>
              <div class="chef-quote">Non vendo prodotti laziali. Racconto il territorio romano attraverso ogni ingrediente.</div>
              <p>Ogni stagione la selezione si aggiorna con i migliori prodotti freschi. Non troverai mai lo stesso catalogo per 12 mesi.</p>
              <div style="margin-top:28px;">
                <a href="?p=catalogo" class="btn-aurum" style="display:inline-block;">Scopri il Catalogo</a>
              </div>
            </div>
            <div class="chef-img">
              <img src="data:image/jpeg;base64,{BOX_B64}" alt="Box FORVM" />
            </div>
          </div>
        </div>
        """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════
# CATALOGO
# ══════════════════════════════════════════════════════════════════
elif current_page == "catalogo":
    st.markdown("""
    <div class="sec-wrap bg-obsidian">
      <div class="sec-label" style="color:rgba(184,147,63,.7);">Catalogo completo</div>
      <h2 class="sec-h2 light">Le Box <em>FORVM</em></h2>
      <p class="sec-sub light">Scegli il tuo momento romano. Ordina su WhatsApp. Consegniamo entro 48 ore.</p>
    </div>
    """, unsafe_allow_html=True)

    # Person selector
    pers_html = ""
    for n in range(1, 6):
        ac = "active" if persons == n else ""
        pers_html += f'<a href="?p=catalogo&pers={n}" class="pers-btn {ac}">{n}</a>'

    st.markdown(f"""
    <div style="padding:32px 80px 0;background:var(--marble,#F4F0E8);">
      <div class="pers-bar">
        <span class="pers-bar-label">Persone a tavola</span>
        {pers_html}
      </div>
    </div>
    """, unsafe_allow_html=True)

    # All boxes
    left_html = ""
    right_html = ""
    for i, box in enumerate(BOXES):
        price = box["prezzi"].get(persons)
        if price is None and box["prezzi"]:
            available = box["prezzi"]
            price = available.get(min(available.keys(), key=lambda k: abs(k-persons)))
        ps = f"per {persons} person{'a' if persons==1 else 'e'}"

        stage_cls = ("badge-estate" if "Estate" in box["stagione"] else
                     "badge-stagionale" if "Stagionale" in box["stagione"] else
                     "badge-premium" if box.get("premium") else "badge-always")
        vino_h = f'<div class="card-vino">&#8674; VINO ABBINATO &mdash; {box["vino"]}</div>' if box["vino"] else ""
        price_h = (f'<div class="card-price">&euro; {price}<span> {ps}</span></div>' if price
                   else '<div class="card-price-na">Prezzo su richiesta &mdash; scrivici</div>')
        btn_cls = "card-cta premium-cta" if box.get("premium") else "card-cta"

        ing_items = "".join(f"<li>{ing}</li>" for ing in box["ingredienti"])
        ing_html = (
            f'<div class="ing-wrap">'
            f'<details class="ing-details">'
            f'<summary>&#8711; Ingredienti &amp; contenuto</summary>'
            f'<ul class="ing-list">{ing_items}</ul>'
            f'</details>'
            f'</div>'
        )

        card = (
            f'<div class="card">'
            f'<div class="card-num">BOX {str(i+1).zfill(2)}</div>'
            f'<div class="card-head">'
            f'<div><div class="card-name">{box["name"]}</div>'
            f'<div class="card-tagline">{box["tagline"]}</div></div>'
            f'<span class="card-emoji">{box["emoji"]}</span>'
            f'</div>'
            f'<span class="badge {stage_cls}">{box["stagione"]}</span>'
            f'<div class="card-desc">{box["desc"]}</div>'
            f'{ing_html}'
            f'{vino_h}'
            f'<div class="card-rule"></div>'
            f'{price_h}'
            f'<a href="{wa_url(box["name"],persons)}" target="_blank" class="{btn_cls}">Ordina su WhatsApp</a>'
            f'</div>'
        )
        if i % 2 == 0: left_html += card
        else: right_html += card

    st.markdown(f"""
    <div style="padding:24px 80px 80px;background:var(--marble,#F4F0E8);">
      <div class="cards-grid">
        <div>{left_html}</div>
        <div>{right_html}</div>
      </div>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════
# COME FUNZIONA
# ══════════════════════════════════════════════════════════════════
elif current_page == "come_funziona":
    st.markdown(f"""
    <div class="sec-wrap bg-obsidian">
      <div class="sec-label" style="color:rgba(184,147,63,.7);">Il processo</div>
      <h2 class="sec-h2 light">Come funziona <em>FORVM</em></h2>
      <p class="sec-sub light">Quattro passi — dall'ordine al tuo tavolo romano.</p>
      <div class="steps">
        <div class="step">
          <span class="step-n">I</span>
          <div class="step-title">Scegli la box</div>
          <div class="step-text">Sfoglia il catalogo e scegli la box per il tuo momento romano — colazione, pranzo, cena, aperitivo o dolce.</div>
        </div>
        <div class="step">
          <span class="step-n">II</span>
          <div class="step-title">Ordina su WhatsApp</div>
          <div class="step-text">Premi il bottone WhatsApp — trovi già il messaggio precompilato con la box scelta. Aggiungi solo il tuo indirizzo.</div>
        </div>
        <div class="step">
          <span class="step-n">III</span>
          <div class="step-title">Confermiamo la consegna</div>
          <div class="step-text">Ti rispondiamo entro 30 minuti. Scegli la fascia oraria — mattina 9-12 o pomeriggio 15-18.</div>
        </div>
        <div class="step" style="padding-right:0;">
          <span class="step-n">IV</span>
          <div class="step-title">Ricevi la tua box</div>
          <div class="step-text">Entro 48 ore — prodotti artigianali, scheda ricetta dello chef, vino laziale abbinato. Apri e inizia.</div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="sec-wrap bg-marble">
      <div class="sec-label">Informazioni pratiche</div>
      <h2 class="sec-h2">Tutto quello che devi sapere</h2>
      <div class="info-tiles">
        <div class="info-tile">
          <span class="info-tile-icon">&#128179;</span>
          <div class="info-tile-title">Come si paga</div>
          <div class="info-tile-text">Satispay o PayPal prima della consegna. Pagamento anticipato obbligatorio.</div>
        </div>
        <div class="info-tile">
          <span class="info-tile-icon">&#127758;</span>
          <div class="info-tile-title">Parliamo la tua lingua</div>
          <div class="info-tile-text">Gestiamo le comunicazioni in italiano e inglese. Non serve parlare italiano per ordinare.</div>
        </div>
        <div class="info-tile" style="border-top-color:#25D366;">
          <span class="info-tile-icon">&#9889;</span>
          <div class="info-tile-title">Garanzia rimborso</div>
          <div class="info-tile-text">Se qualcosa non va — rimborso immediato senza discussioni. Scrivici su WhatsApp.</div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    faqs = [
        ("Devo essere in casa quando consegnate?", "Sì, se non hai una safe box. Ti chiediamo una fascia oraria di 2 ore — la sera prima ti confermiamo con un messaggio WhatsApp."),
        ("Qual è il tempo minimo di preavviso?", "24 ore. Per consegne urgenti scrivici su WhatsApp e vediamo cosa possiamo fare."),
        ("Posso ordinare più box insieme?", "Sì — una sola consegna per tutti gli ordini dello stesso giorno."),
        ("Posso ordinare se non parlo italiano?", "Sì. Gestiamo le comunicazioni in italiano e inglese."),
        ("Come pago?", "Satispay o PayPal prima della consegna. Pagamento anticipato obbligatorio."),
        ("Cosa succede se qualcosa non va?", "Rimborso immediato senza discussioni. Scrivici su WhatsApp."),
    ]
    faq_html = "".join(
        f'<div class="faq-item"><div class="faq-q">{q}</div><div class="faq-a">{a}</div></div>'
        for q, a in faqs
    )
    wa_faq = f"https://wa.me/{WHATSAPP_NUMBER}?text=Ciao%20FORVM!%20Ho%20una%20domanda."
    st.markdown(f"""
    <div class="sec-wrap bg-stone">
      <div class="sec-label">FAQ</div>
      <h2 class="sec-h2">Domande frequenti</h2>
      <div style="margin-top:32px;">{faq_html}</div>
      <div style="margin-top:48px;text-align:center;">
        <a href="{wa_faq}" target="_blank" class="btn-aurum" style="display:inline-block;">Hai un'altra domanda?</a>
      </div>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════
# CHI SIAMO
# ══════════════════════════════════════════════════════════════════
elif current_page == "chi_siamo":
    wa_chi = f"https://wa.me/{WHATSAPP_NUMBER}?text=Ciao%20FORVM!"
    st.markdown(f"""
    <div class="sec-wrap bg-marble">
      <div class="sec-label">Chi seleziona</div>
      <h2 class="sec-h2">La persona dietro <em>FORVM</em></h2>
      <div class="chef-grid">
        <div class="chef-text">
          <p>FORVM nasce da un'ossessione professionale: trovare i prodotti laziali davvero eccezionali. Non i più famosi o i più promossi — i migliori, quelli che meritano di essere portati sulla tavola di chi visita Roma per la prima volta o per la centesima.</p>
          <div class="chef-quote">Il Forum Romano era il mercato di Roma. 2000 anni fa, tutto il Lazio confluiva lì. FORVM riporta quel concetto nel 2026 — il meglio del territorio laziale, consegnato dove sei.</div>
          <p>Ogni prodotto nella nostra selezione è scelto personalmente — visitando i produttori nei Castelli Romani, nei monti di Amatrice, nelle colline della Ciociaria.</p>
          <p>La selezione cambia ogni stagione, seguendo i ritmi del territorio. L'estate porta la Caprese Laziale con i pomodori di Fondi. L'autunno porta i funghi porcini dei Simbruini.</p>
          <div style="margin-top:28px;">
            <a href="{wa_chi}" target="_blank" class="btn-aurum" style="display:inline-block;">Scrivici su WhatsApp</a>
          </div>
        </div>
        {'<div class="chef-img"><img src="data:image/jpeg;base64,' + BOX_B64 + '" alt="Box FORVM"/></div>' if BOX_B64 else '<div></div>'}
      </div>
    </div>
    """, unsafe_allow_html=True)

    prod_data = [
        ("&#129385;","Norcineria Jacovone","Amatrice · RI","Guanciale, salumi stagionati"),
        ("&#129472;","Caseificio Bernardi","Castelli Romani · RM","Pecorino Romano DOP, ricotta"),
        ("&#127863;","Cantina Casale del Giglio","Aprilia · LT","Vini laziali DOCG e DOC"),
        ("&#129388;","Oleificio Colli Sabini","Sabina · RI","Olio EVO DOP, olive da mensa"),
    ]
    prod_html = "".join(
        f'<div class="producer">'
        f'<span class="producer-icon">{icon}</span>'
        f'<div class="producer-name">{name}</div>'
        f'<span class="producer-loc">{loc}</span>'
        f'<div class="producer-prod">{prod}</div>'
        f'</div>'
        for icon, name, loc, prod in prod_data
    )
    st.markdown(f"""
    <div class="sec-wrap bg-stone">
      <div class="sec-label">I nostri produttori</div>
      <h2 class="sec-h2">Le radici del territorio</h2>
      <p class="sec-sub">Non selezioniamo brand — selezioniamo persone.</p>
      <div class="producers">{prod_html}</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="sec-wrap bg-obsidian">
      <div class="sec-label" style="color:rgba(184,147,63,.7);">Stagione corrente</div>
      <h2 class="sec-h2 light">La selezione <em>Estate 2026</em></h2>
      <p class="sec-sub light">Ogni stagione FORVM collabora con uno chef laziale per aggiornare la selezione con i prodotti freschi del momento. L'estate 2026 porta nuovi produttori della costa laziale e delle colline pontine.</p>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════
# PARTNER
# ══════════════════════════════════════════════════════════════════
elif current_page == "partner":
    wa_host = f"https://wa.me/{WHATSAPP_NUMBER}?text=Ciao%20FORVM!%20Sono%20un%20host%20Airbnb%20e%20vorrei%20diventare%20partner."
    st.markdown(f"""
    <div class="hero" style="min-height:55vh;">
      <div class="hero-columns">
        <svg class="col-svg" viewBox="0 0 900 900" preserveAspectRatio="xMaxYMax meet" fill="none" xmlns="http://www.w3.org/2000/svg">
          <rect x="120" y="120" width="52" height="700" fill="#B8933F"/>
          <rect x="110" y="105" width="72" height="22" fill="#B8933F"/>
          <rect x="580" y="120" width="52" height="700" fill="#B8933F"/>
          <rect x="570" y="105" width="72" height="22" fill="#B8933F"/>
          <path d="M172 120 Q292 0 412 120" stroke="#B8933F" stroke-width="8" fill="none"/>
          <rect x="80" y="840" width="760" height="6" fill="#B8933F"/>
          <line x1="132" y1="130" x2="132" y2="800" stroke="#D4AB5A" stroke-width="0.8" opacity="0.3"/>
          <line x1="148" y1="130" x2="148" y2="800" stroke="#D4AB5A" stroke-width="0.8" opacity="0.3"/>
          <line x1="592" y1="130" x2="592" y2="800" stroke="#D4AB5A" stroke-width="0.8" opacity="0.3"/>
          <line x1="608" y1="130" x2="608" y2="800" stroke="#D4AB5A" stroke-width="0.8" opacity="0.3"/>
        </svg>
      </div>
      <div class="hero-content">
        <div class="hero-era">Per gli host Airbnb</div>
        <h1 class="hero-h1"><em>Porta Roma</em><strong>sulla tavola dei tuoi ospiti.</strong></h1>
        <div class="hero-rule"></div>
        <p class="hero-sub">Commissione automatica del 10% su ogni ordine generato dai tuoi ospiti. Zero gestione da parte tua.</p>
        <div class="hero-ctas">
          <a href="{wa_host}" target="_blank" class="btn-aurum">Diventa partner</a>
          <a href="mailto:info@forvm.roma" class="btn-ghost">&#9679; info@forvm.roma</a>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="sec-wrap bg-marble">
      <div class="sec-label">Perché conviene</div>
      <h2 class="sec-h2">Tre buone ragioni</h2>
      <div class="benefits">
        <div class="benefit">
          <span class="benefit-icon">&#128176;</span>
          <div class="benefit-title">Commissione 10%</div>
          <div class="benefit-text">Ogni volta che un tuo ospite ordina, ricevi il 10% automaticamente. Su una Carbonara da €28, guadagni €2.80 senza fare nulla.</div>
        </div>
        <div class="benefit">
          <span class="benefit-icon">&#128715;</span>
          <div class="benefit-title">Zero gestione</div>
          <div class="benefit-text">Tu metti il biglietto nell'appartamento. Noi facciamo tutto il resto — ordini, pagamenti, consegne, problemi.</div>
        </div>
        <div class="benefit">
          <span class="benefit-icon">&#11088;</span>
          <div class="benefit-title">Ospiti più soddisfatti</div>
          <div class="benefit-text">Un ospite che cucina la Carbonara con i prodotti giusti parla bene dell'appartamento. La tua recensione cresce.</div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # Commission table
    rows_html = ""
    for i, box in enumerate(BOXES[:9]):
        bg = ""
        p1 = f"&euro; {box['prezzi'].get(1,'&mdash;')}"
        p2 = f"&euro; {box['prezzi'].get(2,'&mdash;')}"
        p3 = f"&euro; {box['prezzi'].get(3,'&mdash;')}"
        comm = box['prezzi'].get(2, 0)
        comm_str = f'<span class="comm-val">&euro; {comm*0.1:.1f}</span>' if comm else '&mdash;'
        rows_html += (
            f'<tr><td>{box["emoji"]} {box["name"]}</td>'
            f'<td>{p1}</td><td>{p2}</td><td>{p3}</td>'
            f'<td>{comm_str}</td></tr>'
        )

    st.markdown(f"""
    <div class="sec-wrap bg-stone">
      <div class="sec-label">Commissioni</div>
      <h2 class="sec-h2">Quanto guadagni</h2>
      <p class="sec-sub">10% su ogni ordine generato dai tuoi ospiti — calcolato automaticamente a fine mese.</p>
      <div style="overflow-x:auto;margin-top:32px;">
        <table class="partner-table">
          <thead><tr>
            <th style="text-align:left;">Box</th>
            <th>1 persona</th><th>2 persone</th><th>3 persone</th>
            <th style="color:var(--aurum-lt,#D4AB5A);">Commissione (2p)</th>
          </tr></thead>
          <tbody>{rows_html}</tbody>
        </table>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # Contact form
    st.markdown("""
    <div class="sec-wrap bg-obsidian">
      <div class="sec-label" style="color:rgba(184,147,63,.7);">Inizia ora</div>
      <h2 class="sec-h2 light">Diventare partner è <em>semplice</em></h2>
      <p class="sec-sub light">Compila il form oppure scrivici direttamente su WhatsApp — ti rispondiamo entro un'ora.</p>
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
        submitted = st.form_submit_button("Invia richiesta di partnership", use_container_width=True)
        if submitted:
            if nome and whatsapp_num:
                st.success(f"Grazie {nome}. Ti contatteremo al numero {whatsapp_num} entro 24 ore.")
            else:
                st.error("Inserisci nome e WhatsApp per continuare.")

    st.markdown(f"""
    <div class="sec-wrap bg-marble" style="text-align:center;padding-top:40px;padding-bottom:40px;">
      <a href="{wa_host}" target="_blank" class="btn-aurum" style="display:inline-block;">&#128241; Scrivimi su WhatsApp</a>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════
# FOOTER
# ══════════════════════════════════════════════════════════════════
wa_footer = f"https://wa.me/{WHATSAPP_NUMBER}?text=Ciao%20FORVM!"
st.markdown(f"""
<footer class="forvm-footer">
  <div class="footer-grid">
    <div>
      <div class="footer-brand">FORVM</div>
      <div class="footer-tagline">Il mercato di Roma. 2000 anni dopo.<br>Prodotti laziali artigianali selezionati dallo chef,<br>consegnati nel tuo appartamento entro 48 ore.</div>
    </div>
    <div>
      <div class="footer-col-title">Pagine</div>
      <div class="footer-links">
        <a href="?p=home">Home</a>
        <a href="?p=catalogo">Catalogo Box</a>
        <a href="?p=come_funziona">Come Funziona</a>
        <a href="?p=chi_siamo">Chi Siamo</a>
        <a href="?p=partner">Partnership Host</a>
      </div>
    </div>
    <div>
      <div class="footer-col-title">Contatti</div>
      <div class="footer-links">
        <a href="{wa_footer}" target="_blank">WhatsApp</a>
        <a href="https://instagram.com/forvm.roma" target="_blank">@forvm.roma</a>
        <a href="mailto:info@forvm.roma">info@forvm.roma</a>
        <a href="#">Privacy Policy</a>
      </div>
    </div>
  </div>
  <hr class="footer-rule"/>
  <div class="footer-copy">
    <span>&copy; 2026 FORVM &middot; Roma</span>
    <span>Selezionato dallo chef &middot; Consegnato a casa tua</span>
  </div>
</footer>
<a href="{wa_footer}" target="_blank" class="wa-float">
  <span class="wa-float-icon">&#128172;</span>
  <span>Ordina ora</span>
</a>
""", unsafe_allow_html=True)
