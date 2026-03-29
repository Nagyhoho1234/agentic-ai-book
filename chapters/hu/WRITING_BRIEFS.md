# Fejezet-Írási Útmutató — Magyar E-book
# Chapter Writing Briefs — Hungarian E-book

## Általános szabályok / General Rules

- **Nyelv:** Magyar, angol szakkifejezésekkel (lásd VERSIONS.md terminológia policy)
- **Stílus:** Gyakorlatias, közvetlen, tudós-tudósnak. Nem programozóknak írunk.
- **Megszólítás:** Tegező forma ("Próbáld ki...", "Gondolj arra...")
- **Minden fejezet önállóan is olvasható**, de épít az előzőkre
- **Nincs oldalszám-korlát** — annyi legyen, amennyi kell
- **Debreceni példák** minden fejezetben legalább 1-2 konkrét
- **Fájlnév konvenció:** `ch01_cim.md`, `ch02_cim.md`, stb.

---

## TERMINOLÓGIA TULAJDONOS-TÁBLA
## (Melyik fejezet definiál először egy fogalmat)

| Fogalom | Első definíció | Utána használat |
|---------|---------------|-----------------|
| AI / mesterséges intelligencia | Ch 1 | mindenhol |
| LLM (nagy nyelvi modell) | Ch 1 | mindenhol |
| Hallucináció | Ch 2 | Ch 3, 9, 16 |
| Prompt / prompt engineering | Ch 2 | mindenhol |
| Token, kontextusablak | Ch 2 | Ch 5, 9, 11 |
| Hőmérséklet (temperature), top-p | Ch 2 | Ch 5 |
| RAG (Retrieval-Augmented Generation) | Ch 9 | Ch 11, 12 |
| Agent / ágens | Ch 11 | Ch 12, 13, 14 |
| MCP (Model Context Protocol) | Ch 11 | Ch 12, 13 |
| Multi-agent system | Ch 11 | Ch 12 |
| ReACT pattern | Ch 11 | Ch 12 |
| Pipeline (adatfeldolgozási csővezeték) | Ch 7 | Ch 9, 12 |
| Digitális iker / digital twin | Ch 10 | Ch 14 |
| Fine-tuning (finomhangolás) | Ch 9 | Ch 16 |
| Embedding / beágyazás | Ch 9 | Ch 11 |
| Vektor-tár (vector store) | Ch 9 | - |
| Git / verziókezelés | Ch 5 | Ch 7, 13 |
| Python | Ch 5 | Ch 6, 7, 9, 12, 13 |
| Jupyter notebook | Ch 5 | Ch 6 |
| API | Ch 5 | Ch 7, 9, 11, 12, 13 |
| GDPR / EU AI Act | Ch 14 | Ch 16 |
| Posztplágium | Ch 16 | - |
| SARPS keretrendszer | Ch 15 | - |

---

## FEJEZET-HATÁROK ÉS ÍRÁSI UTASÍTÁSOK

### ═══════════════════════════════════════
### PART I: Ismerkedés az AI-val a kutatásban
### ═══════════════════════════════════════

---

### Fejezet 1: Az AI forradalom a tudományos kutatásban
**Fájl:** `ch01_ai_forradalom.md`

**MI VAN BENNE:**
- Miért fontos az AI MINDEN tudós számára (nem csak informatikusoknak)
- A 80/20 probléma: kutatási idő 80%-a adatrendezés (Gentemann et al., 2021)
- AI spektrum: chatbottól az autonóm felfedezésig (5 szint bemutatása)
- Áttörő példák: AlphaFold 3, AI Scientist (Nature, 2026), Berkeley A-Lab, Google Co-Scientist, CRISPR-GPT
- Nehezedik-e a tudomány? (OECD: csökkenő disruptivitás, nagyobb csapatok)
- Mollick 4 szabálya (keretrendszer az egész könyvhöz)
- Debreceni kontextus: 14 kar, Komondor szuperszámítógép, BMW gyár, AI stratégia
- Hogyan használd ezt a könyvet: útvonalak különböző tudósoknak

**MI NINCS BENNE (más fejezetben van):**
- Konkrét promptolási technikák → Ch 2
- Konkrét eszközök bemutatása → Ch 2, 5
- Etikai kérdések részletesen → Ch 16
- Python/kódolás → Ch 5

