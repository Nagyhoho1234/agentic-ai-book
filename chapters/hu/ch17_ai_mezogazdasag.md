# 17. fejezet: AI a precíziós mezőgazdaságban

> **Fejezet-informacio**
> - **Kinek szol:** Agrarkutatoknak, gazdalkodoknak es mezogazdasagi szaktanaacsadoknak
> - **Eloismeretek:** 1-4. fejezet (AI alapok, adatelemzes); a 5-12. fejezet hasznos, de nem kotelezo
> - **Amit megtanulsz:**
>   - Az AI helye a precizios gazdalkodas ciklusaban (adatgyujtestol a donteshozatalig)
>   - Muholdkepes novenyfigyelés, hozam-elorejelzes es ontözesoptimalizalas
>   - Digitalis ikrek es agensek mezogazdasagi alkalmazasai
> - **Szukseges eszkozok:** Browser + terminal + Python (a gyakorlati peldaakhoz)
> - **Kapcsolodo fejezetek:** 7. fejezet (pipeline-ok), 10. fejezet (digitalis ikrek), 19. fejezet (terinformatika)

## Amikor a tábla beszélni kezd

Gábor a Hajdúságban gazdálkodik, hatszáz hektáron kukoricát és búzát termeszt. Minden májusban drónnal repüli végig a tábláit, a Sentinel-2 műhold ötnaponta küld friss NDVI-térképet, a talajnedvesség-szenzorjai óránként jelentenek, az agrometeorológiai állomása pedig percenként rögzíti a hőmérsékletet, a páratartalmat és a szélsebességet. Gábornak nem az adathiány a problémája --- hanem az adatbőség. Egy átlagos tenyészidőszakban a gazdasága több terabájtnyi adatot termel: műholdfelvételek, drónos multispektrális képek, hozamtérképek, talajvizsgálati eredmények, gépi telematikai adatok, időjárási idősorok. Ezek az adatok különböző formátumokban, különböző platformokon, különböző koordináta-rendszerekben érkeznek. Gábor tudja, hogy aranyat ér bennük --- de nincs ideje és kapacitása, hogy minden reggel tizenöt különböző szoftvert nyisson meg, és kézzel rakja össze a képet.

Ez a fejezet arról szól, hogyan változtatja meg a mesterséges intelligencia a precíziós mezőgazdaság minden lépését --- az adatgyűjtéstől a döntéshozatalig, a talajtérképezéstől az autonóm öntözésig. A korábbi fejezetekben megismert AI-eszközöket --- a prompttervezést, az adatelemzést, a kódolási asszisztenseket, a pipeline-okat, a RAG-rendszereket, a digitális ikreket és az ágens-architektúrákat --- most a mezőgazdaság kontextusában alkalmazzuk. Ha eddig laboratóriumi adatokkal vagy klímamodellekkel dolgoztál, itt meglátod, hogyan működnek ugyanezek a módszerek, amikor a labor a szántóföld, a minta a talaj, és a kísérlet egy egész tenyészidőszak.

> **Előfeltételek:** Ez a fejezet feltételezi, hogy elolvastad legalább az 1--4. fejezetet (az AI alapjai, társalgási AI, tudományos írás, adatelemzés kód nélkül). A szakaszok explicit hivatkozásokat tartalmaznak a 5--12. fejezetekre is, de ezek nem előfeltételek --- a lényeget minden szakasz önállóan is elmagyarázza.

---

## 17.1 Az AI a precíziós gazdálkodás ciklusában

A precíziós mezőgazdaság egy ismétlődő ciklust követ: **adatgyűjtés** → **adatfeldolgozás** → **elemzés és értelmezés** → **döntéshozatal** → **végrehajtás** → **monitoring** → és újra adatgyűjtés. Ez a ciklus nem újdonság --- a precíziós mezőgazdaság alapszövege az 1990-es évek óta így írja le a folyamatot. Ami új, az a mesterséges intelligencia belépése a ciklus minden egyes pontjába.

```
        ┌──────────────────────────────────────┐
        │          ADATGYŰJTÉS                  │
        │  Műhold, drón, IoT, szenzor, GPS      │
        │  AI: automatikus adatválogatás,        │
        │      anomáliadetekció                  │
        └──────────┬───────────────────────────┘
                   │
                   ▼
        ┌──────────────────────────────────────┐
        │          ADATFELDOLGOZÁS              │
        │  Tisztítás, integráció, interpoláció  │
        │  AI: ML-alapú outlier-szűrés,         │
        │      automatikus georeferálás          │
        └──────────┬───────────────────────────┘
                   │
                   ▼
        ┌──────────────────────────────────────┐
        │       ELEMZÉS ÉS ÉRTELMEZÉS          │
        │  Hozam-előrejelzés, zónalehatárolás   │
        │  AI: deep learning, LLM-értelmezés,   │
        │      térbeli klaszterezés              │
        └──────────┬───────────────────────────┘
                   │
                   ▼
        ┌──────────────────────────────────────┐
        │          DÖNTÉSHOZATAL                │
        │  VRT-térképek, öntözési terv, permetezés│
        │  AI: DSS, optimalizáció,              │
        │      megerősítéses tanulás             │
        └──────────┬───────────────────────────┘
                   │
                   ▼
        ┌──────────────────────────────────────┐
        │         VÉGREHAJTÁS ÉS MONITORING    │
        │  Változó dózisú kijuttatás, autonóm   │
        │  gépek, valós idejű visszacsatolás    │
        │  AI: computer vision, robotikaAI       │
        └──────────┬───────────────────────────┘
                   │
                   └──────────► vissza az elejére
```

Az AI nem egyetlen ponton lép be ebbe a ciklusba --- hanem mindenhol. Az adatgyűjtésnél automatikusan szűri a felhős műholdfelvételeket és a hibás szenzorjeleket. A feldolgozásnál megtisztítja a hozamtérképeket a kiugró értékektől. Az elemzésnél deep learning modellekkel azonosítja a beteg növényeket és előrejelzi a hozamot. A döntéshozatalnál optimalizálja a műtrágyaadagot és az öntözési ütemezést. A végrehajtásnál vezeti az autonóm permetezőt és a robotkapálót. Ez a fejezet végigvezet ezen a teljes körön.

---

## 17.2 AI a mezőgazdasági adatkezelésben

### Műholdfelvételek: a Sentinel-2-től az értelmezésig

A magyar precíziós mezőgazdaság egyik legnagyobb ajándéka az Európai Unió Copernicus-programja. A Sentinel-2 műholdak ingyenes, 10 méteres felbontású multispektrális felvételeket szolgáltatnak, névlegesen mintegy ötnapos visszatérési idővel. Egy hatszáz hektáros gazdaság minden ötödik napon friss NDVI-, NDRE- és klorofilltartalom-térképet kaphat --- ingyen.

A probléma az, hogy a nyers Sentinel-2 adatok nem használhatók közvetlenül. Légköri korrekció kell, felhőmaszkolás kell, a különböző időpontok felvételeit egymáshoz kell illeszteni, és az eredményt a gazdaság táblahatáraira kell vágni. Hagyományosan ez térinformatikai szakértelmet igényelt --- QGIS-t, Google Earth Engine-t, vagy Python-szkripteket `rasterio` és `geopandas` könyvtárakkal.

Ahogy a 7. fejezetben láttuk, egy pipeline automatizálhatja ezt a folyamatot. De most adjuk hozzá az AI-t:

**1. Automatikus felhőszűrés ML-lel.** A Sentinel-2 saját felhőmaszkja (SCL-réteg) nem mindig pontos. Egy egyszerű random forest osztályozó, amelyet a te tábláidról készült felvételek manuálisan felcímkézett pixelein tanítasz be, jobb felhőmaszkot adhat, mint a gyári algoritmus. A 6. fejezetben megismert modellépítési elvek itt közvetlenül alkalmazhatók.

