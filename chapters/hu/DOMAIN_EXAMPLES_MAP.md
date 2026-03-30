# Szakterületi példák térképe (Domain Examples Map)

> Három magyar tankönyv AI-releváns fejezeteinek leképezése az AI-könyv 16 fejezetére.
> Minden bejegyzés tartalmazza a forrást, a pontos hivatkozást, a javasolt „Szakterületi példa" doboz tartalmát és a szakterületet.

**Források rövidítése:**
- **precagri** = *Precíziós mezőgazdaság* tankönyv (`c:/precagri/chapters_hu/`)
- **hidrogis** = *Hidrológiai térinformatika (Maidment)* tankönyv (`c:/maidment_hidroGIS/chapters_hu/`)
- **gis** = *Geoinformatika 2025* tankönyv (`c:/gis-konyv2025/chapters_v3/`)

---

## 1. fejezet — Az AI forradalom a tudományos kutatásban

### 1.1 Példa: Az adatforradalom a mezőgazdaságban
- **Forrás:** precagri ch03, 3.1 „A megérzéstől az adatvezérelt döntésekig"
- **Hivatkozás:** 3.1.1–3.1.3 — A gazda marék földdel ítéli meg a nedvességet vs. IoT-szenzor-hálózat; a hozammonitorok hektáronként több ezer adatpontot rögzítenek; 9,7 milliárd ember élelmezése 2050-re.
- **Szakterületi példa doboz:** „A precíziós mezőgazdaságban az AI-forradalom azt jelenti, hogy a gazdálkodó megérzését ma már érzékelők, műholdak és gépi tanulási algoritmusok egészítik ki — a hozammérő kombájntól a felhőalapú döntéstámogatásig egyetlen tenyészidőszak alatt terabájtnyi adat keletkezik."
- **Szakterület:** precagri

### 1.2 Példa: Az LSTM mint a hidrológus asszisztense
- **Forrás:** hidrogis ch23, 23.1 „Árvíz-előrejelzés LSTM-hálózatokkal"
- **Hivatkozás:** 23.1.1 — Az LSTM-hálózatok képesek megtanulni az összefüggést csapadék és vízhozam között anélkül, hogy közölnénk velük a fizikát; a gépi tanulás „2026-ban már nem kutatási kuriózum, hanem operatív valóság az árvíz-előrejelzési központokban."
- **Szakterületi példa doboz:** „A hidrológiában az AI már nem akadémiai kuriózum: az árvíz-előrejelzési központok LSTM-hálózatokat alkalmaznak a Tisza vízhozamának napi előrejelzésére, NSE > 0,87 tesztidőszaki pontossággal — anélkül, hogy a modellnek explicit fizikai egyenleteket adnánk meg."
- **Szakterület:** hidrogis

### 1.3 Példa: Az Autonomous GIS paradigmaváltása
- **Forrás:** gis ch22, 21.1 „Miért nehéz a térbeli gondolkodás a nagy nyelvi modellek számára?"
- **Hivatkozás:** A fejezet bevezető bekezdése — „A felhasználó nem azt mondja, hogy 'nyisd meg ezt a réteget, alkalmazz egy 500 méteres puffert', hanem azt, hogy 'melyik települések vannak 500 méteren belül az árvízveszélyes területektől?' és a rendszer maga bontja le a feladatot."
- **Szakterületi példa doboz:** „A geoinformatikában a paradigmaváltás azt jelenti, hogy a GIS-felhasználó természetes nyelven fogalmazza meg a kérdését, és egy AI-ágens önállóan bontja le azt térinformatikai műveletek sorozatára — az eszközhasználó mérnökből döntéshozóvá válik."
- **Szakterület:** gis

---

## 2. fejezet — Társalgási AI: Az első kutatási partnered

### 2.1 Példa: LLM-alapú mezőgazdasági szaktanácsadás
- **Forrás:** precagri ch15, 15.7 „Természetes nyelvi feldolgozás és nagy nyelvi modellek a mezőgazdaságban"
- **Hivatkozás:** 15.7.1 — MI-alapú csevegőrobotok a szaktanácsadásban: „Egy vidéki indiai gazdálkodó szöveges üzenetben írhatja le a paradicsomnövényein észlelt tüneteket, és azonnal diagnózist és kezelési javaslatot kaphat." A fejlődő országokban egyetlen tanácsadóra több ezer háztartás jut.
- **Szakterületi példa doboz:** „A precíziós mezőgazdaságban az LLM-alapú csevegőrobotok áthidalhatják a szaktanácsadói hiányt: a gazdálkodó anyanyelvén kérdez, és valós idejű, helyi viszonyokra szabott növényvédelmi és trágyázási javaslatokat kap — akár SMS-en keresztül, okostelefon nélkül."
- **Szakterület:** precagri