**FORRÁSOK:** EM Ch 1-3, KH Ch 1, OECD Ch 1-5, NAS Ch 1, Debrecen research report

**DEBRECEN:** Komondor 5 PFLOPS, 14 kar, "Modern MI" kurzus, BMW EUR 2Mrd, Magyar AI Stratégia 2025-2030, AI Koalíció

**HANGNEM:** Inspiráló, de nem hype-oló. "Az AI nem varázslat, hanem eszköz — de olyan eszköz, ami mindent megváltoztat."

---

### Fejezet 2: Társalgási AI — Az első kutatási partnered
**Fájl:** `ch02_tarsalgasi_ai.md`

**MI VAN BENNE:**
- LLM alapfogalmak: token, kontextusablak, hallucináció (EZEKET ITT DEFINIÁLJUK)
- Platform-választás 2026: Claude, ChatGPT, Gemini, Copilot — összehasonlító táblázat
- 9 NASA prompt pattern adaptálva általános tudományra:
  1. Recept minta (Recipe)
  2. Kimenet-automatizáló (Output Automator)
  3. Persona minta
  4. Fordított interakció (Flipped Interaction)
  5. Kérdés-finomítás (Question Refinement)
  6. Alternatív megközelítés
  7. Kognitív ellenőrző (Cognitive Verifier)
  8. Tényellenőrző lista (Fact Check List)
  9. Kontextus-kezelő (Context Manager)
- Minták kombinálása összetett feladatokhoz
- Paraméterek: hőmérséklet, top-p, rendszerprompt
- **Bizonyíték-minőség és verifikáció** (kiterjesztett szekció):
  - Mikor gyenge módszertanilag egy AI válasz?
  - Keresztellenőrzés hiteles forrásokkal
  - Az átlátszatlanság problémája: gördülékeny válaszok, rejtett hibákkal
  - Kritikus gondolkodás az AI korában
  - A "másodpilóta" filozófia: soha ne hagyd az AI-t egyedül repülni

**MI NINCS BENNE:**
- Tudományos írás konkrétan → Ch 3
- Adatelemzés feltöltéssel → Ch 4
- Kódolás, terminál → Ch 5
- RAG, saját adatok → Ch 9
- Etika részletesen → Ch 16

**FORRÁSOK:** NASA Cookbook (9 minta), HQ Ch 1, EM Ch 3, OECD Ch 21+26, AI Snake Oil

**DEBRECEN:** "Modern MI" kurzus mint kiindulópont, példák debreceni kutatási területekről

---

### Fejezet 3: AI a tudományos írásban és kommunikációban
**Fájl:** `ch03_tudomanyos_iras.md`

**MI VAN BENNE:**
- Irodalomáttekintés AI-val: összefoglalás, kulcsmegállapítások, rések azonosítása
- Kézirat írás és szerkesztés: nyelvtan, érthetőség, cím, folyóirat-adaptáció
- Bírálói vélemények megválaszolása: stratégiák és sablonok
- Hibák felismerése saját és mások munkájában
- Kutatási pályázatok és grant-javaslatok írása
- Tudománykommunikáció: népszerű cikkek, közösségi média, sajtóközlemények
- Kísérleti tervek és kérdőívek készítése AI-val
- Hivatkozás-hallucináció: felismerés és megelőzés
- **[Etika doboz: "Lásd Ch 16 a teljes etikai tárgyalásért"]**

**MI NINCS BENNE:**
- Promptolási technikák általában → Ch 2 (már definiálva)
- Adatelemzés → Ch 4
- AI írásdetektálás, posztplágium → Ch 16
- Folyóirat-politikák részletesen → Ch 16

**FORRÁSOK:** HQ Ch 2-12 (ELSŐDLEGES), EM Ch 5, OECD Ch 6-8

**DEBRECEN:** Példák magyar nyelvű tudományos írásra, DE folyóiratok, MTMT

---

### Fejezet 4: AI-vel végzett adatelemzés — Kódolás nélkül
**Fájl:** `ch04_adatelemzes_kod_nelkul.md`