**2. LLM-alapú adatminőség-ellenőrzés.** Tölts fel egy Sentinel-2-idősor statisztikáját (átlag NDVI táblánként, időpontonként) egy Claude vagy GPT promptba:

```
Az alábbi táblázat a 12-es tábla NDVI-átlagait mutatja 2025 áprilistól
júliusig, kéthetente. Azonosítsd azokat az időpontokat, ahol az NDVI-érték
valószínűleg hibás (pl. felhőzet, szenzor-probléma), és javasold,
hogyan interpoláljam a hiányzó értékeket.

Dátum        | NDVI átlag | NDVI szórás
2025-04-01   | 0.18       | 0.04
2025-04-15   | 0.31       | 0.06
2025-05-01   | 0.12       | 0.15
2025-05-15   | 0.58       | 0.08
2025-06-01   | 0.71       | 0.07
2025-06-15   | 0.74       | 0.06
2025-07-01   | 0.69       | 0.09
```

A 2. fejezetben részletezett prompttervezési elvek alapján a modell azonnal észreveszi, hogy a május 1-jei érték gyanúsan alacsony (és a szórás is magas), ami felhőzetre vagy részleges felhőborításra utal. Javaslatot tesz időbeli interpolációra vagy az adott felvétel kihagyására.

**3. Automatikus anomáliadetekció.** Ahogy a 4. fejezetben megtanultad a statisztikai kiugró értékek keresését, ugyanezt alkalmazhatod a műholdfelvételek idősoraira. Ha az NDVI egy táblarészen hirtelen 0,3-mal esik két felvétel között, de a szomszédos táblákon nem változik, az nem a műhold hibája --- az lehet kártevő, belvíz, vagy jégkár.

### Szenzor-hálózatok és IoT

A modern precíziós gazdaság IoT-szenzorjai --- talajnedvesség, talajhőmérséklet, levélnedvesség, EC-szondák --- folyamatos adatáramot termelnek. Egy átlagos gazdaság tucatnyi, egy nagyüzem akár több száz szenzorcsomóponttal is rendelkezhet. Ezek az adatok jellemzően LoRaWAN vagy NB-IoT hálózaton keresztül jutnak el egy felhőplatformra vagy helyi szerverre.

Az AI három szinten segít:

- **Edge-szintű szűrés:** Egy kis ML-modell közvetlenül a szenzor-csomóponton fut, és kiszűri a nyilvánvalóan hibás méréseket (negatív talajnedvesség, 80 °C-os talajhőmérséklet) még az adattovábbítás előtt. Ez csökkenti a rádióforgalmat és az adattárolási igényt.
- **Idősor-anomáliadetekció:** Egy LSTM-modell megtanulja a normális napi talajnedvesség-mintázatot (reggeli csúcs, délutáni száradás), és riaszt, ha a minta eltér --- ami szenzor-meghibásodást vagy valós mezőgazdasági eseményt (belvíz, csőtörés) jelezhet.
- **Szenzor-fúzió:** Több szenzor adatait kombinálja egyetlen koherens képpé. A talajnedvesség-mérés önmagában egy pont; ha kombináljuk a domborzatmodellel, a talaj-EC-vel és az időjárási adatokkal, az interpoláció sokkal pontosabb.

### Időjárási API-k és előrejelzések

Ahogy a 7. fejezetben láttuk, az API-k a pipeline-ok alapvető adatforrásai. A mezőgazdasági kontextusban a legfontosabb API-k:

- **Open-Meteo** (ingyenes, nyílt forráskódú): óránkénti és napi előrejelzés, historikus adatok, EU-lefedettség.
- **OMSZ** (Országos Meteorológiai Szolgálat): magyar mérőhálózat adatai.
- **Copernicus Climate Data Store**: ERA5 reanalízis, szezonális előrejelzések.

Egy mezőgazdasági pipeline például minden reggel 6-kor:
1. Letölti az Open-Meteo 7 napos előrejelzését a gazdaság koordinátáira.
2. Letölti a Sentinel-2 legutóbbi felhőmentes felvételét a Copernicus API-n keresztül.
3. Lekérdezi a talajnedvesség-szenzorokat az IoT-platformról.
4. Kiszámolja a referencia-evapotranszspirációt (ET₀) az FAO Penman-Monteith egyenlettel.
5. AI-modellel összeveti az ET₀-t a talajnedvességgel és a növény fenológiai állapotával.
6. Ha öntözés szükséges, riasztást küld Gábor telefonjára.

Ez nem fantázia --- ez egy n8n vagy Apache Airflow workflow, amelyet a 8. fejezetben leírt vizuális programozási elvekkel néhány óra alatt össze lehet rakni.

---

## 17.3 AI-asszisztált növényállomány-monitoring

### NDVI-térképek értelmezése LLM-ekkel

Az NDVI (Normalized Difference Vegetation Index) a precíziós mezőgazdaság legszélesebb körben használt vegetációs indexe. A vörös és a közeli infravörös reflektancia-sávokból számított NDVI értékei 0-tól (csupasz talaj) közel 1-ig (sűrű, egészséges vegetáció) terjednek. Egy Sentinel-2-felvételből számolt NDVI-térkép megmutatja, hol zöld és egészséges az állomány, és hol van probléma.

De mit jelent egy probléma? Az NDVI-térkép egy „forró foltja" --- ahol az érték alacsonyabb a vártnál --- lehet nitrogénhiány, vízstressz, kártevőkár, belvíz, talajtömörödés, vagy egyszerűen a tábla szélén lévő fordulósáv. A hagyományos megközelítés: az agronómus megnézi a térképet, kimegy a terepe, és a tapasztalata alapján értelmezi. De mi van, ha az agronómus nem elérhető, vagy hatszáz hektárt kell egyszerre áttekinteni?

Ahogy a 2. fejezetben részleteztük, a társalgási AI-modellek kiválóan alkalmasak arra, hogy struktúrálatlan vagy félig strukturált adatokat értelmezzenek. Egy NDVI-térkép értelmezéséhez a következő promptot használhatod:

```
Egy 120 hektáros kukoricatáblán (Hajdúság, csernozjom talaj, öntözetlen)
a június 15-i Sentinel-2 NDVI-térkép a következő mintázatot mutatja:

- A tábla északi harmadában az NDVI 0.72-0.78 (egészséges).
- A középső sávban az NDVI hirtelen 0.45-re esik egy 200 méter széles,
  kelet-nyugati irányú sávban.
- A déli harmadban az NDVI 0.65-0.70 (kissé az átlag alatt).
- A tábla délnyugati sarkában egy 2 hektáros folt NDVI-je 0.30.

Kontextus:
- Az elmúlt 3 hétben 12 mm csapadék esett (átlag: 45 mm).
- A tábla középső része egy enyhe mélyedésben fekszik (domborzatmodell alapján).
- Tavaly ugyanitt a hozam 8.2 t/ha volt (táblaátlag: 9.5 t/ha).
- Kukorica V8-V10 fenofázisban van.

Mi okozhatja az egyes mintázatokat? Milyen terepbejárási tervet javasolsz?
```

Egy jól felépített prompt --- a 2. fejezet elvei szerint, kontextussal, konkrét adatokkal és célkérdéssel --- valódi agronómiai értelmezést eredményez. A modell összekapcsolja a domborzatot a belvízzel, az aszályos időszakot a vízstresszel, a délnyugati sarok izolált foltját esetleges géphibával vagy szivárgó drénnel. Természetesen az LLM nem helyettesíti a terepbejárást --- de drámaian csökkenti az időt és az erőfeszítést, amellyel a gazdálkodó eldönti, *hová menjen* és *mit keressen*.

### Multispektrális és hiperspektrális adatok értelmezése

Az NDVI csak a kezdet. A modern drónok --- mint a DJI Matrice 300 RTK Micasense Altum szenzorral --- öt vagy több spektrális sávban rögzítenek adatot: kék, zöld, vörös, vörös él (red edge), közeli infravörös és hőinfravörös. Ezekből számítható:

| Index | Képlet | Mit mér |
|-------|--------|---------|
| NDVI | (NIR - Red) / (NIR + Red) | Általános növényállapot |
| NDRE | (NIR - RedEdge) / (NIR + RedEdge) | Klorofilltartalom, N-hiány |
| GNDVI | (NIR - Green) / (NIR + Green) | Klorofill, alacsony borítás mellett érzékenyebb |
| CWSI | Hőfelvételből származtatott | Vízstressz |

Ahogy a 4. fejezetben megtanultad, az adatelemzés első lépése mindig a feltáró vizsgálat. Tölts fel egy multispektrális indexkészletet (NDVI, NDRE, GNDVI, CWSI táblánkénti zónastatisztikáit) egy AI-chatbe, és kérd meg, hogy azonosítsa azokat a zónákat, ahol az indexek ellentmondanak egymásnak. Például: ha az NDVI normális, de az NDRE alacsony, az korai nitrogénhiányra utalhat, mielőtt az a szabad szemmel vagy az NDVI-n láthatóvá válna.

### Idősorok elemzése: a fenológiai görbe

A legértékesebb információ nem egyetlen felvételből, hanem az idősorból jön. A kukorica NDVI-görbéje jellegzetes alakot követ: alacsony értékek a vetés után, meredek emelkedés a vegetatív növekedés során, csúcs a címerhányás körül, majd fokozatos csökkenés az érés során. Ha egy táblarész görbéje eltér a többitől --- későbbi emelkedés, alacsonyabb csúcs, korábbi visszaesés --- az probléma jele.

Ahogy a 4. fejezetben megismerted a trendvizsgálati módszereket, itt ugyanazokat az eszközöket alkalmazhatod. Egy Claude Code prompttal akár kóddal is generáltathatsz:

```
Írj Python-szkriptet, amely beolvassa a Sentinel-2 NDVI idősorom CSV-jét
(oszlopok: date, zone_id, mean_ndvi, std_ndvi), és minden kezelési zónára
kirajzolja az NDVI fenológiai görbét. Jelöld meg pirossal azokat a zónákat,
ahol a csúcs NDVI 15%-kal alacsonyabb az átlagnál. Használj matplotlib-et.
```

---

## 17.4 Gépi tanulás a mezőgazdasági döntéstámogatásban

### Hozam-előrejelzés

A hozam-előrejelzés a precíziós mezőgazdaság szent grálja. Ha a gazdálkodó már a szezon közepén tudja, melyik táblarészen mennyi termés várható, jobban tervezheti az értékesítést, a szárítást és a logisztikát.

A gépi tanulás ezen a területen az egyik leglátványosabb eredményeket éri el. Ahogy a 6. fejezetben részleteztük a matematikai modellezés elveit, a hozam-előrejelzési modell általános felépítése:

**Bemenetek (features):**
- Időjárási idősorok (hőmérséklet, csapadék, napsugárzás, páratartalom)
- Műholdas vegetációs indexek idősorai (NDVI, NDRE, LAI)
- Talajtulajdonságok (textúra, szervesanyag, pH, tápanyagszintek, EC)
- Gazdálkodási adatok (vetési időpont, fajta, műtrágyaadagok, növényvédelem)
- Történeti hozamadatok (korábbi évek hozamtérképei)

**Kimenet (target):**
- Becsült hozam (t/ha), esetleg konfidencia-intervallummal

**Modellek:**
- **Random forest:** Jó kiindulópont, értelmezhetőbb, mint a mély hálózatok. A változók fontossági rangsorát közvetlenül megkapod, ami agronómiai értelmezést tesz lehetővé (a 6. fejezet SHAP-értékeivel kiegészítve).
- **XGBoost / LightGBM:** A leggyakrabban használt modellek versenyeken és kutatásban egyaránt, jellemzően a random forestnél jobb prediktív teljesítménnyel.
- **CNN-LSTM hibrid:** A CNN-komponens térbeli jellemzőket nyer ki a műholdfelvételekből, az LSTM időbeli mintázatokat tanul a szezonális dinamikából. A kutatásban a legígéretesebb architektúra, de nagyobb adatigénnyel és számítási költséggel jár.

A 6. fejezetben hangsúlyoztuk, hogy minden modellnél a validáció a kulcs. A mezőgazdaságban ez különösen fontos, mert az adatok évről évre drámaian változnak. Egy 2022-es (aszályos) éven tanított modell katasztrofálisan félrejelezhet egy 2023-as (csapadékos) évet. A megoldás: **leave-one-year-out cross-validation**, ahol a modellt mindig az egyik évet kihagyva tanítjuk, és az elhagyott éven teszteljük.

### Talajtérképezés és kezelési zónák

A precíziós tápanyag-gazdálkodás alapja a tábla kezelési zónákra osztása. A hagyományos megközelítés: talaj-EC-felmérés, rácspontos mintavétel, krigelés, majd klaszterezés (pl. k-means). Az AI ezt a munkafolyamatot többféleképpen javítja:

**1. Gépi tanulási alapú interpoláció.** A klasszikus krigelés (amit a precíziós mezőgazdasági szakirodalom a talajtérképezés arany standardjaként kezel) egy változó térbeli autokorrelációs struktúráján alapul. De egy random forest vagy gradient boosting modell nem csak a térbeli pozíciót, hanem segédváltozókat is felhasználhat: a domborzatot, a talaj-EC-t, a műholdfelvételeket, a korábbi hozamtérképeket. Az eredmény gyakran jobb prediktív teljesítmény, mint a hagyományos geostatisztikáé --- különösen, ha a segédváltozók erős összefüggésben vannak a céltulajdonsággal.

**2. Automatikus klaszterszám-meghatározás.** A k-means algoritmusnál a felhasználónak előre meg kell adnia a klaszterek számát. A gyakorlatban az agronómus „érzésre" választ 3-5 zónát. Az AI-megközelítés: futtass k-means-t 2-től 10-ig, számold ki a silhouette-értékeket, és hagyd, hogy a modell válassza ki az optimumot. A 4. fejezetben megismert elbow-módszer itt közvetlenül alkalmazható.

**3. LLM-értelmezés.** Miután a klaszterezés elkészült, tölsd fel a zónák statisztikáit egy AI-chatbe:

```
A 7-es tábla 3 kezelési zónára oszlik. Az egyes zónák jellemzői:

Zóna 1 (42 ha): EC=28 mS/m, szervesanyag=3.2%, pH=6.8,
  átlag NDVI=0.74, átlag hozam (5 év)=9.8 t/ha, CV=8%
Zóna 2 (35 ha): EC=45 mS/m, szervesanyag=2.1%, pH=7.9,
  átlag NDVI=0.61, átlag hozam=7.2 t/ha, CV=22%
Zóna 3 (18 ha): EC=62 mS/m, szervesanyag=1.4%, pH=8.3,
  átlag NDVI=0.48, átlag hozam=5.1 t/ha, CV=35%

Ez egy öntözetlen alföldi tábla, csernozjom-réti átmenettel.
Mi okozza a zónák közötti különbségeket? Milyen differenciált
kezelést javasolsz a következő kukoricaszezonra?
```

Az AI-válasz összekapcsolja a magas EC-t a finomabb textúrával vagy szikesedéssel, a magas variabilitási együtthatót a belvíz-érzékenységgel, és zóna-specifikus műtrágyázási, vetőmagnorma- és esetleg fajtajavaslatot ad.

### Kártevő- és betegségdetekció

A deep learning-alapú képosztályozás a mezőgazdasági AI egyik leglátványosabb sikertörténete. Ahogy a precíziós mezőgazdasági szakirodalom részletezi, a CNN-alapú modellek kontrollált körülmények között 96-99%-os pontossággal képesek növénybetegségeket osztályozni levélfelvételek alapján.

A gyakorlati alkalmazás lépései:

1. **Adatgyűjtés:** Drónnal vagy okostelefonnal készíts felvételeket a beteg és egészséges növényekről. A PlantVillage nyilvános adatkészlet jó kiindulópont a tanításhoz.
2. **Transfer learning:** Ahogy a 6. fejezetben megismerted a modellépítés elveit, ne a nulláról tanítsd a modellt. Vegyél egy előtanított CNN-t (pl. MobileNet, EfficientNet), és finomhangold a saját adataidon. Ez néhány száz címkézett képpel is működőképes modellt ad.
3. **Telepítés edge-eszközre:** A MobileNet-et kifejezetten úgy tervezték, hogy okostelefonokon és beágyazott eszközökön is fusson. A gazdálkodó a terepen, internetkapcsolat nélkül is azonnal diagnózist kaphat.

Az AI-alapú kártevő-előrejelzés egy további lépés: IoT-szenzorból érkező mikroklimatikus adatok (hőmérséklet, páratartalom, levélnedvesség) alapján a modell előrejelzi, mikor lesznek a feltételek kedvezőek egy kórokozó szaporodásához. A 7. fejezetben ismertetett pipeline-logika itt is érvényes: a szenzor mér → a modell értékel → a rendszer riaszt.

---

## 17.5 AI kódolási asszisztensek a mezőgazdasági adatfeldolgozásban

Ahogy az 5. fejezetben részletesen tárgyaltuk, az AI kódolási asszisztensek --- Claude Code, GitHub Copilot, Cursor --- drámaian lecsökkentik a programozási küszöböt. A mezőgazdasági adatfeldolgozás tele van olyan feladatokkal, amelyek programozási tudást igényelnek, de nem programozási problémák: raszter-feldolgozás, zónastatisztikák, koordináta-transzformáció, idősor-elemzés.

### Raszterfeldolgozás Claude Code-dal

Gábor szeretné kiszámolni a tábláinak átlagos NDVI-jét Sentinel-2-felvételből. Hagyományosan ez QGIS-ben történne: GeoTIFF betöltés, vágás táblahatárra, zónastatisztika plugin. De ha ezt hetente, húsz táblára, automatikusan kell csinálni, a QGIS-kattintgatás nem megoldás.

Claude Code-dal:

```
Írj Python-szkriptet, amely:
1. Beolvassa a 'sentinel2_20250615.tif' GeoTIFF fájlt (B4=vörös, B8=NIR sáv).
2. Kiszámolja az NDVI-t pixelenként.
3. Beolvassa a 'tablak.gpkg' GeoPackage fájlt, amely a gazdaság táblahatárait
   tartalmazza (EOV koordináta-rendszer, EPSG:23700).
4. Minden táblára kiszámolja az átlagos, mediánt, szórás és 10. percentilis NDVI-t.
5. Az eredményt CSV-be menti, oszlopok: tabla_id, date, mean_ndvi, median_ndvi,
   std_ndvi, p10_ndvi.
Használj rasterio-t és geopandas-t.
```

Az 5. fejezetben tanult elvek szerint: adj kontextust (formátumok, koordináta-rendszer, sávjelölés), légy specifikus (melyik statisztikák, milyen kimenet), és az eredményt ellenőrizd (a mediánnak és az átlagnak közel kell lennie normális NDVI-eloszlás esetén).

> **Fontos megjegyzés EOV-koordinátákról:** Ahogy a magyar precíziós mezőgazdasági gyakorlatban közismert, az EOV-koordinátákat az értéktartományuk alapján kell azonosítani, nem a fejlécek alapján. Az északi koordináta (Northing) a 0--400 000 tartományba esik, a keleti (Easting) 400 000--1 000 000 közé. A régi adatfájlokban az oszlopfejlécek gyakran felcserélik ezeket. Ha a Claude Code által generált szkript nem a várt helyre illeszti a táblákat, először ellenőrizd a koordináták tartományát!

### Hozamtérkép-tisztítás automatizálása

A nyers hozamtérképek tele vannak hibás értékekkel: a kombájn indulásánál és megállásánál mért hamis hozamok, a fordulókban rögzített értékek, a GPS-csúszások okozta helytelen pozíciók. A precíziós mezőgazdasági szakirodalom részletesen leírja a standard tisztítási lépéseket --- de ezek implementálása programozási feladat.

```
Írj Python-szkriptet, amely megtisztítja a nyers hozamtérképet (shapefile,
attribútumok: yield_tha, speed_kmh, moisture_pct, swath_width_m, lat, lon):

1. Távolítsd el a negatív vagy nulla hozamú pontokat.
2. Távolítsd el a biológiailag lehetetlen hozamokat (kukoricánál >20 t/ha).
3. Távolítsd el a pontokat, ahol a sebesség < 1.5 km/h vagy > 12 km/h.
4. Távolítsd el a táblahatáron kívüli pontokat (gpkg fájl alapján).
5. Alkalmazz 2.5 szórásos lokális szűrőt (50 méteres sugárban).
6. Mentsd a megtisztított adatot új shapefile-ba, és készíts összefoglaló
   statisztikát: hány pontot töröltél, és miért.
```

A 7. fejezet pipeline-szemlélete itt is érvényes: ez a szkript beilleszthető egy automatizált munkafolyamatba, amely minden aratási nap végén lefut a friss adatokon.

### Evapotranszspiráció számítása

Az FAO Penman-Monteith egyenlet a referencia-evapotranszspiráció (ET₀) számításának nemzetközi standardja. Az egyenlet nem bonyolult, de sok bemeneti paramétert igényel (hőmérséklet, páratartalom, szélsebesség, napsugárzás), és a származtatott változók (telítési gőznyomás, nettó sugárzás) kiszámítása hibára hajlamos.

```
Írj Python-függvényt, amely kiszámolja a napi referencia-evapotranszspirációt
az FAO Penman-Monteith egyenlettel. Bemenetek: T_min, T_max (°C),
RH_min, RH_max (%), u2 (m/s 2 méteren), Rs (MJ/m²/nap),
lat (fok), doy (nap a januári naptól). Kimenet: ET0 (mm/nap).
Tartsd be pontosan az FAO-56 dokumentáció módszertanát.
Adj hozzá docstringet és unit-teszteket 3 ismert bemeneti-kimeneti párral.
```

---

## 17.6 Vizuális programozás a mezőgazdasági munkafolyamatokhoz

Ahogy a 8. fejezetben megismerted, a vizuális programozási eszközök --- n8n, KNIME, Node-RED --- lehetővé teszik komplex munkafolyamatok összeállítását programozás nélkül, drag-and-drop módon. A mezőgazdaság tele van olyan feladatokkal, amelyekre ezek az eszközök ideálisak.

### n8n: időjárási riasztások

Képzeld el a következő n8n workflow-t:

```
[Cron trigger: naponta 6:00]
       │
       ▼
[HTTP Request: Open-Meteo API]
  → 7 napos előrejelzés a gazdaság koordinátáira
       │
       ▼
[IF node: max_temp > 35°C VAGY 3_napos_csapadék_összeg > 50mm]
       │                    │
      IGEN                 NEM
       │                    │
       ▼                    ▼
[Telegram üzenet:         [Nincs teendő]
 "Figyelem! Hőhullám /
  heves csapadék várható.
  Részletek: ..."]
       │
       ▼
[Google Sheets: naplózás]
```

Ez a workflow 15 perc alatt összerakható, és naponta automatikusan figyelmeztet a szélsőséges időjárásra. A 8. fejezetben leírt elvek szerint: tartsd egyszerűnek, teszteld manuálisan, majd kapcsold élesbe.

Bővíthető változat:
- Az IF-feltételek személyre szabhatók kultúránként (a kukorica vízstressz-küszöbe más, mint a búzáé).
- Az előrejelzés kombinálható a talajnedvesség-szenzor aktuális értékével (IoT API-hívás).
- Heves csapadék előrejelzésnél automatikusan ellenőrzi, mely táblák fekszenek belvíz-veszélyes mélyedésben (domborzatmodellből előre kiszámolt kockázati térkép).

