# 12. fejezet: AI ágensek építése kutatáshoz

---

## 12.1 Amikor a hétfő reggeli irodalomkutatás három napot vesz el

Képzeld el a következő helyzetet. Dr. Tóth Gábor, a Debreceni Egyetem Környezettudományi Intézetének csoportvezetője minden hétfőn ugyanazt csinálja: leül a gép elé, megnyitja a PubMed-et, a Web of Science-t és a Google Scholart, és végigszűri az előző hét publikációit. A kutatócsoportja talajszennyezéssel foglalkozik, azon belül is nehézfémek bioremediációjával --- egy gyorsan mozgó terület, ahol havonta több száz új cikk jelenik meg.

A szűrés önmagában nem lenne baj. De aztán jön az olvasás: az absztraktok átnézése, a releváns cikkek letöltése, a kulcsfontosságú eredmények kijegyzetelése, és végül az egész összefoglalása a csoportértekezletre. Ami elméletben „néhány órás feladat" lenne, a gyakorlatban rendszeresen kedden délutánig tart. Néha szerdáig. És közben a saját kutatása, a PhD-hallgatói mentorálása és a pályázatírás mind várakozik.

Egy nap Gábor megkérdezi az egyik informatikus kollégáját: „Nem lehetne ezt valahogy automatizálni? Mondjuk, egy AI, ami hétfő reggel megnézi az új cikkeket, elolvassa az absztraktokat, kiválogatja a relevánsat, és ír nekem egy összefoglalót?"

A kolléga mosolyog. „Ez pontosan az, amire az AI ágensek valók."

Ez a fejezet arról szól, hogyan építhetsz ilyen ágenseket --- és ennél sokkal összetettebbeket is --- a saját kutatásodhoz. Az előző fejezetben megismerkedtél az ágensek elméletével: tudod, mi az a ReACT ciklus, mire jó az MCP, hogyan működik a multi-agent koordináció. Most felgyűrjük az ingujjunkat és **építünk**.

---

## 12.2 Ágenskeretrendszerek tudósoknak --- az összehasonlítás

Az elmúlt két évben robbanásszerűen nőtt az ágens-keretrendszerek száma. Ez egyszerre jó hír (van választék) és rossz hír (nehéz eligazodni). Ebben a szekcióban összehasonlítjuk a négy legfontosabb keretrendszert, amelyek tudományos munkához a legalkalmasabbak, és segítünk kiválasztani, melyik illik hozzád.

### 12.2.1 CrewAI --- Szerep-alapú ágens-csapatok

**Mi ez?** A CrewAI egy Python keretrendszer, amelyben **szerepeket** (role) definiálsz az ágenseidnek, **feladatokat** (task) adsz nekik, és **csapatba** (crew) szervezed őket. Az ágensek ezután automatikusan együttműködnek a feladatok végrehajtásán.

**Miért jó tudósoknak?** Mert a gondolkodásmódja megfelel annak, ahogy egy kutatócsoport működik. Van egy kereső, van egy elemző, van egy szintetizáló --- mindenki tudja a dolgát, és az eredmények összefutnak.

**Telepítés:**

```bash
pip install crewai crewai-tools
```

**Alap koncepciók:**

```
┌─────────────────────────────────────────────────┐
│                    CREW                          │
│  (csapat --- az ágensek koordinátora)            │
│                                                  │
│  ┌──────────┐  ┌──────────┐  ┌──────────────┐  │
│  │  AGENT 1 │  │  AGENT 2 │  │   AGENT 3    │  │
│  │ Kereső   │  │ Olvasó   │  │ Szintetizáló │  │
│  │          │  │          │  │              │  │
│  │ role     │  │ role     │  │  role        │  │
│  │ goal     │  │ goal     │  │  goal        │  │
│  │ backstory│  │ backstory│  │  backstory   │  │
│  └────┬─────┘  └────┬─────┘  └──────┬───────┘  │
│       │              │               │           │
│  ┌────▼─────┐  ┌────▼─────┐  ┌──────▼───────┐  │
│  │  TASK 1  │  │  TASK 2  │  │   TASK 3     │  │
│  │ Keresés  │  │ Elemzés  │  │ Összefoglalás│  │
│  └──────────┘  └──────────┘  └──────────────┘  │
└─────────────────────────────────────────────────┘
```

A CrewAI három működési módot támogat:

| Mód | Leírás | Mikor használd? |
|-----|--------|----------------|
| **Sequential** | Az ágensek sorban dolgoznak, az előző kimenete a következő bemenete | Irodalomkutatás, pipeline jellegű feladatok |
| **Hierarchical** | Egy menedzser-ágens osztja ki és felügyeli a feladatokat | Összetett projektek, ahol dönteni kell a sorrendről |
| **Consensual** | Az ágensek megbeszélik és közösen döntik el a megoldást | Értékelési, review típusú feladatok |

A részletes CrewAI példát a 12.3-as szekcióban találod --- ott egy teljes irodalomkutató ágens-csapatot építünk lépésről lépésre.

---

### 12.2.2 LangGraph --- Gráf-alapú munkafolyamatok

**Mi ez?** A LangGraph a LangChain csapat terméke, amely **gráfként** modellezi az ágens-munkafolyamatokat. A gráf csomópontjai (node) a műveletek, az élei (edge) a kapcsolatok, és a teljes rendszer állapotát (state) egy strukturált objektum tárolja.

**Miben különbözik a CrewAI-tól?** A CrewAI-ban szerepeket definiálsz és a keretrendszer intézi a koordinációt. A LangGraph-ban te rajzolod meg a teljes munkafolyamatot --- pontosan te döntöd el, melyik lépés után mi következik, milyen feltételek mellett melyik ágra lép a rendszer, és hol van ciklus (loop).

**Mikor válaszd?**

- Amikor a munkafolyamatod **nem lineáris**: vannak elágazások, feltételes utak, visszalépések
- Amikor **pontos kontrollt** akarsz minden lépés felett
- Amikor a feladatod megköveteli az **állapot-kezelést** --- például egy iteratív elemzés, ahol az ágens addig finomítja az eredményt, amíg egy minőségi küszöböt el nem ér

**Telepítés:**

```bash
pip install langgraph langchain-openai
```

**Egy egyszerű példa --- adatellenőrző ágens:**

```python
from langgraph.graph import StateGraph, END
from typing import TypedDict

class AnalysisState(TypedDict):
    raw_data: str
    cleaned_data: str
    quality_score: float
    report: str

def clean_data(state: AnalysisState) -> dict:
    """Adattisztítás LLM-mel."""
    # Az LLM megtisztítja és strukturálja a nyers adatot
    cleaned = llm.invoke(f"Tisztítsd meg ezt az adatsort: {state['raw_data']}")
    return {"cleaned_data": cleaned.content}

def check_quality(state: AnalysisState) -> dict:
    """Minőségellenőrzés."""
    score = llm.invoke(f"Értékeld 0-1 skálán: {state['cleaned_data']}")
    return {"quality_score": float(score.content)}

def generate_report(state: AnalysisState) -> dict:
    """Jelentés generálása."""
    report = llm.invoke(f"Írj elemzést: {state['cleaned_data']}")
    return {"report": report.content}

def route_by_quality(state: AnalysisState) -> str:
    """Ha a minőség alacsony, vissza a tisztításhoz."""
    if state["quality_score"] < 0.8:
        return "clean_data"    # Újratisztítás
    return "generate_report"   # Tovább a jelentéshez

# Gráf felépítése
graph = StateGraph(AnalysisState)
graph.add_node("clean_data", clean_data)
graph.add_node("check_quality", check_quality)
graph.add_node("generate_report", generate_report)

graph.set_entry_point("clean_data")
graph.add_edge("clean_data", "check_quality")
graph.add_conditional_edges("check_quality", route_by_quality)
graph.add_edge("generate_report", END)

app = graph.compile()
```

Ez a gráf így néz ki vizuálisan:

```
    ┌────────────┐
    │ clean_data │◄──────────────┐
    └─────┬──────┘               │
          ▼                      │
   ┌──────────────┐     minőség  │
   │check_quality │──── < 0.8 ───┘
   └──────┬───────┘
          │ minőség >= 0.8
          ▼
  ┌────────────────┐
  │generate_report │
  └───────┬────────┘
          ▼
        [END]
```

A lényeg: a LangGraph-ban **te vagy az építész**. Ez nagyobb szabadságot ad, de több munkát is jelent. Tudósoknak akkor ajánlom, ha már van némi Python-tapasztalatod (legalább a 5. fejezet szintjén), és a munkafolyamatod természeténél fogva elágazó vagy iteratív.

---

### 12.2.3 AutoGen --- Társalgási multi-ágens rendszerek

**Mi ez?** A Microsoft AutoGen keretrendszere az ágenseket **beszélgető partnerekként** kezeli. Az ágensek üzeneteket küldenek egymásnak, vitatkoznak, kérdeznek, javítanak --- mintha egy csoportos megbeszélésen vennének részt.

**Miben különleges?**

