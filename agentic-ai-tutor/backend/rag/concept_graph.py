"""Topic dependency graph for the AI in Scientific Research book (Hungarian).

Maps concepts to chapters and defines prerequisite relationships
so the system can guide students through topics in order.

Book structure:
  Part I   (Ch 1-4):   Ismerkedés az AI-val a kutatásban
  Part II  (Ch 5-7):   Mindennapi tudományos munka AI-val
  Part III (Ch 8-10):  No-code-tól a szakterület-specifikus AI-ig
  Part IV  (Ch 11-13): Ágentikus AI — Eszközökből munkatársak
  Part V   (Ch 14-16): Felelős AI-adoptáció vezetése
  Part VI  (Ch 17-19): Szakterületi alkalmazások
"""

from dataclasses import dataclass, field


@dataclass
class Concept:
    """A concept/topic in the book."""
    name: str
    chapter: int
    section: str = ""
    prerequisites: list[str] = field(default_factory=list)
    description: str = ""


# ---------------------------------------------------------------------------
# The concept graph -- topics and their prerequisites across 19 chapters
# ---------------------------------------------------------------------------
CONCEPT_GRAPH: dict[str, Concept] = {

    # =====================================================================
    # PART I: Ismerkedés az AI-val a kutatásban (Ch 1-4)
    # =====================================================================

    # ===== Chapter 1: Az AI forradalom a tudományos kutatásban =====
    "ai_fogalom": Concept(
        "Mesterséges intelligencia (AI)", 1, "1.1",
        [],
        "Mi az AI, miért fontos minden tudós számára, az AI spektrum a chatbottól az autonóm felfedezésig",
    ),
    "llm": Concept(
        "Nagy nyelvi modellek (LLM)", 1, "1.2",
        ["ai_fogalom"],
        "Hogyan működnek a nagy nyelvi modellek, transformer architektúra alapjai",
    ),
    "gepi_tanulas": Concept(
        "Gépi tanulás alapfogalmak", 1, "1.3",
        ["ai_fogalom"],
        "Felügyelt, felügyelet nélküli és megerősítéses tanulás alapjai",
    ),
    "mollick_4_szabaly": Concept(
        "Mollick 4 szabálya", 1, "1.4",
        ["ai_fogalom"],
        "Keretrendszer az AI kutatási alkalmazásához: mindig hívd meg, légy a hurokban, stb.",
    ),
    "ai_spektrum": Concept(
        "AI autonómia-spektrum (5 szint)", 1, "1.5",
        ["ai_fogalom", "llm"],
        "Chatbot → kopilot → ágens → autonóm felfedezés szintek",
    ),

    # ===== Chapter 2: Társalgási AI — Az első kutatási partnered =====
    "prompt_engineering": Concept(
        "Prompt engineering", 2, "2.1",
        ["llm"],
        "9 NASA prompt pattern, hatékony promptolás technikái tudósoknak",
    ),
    "hallucinacio": Concept(
        "Hallucináció", 2, "2.2",
        ["llm"],
        "Mikor és miért generál az LLM hamis információt, felismerés és megelőzés",
    ),
    "token": Concept(
        "Token és tokenizáció", 2, "2.3",
        ["llm"],
        "Szöveg feldarabolása tokenekre, hatása a költségre és teljesítményre",
    ),
    "kontextusablak": Concept(
        "Kontextusablak", 2, "2.4",
        ["token"],
        "Maximális beviteli hossz, kontextus-kezelési stratégiák",
    ),
    "homerseklet": Concept(
        "Hőmérséklet és top-p paraméterek", 2, "2.5",
        ["llm", "token"],
        "Generálási paraméterek: hőmérséklet, top-p, rendszerprompt hatásai",
    ),
    "platform_valasztas": Concept(
        "Platform-választás (Claude, ChatGPT, Gemini)", 2, "2.6",
        ["llm", "prompt_engineering"],
        "2026-os LLM platformok összehasonlítása kutatási szempontból",
    ),
    "bizonyitek_verifikacio": Concept(
        "Bizonyíték-minőség és verifikáció", 2, "2.7",
        ["hallucinacio", "prompt_engineering"],
        "Keresztellenőrzés, kritikus gondolkodás, a másodpilóta filozófia",
    ),

    # ===== Chapter 3: AI a tudományos írásban és kommunikációban =====
    "irodalom_attekintes": Concept(
        "Irodalomáttekintés AI-val", 3, "3.1",
        ["prompt_engineering", "hallucinacio"],
        "Összefoglalás, kulcsmegállapítások, rések azonosítása AI segítségével",
    ),
    "kezirat_szerkesztes": Concept(
        "Kézirat írás és szerkesztés", 3, "3.2",
        ["prompt_engineering"],
        "Nyelvtan, érthetőség, folyóirat-adaptáció, bírálói vélemények megválaszolása",
    ),
    "hivatkozas_hallucinacio": Concept(
        "Hivatkozás-hallucináció", 3, "3.3",
        ["hallucinacio", "irodalom_attekintes"],
        "Fabrikált hivatkozások felismerése és megelőzése",
    ),
    "tudomanyos_kommunikacio": Concept(
        "Tudománykommunikáció AI-val", 3, "3.4",
        ["kezirat_szerkesztes"],
        "Népszerű cikkek, közösségi média, sajtóközlemények, pályázatírás",
    ),

    # ===== Chapter 4: AI-vel végzett adatelemzés — Kódolás nélkül =====
    "adatelemzes": Concept(
        "Adatelemzés chatfelületen", 4, "4.1",
        ["prompt_engineering"],
        "Adatok feltöltése és elemzése chat-felületen: CSV, Excel, kép, PDF",
    ),
    "hipotezisvizsgalat": Concept(
        "Hipotézisvizsgálat AI-val", 4, "4.2",
        ["adatelemzes"],
        "Leíró statisztika, hipotézisvizsgálat, regresszió beszélgetésben",
    ),
    "vizualizacio": Concept(
        "Adatvizualizáció AI-val", 4, "4.3",
        ["adatelemzes"],
        "Gyors ábrák és publikáció-minőségű grafikonok AI segítségével",
    ),
    "code_interpreter": Concept(
        "Code Interpreter és Artifacts", 4, "4.4",
        ["adatelemzes", "platform_valasztas"],
        "Platform-specifikus kód-futtatási képességek adatelemzéshez",
    ),

    # =====================================================================
    # PART II: Mindennapi tudományos munka AI-val (Ch 5-7)
    # =====================================================================

    # ===== Chapter 5: AI kódolási asszisztensek =====
    "python": Concept(
        "Python programozás AI-val", 5, "5.1",
        ["adatelemzes"],
        "Környezet beállítása, Python alapok AI segítségével, NumPy, SciPy, Pandas, Matplotlib",
    ),
    "git": Concept(
        "Git verziókezelés", 5, "5.2",
        ["python"],
        "AI-vezérelt verziókezelés, commit, branch, együttműködés",
    ),
    "jupyter": Concept(
        "Jupyter notebook", 5, "5.3",
        ["python"],
        "Interaktív tudományos jegyzetfüzet kóddal, szöveggel és ábrákkal",
    ),
    "claude_code": Concept(
        "Claude Code", 5, "5.4",
        ["python", "prompt_engineering"],
        "Anthropic terminál-alapú AI kódolási asszisztens",
    ),
    "copilot": Concept(
        "GitHub Copilot", 5, "5.5",
        ["python"],
        "GitHub AI kódkiegészítő VS Code-ban és más szerkesztőkben",
    ),
    "cursor": Concept(
        "Cursor és Windsurf", 5, "5.6",
        ["python"],
        "AI-natív kódszerkesztők teljes projektkezeléssel",
    ),
    "api": Concept(
        "API fogalom", 5, "5.7",
        ["python"],
        "Alkalmazásprogramozási interfész: programok közötti kommunikáció",
    ),

    # ===== Chapter 6: AI-támogatott matematikai modellezés =====
    "ode_pde": Concept(
        "ODE és PDE megoldás AI-val", 6, "6.1",
        ["python", "jupyter"],
        "Közönséges és parciális differenciálegyenletek kóddá fordítása AI segítségével",
    ),
    "sympy": Concept(
        "Szimbolikus számítás (SymPy)", 6, "6.2",
        ["python"],
        "Szimbolikus matematika Python-ban: egyszerűsítés, deriválás, integrálás",
    ),
    "monte_carlo": Concept(
        "Monte Carlo szimuláció", 6, "6.3",
        ["python"],
        "Sztochasztikus szimulációk, valószínűségi modellezés",
    ),
    "optuna": Concept(
        "Automatikus modell-kalibráció (Optuna)", 6, "6.4",
        ["python", "monte_carlo"],
        "Hiperparaméter-optimalizálás, Bayes-i módszerek, érzékenységvizsgálat",
    ),
    "pysr": Concept(
        "Szimbolikus regresszió (PySR)", 6, "6.5",
        ["python", "gepi_tanulas"],
        "Egyenlet-felfedezés adatokból, LLM-vezérelt szimbolikus regresszió",
    ),
    "pinns": Concept(
        "Fizika-informált neurális hálózatok (PINNs)", 6, "6.6",
        ["ode_pde", "gepi_tanulas"],
        "Neurális hálózatok fizikai egyenletekkel korlátozva, szurrogát modellek",
    ),

    # ===== Chapter 7: Adat-pipeline-ok és automatizálás =====
    "pipeline": Concept(
        "Pipeline koncepció", 7, "7.1",
        ["python"],
        "Adatfeldolgozási csővezeték: bevitel → tisztítás → transzformáció → elemzés → kimenet",
    ),
    "automatizalas": Concept(
        "Automatizálás", 7, "7.2",
        ["pipeline"],
        "Automatizálási lehetőségek azonosítása, adatbevitel, validáció",
    ),
    "batch_feldolgozas": Concept(
        "Batch (kötegelt) feldolgozás", 7, "7.3",
        ["pipeline", "python"],
        "Nagy mennyiségű adat kötegelt feldolgozása, párhuzamosítás",
    ),
    "cron": Concept(
        "Ütemezett feladatok (cron, watchdog)", 7, "7.4",
        ["automatizalas"],
        "Időzített futtatás, fájlfigyelés, monitoring és riasztás",
    ),
    "reprodukalhato_pipeline": Concept(
        "Reprodukálható pipeline-ok", 7, "7.5",
        ["pipeline", "git"],
        "Konténerizáció, környezetkezelés, Dagster, Nextflow",
    ),

    # =====================================================================
    # PART III: No-code-tól a szakterület-specifikus AI-ig (Ch 8-10)
    # =====================================================================

    # ===== Chapter 8: Vizuális programozás és munkafolyamat-tervezés =====
    "n8n": Concept(
        "n8n vizuális automatizálás", 8, "8.1",
        ["automatizalas"],
        "Általános célú vizuális workflow-építés triggerekkel és akciókkal",
    ),
    "knime": Concept(
        "KNIME vizuális adattudomány", 8, "8.2",
        ["adatelemzes"],
        "Vizuális adattudományi platform, AI Assistant, workflow-ok",
    ),
    "langflow": Concept(
        "LangFlow vizuális LLM pipeline", 8, "8.3",
        ["llm", "prompt_engineering"],
        "Drag-and-drop LLM pipeline-tervezés, RAG chatbot prototípus",
    ),
    "node_red": Concept(
        "Node-RED IoT workflow-ok", 8, "8.4",
        ["automatizalas"],
        "IoT és szenzor-adat workflow-ok vizuális szerkesztése",
    ),
    "orange": Concept(
        "Orange gépi tanulás", 8, "8.5",
        ["gepi_tanulas", "adatelemzes"],
        "Vizuális gépi tanulás nem-programozóknak",
    ),

    # ===== Chapter 9: RAG — Tanítsuk meg az AI-t a saját adatainkra =====
    "rag": Concept(
        "RAG (Retrieval-Augmented Generation)", 9, "9.1",
        ["llm", "prompt_engineering"],
        "Dokumentum-alapú válaszgenerálás architektúrája és alkalmazása",
    ),
    "embedding": Concept(
        "Embedding (beágyazás)", 9, "9.2",
        ["llm", "token"],
        "Szöveg vektorrá alakítása, szemantikus hasonlóság, embedding modellek",
    ),
    "vektor_tar": Concept(
        "Vektor-tár (vector store)", 9, "9.3",
        ["embedding"],
        "Vektorok tárolása és gyors keresése: ChromaDB, Pinecone, FAISS",
    ),
    "chunking": Concept(
        "Chunking stratégiák", 9, "9.4",
        ["rag", "kontextusablak"],
        "Dokumentumok feldarabolása: fix méret, szemantikus, hierarchikus chunking",
    ),
    "fine_tuning": Concept(
        "Fine-tuning (finomhangolás)", 9, "9.5",
        ["llm", "gepi_tanulas"],
        "Encoder és decoder fine-tuning, mikor kell RAG helyett fine-tuning",
    ),
    "bertscore": Concept(
        "RAG minőségértékelés (BERTScore)", 9, "9.6",
        ["rag", "embedding"],
        "BERTScore, ROUGE, 3 szintű RAG minőségi keretrendszer",
    ),

    # ===== Chapter 10: Digitális ikrek =====
    "digitalis_iker": Concept(
        "Digitális iker koncepció", 10, "10.1",
        ["ai_fogalom", "python"],
        "Valós rendszerek virtuális másolatai: adatforrás → modell → vizualizáció → visszacsatolás",
    ),
    "nvidia_omniverse": Concept(
        "NVIDIA Omniverse", 10, "10.2",
        ["digitalis_iker"],
        "Fizika-alapú szimulációs platform digitális ikrekhez",
    ),
    "intertwin": Concept(
        "interTwin", 10, "10.3",
        ["digitalis_iker"],
        "EU nyílt forráskódú digitális iker platform tudományos alkalmazásokhoz",
    ),
    "dt_epitese": Concept(
        "Digitális iker építése AI-val", 10, "10.4",
        ["digitalis_iker", "pipeline", "ode_pde"],
        "Egyszerű digitális iker létrehozása AI segítségével lépésről lépésre",
    ),

    # =====================================================================
    # PART IV: Ágentikus AI — Eszközökből munkatársak (Ch 11-13)
    # =====================================================================

    # ===== Chapter 11: Az AI ágensek megértése =====
    "agens": Concept(
        "AI ágens fogalma", 11, "11.1",
        ["llm", "prompt_engineering", "ai_spektrum"],
        "Huang 10 jellemzője, az autonómia spektruma, eszköztől az ágensig",
    ),
    "react": Concept(
        "ReACT minta", 11, "11.2",
        ["agens"],
        "Gondolat → Cselekvés → Megfigyelés → ismétlés ciklus",
    ),
    "mcp": Concept(
        "MCP (Model Context Protocol)", 11, "11.3",
        ["agens", "api"],
        "Univerzális szabvány AI és külső eszközök összekapcsolására, 10,000+ szerver",
    ),
    "multi_agens": Concept(
        "Multi-ágens rendszerek", 11, "11.4",
        ["agens"],
        "Koordináció, kommunikáció, konfliktus-feloldás több ágens között",
    ),
    "het_retegu_architektura": Concept(
        "7 rétegű ágens-architektúra", 11, "11.5",
        ["agens", "react"],
        "Rétegelt felépítés: észlelés, memória, tervezés, cselekvés, tanulás, együttműködés, biztonság",
    ),
    "agens_biztonsag": Concept(
        "Ágens biztonság és korlátok", 11, "11.6",
        ["agens", "het_retegu_architektura"],
        "Ember-a-hurokban, korlátok beállítása, költségek és méltányosság",
    ),

    # ===== Chapter 12: AI ágensek építése kutatáshoz =====
    "crewai": Concept(
        "CrewAI", 12, "12.1",
        ["agens", "multi_agens", "python"],
        "Szerep-alapú ágens-csapatok építése, legkönnyebb belépési pont",
    ),
    "langgraph": Concept(
        "LangGraph", 12, "12.2",
        ["agens", "python"],
        "Gráf-alapú ágens-munkafolyamatok, legrugalmasabb keretrendszer",
    ),
    "autogen": Concept(
        "AutoGen", 12, "12.3",
        ["multi_agens", "python"],
        "Microsoft társalgási multi-ágens keretrendszer",
    ),
    "claude_agent_sdk": Concept(
        "Claude Agent SDK", 12, "12.4",
        ["agens", "python", "claude_code"],
        "Anthropic profi ágens-fejlesztő eszköztár",
    ),
    "agens_pipeline": Concept(
        "Ágentikus kutatási pipeline-ok", 12, "12.5",
        ["crewai", "mcp", "pipeline"],
        "Irodalomkutató, adatfeldolgozó, kísérlet-figyelő ágensek összekapcsolása",
    ),

    # ===== Chapter 13: Saját programok és eszközök készítése =====
    "streamlit": Concept(
        "Streamlit alkalmazások", 13, "13.1",
        ["python"],
        "Interaktív webes adat-alkalmazások percek alatt Python-ban",
    ),
    "gradio": Concept(
        "Gradio ML felületek", 13, "13.2",
        ["python", "gepi_tanulas"],
        "ML modellek interaktív webes felülete, gyors prototípus",
    ),
    "mcp_szerver": Concept(
        "MCP szerver készítés", 13, "13.3",
        ["mcp", "python", "api"],
        "Saját adatok és eszközök AI-elérhetővé tétele MCP szerverrel",
    ),
    "eszkoz_megosztas": Concept(
        "Eszközök megosztása (GitHub)", 13, "13.4",
        ["git", "streamlit"],
        "Kutatási szoftverek megosztása dokumentációval és verziókezeléssel",
    ),

    # =====================================================================
    # PART V: Felelős AI-adoptáció vezetése (Ch 14-16)
    # =====================================================================

    # ===== Chapter 14: Az AI-val felszerelt kutatólabor =====
    "ai_stack": Concept(
        "Tudományos AI stack", 14, "14.1",
        ["platform_valasztas", "python"],
        "2026-os eszközkészlet: ingyenes szintek → előfizetések → API → HPC",
    ),
    "gdpr": Concept(
        "GDPR a kutatásban", 14, "14.2",
        ["ai_stack"],
        "Adatvédelem, mit küldj felhőbe vs. lokális feldolgozás",
    ),
    "eu_ai_act": Concept(
        "EU AI Act", 14, "14.3",
        ["gdpr", "ai_fogalom"],
        "AI osztályozás, kötelezettségek, megfelelés kutatóknak",
    ),
    "beszerzes": Concept(
        "AI beszerzési útmutató", 14, "14.4",
        ["ai_stack", "eu_ai_act"],
        "Platform-kiválasztás, EU MCC-AI, EDUCAUSE ellenőrzőlista, TCO elemzés",
    ),
    "komondor": Concept(
        "Komondor szuperszámítógép", 14, "14.5",
        ["ai_stack"],
        "5 PFLOPS HPC hozzáférés, GPU klaszter, kutatási számítási erőforrások",
    ),

    # ===== Chapter 15: AI az egyetemen =====
    "sarps": Concept(
        "SARPS keretrendszer", 15, "15.1",
        ["ai_fogalom", "prompt_engineering"],
        "Six Assessment Redesign Pivotal Strategies: értékelés-tervezés AI korában",
    ),
    "posztplagium": Concept(
        "Posztplágium", 15, "15.2",
        ["hallucinacio", "kezirat_szerkesztes"],
        "Hibrid ember-AI írás mint új norma (Eaton), detektálás és szabályozás",
    ),
    "valtozasmenedzsment": Concept(
        "Változásmenedzsment", 15, "15.3",
        ["ai_fogalom"],
        "Oktatói ellenállás kezelése, Rogers innovációdiffúzió, képzési modellek",
    ),
    "bloom_2_szigma": Concept(
        "Bloom 2-szigma probléma", 15, "15.4",
        ["ai_fogalom", "sarps"],
        "AI mint szókratészi tutor: személyre szabott oktatás nagy léptékben",
    ),
    "egyetemi_esettanulmanyok": Concept(
        "Egyetemi AI esettanulmányok", 15, "15.5",
        ["ai_stack", "valtozasmenedzsment"],
        "U of Florida, Helsinki, Northeastern, Johns Hopkins modellek",
    ),

    # ===== Chapter 16: Etika, reprodukálhatóság és az AI jövője =====
    "kutatasi_integritas": Concept(
        "Kutatási integritás az AI korában", 16, "16.1",
        ["hallucinacio", "hivatkozas_hallucinacio"],
        "Fabrikált hivatkozások, képmanipuláció, szintetikus adatok visszaélése",
    ),
    "reprodukalhatosag": Concept(
        "Reprodukálhatóság", 16, "16.2",
        ["pipeline", "git"],
        "Nem-determinisztikus kimenetek dokumentálása, verzió-rögzítés, prompt-naplózás",
    ),
    "etika": Concept(
        "AI etika a kutatásban", 16, "16.3",
        ["eu_ai_act", "kutatasi_integritas"],
        "Szerzőség, torzítás, COPE irányelvek, folyóirat-politikák",
    ),
    "felelosseg_elvek": Concept(
        "Felelős AI elvek", 16, "16.4",
        ["mollick_4_szabaly", "etika"],
        "NASA 5 elve, EUA értékalapú megközelítés, személyes etikai keretrendszer",
    ),
    "ai_jovo": Concept(
        "Az AI jövője a tudományban", 16, "16.5",
        ["agens", "etika"],
        "Négy forgatókönyv, autonóm felfedezés, a tudós változó szerepe",
    ),

    # =====================================================================
    # PART VI: Szakterületi alkalmazások (Ch 17-19)
    # =====================================================================

    # ===== Chapter 17: Precíziós mezőgazdaság =====
    "precizios_mezogazdasag": Concept(
        "Precíziós mezőgazdaság és AI", 17, "17.1",
        ["ai_fogalom", "gepi_tanulas"],
        "AI alkalmazások a mezőgazdaságban: érzékelés, elemzés, beavatkozás",
    ),
    "ndvi": Concept(
        "NDVI és vegetációs indexek", 17, "17.2",
        ["precizios_mezogazdasag", "vizualizacio"],
        "Normalized Difference Vegetation Index, növényzet-állapot felmérés",
    ),
    "hozamterkepzes": Concept(
        "Hozamtérképezés", 17, "17.3",
        ["precizios_mezogazdasag", "adatelemzes"],
        "Területi hozam-variabilitás térképezése, kezelési zónák",
    ),
    "iot_szenzorok": Concept(
        "IoT szenzorok a mezőgazdaságban", 17, "17.4",
        ["precizios_mezogazdasag", "node_red", "pipeline"],
        "Talaj-, időjárás- és növényszenzorok, adatgyűjtő hálózatok",
    ),
    "mezogazdasagi_dt": Concept(
        "Mezőgazdasági digitális iker", 17, "17.5",
        ["precizios_mezogazdasag", "digitalis_iker"],
        "Parcellaszintű digitális iker növénytermesztéshez",
    ),

    # ===== Chapter 18: Hidroinformatika =====
    "hidroinformatika": Concept(
        "Hidroinformatika és AI", 18, "18.1",
        ["ai_fogalom", "python", "ode_pde"],
        "Informatika alkalmazása vízgazdálkodásban, hidrológiai modellezés AI-val",
    ),
    "vizgyujto": Concept(
        "Vízgyűjtő modellezés", 18, "18.2",
        ["hidroinformatika"],
        "Vízgyűjtő-terület lehatárolás, lefolyásmodellezés, csapadék-lefolyás",
    ),
    "dem": Concept(
        "DEM (digitális terepmodell)", 18, "18.3",
        ["hidroinformatika"],
        "Domborzatmodellek előállítása, feldolgozása és hidrológiai alkalmazása",
    ),
    "arviz_elorejelzes": Concept(
        "Árvíz-előrejelzés AI-val", 18, "18.4",
        ["hidroinformatika", "gepi_tanulas", "vizgyujto"],
        "Gépi tanulás és fizikai modellek kombinálása árvíz-előrejelzéshez",
    ),
    "saint_venant": Concept(
        "Saint-Venant egyenletek", 18, "18.5",
        ["ode_pde", "hidroinformatika"],
        "Sekélyvízi egyenletek numerikus megoldása, 1D/2D áramlásmodellezés",
    ),
    "hidro_dt": Concept(
        "Hidrológiai digitális iker", 18, "18.6",
        ["hidroinformatika", "digitalis_iker", "arviz_elorejelzes"],
        "Valós idejű vízügyi monitoring és előrejelzés digitális ikerrel",
    ),

    # ===== Chapter 19: Térinformatika és távérzékelés =====
    "terinformatika": Concept(
        "Térinformatika (GIS) és AI", 19, "19.1",
        ["ai_fogalom", "python", "vizualizacio"],
        "Térinformatikai rendszerek AI-val, térbeli elemzés automatizálása",
    ),
    "gis": Concept(
        "GIS szoftverek és könyvtárak", 19, "19.2",
        ["terinformatika"],
        "QGIS, ArcGIS, GeoPandas, Rasterio, Folium",
    ),
    "taverzekeles": Concept(
        "Távérzékelés", 19, "19.3",
        ["terinformatika", "ndvi"],
        "Műholdas és drónos adatgyűjtés, Sentinel, Landsat, spektrális elemzés",
    ),
    "geostatisztika": Concept(
        "Geostatisztika", 19, "19.4",
        ["terinformatika", "adatelemzes", "hipotezisvizsgalat"],
        "Variogram, kriging, térbeli interpoláció, bizonytalanság-becslés",
    ),
    "autonom_gis": Concept(
        "Autonóm GIS ágens", 19, "19.5",
        ["terinformatika", "agens", "gis"],
        "LLM-vezérelt térinformatikai elemzés, természetes nyelvű térbeli lekérdezés",
    ),
}