### KNIME: szenzor-adatok elemzése

A KNIME-ot a 8. fejezetben elsősorban laboradatok elemzésére használtuk. A mezőgazdasági alkalmazás nagyon hasonló:

1. **CSV Reader:** Talajnedvesség-szenzor naplófájljainak beolvasása.
2. **Missing Value:** Hiányzó mérések interpolálása (lineáris vagy spline).
3. **Time Series:** Napi átlagok, heti trendek kiszámítása.
4. **Joiner:** A szenzor-adatok összekapcsolása az időjárási adatokkal dátum alapján.
5. **Linear Regression / Random Forest:** A talajnedvesség-csökkenés mértékének modellezése a hőmérséklet és a szélsebesség függvényében.
6. **Interactive Chart:** Vizualizáció --- melyik szenzor mutat rendellenességet.

A KNIME ereje itt az, hogy a gazdálkodó (vagy az agronómus) látja a teljes feldolgozási folyamatot vizuálisan, és minden node-nál ellenőrizheti az adatot. Ez a 8. fejezetben hangsúlyozott átláthatósági elv mezőgazdasági alkalmazása.

---

## 17.7 RAG a mezőgazdasági tudásmenedzsmentben

Ahogy a 9. fejezetben részletesen tárgyaltuk, a Retrieval-Augmented Generation (RAG) lehetővé teszi, hogy egy nagy nyelvi modellt saját dokumentumaiddal „táplálj", és a válaszokat a te adataidra alapozva kapd.

### A gazdálkodó személyes tudásbázisa

Képzeld el, hogy Gábor az elmúlt öt évben a következő dokumentumokat halmozta fel:

- 47 talajvizsgálati jegyzőkönyv (PDF, különböző laboratóriumoktól)
- 5 éves hozamtérkép-adatsor (CSV-k és shapefile-ok összefoglalóival)
- 230 időjárási nap összefoglalója (saját feljegyzések)
- 15 szaktanácsadói jelentés (Word és PDF)
- Az összes permetezési és műtrágyázási napló (Excel)
- 3 belvízjelentés az önkormányzattól
- A gazdaság KAP-pályázati dokumentációja
- Gépkönyvek és szervizjegyzékek

Ezeket a dokumentumokat feltöltheti egy RAG-rendszerbe --- a 9. fejezetben ismertetett architektúra szerint: chunkolás, embedding, vektortárolás, retrieval, generálás. Ezután kérdéseket tehet fel természetes nyelven:

> „Melyik táblán volt a legmagasabb a nitrát-N szint a 2023-as őszi talajmintavételnél, és mit írt erre a szaktanácsadó?"

> „A 12-es tábla átlaghozama az elmúlt 5 évben hogyan viszonyul a gazdaság átlagához? Volt-e évjárathatás?"

> „A permetezési naplók szerint hányszor alkalmaztam gombaölő szert a búzán 2024-ben, és milyen készítménnyel?"

A RAG-rendszer nem „kitalálja" a választ --- hanem megkeresi a releváns dokumentumrészleteket, és azok alapján válaszol. Ez a 9. fejezetben hangsúlyozott hallucináció-csökkentő mechanizmus.

### Szabályozási dokumentumok RAG-ja

A magyar gazdálkodók egyre összetettebb szabályozási környezetben dolgoznak. A KAP 2023--2027-es ciklusa, az ökorendszerek, a Farm to Fork stratégia, a nitrátdirektíva, a növényvédelmi szabályozás --- ezek mind több száz oldalas dokumentumok, amelyeket a gazdálkodónak ismernie kellene, de senki sem olvassa el őket teljes terjedelmükben.

Egy RAG-rendszer, amelybe feltöltöd a releváns jogszabályokat és KAP-útmutatókat, lehetővé teszi:

> „Ha ökológiai minősítéssel rendelkezem és 200 hektárnál nagyobb gazdaságom van, milyen precíziós mezőgazdasági beruházásokra kaphatok támogatást, és mekkora a maximális támogatási intenzitás?"

> „A nitrátdirektíva szerint mennyi nitrogént juttathatók ki hektáronként és évente a 7-es táblán, ha az érzékeny területnek minősül?"

A válasz pontosan hivatkozik a forrás-dokumentumra és a releváns bekezdésre --- ahogy a 9. fejezetben tárgyalt forrásmegjelölési mechanizmus működik.

### Szaktudás-aggregáció: a „chatbot a farmról"

A legambiciózusabb alkalmazás: egy RAG-rendszer, amely az összes fenti adatforrást egyesíti --- talajvizsgálatok, hozamadatok, időjárás, szaktanácsadói vélemények, szabályozás --- és egyetlen felületen teszi elérhetővé. Ez nem pusztán keresőmotor; az LLM képes összekapcsolni különböző dokumentumokból származó információkat:

> „Tavaly a 3-as táblán alacsony volt a hozam. A talajvizsgálat magas pH-t mutatott (8.1). A szaktanácsadó foszforhiányt diagnosztizált. Az időjárás aszályos volt májusban. Ezek közül mi a legvalószínűbb fő ok, és mit tegyek az idén?"

---

## 17.8 Mezőgazdasági digitális ikrek

Ahogy a 10. fejezetben részletesen bemutattuk, a digitális iker egy fizikai rendszer számítógépes modellje, amelyet valós idejű adatokkal folyamatosan frissítenek. A mezőgazdaság különösen alkalmas terep a digitális ikreknek, mert egy tábla állapota sok mérhető változóval leírható, és a szimulációnak közvetlen gazdasági haszna van.

### A mezőgazdasági digitális iker komponensei

Egy szántóföldi digitális iker négy almodellt integrál:

**1. Növénynövekedési modell** (pl. DSSAT, APSIM, AquaCrop)
- Szimulálja a fotoszintézist, a légzést, a tápanyagfelvételt, a fenológiai fejlődést.
- Bemenetek: időjárás, talaj, fajta, gazdálkodási beavatkozások.
- Kimenet: napi biomassza, LAI, hozambecslés.

**2. Talajvízháztartási modell**
- Nyomon követi a talaj vízháztartási mérlegét: csapadék + öntözés - ET - mélyszivárgás - lefolyás.
- Különböző mélységekben modellez: felszín, gyökérzóna, altalaj.
- A talajnedvesség-szenzorokkal validálható és kalibrálható.

**3. Időjárási modell / előrejelzés**
- Rövid távú (1--7 nap): determinisztikus előrejelzés API-ról.
- Közepes távú (1--4 hét): ensemble-előrejelzés, bizonytalansággal.
- Szezonális (1--6 hónap): éghajlati forgatókönyvek.

**4. Gazdasági modell**
- Input-árak (műtrágya, vetőmag, növényvédő szer, üzemanyag, víz).
- Termény-árak (aktuális és forward-árak).
- A szimulált hozam és az input-felhasználás alapján jövedelmezőséget számol.

A 10. fejezetben leírt elvek szerint: a digitális iker nem egyetlen monolitikus modell, hanem moduláris rendszer, amelyet a valós adatok folyamatosan kalibrálnak.

### „Mi lenne, ha..." szimulációk

A digitális iker igazi ereje a szcenárió-elemzésben rejlik:

- *„Mi lenne, ha 20%-kal csökkenteném a nitrogén-fejtrágyát a 3-as zónában?"* → A modell szimulálja a hozamcsökkenést és a megtakarítást, és kiszámolja a nettó hatást.
- *„Mi lenne, ha két héttel korábban vetnék?"* → A modell a historikus időjárási adatokkal futtatva megmutatja a korábbi vetés hozamhatását és kockázatát.
- *„Mi lenne, ha öntöznék a kritikus virágzási periódusban, 30 mm/hét adaggal?"* → A modell összeveti az öntözés költségét a hozamnövekedéssel.

