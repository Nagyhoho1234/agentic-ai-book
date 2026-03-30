# 8. fejezet: Vizuális programozás és munkafolyamat-tervezés

> **Fejezet-informacio**
> - **Kinek szol:** Vizualisan gondolkodo kutatoknak, akik kod nelkul szeretnenek automatizalni
> - **Eloismeretek:** 4. fejezet (adatelemzes); a 7. fejezet hasznos, de nem kotelezo
> - **Amit megtanulsz:**
>   - Node-alapu vizualis programozas alapfogalmai
>   - n8n, KNIME, LangFlow es Node-RED eszkozok hasznalata
>   - Mikor valaszd a vizualis megkozelitest es mikor a hagyomanyos kodolast
> - **Szukseges eszkozok:** Browser + terminal (n8n/KNIME telepites)
> - **Kapcsolodo fejezetek:** 5. fejezet (kodolas), 7. fejezet (pipeline-ok), 12. fejezet (agensek epitese)

## Amikor a folyamatábra maga a program

Képzeld el Katalint, egy ökológust a Debreceni Egyetem Természettudományi Karán. Katalin remekül ért a statisztikához, a kísérlettervezéshez és az adatértelmezéshez. Amikor megtervez egy kísérletet, mindig folyamatábrát rajzol: mi történik először, milyen döntési pontok vannak, hová kerülnek az adatok, hogyan lesz belőlük eredmény. A folyamatábrái precízek, logikusak, követhetők.

De amikor le kellene ülnie Python-kódot írni, valami elakad. A szintaxis idegen, a hibaüzenetek érthetetlenek, a kapcsos zárójelek és a behúzások apró eltérései órákig tartó hibakeresésbe torkollnak. Katalin nem buta — egyszerűen másképp gondolkodik. Vizuálisan.

Egy konferencián viszont felfedez valamit, ami megváltoztatja a munkáját: egy eszközt, ahol a folyamatábrája *maga a program*. Ahol dobozokat (node-okat) húz a vászonra, összekötögetőkkel kapcsolja össze őket, és a rendszer végrehajtja pontosan azt, amit rajzolt. Nem kell szintaxist tanulnia. Nem kell hibát keresnie egy ezer soros kódban. A gondolkodása és az eszköz nyelve ugyanaz.

Ez a vizuális programozás.

Ez a fejezet neked szól, ha valaha is úgy érezted, hogy a programozás falat húz közéd és az automatizálás közé. Megmutatom, hogy a modern vizuális eszközök — az n8n-től a KNIME-on át a LangFlow-ig — hogyan teszik lehetővé, hogy kód írása nélkül építs munkafolyamatokat, adatelemzési pipeline-okat és akár mesterséges intelligenciával hajtott rendszereket.

---

## Miért működik a vizuális programozás a tudósok számára?

### A folyamatábra a természetes gondolkodás

Ha visszagondolsz a kutatási módszertanra, amit az egyetemen tanultál, szinte mindent folyamatábraként mutatok be. A kísérleti protokoll lépésekből áll. A statisztikai elemzés egymásra épülő fázisokból. Az adatfeldolgozás: betöltés, tisztítás, transzformáció, elemzés, vizualizáció. Ezek mind *szekvenciális, elágazó, összekapcsolt lépések* — pontosan az, amit egy vizuális programozási felület ábrázol.

A vizuális programozás nem egy "könnyített" változata a "valódi" programozásnak. Ez egy másik paradigma, amelynek megvannak a maga erősségei:

**Azonnali áttekinthetőség.** Egy Python-szkript olvasásához értened kell a nyelvet. Egy vizuális munkafolyamatot bárki áttekinthet egyetlen pillantással: látod, honnan jönnek az adatok, min mennek keresztül, és hová jutnak.

**Beépített dokumentáció.** A vizuális workflow maga a dokumentáció. Amikor egy éven belül visszanézel egy elemzést, nem kell visszafejtened a kódot — a rajz elmondja, mit csináltál.

**Alacsonyabb belépési küszöb.** Nem kell megtanulnod egy programozási nyelv szintaxisát ahhoz, hogy hatékony automatizálásokat építs. Ez különösen fontos olyan kutatók számára, akiknek az elsődleges feladata nem a programozás, hanem a szakterületi munka.

**Reprodukálhatóság.** A vizuális munkafolyamatok megoszthatók, újrafuttathatók, és másoknak is érthetők — a nyílt tudomány egyik alapkövetelménye.

**Kevesebb szintaktikai hiba.** Node-ok összekötögetésekor nem fogsz elfelejteni egy kettőspontot, nem cserélsz össze egy változónevet, nem hibázol a behúzásban. A hibák logikai természetűek maradnak, nem szintaktikaiak.

### Mikor NEM jó a vizuális megközelítés?

Természetesen a vizuális programozás sem mindenható. Ha egyedi algoritmusokat implementálsz, ha nagy teljesítményű számítást végzel, vagy ha egy nagyon specifikus szoftverkönyvtárat kell használnod, a hagyományos kódolás továbbra is az erősebb eszköz. A fejezet végén részletes döntési útmutatót találsz.

---

> **Ne csinalld!**
> Ne epitts bonyolult, sok node-bol allo munkafolyamatot egybol. Kezdd ket-harom node-dal (pl. fajl beolvasas → szures → kimenet), es csak akkor bovitsd, ha ez mukodik. A vizualis feluleten konnyu "lego-szenvedely"-be esni, es egy attekinthetetlen, 50 node-os szornyeteget epiteni, amelyet senki — beleertve teged harom honap mulva — nem fog megerteni.