- **GroupChat**: több ágens egy „szobában", ahol egy GroupChatManager moderálja a beszélgetést
- **Kódfuttatás**: az ágensek nemcsak beszélnek, hanem kódot is írhatnak és futtathatnak --- Docker konténerben, biztonságosan
- **Human-in-the-loop**: bármikor beleszólhatsz a beszélgetésbe, mint egy résztvevő

**Telepítés:**

```bash
pip install autogen-agentchat
```

**Egyszerű példa --- két ágens vitatkozik egy eredményről:**

```python
from autogen import AssistantAgent, UserProxyAgent

# Elemző ágens
analyst = AssistantAgent(
    name="Elemző",
    system_message="""Környezettudomány szakértő vagy.
    Elemezd a kapott adatokat, és fogalmazd meg
    a következtetéseidet.""",
    llm_config={"model": "gpt-4o"}
)

# Kritikus ágens
critic = AssistantAgent(
    name="Kritikus",
    system_message="""Statisztikus vagy, aki kritikusan
    vizsgálja az elemzéseket. Kérdőjelezd meg a gyenge
    pontokat és javasold a javításokat.""",
    llm_config={"model": "gpt-4o"}
)

# Emberi résztvevő (jóváhagyja a végeredményt)
user = UserProxyAgent(
    name="Kutató",
    human_input_mode="TERMINATE",  # Csak a végén kér jóváhagyást
    code_execution_config={"work_dir": "output"}
)

# A beszélgetés elindítása
user.initiate_chat(
    analyst,
    message="Elemezd a mellékelt talajminta-adatokat: Cd=2.3mg/kg, Pb=45mg/kg, Zn=120mg/kg"
)
```

**Mikor válaszd az AutoGen-t?**

- Ha a feladatod **iteratív finomítást** igényel (pl. elemzés → kritika → javítás → újraértékelés)
- Ha **kódfuttatás** is kell az ágens-munkafolyamatban (statisztikai elemzés, ábrák generálása)
- Ha a Microsoft-ökoszisztémában dolgozol (Azure, VS Code)

---

### 12.2.4 Claude Agent SDK --- Professzionális eszköztár

**Mi ez?** Az Anthropic Claude Agent SDK-ja egy Python könyvtár, amely a Claude modellcsalád képességeire épít. Nem egy generikus ágens-keretrendszer, hanem a Claude „natív" módja az ágens-munkafolyamatok építésének.

**Miben különleges?**

- **Extended thinking**: a Claude „hangosan gondolkodik" --- láthatod a gondolkodási folyamatát, ami a tudományos munkában különösen hasznos az átláthatóság szempontjából
- **Natív eszközhasználat**: a Claude function calling rendszere közvetlenül integrálódik
- **MCP integráció**: a Claude az MCP protokollt natívan támogatja, így az ágenseid közvetlenül csatlakozhatnak fájlrendszerekhez, adatbázisokhoz, API-khoz
- **Computer use**: a Claude képes grafikus felületeket kezelni (kattintás, gépelés, navigáció)

**Telepítés:**

```bash
pip install claude-agent-sdk
```

**Egyszerű példa:**

```python
from claude_agent_sdk import Agent, Tool

# Eszköz definiálása
search_tool = Tool(
    name="search_pubmed",
    description="Keresés a PubMed adatbázisban",
    parameters={
        "query": {"type": "string", "description": "Keresési kifejezés"},
        "max_results": {"type": "integer", "description": "Max. találatok"}
    },
    handler=pubmed_search_function  # A te függvényed
)

# Ágens létrehozása
agent = Agent(
    model="claude-sonnet-4-20250514",
    tools=[search_tool],
    system_prompt="""Környezettudományi kutatási asszisztens vagy.
    A felhasználó kérdései alapján keress releváns publikációkat
    és foglald össze az eredményeket."""
)

# Futtatás
result = agent.run("Keresd meg a legújabb cikkeket a kadmium bioremediációjáról talajban")
print(result)
```

**Mikor válaszd a Claude Agent SDK-t?**

- Ha már a Claude-ot használod és szeretnéd kihasználni az extended thinking és MCP képességeit
- Ha az **átláthatóság** különösen fontos (extended thinking megmutatja a gondolkodási folyamatot)
- Ha az ágenseid **fájlrendszerekhez és adatbázisokhoz** is csatlakoznak (MCP)

---

### 12.2.5 Az összehasonlító táblázat

Ez az egyetlen hely a könyvben, ahol a négy keretrendszert egymás mellé tesszük. Mentsd el --- később vissza fogsz ide lapozni.

| Szempont | CrewAI | LangGraph | AutoGen | Claude Agent SDK |
|----------|--------|-----------|---------|-----------------|
| **Megközelítés** | Szerep-alapú csapatok | Gráf-alapú munkafolyamatok | Társalgási ágensek | Natív Claude integráció |
| **Tanulási görbe** | Alacsony | Közepes--magas | Közepes | Alacsony--közepes |
| **Rugalmasság** | Közepes | Nagyon magas | Magas | Közepes |
| **Kódfuttatás** | Korlátozott | Egyedi node-okkal | Beépített (Docker) | Computer use |
| **Multi-agent** | Natív (Crew) | Egyedi gráfokkal | Natív (GroupChat) | Egyedi megoldással |
| **MCP támogatás** | Plugin-nal | Plugin-nal | Plugin-nal | Natív |
| **Állapotkezelés** | Automatikus | Explicit StateGraph | Üzenet-alapú | Kontextusablak |
| **Vizualizáció** | Korlátozott | Gráf-vizualizáció | Beszélgetés-log | Extended thinking |
| **LLM-függetlenség** | Igen (bármely LLM) | Igen (bármely LLM) | Igen (bármely LLM) | Csak Claude |
| **Ideális felhasználás** | Csapat-jellegű feladatok | Komplex, elágazó folyamatok | Iteratív finomítás, kódfuttatás | Claude-ökoszisztéma, MCP |
| **Python-tudás igénye** | Minimális | Jelentős | Közepes | Minimális--közepes |
| **Dokumentáció** | Jó, aktív közösség | Jó, de gyorsan változik | Jó, Microsoft-támogatás | Növekvő |
| **Tudósnak ajánlom** | Első ágens-projekt | Haladó munkafolyamatok | Kódfuttató feladatok | Ha Claude a fő modelled |

**A döntési fa:**

```
Építeni akarsz egy kutatási ágenst?
│
├─ Első alkalom?
│  └─► CrewAI (legegyszerűbb belépési pont)
│
├─ Elágazó, iteratív munkafolyamat kell?
│  └─► LangGraph (teljes kontroll a gráf felett)
│
├─ Ágensek, amelyek kódot is futtatnak?
│  └─► AutoGen (beépített kódfuttatás)
│
├─ Claude-ot használod és MCP-t akarsz?
│  └─► Claude Agent SDK (natív integráció)
│
└─ Nem akarsz kódolni egyáltalán?
   └─► n8n vizuális ágensek (lásd 8. fejezet)
```

---

## 12.3 Első kutatási ágensek építése

Most jön a lényeg. Három komplett, működő ágens-rendszert építünk, amelyek valódi kutatási problémákat oldanak meg. Mindegyiknél lépésről lépésre haladunk, és a kód minden sorát megmagyarázom.

### 12.3.1 Irodalomkutató ágens-csapat (CrewAI)

Visszatérünk Dr. Tóth Gábor problémájához: automatizáljuk a heti irodalomkutatást. Három ágenst építünk, akik csapatban dolgoznak:

1. **Kereső ágens** --- megkeresi az új publikációkat a megadott témában
2. **Olvasó ágens** --- elolvassa és értékeli a találatokat
3. **Szintetizáló ágens** --- összefoglalót ír a csoportértekezletre

#### 1. lépés: A projekt előkészítése

```bash
# Új könyvtár létrehozása
mkdir irodalom_kutato
cd irodalom_kutato

# Virtuális környezet (lásd 5. fejezet)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Csomagok telepítése
pip install crewai crewai-tools langchain-openai
```

Szükséged lesz egy OpenAI API kulcsra (vagy bármely más LLM-szolgáltató kulcsára). Hozz létre egy `.env` fájlt:

```
OPENAI_API_KEY=sk-a-te-kulcsod-ide
SERPER_API_KEY=a-te-serper-kulcsod  # Google kereséshez
```

> **Megjegyzés:** A Serper API (serper.dev) ingyenes szinten 2500 keresést ad havonta --- egy heti irodalomkutatáshoz ez bőven elég. Alternatívaként használhatod a `DuckDuckGoSearchRun` eszközt is, ami teljesen ingyenes.

#### 2. lépés: Az ágensek definiálása