Az AquaCrop modell --- amelyet az FAO kifejezetten egyszerűnek és hozzáférhetőnek szántak --- különösen alkalmas a „mi lenne, ha" kérdések megválaszolására. Az AquaCrop a lombfedettséget használja fő állapotváltozóként (nem a LAI-t), ami csökkenti a kalibráláshoz szükséges paramétereket, és a gazdálkodó számára is érthetőbb.

### Az AI szerepe a digitális ikerben

Az AI három ponton kapcsolódik a digitális ikerhez:

1. **Automatikus kalibráció.** A növénynövekedési modell paramétereinek beállítása (pl. a fajta-specifikus fejlődési paraméterek) hagyományosan kézi munka. Optimalizációs algoritmusokkal (genetikus algoritmus, Bayesian optimalizáció --- a 6. fejezet témái) ez automatizálható.

2. **Valós idejű adatasszimiláció.** A szenzor-adatok és a modell-előrejelzés közötti eltérést az AI folyamatosan korrigálja. Ha a talajnedvesség-szenzor 5%-kal kevesebbet mutat, mint a modell jósol, az AI módosítja a modell állapotát.

3. **Forgatókönyv-generálás LLM-mel.** Ahelyett, hogy a gazdálkodónak kézzel kellene megadnia a „mi lenne, ha" paramétereket, természetes nyelven fogalmazhat:

```
Szimulálj három forgatókönyvet a 7-es tábla kukoricájára:
1. Jelenlegi gyakorlat (160 kg N/ha, öntözés nélkül)
2. Csökkentett nitrogén (120 kg N/ha) + hiányöntözés (virágzáskor 2x20 mm)
3. Jelenlegi nitrogén + teljes öntözési program (heti 25 mm júliustól)
Használd a 2022-es (aszályos) időjárást a legrosszabb forgatókönyvhöz.
```

Az LLM lefordítja a természetes nyelvű kérést a szimulációs modell paramétereire, lefuttatja a szimulációkat, és összefoglalja az eredményeket --- táblázatban és szöveges értelmezéssel.

---

## 17.9 AI-ágensek az autonóm gazdálkodásban

Ahogy a 11. és 12. fejezetben részletesen tárgyaltuk, az AI-ágensek önálló döntéshozatalra képes rendszerek, amelyek érzékelik a környezetüket, terveznek, és cselekszenek. A mezőgazdaság az ágensek egyik legtermészetesebb alkalmazási területe, mert a döntések ismétlődőek, időkritikusak, és nagy mennyiségű adat áll rendelkezésre.

### Multi-ágens rendszer az öntözésütemezéshez

Képzeljünk el egy multi-ágens rendszert, amelyben minden tábla rendelkezik egy saját „tábla-ágenssel":

```
┌────────────────────────────────────┐
│        FARM KOORDINÁTOR ÁGENS      │
│  (gazdaság-szintű optimalizáció)   │
│  - Vízkvóta elosztása              │
│  - Energia-optimalizáció            │
│  - Prioritás-kezelés               │
└────────────┬───────────────────────┘
             │
    ┌────────┼────────┬────────────┐
    ▼        ▼        ▼            ▼
┌────────┐┌────────┐┌────────┐┌────────┐
│Tábla-1 ││Tábla-2 ││Tábla-3 ││Tábla-N │
│ ágens  ││ ágens  ││ ágens  ││ ágens  │
│        ││        ││        ││        │
│Szenzor ││Szenzor ││Szenzor ││Szenzor │
│Modell  ││Modell  ││Modell  ││Modell  │
│Döntés  ││Döntés  ││Döntés  ││Döntés  │
└────────┘└────────┘└────────┘└────────┘
```

**Tábla-ágens működése:**
1. **Érzékelés:** Lekérdezi a talajnedvesség-szenzort, az időjárás-előrejelzést, a műholdas NDVI-t.
2. **Állapotbecslés:** A digitális iker modellel becsüli a növény aktuális vízstressz-szintjét.
3. **Döntés:** Ha a talajnedvesség a MAD (Management Allowable Depletion) küszöb alá süllyed, és az előrejelzés nem ígér elég csapadékot, öntözést kér.
4. **Kommunikáció:** Az öntözési igényt jelenti a koordinátor-ágensnek.

**Koordinátor-ágens működése:**
1. **Összegyűjti** az összes tábla-ágens igényét.
2. **Optimalizál:** Ha egyszerre három tábla kér öntözést, de a szivattyúkapacitás csak kettőre elég, a koordinátor a növények vízstressz-érzékenysége és a fenológiai fázis alapján prioritást szab. A kukorica virágzáskor kritikusabb, mint a búza érés végén.
3. **Ütemez:** Elkészíti az öntözési menetrendet, amely minimalizálja az energiaköltséget (éjszakai öntözés, amikor az áramár alacsonyabb).
4. **Végrehajt:** Parancsot küld az öntözőrendszer vezérlőjének, vagy riasztást küld a gazdálkodónak, ha kézi beavatkozás szükséges.

Ez a 11. fejezetben leírt multi-ágens architektúra mezőgazdasági alkalmazása. A megerősítéses tanulás --- amelyet a precíziós mezőgazdasági szakirodalom is tárgyal --- itt úgy működik, hogy az ágens próba és hiba útján (szimulációban, nem a valós táblán!) megtanulja az optimális öntözési stratégiát: a jutalomfüggvény a hozam és a vízmegtakarítás kombinációja.

### Kártevő-reagáló ágens

Egy másik ágens-típus a kártevő-reagáló rendszer:

1. **Detekciós ágens:** Drónfelvételek és terepi kamerák képeit elemzi CNN-modellel. Ha anomáliát talál, riasztást küld.
2. **Diagnosztikai ágens:** A riasztás alapján összegyűjti a kontextust (időjárási adatok, korábbi kártevő-előfordulások, szomszédos táblák állapota), és LLM-alapú értelmezéssel azonosítja a legvalószínűbb kórokozót/kártevőt.
3. **Beavatkozási ágens:** A diagnózis alapján javaslatot tesz: melyik készítménnyel, milyen dózisban, melyik területen permetezzünk. Figyelembe veszi a szabályozási korlátokat (várakozási idő, nitrátérzékeny terület, méhek védelme).
4. **Végrehajtási ágens:** A jóváhagyott tervet a változó dózisú permetező vezérlőjébe tölti, vagy a drónpermetezőt programozza.

Ahogy a 12. fejezetben hangsúlyoztuk: a human-in-the-loop elv a mezőgazdaságban különösen fontos. Egyetlen ágens sem dönthet önállóan egy növényvédő szer kijuttatásáról --- a gazdálkodó jóváhagyása minden kritikus ponton szükséges.

---

## 17.10 Magyar precíziós mezőgazdaság: helyzet és lehetőségek

### A magyar kontextus

Magyarország egyedülálló helyzetben van a precíziós mezőgazdaság szempontjából. Az Alföld --- Európa egyik legnagyobb összefüggő síksága --- csernozjom és réti talajokkal, ideális a nagyüzemi szántóföldi gazdálkodásnak. A sík terep kedvez a gépesítésnek és a precíziós technológiáknak. Ugyanakkor a víz a kritikus korlátozó tényező: az éves csapadék az Alföld középső részein mindössze 500 mm körüli, és a változékonyság drámai. A 2022-es aszály katasztrofális kukoricahozamokat eredményezett, ami nyomatékosan jelezte a precíziós vízgazdálkodás szükségességét.

A birtokszerkezet polarizált: kevés nagyüzem (az egykori szövetkezeti gazdaságok utódai) műveli a terület zömét, miközben sok kistermelő néhány hektáros parcellákon gazdálkodik. A precíziós mezőgazdaság gazdaságtana a nagyobb léptéket részesíti előnyben --- de az AI-eszközök demokratizáló hatása ezt a képletet kezdi megváltoztatni.