**MI VAN BENNE:**
- Adatok feltöltése és elemzése chat-felületen: CSV, Excel, kép, PDF
- AI-alapú exploratív adatelemzés
- Statisztikai elemzés beszélgetésben: leíró stat, hipotézisvizsgálat, regresszió
- Adatvizualizáció: gyors ábrák és publikáció-minőségű grafikonok
- Platform-specifikus képességek: Code Interpreter, Artifacts, Gemini+Sheets
- Mikor nem elég a no-code megközelítés → átvezetés Ch 5-re
- **Olvasási útvonalak** (fejezet végén):
  - Társadalomtudós: Ch 1-4 → Ch 8 → Ch 9 → Ch 15-16
  - Laborbiológus: Ch 1-5 → Ch 7 → Ch 9 → Ch 12 → Ch 15-16
  - Számítógépes/fizikai tudós: Ch 1-6 → Ch 7 → Ch 9 → Ch 10 → Ch 11-12 → Ch 15-16
  - Labor/csoportvezető: Ch 1-4 → Ch 14 → Ch 15 → Ch 16
  - Oktatásközpontú: Ch 1-4 → Ch 15 → Ch 16
  - Teljes út: minden fejezet sorrendben

**MI NINCS BENNE:**
- Promptolás általában → Ch 2
- Python kódolás → Ch 5
- Automatizált pipeline-ok → Ch 7
- Vizuális programozás (KNIME, Orange) → Ch 8

**FORRÁSOK:** HQ Ch 9-10, SL Ch 4-5+8+15, OECD Ch 9, KNIME (kontextus)

**DEBRECEN:** Példa valós debreceni kutatási adatsorral

---

### ═══════════════════════════════════════
### PART II: Mindennapi tudományos munka AI-val
### ═══════════════════════════════════════

---

### Fejezet 5: AI kódolási asszisztensek — Kód írása programozás nélkül
**Fájl:** `ch05_kodolasi_asszisztensek.md`

**MI VAN BENNE:**
- Paradigmaváltás: leírod mit akarsz vs. szintaxis tanulás
- Környezet beállítása AI segítségével: Python, pip, venv, VS Code
- 2026 eszköztár: Claude Code, GitHub Copilot, Cursor, Windsurf, Codex
  - Összehasonlító táblázat (EZ AZ EGYETLEN HELY a teljes összehasonlításnak)
- Első AI-asszisztált Python scriptek:
  - Adattisztítás
  - Publikáció-minőségű ábrák
  - Modell illesztés mérési adatokra
  - Fájlok kötegelt feldolgozása
- A visszacsatolási hurok: leírás → generálás → tesztelés → finomítás
- Git verziókezelés (AI-vezérelt) — ITT DEFINIÁLJUK
- Jupyter notebook mint tudós laboratóriumi füzet — ITT DEFINIÁLJUK
- Python kulcskönyvtárak: NumPy, SciPy, Pandas, Matplotlib, scikit-learn
- API fogalom bevezetése — ITT DEFINIÁLJUK

**MI NINCS BENNE:**
- Matematikai modellezés → Ch 6
- Pipeline-ok, automatizálás → Ch 7
- Vizuális programozás → Ch 8
- Ágens-keretrendszerek → Ch 12
- Eszközépítés (Streamlit) → Ch 13
- Környezet-beállítás részletek → Appendix A

**FORRÁSOK:** SL Section I, Learn AI Python (Porter&Zingaro), GitHub Copilot Practice (Wienholt), Copilot Handbook (Bos&Pagels), NASA kód-architektúra

**DEBRECEN:** Komondor hozzáférés, NVIDIA DLI képzési központ

---

### Fejezet 6: AI-támogatott matematikai modellezés és szimuláció
**Fájl:** `ch06_matematikai_modellezes.md`

**MI VAN BENNE:**
- **CORE (mindenki számára):**
  - Kutatási kérdéstől a matematikai megfogalmazásig AI-val
  - Egyenletek kóddá fordítása: ODE-k, PDE-k, optimalizálás
  - AI mint fordító: egyenletből Python egy prompttal
  - Szimbolikus számítás SymPy-val
  - Szimulációs modellek: ágens-alapú, Monte Carlo, sztochasztikus
  - Automatikus modell-kalibráció: Optuna, Bayes-i módszerek, érzékenységvizsgálat