```python
# irodalom_kutato.py

from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import datetime

load_dotenv()

# Az LLM, amit az ágensek használnak
llm = ChatOpenAI(model="gpt-4o", temperature=0.1)

# Eszközök
search_tool = SerperDevTool()  # Google keresés
scrape_tool = ScrapeWebsiteTool()  # Weboldal-tartalom kinyerése

# ─── 1. ÁGENS: KERESŐ ────────────────────────────────────
searcher = Agent(
    role="Tudományos irodalomkereső",
    goal="""Megtalálni az elmúlt 7 nap legfontosabb publikációit
    a megadott kutatási témában. Csak peer-reviewed forrásokból
    és elismert preprint-szerverekről (arXiv, bioRxiv, EarthArXiv)
    keress.""",
    backstory="""Tapasztalt tudományos könyvtáros vagy, aki 20 éve
    segít kutatóknak az irodalomkeresésben. Ismered a PubMed, Web of
    Science és Google Scholar adatbázisokat. Tudod, hogyan kell
    hatékony keresőkifejezéseket alkotni, és ki tudod szűrni a
    predátor folyóiratokat.""",
    tools=[search_tool, scrape_tool],
    llm=llm,
    verbose=True,  # Láthatod, mit csinál
    allow_delegation=False  # Nem delegálhat másnak
)

# ─── 2. ÁGENS: OLVASÓ ────────────────────────────────────
reader = Agent(
    role="Kritikus olvasó és értékelő",
    goal="""Elolvasni a talált publikációk absztraktjait és elérhető
    teljes szövegeit, értékelni a módszertani minőséget és a
    relevancia-szintet a kutatócsoport szempontjából.""",
    backstory="""Posztdoktori kutató vagy, aki a szakterületed
    legmélyebb ismerőjeként értékeli az új publikációkat. Különösen
    figyelsz a módszertanra: a mintavétel megfelelőségére, a
    statisztikai elemzés helyességére, és az eredmények
    reprodukálhatóságára. Minden cikkhez relevancia-pontszámot
    adsz 1-10 skálán.""",
    tools=[scrape_tool],
    llm=llm,
    verbose=True,
    allow_delegation=False
)

# ─── 3. ÁGENS: SZINTETIZÁLÓ ──────────────────────────────
synthesizer = Agent(
    role="Kutatási szintetizáló és jelentésíró",
    goal="""A talált és értékelt publikációkból egy strukturált,
    tömör heti összefoglalót készíteni a kutatócsoport számára.
    Az összefoglaló legyen informatív, de rövid --- maximum 2 oldal.""",
    backstory="""Tudományos kommunikációs szakértő vagy. Képes vagy
    komplex eredményeket egyszerűen és pontosan összefoglalni.
    Az összefoglalóid mindig tartalmazzák: a legfontosabb új
    eredményeket, a módszertani innovációkat, és a kutatócsoport
    számára releváns következtetéseket.""",
    llm=llm,
    verbose=True,
    allow_delegation=False
)
```

**Mit csinálnak ezek a mezők?**

- **`role`**: Az ágens „beosztása" --- ezt használja a keretrendszer, amikor az ágensek egymásra hivatkoznak
- **`goal`**: Mi a konkrét feladata --- minél specifikusabb, annál jobb az eredmény
- **`backstory`**: Az ágens „személyisége" és szakmai háttere --- ez befolyásolja, hogyan közelíti meg a feladatot
- **`tools`**: Milyen eszközöket használhat (keresés, weboldal-olvasás stb.)
- **`verbose=True`**: Kiírja a konzolra, mit csinál éppen --- hibakereséshez elengedhetetlen
- **`allow_delegation`**: Megengedett-e, hogy az ágens átadja a feladatát egy másiknak

#### 3. lépés: A feladatok definiálása

```python
# A mai dátum (a keresés időablakához)
today = datetime.date.today()
week_ago = today - datetime.timedelta(days=7)

# ─── KUTATÁSI TÉMA (ezt változtasd a sajátodra) ──────────
research_topic = "heavy metal bioremediation soil microorganisms"
group_focus = """A kutatócsoportunk a talaj nehézfém-szennyezésének
bioremediációjával foglalkozik, különös tekintettel a mikrobiális
közösségek szerepére. Aktuális projektjeink: (1) kadmium-akkumuláló
baktériumtörzsek izolálása Tisza-menti üledékekből, (2) mikorrhiza-
gombák szerepe a fitoremediációban, (3) metagenomikai módszerek
alkalmazása szennyezett talajok mikrobiom-elemzésében."""

# ─── 1. FELADAT: KERESÉS ─────────────────────────────────
search_task = Task(
    description=f"""Keress az elmúlt 7 nap ({week_ago} -- {today})
    publikációiban a következő témában: {research_topic}

    Használd a következő keresési stratégiát:
    1. Google Scholar keresés a fő kulcsszavakkal
    2. Bővített keresés szinonimákkal és kapcsolódó kifejezésekkel
    3. Szűrd ki a nem peer-reviewed és predátor forrásokat

    Az eredmény: minden talált cikkhez add meg a szerzőket, címet,
    folyóiratot, DOI-t (ha elérhető), és az absztrakt URL-jét.
    Minimum 10, maximum 30 találatot gyűjts.""",
    expected_output="""Strukturált lista a talált publikációkról:
    - Szerzők, Cím, Folyóirat, Dátum, DOI, URL
    Minimum 10, maximum 30 tétel.""",
    agent=searcher
)

# ─── 2. FELADAT: OLVASÁS ÉS ÉRTÉKELÉS ───────────────────
read_task = Task(
    description=f"""Olvasd el az előző ágens által talált
    publikációk absztraktjait. Minden cikkhez:

    1. Értékeld a relevancia-szintet 1-10 skálán a következő
       kutatási fókusz alapján: {group_focus}
    2. Foglald össze 2-3 mondatban a fő eredményt
    3. Jelezd, ha módszertani innovációt tartalmaz
    4. Jelezd, ha közvetlenül alkalmazható a mi kutatásunkban

    Rangsorold a cikkeket relevancia szerint.""",
    expected_output="""Rangsorolt lista minden cikkről:
    - Relevancia-pontszám (1-10)
    - Rövid összefoglaló (2-3 mondat)
    - Módszertani innováció: igen/nem
    - Alkalmazhatóság: közvetlen/közvetett/nincs
    Az 5 alatti pontszámúakat csak felsorold, ne részletezd.""",
    agent=reader,
    context=[search_task]  # Megkapja a keresés eredményét
)

# ─── 3. FELADAT: SZINTÉZIS ───────────────────────────────
synthesis_task = Task(
    description=f"""Az értékelt publikációk alapján készíts egy
    heti irodalmi összefoglalót a kutatócsoport számára.

    A kutatócsoport fókusza: {group_focus}

    Az összefoglaló struktúrája:
    1. **Heti áttekintés** (3-5 mondat): mi volt a hét fő trendje
    2. **Top 5 legfontosabb cikk**: mindegyikhez 1 bekezdés
    3. **Módszertani újdonságok**: ha volt releváns
    4. **Javaslatok**: milyen cikkeket érdemes a csoportban
       részletesen megbeszélni
    5. **Keresési statisztika**: hány cikket találtunk, mennyit
       szűrtünk ki, a releváns cikkek aránya

    A nyelv legyen magyar, de a szakkifejezések maradhatnak angolul.
    Az összefoglaló maximum 2 oldal legyen.""",
    expected_output="""Strukturált heti irodalmi összefoglaló
    a fenti 5 szekcióval, magyar nyelven, maximum 2 oldal.""",
    agent=synthesizer,
    context=[read_task]  # Megkapja az értékelés eredményét
)
```

#### 4. lépés: A csapat összeállítása és futtatása

```python
# ─── A CSAPAT ─────────────────────────────────────────────
crew = Crew(
    agents=[searcher, reader, synthesizer],
    tasks=[search_task, read_task, synthesis_task],
    process=Process.sequential,  # Sorban dolgoznak
    verbose=True
)

# ─── FUTTATÁS ─────────────────────────────────────────────
print("=" * 60)
print(f"Heti irodalomkutatás indítása: {today}")
print(f"Téma: {research_topic}")
print("=" * 60)

result = crew.kickoff()

# Eredmény mentése
output_file = f"heti_irodalom_{today}.md"
with open(output_file, "w", encoding="utf-8") as f:
    f.write(f"# Heti irodalmi összefoglaló\n")
    f.write(f"## {week_ago} -- {today}\n\n")
    f.write(str(result))

print(f"\nAz összefoglaló elmentve: {output_file}")
```

#### 5. lépés: Futtatás és az eredmény

```bash
python irodalom_kutato.py
```

A konzolra részletes logot fogsz látni: a kereső ágens elkezdi a keresést, megtalálja a cikkeket, átadja az olvasó ágensnek, aki értékeli őket, majd a szintetizáló összeállítja az összefoglalót. Az egész folyamat 3-8 perc, attól függően, hány cikket talál és milyen mélyen elemzi őket.

Az eredmény egy Markdown fájl, amit közvetlenül felhasználhatsz a csoportértekezleten, elküldhetsz emailben, vagy beilleszthetsz a kutatási jegyzeteidbe.

#### 6. lépés: Automatizálás --- hétfő reggeli ütemezés