## Node-alapú szerkesztők: az alapkoncepció

Mielőtt belevágnánk a konkrét eszközökbe, értsük meg az alapvető koncepciót, amely mindegyikben közös.

### Mi az a node?

Egy **node** (csomópont) egyetlen művelet. Lehet egyszerű — "olvasd be ezt a CSV-fájlt" — vagy összetett — "futtasd le ezt a gépi tanulási modellt". Minden node-nak vannak **bemenetei** (honnan kapja az adatot) és **kimenetei** (hová továbbítja az eredményt).

### Mi az a connection (összeköttetés)?

Amikor egy node kimenetét egy másik node bemenetéhez kötöd, **connection**-t hozol létre. Ez határozza meg az adatáramlás irányát. Az adat balról jobbra (vagy fentről lefelé) halad a munkafolyamatban.

### Mi az a workflow (munkafolyamat)?

A node-ok és connection-ök együttese egy **workflow**: a teljes feldolgozási folyamat, az adatbetöltéstől az eredményig. Ez az, ami a vizuális vásznon megjelenik — lényegében egy futtatható folyamatábra.

### A közös minta

Szinte minden vizuális eszköz ugyanazt a mintát követi:

```
[Trigger / Indítás] → [Adatforrás] → [Feldolgozás] → [Döntés] → [Kimenet]
```

Legyen szó munkafolyamat-automatizálásról (n8n), adatelemzésről (KNIME), LLM pipeline-okról (LangFlow) vagy IoT-ról (Node-RED) — az alapelv ugyanaz. Ha megtanulod az egyiket, a többit is gyorsan megérted.

> **💧 Szakterületi példa: ModelBuilder → Python export a hidrológiában**
>
> A hidrológiai térinformatikában a ModelBuilder vagy a QGIS grafikus modellező „vizuális programozást" kínál: a kutató dobozokból és nyilakból építi fel a DEM → folyásirány → vízgyűjtő munkafolyamatot, majd egyetlen kattintással Python-szkriptre exportálja. Ez pontosan az a Trigger → Adatforrás → Feldolgozás → Kimenet minta, amit fentebb láttunk. A ModelBuilder-ben felépített vízgyűjtő-lehatárolási munkafolyamat vizuálisan átlátható, és a QGIS grafikus modellező nyílt forráskódú alternatívát kínál ugyanerre.
>
> *Forrás: hidrogis ch12, 12.11 „A ModelBuilder mint híd a szkripteléshez"*

---

## n8n — Munkafolyamat-automatizálás nyílt forráskóddal

### Mi az n8n?

Az n8n (ejtsd: "n-eight-n", "nodemation" rövidítése) egy nyílt forráskódú munkafolyamat-automatizálási platform. Gondolj rá úgy, mint egy vizuális szerelőműhelyre, ahol különböző szolgáltatásokat — e-mail, adatbázis, API-k, mesterséges intelligencia — kötögethetel össze anélkül, hogy egyetlen sor kódot írnál.

Az n8n két kulcselőnye a hasonló eszközökhöz (Zapier, Make) képest:

1. **Adatvédelem.** Az n8n-t futtathatod a saját gépeden vagy a saját szerveredén. Az adataid nem kerülnek harmadik fél felhőjébe — ami kutatási adatok esetén alapvető fontosságú lehet.

2. **Költséghatékonyság.** Az n8n munkafolyamat-futásonként számol, nem lépésenként. Egy 20 lépéses workflow egyetlen futtatásnak számít, nem húsznak. Ez a különbség hatalmas lehet komplex automatizálásoknál.

### Telepítés

Három módja van az indulásnak:

**n8n Cloud (legegyszerűbb, kezdőknek ideális)**

Regisztrálj az n8n.io oldalon — kapsz egy ingyenes próbaidőszakot, nincs szükség semmilyen telepítésre. Böngészőből eléred a teljes felületet.

**Lokális telepítés (npm)**

Ha a géped előtt szeretnéd futtatni (és a Node.js már telepítve van):

```bash
npm install n8n -g
n8n
```

Ezután a böngészőben nyisd meg: `http://localhost:5678`

**Docker (ajánlott tartós használatra)**

A Docker a legstabilabb módszer, és ismerős lehet, ha a 7. fejezetből már találkoztál konténerizált környezetekkel:

```bash
docker run -it --rm --name n8n -p 5678:5678 n8nio/n8n
```

Egy akadémiai labor számára a Docker-alapú telepítés az ideális: izolált, reprodukálható, és könnyen áthelyezhető egyik gépről a másikra.

### A felület megismerése

Amikor először nyitod meg az n8n-t, a következőt látod:

- **Dashboard:** A munkafolyamatok áttekintése, keresés, új workflow létrehozása
- **Workflow Editor (Vászon):** A központi munkaterület, ahol a node-okat elhelyezed és összekötöd
- **Node Library:** Több mint 400 előre elkészített integráció — Gmail, Slack, Google Sheets, adatbázisok, AI-modellek, és még sok más
- **Credentials (Hitelesítő adatok):** API-kulcsok és OAuth tokenek biztonságos, titkosított tárolása
- **Executions (Futtatások):** Minden korábbi futtatás naplója, bemenetekkel, kimenetekkel és hibákkal

### Az első workflow: "Hello, World!"

Kezdjük a legegyszerűbb munkafolyamattal, hogy megértsd az alaplogikát:

1. Kattints a **"New Workflow"** gombra
2. Add hozzá a **Manual Trigger** node-ot (ez indítja a folyamatot, amikor rákattintasz)
3. Add hozzá egy **Set** node-ot, és állítsd be benne: `message` = `"Hello, World!"`
4. Kösd össze a Trigger kimenetét a Set bemenetével
5. Kattints az **"Execute Workflow"** gombra
6. Nézd meg a Set node kimenetét — ott van az üzeneted

Gratulálok, megépítetted az első automatizálásodat! Ez a minta — trigger, feldolgozás, kimenet — a legtöbb n8n workflow alapja.

### Trigger-ek, Action-ök, konnektorok

Az n8n node-jait három fő kategóriába sorolhatjuk:

**Trigger node-ok** — ezek indítják el a munkafolyamatot:
- **Schedule Trigger:** Időzített futtatás (naponta reggel 7-kor, minden hétfőn, 15 percenként...)
- **Webhook Trigger:** Valós idejű reagálás egy HTTP-kérésre (egy másik rendszer "szól" az n8n-nek)
- **Polling Trigger:** Rendszeres lekérdezés (5 percenként ellenőrzi, van-e új adat)
- **Chat Trigger:** Chatbot-felület, amin keresztül te magad küldöd az utasítást

**Action node-ok** — ezek hajtják végre a feladatokat:
- **Integration node-ok:** Külső szolgáltatásokhoz kapcsolódnak (Gmail, Slack, Google Drive, Notion, adatbázisok)
- **Transformation node-ok:** Adatokat alakítanak át (Set, Edit Fields, Filter, Sort)
- **HTTP Request:** Az "svájci bicska" — bármilyen API-hoz kapcsolódik, amelyhez nincs dedikált node

**Logic node-ok** — ezek hozzák a döntéseket:
- **IF:** Igen/nem elágazás (például: ha a hőmérséklet > 30°C, küldj riasztást)
- **Switch:** Többfelé ágazás (például: a cikk témája alapján különböző feldolgozás)
- **Loop Over Items:** Elemenkénti feldolgozás (például: minden egyes fájlra futtasd le ugyanazt a műveletet)
- **Merge:** Több ág eredményének egyesítése

### Példa-workflow: Publikáció-figyelő rendszer

Most építsünk valami igazán hasznos dolgot. Képzeld el, hogy szeretnéd automatikusan figyelni, megjelentek-e új cikkek a szakterületeden, és ha igen, egy AI-összefoglalót kapni róluk e-mailben.

**A workflow felépítése:**

```
[Schedule Trigger]          ← Naponta reggel 8-kor indul
       ↓
[HTTP Request]              ← Lekérdezi a PubMed/arXiv API-t
       ↓                      (keresési kifejezés: a te kulcsszavaid)
[IF]                        ← Van-e új találat az utolsó lekérdezés óta?
       ↓ (igen)
[Loop Over Items]           ← Minden egyes új cikkre:
       ↓
[OpenAI / Claude node]     ← AI összefoglalja a cikk absztraktját
       ↓                      (3-4 mondatos összefoglaló + relevancia-értékelés)
[Set Node]                  ← Formázza az üzenetet
       ↓
[Gmail / Slack node]        ← Elküldi neked az összefoglalót
```

**Lépésről lépésre:**

1. **Schedule Trigger:** Állítsd be napi futtatásra, reggel 8:00-ra. Ügyelj, hogy az n8n időzónája megegyezzen a tieddel.

2. **HTTP Request node:** Konfiguráld a PubMed E-utilities API-t vagy az arXiv API-t. Például az arXiv-nál:
   - URL: `http://export.arxiv.org/api/query`
   - Paraméterek: `search_query=all:machine+learning+ecology`, `sortBy=submittedDate`, `max_results=10`

3. **IF node:** Ellenőrizd, hogy az eredmény tartalmaz-e az utolsó 24 órában megjelent cikket. Ha nem, a workflow itt véget ér — nem kapsz felesleges e-mailt.

4. **Loop Over Items:** Ha vannak új cikkek, egyenként feldolgozza őket.

5. **OpenAI (vagy más LLM) node:** A rendszerpromptban add meg: *"Foglald össze ezt a tudományos absztraktot 3-4 mondatban magyarul. Értékeld a relevancia-szintet 1-5 skálán a következő kutatási terület szempontjából: [a te szakterületed]."*

6. **Set node:** Formázd meg a kimenetet szépen: cím, szerzők, AI-összefoglaló, relevancia, link az eredeti cikkre.

7. **Gmail node:** Küldd el magadnak (vagy a kutatócsoportodnak) az összesített napi összefoglalót.

Ez a workflow naponta 5-10 perc olvasást spórol meg neked, és biztosítja, hogy nem maradsz le fontos publikációról. És mindezt egyetlen sor kód nélkül építetted meg.

### AI-integráció az n8n-ben

Az n8n egyik legnagyobb erőssége, hogy közvetlenül integrálhatók bele nagy nyelvi modellek (LLM-ek). Az AI-node-ok a következő feladatokra használhatók munkafolyamatokon belül:

- **Szöveg-összefoglalás:** Hosszú dokumentumok, cikkek, jegyzőkönyvek tömörítése
- **Osztályozás:** Bejövő adatok (e-mailek, kérdőív-válaszok, cikkek) automatikus kategorizálása
- **Fordítás:** Többnyelvű kutatási együttműködésekhez
- **Adatkinyerés:** Struktúrálatlan szövegből (PDF-ek, e-mailek) strukturált adatok kinyerése
- **Döntéstámogatás:** Az AI javaslatot tesz, de a végső döntést te hozod