Az RTK korrekciós hálózat 2023-ra mintegy 3000 mezőgazdasági gépet szolgált ki, hozzávetőleg 1,2 millió hektárt lefedve --- a teljes művelt terület több mint negyedét. Ez a centiméteres pontosságú helymeghatározás az automata kormányzás, az állandó nyomsávos gazdálkodás és a precíziós vetés alapja.

### Debrecen és az Alföld kutatóközpontjai

A **Debreceni Egyetem** Mezőgazdaság-, Élelmiszer-tudományi és Környezetgazdálkodási Kara a precíziós növénytermesztési kutatás úttörője az Alföldön. Kiterjedt szántóföldi kísérleteik a kukorica és a búza változó dózisú nitrogén-kijuttatásáról azt a helyi bizonyítékbázist teremtik meg, amelyre a magyar gazdálkodóknak a technológia elfogadásához szükségük van. Debrecen szerepe az AI-mezőgazdaság kontextusában azért különösen fontos, mert a gyakorlati kísérletezés és az adattudomány itt találkozik: a kísérleti adatokat egyre inkább gépi tanulási modellekkel elemzik, és a változó dózisú kijuttatási térképeket ML-algoritmusokkal optimalizálják.

A **MATE** (Magyar Agrár- és Élettudományi Egyetem) precíziós mezőgazdasági szakirányú továbbképzést kínál, amely integrálja a távérzékelést, a térinformatikát, a drónüzemeltetést és a gazdaságirányítási információs rendszereket. A **Szegedi Tudományegyetem** a drónos alkalmazásokat állította precíziós mezőgazdasági tantervének középpontjába.

A **KITE Zrt.** --- az ország vezető mezőgazdasági integrátora --- a PGR (Precíziós Gazdálkodási Rendszer) nevű integrált platformot fejlesztette ki, amely összegyűjti a szántóföldi műveletek gépadatait, döntéstámogató algoritmusokon dolgozza fel, és közvetlenül felhasználható ajánlásokat ad. A KITE hálózata az Alföld jelentős részét lefedi.

### A Hortobágy és a Hajdúság: ahol az AI-nak dolgoznia kell

A Hortobágy és a Hajdúság térsége koncentráltan mutatja a magyar precíziós mezőgazdaság minden kihívását:

- **Belvíz:** A sík terepen a mikromélyedésekben összegyűlő víz hetekig elborítja a táblákat. Nagy felbontású domborzatmodellek (drónos fotogrammetria, LiDAR) azonosítják a kockázatos területeket. Az AI hozzáadott értéke: a domborzat, a talaj-EC, a historikus belvízjelentések és az időjárás-előrejelzés kombinálásával prediktív belvízkockázati térkép készíthető, amely előre figyelmezteti a gazdálkodót.

- **Szikesedés:** Az Alföld egyes területein a szolonyec (szikes) talajok természetes előfordulása mellett a másodlagos szikesedés is probléma. A talaj-EC-felmérés térképezi a kiterjedést, de az AI a Sentinel-2 idősorokkal és a talajadatokkal kombinálva finomabb zonációt adhat.

- **Aszálystressz:** A 2022-es tapasztalatok alapján az aszály-előrejelzés és a hiányöntözés optimalizálása létfontosságú. Az AquaCrop modell --- a magyar kutatásban is használt eszköz --- különösen alkalmas a víztermelékenység-elemzésre.

- **Munkaerőhiány:** Az aratási idényben a napszámok elérik a 15 000 forintot, és az idénymunkások egyre inkább külföldi munkát választanak. Az autonóm gépek és az AI-alapú döntéstámogatás itt nem luxus, hanem szükségszerűség.

### Lehetőségek az AI-korszakban

A magyar precíziós mezőgazdaság előtt álló legnagyobb lehetőségek:

1. **A kis- és közepes gazdaságok bevonása.** Az AI-eszközök demokratizáló hatása --- a ChatGPT-alapú agronómiai tanácsadástól a nyílt forráskódú drone-feldolgozó szoftverekig --- csökkenti a belépési küszöböt. A „precíziós mezőgazdaság mint szolgáltatás" modell (ahol a gazdálkodó nem a drónot vásárolja meg, hanem a szolgáltatást) további lépés ebben az irányban.

2. **Az adatinteroperabilitás megoldása.** A John Deere traktor, a DJI drón és a harmadik féltől származó gazdaságirányítási szoftver közötti adatáramlás jelenleg akadozik. Az AI-ágensek --- ahogy a 11. fejezetben tárgyaltuk --- hidat képezhetnek: egy intelligens middleware automatikusan konvertálja és integrálja a különböző forrásokból érkező adatokat.

3. **Az öntözésfejlesztés felgyorsítása.** A kormányzati programok célja az öntözött terület bővítése. A precíziós öntözés --- talajnedvesség-szenzorok, változó dózisú szabályozás, AI-alapú ütemezés --- biztosítja, hogy minden csepp víz hatékonyan hasznosuljon.

4. **KAP-támogatások maximalizálása.** A VP2-4.1.8-21 pályázati program precíziós mezőgazdasági beruházásokat finanszíroz, 50-65%-os támogatási intenzitással. Az AI-eszközök (gazdaságirányítási szoftverek, döntéstámogató rendszerek) közvetlenül támogathatók ebből a keretből.

5. **A körforgásos gazdasági modell erősítése.** A precíziós tápanyag-gazdálkodás csökkenti a műtrágya-pazarlást, a precíziós permetezés a növényvédőszer-felhasználást. Ez összhangban áll az EU Farm to Fork stratégiájával, és hosszú távon javítja a talajminőséget --- ami az intenzív művelés évtizedei után a magyar talajok egy részén kritikus kérdés.

---

## 17.11 Gyakorlati feladatok

### 1. feladat: NDVI-idősor elemzése és értelmezése

**Cél:** Műholdas vegetációs index idősor feltáró elemzése és AI-asszisztált értelmezése.

**Eszközök:** Bármely AI-chat (Claude, ChatGPT), opcionálisan KNIME vagy Python.

**Lépések:**

1. Töltsd le a Google Earth Engine-ből vagy a Copernicus Open Access Hub-ról a Sentinel-2 NDVI-idősorod egy kiválasztott mezőgazdasági táblára (ha nincs saját, használj egy nyilvánosan elérhető mintaterületet, pl. a Debreceni Egyetem kísérleti telepét).

2. Készíts egy táblázatot a kéthetenkénti átlagos NDVI-értékekkel (ha 3-5 kezelési zónára osztod a táblát, még jobb).

3. Tölsd fel az adatokat egy AI-chatbe a következő prompttal:
   ```
   Az alábbi adatok egy [növényfaj] tábla NDVI-idősorát mutatják
   [év] [hónaptól-hónapig], [helyszín]. Elemezd a fenológiai
   görbét minden zónára. Azonosíts anomáliákat, és adj agronómiai
   értelmezést. Milyen kiegészítő adatokra lenne szükség a
   pontosabb diagnózishoz?
   ```

4. Értékeld az AI válaszát: mennyire helytálló az agronómiai értelmezés? Kérdezz vissza a bizonytalan pontokon.

**Értékelési szempont:** Nem az AI-válasz pontossága a lényeg, hanem az, hogy megtanuld a hatékony promptolást mezőgazdasági kontextusban (2. fejezet), és kritikusan értékeld az AI-javaslatokat.

---

### 2. feladat: Hozamtérkép-tisztító szkript írása AI kódolási asszisztenssel

**Cél:** Automatizált hozamtérkép-tisztítás Python-szkripttel, AI-asszisztens segítségével.

**Eszközök:** Claude Code vagy GitHub Copilot, Python (geopandas, shapely).

**Lépések:**

1. Keress egy nyilvánosan elérhető nyers hozamtérképet (pl. az USDA Ag Data Commons-ról, vagy generálj szintetikus adatot).