Ha azt szeretnéd, hogy ez minden hétfő reggel automatikusan lefusson, egy egyszerű cron job-bal (Linux/Mac) vagy Task Scheduler-rel (Windows) megoldhatod:

```bash
# Linux/Mac: minden hétfő reggel 7:00-kor
crontab -e
# Add hozzá:
0 7 * * 1 cd /path/to/irodalom_kutato && /path/to/venv/bin/python irodalom_kutato.py
```

Még elegánsabb megoldás, ha az eredményt emailben is elküldöd a csoportnak --- ehhez a CrewAI-hoz egy egyszerű email-küldő eszközt (tool) adhatsz, vagy az n8n-ből hívod meg a scriptet (lásd 8. fejezet).

> **Gyakorlat:** Próbáld ki a saját kutatási témáddal! Változtasd meg a `research_topic` és `group_focus` változókat, és futtasd le. Az első futtatás mindig tanulságos: meglátod, hol kell finomítani a promptokon.

---

### 12.3.2 Adatfeldolgozó ágens-pipeline

A második ágens-rendszerünk egy gyakori kutatási problémát old meg: heterogén adatforrásokból érkező adatok egységesítése, tisztítása és előzetes elemzése.

**A probléma:** Egy ökológiai kutatócsoport négyféle formátumban kapja az adatokat: (1) CSV fájlok a terepi mérésekből, (2) Excel táblázatok a laborból, (3) szöveges logok az automatikus mérőállomásokról, és (4) PDF-ek az együttműködő partnerek jelentéseiből. Mielőtt bármit elemezhetnének, órákat töltenek az adatok egységesítésével.

**A megoldás:** Egy ágens-pipeline, amely automatikusan:
1. Felismeri a formátumot
2. Kinyeri és strukturálja az adatokat
3. Ellenőrzi a minőséget (hiányzó értékek, outlier-ek, egységek)
4. Egységes formátumba konvertál
5. Előzetes statisztikát készít

```python
# adatfeldolgozo_pipeline.py

from crewai import Agent, Task, Crew, Process

# ─── 1. ÁGENS: FORMÁTUMFELISMERŐ ─────────────────────────
format_detector = Agent(
    role="Adatformátum-szakértő",
    goal="""Felismerni a bemeneti adatok formátumát, struktúráját,
    és az oszlopok/mezők jelentését. Azonosítani a mértékegységeket,
    a dátumformátumokat, és a kódolási sémákat.""",
    backstory="""Adatmérnök vagy, aki 15 éve dolgozik tudományos
    adatokkal. Láttad már az összes furcsa formátumot, amit
    kutatók képesek produkálni. Tudod, hogy egy 'konc' oszlop
    valószínűleg koncentrációt jelent, és a ',' tizedes
    elválasztó Európában, de ezres-elválasztó Amerikában.""",
    llm=llm,
    verbose=True
)

# ─── 2. ÁGENS: ADATTISZTÍTÓ ──────────────────────────────
data_cleaner = Agent(
    role="Adatminőség-ellenőr",
    goal="""Tisztítani az adatokat: hiányzó értékek kezelése,
    outlier-ek azonosítása, egységek egységesítése, formátumok
    konvertálása. Minden módosítást dokumentálni.""",
    backstory="""Biostatisztikus vagy, akinek a legfontosabb elve:
    'Semmit nem törlünk, mindent dokumentálunk.' Ha outlier-t
    találsz, megjelölöd, de nem törlöd automatikusan --- a kutató
    döntse el, mi legyen vele.""",
    llm=llm,
    verbose=True
)

# ─── 3. ÁGENS: ELEMZŐ ────────────────────────────────────
analyzer = Agent(
    role="Előzetes statisztikai elemző",
    goal="""Alapstatisztikákat készíteni a tisztított adatokból:
    leíró statisztikák, eloszlások, korrelációk, trendek.
    Anomáliákat és érdekes mintákat azonosítani.""",
    backstory="""Adattudós vagy, aki a felfedező adatelemzés
    (EDA) mestere. Tudod, hogy a jó elemzés nem a végső
    válaszokat adja, hanem a jó kérdéseket fogalmazza meg.""",
    llm=llm,
    verbose=True
)

# ─── FELADATOK ────────────────────────────────────────────
detect_task = Task(
    description="""Elemezd a következő adatforrást:
    {input_data}

    Határozd meg:
    1. Fájlformátum és kódolás
    2. Oszlopok/mezők neve és valószínű jelentése
    3. Mértékegységek
    4. Dátumformátum
    5. Hiányzó értékek jelölése (NA, NULL, üres, -999, stb.)
    6. Adatok valószínű eredete és kontextusa""",
    expected_output="Strukturált formátum-leírás a fenti pontokkal.",
    agent=format_detector
)

clean_task = Task(
    description="""A formátumelemzés alapján tisztítsd az adatokat:
    1. Egységesítsd a mértékegységeket (SI rendszer)
    2. Konvertáld a dátumokat ISO 8601 formátumba
    3. Azonosítsd és jelöld meg a hiányzó értékeket
    4. Azonosítsd és jelöld meg az outlier-eket (IQR módszer)
    5. Dokumentáld MINDEN módosítást egy 'változásnapló'-ban

    FONTOS: Ne törölj adatot! Csak jelöld meg a problémásakat.""",
    expected_output="""Tisztított adatok + változásnapló, amely
    minden módosítást dokumentál (mit, miért, eredeti érték).""",
    agent=data_cleaner,
    context=[detect_task]
)

analyze_task = Task(
    description="""A tisztított adatok alapján készíts előzetes
    elemzést:
    1. Leíró statisztikák (átlag, medián, szórás, min, max)
    2. Hiányzó értékek aránya oszloponként
    3. Outlier-ek száma és jellege
    4. Oszlopok közötti korrelációk (ha numerikusak)
    5. Észrevételek és javaslatok a további elemzéshez

    Az eredmény legyen Markdown formátumú, táblázatokkal.""",
    expected_output="Markdown formátumú EDA-jelentés táblázatokkal.",
    agent=analyzer,
    context=[clean_task]
)

# ─── PIPELINE ÖSSZEÁLLÍTÁSA ───────────────────────────────
pipeline = Crew(
    agents=[format_detector, data_cleaner, analyzer],
    tasks=[detect_task, clean_task, analyze_task],
    process=Process.sequential,
    verbose=True
)

# ─── FUTTATÁS ─────────────────────────────────────────────
# Példa bemenet: egy CSV fájl tartalmának beolvasása
with open("minta_adatok.csv", "r", encoding="utf-8") as f:
    data_content = f.read()

result = pipeline.kickoff(
    inputs={"input_data": data_content}
)

# Eredmény mentése
with open("eda_jelentes.md", "w", encoding="utf-8") as f:
    f.write(str(result))

print("Az EDA-jelentés elkészült: eda_jelentes.md")
```

**Mire figyelj:**

- Az LLM-ek kontextusablakának mérete korlátot szab annak, mekkora adatot tudsz egyszerre feldolgozni. Egy 10 000 soros CSV nem fér bele --- ilyenkor az adatot darabokra (chunk) kell bontani, vagy csak egy mintát (sample) küldesz az ágensnek
- Az ágens által generált statisztikákat **mindig ellenőrizd** --- az LLM-ek nem kalkulátorok, a számolásaik nem mindig pontosak
- Ha pontos statisztikát akarsz, adj az ágensnek egy Python-kódfuttató eszközt (tool), amellyel pandas/numpy/scipy kódot futtathat

---

### 12.3.3 Kísérlet-figyelő és riasztó ágens

A harmadik ágens-rendszerünk egy **folyamatos monitorozó**, amely figyeli a futó kísérleteidet és riaszt, ha valami nem stimmel.

**A felhasználási eset:** Egy biológiai kísérletsorozat fut, amelyben 48 Petri-csészében különböző baktériumtörzsek növekedését mérik. Egy automatikus leolvasó óránként rögzíti az optikai denzitást (OD600). A kísérlet 72 órás, és éjjel-nappal fut. A kutató nem ülhet a gép előtt --- de tudni akar róla, ha valami szokatlan történik.

