# FORVM 🏛️

**Il mercato di Roma. 2000 anni dopo.**
*Prodotti Laziali Artigianali · Consegna 48h Roma*

## Scopo del Progetto
FORVM è un'applicazione web sviluppata in Streamlit che offre un servizio di consegna di box gastronomiche artigianali. Il servizio è pensato per i turisti e i viaggiatori che alloggiano in appartamenti o case vacanze a Roma, permettendo loro di cucinare le ricette della tradizione romana (Carbonara, Amatriciana, Cacio e Pepe, ecc.) con ingredienti locali autentici, selezionati da uno chef e consegnati entro 48 ore.

L'applicazione funge da vetrina, catalogo dinamico e portale per host partner, reindirizzando tutti gli ordini verso un sistema di messaggistica diretta su WhatsApp.

## File Critici e Struttura

L'intera applicazione è un'architettura monolitica contenuta in un singolo file:
* **`forvm.py`**: Il cuore dell'applicazione. Gestisce il routing delle pagine tramite query parameters (`st.query_params`), lo stato della sessione (numero di persone a tavola), il database in memoria dei prodotti (`BOXES`), e l'intero strato visivo (CSS personalizzato iniettato via `st.markdown`).

## Dati e Logica di Core (Il Catalogo)
L'applicazione prende la sua forma dalla struttura dati principale, una lista di dizionari chiamata `BOXES`. Ogni box definisce l'offerta di prodotto:
* `id`, `name`, `emoji`, `tagline`, `desc`: Metadati di presentazione.
* `ingredienti`: Array di stringhe che popola i menu a tendina (es. *"Guanciale DOP di Amatrice (100g a persona)"*).
* `prezzi`: Un dizionario dinamico (es. `{1: 18, 2: 28, 3: 38}`) che scala in base alla selezione dell'utente (parametro `pers`).
* `stagione`, `vino`, `premium`: Etichette di catalogazione e abbinamento.

L'azione principale del sito è la funzione `wa_url(box_name, n)`, che genera un URL WhatsApp precompilato (es. *"Ciao FORVM! Vorrei ordinare La Carbonara per 2 persone..."*) trasformando il sito in un funnel di conversione diretto.

## Obiettivi e Sezioni Principali
1.  **Home & Catalogo**: Guidare l'utente verso la selezione della box, calcolando i prezzi in tempo reale in base al numero di ospiti.
2.  **Come Funziona**: Spiegare il processo in 4 fasi lapidarie (Scegli, Ordina, Conferma, Ricevi) e gestire le FAQ e le policy di pagamento (Satispay/PayPal).
3.  **Chi Siamo**: Raccontare il territorio e la filiera corta mostrando i produttori reali (es. *Norcineria Jacovone*, *Caseificio Bernardi*).
4.  **Per gli Host (Partnership)**: Un modulo dedicato ai gestori di case vacanza per generare una rendita passiva (commissione automatica del 10% calcolata programmaticamente dalla tabella prezzi).