- **ADVANCED (dobozban, opcionális, számítógépes tudósoknak):**
  - Egyenlet-felfedezés: szimbolikus regresszió PySR-rel
  - LLM-vezérelt szimbolikus regresszió fizikai prior-okkal
  - Fizika-informált neurális hálózatok (PINNs)
  - Szurrogát modellek drága szimulációkhoz

**MI NINCS BENNE:**
- Python alapok → Ch 5 (már definiálva)
- Adatpipeline-ok → Ch 7
- Digitális ikrek → Ch 10
- AI ágensek → Ch 11-12

**FORRÁSOK:** SL Section II (ELSŐDLEGES), OECD Ch 12+19, Deep Learning Earth Sciences (PINNs)

**DEBRECEN:** Példák debreceni kutatási területekről (hidrológia, anyagtudomány, mezőgazdaság)

---

### Fejezet 7: Adat-pipeline-ok és automatizálás
**Fájl:** `ch07_adat_pipeline.md`

**MI VAN BENNE:**
- Pipeline koncepció: bevitel → tisztítás → transzformáció → elemzés → kimenet
- Automatizálási lehetőségek azonosítása a munkafolyamatban
- Adatbevitel: fájlok, adatbázisok, API-k, szenzorok
- Tisztítás, validáció, minőségértékelés: hiányzó értékek, outlier-ek
- Kötegelt feldolgozás nagy mennyiségben
- Ütemezett feladatok és monitoring (cron, watchdog)
- Pipeline eszközök: egyszerű scriptek → Dagster → Nextflow
- Reprodukálhatóság: konténerizáció, környezetkezelés, dokumentáció

**MI NINCS BENNE:**
- Python alapok → Ch 5
- Vizuális automatizálás (n8n) → Ch 8
- RAG pipeline-ok → Ch 9
- Ágens-alapú pipeline-ok → Ch 12
- Docker részletek → Appendix A

**FORRÁSOK:** NASA CMR connector, KH Ch 5, OECD Ch 17-18, NAS Ch 5, SL Ch 7

**DEBRECEN:** Példa szenzor-adatok automatikus feldolgozására (meteorológia, vízügy, mezőgazdasági IoT)

---

### ═══════════════════════════════════════
### PART III: No-code-tól a szakterület-specifikus AI-ig
### ═══════════════════════════════════════

---

### Fejezet 8: Vizuális programozás és munkafolyamat-tervezés
**Fájl:** `ch08_vizualis_programozas.md`

**MI VAN BENNE:**
- Miért vonzó a vizuális programozás tudósoknak (folyamatábrák természetesek)
- Node-alapú szerkesztők koncepciója
- **n8n:** általános célú vizuális automatizálás
  - Telepítés és első workflow
  - Triggerek, akciók, csatlakozók
  - Példa: új cikkek figyelése → összefoglalás → email értesítés
  - AI integráció n8n workflow-kba
- **KNIME:** vizuális adattudomány
  - KNIME Analytics Platform bemutatása
  - KNIME AI Assistant (természetes nyelvű workflow-építés)
  - Példa: adatbetöltés → tisztítás → klaszterezés → vizualizáció
- **LangFlow:** vizuális LLM pipeline-tervezés
  - RAG chatbot építése drag-and-drop-pal
  - Prototípus → kód exportálás
- **Node-RED:** IoT és szenzor-adat workflow-ok (röviden)
- **Orange:** gépi tanulás nem-programozóknak (röviden)
- Mikor használj vizuálist vs. kód-alapút

**MI NINCS BENNE:**
- n8n AI agent építés részletesen → Ch 12
- RAG architektúra részletesen → Ch 9
- Python kódolás → Ch 5
- Adat-pipeline kódban → Ch 7

**FORRÁSOK:** KNIME (Acito), n8n (Natheem), NASA LangFlow section, Orange docs

**DEBRECEN:** Példa debreceni labormérés automatizálására n8n-nel

---

### Fejezet 9: RAG — Tanítsuk meg az AI-t a saját adatainkra
**Fájl:** `ch09_rag.md`