```python
# kiserleti_monitor.py

from crewai import Agent, Task, Crew
import json
import smtplib
from email.mime.text import MIMEText

# ─── MONITOROZÓ ÁGENS ────────────────────────────────────
monitor = Agent(
    role="Kísérleti adat-monitorozó",
    goal="""Folyamatosan figyelni a beérkező mérési adatokat.
    Azonnal riasztani, ha:
    - Szokatlan értéket lát (outlier a növekedési görbéhez képest)
    - Egy minta növekedése váratlanul megáll vagy visszaesik
    - Kontamináció jeleire utaló minta megjelenik
    - A mérőrendszer hibája gyanítható (azonos értékek, NaN-ok)""",
    backstory="""Tapasztalt mikrobiológus vagy, aki 20 éve
    dolgozik bakteriális növekedési kísérletekkel. Fejből ismered
    a tipikus növekedési görbéket (lag fázis, exponenciális,
    stacionárius, halálozási fázis) és azonnal észreveszed,
    ha valami eltér a normálistól.""",
    llm=llm,
    verbose=True
)

def check_experiment_data(data_file: str) -> str:
    """Beolvassa és ellenőrzi a legutóbbi mérési adatokat."""
    with open(data_file, "r") as f:
        data = json.load(f)

    # Az ágens elemzi az adatokat
    check_task = Task(
        description=f"""Elemezd a következő mérési adatokat.
        Ez egy bakteriális növekedési kísérlet, OD600 mérésekkel.

        Adatok: {json.dumps(data, indent=2)}

        Ellenőrizd:
        1. Van-e outlier érték?
        2. Van-e minta, amelyik nem a várt növekedési görbét követi?
        3. Van-e kontamináció jele (váratlan, gyors növekedés)?
        4. Van-e műszerhiba jele (NaN, állandó érték, negatív OD)?

        Ha BÁRMILYEN problémát találsz, jelezd a szintjét:
        🔴 KRITIKUS: azonnali beavatkozás szükséges
        🟡 FIGYELMEZTETÉS: érdemes megnézni
        🟢 RENDBEN: minden normális

        Válaszolj JSON formátumban:
        {{"status": "KRITIKUS/FIGYELMEZTETÉS/RENDBEN",
          "problems": [...],
          "recommendation": "..."}}""",
        expected_output="JSON formátumú állapotjelentés.",
        agent=monitor
    )

    crew = Crew(agents=[monitor], tasks=[check_task])
    result = crew.kickoff()
    return str(result)

def send_alert(message: str, recipients: list):
    """Email riasztás küldése."""
    msg = MIMEText(message, "plain", "utf-8")
    msg["Subject"] = "⚠️ Kísérleti riasztás"
    msg["From"] = "labor.monitor@university.hu"
    msg["To"] = ", ".join(recipients)

    with smtplib.SMTP("smtp.university.hu", 587) as server:
        server.starttls()
        server.login("labor.monitor@university.hu", "jelszo")
        server.send_message(msg)

# ─── MONITOROZÁSI CIKLUS ─────────────────────────────────
import time
import schedule

def hourly_check():
    """Óránkénti ellenőrzés."""
    print(f"Ellenőrzés indítása: {datetime.datetime.now()}")

    result = check_experiment_data("latest_measurements.json")
    result_dict = json.loads(result)

    if result_dict["status"] in ["KRITIKUS", "FIGYELMEZTETÉS"]:
        send_alert(
            f"Kísérleti riasztás: {result_dict['status']}\n\n"
            f"Problémák:\n" +
            "\n".join(f"- {p}" for p in result_dict["problems"]) +
            f"\n\nJavaslat: {result_dict['recommendation']}",
            recipients=["toth.gabor@unideb.hu", "phd.hallgato@unideb.hu"]
        )
        print(f"Riasztás elküldve: {result_dict['status']}")
    else:
        print("Minden rendben.")

# Óránkénti futtatás
schedule.every(1).hours.do(hourly_check)

print("Kísérleti monitor elindult. Ctrl+C a leállításhoz.")
while True:
    schedule.run_pending()
    time.sleep(60)
```

**A három ágens-rendszer összefoglalása:**

| Rendszer | Ágensek | Futási mód | Tipikus használat |
|----------|---------|------------|-------------------|
| Irodalomkutató | 3 (keresés → olvasás → szintézis) | Heti, ütemezett | Csoportértekezletre összefoglaló |
| Adatfeldolgozó | 3 (formátum → tisztítás → elemzés) | Igény szerint | Új adatbevitel feldolgozása |
| Kísérlet-monitorozó | 1 (folyamatos figyelés) | Folyamatos, óránkénti | Hosszan futó kísérletek felügyelete |

---

## 12.4 Ágensek csatlakoztatása adatokhoz: MCP a gyakorlatban

Az előző fejezetben megismerkedtél az MCP (Model Context Protocol) fogalmával. Most nézzük meg, hogyan használod a gyakorlatban, hogy az ágenseid közvetlenül elérhessék a kutatási adataidat és eszközeidet.

### Az MCP lényege, röviden

Az MCP egy szabványos protokoll, amelyen keresztül az LLM-ek (és az ágensek) csatlakozhatnak külső adatforrásokhoz és eszközökhöz. Gondolj rá úgy, mint az USB-re: egy szabványos csatlakozó, amelyen bármi csatlakoztatható.

```
┌──────────────┐     MCP      ┌──────────────────────┐
│              │   protokoll   │                      │
│   AI ÁGENS   │◄────────────►│  MCP SZERVER          │
│              │              │                      │
│  (Claude,    │              │  - Fájlrendszer      │
│   GPT,       │              │  - Adatbázis         │
│   bármely    │              │  - API               │
│   LLM)       │              │  - Műszer            │
│              │              │  - Bármi             │
└──────────────┘              └──────────────────────┘
```

### 12.4.1 Fájlrendszer --- az ágens olvas és ír fájlokat

A legegyszerűbb MCP-használat: az ágens közvetlenül hozzáfér a fájljaidhoz. Nem kell copy-paste-elned az adatokat a chatablakba --- az ágens maga olvassa be, amit kell.

**Miért hasznos kutatásban?**

- Az ágens közvetlenül olvashatja a mérési eredményeket tartalmazó CSV-ket
- Átolvashatja a korábbi elemzéseid kódját és dokumentációját
- Az elkészült összefoglalókat közvetlenül a megfelelő mappába mentheti

**Beállítás Claude Desktop-pal:**

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "C:/Users/kutato/research_data",
        "C:/Users/kutato/publications"
      ]
    }
  }
}
```

Ezzel a Claude Desktop-ban futó ágens hozzáfér a `research_data` és `publications` mappáidhoz. **Fontos biztonsági szempont:** csak azokat a mappákat add meg, amelyekhez valóban hozzáférést akarsz adni. Ne add meg a teljes C: meghajtót!

### 12.4.2 Adatbázisok --- az ágens lekérdezi a kutatási adatbázisodat

Ha a kutatócsoportod adatait adatbázisban (SQLite, PostgreSQL, MySQL) tároljátok, az MCP-n keresztül az ágens közvetlenül lekérdezheti az adatbázist.

```json
{
  "mcpServers": {
    "sqlite": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-sqlite",
        "C:/Users/kutato/research_data/measurements.db"
      ]
    }
  }
}
```

**Milyen kérdéseket tehetsz fel az ágensnek?**

- „Mennyi kadmium-mérésünk van 2024-ből a Tisza-menti mintavételi pontokról?"
- „Melyik mintavételi helyen volt a legmagasabb átlagos ólomkoncentráció?"
- „Készíts összesítő táblázatot a tavalyi mérésekből, szűrve a pH < 6 mintákra"

Az ágens SQL-lekérdezéseket generál és futtat --- te természetes nyelven kérdezed, ő a megfelelő SQL-t írja.

### 12.4.3 API-k --- az ágens eléri a külső szolgáltatásokat

Sok kutatási adatforrás API-n (Application Programming Interface) keresztül érhető el: PubMed, CrossRef, GBIF, Copernicus, USGS, OpenMeteo, és így tovább. MCP szerverek segítségével ezeket is elérhetővé teheted az ágensed számára.

**Példa: időjárási adatok lekérdezése:**

```json
{
  "mcpServers": {
    "weather": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-weather"
      ],
      "env": {
        "WEATHER_API_KEY": "a_te_api_kulcsod"
      }
    }
  }
}
```

**Példa: GitHub repository elérése (kód, dokumentáció):**

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-github"
      ],
      "env": {
        "GITHUB_TOKEN": "a_te_github_tokenod"
      }
    }
  }
}
```

### 12.4.4 Műszerek és szenzorok --- az ágens a laborod részévé válik

Ez a legizgalmasabb terület: az ágens közvetlen kapcsolatban áll a laboratóriumi műszerekkel vagy a terepi szenzorokkal. Ehhez általában egyedi MCP szervert kell írni (lásd a következő szekciót és a 13. fejezetet), de a koncepció egyszerű:

```
┌─────────────────┐    MCP     ┌───────────────┐     ┌──────────┐
│   AI ÁGENS      │◄──────────►│  Egyedi MCP   │◄───►│  Műszer  │
│                 │            │  szerver       │     │  (pl.    │
│ "Mennyi a       │            │  (Python)      │     │  spektro-│
│  jelenlegi OD?" │            │               │     │  méter)  │
└─────────────────┘            └───────────────┘     └──────────┘
```

**Valós példa:** Egy Debreceni kutatócsoport UV-Vis spektrofotométerének kimeneti adatait olvassa egy Python script, amely MCP szerveren keresztül elérhetővé teszi az ágens számára. A kutató annyit kérdez: „Mi az utolsó minta abszorbanciája 254 nm-en?" --- és az ágens közvetlenül a műszer aktuális kimenetéből válaszol.

### 12.4.5 Több MCP szerver együttes használata