Az n8n-ben az AI-integráció a következő node-okkal történik:

- **Chat Model node-ok:** OpenAI (GPT-4), Anthropic (Claude), Google (Gemini) és más LLM-ek csatlakoztatása
- **AI Agent node:** Egy "koordinátor", amely célokat kap, és eszközöket (tool-okat) használ azok eléréséhez
- **Memory node-ok:** Beszélgetés-kontextus megőrzése több üzenetváltáson keresztül

Fontos: az AI Agent node részletes tárgyalása — többágenses rendszerek, tool-használat, MCP-integráció — a 12. fejezetben következik. Itt most azt értsd meg, hogy az n8n-ben az AI nem egy különálló világ, hanem egyszerűen egy újabb node, amelyet beköthetsz a munkafolyamatodba.

### Az n8n kifejezés-szintaxisa

Az n8n-ben az adatok JSON-tömbökként áramlanak node-ról node-ra. Ha egy node kimenetéből szeretnél adatot felhasználni egy másik node-ban, **kifejezéseket** (expression) használsz:

```
{{ $('NodeNeve').item.json.mezo.almezo }}
```

Például, ha az OpenWeatherMap node-ból kéred a hőmérsékletet:

```
{{ $('OpenWeatherMap').item.json.main.temp }}
```

Ez a szintaxis az n8n "titkos fűszere" — ha ezt megtanulod, bármilyen adatot átmozgathatsz bármelyik node-ból bármelyik másikba.

### Mikor használj n8n-t, és mikor írj kódot?

| Használj n8n-t, amikor... | Írj kódot, amikor... |
|---|---|
| Szolgáltatásokat kötsz össze (API → e-mail → adatbázis) | Egyedi algoritmust implementálsz |
| Rendszeres, ütemezett feladatokat automatizálsz | Nagy adatmennyiséget dolgozol fel egyedi logikával |
| Prototípust építesz gyorsan | Teljesítmény-kritikus a feladat |
| Nem programozó kollégákkal közösen dolgozol | Specifikus tudományos könyvtárat kell használnod |
| AI-t integrálsz meglévő munkafolyamatba | A workflow 50+ elágazást tartalmaz |

Az n8n ereje a *rendszerek összekapcsolásában* van. Ha a feladatod az, hogy "ha X történik, csináld Y-t, majd Z-t", az n8n a te eszközöd.

---

## KNIME Analytics Platform — Adatelemzés vizuálisan

### Mi a KNIME?

A KNIME (ejtsd: "nájm", a "Konstanz Information Miner" rövidítése) egy ingyenes, nyílt forráskódú analitikai platform, amelyet a Konstanzi Egyetemen fejlesztettek ki Németországban. A KNIME kifejezetten az adatelemzésre és a prediktív analitikára lett tervezve — nem munkafolyamat-automatizálásra (mint az n8n), hanem tudományos adatfeldolgozásra.

Miért népszerű a KNIME az adattudományban?

1. **Ingyenes és nyílt forráskódú** — nincs licencdíj, ami akadémiai környezetben alapvető szempont
2. **"Citizen data scientist" filozófia** — a KNIME-ot kifejezetten azzal a céllal tervezték, hogy domain-szakértők (biológusok, közgazdászok, mérnökök) is végezhessenek komoly adatelemzést programozás nélkül
3. **CRISP-DM integráció** — a KNIME munkafolyamatai természetesen követik a CRISP-DM (Cross-Industry Standard Process for Data Mining) módszertant, amely az adatelemzés ipari szabványa
4. **Hatalmas node-könyvtár** — több ezer node áll rendelkezésre: adatbetöltés, tisztítás, transzformáció, statisztika, gépi tanulás, deep learning, szövegbányászat, kép-feldolgozás
5. **Reprodukálhatóság** — a workflow maga a dokumentáció, megosztható és újrafuttatható

### A KNIME felülete

A KNIME felépítése hasonló az n8n-hez, de az adattudományra van optimalizálva:

- **Workflow Editor (Vászon):** Itt helyezed el és kötöd össze a node-okat
- **Node Repository:** Kereshető katalógus, kategóriák szerint rendezve (I/O, Manipulation, Analytics, Views, stb.)
- **KNIME Explorer:** Projektek és munkafolyamatok kezelése
- **Node Description:** A kiválasztott node részletes dokumentációja
- **Console:** Futtatás monitorozása és hibaelhárítás

A KNIME egyedi jellemzője a **jelzőlámpa-rendszer**: minden node-on van egy státuszjelző:
- **Piros:** Nincs konfigurálva (még be kell állítanod)
- **Sárga:** Konfigurálva van, de még nem futott le
- **Zöld:** Sikeresen végrehajtva

Ez a vizuális visszajelzés azonnal megmutatja, hol tart az elemzésed.

### Port-típusok a KNIME-ban

A node-ok portjain keresztül áramlik az adat:
- **Adatportok (háromszög):** Adattáblákat visznek
- **Modellportok (kék négyzet):** Betanított modelleket adnak tovább
- **Flow variable portok (piros kör):** Paramétereket továbbítanak, amelyek dinamikussá teszik a munkafolyamatot

### KNIME AI Assistant: munkafolyamatok természetes nyelvvel

A KNIME legújabb fejlesztése a beépített **AI Assistant**, amellyel természetes nyelven írhatsz le egy elemzési feladatot, és a rendszer javaslatot tesz a megfelelő munkafolyamatra.