**MI VAN BENNE:**
- Miért nem elég az általános AI: nem ismeri az adataidat
- RAG architektúra: dokumentum-betöltés, chunking, embedding, vektor-tár, visszakeresés, generálás
  - **embedding/beágyazás ITT DEFINIÁLJUK**
  - **vektor-tár ITT DEFINIÁLJUK**
  - **fine-tuning/finomhangolás ITT DEFINIÁLJUK**
- Chatbot építése saját kutatási dokumentumokra
- Szemantikus keresés kontrollált szókészletek felett
- RAG minőség értékelése: BERTScore, ROUGE, 3 szintű keretrendszer
- Fine-tuning amikor a RAG nem elég (kis adathalmazok is működnek!)
  - Encoder fine-tuning (klasszifikáció)
  - Decoder fine-tuning (generálás)

**MI NINCS BENNE:**
- Prompt technikák → Ch 2
- Vizuális RAG építés LangFlow-val → Ch 8
- Ágens-rendszerek → Ch 11-12
- Etika → Ch 16

**FORRÁSOK:** NASA OSDR+EJ notebookok (ELSŐDLEGES), KH Ch 2, OECD Ch 6+20+23+28

**DEBRECEN:** Példa DE kutatási dokumentumok feletti RAG rendszerrel

---

### Fejezet 10: Digitális ikrek — Valós rendszerek virtuális másolatai
**Fájl:** `ch10_digitalis_ikrek.md`

**MI VAN BENNE:**
- Mi a digitális iker és miért kell a tudósoknak — ITT DEFINIÁLJUK
- Architektúra: adatforrások → modell → vizualizáció → visszacsatolás
- Platformok:
  - NVIDIA Omniverse (fizika-alapú, domináns)
  - Ansys TwinAI (mérnöki szimuláció)
  - interTwin (EU, nyílt forráskódú, tudományos: fizika, csillagászat, klíma)
  - Nyílt forráskódú alternatívák
- Egyszerű digitális iker építése AI segítségével
- Szakterületi példák:
  - Környezeti monitoring és klíma
  - Ipari folyamatok (BMW Debrecen kontextus)
  - Biológiai rendszerek
  - Infrastruktúra és energiaoptimalizálás
- **Debreceni kapcsolódás: Járműipari és AI Koordinációs Intézet, BMW gyár**

**MI NINCS BENNE:**
- Matematikai modellezés alapok → Ch 6
- Szenzor-adatok pipeline-ban → Ch 7
- AI ágensek → Ch 11
- Governance/szabályozás → Ch 14, 16

**FORRÁSOK:** Digital Twin Fundamentals (Vohra), Digital Twin Handbook (Thakker), NatAcad DT, interTwin paper, Fusion DT paper, KH Ch 11, OECD Ch 15+18, DL Earth Sci

**DEBRECEN:** BMW gyár, Járműipari és AI Intézet, Komondor, mezőgazdasági digitális iker lehetőségek

---

### ═══════════════════════════════════════
### PART IV: Ágentikus AI — Eszközökből munkatársak
### ═══════════════════════════════════════

---

### Fejezet 11: Az AI ágensek megértése
**Fájl:** `ch11_ai_agensek.md`

**MI VAN BENNE:**
- Eszközöktől az ágensekig: az autonómia spektruma
- **Ágens/agent ITT DEFINIÁLJUK** — Huang 10 jellemzője
- **7 rétegű ágens-architektúra ITT DEFINIÁLJUK**
- Mollick Kentaur vs. Kiborg módjai
- **ReACT minta ITT DEFINIÁLJUK:** Gondolat → Cselekvés → Megfigyelés → ismétlés
- **MCP (Model Context Protocol) ITT DEFINIÁLJUK:**
  - Univerzális szabvány AI és külső eszközök összekapcsolására
  - 10,000+ szerver, minden nagy platform támogatja
- **Multi-ágens rendszerek ITT DEFINIÁLJUK:**
  - Koordináció, kommunikáció, konfliktus-feloldás
- Biztonság, korlátok, ember-a-hurokban
- Az AI ágens gazdaságtana: költségek, hozzáférés, méltányosság

