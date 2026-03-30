# Terminologiai stiluslap / Terminology Style Sheet

Ez a dokumentum rogziti a konyv egeszeben kovetendo terminologiai donteseket. Celja a Hunglish minimalizalasa, a terminologiai kovetkezetesseg biztositasa es a celkozonseg (nem-programozo magyar kutatók) kiszolgalasa.

---

## 1. Altalanos szabalyok

- **Elso elofordulaskor** mindig add meg az angol terminust zarojelben: *agensek (agents)*.
- Utana hasznaald kovetkezetesen a valasztott magyar formaat.
- Ha a magyar terminus nem terjedt el, az angol forma maradhat, de *kurzivval* jelolve.

---

## 2. Preferalt magyar terminusok (magyar forma hasznalando a szovegben)

| Angol | Preferalt magyar | Kerulendo | Megjegyzes |
|-------|-----------------|-----------|------------|
| agent | **agens** | agent (fonevre) | Jelzoi hasznalat: "agensaalapu", "agensszeru" |
| agentic AI | **agensaalapu AI** | agentic AI (fonevre) | Jelzoi: "agensszeru AI" is elfogadhato |
| hallucination | **hallucianció** | — | Meghonosodott magyar forma |
| prompt | **prompt** | promptolas → OK igeként | Fonev marad angolul; az igesitett "promptolás" elfogadhato |
| fine-tuning | **finomhangolas** | fine-tuning (fuutó szovegben) | Elso elofordulaas: "finomhangolas (fine-tuning)" |
| embedding | **embedding** | beagyazas | A termeszetes nyelvi kontextusban az "embedding" termjedt el |
| token | **token** | zseton | Meghonosodott forma |
| context window | **kontextusablak** | context window (futo szovegben) | |
| chain of thought | **gondolati lancolat** | — | Elso elofordulas: "gondolati lancolat (Chain of Thought)" |
| retrieval-augmented generation | **RAG** | — | Betuszot hasznalunk; elso elofordulas: teljes kifejtéss |
| digital twin | **digitalis iker** | digitalis ikerpaar | |
| workflow | **munkafolyamat** | workflow (futo szovegben) | Technikai kontextusban "workflow" elfogadhato |
| dashboard | **dashboard** | muszerfalat | Meghonosodott angol forma |
| node | **node** / **csomopont** | — | Vizualis programozasi kontextusban mindketto jo |
| adoption | **elterjedes** / **elfogadas** | adoptacio | Tipikus rossz tukorforditas |
| curriculum | **tanterv** / **kepzesi struktura** | curriculum (futo szovegben) | |
| disruptive | **attoro** | diszruptiv | |

---

## 3. Mindig angolul marrado terminusok

Ezek a terminusok annyira bevettek, hogy magyaritasuk zavart okozna:

- **AI** (nem MI — lasd kovetkezo szekció)
- **API**
- **CSV**, **JSON**, **PDF**
- **Python**, **Git**, **GitHub**
- **ChatGPT**, **Claude**, **Gemini**, **Copilot**
- **KNIME**, **n8n**, **LangFlow**, **LangGraph**, **CrewAI**
- **Streamlit**, **Gradio**
- **RAG**
- **pipeline** (technikai terminus; magyarazo kontextusban "adatfeldolgozasi csovezeték" is hasznalhato)
- **MCP** (Model Context Protocol)
- **CUDA**, **GPU**, **CPU**
- **Docker**, **Kubernetes**
- **Markdown**
- **NDVI**, **DEM**, **GIS**
- **prompt**
- **token**
- **embedding**
- **dashboard**

---

## 4. AI vs. MI dontes

A konyvben kovetkezetesen **AI**-t hasznalunk, nem MI-t.

**Indoklas:**
- A magyar tudomanyos kozbeszeadben az "AI" erosebb es elterjedtebb.
- A celkozonseg (kutatók, oktatók) nemzetkozi kontextusban dolgozik, ahol az "AI" az egyertelmu.
- Az "MI" formaalisan helyes, de a konyv hangnemeehez es celkozonseegehez az "AI" illeszkedik jobban.
- Elso elofordulaskor (1. fejezet): "Mesterseges intelligencia (MI, angolul: Artificial Intelligence, AI)" — utana kovetkezetesen AI.

---

## 5. Kerulendo tukorforditasok (tiltolista)

| Rossz forma | Helyes alternativa |
|-------------|-------------------|
| adoptacio | elterjedes, elfogaadas, bevezetes |
| curriculumban | tantervben, kepzesi strukturaban |
| diszruptiv | attoro, alapvetoen uj |
| enable-olni | lehetove tenni |
| in-kind hozzaajarulas | termeszetbeni hozzajarulas |
| tutored | — (elutes/nyers angol; torolni vagy atirni) |
| implement-alni | megvalositani, bevezetni |

---

## 6. Osszeteett terminusok irásmodja

- **AI-alapu** (kotojeles)
- **AI-tamogatott** (kotojeles)
- **no-code** (kotojeles, angol marad)
- **open source** / **nyilt forraskodu** (mindketto elfogadhato; legyel kovetkezetes egy fejezeten belul)

---

## 7. Hasznalati utmutato

1. Uj terminus bevezetesekor mindig hasznald az "**magyar** (*angol*)" formatumot.
2. Egy fejezeten belul ne valtogass ket forma kozott (pl. ne ird egyszer "agensnek", egyszer "agent"-nek).
3. Ha bizonytalaan vagy, nezd meg a glosszariumot (glossary.md) — a ket dokumentumnak konzisztensnek kell lennie.
4. A szektoraalis fejezetekben (17-19) a szakteriuleti terminologia (pl. NDVI, Boussinesq-egyenlet, EOV) marad a szakma szokaasos formajaban.