Például beírod:
> *"Tölts be egy CSV-fájlt, szűrd ki a hiányzó értékeket, normalizáld a numerikus oszlopokat, futtass k-means klaszterezést 3 klaszterrel, és jelenítsd meg az eredményt szórásgrafikon-on."*

Az AI Assistant összeállít egy workflow-vázlatot a megfelelő node-okkal. Te átnézed, módosítod ha kell, és futtatod. Ez drámaian lerövidíti a tanulási görbét — nem kell ismerned a több ezer node nevét, elég ha leírod, mit szeretnél.

### Példa: Teljes adatelemzési workflow kód nélkül

Vegyünk egy konkrét példát. Tegyük fel, hogy van egy ökológiai adathalmazod Hortobágyi madármegfigyelésekből: fajnév, dátum, koordináták, időjárási adatok, élőhely-típus. Szeretnéd megérteni, milyen csoportokat alkotnak a megfigyelések.

**A KNIME workflow:**

```
[CSV Reader]                    ← Betölti az adatfájlt
       ↓
[Data Explorer]                 ← Áttekintés: oszloptípusok, eloszlások, hiányzó értékek
       ↓
[Missing Value]                 ← Hiányzó értékek kezelése (átlag, medián, vagy elhagyás)
       ↓
[Column Filter]                 ← Csak a releváns oszlopok megtartása
       ↓
[Normalizer]                    ← Numerikus értékek normalizálása (min-max vagy z-score)
       ↓
[k-Means]                       ← Klaszterezés (k=3, 4, 5 — próbálgasd)
       ↓
[Color Manager]                 ← Szín hozzárendelése a klaszterekhez
       ↓
[Scatter Plot]                  ← Vizualizáció: két változó mentén ábrázolva,
                                   szín = klaszter
```

**Lépésről lépésre:**

1. **CSV Reader:** Duplán kattints a node-ra, böngészd ki a fájlodat, kattints az "OK"-ra. Ennyi. A node beolvassa az adatokat és felismeri az oszloptípusokat.

2. **Data Explorer:** Kösd össze az előző node kimenetével, futtasd le (zöld háromszög gomb). A node megmutatja az eloszlásokat, az alapstatisztikákat, a hiányzó értékek arányát. Ez az első lépés, mielőtt bármit tennél az adatokkal.

3. **Missing Value:** Konfigurálás a node dupla kattintásával: válaszd ki, hogy a hiányzó numerikus értékeket átlaggal, mediánnal pótold-e, vagy az egész sort eldobod. Kategorikus értékeknél a leggyakoribb értékkel.

4. **Column Filter:** Jelöld ki, melyik oszlopokra van szükséged a klaszterezéshez. A "fajnév" és a "dátum" szöveges mezők most nem kellenek — csak a numerikus jellemzők (hőmérséklet, tengerszint feletti magasság, csapadék stb.).

5. **Normalizer:** Válassz normalizálási módszert (min-max a [0,1] tartományra skáláz, z-score az átlagot 0-ra, a szórást 1-re állítja). Ez fontos, mert a klaszterezés érzékeny a változók skálájára.

6. **k-Means:** Állítsd be a klaszterek számát. Nem tudod, mennyi a jó? Próbáld ki 3-mal, 4-gyel, 5-tel, és hasonlítsd össze az eredményeket. A node kimenete az eredeti táblázat egy új "Cluster" oszloppal kiegészítve.

7. **Color Manager + Scatter Plot:** Rendelj színt a klaszterekhez, majd ábrázold őket. Azonnal láthatod, milyen csoportokat talált az algoritmus.

Ez az egész elemzés **nulla sor kóddal** készült. Minden lépés látható, auditálható, és bárki által megismételhető.

### Prediktív analitika programozás nélkül

A KNIME igazi ereje a prediktív modellezésben mutatkozik meg. A platform támogatja a leggyakoribb gépi tanulási algoritmusokat, mind vizuálisan konfigurálhatóan:

**Felügyelt tanulás (supervised learning):**
- **Osztályozás:** Decision Tree, Random Forest, Gradient Boosted Trees, Logistic Regression, SVM, Neural Network
- **Regresszió:** Linear Regression, Polynomial Regression, Random Forest Regressor

**Felügyelet nélküli tanulás (unsupervised learning):**
- **Klaszterezés:** k-Means, Hierarchical Clustering, DBSCAN
- **Dimenziócsökkentés:** PCA (Principal Component Analysis)

**Egy tipikus prediktív workflow:**

```
[Adatbetöltés] → [Tisztítás] → [Partitioning] → [Learner] → [Predictor] → [Scorer]
                                     ↓                            ↑
                              [Training set]              [Test set]
```

A **Partitioning** node kettéosztja az adatot tanító és teszt halmazra (például 70/30). A **Learner** node betanítja a modellt a tanító adaton. A **Predictor** node alkalmazza a modellt a teszt adatra. A **Scorer** node kiértékeli a teljesítményt (accuracy, precision, recall, F1-score, RMSE — a feladattól függően).

Ez az, amit a prediktív analitika könyvek több száz oldalon tárgyalnak — és a KNIME-ban az egészet összekötögeted 6-8 node-ból.

### Metanode-ok és Komponensek

Ahogy a munkafolyamataid bonyolultabbá válnak, a KNIME lehetővé teszi, hogy node-csoportokat **metanode-okba** vagy **komponensekbe** csomagolj. Ezek újrahasználható "szub-workflow-k" — mintha egy saját node-ot készítenél, amely belül több lépésből áll.