**MI NINCS BENNE:**
- Konkrét ágens-építés → Ch 12
- Eszközépítés (Streamlit, MCP szerver készítés) → Ch 13
- Költségek, beszerzés részletesen → Ch 14
- Etika részletesen → Ch 16

**FORRÁSOK:** KH Ch 1-4 (ELSŐDLEGES), EM Ch 6, NASA ReACT ágensek, KH Ch 12, Copilot Handbook Ch 7 (MCP)

**DEBRECEN:** Hogyan használhatnák a DE kutatói az ágenseket a mindennapokban

---

### Fejezet 12: AI ágensek építése kutatáshoz
**Fájl:** `ch12_agensek_epitese.md`

**MI VAN BENNE:**
- Ágens-keretrendszerek tudósoknak:
  - CrewAI: szerep-alapú ágens-csapatok (legkönnyebb belépési pont)
  - LangGraph: gráf-alapú munkafolyamatok (legrugalmasabb)
  - AutoGen: társalgási multi-ágens rendszerek
  - Claude Agent SDK: profi eszköztár
  - Összehasonlító táblázat (EZ AZ EGYETLEN HELY)
- Első kutatási ágensek építése:
  - Irodalomkutató ágens-csapat: kereső → olvasó → szintetizáló
  - Adatfeldolgozó ágens-pipeline
  - Kísérlet-figyelő és riasztó ágens
- Ágensek csatlakoztatása adatokhoz és eszközökhöz MCP-vel
- Végponttól végpontig ágentikus kutatási munkafolyamatok
- Monitoring és hibakeresés

**MI NINCS BENNE:**
- Ágens-elmélet → Ch 11 (már definiálva)
- MCP fogalom → Ch 11 (már definiálva)
- Streamlit/Gradio interfészek → Ch 13
- n8n vizuális ágens-építés → Ch 8

**FORRÁSOK:** KH Ch 2-3 (ELSŐDLEGES), NASA agent.py+chains.py, OECD Ch 5+22, n8n Ch 4 (AI agents)

**DEBRECEN:** Példa: debreceni irodalomkutató ágens-csapat építése

---

### Fejezet 13: Saját programok és eszközök készítése
**Fájl:** `ch13_eszkozok_keszitese.md`

**MI VAN BENNE:**
- Mikor kell saját szoftver a kutatásodhoz
- Webes felületek percek alatt:
  - Streamlit: adat-feltöltős elemző alkalmazás
  - Gradio: ML modell interaktív felülete
  - Példa: 3 konkrét tudományos alkalmazás
- MCP szerverek készítése: adataid és eszközeid AI-elérhetővé tétele
- Megosztás GitHub-on dokumentációval

**MI NINCS BENNE:**
- Python alapok → Ch 5
- AI kódolási asszisztensek → Ch 5
- Ágens-építés → Ch 12
- Docker/pip csomagolás → Appendix A
- API tervezés (túl fejlesztő-orientált)
- Nyílt forráskódú best practice-ek (túl fejlesztő-orientált)

**FORRÁSOK:** KH Ch 5, NASA kód-modulok, Copilot Handbook Ch 7 (MCP)

**DEBRECEN:** Példa: debreceni kutatócsoport számára készített egyszerű webes eszköz

---

### ═══════════════════════════════════════
### PART V: Felelős AI-adoptáció vezetése
### ═══════════════════════════════════════

---

### Fejezet 14: Az AI-val felszerelt kutatólabor
**Fájl:** `ch14_ai_labor.md`

**MI VAN BENNE:**
- A 2026-os tudományos AI stack: mi hova való
- Költségkezelés: ingyenes szintek → előfizetések → API költségvetés → HPC
- Számítási erőforrások: laptop → felhő → Komondor szuperszámítógép
- **Adatbiztonság és adatvédelem:**
  - Mit küldj felhő AI-nak vs. mit tarts lokálisan
  - **GDPR ITT DEFINIÁLJUK** a kutatási adatok kontextusában
  - **EU AI Act ITT DEFINIÁLJUK**
- **AI beszerzési útmutató:**
  - Platform-kiválasztási szempontok kutatási intézményeknek
  - EU MCC-AI (Model Contractual Clauses)
  - EDUCAUSE beszerzési ellenőrzőlista európai adaptációja
  - Teljes birtoklási költség (TCO) elemzés