Az igazi erő abban van, amikor **több adatforrást kombinálsz**. Az ágens egyszerre éri el a fájljaidat, az adatbázist, a külső API-kat és a műszereidet:

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem",
               "C:/Users/kutato/research_data"]
    },
    "database": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sqlite",
               "C:/Users/kutato/research_data/lab.db"]
    },
    "pubmed": {
      "command": "python",
      "args": ["C:/Users/kutato/mcp_servers/pubmed_server.py"]
    }
  }
}
```

Ezzel az ágens egy kérdésre, mint például „Hasonlítsd össze a legutóbbi kadmium-méréseinket a szakirodalomban közölt átlagértékekkel", képes:

1. Lekérdezni a helyi adatbázisból a méréseiteket
2. Keresni a PubMed-en releváns publikációkat
3. Beolvasni a korábbi elemzéseidet a fájlrendszerből
4. Mindezt összegezni egy koherens válaszban

---

## 12.5 Saját MCP szerver építése a laborodnak

Ha a meglévő MCP szerverek nem fedik le az igényeidet --- és kutatóként valószínűleg nem fogják, mert minden labor egyedi ---, saját MCP szervert is írhatsz. Ez könnyebb, mint gondolnád.

### Az alapstruktúra

Egy MCP szerver lényegében egy Python (vagy Node.js) program, amely:

1. **Eszközöket (tools)** definiál, amelyeket az ágens meghívhat
2. **Erőforrásokat (resources)** tesz elérhetővé, amelyeket az ágens olvashat
3. Az MCP protokollon kommunikál az ágens-rendszerrel

```python
# lab_mcp_server.py — Egyszerű MCP szerver a laborodnak

from mcp.server import Server, NotificationOptions
from mcp.server.models import InitializationOptions
import mcp.server.stdio
import mcp.types as types
import sqlite3
import json

# Szerver létrehozása
server = Server("lab-server")

# ─── ESZKÖZ 1: Mérési adatok lekérdezése ─────────────────
@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name="query_measurements",
            description="""Lekérdezi a laboratóriumi méréseket
            az adatbázisból. Szűrhető dátum, minta-azonosító
            és paraméter szerint.""",
            inputSchema={
                "type": "object",
                "properties": {
                    "parameter": {
                        "type": "string",
                        "description": "Mérendő paraméter (pl. Cd, Pb, pH)"
                    },
                    "start_date": {
                        "type": "string",
                        "description": "Kezdő dátum (YYYY-MM-DD)"
                    },
                    "end_date": {
                        "type": "string",
                        "description": "Záró dátum (YYYY-MM-DD)"
                    }
                },
                "required": ["parameter"]
            }
        ),
        types.Tool(
            name="get_sample_info",
            description="Visszaadja egy minta összes adatát az azonosítója alapján.",
            inputSchema={
                "type": "object",
                "properties": {
                    "sample_id": {
                        "type": "string",
                        "description": "Minta-azonosító (pl. T3-2024-001)"
                    }
                },
                "required": ["sample_id"]
            }
        )
    ]

@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict | None
) -> list[types.TextContent]:

    if name == "query_measurements":
        db = sqlite3.connect("lab_measurements.db")
        cursor = db.cursor()

        query = "SELECT * FROM measurements WHERE parameter = ?"
        params = [arguments["parameter"]]

        if "start_date" in arguments:
            query += " AND date >= ?"
            params.append(arguments["start_date"])
        if "end_date" in arguments:
            query += " AND date <= ?"
            params.append(arguments["end_date"])

        cursor.execute(query, params)
        results = cursor.fetchall()
        db.close()

        return [types.TextContent(
            type="text",
            text=json.dumps(results, indent=2, ensure_ascii=False)
        )]

    elif name == "get_sample_info":
        db = sqlite3.connect("lab_measurements.db")
        cursor = db.cursor()
        cursor.execute(
            "SELECT * FROM samples WHERE sample_id = ?",
            [arguments["sample_id"]]
        )
        result = cursor.fetchone()
        db.close()

        return [types.TextContent(
            type="text",
            text=json.dumps(result, ensure_ascii=False)
        )]

# Szerver indítása
async def main():
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream, write_stream,
            InitializationOptions(
                server_name="lab-server",
                server_version="0.1.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={}
                )
            )
        )

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```

Ez a szerver két eszközt biztosít: mérési adatok lekérdezését és mintainformáció visszaadását. Az ágens ezeket az eszközöket automatikusan „megtanulja" az MCP protokollon keresztül, és szükség szerint hívja meg.

> **A 13. fejezetben** részletesen foglalkozunk az MCP szerverek építésével: több eszközzel, erőforrásokkal, teszteléssel és dokumentációval. Itt a koncepcióra és a működő minimálpéldára koncentráltunk.

---

## 12.6 Végponttól végpontig: ágentikus kutatási munkafolyamat

Most, hogy ismered az egyes építőelemeket, nézzük meg, hogyan állnak össze egy **teljes kutatási ciklusban**. Az alábbi munkafolyamat bemutatja, hogyan támogathatják az ágensek a kutatás minden fázisát --- a hipotézistől a publikációig.

### A teljes ciklus

```
┌────────────────────────────────────────────────────────────────────┐
│                ÁGENTIKUS KUTATÁSI MUNKAFOLYAMAT                   │
│                                                                    │
│  1. HIPOTÉZIS          2. ADAT              3. ELEMZÉS            │
│  ┌────────────┐        ┌────────────┐       ┌────────────┐        │
│  │ Irodalom-  │        │ Adat-      │       │ Statisztikai│       │
│  │ kutató     │───────►│ feldolgozó │──────►│ elemző     │        │
│  │ ágens-csap.│        │ pipeline   │       │ ágens      │        │
│  └────────────┘        └────────────┘       └─────┬──────┘        │
│        │                                          │               │
│        ▼                                          ▼               │
│  ┌────────────┐                            ┌────────────┐         │
│  │ Hipotézis- │                            │ Vizualizáló│         │
│  │ generáló   │                            │ ágens      │         │
│  └────────────┘                            └─────┬──────┘         │
│                                                  │               │
│  4. JELENTÉS           5. REVIEW                 │               │
│  ┌────────────┐        ┌────────────┐            │               │
│  │ Jelentés-  │◄───────│ ▲ EMBER ▲  │◄───────────┘               │
│  │ író ágens  │        │ döntéspont │                              │
│  └────────────┘        └────────────┘                              │
└────────────────────────────────────────────────────────────────────┘
```

### Részletes megvalósítás CrewAI-val

```python
# kutatas_workflow.py — Teljes kutatási ciklus ágens-csapattal

from crewai import Agent, Task, Crew, Process

# ═══════════════════════════════════════════════════════════
# 1. FÁZIS: HIPOTÉZIS GENERÁLÁSA
# ═══════════════════════════════════════════════════════════

literature_agent = Agent(
    role="Irodalomkutató",
    goal="Összegyűjteni és szintetizálni a releváns szakirodalmat",
    backstory="Tapasztalt könyvtáros, aki ismeri a szakterület kulcspublikációit.",
    tools=[search_tool, scrape_tool],
    llm=llm
)

hypothesis_agent = Agent(
    role="Hipotézis-generáló",
    goal="""Az irodalmi áttekintés alapján azonosítani a kutatási
    réseket és tesztelhető hipotéziseket javasolni""",
    backstory="""Kreatív kutató, aki a meglévő irodalom alapján képes
    felismerni a nyitott kérdéseket és tesztelhető formába önteni.""",
    llm=llm
)

lit_review_task = Task(
    description="""Készíts irodalmi áttekintést a következő témában:
    '{research_question}'
    Gyűjts legalább 15 releváns publikációt az elmúlt 5 évből.
    Azonosítsd a fő eredményeket, az ellentmondásokat és a nyitott
    kérdéseket.""",
    expected_output="Strukturált irodalmi áttekintés nyitott kérdésekkel.",
    agent=literature_agent
)

hypothesis_task = Task(
    description="""Az irodalmi áttekintés alapján:
    1. Azonosíts 3-5 kutatási rést (knowledge gap)
    2. Mindegyikhez fogalmazz meg egy tesztelhető hipotézist
    3. Mindegyik hipotézishez javasold a szükséges kísérleti
       elrendezést és a minimálisan szükséges mintaméretet
    4. Rangsorold a hipotéziseket megvalósíthatóság szerint""",
    expected_output="""3-5 tesztelhető hipotézis, kísérleti tervvel
    és megvalósíthatósági rangsorrral.""",
    agent=hypothesis_agent,
    context=[lit_review_task]
)

# ═══════════════════════════════════════════════════════════
# 2. FÁZIS: ADATFELDOLGOZÁS
# ═══════════════════════════════════════════════════════════

data_agent = Agent(
    role="Adatfeldolgozó",
    goal="A nyers kísérleti adatok tisztítása és strukturálása",
    backstory="Precíz adatmérnök, aki minden lépést dokumentál.",
    llm=llm
)