Például készíthetsz egy "Adattisztítás" komponenst, amelyet minden projekted elején beillesztesz, és amely magában foglalja a hiányzó értékek kezelését, a kiugró értékek szűrését és a normalizálást.

### KNIME Hub: közösségi munkafolyamatok

A KNIME Hub (hub.knime.com) egy online tárház, ahol felhasználók megosztják a munkafolyamataikat. Ha egy adott elemzési feladathoz keresel kiindulópontot — legyen az szövegbányászat, képelemzés, vagy idősor-előrejelzés — jó eséllyel találsz egy kész workflow-t, amelyet letöltesz, adaptálsz, és futtatod.

### R és Python integrálása

A KNIME nem zár be a vizuális világba. Ha van egy lépés, amelyhez mégis kódra van szükség — mondjuk egy speciális R-csomag vagy egy Python-könyvtár —, használhatsz **R Snippet** vagy **Python Script** node-okat. Ezek beilleszthetők a vizuális workflow-ba, és a bemenetük/kimenetük ugyanúgy összeköthető a többi node-dal. A legjobb két világ: vizuális keretrendszer, kódbetétekkel ahol szükséges.

---

## LangFlow — Vizuális LLM pipeline-tervező

### Mi a LangFlow?

Ha az n8n az általános célú munkafolyamat-automatizálás eszköze, és a KNIME az adatelemzésé, akkor a **LangFlow** kifejezetten a nagy nyelvi modellekre (LLM) épülő alkalmazások vizuális tervezőeszköze. A LangFlow a LangChain keretrendszer vizuális felülete — lehetővé teszi, hogy LLM-pipeline-okat építs drag-and-drop módszerrel.

### Miért érdekes ez tudósoknak?

A 9. fejezetben részletesen megismered a RAG (Retrieval-Augmented Generation) architektúrát. A LangFlow előnye az, hogy ezt az architektúrát — amely kódban több tucat sornyi Python — **vizuálisan** építheted fel:

- Válaszd ki az LLM-et (OpenAI, Anthropic, Ollama, stb.)
- Válaszd ki a beágyazási modellt (embedding model)
- Válaszd ki a vektortárat (Chroma, Pinecone, FAISS)
- Kösd össze a komponenseket
- Teszteld a beépített chat-felületen

### Példa: RAG chatbot építése drag-and-drop módszerrel

Képzeld el, hogy a kutatócsoportodnak van 50 publikációja az elmúlt 5 évből, és szeretnél egy chatbotot, amely ezekre a cikkekre alapozva válaszol kérdésekre.

**A LangFlow workflow:**

```
[Document Loader]          ← Betölti a PDF-eket
       ↓
[Text Splitter]            ← Felosztja kisebb darabokra (chunk-okra)
       ↓
[Embedding Model]          ← Beágyazási vektorokat generál
       ↓
[Vector Store]             ← Eltárolja a vektorokat
       ↓
[Retriever]                ← Keresési motor a vektortáron
       ↓
[LLM + Prompt Template]   ← Az LLM a megtalált szövegrészletek alapján válaszol
       ↓
[Chat Interface]           ← A felhasználó kérdez, a rendszer válaszol
```

A lényeg: ezt az egész pipeline-t vizuálisan építed, dobozokat húzogatva és összekötve. Nem kell tudnod, hogyan működik a LangChain Python API-ja belül. A LangFlow elvégzi a "fordítást".

### Prototípus-készítés kódolás előtt

A LangFlow különösen hasznos **prototípus-készítésre**. Ha nem vagy biztos benne, melyik LLM, melyik embedding modell, vagy melyik chunk-méret működik legjobban a te adataiddal, a LangFlow-ban percek alatt kipróbálhatsz különböző kombinációkat — anélkül, hogy minden alkalommal átírnád a kódot.

Ha aztán a prototípus működik, és production-ready megoldásra van szükséged, exportálhatod a konfigurációt és Python-kódként implementálhatod. De sok esetben a LangFlow felülete maga is elegendő a napi használathoz.

### A RAG architektúra részleteiről

Ne feledd: a RAG-ról, a beágyazásokról és a vektortárakról a 9. fejezet szól részletesen. Itt most azt az üzenetet vidd magaddal, hogy ezek a komplex rendszerek is építhetők vizuálisan — nem kell azonnal a mély kódba ugrania annak, aki először találkozik velük.

---

## Node-RED — IoT és szenzor-adatok munkafolyamatai

A **Node-RED** az IBM által fejlesztett, nyílt forráskódú vizuális programozási eszköz, amelyet eredetileg az IoT (Internet of Things) világára terveztek. Ha a kutatásod szenzorokkal, mérőműszerekkel, adatgyűjtő rendszerekkel dolgozik, a Node-RED a te eszközöd.

### Miért releváns tudósoknak?

- **Szenzor-adatgyűjtés automatizálása:** Hőmérséklet-szenzorok, légnyomásmérők, vízmintázók adatainak valós idejű feldolgozása
- **MQTT-protokoll támogatás:** Az IoT-világban elterjedt kommunikációs protokoll natív kezelése
- **Dashboard-készítés:** Valós idejű adatmegjelenítés webes felületen, kód nélkül
- **Riasztási rendszerek:** Ha egy szenzorérték túllép egy küszöböt, azonnali értesítés (e-mail, SMS, Slack)

### Egy tipikus Node-RED workflow kutatási kontextusban

