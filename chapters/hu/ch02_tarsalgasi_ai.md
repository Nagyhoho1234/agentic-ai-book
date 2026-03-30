# 2. fejezet: Társalgási AI — Az első kutatási partnered

> **Fejezet-informacio**
> - **Kinek szol:** Kutatoknak, oktatoknak es hallgatoknak, akik elkezdenenek AI chatbotokat hasznalni a munkahoz
> - **Eloismeretek:** 1. fejezet (ajanlott, de nem kotelezo)
> - **Amit megtanulsz:**
>   - Hogyan mukodik egy nagy nyelvi modell (tokenek, kontextusablak, hallucianció)
>   - A negy nagy platform (Claude, ChatGPT, Gemini, Copilot) osszehasonlitasa
>   - Hatekony promptolasi technikak es mintak tudomanyos munkara
> - **Szukseges eszkozok:** Browser only
> - **Kapcsolodo fejezetek:** 1. fejezet (AI alapok), 3. fejezet (tudomanyos iras), 16. fejezet (etika)

> *„A helyes kérdés feltevése gyakran fontosabb, mint a válasz megtalálása."*
> — Albert Einstein (gyakran idézett parafrázis)

---

## 2.1 Amikor a saját szakterületed nem elég

<!-- [SZERKESZTOI MEGJEGYZES / GPT-5.4 review] "Kepzeld el a kovetkezo helyzetet" — ez az 1. fejezet utan a masodik ilyen nyitas. A minta (kepzeld el + jelenet + AI mint megoldas) ismetlodik a konyv szinte minden fejezetenek elejen; a monotonia elkerulese erdekeben fontold meg alternativ bevezeto formulak hasznalatat nehany fejezetben. -->
Képzeld el a következő helyzetet. Tiszai ökológus vagy, évek óta a folyó makrogerinctelen-faunáját kutatod. Egy hétfő reggel a projektvezető bejelenti: a következő pályázatban izotóphidrológiai adatokkal is alá kell támasztani az eredményeket. A deutérium- és oxigén-18-arányok, a keverési modellek, a Rayleigh-frakcionáció — mindez teljesen idegen terep. Három heted van, mire a pályázati tervezetet le kell adni.

Mit csinálsz?

Öt évvel ezelőtt a válasz egyértelmű lett volna: keress egy izotópgeokémikust, kérj konzultációt, olvasd végig Craig (1961) klasszikus cikkét, majd próbáld két hét alatt megérteni, amit ő évtizedekig tanult. Ma van egy másik lehetőséged is — nem helyettesítője, hanem *kiegészítője* a hagyományos útnak: megkérhetsz egy nagy nyelvi modellt (LLM-et), hogy legyen az ideiglenes tutored.

Nem azért, mert az AI mindent tud. Hanem azért, mert egy jól irányított társalgás órákon belül áttekintést adhat a mező terminológiájáról, a kulcskoncepcióiról, a kritikus cikkekről — és ami a legfontosabb, segít *jobb kérdéseket megfogalmazni*, mielőtt az igazi szakértővel leülsz beszélgetni.

Ez a fejezet erről szól: hogyan használd a társalgási AI-t úgy, mint egy intellektuálisan stimuláló, de megbízhatatlan gyakornokot — aki gyors, kreatív, minden nyelven beszél, de rendszeresen kitalál dolgokat, amiket soha nem ellenőrzött.

---

## 2.2 Hogyan „gondolkodik" egy nagy nyelvi modell?

Mielőtt bármit kérnél egy AI-tól, érdemes megérteni, mi történik a motorháztető alatt. Nem azért, hogy programozóvá válj, hanem azért, mert a működés megértése segít felismerni, *mikor bízhatsz benne és mikor nem*.

### 2.2.1 Token — a nyelv legkisebb építőköve

> **Definíció: Token** — Az a legkisebb egység, amelyre a nyelvi modell a szöveget felbontja. Egy token lehet egy teljes szó, egy szótöredék, egy írásjel vagy akár egy szóköz. A magyar „hidrogeológiai" szó például több tokenre bomlik (pl. „hidro", „geo", „lógiai"), míg az angol „the" egyetlen token. A modellek a tokenekhez számokat rendelnek, és ezekkel a számokkal dolgoznak — amikor válaszolnak, a számokból állítják vissza az emberi szöveget.

Miért fontos ez neked? Mert a modellek *tokenben* számolnak, nem szavakban. Amikor egy platformon azt olvasod, hogy „200K kontextusablak", az 200 000 tokent jelent — ami nagyjából 150 000 angol szó, de magyarul kevesebb, mert a magyar nyelv agglutináló szerkezete miatt egy-egy szó több tokent igényel.

### 2.2.2 A következő token megjóslása — és semmi több

Az LLM-ek működési elve meglepően egyszerű: **a rendszer megpróbálja megjósolni, melyik token következik a sorozatban**. Csak ennyi. Nincs mögötte „értés", „meggyőződés" vagy „szándék" — van egy hatalmas valószínűségi tér, amelyet a tanítás során több billió token feldolgozásával épített fel.

Amikor beírod: „A víz forráspontja tengerszinten..." — a modell nem „tudja", hogy 100 °C a válasz. Ehelyett a tanítóadatai alapján kiszámítja, hogy a következő token valószínűleg „100", utána „°", utána „C". A modell eredménye statisztikailag helyes *mintázat*, nem tényismeret.

Ez a különbségtétel kritikus. Ahogy Narayanan és Kapoor fogalmaz: az LLM-ek nem hazudnak — mert a hazugsághoz tudni kellene az igazságot. Ehelyett egyszerűen közömbösek az igazság iránt. Harry Frankfurt filozófus terminológiájával élve: *bullshit generátorok* — nem az a céljuk, hogy igazat mondjanak, hanem az, hogy meggyőzően hangozzanak.

### 2.2.3 Kontextusablak — az AI „munkamemóriája"

> **Definíció: Kontextusablak (context window)** — Az a maximális tokenszám, amelyet a modell egyetlen interakció során „lát" — beleértve a te kérdésedet, a korábbi üzeneteket és a modell saját válaszait. Ami kívül esik a kontextusablakon, azt a modell szó szerint nem látja, nem emlékszik rá.

A kontextusablak a gyakorlatban azt jelenti, hogy:

- Egy rövid ablakú modell (pl. 8K token) csak néhány oldalnyi szöveget tud egyszerre feldolgozni.
- Egy nagy ablakú modell (pl. 200K vagy 1M token) akár egy teljes könyvet is „elolvashat" — de a figyelem a szöveg közepén gyengébb lehet, mint az elején vagy a végén.
- Amikor egy hosszú beszélgetés közben azt érzed, hogy a modell „elfelejti" a korábbi utasításaidat, az a kontextusablak telítődése.