2. Kérd meg az AI-asszisztenst, hogy írjon tisztítószkriptet a 17.5-ös szakaszban leírt lépések szerint.

3. Futtasd a szkriptet, és vizualizáld az eredményt: a nyers és a megtisztított hozamtérkép egymás mellé helyezve.

4. Módosítsd a paramétereket (szórásküszöb, sebességhatárok) és figyeld meg, hogyan változik az eredmény.

5. Dokumentáld a tapasztalataidat: melyik tisztítási lépés távolította el a legtöbb pontot? A maradék térkép agronómiailag ésszerű?

**Értékelési szempont:** A 5. fejezetben tanult iteratív fejlesztési folyamat alkalmazása: kérés → eredmény → javítás → újra futtatás.

---

### 3. feladat: Időjárási riasztó workflow n8n-nel

**Cél:** Automatikus időjárási riasztó rendszer felépítése vizuális programozással.

**Eszközök:** n8n (self-hosted vagy cloud), Open-Meteo API, Telegram vagy e-mail.

**Lépések:**

1. Telepítsd az n8n-t (a 8. fejezet útmutatása szerint).

2. Építsd meg a 17.6-os szakaszban leírt workflow-t: Cron trigger → Open-Meteo API → IF-elágazás → értesítés.

3. Bővítsd a workflow-t:
   - Adj hozzá egy fagyveszély-riasztást (min_temp < 0°C áprilisban-májusban).
   - Adj hozzá egy aszálystressz-indexet: ha az elmúlt 14 nap csapadékösszege < 10 mm ÉS a max_temp > 30°C, riasszon.
   - Naplózz minden riasztást egy Google Sheets táblázatba.

4. Futtasd a workflow-t egy hétig, és értékeld: mennyi volt a valódi riasztás és a „hamis pozitív"?

**Értékelési szempont:** A 8. fejezetben tanult no-code automatizálási elvek alkalmazása valós mezőgazdasági kontextusban.

---

### 4. feladat: RAG-rendszer gazdálkodási dokumentumokra

**Cél:** Személyes tudásbázis felépítése saját (vagy minta-) mezőgazdasági dokumentumokból.

**Eszközök:** Bármely RAG-platform (a 9. fejezetben tárgyaltak közül), pl. AnythingLLM, PrivateGPT, vagy egy felhőalapú megoldás.

**Lépések:**

1. Gyűjts össze 5-10 mezőgazdasági dokumentumot:
   - Talajvizsgálati jegyzőkönyvek (ha nincs sajátod, keress mintadokumentumot a Nemzeti Élelmiszerlánc-biztonsági Hivatal weboldaláról)
   - Egy KAP-ökorendszer útmutató részlet
   - Egy növényvédelmi szabályozási kivonat
   - Időjárási összefoglaló egy tenyészidőszakról

2. Tölsd fel a dokumentumokat a RAG-rendszerbe.

3. Tesztelj 10 kérdéssel, amelyek:
   - Egyetlen dokumentumból megválaszolhatók (pl. „Mekkora volt a 3-as tábla pH-ja?")
   - Több dokumentum összekapcsolását igénylik (pl. „A talajvizsgálat alapján van-e kockázata a nitrát-kimosódásnak a 2-es táblán, figyelembe véve az éves csapadékot?")
   - A rendszer korlátait tesztelik (pl. „Milyen fajta kukoricát vetek jövőre?" --- ahol a dokumentumokban nincs erről szó)

4. Dokumentáld: hány kérdésre adott helyes választ? Hol hallucrinált?

**Értékelési szempont:** A 9. fejezetben tanult RAG-architektúra működésének megértése és a hallucináció-felismerés gyakorlása.

---

### 5. feladat: Egyszerű öntözési döntéstámogató modell

**Cél:** A talaj vízmérlegén alapuló öntözés-ütemezési modell megépítése AI-asszisztens segítségével.

**Eszközök:** Claude Code vagy ChatGPT Code Interpreter, Python.

**Lépések:**

1. Kérd meg az AI-asszisztenst:
   ```
   Írj Python-programot, amely implementálja az FAO-56 talajvízháztartási
   mérleg módszert öntözés-ütemezésre. A modell:
   - Napi lépésekben számol.
   - Bemenet: napi hőmérséklet (min, max), csapadék, szélsebesség,
     napsugárzás, páratartalom.
   - Kiszámolja ET0-t Penman-Monteith-tel.
   - A növénytényezőt (Kc) a fenológiai fázis alapján határozza meg
     (kukorica: Kc_ini=0.3, Kc_mid=1.2, Kc_end=0.35).
   - Nyomon követi a talaj vízháztartási mérlegét (mezei vízkapacitás,
     hervadáspont, MAD=50% megadható).
   - Ha a kimerülés eléri a MAD-ot, öntözést javasol a mezei
     vízkapacitás feltöltéséig.
   - Készít grafikont: talajnedvesség idősor, ET, csapadék, öntözés.
   ```

2. Futtasd a modellt valós vagy szintetikus időjárási adatokkal egy teljes tenyészidőszakra.

3. Kísérletezz: hogyan változik az öntözési igény, ha a MAD-ot 30%-ra csökkented (érzékenyebb kultúra) vagy 60%-ra emeled (aszálytűrőbb fajta)?

4. Bővítsd: adj hozzá egy 5 napos előrejelzés-modult, amely a következő napok várható csapadéka alapján elhalasztja az öntözést, ha jelentős eső várható.

**Értékelési szempont:** A 6. fejezetben tanult modellezési elvek alkalmazása, a 10. fejezetben tárgyalt „mi lenne, ha" gondolkodás, és az 5. fejezetben gyakorolt AI-asszisztens-alapú kódfejlesztés kombinálása.

---

## Összefoglalás

A mesterséges intelligencia nem egy újabb gép a traktormúzeumban --- hanem egy új réteg, amely a precíziós mezőgazdaság minden meglévő elemét hatékonyabbá teszi. A műholdfelvételt nem csak letöltjük, hanem automatikusan értelmezzük. A szenzor-adatot nem csak gyűjtjük, hanem anomáliákat keresünk benne. A hozamtérképet nem csak kinyomtatjuk, hanem gépi tanulással elemezzük és jövőbeli hozamot jelzünk előre belőle. A döntéstámogató rendszert nem csak konzultáljuk, hanem autonóm ágenseket bízunk meg a rutin döntések végrehajtásával.

A magyar mezőgazdaság --- az Alföld csernozjom talajától a Hortobágy belvizes mélyedésein át a debreceni kutatóhelyekig --- ideális terepe ennek a transzformációnak. A kihívások valósak: aszály, belvíz, szétaprózott birtokszerkezet, képzett munkaerő hiánya, vidéki internetkapcsolat korlátai. De az eszközök is elérhetők: ingyenes Sentinel-2 felvételek, nyílt forráskódú AI-modellek, megfizethető IoT-szenzorok, és --- talán a legfontosabb --- azok a prompttervezési, adatelemzési és automatizálási készségek, amelyeket ennek a könyvnek az előző fejezeteiben sajátítottál el.

A precíziós mezőgazdaság nem a tehetős nagyüzemek kiváltsága. Az AI-eszközök demokratizáló hatása, a „precíziós szolgáltatás" üzleti modellek és az EU támogatási programok együttesen nyitnak utat ahhoz, hogy a technológia előnyei a kisebb gazdaságokhoz is eljussanak. Gábornak hatszáz hektáron is segít az AI --- de a szomszéd Jánosnak, aki ötven hektáron gazdálkodik, az okostelefonos kártevő-felismerés és az automatikus időjárási riasztás éppúgy napi szintű hasznot hoz.

A következő lépés a tiéd: válaszd ki az öt gyakorlati feladat közül azt, amelyik a legközelebb áll a saját szakterületedhez vagy érdeklődésedhez, és próbáld ki. A legjobb tanulás a cselekvéssel kezdődik --- a szántóföldön éppúgy, mint a terminálban.