```
[MQTT In]               ← Szenzor adatot küld
       ↓
[Function]              ← Kalibrációs számítás
       ↓
[Switch]                ← Értékelés: normál / figyelmeztetés / riasztás
       ↓          ↓           ↓
[Dashboard]   [Database]  [Email Alert]
```

A Node-RED erőssége a **valós idejű adatáramlás** — nem ütemezett futtatásokról van szó (mint az n8n-nél), hanem folyamatos adatfeldolgozásról. Ha a Debreceni Egyetem meteorológiai állomásáról percenként érkeznek adatok, a Node-RED folyamatosan dolgozza fel őket, tárolja az adatbázisban, és riaszt, ha valami rendelleneset észlel.

---

## Orange — Gépi tanulás nem-programozóknak

Az **Orange** (orange.biolab.si) egy nyílt forráskódú, egyetemi fejlesztésű vizuális adatelemzési és gépi tanulási eszköz, amelyet a Ljubljanai Egyetem Bioinformatikai Laboratóriuma fejleszt és tart karban.

### Miért érdemes ismerni?

- **Kifejezetten oktatási célra tervezett:** Az Orange felülete a lehető legegyszerűbb — ideális, ha először találkozol gépi tanulási fogalmakkal
- **Interaktív vizualizációk:** Minden elemzési lépésnél azonnal megjelenik az eredmény vizuális formában — scatter plot, heatmap, dendrogram
- **Beépített widgetek:** Az Orange-ban a node-okat "widgeteknek" hívják, és előre beépített elemzési widgetek százai állnak rendelkezésre
- **Bioinformatikai és szövegbányászati kiegészítők:** Speciális modul génexpressziós adatokhoz, szövegbányászathoz és képelemzéshez
- **Gyors tanulási görbe:** Egy hallgató az első órán már működő klaszterezést épít

### Miben különbözik a KNIME-tól?

Az Orange kisebb, könnyebb és fókuszáltabb. Ha a KNIME egy teljes értékű adatelemzési műhely, az Orange egy jól felszerelt tanterem. Kutatási felhasználásra mindkettő alkalmas, de a KNIME több ipari integrációt és nagyobb léptékű feldolgozást kínál. Az Orange-t akkor válaszd, ha gyorsan akarsz felfedező elemzést végezni (exploratory data analysis), vagy ha hallgatókat tanítasz.

---

## Döntési útmutató: vizuális vagy kódalapú megközelítés?

Most, hogy ismered a főbb vizuális eszközöket, jogosan merül fel a kérdés: mikor használj vizuális eszközt, és mikor hagyományos kódolást?

### Válaszd a vizuális megközelítést, ha...

- **A feladat standard és jól definiált.** Adatbetöltés, tisztítás, alapvető statisztika, klaszterezés, osztályozás, regresszió — ezekre a KNIME vagy Orange tökéletes.
- **Szolgáltatásokat kötsz össze.** API → feldolgozás → értesítés típusú munkafolyamatokra az n8n ideális.
- **Gyors prototípusra van szükség.** LLM pipeline-okat percek alatt építhetsz a LangFlow-ban.
- **Nem-programozó kollégákkal dolgozol.** A vizuális workflow közös nyelv — mindenki megérti.
- **Reprodukálhatóság és átláthatóság fontos.** A workflow maga a dokumentáció.
- **IoT/szenzor-adatokkal dolgozol valós időben.** Node-RED.

### Válaszd a kódalapú megközelítést, ha...

- **Egyedi algoritmust implementálsz.** Saját statisztikai módszer, speciális szimulációs logika.
- **Nagy teljesítményű számításra van szükség.** HPC-klaszteren futó párhuzamosított kód.
- **Nagyon specifikus könyvtárat kell használnod.** Például egy ritka bioinformatikai Python-csomag, amelynek nincs vizuális node-ja.
- **A munkafolyamat rendkívül összetett és dinamikus.** 100+ elágazás, bonyolult ciklusok, rekurzív logika.
- **Verziókezelésre van szükség minden részletben.** A kód git-ben verziózható; a vizuális workflow-fájlok kevésbé könnyen diff-elhetők.

### A valóság: a legtöbb kutató mindkettőt használja

A legjobb megközelítés ritkán "csak vizuális" vagy "csak kód". A gyakorlatban a két világ kombinációja a leghatékonyabb:

- A KNIME-ban megépíted az adatfeldolgozási pipeline-t, de egy lépésben Python Snippet node-ot használsz egy speciális számításhoz
- Az n8n-ben automatizálod a rendszeres feladatokat, de egy HTTP Request node-dal egy saját Python-szerveredre küldesz adatot
- A LangFlow-ban prototípust építesz, majd a végleges verziót Python-kódként implementálod

> **🗺️ Szakterületi példa: Plan-and-Execute architektúra GIS-feladatokhoz**
>
> Az Autonomous GIS Plan-and-Execute architektúrája először megjeleníti a teljes munkafolyamat-tervet — az adatletöltéstől az erdőborítottság-változási térkép generálásáig —, és a felhasználó jóváhagyása után automatikusan végrehajtja a hat lépést. Amikor a felhasználó azt kéri: „Készíts térképet a Dunántúl erdőborítottságának változásáról 2018–2024 között", az ágens egy hatlépéses tervet készít (megyepoligonok → WorldCover letöltés → erdő-maszk → zonális statisztika → változási térkép → összefoglaló), amelyet vizuálisan is megjelenít. Ez a vizuális tervező és kódalapú végrehajtás ötvözete a gyakorlatban.
>
> *Forrás: gis ch22, 21.3.2 „A Plan-and-Execute architektúra"*