- Csapat-együttműködés: workflow-ok megosztása, kollégák képzése
- AI hatás mérése: megtakarított idő, javult minőség, új képességek
- **[Etika doboz: "Lásd Ch 16"]**

**MI NINCS BENNE:**
- Konkrét eszközök összehasonlítása → Ch 5 (kód), Ch 8 (vizuális)
- Ágens-építés → Ch 12
- Egyetemi stratégia → Ch 15
- Etika és szabályozás részletesen → Ch 16

**FORRÁSOK:** EUA Ch 2+4, KH Ch 4-5, OECD Ch 17+27+29, NAS Ch 4, WEF Procurement, Oxford Handbook Part 3+5

**DEBRECEN:** Komondor hozzáférési útmutató, DE informatikai infrastruktúra, helyi iparági partnerek

---

### Fejezet 15: AI az egyetemen — Oktatás, tanulás és intézményi átalakulás
**Fájl:** `ch15_ai_az_egyetemen.md`

**MI VAN BENNE:**
- **15.1 Egyetemi esettanulmányok (átvehető modellekként):**
  - University of Florida: AI az egész tananyagban
  - University of Helsinki: Elements of AI (2M beiratkozás)
  - Northeastern: Claude kampusz-szintű bevezetés
  - Johns Hopkins: Ágentikus AI tanúsítvány
- **15.2 AI az oktatásban és témavezetésben:**
  - Kurzus-előkészítés AI-val: tematika, olvasmányok, előadásanyag
  - Értékelés-tervezés: a "házifeladat-apokalipszis" elkerülése
  - **SARPS keretrendszer ITT DEFINIÁLJUK** (Six Assessment Redesign Pivotal Strategies)
  - AI-támogatott szakdolgozat és disszertáció témavezetés
  - Hallgatói AI-politikák: mit engedélyezzünk, mit követeljünk meg, mit tiltsunk
  - AI mint szókratészi tutor: Bloom 2-szigma problémája nagy léptékben
  - Gyakorlati példák: Khanmigo, Claude for Education
- **15.3 Változásmenedzsment az AI-adoptációhoz:**
  - Oktatói ellenállás: megértés és kezelés
  - Egyenetlen digitális készségek a szakterületek között
  - Rogers innovációdiffúzió alkalmazva egyetemekre (lengyel tanulmány adatai)
  - Ösztönző struktúrák: hogyan jutalmazzuk az AI-integrációt
  - Képzési modellek: workshopok, gyakorlatközösségek, peer mentoring
  - Az EUA részvételi megközelítése: teljes közösség bevonása
- **15.4 Útiterv a Debreceni Egyetem számára:**
  - Mit birtokol a DE: erősségek és meglévő eszközök
  - Mire van szüksége a DE-nek: hiányok és prioritások
  - Háromfázisú AI-átállási terv
  - Hogyan illeszkedik ez a könyv a tantervbe

**MI NINCS BENNE:**
- Konkrét AI eszközök → Ch 2, 5, 8
- Etika és szabályozás → Ch 16
- Labor-szintű AI stack → Ch 14
- Posztplágium → Ch 16

**FORRÁSOK:** SK egész könyv (ELSŐDLEGES), EUA Ch 1-3+5 (ELSŐDLEGES), EM Ch 7-8, OECD Ch 24-25+31, Teaching with AI (Bowen), GenAI Higher Ed (Chan&Colloton SARPS), Debrecen research, university research reports (mind az 5)

**DEBRECEN:** KÖZPONTI FEJEZET — teljes debreceni útiterv, helyi partnerek, Magyar Akkreditációs Bizottság, PULI GPT

---

### Fejezet 16: Etika, reprodukálhatóság és az AI jövője a tudományban
**Fájl:** `ch16_etika_jovo.md`

**MI VAN BENNE:**
- **16.1 Kutatási integritás az AI korában:**
  - Fabrikált hivatkozások és hallucinált referenciák
  - AI-generált képmanipuláció és felismerés
  - Szintetikus adatok visszaélése: mikor tűnik valósnak a generált adat
  - Detektáló eszközök: AI-generált szöveg- és képdetektorok
  - **Posztplágium koncepció ITT DEFINIÁLJUK** (Eaton): hibrid ember-AI írás mint új norma
  - Statisztika: ~13.5% PubMed cikk 2024-ben LLM-jeleket mutatott
  - Biobiztonsági megfontolások: AI-támogatott biológiai tervezés kockázatai
