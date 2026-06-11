# Design System & Visual Identity: FORVM

Questo documento illustra le direttive visive e i pattern di design estratti direttamente dal file `forvm.py`. L'identità dell'applicazione non è un template generico, ma è modellata sul concetto del "Lapidario Romano", utilizzando architetture classiche, marmi e oro.

## Identità Visiva e Colori (Root Tokens)
La palette colori è codificata nelle variabili CSS `:root` e si basa su toni materici, pietre romane e inchiostri scuri per un elevato contrasto ed eleganza.

* **Marmi (Sfondi principali e Card):**
    * `--marble`: `#F4F0E8` (Sfondo base corpo e card)
    * `--marble-mid`: `#EDE7D9` (Sezioni di stacco, es. Manifesto)
    * `--marble-dk`: `#E0D8C8`
* **Pietra / Travertino (Bordi e sfondi secondari):**
    * `--travertine`: `#D4C9B0`
    * `--stone`: `#A89880`
    * `--stone-dk`: `#7A6B5A`
* **Oro (Accenti, Call to Action, Loghi):**
    * `--aurum`: `#B8933F` (Colore primario del brand)
    * `--aurum-lt`: `#D4AB5A`
    * `--aurum-dk`: `#8B6B28`
* **Ossidiana e Inchiostro (Testi e Navbar):**
    * `--obsidian`: `#1A1612` (Sfondo Navbar, Hero, Sezioni scure)
    * `--ink`: `#2C2419` (Testo principale)
    * `--ink-mid`: `#4A3F32`
    * `--ink-lt`: `#6B5C4A`
* **Azione Esterna:**
    * `--wa`: `#25D366` (Bottone WhatsApp)

## Tipografia (Type Scale)
La gerarchia dei font riflette la monumentalità romana e la leggibilità moderna:
1.  **H1, H2, H3 (Titoli monumentali):** `Cormorant Garamond`, serif. Usato per i pesi visivi principali (es. *Il mercato di Roma*, nomi delle Box).
2.  **Etichette, Numeri Lapidari, Logo:** `Cinzel`, serif. Usato per elementi strutturali, badge (`BOX 01`, `I · SELEZIONE`) e bottoni primari. Tutto in maiuscolo, con forte `letter-spacing` (3px - 8px).
3.  **Corpo del testo (Descrizioni, ingredienti):** `DM Sans`, sans-serif. Leggero (`font-weight: 300` e `400`), alta leggibilità.

## Pattern Architetturali (Componenti)

### 1. La Sezione Hero (Il Colonnato)
L'app si apre non con una fotografia, ma con un'illustrazione vettoriale (SVG) di un arco e un colonnato romano renderizzati direttamente nel markup, fusi con un gradiente obliquo e un overlay a texture di marmo. Questa sezione domina la pagina e fissa immediatamente il posizionamento del prodotto: storico, lussuoso, romano.

### 2. Struttura "Lapidaria" delle Card (Il Catalogo)
Le `box-card` seguono una struttura a blocco di marmo:
* Sfondo `--marble`.
* Un `hover` state che rivela una fessura dorata superiore (bordo superiore sfumato `linear-gradient`).
* **Badge Stagionali "Scalpellati":** Badges monolitici come `badge-estate` (Sfondo `#FFF4D6`, testo `#7A5800`) o `badge-premium` (Sfondo `--ink`, testo `--aurum`).
* **Ingredienti (Accordion):** Una lista di ingredienti nascosta dietro un `<details>/<summary>` minimale, decorata con un puntino dorato (`·`) tramite pseudo-elemento `::before`.

### 3. I Pulsanti
* **`btn-aurum`**: Pulsante solido in oro con testo ossidiana, font Cinzel maiuscolo. Call to Action primaria del sito.
* **`btn-ghost`**: Pulsante trasparente con bordo sottile, usato in accompagnamento sulla hero.
* **`wa-float` & `nav-wa`**: Pulsanti funzionali verde WhatsApp, spezzano la palette classica per guidare l'utente verso l'azione di acquisto concreta.

### 4. Navigazione a Stati (Il Selettore Persone)
Invece di classici menu a tendina di Streamlit (che vengono nascosti via CSS `display: none!important`), l'interfaccia utilizza una `pers-bar` custom: bottoni a blocco stile tab (1, 2, 3, 4, 5 persone) che ricaricano la pagina modificando programmaticamente l'URL query e ricalcolando i prezzi estratti dal dizionario Python.