---

## Vizuális és kódalapú eszközök kombinálása

### A "legjobb két világ" stratégia

A leghatékonyabb kutatók nem választanak az eszközök között — kombinálják őket. Íme néhány bevált minta:

**1. Vizuális tervezés → Kód implementáció**

Használd a LangFlow-t vagy az n8n-t a gondolkodás fázisában: "Milyen lépésekből áll a pipeline-om? Milyen sorrendben? Hol vannak az elágazások?" Ha a vizuális prototípus működik, és production-szintű megoldásra van szükséged, implementáld Python-ban.

**2. Kódalapú elemzés → Vizuális automatizálás**

Írd meg a speciális elemzési szkriptedet Python-ban (vagy R-ben), csomagold be egy API-vá (például FastAPI-val), és hívd meg n8n-ből. Így az elemzési logika rugalmas marad, de az automatizálás (ütemezés, értesítés, adattovábbítás) vizuális.

**3. Vizuális adattisztítás → Kód modellezés → Vizuális deployment**

A KNIME-ban tisztítsd és készítsd elő az adatokat (ez a munka 80%-a!). Exportáld CSV-be. Futtasd le az egyedi modellezési kódodat. Az eredményeket töltsd vissza a KNIME-ba vizualizációhoz és riportoláshoz.

**4. n8n mint "ragasztóanyag"**

Az n8n kiválóan alkalmas arra, hogy összekösse a különböző eszközeidet:
- Schedule Trigger → letölti a legújabb adatokat
- HTTP Request → elküldi a Python-szkriptednek feldolgozásra
- Set node → formázza az eredményt
- Gmail node → elküldi a kutatócsoportnak

### Debreceni példa: multidiszciplináris kutatás

Képzelj el egy kutatási projektet, amely a Hortobágy mikroklímáját vizsgálja madárpopulációs adatokkal összevetve:

1. **Node-RED** gyűjti a terepi szenzorok adatait (hőmérséklet, páratartalom, szélsebesség) MQTT-n keresztül, és tárolja adatbázisban
2. **n8n** naponta reggel lefuttatja az adatletöltést, összefésüli a szenzor-adatokat a madármegfigyelésekkel, és elindítja az elemzést
3. **KNIME** elvégzi az adattisztítást, a korrelációs elemzést és a klaszterezést
4. Egy **Python-szkript** (KNIME Python Snippet node-ból hívva) lefuttatja az egyedi statisztikai tesztet, amelyet a csapat fejlesztett
5. Az eredményeket **n8n** küldi el a csapatnak Slack-en, és archiválja Google Drive-on
6. Ha valami anomáliát észlel az automatikus elemzés, **n8n** e-mailt küld a projekt-vezetőnek

Egyetlen eszköz sem tudja mindezt egyedül. De együtt, vizuálisan összekapcsolva, egy erőteljes és teljesen automatizált kutatási infrastruktúrát alkotnak.

---

## Összefoglaló: az eszközök áttekintése

| Eszköz | Fő felhasználás | Erősség | Típikus felhasználó |
|--------|-----------------|---------|---------------------|
| **n8n** | Munkafolyamat-automatizálás | 400+ integráció, AI-node-ok, self-hosted | Bármilyen kutató, aki rendszeres feladatokat automatizálna |
| **KNIME** | Adatelemzés, prediktív analitika | Teljes ML-pipeline vizuálisan, ingyenes | Adatelemzéssel foglalkozó kutató, "citizen data scientist" |
| **LangFlow** | LLM pipeline-ok építése | RAG, chatbot, LLM-alkalmazások drag-and-drop-pal | Kutató, aki AI-alkalmazást épít szövegalapú adatokra |
| **Node-RED** | IoT, szenzor-adatok | Valós idejű adatáramlás, MQTT, dashboard | Terepi kutató, laborkísérlet-automatizálás |
| **Orange** | Felfedező adatelemzés, oktatás | Egyszerű felület, interaktív vizualizáció | Hallgatók, először gépi tanulással ismerkedők |

---

## Amit ebből a fejezetből vigyél magaddal

1. **A vizuális programozás nem "könnyített programozás"** — ez egy önálló, erőteljes paradigma, amely sok kutatási feladatra jobban illeszkedik, mint a hagyományos kódolás.

2. **Nem kell választanod** a vizuális és kódalapú megközelítés között. A kettő kiegészíti egymást.

3. **Kezdd az n8n-nel**, ha automatizálni szeretnéd a rendszeres feladataidat (adatletöltés, értesítések, AI-feldolgozás). Kezdd a **KNIME-mal**, ha adatelemzést végzel. Kezdd a **LangFlow-val**, ha LLM-alapú alkalmazást építesz.

4. **A vizuális workflow maga a dokumentáció** — ez a reprodukálható tudomány egyik legjobb barátja.

5. **A 12. fejezetben** visszatérünk az n8n-hez, és részletesen megépítjük vele az első AI-ágensedet. Most az alapokat fektetted le.

Katalin, az ökológus — akiről a fejezet elején olvastál — ma már a KNIME-ban elemzi a terepi adatait, az n8n automatikusan figyeli a PubMed-et, és a LangFlow-ban épített chatbot válaszol a hallgatói kérdéseire a kutatócsoportja publikációi alapján. Mindezt anélkül, hogy megtanult volna programozni.

A munkafolyamataid nem a fejedben kell, hogy maradjanak. Rajzold meg őket — és hadd fussanak.