Gyakorlati tipp: ha fontos utasítást adsz a modellnek, ismételd meg a beszélgetés során, különösen hosszú interakcióknál.

### 2.2.4 Hallucináció — amikor az AI magabiztosan téved

> **Definíció: Hallucináció** — Amikor a nyelvi modell olyan információt generál, amely tényszerűen hamis, de a szöveg stílusa, nyelvtana és magabiztossága semmiben nem különbözik a helyes válaszokétól. A modell „nem tudja", hogy téved — egyszerűen az a tokensorozat volt a legvalószínűbb.

A hallucinációk nem ritka hibák — a modell működési elvének közvetlen következményei. Klasszikus példák:

- **Nemlétező irodalmi hivatkozások.** Egy ügyvéd 2023-ban bírósági beadványba emelt hat ChatGPT által generált jogesetet — egyik sem létezett. A szerzők, a folyóiratcímek, sőt az oldalszámok is kitaláltak voltak, de tökéletesen hiteles formában.
- **Halálos gombászkönyvek.** Az Amazon-on megjelent AI-generált gombászati útmutatók potenciálisan mérgező fajokat jelöltek meg ehető gyanánt.
- **Hamis tudományos állítások.** Egy modell képes meggyőzően „levezetni", miért oldódik az arany sósavban (valójában nem oldódik — királyvízben igen).

A hallucináció legveszélyesebb formája az, amelyik *majdnem* igaz. Ha a modell teljesen értelmetlen dolgot mond, észreveszed. De ha a válasz 95%-ban korrekt, és a maradék 5% finoman hibás — az a tudományos munkában katasztrofális lehet.

> **Ne csinalld!**
> Soha ne illeszd be kozvetlenul egy AI-valaszt tudomanyos kéziratba vagy palyazatba az irodalmi hivatkozasok egyenkenti ellenorzese nelkul. Az LLM-ek rendszeresen generälnak nem letezo cikkeket, hamis DOI-kat es kitalalt szerzokat. Egyetlen leleplezo hamis hivatkozas a kéziratodban a biralok szemeben az egesz munka hitelességet alarassa.

---

## 2.3 A platformok tája 2026-ban

2026 márciusában négy nagy, általánosan elérhető AI-platform versenyez a kutatók figyelméért. Mindegyiknek vannak erősségei és korlátai. Az alábbi táblázat a legfontosabb jellemzőket foglalja össze:

| Jellemző | **Claude** (Anthropic) | **ChatGPT** (OpenAI) | **Gemini** (Google) | **Copilot** (Microsoft) |
|---|---|---|---|---|
| **Aktuális csúcsmodell** | Claude Opus 4 | GPT-4.5 / o3 | Gemini 2.5 Pro | GPT-4.5 (Copilot felületen) |
| **Kontextusablak** | 200K (standard), 1M (extended) | 128K | 1M+ | 128K |
| **Ingyenes szint** | Korlátozott (Claude.ai) | GPT-4o mini, korlátozott | Ingyenes szint elérhető | Microsoft 365-be integrált |
| **Fizetős ár (havi)** | ~20 USD (Pro) | ~20 USD (Plus), ~200 USD (Pro) | ~20 USD (Advanced) | Microsoft 365 Copilot: ~30 USD |
| **Legnagyobb erősség** | Hosszú dokumentumok elemzése, árnyalt gondolkodás, biztonságos válaszok | Széles ökoszisztéma, képgenerálás (DALL-E), bővítmények | Óriási kontextus, Google-keresés integráció, multimodális | Office-integráció, Bing-keresés, vállalati környezet |
| **Tudományos alkalmazásban kiemelkedő** | Irodalomfeldolgozás, kritikus elemzés, kódolás | Általános kutatási asszisztens, kreatív feladatok | Hosszú cikkek/adatkészletek feldolgozása | Gyors tényellenőrzés weben, irodai dokumentumok |
| **Fő korlát** | Nem keres a weben alapértelmezésben | Hallucináció-arány magasabb lehet kreatív módban | Nem mindig elérhető minden régióban | Önálló kutatásra kevésbé alkalmas |
| **API hozzáférés** | Igen | Igen | Igen | Korlátozott |
| **Képfeldolgozás** | Igen | Igen | Igen | Igen |
| **Keresés integrálva** | Korlátozott | Igen (Browse) | Igen (Google Search) | Igen (Bing) |

**Melyiket válaszd?**

Nincs „legjobb" platform — van, amelyik a *te* feladatodra a legalkalmasabb:

- **Hosszú dokumentumot kell feldolgozni** (pályázati kiírás, 80 oldalas review cikk)? → Claude vagy Gemini (nagy kontextusablak).
- **Gyors tényellenőrzés kell friss forrásokból**? → ChatGPT Browse vagy Copilot (web-keresés integráció).
- **Google Workspace-ben dolgozol** (Docs, Sheets)? → Gemini.
- **Microsoft 365-öt használsz** (Word, Excel, Teams)? → Copilot.
- **Kód kell** (Python, R)? → Claude vagy ChatGPT (mindkettő erős, de a 9. és 11. fejezetben mélyebben foglalkozunk ezzel).

A legfontosabb tanács: **ne ragadj le egyetlen platformnál**. Használj legalább kettőt párhuzamosan, és hasonlítsd össze a válaszokat — ez az egyik leghatékonyabb módja a hallucináció-szűrésnek.

---

## 2.4 Prompt engineering — a jó kérdés művészete