data_task = Task(
    description="""Dolgozd fel a kísérleti adatokat:
    {experimental_data}

    1. Ellenőrizd az adatminőséget
    2. Kezeld a hiányzó értékeket
    3. Azonosítsd az outlier-eket
    4. Készíts tisztított adathalmazt
    5. Dokumentáld a feldolgozási lépéseket""",
    expected_output="Tisztított adathalmaz + feldolgozási napló.",
    agent=data_agent
)

# ═══════════════════════════════════════════════════════════
# 3. FÁZIS: ELEMZÉS ÉS VIZUALIZÁCIÓ
# ═══════════════════════════════════════════════════════════

stats_agent = Agent(
    role="Statisztikai elemző",
    goal="A tisztított adatok statisztikai elemzése",
    backstory="""Biostatisztikus, aki nem csak lefuttatja a teszteket,
    hanem értelmezi is az eredményeket és figyel a hatásméretre,
    nem csak a p-értékre.""",
    llm=llm
)

stats_task = Task(
    description="""Elemezd a tisztított adatokat:
    1. Leíró statisztikák
    2. A hipotézis teszteléséhez szükséges statisztikai próba
       kiválasztása és elvégzése
    3. Hatásméret (effect size) kiszámítása
    4. Konfidencia-intervallumok
    5. Az eredmények értelmezése tudományos kontextusban

    FONTOS: Ne csak a p-értéket nézd! A hatásméret és a
    gyakorlati jelentőség legalább olyan fontos.""",
    expected_output="""Statisztikai elemzés eredményei,
    értelmezéssel és vizualizációs javaslatokkal.""",
    agent=stats_agent,
    context=[data_task]
)

# ═══════════════════════════════════════════════════════════
# 4. FÁZIS: JELENTÉSÍRÁS
# ═══════════════════════════════════════════════════════════

report_agent = Agent(
    role="Tudományos jelentésíró",
    goal="""Strukturált kutatási jelentés készítése az eredmények
    alapján, IMRaD formátumban""",
    backstory="""Tapasztalt tudományos szerző, aki ismeri az IMRaD
    formátumot és a szakterület publikációs szokásait.""",
    llm=llm
)

report_task = Task(
    description="""Az összes előző fázis eredménye alapján készíts
    kutatási jelentést IMRaD formátumban:

    1. Introduction: a kutatási kérdés és a hipotézis kontextusa
    2. Methods: a kísérleti elrendezés és az elemzési módszerek
    3. Results: a statisztikai eredmények, táblázatokkal és
       ábraleírásokkal
    4. Discussion: az eredmények értelmezése, korlátok, jövőbeli
       irányok

    A nyelv legyen világos, tömör, tudományos magyar.""",
    expected_output="Teljes kutatási jelentés IMRaD formátumban.",
    agent=report_agent,
    context=[lit_review_task, stats_task]
)

# ═══════════════════════════════════════════════════════════
# A TELJES MUNKAFOLYAMAT
# ═══════════════════════════════════════════════════════════

research_crew = Crew(
    agents=[literature_agent, hypothesis_agent, data_agent,
            stats_agent, report_agent],
    tasks=[lit_review_task, hypothesis_task, data_task,
           stats_task, report_task],
    process=Process.sequential,
    verbose=True
)

# Futtatás
result = research_crew.kickoff(inputs={
    "research_question": "Hogyan befolyásolja a talaj pH-ja "
        "a kadmium bioverfügbarkeit-jét agyagos talajokban?",
    "experimental_data": "adatok betöltése a fájlrendszerből..."
})
```

**Fontos:** Ez a munkafolyamat **nem helyettesíti a kutatót** --- hanem felgyorsítja a munkáját. Az irodalomkutatás, az adattisztítás és a jelentésvázlat automatizálható, de a hipotézis jóváhagyása, az eredmények értelmezése és a publikáció véglegesítése az ember dolga.

---

## 12.7 Emberi döntési pontok: hol NE legyen autonóm az ágens

Ez a szekció a fejezet talán legfontosabb része. Az ágensek erősek, de **nem tévedhetetlenek** --- és a kutatásban a tévedés következményei súlyosak lehetnek. Egy rosszul értelmezett statisztikai eredmény, egy félreolvasott cikk, egy figyelmen kívül hagyott outlier: ezek mind tudományos hibákhoz vezethetnek.

### A három szint

```
┌─────────────────────────────────────────────────────┐
│              AUTOMATIZÁLÁS SZINTJEI                  │
│                                                     │
│  🟢 TELJESEN AUTOMATIZÁLHATÓ                        │
│  ─────────────────────────────                      │
│  • Irodalomkeresés és szűrés                        │
│  • Adatformátum-felismerés és -konverzió            │
│  • Leíró statisztikák készítése                     │
│  • Jelentésvázlat generálása                        │
│  • Kísérleti adatok monitorozása                    │
│  • Rutin adattisztítás (dokumentáltan)              │
│                                                     │
│  🟡 ÁGENS JAVASOL, EMBER DÖNT                       │
│  ─────────────────────────────                      │
│  • Statisztikai próba kiválasztása                  │
│  • Outlier-ek kezelése (törlés vs. megtartás)       │
│  • Hipotézisek rangsorolása                         │
│  • Kísérleti terv módosítása                        │
│  • Eredmények értelmezése                           │
│                                                     │
│  🔴 CSAK EMBER                                      │
│  ─────────────────                                  │
│  • Kutatási kérdés véglegesítése                    │
│  • Etikai döntések (emberi alanyok, állatetika)     │
│  • Eredmények tudományos publikálása                │
│  • Társszerzők bevonása és a szerzőség eldöntése    │
│  • Pályázati döntések                               │
│  • Reprodukálhatóság igazolása                      │
└─────────────────────────────────────────────────────┘
```

### Human-in-the-loop implementálása CrewAI-ban

A CrewAI lehetővé teszi, hogy egy feladat befejezése után az ágens **megvárja az emberi jóváhagyást** mielőtt a következő lépésre menne:

```python
from crewai import Task

# Ez a feladat megvárja az emberi jóváhagyást
stats_task = Task(
    description="Statisztikai elemzés elvégzése...",
    expected_output="Statisztikai eredmények...",
    agent=stats_agent,
    human_input=True  # Az ágens megáll és megkérdezi az embert
)
```

A `human_input=True` beállítással a feladat befejezése után a rendszer kiírja az eredményt és megvárja a te visszajelzésedet. Elfogadhatod, módosíthatod, vagy visszaküldeted az ágenssel.

### Gyakorlati tanácsok az emberi felügyelethez

1. **Minden statisztikai eredményt ellenőrizz.** Az LLM-ek nem kalkulátorok --- a számolásaik közelítők. Ha pontos statisztikát akarsz, adj az ágensnek Python-kódfuttató eszközt, és a kód kimenetét nézd, nem az LLM „fejszámolását".

2. **Minden hivatkozást ellenőrizz.** Az LLM-ek hajlamosak hivatkozásokat kitalálni (hallucináció). Az irodalomkutató ágensed által talált cikkeket mindig nézd meg, hogy valóban léteznek-e.

3. **Az outlier-döntés mindig az ember dolga.** Az ágens megjelölheti az outlier-eket, de a döntés, hogy törlöd, megtartod, vagy további vizsgálatot indítasz, a tiéd.

4. **A „miért" fontosabb, mint a „mit".** Ha az ágens javasol valamit (pl. „Kruskal-Wallis tesztet javaslok"), kérdezd meg, miért. Ha a magyarázat nem meggyőző, nézz utána magad.

---

## 12.8 Monitoring és hibakeresés: amikor az ágens nem azt csinálja, amit kellene

Az ágensek komplex rendszerek, és mint minden komplex rendszer, néha nem azt csinálják, amit várnál. Ebben a szekcióban megtanulod, hogyan figyeld és javítsd az ágenseid viselkedését.

### 12.8.1 A verbose mód: az első védelmi vonal

Az összes keretrendszer támogat valamilyen „bőbeszédű" módot, ahol az ágens kiírja, mit gondol, mit dönt, milyen eszközt hív meg és mit kap vissza. **Mindig kapcsold be fejlesztés közben.**

```python
# CrewAI
crew = Crew(agents=[...], tasks=[...], verbose=True)

# LangGraph — LangSmith trace-eléssel
import os
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "ls_..."