### 2.2 Példa: Természetes nyelvű GIS-lekérdezések
- **Forrás:** gis ch22, 21.9 „Természetes nyelvű GIS-lekérdezések: részletes példák"
- **Hivatkozás:** 21.9.1–21.9.3 — Egyszerű lekérdezéstől („mely települések vannak 500 m-en belül?") az összetett tér-idő elemzésig, a felhasználó természetes nyelven kommunikál a GIS-sel.
- **Szakterületi példa doboz:** „Az Autonomous GIS-ben a térinformatikus nem SQL-t vagy Python-kódot ír, hanem természetes nyelven kérdez: 'Melyik Natura 2000 területen nőtt a beépítettség 2020 óta?' — és a rendszer maga generálja a lekérdezést, futtatja az elemzést, és megjeleníti az eredményt térképen."
- **Szakterület:** gis

---

## 3. fejezet — AI a tudományos írásban és kommunikációban

### 3.1 Példa: Tudáskinyerés a mezőgazdasági szakirodalomból
- **Forrás:** precagri ch15, 15.7.2 „Tudáskinyerés és döntéstámogatás"
- **Hivatkozás:** „Évente több ezer tudományos cikk jelenik meg a növénytermesztésről [...] MI-rendszerek automatikusan átvizsgálhatják ezt az irodalmat, kinyerhetik a legfontosabb eredményeket (pl. 'a cink 0,5%-os lombtrágyaként történő kijuttatása 12%-kal növelte a búzahozamot meszes talajokon'), és kereshető tudásbázisokba rendezhetik azokat."
- **Szakterületi példa doboz:** „A mezőgazdasági kutatásban az NLP-rendszerek képesek több ezer cikkből strukturált tudást kinyerni — például a konkrét tápanyag-dózis és hozamválasz összefüggéseket — és kereshető tudásbázisba rendezni, amely a döntéstámogató rendszerek és a kutatói irodalomfeldolgozás alapja."
- **Szakterület:** precagri

---

## 4. fejezet — AI-vel végzett adatelemzés kódolás nélkül

### 4.1 Példa: Hozamtérkép-adatok tisztítása és feltáró elemzése
- **Forrás:** precagri ch14, 14.4 „Adattisztítás és minőség-ellenőrzés"
- **Hivatkozás:** A hozamtérképek adattisztítási lépései: lehetetlen értékek eltávolítása, menetek elején/végén rögzített pontok kiszűrése, 2–3 szóráson túli lokális kiugró értékek szűrése, térbeli szűrők. Nyers hozamadatokból negatív hozamok, GPS-eltolódás, szemnedvesség-torzítás kiszűrése szükséges.
- **Szakterületi példa doboz:** „A precíziós mezőgazdaságban a nyers hozamtérképek mindig tartalmazzák a kombájn felfutási hibáit, a GPS-eltolódásokat és a menetek átfedéséből adódó dupla számolásokat — az AI-asszisztens lépésről lépésre végigvezetheti a kutatót a négy-öt lépéses szűrési folyamaton, kód nélkül."
- **Szakterület:** precagri

### 4.2 Példa: Kezelési zónák lehatárolása térbeli klaszterezéssel
- **Forrás:** precagri ch14, 14.5 „Térbeli adatintegráció és térinformatikai munkafolyamatok"
- **Hivatkozás:** A tipikus munkafolyamat: táblahatár → adatrétegek importálása (hozamtérképek, EC-felmérés, domborzat, NDVI) → közös rácsfelbontásra interpolálás → klaszterező algoritmussal kezelési zónák lehatárolása → előíró térkép generálása VRT-hez.
- **Szakterületi példa doboz:** „Egy mezőgazdasági szaktanácsadó öt adatréteget — hozamtérkép, talaj-EC, domborzat, NDVI és talajminta — felviszünk egy GIS-be, és a térbeli klaszterelemzés 3–5 kezelési zónát tár fel, amelyek alapján a változó dózisú műtrágya-kijuttatás megtervezhető. Az AI-asszisztens természetes nyelvű párbeszéddel végigkíséri az elemzést."
- **Szakterület:** precagri

### 4.3 Példa: Hidrológiai adatvizsgálat és józansági ellenőrzés
- **Forrás:** hidrogis ch24, 24.4.2 „1. lépés: Az ágens beolvassa és megvizsgálja az adatokat"
- **Hivatkozás:** Az ágens betölti a Zala folyó adatait, diagnosztikus statisztikákat számol (lefolyási tényező 0,23; fajlagos vízhozam 164 mm/év), összeveti regionális normális értékekkel, és ellenőrzi a hiányosságokat — 12 hiányzó nap lineáris interpolációval pótolva.
- **Szakterületi példa doboz:** „Egy hidrológiai ágens a Zala folyó 11 évnyi adatát betöltve automatikusan kiszámítja a lefolyási tényezőt (0,23), a fajlagos vízhozamot (164 mm/év), azonosítja a 12 hiányzó napot, és összeveti az értékeket a közép-európai normálértékekkel — mindez kód nélkül, természetes nyelvi párbeszédben."
- **Szakterület:** hidrogis

---

## 5. fejezet — AI kódolási asszisztensek

### 5.1 Példa: Vízgyűjtő-lehatárolási szkript automatizálása
- **Forrás:** hidrogis ch12, 12.7 „Vízgyűjtő-lehatárolási szkript felépítése lépésről lépésre"
- **Hivatkozás:** 12.7.1–12.7.3 — Teljes ArcPy-szkript a DEM feltöltésétől a vízgyűjtő-lehatárolásig, 2149 texasi HUC-10 vízgyűjtőre vagy a Duna 23 866 részvízgyűjtőjére skálázva. „Húsz perc szorozva kétezer ismétléssel majdnem egy hónapnyi munkát tesz ki."
- **Szakterületi példa doboz:** „A hidrológiai térinformatikában a vízgyűjtő-lehatárolás 6–8 egymásra épülő GIS-lépésből áll — az AI-kódolási asszisztens egyetlen promptból generálja a teljes ArcPy- vagy PyQGIS-szkriptet, amely akár 23 866 részvízgyűjtőt is feldolgoz egyetlen éjszaka alatt."
- **Szakterület:** hidrogis

### 5.2 Példa: NDVI-számítás és vegetációs index kódgenerálás
- **Forrás:** gis ch22, 21.4.2 „Kódgenerálás: rugalmasság és kockázat"
- **Hivatkozás:** A GeoPandas-, rasterio- és GEE-munkafolyamatok tipikus mintái; az LLM-ek generálta kód: „NDVI = (NIR - Red) / (NIR + Red)"; sandbox végrehajtás, iteratív javítás 2–3 lépésben.
- **Szakterületi példa doboz:** „A geoinformatikában az AI-kódolási asszisztens teljes rasterio-szkriptet generál: Sentinel-2 felvétel betöltése, NDVI-számítás, maszkolt zonális statisztika, eredmény mentése — és ha a kód hibás, a hibaüzenet alapján 2–3 iterációban javítja."
- **Szakterület:** gis

---

## 6. fejezet — AI-támogatott matematikai modellezés és szimuláció

### 6.1 Példa: GR4J csapadék-lefolyás modell és Oudin PET-képlet
- **Forrás:** hidrogis ch24, 24.4.1 „A feladat beállítása" és 24.11.2 „Az ágenses kalibrálás végigvezetése"
- **Hivatkozás:** A GR4J 4 paramétere ($x_1$: termelési tározó kapacitás, $x_2$: talajvízcsere, $x_3$: útvonalválasztási tározó, $x_4$: egységhidrográf időbázis); az Oudin PET-képlet: $PE = \frac{R_a}{\lambda \rho} \cdot \frac{T_a + 5}{100}$.
- **Szakterületi példa doboz:** „A hidrológiai modellezésben a GR4J modell négy paraméterrel írja le a csapadék lefolyássá alakulását — az AI-asszisztens képes a képleteket implementálni, a paraméterek fizikai jelentését magyarázni, és a kezdeti értékeket a vízgyűjtő jellemzőiből kiindulva becsülni."
- **Szakterület:** hidrogis

### 6.2 Példa: Növénynövekedési modellek mint DSS-eszközök
- **Forrás:** precagri ch16, 16.3 „Növénynövekedési modellek mint döntéstámogató eszközök"
- **Hivatkozás:** A folyamat-alapú növénynövekedési modellek (DSSAT CERES, APSIM) matematikai egyenletekkel írják le a növény fiziológiai válaszát a környezetre; az MI-modellek kiegészíthetik, ahol a fizikai modell nem adekvát.
- **Szakterületi példa doboz:** „A mezőgazdasági döntéstámogatásban a folyamat-alapú növénynövekedési modellek (DSSAT, APSIM) matematikai egyenletekkel szimulálják a növény fejlődését — az AI-asszisztens segíthet a modell felállításában, paraméterezésében és az eredmények értelmezésében."
- **Szakterület:** precagri

### 6.3 Példa: LSTM LSTM-cella matematikája
- **Forrás:** hidrogis ch23, 23.1.1 „Miért alkalmasak a rekurrens hálózatok a vízhozam-előrejelzésre?"
- **Hivatkozás:** Az LSTM-cella kapu-egyenletei: $f_t = \sigma(W_f \cdot [h_{t-1}, x_t] + b_f)$; $C_t = f_t \odot C_{t-1} + i_t \odot \tilde{C}_t$; és az NSE veszteségfüggvény: $\mathcal{L}_{\text{NSE}} = 1 - \frac{\sum_t (Q_{\text{obs},t} - Q_{\text{pred},t})^2}{\sum_t (Q_{\text{obs},t} - \overline{Q}_{\text{obs}})^2}$.
- **Szakterületi példa doboz:** „Az árvíz-előrejelzésben az LSTM-hálózat kapu-mechanizmusa (felejtő-, bemeneti és kimeneti kapu) lehetővé teszi, hogy a hálózat a gyors felszíni lefolyást és a lassú alapvízhozam-komponenst egyszerre tanulja meg — az NSE-veszteségfüggvény az árvízi csúcsokra fókuszálja a tanítást."
- **Szakterület:** hidrogis

---

## 7. fejezet — Adat-pipeline-ok és automatizálás

### 7.1 Példa: Mezőgazdasági adatfolyam az érzékelőtől a döntésig
- **Forrás:** precagri ch14, 14.1 „Az adatok életciklusa a precíziós mezőgazdaságban"
- **Hivatkozás:** A teljes életciklus: gyűjtés → átvitel → tárolás → tisztítás → elemzés → döntés → visszacsatolás. „Egyetlen vetési művelet egyidejű adatfolyamokat generálhat a vetési tőszámról, a maglehelyezés egyenletességéről, a soregységek talajnyomásáról, a sebességről, az üzemanyag-fogyasztásról — másodperc alatti időközönként."
- **Szakterületi példa doboz:** „A precíziós mezőgazdaságban egyetlen vetőgép menet közben tucatnyi adatfolyamot generál (vetőmag-sűrűség, talajnyomás, sebesség, GPS-pozíció) — a pipeline az érzékelőktől a felhőplatformon keresztül a változó dózisú kijuttatási térképig automatizált, és az adattisztítás a teljes minőség kulcsa."
- **Szakterület:** precagri

### 7.2 Példa: ISOBUS és ADAPT — formátumok átalakítása
- **Forrás:** precagri ch14, 14.2 „Adatgyűjtés: formátumok, protokollok és szabványok" és 14.8 „Nyílt adatok és interoperabilitási szabványok"
- **Hivatkozás:** Az ISOBUS (ISO 11783) a gépek közötti kommunikáció szabványa; az ADAPT nyílt forráskódú keretrendszer a különböző gyártók adatformátumainak konvertálásához — köztes fordítóréteg shapefile, GeoTIFF, CSV, LAS és tulajdonosi formátumok között.
- **Szakterületi példa doboz:** „Az agráradatok interoperabilitását az ADAPT keretrendszer biztosítja: köztes fordítórétegként bármely gépgyártó (John Deere, Case IH, AGCO) tulajdonosi adatformátumát képes olvasni — az AI-pipeline ezt a konverziót automatizálhatja."
- **Szakterület:** precagri

### 7.3 Példa: Kötegelt vízgyűjtő-feldolgozás Pythonnal
- **Forrás:** hidrogis ch12, 12.13 „Gyakorlati minták kötegelt feldolgozáshoz"
- **Hivatkozás:** 12.13.1 „Ciklus a bemeneti fájlokon" — for ciklus a bemeneti DEM-fájlokon, eredmények naplózása CSV-be; 12.13.3 „A HUC magyar megfelelőinek feldolgozása" — az összes magyar részvízgyűjtő automatizált feldolgozása.
- **Szakterületi példa doboz:** „A hidrológiai térinformatikában egy Python-pipeline ciklusban dolgozza fel az ország összes részvízgyűjtőjét: DEM feltöltés, folyásirány, vízgyűjtő-lehatárolás — eredménynaplózással és hibakezeléssel, egy éjszaka alatt."
- **Szakterület:** hidrogis

---

## 8. fejezet — Vizuális programozás és munkafolyamat-tervezés

### 8.1 Példa: ModelBuilder → Python export a hidrológiában
- **Forrás:** hidrogis ch12, 12.11 „A ModelBuilder mint híd a szkripteléshez"
- **Hivatkozás:** 12.11.1–12.11.2 — ModelBuilder-ben felépített vízgyűjtő-lehatárolási munkafolyamat exportálása Python-szkriptbe; 12.11.3 — QGIS grafikus modellező mint nyílt forráskódú alternatíva.
- **Szakterületi példa doboz:** „A hidrológiai térinformatikában a ModelBuilder vagy a QGIS grafikus modellező 'vizuális programozást' kínál: a kutató dobozokból és nyilakból építi fel a DEM → folyásirány → vízgyűjtő munkafolyamatot, majd egyetlen kattintással Python-szkriptre exportálja."
- **Szakterület:** hidrogis

### 8.2 Példa: Plan-and-Execute architektúra GIS-feladatokhoz
- **Forrás:** gis ch22, 21.3.2 „A Plan-and-Execute architektúra"
- **Hivatkozás:** A felhasználó kéri: „Készíts térképet a Dunántúl erdőborítottságának változásáról 2018–2024 között." Az ágens 6 lépéses tervet készít (megyepoligonok → WorldCover letöltés → erdő-maszk → zonális stat → változási térkép → összefoglaló), a felhasználó jóváhagyja, majd az ágens végrehajtja.
- **Szakterületi példa doboz:** „Az Autonomous GIS Plan-and-Execute architektúrája először megjeleníti a teljes munkafolyamat-tervet — az adatletöltéstől az erdőborítottság-változási térkép generálásáig —, és a felhasználó jóváhagyása után automatikusan végrehajtja a hat lépést."
- **Szakterület:** gis

---

## 9. fejezet — RAG: Tanítsuk meg az AI-t a saját adatainkra

### 9.1 Példa: Térbeli RAG környezeti hatásvizsgálathoz
- **Forrás:** gis ch22, 21.6 „Térbeli RAG: vektor és gráf visszakeresés szakterületi GIS tudáshoz"
- **Hivatkozás:** 21.6.1–21.6.2 — A RAG koncepció térbeli kiterjesztése; egy környezeti hatásvizsgálati példa, ahol a RAG-rendszer a felhasználó kérdéséhez releváns térbeli dokumentumokat, szabályozásokat és korábbi elemzéseket keres elő vektor- és gráf-alapú visszakereséssel.
- **Szakterületi példa doboz:** „A geoinformatikában a térbeli RAG a felhasználó kérdéséhez nemcsak szöveges dokumentumokat, hanem releváns téradatokat, korábbi elemzési eredményeket és szabályozási szövegeket is visszakeres — például egy környezeti hatásvizsgálathoz az adott területre vonatkozó Natura 2000 szabályokat és korábbi monitoring eredményeket."
- **Szakterület:** gis

### 9.2 Példa: LLM-ek és a mezőgazdasági szakterminológia
- **Forrás:** precagri ch15, 15.7.3 „Kihívások és korlátok"
- **Hivatkozás:** „A mezőgazdasági nyelv rendkívül specializált, olyan szakterminológiával és helyi növénynevekkel, amelyek nem feltétlenül szerepelnek megfelelően az általános célú nyelvi modellek betanítási adataiban." Többnyelvű támogatás szükségessége, pontossági kockázatok.
- **Szakterületi példa doboz:** „A mezőgazdasági RAG-rendszereknél a legnagyobb kihívás, hogy az általános célú LLM-ek nem ismerik a helyi szakterminológiát (pl. belvíz, szikes talaj, őszi búza fajtanevek) — a RAG a helyi agrártudásbázissal egészíti ki a modellt."
- **Szakterület:** precagri

---

## 10. fejezet — Digitális ikrek: Valós rendszerek virtuális másolatai

### 10.1 Példa: Budapest hősziget-szimuláció 3D digitális ikerrel
- **Forrás:** gis ch19, 18.6.2 „Klímaadaptáció a városi digitális ikerrel: Budapest hősziget-szimuláció"
- **Hivatkozás:** 3D épületmodell (LoD2), ENVI-met mikroklíma-szimulációs motor; Budapest belső kerületeiben (V.–VIII.) a nyári éjszakai hőmérséklet 4–8 °C-kal magasabb; szimulációs forgatókönyvek: „Mi történik, ha a Blaha Lujza tér parkolóját zöldfelületre cseréljük? Ha a Nagykörút mentén fasorokat ültetünk?"
- **Szakterületi példa doboz:** „Budapest digitális ikreben a 3D épületmodell és az ENVI-met mikroklíma-motor segítségével szimulálható, hogy egy új fasor a Nagykörúton hány fokkal csökkentené a nyári hőmérsékletet — a döntéshozó a beavatkozást a megvalósítás előtt virtuálisan teszteli."
- **Szakterület:** gis

### 10.2 Példa: A digitális iker érettségi szintjei
- **Forrás:** gis ch19, 18.5.1 „A digitális iker érettségi modellje"
- **Hivatkozás:** Négy szint: Level 1 (statikus replika — CityGML modell), Level 2 (szinkronizált iker — valós idejű szenzor), Level 3 (prediktív iker — szimulációs forgatókönyv), Level 4 (autonóm iker — zárt visszacsatolási hurok, pl. zsilipvezérlés árvízi modell alapján).
- **Szakterületi példa doboz:** „A digitális ikrek négy érettségi szintje a statikus 3D modelltől az autonóm visszacsatolásig terjed — a legmagasabb szinten a rendszer az árvízi előrejelzés alapján automatikusan vezérli a zsilipet, emberi beavatkozás nélkül."
- **Szakterület:** gis

### 10.3 Példa: Vízgyűjtő digitális iker
- **Forrás:** gis ch19, 18.7.1 „Vízgyűjtő digitális iker"
- **Hivatkozás:** Tájléptékű digitális iker, amely vízgyűjtőket modellez szenzor → modell → beavatkozás visszacsatolási ciklussal; a hidrológiai digitális iker az ERA5 adatokkal, a vízmérce-adatokkal és a szimulációs motorral (CWatM, MODFLOW) dolgozik.
- **Szakterületi példa doboz:** „A vízgyűjtő digitális ikerben a meteorológiai szenzorok, vízmérce-állomások és a hidrológiai szimulációs motor (pl. MODFLOW) zárt ciklust alkotnak: a szenzor-adatokból a modell árvízi előrejelzést készít, amely alapján az öntözés vagy a gátzár vezérelhető."
- **Szakterület:** gis

### 10.4 Példa: Precíziós öntözés mint zárt hurkú rendszer
- **Forrás:** precagri ch20, 20.6 „Vízgazdálkodási kihívások"
- **Hivatkozás:** Talajnedvesség-érzékelők → evapotranspirációs modell → hiányöntözés → center-pivot változó dózisú kijuttatás. „A precíziós öntözés Magyarországon a klimaváltozás túlélési technológiája."
- **Szakterületi példa doboz:** „A magyar Alföldön a precíziós öntözés zárt visszacsatolási hurkot valósít meg: talajnedvesség-szenzor → ET-modell → öntözési döntés → center-pivot változó dózisú kijuttatás — ami a digitális iker 4. szintjének mezőgazdasági megvalósítása."
- **Szakterület:** precagri

---

## 11. fejezet — Az AI ágensek megértése

### 11.1 Példa: Az ágenshurok a hidrológiai kalibrálásban
- **Forrás:** hidrogis ch24, 24.1.2 „Az ágenshurok: tervezés, végrehajtás, értékelés, iteráció"
- **Hivatkozás:** Az ágens célt kap („kalibráld a HEC-HMS modellt, NSE > 0,7"), részfeladatokra bontja (10 lépés: adatbetöltés → paraméterek → futtatás → értékelés → módosítás → iteráció), eszközöket hív, diagnosztizálja a hibákat („a csúcsok túl magasak → görbe-szám túl magas"), és dokumentálja a gondolkodási láncot.
- **Szakterületi példa doboz:** „A hidrológiai modellkalibrálásban az AI-ágens ciklikusan működik: tervet készít, futtatja a modellt, értékeli az eredményt ('a szimulált csúcsok túl korán jönnek → késleltetési idő túl rövid'), módosítja a paramétereket, és iterál — 100–1000 modellfuttatás helyett 50–200-ból konvergál."
- **Szakterület:** hidrogis

### 11.2 Példa: ReAct-ciklus a Natura 2000 elemzésben
- **Forrás:** gis ch22, 21.3.1 „A ReAct keretrendszer és geoinformatikai alkalmazása"
- **Hivatkozás:** Nyolclépéses ReAct-ciklus: Gondolat → Cselekvés (STAC API) → Megfigyelés → Gondolat → Cselekvés (Python: zonális statisztika) → Megfigyelés → Gondolat (eredmény-ellenőrzés) → Prezentáció. „Melyik Natura 2000 területen nőtt a beépítettség 2020 óta?"
- **Szakterületi példa doboz:** „A geoinformatikai ReAct-ágensben a gondolkodás és cselekvés váltakozik: az ágens STAC API-n keresztül letölti a WorldCover adatokat, Python-kóddal zonális statisztikát számol, ellenőrzi az eredményt, és bemutatja: 12 Natura 2000 területen nőtt a beépítettség."
- **Szakterület:** gis

### 11.3 Példa: Többágenses rendszer a GIS-ben
- **Forrás:** gis ch22, 21.3.4 „Többágenses rendszerek"
- **Hivatkozás:** Négy specializált ágens: adat-kereső (STAC, WFS, PostGIS), GIS-analizátor (SQL, Python), kartográfus (színválasztás, szimbolizáció), kritikus (CRS-ellenőrzés, topológiai validáció) — üzenetbuszon kommunikálnak.
- **Szakterületi példa doboz:** „A geoinformatikában a többágenses rendszer négy specializált ágenst kombinál: az adat-kereső megtalálja a Sentinel-2 adatokat, a GIS-analizátor elvégzi a térbeli elemzést, a kartográfus elkészíti a térképet, a kritikus ellenőrzi a CRS-t és a topológiát."
- **Szakterület:** gis

---

## 12. fejezet — AI ágensek építése kutatáshoz

### 12.1 Példa: Hidrológiai modellezési ágens architektúrája és a Zala folyó kalibrálása
- **Forrás:** hidrogis ch24, 24.3 „Egy hidrológiai modellezési ágens architektúrája" és 24.11 „Magyar kidolgozott példa: A Zala vízgyűjtője"
- **Hivatkozás:** 24.3.1 Gondolkodó motor (LLM mint következtető mag); 24.3.2 Eszközkészlet (modellfuttató, adatolvasó, statisztikai kiértékelő, vizualizáló); 24.3.3 Orkesztrációs keretrendszer. Zala vízgyűjtő (930 km²) kalibrálás: ERA5-Land + OVF vízhozamadatok, GR4J modell, 6 iteráció, KGE = 0,78, 47 modellfuttatás, ~3 perc.
- **Szakterületi példa doboz:** „A Zala folyó vízgyűjtőjére (930 km²) épített hidrológiai ágens az ERA5-Land csapadékból, az OVF vízhozamadatokból és a Corine felszínborításból kiindulva 47 modellfuttatással kalibrálta a GR4J modellt KGE = 0,78 teljesítményre — a teljes folyamat dokumentálva, a gondolkodási lánc naplózva."
- **Szakterület:** hidrogis

### 12.2 Példa: Automatikus Sentinel-2 elemzés és riportgenerálás
- **Forrás:** gis ch22, 21.8.3 „Esettanulmány: automatikus Sentinel-2 elemzés és riportgenerálás"
- **Hivatkozás:** MI-ágens, amely automatikusan elemzi a Sentinel-2 adatokat és riportot generál erdőborítás-változásról — letöltés, osztályozás, változásdetekció, térkép, szöveges összefoglaló.
- **Szakterületi példa doboz:** „Egy GIS-ágens a Sentinel-2 adatokat automatikusan letölti, osztályozza, a változásdetekciót elvégzi, térképet és szöveges riportot generál az erdőborítás-változásról — a teljes munkafolyamat természetes nyelvi prompttal indul."
- **Szakterület:** gis

---

## 13. fejezet — Saját programok és eszközök készítése

### 13.1 Példa: Minimális működő hidrológiai ágens építése
- **Forrás:** hidrogis ch24, 24.12 „Saját hidrológiai ágens építése"
- **Hivatkozás:** 24.12.1 „Minimális működő példa" — Python-kód az LLM + eszközök + orkesztráció összekapcsolására; 24.12.2 „Gyakorlati tippek az implementáláshoz" — eszköz-API tervezés, hibakezelés, naplózás.
- **Szakterületi példa doboz:** „A fejezet Python-kódpéldával mutatja be, hogyan építhető minimális hidrológiai ágens: az LLM-et eszközökkel (modellfuttató, adatolvasó, statisztikai kiértékelő) kapcsoljuk össze orkesztrációs keretrendszerben, és a gondolkodási lánc naplózásával biztosítjuk az auditálhatóságot."
- **Szakterület:** hidrogis

### 13.2 Példa: Geoinformatikai eszköztár tervezése LLM-hez
- **Forrás:** gis ch22, 21.4.1 „Az LLM és a szoftverkörnyezet kapcsolata: tool use"
- **Hivatkozás:** 15–30 jól definiált eszköz az optimális tartomány; STAC-kereső, térbeli műveleti, raszteres feldolgozó, vizualizációs és validációs eszközök JSON schema leírással; hierarchikus szervezés.
- **Szakterületi példa doboz:** „Az Autonomous GIS eszköztárának tervezésénél 15–30 jól definiált eszköz a optimális: STAC-kereső, pufferelő, zonális statisztikát számító, térképgeneráló és CRS-validáló — mindegyiket JSON schemával írjuk le az LLM számára."
- **Szakterület:** gis

---

## 14. fejezet — Az AI-val felszerelt kutatólabor

### 14.1 Példa: FMIS — farmirányítási információs rendszerek
- **Forrás:** precagri ch14, 14.6 „Farmirányítási információs rendszerek (FMIS)"
- **Hivatkozás:** A John Deere Operations Center, Climate FieldView és hasonló felhőplatformok, amelyek a gépekből, érzékelőkből, műholdakból és meteorológiai szolgálatokból származó adatokat egyetlen felületen egyesítik.
- **Szakterületi példa doboz:** „A precíziós mezőgazdaságban a farmirányítási információs rendszer (FMIS) az AI-val felszerelt kutatólabor megfelelője: egyetlen platformon egyesíti a hozamtérképet, a műholdas NDVI-t, a talajszenzorokat és az időjárás-előrejelzést — és gépi tanulással generál kijuttatási ajánlásokat."
- **Szakterület:** precagri

### 14.2 Példa: Magyar egyetemek precíziós mezőgazdasági képzése
- **Forrás:** precagri ch20, 20.7 „Magyar kutatóintézetek és innováció"
- **Hivatkozás:** MATE precíziós mezőgazdasági szakirányú továbbképzés (2 félév, távérzékelés + térinformatika + drón + VRT + FMIS); Debreceni Egyetem VRT nitrogén-kísérletek; Szegedi Egyetem drón-program. „Az egyetemek úgy tervezik programjaikat, hogy azok egy továbbképzési útvonal első modulját jelentsék."
- **Szakterületi példa doboz:** „A MATE, a Debreceni és a Szegedi Egyetem precíziós mezőgazdasági programjai integrálják a távérzékelést, a drónüzemeltetést, a gépi tanulást és a farmmenedzsmentet — a magyar tapasztalat azt mutatja, hogy a képzés a technológia-elterjedés legnagyobb szűk keresztmetszete."
- **Szakterület:** precagri

---

## 15. fejezet — AI az egyetemen

### 15.1 Példa: Képalapú növénybetegség-felismerés mint oktatási projekt
- **Forrás:** precagri ch15, 15.5.1 „Képalapú betegségfelismerés"
- **Hivatkozás:** CNN-ek 95%+ pontossággal azonosítanak növénybetegségeket levélfotókról; transfer learning ImageNet-előtanított hálózatokkal (MobileNet az okostelefonon); 10 000 levélfelvételes adathalmaz, növénypatológus címkéivel.
- **Szakterületi példa doboz:** „A növénybetegség-felismerés kiváló hallgatói projekt: a MobileNet architektúra transfer learninggel, 10 000 címkézett levélfotón betanítva 95%+ pontossággal azonosítja a burgonyavészt — és az eredmény okostelefonon is fut, a gazdálkodó kezében."
- **Szakterület:** precagri

### 15.2 Példa: U-Net szemantikus szegmentálás oktatási esettanulmányként
- **Forrás:** gis ch21, 20.2.4 „Szemantikus szegmentálás: a U-Net architektúra"
- **Hivatkozás:** A U-Net encoder-decoder architektúra skip connectionnel; Sentinel-2 13-csatornás bemenet, cross-entropy + Dice loss, felszínborítás-osztályozás. Matematikai képletek: $\mathcal{L}_{CE}$ és $\mathcal{L}_{Dice}$.
- **Szakterületi példa doboz:** „A U-Net architektúra ideális mélytanulási oktatási példa: az encoder lépcsőzetesen csökkenti a felbontást, a decoder visszaállítja, a skip connectionök megőrzik a részleteket — a hallgatók Sentinel-2 felvételen felszínborítás-térképet készítenek, miközben a cross-entropy és Dice loss veszteségfüggvényeket is megértik."
- **Szakterület:** gis

### 15.3 Példa: Erdőtűz-kár U-Net szegmentálás
- **Forrás:** gis ch21, 20.12 „Erdotuz-kar becsles U-Net-tel: reszletes esettanulmany"
- **Hivatkozás:** Sentinel-2 pre- és post-fire felvételek, dNBR index, U-Net szegmentálás, összehasonlítás a klasszikus dNBR-módszerrel.
- **Szakterületi példa doboz:** „Az erdőtűz-kár becslése U-Net-tel praxis-közeli hallgatói projekt: a Sentinel-2 tűz előtti/utáni felvételekből a hálózat pixelszinten szegmentálja a leégett területet, és az eredmény összevethető a klasszikus dNBR-módszerrel."
- **Szakterület:** gis

---

## 16. fejezet — Etika, reprodukálhatóság és az AI jövője

### 16.1 Példa: Algoritmikus elfogultság a mezőgazdasági MI-ben
- **Forrás:** precagri ch15, 15.8.2 „Algoritmikus elfogultság"
- **Hivatkozás:** „Egy kizárólag nagyüzemi monokultúrás gazdaságokban készült képeken betanított betegségfelismerő modell teljesen csődöt mondhat, ha kisgazdaságok polikultúrás rendszereiben alkalmazzák." Az elfogultság a címkézési folyamaton keresztül is bekerülhet.
- **Szakterületi példa doboz:** „A mezőgazdasági MI-ben az algoritmikus elfogultság valós kockázat: a kizárólag nagyparcellás, mérsékelt övi adatokon tanított hozam-előrejelző modell szisztematikusan hibás eredményt ad trópusi kisgazdaságokban — a betanítási adatok diverzifikálása és a helyi validáció elengedhetetlen."
- **Szakterület:** precagri

### 16.2 Példa: Magyarázható MI (XAI) a döntéstámogatásban
- **Forrás:** precagri ch15, 15.8.3 „Magyarázhatóság és a feketedoboz-probléma" és ch16, 16.7 „A mesterséges intelligencia integrálása a döntéstámogatásba"
- **Hivatkozás:** Grad-CAM kiemeli a CNN által felismert levélfoltokat; SHAP-értékek számszerűsítik az egyes jellemzők hozzájárulását; a gazdálkodó „joggal bizalmatlan azokkal az ajánlásokkal szemben, amelyeket nem ért"; a DSS elfogadásának kulcsa az átláthatóság.
- **Szakterületi példa doboz:** „A mezőgazdasági döntéstámogatásban a Grad-CAM vizuálisan kiemeli, mely levélfoltok váltották ki a betegségdiagnózist — a gazdálkodó összevetheti a saját megfigyelésével, és eldöntheti, cselekszik-e. A magyarázhatóság nem luxus, hanem az elfogadás feltétele."
- **Szakterület:** precagri

### 16.3 Példa: Hallucináció és a Dunning-Kruger ágens
- **Forrás:** hidrogis ch24, 24.10.1–24.10.2 „Hallucináció a tudományos gondolkodásban" és „Túlzott magabiztosság és a Dunning-Kruger ágens"
- **Hivatkozás:** Az ágens „hihetően hangzó, de tényszerűen helytelen információkat generálhat"; a „Dunning-Kruger ágens" túlzott magabiztosságot mutathat kalibrációs eredmények értelmezésében; a megalapozottsági mechanizmusok (adatfájlok, modellkimenetek, fizikai korlátok) szükségessége.
- **Szakterületi példa doboz:** „A hidrológiai ágensek kockázata a hallucináció: a modell hihetően érvelhet amellett, hogy a kalibrálás kiváló, miközben fizikailag lehetetlen paraméterértékeket használ — a megalapozottsági mechanizmusok (valós adatok, fizikai korlátok) és az ember-a-hurokban felügyelet elengedhetetlen."
- **Szakterület:** hidrogis

### 16.4 Példa: Reprodukálhatóság és a gondolkodási lánc naplózása
- **Forrás:** hidrogis ch24, 24.8 „Reprodukálhatóság és auditálhatóság"
- **Hivatkozás:** 24.8.1 — A gondolkodási lánc (chain of thought) nyilvántartása: minden ágensműveletet, gondolatot és eszközkimenetet naplózni kell; 24.8.2 — A reprodukálhatóság biztosítása: rögzített LLM-verzió, seed, eszköz-verziók.
- **Szakterületi példa doboz:** „A hidrológiai ágenses kalibrálás reprodukálhatóságát a gondolkodási lánc naplózása biztosítja: minden paraméterdöntés, diagnosztikus gondolat és modellfuttatás dokumentálva van — szemben a hagyományos 'hajnali kettős hangolgatással', ahol a döntések rekonstruálhatatlanok."
- **Szakterület:** hidrogis

### 16.5 Példa: Adattulajdon és adatvédelem a precíziós mezőgazdaságban
- **Forrás:** precagri ch14, 14.7 „Adatmegosztás, adatvédelem és tulajdonjog" és ch15, 15.8.5 „Adatvédelem és tulajdonjog"
- **Hivatkozás:** „Kié a precíziós mezőgazdasági platform által gyűjtött adatállomány: a gazdálkodóé, a technológiai szolgáltatóé vagy a berendezésgyártóé?" Gazdálkodók által irányított adatszövetkezetek szükségessége; az EU mezőgazdasági adatterek.
- **Szakterületi példa doboz:** „A precíziós mezőgazdaságban az adattulajdon kérdése megoldatlan: ha a gazda feltölti a hozamadatait egy felhőplatformra, a szolgáltató eladhatja-e azokat egy biztosítónak? A gazdálkodói adatszövetkezetek és az átlátható adatirányítás a bizalom építésének alapja."
- **Szakterület:** precagri

---

## Összefoglaló statisztika

| AI-könyv fejezet | precagri | hidrogis | gis | Összes példa |
|---|---|---|---|---|
| 1. AI forradalom | 1 | 1 | 1 | 3 |
| 2. Társalgási AI | 1 | 0 | 1 | 2 |
| 3. Tudományos írás | 1 | 0 | 0 | 1 |
| 4. Adatelemzés | 2 | 1 | 0 | 3 |
| 5. Kódolási asszisztensek | 0 | 1 | 1 | 2 |
| 6. Matematikai modellezés | 1 | 2 | 0 | 3 |
| 7. Adat-pipeline | 2 | 1 | 0 | 3 |
| 8. Vizuális programozás | 0 | 1 | 1 | 2 |
| 9. RAG | 1 | 0 | 1 | 2 |
| 10. Digitális ikrek | 1 | 0 | 3 | 4 |
| 11. AI ágensek | 0 | 1 | 2 | 3 |
| 12. Ágensek építése | 0 | 1 | 1 | 2 |
| 13. Eszközök készítése | 0 | 1 | 1 | 2 |
| 14. AI labor | 2 | 0 | 0 | 2 |
| 15. AI az egyetemen | 1 | 0 | 2 | 3 |
| 16. Etika és jövő | 2 | 2 | 0 | 4* |
| **Összesen** | **15** | **12** | **14** | **41** |

*A 16. fejezetnek 5 bejegyzése van, mert az etikai és reprodukálhatósági témák több szálat igényelnek.

---

## Felhasznált forrásfejezetek kereszthivatkozása

| Forrásfejezet | Hivatkozva (AI-könyv fejezetek) |
|---|---|
| precagri ch03 (adatforradalom) | 1 |
| precagri ch14 (data pipeline) | 4, 7, 16 |
| precagri ch15 (AI/ML) | 2, 3, 6, 9, 15, 16 |
| precagri ch16 (DSS) | 6, 16 |
| precagri ch20 (Magyarország) | 10, 14 |
| hidrogis ch12 (automatizálás) | 5, 7, 8 |
| hidrogis ch23 (ML hidrológia) | 1, 6 |
| hidrogis ch24 (ágens AI) | 4, 6, 11, 12, 13, 16 |
| gis ch19 (3D, digital twin) | 10 |
| gis ch21 (ML/DL geoinf.) | 15 |
| gis ch22 (Autonomous GIS) | 1, 2, 5, 8, 9, 11, 12, 13 |