> **Definíció: Prompt** — Az az utasítás, kérdés vagy szöveg, amelyet a felhasználó a nyelvi modellnek ad. A prompt lehet egyetlen mondat („Mi a fotoszintézis?"), de lehet több bekezdésnyi, strukturált instrukció is, amely kontextust, szerepet, formátumot és korlátokat tartalmaz.

> **Definíció: Prompt engineering** — A promptok tudatos tervezésének és finomításának gyakorlata annak érdekében, hogy a modell a lehető leghasznosabb, legpontosabb és leginkább releváns választ adja. Nem programozás — inkább a kérdezés művészete.

Az LLM-ek használatának legfontosabb készsége nem az, hogy ismerd a modell architektúráját, hanem az, hogy **jó kérdéseket tudj feltenni**. Egy jól megírt prompt drámaian javítja a válasz minőségét — egy rosszul megírt prompt pedig félrevezető, felszínes vagy irreleváns eredményeket ad.

A NASA Science Mission Directorate egy nyílt hozzáférésű útmutatót készített az LLM-ek tudományos célú használatáról, amelyben kilenc prompt-mintázatot (prompt pattern) mutat be. Ezeket a mintázatokat eredetileg White és társai (2023) publikálták az *„A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT"* című cikkben. Az alábbiakban mind a kilenc mintázatot bemutatom, a NASA-példákat általános tudományos példákkal kiegészítve.

---

### 2.4.1 Recipe Pattern — Kísérleti protokollok generálása

**Mire jó?** Amikor ismered a végcélt és néhány lépést, de nem a teljes folyamatot. Olyan, mintha egy szakácskönyvből kikeresnél egy receptet — tudod, milyen ételt akarsz, van néhány hozzávalód, de a pontos lépéseket a modellre bízod.

**Sablon:**

```
Szeretném elvégezni a következőt: [feladat leírása].
Tudom, hogy szükségem lesz a következő lépésekre: [A, B, C lépés].
Kérlek, adj egy teljes, lépésenkénti útmutatót.
Töltsd ki a hiányzó lépéseket.
```

**Példa — Talajtani kutatás:**

```
Szeretném meghatározni egy mezőgazdasági talaj szervesanyag-tartalmát
izzítási veszteség (loss on ignition) módszerrel.
Tudom, hogy szükségem lesz a következőkre:
- mintavétel a szántóföldről
- szárítás
- izzítás kemencében
- tömegmérés

Kérlek, adj teljes protokollt a mintavételtől az eredmény kiszámításáig.
Töltsd ki a hiányzó lépéseket, beleértve a pontos hőmérsékleteket,
időtartamokat és a szükséges felszerelést.
```

**Példa — Ökológia:**

```
Szeretném felmérni egy folyószakasz makrogerinctelen diverzitását
a Magyar Nemzeti Biodiverzitás-monitorozó Rendszer módszertana szerint.
Tudom, hogy szükségem lesz:
- mintavételi pontok kijelölése
- surber-mintavevő használata
- konzerválás alkoholban
- határozás családszintig

Kérlek, adj egy teljes terepi és laboratóriumi protokollt.
Töltsd ki a hiányzó lépéseket.
```

**Mire figyelj:** A Recipe pattern erősségei és korlátai egyszerre a specifikusság. Ha túl kevés kiindulási lépést adsz, a modell általános lesz. Ha a szakterületed nagyon speciális (pl. egy konkrét műszer kalibrálása), a válasz lehet felszínes — mert a tanítóadatokban kevés releváns szöveg volt. Mindig ellenőrizd a javasolt paramétereket (hőmérséklet, koncentráció, idő) szakirodalommal.

---

### 2.4.2 Output Automator — Szkriptek generálása leírásból

**Mire jó?** Amikor a modell válaszából azonnal futtatható kódot, szkriptet vagy automatizálható munkafolyamatot szeretnél kapni — ahelyett, hogy te írnád át manuálisan.

**Sablon:**

```
Készíts egy szkriptet, amely [feladat leírása],
a következő paraméterekkel: [paraméterek].
Az eredményt [formátum] formátumban add ki.
```

**Példa — Környezettudományi adatgyűjtés:**

```
Készíts egy Python-szkriptet, amely a Copernicus Climate Data Store API-n
keresztül letölti a Kárpát-medence napi átlaghőmérséklet-adatait
2020 január 1-től 2024 december 31-ig, 0.25 fokos rácsfelbontással.
Az eredményt CSV formátumban mentse el, az oszlopok legyenek:
dátum, szélesség, hosszúság, hőmérséklet_celsius.
```

**Példa — Bioinformatika:**

```
Készíts egy R-szkriptet, amely beolvas egy FASTA formátumú fájlt,
kiszámítja az egyes szekvenciák GC-tartalmát,
és az eredményt egy összesítő táblázatban adja ki CSV formátumban,
az oszlopok: szekvencia_azonosító, hossz, gc_tartalom_százalék.
```

**Mire figyelj:** A generált kódot *mindig* teszteld, mielőtt éles adaton futtatod. Az AI által írt szkriptek gyakran szintaktikailag helyesek, de tartalmazhatnak logikai hibákat, elavult API-hívásokat vagy rossz paraméterneveket. A kódgenerálás részleteivel az 5. fejezet foglalkozik.

---

### 2.4.3 Persona Pattern — Szakértői perspektíva kérése

**Mire jó?** Amikor azt szeretnéd, hogy a modell egy adott szakterület szakértőjének nézőpontjából válaszoljon. Ez a mintázat azért működik, mert az LLM-ek tanítóadatai tartalmaznak különböző szakértők által írt szövegeket — és amikor „szerepet" adsz a modellnek, az a válaszgenerálás valószínűség-eloszlását az adott szerep szövegeinek mintázatai felé tolja.

Ahogy Mollick fogalmaz: ez nem filozófiai állítás arról, hogy az AI „megjátssza" a szakértőt — ez egy praktikus technika, amely javítja a válaszok minőségét.

**Sablon:**

```
Válaszolj a [téma] kérdéseimre úgy, mintha [specifikus szakértő] lennél.
```

**Példa — Interdiszciplináris kutatás:**

```
Válaszolj a kérdéseimre a talajvíz-arzén problémáról úgy,
mintha egy hidrogeokémikus lennél, aki 20 éve kutatja az Alföld
arzénszennyezését. Használj szaktechnikai nyelvet, de ahol bonyolult
koncepciót vezetsz be, adj egy rövid magyarázatot is.
```

**Példa — Módszertani konzultáció:**

```
Válaszolj a statisztikai kérdéseimre úgy, mintha egy biostatisztikus
lennél, aki ökológiai adatelemzésre specializálódott.
A vizsgálatom: kis mintaszámú (n=12) terepi kísérlet, ahol
a kezelések hatását szeretném kimutatni fajgazdagságra.
Milyen tesztet javasol, és miért?
```

**Példa — Peer review szimuláció:**

```
Válaszolj úgy, mintha egy szigorú, de konstruktív bíráló lennél
egy Q1-es ökológiai folyóiratnál. Fogom beilleszteni az absztraktomat,
és szeretném, ha rámutatnál a gyenge pontjaira.
```

**Mire figyelj:** A persona pattern nem teszi a modellt valódi szakértővé. A „szakértő hangon" adott téves válasz veszélyesebb, mint a nyilvánvalóan bizonytalan válasz, mert nehezebb felismerni a hibát. A persona patternt mindig kombinálni érdemes a Fact Check List patternnel (lásd 2.4.8).

> **🌾 Szakterületi példa: LLM-alapú mezőgazdasági szaktanácsadás**
>
> A precíziós mezőgazdaságban az LLM-alapú csevegőrobotok áthidalhatják a szaktanácsadói hiányt: a fejlődő országokban egyetlen tanácsadóra több ezer háztartás jut. A gazdálkodó anyanyelvén kérdezhet — akár szöveges üzenetben, okostelefon nélkül — és valós idejű, helyi viszonyokra szabott növényvédelmi és trágyázási javaslatokat kaphat. Egy vidéki indiai gazdálkodó például szöveges üzenetben írhatja le a paradicsomnövényein észlelt tüneteket, és azonnal diagnózist és kezelési javaslatot kap. A persona pattern itt különösen hasznos: a chatbot „tapasztalt agronómus" szerepben célzottabb válaszokat ad, mint általános kérdezési módban.
>
> *Forrás: precagri 15.7 „Természetes nyelvi feldolgozás és nagy nyelvi modellek a mezőgazdaságban"*

---

### 2.4.4 Flipped Interaction — Szókratészi tanulás

**Mire jó?** Amikor nem te kérdezed az AI-t, hanem az AI kérdez téged — és a kérdésein keresztül mélyíti a megértésedet. Ez a szókratészi módszer AI-verziója: a modell nem ad kész választ, hanem rávezet.

**Sablon:**

```
Ahelyett, hogy közvetlenül elmagyaráznád, tegyél fel nekem kérdéseket
egyenként a [téma] témában, hogy segíts jobban megérteni a koncepciót.
Adj visszajelzést a válaszaimra.
```

**Példa — Új szakterület tanulása:**

```
Ahelyett, hogy elmagyaráznád, tegyél fel nekem kérdéseket egyenként
a Bayes-statisztikáról, hogy megértsem az alapelveit.
A háttértudásom: frequentista statisztikát tanultam az egyetemen,
de a Bayes-módszerekkel nem találkoztam.
Adj visszajelzést minden válaszomra, mielőtt a következő kérdésre lépnél.
```

**Példa — Hipotézis tesztelése:**

```
Szeretném tesztelni a hipotézisem, hogy az invazív bálványfa
(Ailanthus altissima) terjedése a Tisza mentén összefügg
az árvízgyakoriság változásával.

Ahelyett, hogy véleményeznéd, tegyél fel nekem szókratészi kérdéseket
egyenként, amelyek segítenek felismerni a hipotézis erősségeit
és gyengeségeit. A végén foglald össze, milyen pontokra kellene
jobban odafigyelnem.
```

**Mire figyelj:** Ez a mintázat rendkívül hatékony tanulásra és önellenőrzésre. A NASA-tapasztalatok szerint néha a modell nem ad visszajelzést a válaszaidra, hanem csak sorolja a kérdéseket. Ha ez történik, pontosítsd a promptot: „Adj visszajelzést minden válaszomra, és csak ezután lépj a következő kérdésre." Az is segít, ha hozzáteszed: „Ha a válaszom téves, javíts ki és magyarázd el, miért."

---

### 2.4.5 Question Refinement — Kutatási kérdés élesítése

**Mire jó?** Amikor van egy homályos kutatási kérdésed, és segítségre van szükséged, hogy azt pontosabbá, specifikusabbá, vizsgálhatóbbá tedd. A modell a kérdésedet átfogalmazza, és te eldöntöd, melyik verzió ragadja meg legjobban a szándékodat.

**Sablon:**

```
Finomítsd a következő kérdésemet, hogy specifikusabb és egyértelműbb legyen,
fókuszálva a [kívánt aspektus] szempontra: "[eredeti kérdés]"
```

**Példa — Ökológiai kutatás:**

```
Finomítsd a következő kérdésemet, hogy specifikusabb és egyértelműbb
legyen, fókuszálva a mérhető változókra és az ok-okozati mechanizmusra:

"Hogyan hat a klímaváltozás a biodiverzitásra Magyarországon?"
```

**Várható eredmény (a modell valami ilyesmit fog javasolni):**

A modell visszaadhat például ilyen finomított változatokat:

- *„Milyen mértékben változott a tavaszi vonuló madárfajok megérkezési dátuma a Hortobágyon az elmúlt 30 évben, és ez korrelál-e a márciusi átlaghőmérséklet emelkedésével?"*
- *„Hogyan változott az őshonos kétéltű fajok populációmérete a Tisza menti holtágakban a 2003-2023 közötti időszakban, és kimutatható-e összefüggés az éves csapadékmennyiség változásával?"*

**Mire figyelj:** A modell hajlamos a kérdést szűkíteni — ez általában jó, de ellenőrizd, hogy a finomított kérdés valóban azt ragadja-e meg, amit vizsgálni akarsz. Használd kiindulópontnak, ne végeredményként.

---

### 2.4.6 Alternative Approach — Módszertani alternatívák feltérképezése

**Mire jó?** Amikor van egy módszered, de szeretnéd tudni, milyen más megközelítések léteznek. Ez különösen hasznos, ha egy régen kialakult módszertant használsz, és nem vagy biztos benne, hogy nincs-e jobb, újabb alternatíva.

**Sablon:**

```
Mutass be különböző megközelítéseket a [feladat] megoldására,
figyelembe véve különböző adattípusokat, módszereket, eszközöket
vagy algoritmusokat.
```

**Példa — Távérzékelés:**

```
Mutass be különböző megközelítéseket a felszínborítás-változás
detektálására a Hortobágyon 2015 és 2025 között,
figyelembe véve különböző műholdas adatforrásokat (Sentinel-2,
Landsat 9, PlanetScope), módszereket (pixelalapú, objektumalapú,
deep learning) és szoftvereket (QGIS, Google Earth Engine, Python).
Mindegyik megközelítésnél jelezd az előnyöket és hátrányokat.
```

**Példa — Analitikai kémia:**

```
Mutass be különböző megközelítéseket a nehézfém-szennyezés
meghatározására talajtani mintákban, figyelembe véve az AAS,
ICP-OES, ICP-MS és XRF módszereket. Az összehasonlításban
szerepeljen a kimutatási határ, a költség, a mintaelőkészítés
bonyolultsága és a többelemes képesség.
```

**Mire figyelj:** Ez a mintázat rendkívül hasznos a módszertani vakfoltok felismerésére. Előfordulhat, hogy a modell olyan módszert is javasol, amelyről nem hallottál — ilyenkor *feltétlenül* ellenőrizd a szakirodalomban, hogy a módszer létezik-e és alkalmazható-e a te kontextusodban.

---

### 2.4.7 Cognitive Verifier — Komplex problémák felbontása

**Mire jó?** Az LLM-ek gyakran jobb eredményt adnak, ha egy nagy kérdést több kisebb részkérdésre bontunk. Ez a mintázat arra kéri a modellt, hogy *maga* végezze el a dekompozíciót — és a részkérdések megválaszolásán keresztül jusson el az átfogó válaszhoz.

**Sablon:**

```
A következő kérdéshez: "[eredeti kérdés]"
— javasolj részkérdéseket, amelyek segítenek feltárni a téma
különböző aspektusait, és amelyek megválaszolása egy átfogóbb,
megalapozottabb végső válaszhoz vezet.
```

**Példa — Környezettudomány:**

```
A következő kérdéshez:
"Miért emelkedik a nitrátkoncentráció a felső-tiszai kutak vizében?"

Javasolj részkérdéseket, amelyek segítenek feltárni a probléma
különböző aspektusait (geológiai, mezőgazdasági, hidrológiai,
szabályozási), és amelyek megválaszolása egy átfogóbb,
megalapozottabb végső válaszhoz vezet.
```

**Példa — Társadalomtudomány:**

```
A következő kérdéshez:
"Miért csökken a természettudományos pályára jelentkezők száma
Magyarországon?"

Javasolj részkérdéseket, amelyek segítenek feltárni a probléma
különböző aspektusait (oktatási, gazdasági, kulturális, demográfiai),
és amelyek megválaszolása egy átfogóbb, megalapozottabb végső
válaszhoz vezet.
```

**Mire figyelj:** Ez az egyik legmegbízhatóbb mintázat, mert nem a válasz faktualitásától függ, hanem a *gondolkodási struktúra* minőségétől. Az LLM-ek általában jól bontják részkérdésekre a problémákat — de a részkérdésekre adott válaszokat ugyanúgy ellenőrizni kell, mint bármely más AI-kimenetet.

---

### 2.4.8 Fact Check List — Feltételezések explicitté tétele

**Mire jó?** Arra kéri a modellt, hogy minden válaszához csatoljon egy listát azokról a tényekről és feltételezésekről, amelyekre a válasz épül — így te eldöntheted, melyiket kell ellenőrizni.

**Sablon:**

```
Mostantól, amikor választ adsz, készíts egy listát azokról a tényekről,
amelyekre a válasz épül, és amelyeket érdemes ellenőrizni.
Ezt a listát a válaszod végén jelenítsd meg.
```

**Példa — Farmakológia:**

```
Mostantól, amikor választ adsz, készíts egy listát azokról a tényekről,
amelyekre a válasz épül, és amelyeket érdemes ellenőrizni.
Ezt a listát a válaszod végén jelenítsd meg.

Kérdés: Milyen mechanizmuson keresztül fejti ki hatását a metformin
a 2-es típusú cukorbetegség kezelésében?
```

**Példa — Geológia:**

```
Mostantól, amikor választ adsz, készíts egy listát azokról a tényekről,
amelyekre a válasz épül, és amelyeket érdemes ellenőrizni.
Ezt a listát a válaszod végén jelenítsd meg.

Kérdés: Mi okozza a bükki mészkőbarlangok cseppkőképződését,
és milyen ütemben növekednek a sztalaktitok?
```

**Várható kimeneti forma:**

A válasz után valami ilyesmit látsz:

> **Ellenőrizendő tények:**
> 1. A sztalaktit-növekedési ütem évi 0,01–0,3 mm — ✓ forrás: Fairchild & Baker (2012)
> 2. A CO₂ parciális nyomása a talajban 10-100× a légköri érték — ✓ ellenőrizendő
> 3. A bükki barlangok uralkodó kőzete triász mészkő — ✓ ellenőrizendő helyi geológiai adatokkal

<!-- [SZERKESZTOI MEGJEGYZES / GPT-5.4 review] "te felelősséged" — a "te maradsz a felelos" vezermmotivum ismetlodik a konyvben (lasd meg 2.7.5 "masodpilota" szekció es tobb kesobbi fejezet). Erdemes ellenorizni, hogy az ismetlesek uj kontextust adnak-e, vagy tartalmilag redundansak. -->
**Mire figyelj:** Ez a mintázat nem garantálja, hogy a tények helyesek — csak annyit tesz, hogy *explicitté* teszi őket. A tényleges ellenőrzés a te felelősséged. De már az is hatalmas segítség, ha tudod, *mit* kell ellenőrizni, ahelyett, hogy vakon elfogadnád az egész választ.

---

### 2.4.9 Context Manager — Az AI fókuszának beállítása

**Mire jó?** Szűkíti a modell válaszának hatókörét: megmondod, milyen kontextust vegyen figyelembe, és mit hagyjon figyelmen kívül. Különösen hasznos, ha egy szakterület egy nagyon specifikus részterületéről kérdezel, és nem akarod, hogy a modell az általános áttekintésnél ragadjon le.

**Sablon:**

```
Amikor a [téma] témáról válaszolsz, kizárólag a [specifikus altéma]
információit vedd figyelembe. Hagyd figyelmen kívül a [kizárt altéma]
szempontokat.
```

**Példa — Hidrológia:**

```
Amikor a Tisza vízminőségéről válaszolsz, kizárólag a mikrobiológiai
paramétereket vedd figyelembe (coliform-szám, E. coli, Enterococcus).
Hagyd figyelmen kívül a kémiai paramétereket (nehézfémek, nitrát, foszfát)
és a fizikai paramétereket (hőmérséklet, zavarosság, vezetőképesség).
```

**Példa — Klímatudomány:**

```
Amikor az éghajlatváltozás hatásairól válaszolsz, kizárólag
a Kárpát-medence szőlőtermesztésére gyakorolt hatásokat vedd figyelembe.
Hagyd figyelmen kívül a globális hatásokat és más mezőgazdasági
ágazatokat.
```

**Mire figyelj:** A NASA-tapasztalatok szerint a lusta, általános megfogalmazás (pl. „Hagyd figyelmen kívül a transit módszert") nem mindig működik — a modell gyakran mégis belefoglalja a kizárt témát. Strukturáltabban kell fogalmazni: egyértelműen megmondani, mit *tartalmazzon* a válasz, nem csak azt, mit ne.

---

## 2.5 Mintázatok kombinálása — egy kidolgozott példa

A fenti kilenc mintázat önmagában is hasznos, de igazi erejüket a *kombinálásban* nyerik el. Nézzük meg, hogyan rakhatunk össze egy összetett promptot egy valós kutatási feladathoz.

**A helyzet:** Egy debreceni növényökológus szeretné megérteni, hogyan alkalmazhatna távérzékelési módszereket a löszgyepek állapotfelmérésére a Hortobágyon — de eddig kizárólag terepi módszerekkel dolgozott.

**A kombinált prompt:**

```
[Persona + Recipe + Context Manager + Fact Check List kombináció]

Te egy távérzékelési szakértő vagy, aki ökológiai alkalmazásokra
specializálódott, különösen száraz gyepterületek monitorozására
Közép-Európában. (PERSONA)

Szeretném megérteni, hogyan alkalmazhatok műholdas távérzékelést
a hortobágyi löszgyepek állapotfelmérésére.

Tudom, hogy szükségem lesz:
- vegetációs indexek kiszámítására (NDVI, EVI)
- terepi referencia-adatokra
- valamilyen osztályozási módszerre

Kérlek, adj egy teljes munkafolyamatot a műholdas adatkiválasztástól
az eredmények validálásáig. Töltsd ki a hiányzó lépéseket. (RECIPE)

Kizárólag a Sentinel-2 adatokra fókuszálj, és hagyd figyelmen kívül
a Landsat, MODIS és drón-alapú megközelítéseket. (CONTEXT MANAGER)

A válaszod végén készíts egy listát azokról a tényekről, amelyekre
a válasz épül, és amelyeket érdemes ellenőrizni. (FACT CHECK LIST)
```

**Miért működik ez jól?**

1. A **Persona** beállítja a szakmai szintet és a nézőpontot.
2. A **Recipe** strukturálja a választ lépésekre.
3. A **Context Manager** megakadályozza, hogy a modell szétszóródjon.
4. A **Fact Check List** átláthatóvá teszi, mit kell utána ellenőrizni.

**Továbbfejlesztés:** Ha a válasz megérkezett, használd a **Question Refinement** mintázatot, hogy a felmerülő részkérdéseket pontosítsd, majd az **Alternative Approach** mintázattal kérdezz rá a Sentinel-2-n kívüli opciókra is — de *tudatosan*, miután a fő megközelítést megértetted.

> **🌾 Szakterületi példa: Természetes nyelvű GIS-lekérdezések**
>
> Az Autonomous GIS-ben a térinformatikus nem SQL-t vagy Python-kódot ír, hanem természetes nyelven kérdez: „Melyik Natura 2000 területen nőtt a beépítettség 2020 óta?" — és a rendszer maga generálja a lekérdezést, futtatja az elemzést, és megjeleníti az eredményt térképen. Az egyszerű kérdéstől („mely települések vannak 500 m-en belül?") az összetett tér-idő elemzésig a felhasználó természetes nyelven kommunikál a GIS-sel. Ez a promptolási minták közvetlen alkalmazása: a Persona, Recipe és Context Manager kombinációja a térinformatikai szoftverbe építve.
>
> *Forrás: gis 21.9 „Természetes nyelvű GIS-lekérdezések: részletes példák"*

---

## 2.6 Paraméterek: hőmérséklet, top-p, rendszerprompt

A promptok mellett van néhány technikai paraméter, amelyet a legtöbb platformon beállíthatsz (vagy amelyek a háttérben működnek). Ezek finomhangolják, *hogyan* generálja a modell a választ.

### 2.6.1 Hőmérséklet (temperature)

> **Definíció: Hőmérséklet (temperature)** — Egy szám (jellemzően 0 és 2 között), amely szabályozza, mennyire „kreatív" vagy „kiszámítható" a modell válasza. Alacsony hőmérséklet (pl. 0,1) esetén a modell szinte mindig a legvalószínűbb tokent választja — a válasz konzisztens, de száraz. Magas hőmérséklet (pl. 1,5) esetén a modell kisebb valószínűségű tokeneket is választhat — a válasz változatosabb, kreatívabb, de megbízhatatlanabb.

**Analógia:** Képzeld el a hőmérsékletet úgy, mint egy egyetemi kolléga viselkedését. Alacsony hőmérsékleten ő a pedáns statisztikus, aki mindig a tankönyvi választ adja. Magas hőmérsékleten ő a kreatív brainstorming-partner, aki vad ötleteket dob be — amelyek néha zseniálisak, néha abszurdak.

**Mikor állítsd alacsonyra (0–0,3)?**
- Ténykérdések, definíciók megadásakor
- Kód generálásakor
- Adatkivonatoláskor (structured data extraction)
- Hivatkozások keresésekor (bár erre amúgy se ideális az AI)

**Mikor állítsd magasabbra (0,7–1,2)?**
- Ötleteléskor (brainstorming)
- Alternatív hipotézisek generálásakor
- Kreatív szöveg írásakor (konferencia-poszter címe, pályázat „impact" szekciója)

**Mikor ne nyúlj hozzá?**
- A legtöbb általános kutatási kérdésnél az alapértelmezett beállítás (jellemzően 0,7–1,0 körül) megfelelő.

### 2.6.2 Top-p (nucleus sampling)

> **Definíció: Top-p** — Egy szám 0 és 1 között, amely azt szabályozza, mekkora valószínűségi „medencéből" választ a modell. Top-p = 0,5 azt jelenti, hogy a modell csak azokból a tokenekből választ, amelyek együttesen lefedik a valószínűség-eloszlás felső 50%-át. Top-p = 1,0 azt jelenti, hogy az összes lehetséges token szóba jöhet.

A top-p és a hőmérséklet hasonló hatást ér el, de más módon. A gyakorlatban:

- **Top-p = 0,1:** Nagyon determinisztikus, szinte nincs variáció.
- **Top-p = 0,9:** Széles választék, változatosabb válaszok.

**Gyakorlati tanács:** Ne változtasd egyszerre a hőmérsékletet *és* a top-p-t. Válassz egyet, és azzal kísérletezz. A legtöbb tudományos feladathoz a hőmérséklet intuitívabb és könnyebben kezelhető paraméter.

### 2.6.3 Rendszerprompt (system prompt)

> **Definíció: Rendszerprompt (system prompt)** — Egy speciális utasítás, amelyet a beszélgetés *elején* adsz a modellnek, és amely az egész interakciót keretezi. A rendszerprompt határozza meg a modell „személyiségét", viselkedési szabályait, válaszformátumát és korlátait. A felhasználó üzeneteitől elkülönítve kezeli a rendszer, és (elvileg) nagyobb súlya van.

A rendszerprompt a chatfelületen nem mindig érhető el közvetlenül — az API-n és egyes haladó felületeken (pl. Claude Projects, ChatGPT Custom Instructions) azonban beállítható.

**Példa — Kutatási asszisztens rendszerpromptja:**

```
Te egy szigorú, de segítőkész tudományos asszisztens vagy.
A felhasználó magyar környezetkutató, PhD-hallgató.

Szabályok:
1. Minden faktikus állításnál jelezd a bizonytalanságodat
   (biztos / valószínű / bizonytalan).
2. Soha ne találj ki irodalmi hivatkozást. Ha nem vagy biztos
   egy hivatkozásban, írd: "[hivatkozás ellenőrzendő]".
3. Ha egy kérdés túlmutat a tudásodon, mondd meg őszintén.
4. Válaszolj magyarul, de a szakkifejezéseket angolul is
   tüntesd fel zárójelben.
5. Tartsd a válaszaidat strukturáltan: használj számozott
   listákat és alcímeket.
```

**Miért fontos ez kutatóknak?** Mert egy jól megírt rendszerprompt drámaian csökkenti a hallucináció-kockázatot. Az a szabály, hogy „soha ne találj ki hivatkozást", nem *garantálja*, hogy a modell nem fog — de a tapasztalat szerint jelentősen csökkenti az ilyen esetek számát.

---

## 2.7 Bizonyítékminőség és ellenőrzés

Ez talán a fejezet legfontosabb szekciója. Mindaz, amit eddig olvastál — a promptminták, a paraméterek, a platformok — eszközök. De az eszköz értéke azon múlik, hogyan kezeled az eredményeit.

### 2.7.1 Hogyan ismerd fel a módszertanilag gyenge AI-választ?

Egy AI-válasz módszertani gyengeségének jelei:

1. **Túlzott magabiztosság részletes állításokban.** Ha a modell pontos számokat ad (pl. „a biodiverzitásvesztés üteme évi 2,7%") hivatkozás nélkül — gyanús. A valós tudományban a pontos számokhoz mindig forrás társul.

2. **Hivatkozások, amelyek „túl jók, hogy igazak legyenek".** Ha a modell egy tökéletesen releváns cikket idéz tökéletesen releváns címmel és szerzőkkel — ellenőrizd. A hallucinált hivatkozások gyakran *hihetetlenül* célratörőek, mert a modell a kérdésedből generálja őket visszafelé.

3. **Egyoldalú áttekintés.** Ha a modell nem említ ellenérveket, alternatív magyarázatokat vagy korlátokat — az nem objektív összefoglaló, hanem szöveggeneráló mintázat.

4. **Terminológiai zavar.** Ha a modell felváltva használ szinonimákat, amelyek valójában nem szinonimák a szakterületen (pl. „accuracy" és „precision"), az felszínes „értésre" utal.

5. **Anakronisztikus információ.** A modell a tanítási adatai alapján válaszol — ha 2024-es tanítóadatokkal rendelkezik, a 2025-ös fejleményekről nem tudhat (hacsak nem webes keresést végez).

### 2.7.2 Keresztellenőrzés hiteles forrásokkal

Az AI-válasz soha nem végpont — mindig kiindulópont. Az ellenőrzés lépései:

1. **Hivatkozás-verifikáció.** Minden AI által javasolt hivatkozást ellenőrizz a Google Scholarben, a Crossref-en vagy a DOI-feloldón. Létezik-e a cikk? Az a szerző írta? Abban a folyóiratban jelent meg? Azt mondja, amit az AI állít?

2. **Állítás-verifikáció.** A kulcsfontosságú állításokat nézd meg legalább egy másik, hiteles forrásban (tankönyv, review cikk, adatbázis). Ha az AI azt állítja, hogy a Tisza éves átlagos vízhozama X m³/s — nézd meg az OVF vagy VIZITERV adatbázisában.

3. **Konzisztencia-ellenőrzés.** Kérdezd meg ugyanazt más szavakkal, vagy más platformon. Ha két különböző AI ellentétes választ ad, az piros zászló.

4. **Szakértői validáció.** A komplex kérdéseknél az AI-válasz maximum a *kiindulópont* lehet a szakértővel való beszélgetéshez — nem a helyettesítője.

### 2.7.3 Az átlátszatlanság problémája

Az LLM-ek fundamentális korlátja, hogy **nem tudod rekonstruálni, hogyan jutottak egy válaszhoz**. Amikor egy statisztikai tesztet alkalmazol, pontosan tudod, milyen feltételezésekre épül, és a számítás minden lépése auditálható. Amikor egy LLM válaszol, a „gondolkodási folyamat" egy milliárd-paraméterű neurális háló súlyaiban van kódolva — még az AI fejlesztői sem tudják pontosan megmondani, miért generálta az adott választ.

Ez az opacity problem — az átlátszatlanság problémája — a tudományos alkalmazásban különösen súlyos. A tudomány alapelve a megismételhetőség és a módszertani transzparencia. Amikor az AI-t kutatási eszközként használod, dokumentálnod kell:

- Milyen modellt használtál (név és verzió)?
- Mi volt a prompt?
- Milyen paramétereket állítottál be?
- Hogyan validáltad az eredményt?

Ezek nélkül az AI-asszisztált kutatás nem megismételhető — és ami nem megismételhető, az nem tudomány.

### 2.7.4 Kritikus gondolkodás az AI korában

A kognitív torzítások, amelyeket Narayanan és Kapoor dokumentál, fokozottan érvényesek az AI-val való interakcióban:

- **Az automatizálás torzítása (automation bias).** Hajlamosak vagyunk elfogadni a gépi választ, különösen ha az magabiztosan, jól strukturáltan van megfogalmazva. Egy LLM válasza *mindig* magabiztos — ez nem a pontosság jele, hanem a szöveggenerálás sajátossága.

- **A halo-effektus.** Ha az AI egy korábbi kérdésedre brilliáns választ adott, hajlamos leszel a következő válaszát is kritikátlanul elfogadni. De az LLM-ek teljesítménye *nem konzisztens* — Mollick „egyenetlen határvonalnak" (jagged frontier) nevezi ezt a jelenséget. Az AI egy nehéz feladatot megoldhat brilliánsan, miközben egy egyszerűn megbukik.

- **A kvantifikációs torzítás.** Ha az AI számokat ad (90%-os pontosság, p < 0.001), hajlamosak vagyunk nagyobb hitelt adni nekik, mint amennyit érdemelnek — anélkül, hogy megkérdeznénk: mit jelent ez a kontextusban?

- **Az illuzórikus megértés.** Az LLM-mel való beszélgetés *átélése* azt az érzést kelti, hogy valódi párbeszédet folytatsz egy gondolkodó entitással. Ez nem így van. Az LLM nem ért, nem gondolkodik, nem formál véleményt. Jól jósolja meg, milyen szöveg következne a te szöveged után — és ez néha megdöbbentően hasznosnak tűnik, de fundamentálisan különbözik a megértéstől.

Carl Sagan „badarságdetektora" (baloney detection kit) itt fontosabb, mint valaha. Minden AI-válasznál kérdezd meg magadtól:

1. Honnan „tudhatná" ezt a modell? (A tanítóadataiból — amelyek tartalmazhatnak hibákat.)
2. Hogyan ellenőrizhetem? (Független forrásból — nem egy másik prompttal.)
3. Mi változna, ha ez téves lenne? (Ha sok múlik rajta, több ellenőrzés kell.)
4. Milyen alternatív magyarázat létezik? (Az AI hajlamos egyetlen narratívát adni.)

### 2.7.5 A „másodpilóta" filozófia

A NASA a maga útmutatójában gyönyörű analógiát használ: az AI olyan, mint a másodpilóta (co-pilot) egy repülőgépen. Segít navigálni, figyeli a műszereket, kiszámol dolgokat — de a felelősség mindig a kapitányé. És a kapitány *soha nem hagyja az autopilótát felügyelet nélkül*, különösen nem leszálláskor.

Mollick hasonló következtetésre jut a négy szabályával:

1. **Mindig hívd meg az AI-t az asztalhoz.** Próbáld ki minden feladatnál — mert az AI képességeinek határvonala egyenetlen és állandóan változik. Nem tudhatod, miben segít, amíg ki nem próbálod.

2. **Légy az ember a hurokban.** Az AI hibázik — hallucinál, torzít, konfabulál. Te vagy a minőségellenőrzés. De az „ember a hurokban" lenni többet jelent, mint a kimenet átnézését: elég szaktudás kell ahhoz, hogy a *plauzibilisen hangzó* hibákat is felismerd.

3. **Kezeld úgy, mint egy embert — de mondd meg, milyen embert.** A persona prompting azért működik, mert a modell emberi szövegeken tanult. Amikor szerepet adsz neki, a válaszgenerálás eloszlása az adott szerep szövegmintázatai felé tolódik.

4. **Feltételezd, hogy ez a legrosszabb AI, amit valaha használni fogsz.** A mai modellek primitívek lesznek az 5 év múlvaiakhoz képest. Fektess be most a tanulásba — a megtérülés exponenciálisan nő.

A másodpilóta analógia legfontosabb tanulsága: **a cél nem az, hogy az AI gondolkodjon helyetted, hanem az, hogy te jobban gondolkodj az AI segítségével**.

---

## 2.8 Összefoglaló: a társalgási AI mint kutatási eszköz

Ebben a fejezetben az alábbi koncepciókat definiáltuk és jártuk körül:

| Fogalom | Rövid definíció |
|---------|----------------|
| **Token** | Az LLM legkisebb szövegegysége — szó, szótöredék vagy írásjel |
| **Kontextusablak (context window)** | A modell „munkamemóriája" — ennyi tokent lát egyszerre |
| **Hallucináció** | Magabiztos, de hamis AI-kimenet |
| **Prompt** | Az utasítás/kérdés, amit a modellnek adsz |
| **Prompt engineering** | A promptok tudatos tervezése a jobb válaszokért |
| **Hőmérséklet (temperature)** | A válasz kreativitásának/kiszámíthatóságának szabályozója |
| **Top-p** | A válasz diverzitásának szabályozása valószínűségi küszöbbel |
| **Rendszerprompt (system prompt)** | Az interakciót keretező háttér-utasítás |

A kilenc prompt-mintázat, amelyet a NASA anyaga alapján adaptáltunk:

| Mintázat | Fő alkalmazás |
|----------|--------------|
| Recipe | Kísérleti protokollok, lépéssoros munkafolyamatok |
| Output Automator | Szkriptek, automatizálható kimenetek |
| Persona | Szakértői nézőpont, szerepalapú válaszok |
| Flipped Interaction | Szókratészi tanulás, hipotézis-tesztelés |
| Question Refinement | Kutatási kérdések élesítése |
| Alternative Approach | Módszertani alternatívák feltérképezése |
| Cognitive Verifier | Komplex problémák dekompozíciója |
| Fact Check List | Feltételezések explicitté tétele |
| Context Manager | Az AI fókuszának szűkítése |

És a legfontosabb lecke: **az AI válaszai nem bizonyítékok — hipotézisek, amelyeket ellenőrizni kell**.

---

## 2.9 Próbáld ki — gyakorlati feladatok

1. **Ismerkedés a platformokkal.** Ugyanazt a kutatási kérdést tedd fel Claude-nak, ChatGPT-nek és Gemininek. Hasonlítsd össze a válaszok mélységét, struktúráját és a hivatkozott irodalmat. Hány hivatkozás valódi?

2. **Recipe pattern a saját munkádhoz.** Fogalmazz meg egy Recipe promptot a saját kutatási módszertanod egy lépéséhez, amelyet jól ismersz. Mennyire pontos az AI válasza?

3. **Persona + Fact Check List kombináció.** Kérj meg egy AI-t, hogy válaszoljon egy szakterületeden kívüli kérdésre szakértői személyiségben, és csatolja a tényellenőrzési listát. Ellenőrizz legalább 3 tényt a listáról.

4. **Hőmérséklet-kísérlet.** Ha API-hozzáférésed van (vagy egy platformon állíthatod a hőmérsékletet), tedd fel ugyanazt a kérdést temperature = 0,1 és temperature = 1,5 beállítással. Dokumentáld a különbségeket.

5. **Rendszerprompt írása.** Írj egy rendszerpromptot a saját kutatási területedhez, amely tartalmazza a fenti „szabályokat" (bizonytalanság jelzése, hivatkozások ellenőrzése stb.). Használd egy héten át, és figyeld, hogyan változik az AI válaszainak minősége.

---

*A következő fejezetben (3. fejezet) a tudományos írás specifikus feladataival foglalkozunk: hogyan segíthet az AI a cikkstruktúra kialakításában, a szöveg javításában és a peer review-ra való felkészülésben — de miért nem szabad a tartalomgenerálást rábízni.*

---

## Hivatkozások és további olvasmányok

- White, J., Fu, Q., Hays, S. et al. (2023). *A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT.* arXiv:2302.11382.
- NASA Science Mission Directorate (2024). *LLM Cookbook for Open Science.* https://github.com/nasa-impact/smd-llm-workshop
- Mollick, E. (2024). *Co-Intelligence: Living and Working with AI.* Portfolio/Penguin. — 3. fejezet: Four Rules for Co-Intelligence.
- Narayanan, A. & Kapoor, S. (2024). *AI Snake Oil: What Artificial Intelligence Can Do, What It Can't, and How to Tell the Difference.* Princeton University Press. — 4. fejezet: The Language of Deception; 7. fejezet: Why Do Myths About AI Persist?
- Habibi, F., Khodadadi, E. & Salehi, H. (2023). *ChatGPT for Scientific Research: A Hands-on Guide.* — 1. fejezet.
- Frankfurt, H. G. (2005). *On Bullshit.* Princeton University Press.
- Bender, E. M. et al. (2021). On the Dangers of Stochastic Parrots: Can Language Models Be Too Big? *FAccT 2021.*
- Vaswani, A. et al. (2017). Attention Is All You Need. *NeurIPS.*
- Kapoor, S. & Narayanan, A. (2023). Leakage and the Reproducibility Crisis in Machine-Learning-Based Science. *Patterns.*
- Walters, W. H. & Wilder, E. I. (2023). Fabrication and Errors in Bibliographic Citations Generated by ChatGPT. *Scientific Reports.*