def get_prerequisites(concept_key: str) -> list[str]:
    """Get all prerequisite concepts (recursive) for a given concept."""
    visited = set()
    result = []

    def _walk(key: str):
        if key in visited or key not in CONCEPT_GRAPH:
            return
        visited.add(key)
        for prereq in CONCEPT_GRAPH[key].prerequisites:
            _walk(prereq)
            if prereq not in result:
                result.append(prereq)

    _walk(concept_key)
    return result


def get_concepts_for_chapter(chapter: int) -> list[str]:
    """Get all concept keys for a given chapter number."""
    return [k for k, v in CONCEPT_GRAPH.items() if v.chapter == chapter]


def get_concepts_for_part(part: int) -> list[str]:
    """Get all concept keys for a given part number (I-VI).

    Part I:   Ch 1-4
    Part II:  Ch 5-7
    Part III: Ch 8-10
    Part IV:  Ch 11-13
    Part V:   Ch 14-16
    Part VI:  Ch 17-19
    """
    part_ranges = {
        1: range(1, 5),
        2: range(5, 8),
        3: range(8, 11),
        4: range(11, 14),
        5: range(14, 17),
        6: range(17, 20),
    }
    chapters = part_ranges.get(part, range(0))
    return [k for k, v in CONCEPT_GRAPH.items() if v.chapter in chapters]


def get_concept_tree() -> dict:
    """Return the full concept graph as a serializable dict."""
    return {
        key: {
            "name": c.name,
            "chapter": c.chapter,
            "section": c.section,
            "prerequisites": c.prerequisites,
            "description": c.description,
        }
        for key, c in CONCEPT_GRAPH.items()
    }