# AutoGen
agent = AssistantAgent(name="Elemző", llm_config={...})
# Az AutoGen alapból verbose
```

### 12.8.2 Tipikus hibák és megoldásaik

| Hiba | Tünet | Megoldás |
|------|-------|---------|
| **Ágens körbejár** | Ugyanazt a lépést ismétli többször | Adj `max_iter` limitet; pontosítsd a feladat leírását |
| **Nem használja az eszközöket** | Válaszol fejből, nem keres/nem kérdez le | A `goal`-ban és a `description`-ben expliciten mondd meg, hogy használja az eszközöket |
| **Rossz eszközt választ** | A kereső ágens a scrape tool-t hívja keresés helyett | Pontosítsd az eszközök `description`-jét |
| **Kontextusablak túlcsordulás** | Hibaüzenet a token-limitről | Csökkentsd az adatmennyiséget; használj összefoglalót a teljes adat helyett |
| **Hallucináció** | Az ágens kitalál adatokat, hivatkozásokat | Adj hozzá ellenőrző ágenst; kérj forrás-hivatkozást minden állításhoz |
| **Lassúság** | A munkafolyamat percek helyett fél órát tart | Használj kisebb modellt a rutin feladatokra (gpt-4o-mini); csökkentsd az iterációk számát |
| **Inkonzisztens kimenet** | Különböző futtatások nagyon eltérő eredményt adnak | Csökkentsd a temperature-t (0.0--0.2 az analitikus feladatokhoz); adj strukturáltabb promptokat |

### 12.8.3 Observability eszközök

Ha komolyabban foglalkozol az ágens-fejlesztéssel, érdemes megismerkedned a dedikált observability (megfigyelhetőség) eszközökkel:

| Eszköz | Mire jó | Díjszabás |
|--------|---------|-----------|
| **LangSmith** | LangChain/LangGraph trace-ek, kiértékelés | Ingyenes szint elérhető |
| **Langfuse** | Nyílt forráskódú LLM-observability | Ingyenes (self-hosted) |
| **AgentOps** | Ágens-specifikus monitorozás | Ingyenes szint elérhető |
| **Arize AI** | LLM-performancia és drift-detekció | Ingyenes szint elérhető |

Ezek az eszközök vizuálisan mutatják meg, mit csinált az ágens: melyik lépésben mennyi időt töltött, milyen prompt-ot küldött, milyen választ kapott, és hol akadt el. Ez megbecsülhetetlen információ, amikor egy nem működő ágenst akarsz megjavítani.

---

## 12.9 Naplózás és reprodukálhatóság: az ágens-futtatások dokumentálása

A tudományos kutatásban a reprodukálhatóság alapkövetelmény. Ha az ágensed eredménye bekerül egy publikációba, tudnod kell pontosan rekonstruálni, hogyan jutott arra az eredményre. Ez nem triviális, mert az LLM-ek nem determinisztikusak --- ugyanaz a prompt két különböző futtatásban eltérő eredményt adhat.

### 12.9.1 Amit naplóznod kell

Minden ágens-futtatásnál rögzítsd a következőket:

```python
import json
import datetime
import hashlib

def log_agent_run(run_id, config, inputs, outputs, metadata):
    """Ágens-futtatás naplózása."""
    log_entry = {
        "run_id": run_id,
        "timestamp": datetime.datetime.now().isoformat(),
        "config": {
            "framework": "crewai",
            "framework_version": "0.28.0",
            "model": config["model"],
            "model_version": config.get("model_version", "unknown"),
            "temperature": config["temperature"],
            "agents": [
                {
                    "role": a.role,
                    "goal": a.goal,
                    "backstory": a.backstory,
                    "tools": [t.name for t in a.tools]
                }
                for a in config["agents"]
            ],
            "tasks": [
                {
                    "description": t.description,
                    "expected_output": t.expected_output,
                    "agent_role": t.agent.role
                }
                for t in config["tasks"]
            ]
        },
        "inputs": inputs,
        "outputs": str(outputs),
        "input_hash": hashlib.sha256(
            json.dumps(inputs, sort_keys=True).encode()
        ).hexdigest(),
        "metadata": metadata
    }

    # Mentés fájlba
    log_file = f"logs/run_{run_id}.json"
    with open(log_file, "w", encoding="utf-8") as f:
        json.dump(log_entry, f, indent=2, ensure_ascii=False)

    return log_file
```

### 12.9.2 A reprodukálhatóság hat pillére

| Pillér | Mit jelent | Hogyan biztosítsd |
|--------|-----------|-------------------|
| **1. Modell-verzió** | Melyik modellt használtad, melyik verzióban | Rögzítsd a modell nevét és verzióját (pl. `gpt-4o-2024-08-06`) |
| **2. Promptok** | Pontosan milyen szöveget kapott a modell | Mentsd el az összes system prompt-ot, task description-t, backstory-t |
| **3. Eszközök és adatforrások** | Milyen eszközöket használt, milyen adatokat ért el | Naplózd az eszközhívásokat és azok bemeneteit/kimeneteit |
| **4. Paraméterek** | Temperature, max tokens, stb. | Rögzítsd az LLM-konfigurációt |
| **5. Bemenet** | Milyen adatot kapott bemenetként | Mentsd el vagy hash-eld a bemeneti adatokat |
| **6. Kimenet** | Milyen eredményt adott | Mentsd el a teljes kimenetet, beleértve a köztes eredményeket is |

### 12.9.3 Verziókezelés az ágens-kódhoz

A Git (lásd 5. fejezet) itt különösen fontos. Az ágens „viselkedését" a promptok, a konfigurációk és a kód együttesen határozza meg, és mindezeket verziózni kell:

```
irodalom_kutato/
├── agents/
│   ├── searcher.py          # Kereső ágens definíciója
│   ├── reader.py            # Olvasó ágens definíciója
│   └── synthesizer.py       # Szintetizáló ágens definíciója
├── tasks/
│   ├── search_task.py       # Keresési feladat
│   ├── read_task.py         # Olvasási feladat
│   └── synthesis_task.py    # Szintézis feladat
├── prompts/
│   ├── searcher_prompt.txt  # A kereső ágens promptja (verziózva!)
│   ├── reader_prompt.txt    # Az olvasó ágens promptja
│   └── synthesizer_prompt.txt
├── config/
│   └── config.yaml          # LLM-konfiguráció, paraméterek
├── logs/                    # Futtatási naplók
├── outputs/                 # Eredmények
├── .env                     # API kulcsok (NEM kerül Git-be!)
├── .gitignore               # .env és logs/ kizárása
├── requirements.txt         # Python-függőségek (verziószámokkal!)
└── main.py                  # Fő futtatási script
```

```bash
# .gitignore
.env
logs/
outputs/
__pycache__/
```

**Fontos:** Az API kulcsokat **soha** ne commitold a Git repository-ba! A `.env` fájl mindig a `.gitignore`-ban legyen.

### 12.9.4 A reprodukálhatóság korlátai

Őszintének kell lennem: az LLM-alapú ágensek **nem teljesen reprodukálhatók**. Még `temperature=0.0` mellett is előfordulhat, hogy két futtatás eltérő eredményt ad, mert:

- A modellek frissülhetnek a háttérben (az API-verziók változhatnak)
- A szerveroldali véletlenszám-generálás nem mindig determinisztikus
- A keresési eszközök eredményei időben változnak (új cikkek jelennek meg)

**Mit tehetsz?**

1. **Mentsd az eredményeket:** Ne csak a kódot tárold, hanem a kimeneteket is
2. **Futtatsd többször:** Ha fontos eredményről van szó, futtasd 3-5-ször és nézd a konzisztenciát
3. **Használj seed-et, ha elérhető:** Néhány API támogatja a `seed` paramétert a reprodukálhatósághoz
4. **Dokumentáld az eltéréseket:** Ha két futtatás eltérő eredményt ad, az is érdekes adat

---

## 12.10 Összefoglalás és következő lépések

Ebben a fejezetben megtanultad, hogyan építs AI ágenseket a kutatásodhoz:

**Amit megépítettünk:**

- Irodalomkutató ágens-csapat (CrewAI), amely automatikusan keres, olvas és szintetizál
- Adatfeldolgozó pipeline, amely heterogén adatokat egységesít
- Kísérlet-monitorozó ágens, amely folyamatosan figyel és riaszt
- Végponttól végpontig kutatási munkafolyamat, a hipotézistől a jelentésig

**Amit megtanultál:**

- Négy keretrendszer összehasonlítása: CrewAI, LangGraph, AutoGen, Claude Agent SDK
- MCP-vel adatforrások csatlakoztatása: fájlrendszer, adatbázis, API, műszerek
- Saját MCP szerver építésének alapjai
- Az emberi döntési pontok fontossága
- Monitoring, hibakeresés és naplózás

**A következő fejezetben** (13. fejezet) megtanuljuk, hogyan készíts saját kutatási eszközöket: Streamlit webalkalmazásokat, Gradio felületeket, és részletes MCP szervereket, amelyekkel az ágenseid még hatékonyabbá válnak.

**Gyakorlati javaslat:** Ne próbáld meg egyszerre az egész fejezetet implementálni. Kezdd az irodalomkutató ágenssel (12.3.1) --- ez a leggyorsabb siker-élmény. Ha az működik, építsd ki az adatfeldolgozó pipeline-t. És csak aztán gondolkodj a teljes kutatási munkafolyamaton.

> **Gábor, a csoportvezető** két héttel később: a hétfő reggeli irodalomkutatás most 15 percébe kerül --- megnyitja az emailjét, elolvassa az ágens által készített összefoglalót, és a csoportértekezletre már a tartalomra koncentrálhat, nem a keresésre. A PhD-hallgatói megtanulták az ágens karbantartását, és már a saját kutatási témájukra is adaptálták. A felszabadult idő? Gábor végre ráér a saját cikkét írni.