- **16.2 AI etika a tudományos kutatásban (konszolidálva Ch 3, 14-ből):**
  - Szerzőség: ki írta ezt a cikket?
  - Torzítás az AI-generált elemzésekben
  - EU AI Act: osztályozás, kötelezettségek, megfelelés kutatóknak
  - Folyóirat-politikák AI-használatról (2026 állapot)
  - COPE irányelvek
- **16.3 Reprodukálhatóság az AI korában:**
  - A reprodukálhatósági kihívás: nem-determinisztikus kimenetek
  - AI-támogatott munkafolyamatok dokumentálása: mit rögzítsünk
  - Verzió-rögzítés, prompt-naplózás, seed-fixálás
  - Az "AI módszerek" szekció írása a cikkeidben
  - Promptok, konfigok, ágens-definíciók megosztása
- **16.4 Elvek a felelős AI-hoz a tudományban:**
  - NASA 5 elve: Átláthatóság, Bizalom, Csapatmunka, Képzés, Technikák
  - Mollick 4 szabálya újralátogatva mint etikai korlátok
  - EUA értékalapú megközelítés
  - Személyes AI etikai keretrendszer építése
- **16.5 Merre tart mindez:**
  - Négy forgatókönyv: Stagnálás, Lassú növekedés, Exponenciális növekedés, AGI
  - Teljesen autonóm tudományos felfedezés: ígéret és veszély
  - A tudós változó szerepe: cselekvéstől az irányításig az együttműködésig
  - Első lépéseid a könyv befejezése után

**MI NINCS BENNE:**
- Konkrét promptolási technikák → Ch 2
- Konkrét eszközök → Ch 5, 8
- Egyetemi stratégia → Ch 15
- Beszerzés → Ch 14

**FORRÁSOK:** EM Ch 2+9, HQ Ch 13-14, KH Ch 6-7+12, EUA Ch 1+4-5, NAS Ch 3-4, OECD Ch 26+30-31, AI Snake Oil, Oxford Handbook Parts 2+3+9

**DEBRECEN:** Magyar szabályozási kontextus, DE etikai bizottság, HUN-REN irányelvek

---

### ═══════════════════════════════════════
### FÜGGELÉKEK
### ═══════════════════════════════════════

### Appendix A: AI kutatási környezet beállítása
**Fájl:** `appendix_a_kornyezet.md`
- Python, git, VS Code, Claude Code, Cursor telepítés lépésről lépésre
- API kulcsok és fiókok (Claude, OpenAI, Gemini)
- Komondor hozzáférés (DE felhasználóknak)
- Docker és pip csomagolás (Ch 13-ból ide mozgatva)
- Ajánlott hardver és felhőopciók

### Appendix B: Prompt-könyvtár tudósoknak (50+)
**Fájl:** `appendix_b_prompt_konyvtar.md`
- Irodalomáttekintés és szintézis (10)
- Írás és szerkesztés (10)
- Adatelemzés és vizualizáció (10)
- Kísérleti tervezés (5)
- Kódgenerálás és hibakeresés (10)
- Ágens-utasítások és rendszerpromptok (5)

### Appendix C: Források és további olvasmányok
**Fájl:** `appendix_c_forrasok.md`
- Annotált könyvlista (mit olvass melyikből)
- Kulcscikkek
- Online kurzusok és tanúsítványok
- Közösségek és fórumok
- Magyar nyelvű AI-források (PULI GPT, HuSpaCy, AI Koalíció, HUN-REN)
- Szakterület-specifikus könyvajánlók

### Előszó
**Fájl:** `ch00_eloszo.md`
- Kinek szól ez a könyv
- Mit jelent a "nem-programozó"
- Hogyan használd a társwebhelyet és a kódtárat
- Köszönetnyilvánítás

### Szójegyzék / Glosszárium
**Fájl:** `glossary.md`
- Minden angol szakkifejezés magyar magyarázattal
- ABC sorrendben
