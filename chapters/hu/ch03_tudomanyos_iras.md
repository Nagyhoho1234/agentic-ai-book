# 3. fejezet: AI a tudományos írásban és kommunikációban

> **Fejezet-informacio**
> - **Kinek szol:** Kutatoknak es hallgatoknak, akik angol nyelvu cikkeket, palyazatokat vagy disszertaciot irnak
> - **Eloismeretek:** 2. fejezet (promptolasi alapok)
> - **Amit megtanulsz:**
>   - AI-val tamogatott irodalomattekintes es reskutatas
>   - Kezirat szerkesztese, stilisztikai csiszolasa es lektoralasa AI-val
>   - Biraloi valaszok es tudomanyos kommunikacio keszitese
> - **Szukseges eszkozok:** Browser only
> - **Kapcsolodo fejezetek:** 2. fejezet (promptolas), 16. fejezet (etika es szerzoi integritas)

## Nyitó jelenet: Hajnali három, és a határidő holnap van

Képzeld el a következő helyzetet. Nóra, egy debreceni környezettudományi kutató, három éve dolgozik a Tisza mikroplasztik-szennyezettségéről szóló kutatásán. Az eredmények megvannak, az adatok tiszták, a konklúzió erős. De a kéziratot az *Environmental Science & Technology*-nak kell benyújtania — angolul, anyanyelvi szinten, a folyóirat sajátos formátumában és hangnemében. Nóra angolul jól olvas, konferenciákon előad, de egy 8000 szavas kézirat stilisztikai csiszolása más kategória. A professzionális lektorálás 400-800 euró, a határidő pedig holnap.

Nóra nincs egyedül. A világ kutatóinak többsége nem angol anyanyelvű, mégis egy angol nyelvű publikációs rendszerben kell helytállniuk. Ez az egyenlőtlenség évtizedek óta létezik — de 2024-től kezdve drasztikusan csökkent. Az AI-alapú nyelvi eszközök ma már nem egyszerűen nyelvtani hibákat javítanak: átstrukturálják az érvelést, igazítják a hangnemet a célfolyóirathoz, és percek alatt elvégzik azt, amire korábban napokat kellett szánni.

Ez a fejezet végigvezet a tudományos írás és kommunikáció teljes folyamatán — az irodalomáttekintéstől a kézirat megírásán és a bírálói válaszokon át a tudománynépszerűsítésig —, és megmutatja, hol és hogyan használhatod az AI-t hatékonyan, felelősen, és a saját tudományos hangod megőrzésével.

---

## 3.1 Irodalomáttekintés AI-val

### A probléma mérete

Naponta több mint 4000 új orvos-biológiai cikk jelenik meg. A természettudományok más területein sem jobb a helyzet. Egy átfogó irodalomáttekintés, ami 15 éve még egy-két hét intenzív munkával megoldható volt, ma fizikailag lehetetlen kézzel elvégezni. Nem azért, mert a kutatók lustábbak lennének — egyszerűen több a publikáció, mint amennyit emberi szem képes feldolgozni.

Az AI nem helyettesíti a kritikus olvasást, de drámaian felgyorsítja az előszűrést: segít megtalálni a releváns cikkeket, összefoglalni a tartalmakat, kiemelni a kulcsmegállapításokat, és ami a legértékesebb — feltárni a diszciplínák közötti kapcsolatokat.

### Cikkek összefoglalása

A legkézenfekvőbb felhasználás: feltöltesz egy PDF-et, és kérsz egy összefoglalót. De az eredmény minősége drámaian függ a prompt minőségétől. Íme egy hatékony megközelítés:

> **Prompt:** *„Foglald össze ezt a cikket a következő struktúrában: (1) Fő kutatási kérdés, (2) Alkalmazott módszer, (3) Legfontosabb 3 eredmény számszerű adatokkal, (4) A szerzők által elismert korlátok, (5) Hogyan kapcsolódik ez a [saját kutatási témád] területéhez."*

Ez a „strukturált összefoglalás" technika sokkal informatívabb eredményt ad, mint az egyszerű „foglald össze" kérés, mert az AI-t arra kényszeríti, hogy a számodra releváns dimenziók mentén dolgozza fel a szöveget.

**Gyakorlati példa — progresszív promptolás:**

Tegyük fel, hogy a Tisza vízgyűjtőjének mikroplasztik-szennyezettségéről írsz review cikket. Kezdheted általánosan:

> *„Foglald össze ennek a cikknek a fő megállapításait az édesvízi mikroplasztik-kutatás szempontjából."*

Majd szűkíted:

> *„Milyen mintavételi módszert használtak? Hogyan viszonyul ez a Manta trawl technikához, amit mi alkalmazunk?"*

És tovább mélyítesz:

> *„Milyen részecskeméret-tartományt vizsgáltak? Van adat a 100 mikron alatti frakciókról?"*

Ez a progresszív promptolás — általánosról a specifikusra haladva — sokkal mélyebb megértést ad, mint egyetlen kérdés.

### Kulcsmegállapítások kiemelése

Amikor sok cikket kell gyorsan áttekintened, az AI „szkennelő" képessége különösen hasznos:

> **Prompt:** *„Ebből a 10 cikkből (címek felsorolva) melyik tartalmaz konkrét adatot a következőkre: (a) édesvízi mikroplasztik koncentráció mg/L-ben, (b) domináns polimer típusok, (c) szezonális változékonyság? Készíts összefoglaló táblázatot."*

Az LLM képes a „skimming and scanning" stratégiát alkalmazni — gyorsan azonosítja a főbb pontokat (skimming), majd konkrét adatokat keres (scanning). Ahogy Han és szerzőtársai (2024) megállapították, ez a képesség különösen hasznos az irodalomáttekintés szűrési fázisában, amikor 50-100 cikk relevanciáját kell eldöntened.

> **Ne csinalld!**
> Ne engedd, hogy az AI irja meg a keziratod erdemben uj reszet (bevezetes, targyalas, konkluzio) a te kozremeukodésed nelkul. Az AI remek szerkeszto, stilisztikai tanaacsado es osszefoglalo — de ha a gondolatmenetet is o irja, az a te tudomanyos hangod eltuneseet jelenti, es a biralok ezt eszik meg fogjak. Hasznald szerkesztesre, ne szerzosegre.

### Kutatási rések azonosítása

Ez az AI egyik legértékesebb képessége az irodalomfeldolgozásban — és egyben az egyik legkockázatosabb. Kérheted:

> **Prompt:** *„A mellékelt öt cikk alapján milyen kutatási kérdések maradtak megválaszolatlanul az édesvízi mikroplasztik ökotoxikológiájában? Különösen érdekelnek a közép-európai édesvízi rendszerekre vonatkozó hiányok."*

Az AI válasza jellemzően releváns és jól strukturált lesz, de két fontos figyelmeztetéssel:

1. **Az AI meglévő tudást aggregál, nem generál valódi innovációt.** A javasolt „rések" többsége az adott terület szakértői számára már ismert. Ne várd, hogy az AI forradalmi kutatási irányokat javasol — inkább arra használd, hogy szisztematikusan feltérképezd, amit már mások is látnak.

2. **A hallucinációs kockázat itt különösen magas.** Az AI „kutatási rés"-nek tüntethet fel valamit, amit valójában már részletesen vizsgáltak — csak éppen nem volt a kontextusablakában az a cikk. Mindig ellenőrizd a javasolt réseket a Scopus, Web of Science vagy Google Scholar segítségével.

### Diszciplínák közötti kapcsolatok feltárása

A szemantikus elemzésen alapuló AI eszközök itt mutatják a legnagyobb erejüket. A hagyományos kulcsszavas keresés megköveteli, hogy ismerd a megfelelő terminológiát — de mi van, ha egy másik tudományterületen ugyanazt a problémát teljesen más szavakkal írják le?

Klasszikus példa: a „mikroplasztik transzport folyóvizekben" témát a hidrológusok az áramlástani modellezés nyelvén tárgyalják, a biológusok az ökoszisztéma-hatások felől közelítik, az anyagtudósok a polimer degradáció szemszögéből vizsgálják. Egy ember nehezen látja át mind a három perspektívát — az AI viszont képes ezeket összekapcsolni.

> **Prompt:** *„A mikroplasztik transzport folyóvizekben témát három különböző diszciplína vizsgálja: hidrológia, akvatikus ökológia és polimertudomány. Azonosíts 3-3 kulcscikket mindegyik területről, amelyek módszertani megközelítése kombinálható lenne egy interdiszciplináris kutatási projektben."*

Ahogy az OECD (2023) jelentése is kiemeli, a szemantikus elemzésen alapuló eszközök képesek olyan releváns cikkeket is megtalálni, amelyeket a kulcsszavas keresés elvétene — éppen azért, mert megértik a szöveg *jelentését*, nem csak a benne szereplő szavakat.

**Tipp:** Olyan AI-alapú irodalomkereső eszközök, mint a Semantic Scholar, Elicit, Consensus vagy a Connected Papers, kimondottan erre a célra készültek. Használd ezeket a hagyományos adatbázisok (Scopus, Web of Science) kiegészítéseként, nem helyettesítéseként.

> **🌾 Szakterületi példa: Tudáskinyerés a mezőgazdasági szakirodalomból**
>
> A mezőgazdasági kutatásban évente több ezer tudományos cikk jelenik meg a növénytermesztésről, és egyetlen kutató képtelen mindezt feldolgozni. Az NLP-rendszerek képesek ezekből strukturált tudást kinyerni — például a konkrét tápanyag-dózis és hozamválasz összefüggéseket (pl. „a cink 0,5%-os lombtrágyaként történő kijuttatása 12%-kal növelte a búzahozamot meszes talajokon") — és kereshető tudásbázisba rendezni. Ez a tudásbázis a döntéstámogató rendszerek és a kutatói irodalomfeldolgozás alapja: a fenti diszciplínák közötti kapcsolatok feltárásának agrár-specifikus megvalósulása.
>
> *Forrás: precagri 15.7.2 „Tudáskinyerés és döntéstámogatás"*

---

## 3.2 Kézirat írása és szerkesztése

### Nyelvi javítás: több mint nyelvtanellenőrzés

A legkézenfekvőbb és talán legértékesebb felhasználás: a kézirat nyelvi csiszolása. De az AI nem egyszerűen egy fejlettebb Grammarly — alapvető különbség, hogy *megmagyarázza* a javításait.

> **Prompt:** *„Olvasd el az alábbi szöveget. Azonosíts minden hibát, következetlenséget, nyelvtani problémát, szokatlan kifejezést és nehézkes mondatot. Javasolj javításokat, és mindegyiknél magyarázd el részletesen, miért szükséges a változtatás."*

Ez a „javíts és magyarázd" megközelítés nem csak jobb szöveget eredményez — tanulási eszközként is működik. Minden egyes javításnál megérted, *miért* volt rossz az eredeti megfogalmazás, és legközelebb már nem követed el ugyanazt a hibát. Ahogy Han és szerzőtársai (2024) rámutattak, ez alapvetően különbözik a hagyományos nyelvtanellenőrzőktől és parafrázis-eszközöktől, amelyek egyszerűen átírják a szöveget magyarázat nélkül.

**Gyakorlati példa:**

*Eredeti szöveg:*
> „The concentration of microplastics was measured in the water samples which were collected from five different locations of the Tisza river during the summer period of 2024."

*AI javítás:*
> „Microplastic concentrations were measured in water samples collected from five locations along the Tisza River during summer 2024."

*Magyarázat:* (1) „The concentration" → „Concentrations" — tudományos szövegben a többes szám pontosabban tükrözi, hogy több mintáról van szó. (2) „which were collected" → „collected" — a vonatkozói mellékmondat feleslegesen nehezíti a mondatot; a participiális szerkezet tömörebb. (3) „five different locations" → „five locations" — a „different" redundáns, mert öt helyszín nyilvánvalóan különböző. (4) „of the Tisza river" → „along the Tisza River" — az „along" földrajzi kontextusban természetesebb, és a folyóneveknél a „River" nagybetűs. (5) „during the summer period of 2024" → „during summer 2024" — tömörebb, a „period" felesleges.

Egyetlen mondat — öt javítás, mindegyik mögött konkrét stilisztikai vagy nyelvtani indok. Ha ezt 30 oldalon végigcsinálod, nemcsak jobb kéziratod lesz, hanem jobb íróvá is válsz.

### Az érvelés átstrukturálása

Nemcsak a mondatok szintjén, hanem a bekezdések és fejezetek szintjén is kérhetsz segítséget:

> **Prompt:** *„Az alábbi Discussion szekció három fő megállapítást tárgyal, de a logikai íve nem világos. Strukturáld át úgy, hogy: (1) a legfontosabb eredménnyel kezdődjön, (2) minden megállapításnál először az eredmény, aztán az irodalmi kontextus, végül az implikáció legyen, (3) az utolsó bekezdés a kutatás korlátaival és jövőbeli irányokkal zárjon."*

Az AI különösen jó az ilyen makro-szintű szerkezeti problémák megoldásában, mert a kontextusablakában egyszerre látja az egész szekciót, és képes az összefüggéseket a szövegen belül újrarendezni.

### Érthetőség javítása

A tudományos szöveg egyik legnagyobb csapdája a „curse of knowledge" — annyira benne vagy a témában, hogy nem veszed észre, amit neked magától értetődő, az az olvasó számára érthetetlen. Az AI külső szemként tud funkcionálni:

> **Prompt:** *„Olvasd el ezt az Abstract-ot egy olyan biológus szemével, aki nem foglalkozik mikroplasztik-kutatással. Jelöld meg azokat a kifejezéseket vagy mondatokat, amelyek extra háttértudást igényelnek, és javasolj egyszerűbb megfogalmazást."*

### A hangnem igazítása különböző folyóiratokhoz

Egy *Nature*-be szánt cikk hangnemben, struktúrában és terjedelemben gyökeresen különbözik egy *Water Research*-be írt szakcikktől. Az AI képes az adaptációra:

> **Prompt:** *„Írd át ezt az Introduction-t úgy, hogy megfeleljen a Nature Communications stílusának: szélesebb kontextussal indítson, ne legyen túl technikai az első két bekezdés, és a kutatási kérdés társadalmi relevanciáját is jelenítse meg."*

**Fontos figyelmeztetés:** az AI-val átírt szöveg soha nem a végleges verzió. A te szakértői ítéleted nélkülözhetetlen — az AI nem ismeri a te specifikus eredményeidet, a terület aktuális vitáit, vagy a bírálók várható kifogásait. Használd az AI-t mint egy rendkívül gyors és türelmes szerkesztőt, de a végső szó mindig a tiéd.

### Fordítás és nyelvi akadályok lebontása

Külön kiemelendő, hogy az LLM-ek a fordításban is felülmúlják a hagyományos fordítóeszközöket (Google Translate, DeepL), különösen a szakterminológia kezelésében. Han és szerzőtársai (2024) összehasonlító tesztjei szerint a GPT-4 konzisztensebb és pontosabb fordítást adott szakszövegek esetén, mint bármelyik mainstream fordító.

**Tipp nem angol anyanyelvű kutatóknak:** Írd meg a kézirat első vázlatát magyarul, aztán fordíttasd és csiszoltasd az AI-val. Ezt követően a „javíts és magyarázd" módszerrel finomítsd tovább. Ez a kétlépéses folyamat sokkal természetesebb végeredményt ad, mintha közvetlenül angolul próbálnál fogalmazni.

Sőt, a promptjaidat is írhatod magyarul — az LLM-ek hasonló minőségű választ adnak, függetlenül attól, milyen nyelven írod a kérést.

---

## 3.3 Hatásos cikkcímek készítése

### Miért számít a cím?

A cím az első — és gyakran az egyetlen — dolog, amit egy potenciális olvasó lát. Egy jó cím tömör, informatív, és felkelti az érdeklődést. Egy rossz cím eltemethet egy egyébként kiváló kutatást. A hagyományos címadás időigényes, iteratív folyamat — az AI ezt néhány másodpercre csökkenti, és kreatív kiindulópontot ad.

### A módszer

> **Prompt:** *„Az alábbi kézirat-vázlat alapján javasolj 10 különböző címet a következő stílusokban: 3 formális, leíró címet; 3 kreatív, figyelemfelkeltő címet metaforával vagy szójátékkal; 2 kérdés formájú címet; 2 „kettőspontost" címet (alcímmel). A kutatás a Tisza folyó mikroplasztik-szennyezettségéről szól."*

### Példák: előtte és utána

| # | Eredeti (gyenge) cím | AI-asszisztált cím | Mi változott? |
|---|---|---|---|
| 1 | „Study of Microplastic Pollution in the Tisza River" | „Microplastic transport in the Tisza River: Seasonal dynamics and polymer-specific accumulation in a Central European watershed" | A „Study of..." semmitmondó. Az új cím megmondja, *mit* vizsgáltak (transzport, szezonalitás, polimer-specifikus akkumuláció) és *hol* (közép-európai vízgyűjtő). |
| 2 | „Investigation of Microplastics in River Water Samples" | „Drifting hazards: Microplastic abundance and composition along 500 km of the Tisza River" | A „Drifting hazards" metafora felkelti az érdeklődést, miközben a szám (500 km) konkréttá teszi a kutatást. |
| 3 | „The Presence of Microplastic Particles in the Tisza" | „How polluted is Central Europe's forgotten river? A microplastic survey of the Tisza from source to confluence" | A kérdés forma meghívja az olvasót, a „forgotten river" érzelmeket kelt, a „source to confluence" a kutatás léptékét jelzi. |
| 4 | „Analysis of Microplastics in a Hungarian River" | „The environmental paradox of flood control: Microplastic redistribution by regulated river flows in the Tisza Basin" | A „paradox" szó intellektuális feszültséget teremt, és az ár-vízvédelmi kontextus szélesebb olvasóközönséget szólít meg. |

### Gyakorlati tanácsok

- **Kérj több körben címeket.** Az első 10 javaslat után kérd: *„Most adj 5 még merészebbet"* vagy *„5 konzervatívabbat, amik biztosan átmennek egy bírálón."*
- **Használd az AI javaslatait nyersanyagként.** Gyakran nem egy egész címet, hanem egy-egy szót vagy szerkezetet veszel át, és abból építed a végleges változatot.
- **Adaptáld a célfolyóirathoz.** A *Nature* és a *Science* gyakran rövid, provokatív címeket kedvelnek; a szakterületi folyóiratok a részletes, leíró címeket preferálják. Mondd meg az AI-nak, melyik folyóiratba szánod.

---

## 3.4 Bírálói vélemények megválaszolása

### Miért az egyik legstresszesebb feladat?

A peer review válasz egy sajátos műfaj: egyszerre kell diplomatikusnak és határozottnak lenned, elismerned a jogos kritikát és megvédened az álláspontodat, technikai részletekbe menned és mégis áttekinthetően írni. Ráadásul gyakran érzelmileg terhelt helyzetben — miután valaki keményen bírálta a munkádat.

Han és szerzőtársai (2024) tesztjei szerint ez az AI egyik legimpozánsabb képessége: a modell „progresszív" érvelési stílusban építi fel a válaszokat, szisztematikusan sorakoztatja az érveket, és megőrzi a semleges, professzionális hangnemet — mindazt, amit egy stresszes kutató hajnali háromkor nehezen tud produkálni.

### Stratégia: Pont-by-pont válasz sablon

Az alábbi struktúra szinte minden folyóiratnál elfogadott, és az AI természetesen ebben a formátumban dolgozik:

> **Prompt:** *„Az alábbiakban a kéziratom ([cím]) bírálói véleménye olvasható. Készíts pont-by-pont választ a következő struktúrában: (1) Idézd a bíráló megjegyzését dőlt betűvel. (2) Alatta írd a választ normál betűvel. (3) Kezdd minden választ a bíráló hozzájárulásának elismerésével. (4) Ha módosítottunk a kéziraton, idézd az új szöveget és jelöld a helyet. (5) Ha nem értünk egyet, udvariasan de határozottan érveljünk, irodalmi hivatkozásokkal alátámasztva."*

**Példa — egyszerű módszertani kérdés:**

*Bíráló megjegyzése:*
> *„The authors should explain why they chose Raman spectroscopy over FTIR for particle identification."*

*AI-asszisztált válasz:*
> We thank the reviewer for this important question. We chose micro-Raman spectroscopy over FTIR for two main reasons. First, Raman spectroscopy provides superior spatial resolution (< 1 μm vs. ~10 μm for FTIR), which is critical for identifying particles in the < 100 μm size range that dominated our samples (see Fig. 3). Second, Raman analysis can be performed directly on water-immersed samples, eliminating the drying artifacts that affect FTIR measurements (Araujo et al., 2018). We have added a brief justification to Section 2.3 of the revised manuscript (lines 142–148, highlighted in yellow).

Figyeld meg a válasz szerkezetét: elismerés → két konkrét ok → irodalmi hivatkozás → utalás a kézirat-módosításra. Ez az a struktúra, amit a bírálók látni akarnak.

### Nehéz bírálói kommentek kezelése

Időnként a bíráló olyasmit kér, ami nem teljesíthető — például egy műszert, amihez nincs hozzáférésed, vagy egy kísérletet, ami a kutatás hatókörén kívül esik. Az AI itt különösen hasznos, mert képes „diplomatikus elutasítást" fogalmazni:

> **Prompt:** *„A bíráló kéri, hogy ismételjük meg a kísérleteket XRF spektrométerrel. Sajnos nem áll rendelkezésünkre ilyen műszer, és a projekt költségvetése nem teszi lehetővé a beszerzést. Fogalmazz udvarias, de hatozott választ, amelyben (1) elismered a javaslat értékét, (2) elmagyarázod a korlátot, (3) kiemeled, milyen alternatív módszerrel erősítettük meg az eredményeinket, (4) javaslod ezt jövőbeli kutatás irányaként."*

*AI-asszisztált válasz:*
> We greatly appreciate the reviewer's suggestion to include XRF spectroscopy, which would indeed provide complementary elemental composition data. Unfortunately, our laboratory does not currently have access to an XRF spectrometer, and the project budget does not permit external analysis at this stage. To address this concern, we have strengthened our polymer identification by running duplicate Raman analyses and cross-referencing our spectra against the SLOPP library (Munno et al., 2020), achieving > 95% match confidence for all identified polymers. We have noted XRF analysis as a valuable direction for future research in the revised Discussion (lines 387–390). We believe this approach provides robust identification for the purposes of the current study.

### Ellenséges hangnemű bírálatok kezelése

Ritkán, de előfordul, hogy a bíráló hangja sértő vagy személyeskedő. Az AI ilyen helyzetben is megőrzi a professzionalizmust:

> **Prompt:** *„A bíráló a következőt írta: [ellenséges komment másolása]. Fogalmazz választ, amely (1) kizárólag a tartalmi kérdésre reagál, (2) figyelmen kívül hagyja a hangnemet, (3) tényszerűen érvel, és (4) semmilyen módon nem utánozza az ellenséges stílust."*

**Arany szabály:** Soha ne küldj bírálói választ anélkül, hogy legalább egy napot aludtál rá, és egy kolléga is átolvasta. Az AI megírhatja a vázlatot, de a te neved áll alatta.

---

## 3.5 Hibák felismerése saját és mások munkájában

### A reprodukálhatósági válság kontextusa

Baker (2016) *Nature*-ben megjelent felmérésében 1500 tudós ismerte el, hogy nehézségeik vannak más kutatók eredményeinek reprodukálásával. A hibák — terminológiai pontatlanságoktól a matematikai elírásokon át a félreidézésekig — szisztematikusan jelen vannak a tudományos irodalomban.

Az AI nem helyettesíti a szakértői ellenőrzést, de *kiegészíti* azt — és olyan hibákat is észrevehet, amelyeket az emberi szem a 43. átolvasásnál sem vesz észre.

### Terminológiai és fogalmi hibák

> **Prompt:** *„Ellenőrizd az alábbi bekezdés kémiai és terminológiai pontosságát. Jelöld meg a hibás vagy pontatlan állításokat, és adj korrekt megfogalmazást hivatkozásokkal."*

Han és szerzőtársai (2024) tesztjei szerint az AI képes volt felismerni, hogy a PFOSA-t (perfluoroktán-szulfonamid) helytelenül „amino-csoporttal rendelkező" vegyületként azonosították, holott szulfonamid-csoportja van. Ugyanakkor más hibákat kihagyott, és a saját javításaiban is előfordultak pontatlanságok.

**Tanulság:** Az AI hibakeresése hasznos, de *mindig kevert eredményt ad* — helyes javítások és újabb hibák keverékét. Soha ne fogadd el kritikai értékelés nélkül.

### Matematikai és egyenlet-hibák

> **Prompt:** *„Ellenőrizd az alábbi kinetikai egyenleteket (pszeudo-első-rendű, pszeudo-másod-rendű, Elovich, intrapartikuláris diffúzió). Írd ki a helyes formákat, és jelöld, ha a kéziratban eltérés van."*

Az AI megadta a helyes egyenleteket mind a négy modellre, de a linearizált pszeudo-másod-rendű egyenletben nem vette észre a hibát, sőt a saját javításában is hibázott — a természetes logaritmus helyett tízes alapú logaritmust használt. Ez a tipikus minta: az AI jobb a fogalmi hibák felismerésében, mint a matematikai részletekben.

### Félreidézések (misquotation) ellenőrzése

Az egyik leginsidiosabb hiba a tudományos irodalomban: amikor egy szerző félreidézi a hivatkozott forrást — nem szándékosan, hanem mert emlékezetből írta, vagy rosszul értelmezett egy statisztikát.

> **Prompt:** *„Az alábbi bekezdésben a szerzők három korábbi tanulmányra hivatkoznak. Hasonlítsd össze az itt leírt állításokat a hivatkozott cikkek tényleges megállapításaival. Van-e eltérés?"*

Az AI itt a legjobb, ha a hivatkozott cikkek is hozzáférhetők számára (nyílt hozzáférésű cikkek, vagy feltöltöd a PDF-eket). A félreidézések felderítése a tesztek során az AI egyik legmegbízhatóbb képességének bizonyult.

### Gyakorlati munkafolyamat hibakereséshez

1. **Írd meg a kéziratot** (vagy a releváns szekciót).
2. **Futtasd le az AI-t** a fenti promptokkal (terminológia, egyenletek, hivatkozások külön-külön).
3. **Értékeld kritikusan** az AI javaslatait — ne fogadj el semmit vakon.
4. **Ellenőrizd az AI javításait is** — a modell saját válaszaiban is lehetnek hibák.
5. **Ismételd meg más LLM-mel** — a Claude, a ChatGPT és a Gemini gyakran különböző hibákat találnak meg.

---

## 3.6 Kutatási pályázatok és grant-javaslatok írása

### Ötletelés és ismerkedés egy új területtel

Amikor egy új kutatási irányt fontolgatsz — különösen egy interdiszciplináris projektet, ahol nem vagy otthon minden részdiszciplínában —, az AI ideális „felderítő" eszköz:

> **Prompt:** *„Szeretnék egy kutatási projektet indítani a szabályozott folyami áramlások és a mikroplasztik újraeloszlás kapcsolatáról a Tisza vízgyűjtőjén. Foglald össze a téma jelenlegi állását 500 szóban, kiemelve a legfontosabb megválaszolatlan kérdéseket."*

Az LLM válasza jellemzően részletesebb és célzottabb, mint egy Google-keresés eredménye, mert az interaktív kérdés-válasz formátum lehetővé teszi a fokozatos mélyítést. Ahogy Han és szerzőtársai (2024) tapasztalták: az AI nem ad forradalmi ötleteket, de a meglévő tudás szisztematikus aggregálásában — ami a pályázatírás kiindulópontja — kifejezetten hatékony.

### Tudáshiányok feltérképezése

A pályázat egyik legkritikusabb eleme a „knowledge gap" meggyőző bemutatása: miért szükséges ez a kutatás?

> **Prompt:** *„A fenti összefoglaló alapján azonosíts 8-10 konkrét tudáshiányt az édesvízi mikroplasztik transzport területén. Mindegyiknél jelöld, hogy (a) mekkora a kutatási közösség figyelme erre a kérdésre (alulkutatott / mérsékelten kutatott / intenzíven kutatott), és (b) milyen módszertannal lenne vizsgálható."*

**Gyakorlati példa — AI-generált tudáshiányok:**

1. *Mikroklíma-variáció hatása a mikroplasztik lebontási sebességre folyóvízi üledékben* — alulkutatott — terepi mikrokozmos kísérletek UV-szenzorokkal
2. *Árvízi események szerepe a parti zónában felhalmozódott mikroplasztik mobilizálásában* — mérsékelten kutatott — időszakos mintavétel árvíz előtt/közben/után
3. *Urbanizáció és csapadékvíz-elvezető rendszerek mint pontforrások a Tisza mellékfolyóiban* — alulkutatott — összehasonlító vizsgálat városias és természetes vízgyűjtőkön
4. *Biológiai film (biofilm) képződés mikroplasztik felszínén és ennek hatása a süllyedési sebességre* — intenzíven kutatott — laboratóriumi mezokozmosz kísérletek

Nem mind eredeti — de szisztematikus, és jó kiindulópont a pályázat „Significance" szekciójához.

### Pályázati vázlat készítése

A teljes munkafolyamat:

1. **Ismerkedés** a témával (fent)
2. **Tudáshiányok** azonosítása (fent)
3. **Kiválasztás és elmélyítés**: válassz egy-két hiányt, és kérd az AI-t, hogy részletezze a lehetséges módszertant és a várt eredményeket
4. **Vázlat generálása**:

> **Prompt:** *„Készíts egy 2 oldalas kutatási pályázat-vázlatot az alábbi struktúrában: (1) Bevezetés és tudományos háttér, (2) Kutatási célok (3 konkrét cél), (3) Módszertani megközelítés, (4) Várható eredmények és hatásuk, (5) Időterv (36 hónap). A téma: [a választott tudáshiány kidolgozása]. A célfolyóirat/pályázat: NKFIH posztdoktori ösztöndíj / ERC Starting Grant."*

**Kritikus figyelmeztetés:** Az AI által generált hivatkozások a pályázati vázlatban jellemzően *fiktívek*. A modell ezt általában jelzi is, de ne hagyatkozz rá — minden egyes hivatkozást manuálisan ellenőrizz, vagy cseréld ki valós forrásokra. (A hivatkozás-hallucináció problémáját részletesen tárgyaljuk a 3.9-es alfejezetben.)

### Pályázati szervezetek elvárásai

Fontos tudni, hogy a nagy pályázati szervezetek eltérő álláspontot képviselnek:

- **NSF** (USA): kéri, hogy a pályázók jelezzék az AI felhasználásának mértékét; a bírálóknak tilos AI-eszközökbe feltölteni pályázati anyagokat.
- **NIH** (USA): nem tiltja az AI használatát a pályázatírásban, de a plágium- és adatfabrikálási szabályok természetesen érvényesek; a bírálóknak tilos AI-t használni.
- **NKFIH** (Magyarország): a mindenkori pályázati kiírás irányadó — mindig ellenőrizd a konkrét felhívás feltételeit.

**Általános szabály:** Mindig nézd meg a pályázati kiírás aktuális AI-politikáját, mielőtt benyújtod. A szabályok gyorsan változnak.

---

## 3.7 Tudománykommunikáció

### Miért fontos — és miért nehéz?

A klímaváltozás, a környezetszennyezés, a járványok — mind olyan témák, ahol a közérthetőség nem luxus, hanem szükségszerűség. De egy kutató, aki napi 8 órát tölt szakcikkek írásával, ritkán képes átkapcsolni a „közérthető" módba. Az AI ebben az átkapcsolásban segít.

### Népszerű tudományos cikk

> **Prompt:** *„Írd át az alábbi kutatási cikk absztraktját népszerű tudományos cikké, amelyet egy Magyar Narancs / Qubit olvasó is megért. Maximum 500 szó, könnyed hangnem, személyes megszólítás, hasonlatok a mindennapi életből. Kerüld a szakkifejezéseket, vagy ha elkerülhetetlen, zárójelben magyarázd el."*

**Gyakorlati példa:**

*Eredeti absztrakt:*
> „Microplastic (MP) concentrations ranging from 2.4 to 18.7 particles/L were detected in surface water samples from the Tisza River, with polyethylene (PE) and polypropylene (PP) constituting 73% of identified polymers."

*AI-generált népszerű tudományos szöveg:*
> Amikor legközelebb a Tiszánál sétálsz, gondolj bele: minden liter vízben akár 19 apró műanyag szilánk úszkálhat — szabad szemmel láthatatlanul. Egy friss kutatás szerint a Tisza vizében mindenhol ott vannak ezek a mikroplasztiknak nevezett, milliméternél kisebb törmelékek. A legnagyobb részük ugyanabból az anyagból készült, mint a bevásárlószatyrod (polietilén) vagy a joghurtos dobozod (polipropilén). Nem látod, nem érzed, de ott vannak — és a hatásuk az élővilágra még alig ismert.

Figyeld meg, hogy az AI automatikusan alkalmazta a hasonlatokat (bevásárlószatyor, joghurtos doboz), a személyes megszólítást, és a drámai szünetet („Nem látod, nem érzed, de ott vannak") — mindezt a szakmai pontosság megőrzése mellett.

### Közösségi média

> **Prompt:** *„Írj 3 Twitter/X posztot (max. 280 karakter) a fenti kutatásról. Legyen bennük 2-3 releváns hashtag és egy figyelemfelkeltő nyitómondat."*

*AI javaslat 1:*
> Minden liter Tisza-vízben akár 19 láthatatlan műanyag szilánk. Új kutatás feltárja, mit rejtett eddig a folyó. 🔬🌊 #Mikroplasztik #Tisza #Környezettudomány

*AI javaslat 2:*
> A bevásárlószatyrod a Tiszában végzi? Kutatóink megmérték: a folyó tele van polietilén és polipropilén töredékekkel. 🧪 #Kutatás #Mikroplasztik #Debrecen

*AI javaslat 3:*
> 500 km Tisza, több ezer vízminta, egy riasztó eredmény: a mikroplasztik mindenhol ott van. De mi következik ebből az élővilágra? 🐟 #TiszaKutatás #Környezetvédelem

### Sajtóközlemény

> **Prompt:** *„Készíts egy 300 szavas sajtóközleményt az alábbi kutatási cikk alapján. Formátum: címsor, lead bekezdés (ki, mit, mikor, hol, miért), háttér, idézet a kutatásvezetőtől (fiktív, de reális hangnemben), a kutatás jelentősége, elérhetőség."*

Ez különösen hasznos, ha az egyetemi kommunikációs osztállyal dolgozol, és szükséged van egy kiindulópontra, amit ők tovább csiszolhatnak.

### Prezentációs vizuális elemek

Az AI képgeneráló eszközök (DALL-E, Midjourney, Stable Diffusion) forradalmasították a tudományos prezentációk vizuális világát. Nem a tudományos ábrák kiváltásáról van szó — az adatvizualizáció továbbra is a kutató feladata —, hanem a *kísérő vizuális elemekről*:

- **Címdia** egy konferencia-előadáshoz: *„Generálj egy fotorealisztikus képet egy kristálytiszta folyóról, amelyben nagyítólencsével nézve apró, színes műanyag részecskéket látni. Stílus: National Geographic fotó."*
- **Gondolati térkép** egy kutatási projekt bemutatásához
- **Infografika vázlat** egy poszterhez

**Fontos:** Egyes kiadók (pl. Elsevier, a Science családja) korlátozzák az AI-generált képek használatát publikációkban. Prezentációkban, oktatási anyagokban és közösségi médiában viszont szabadon használhatók. Mindig ellenőrizd a célfolyóirat aktuális irányelveit.

---

## 3.8 Kísérleti tervek és kérdőívek készítése AI-val

### Kísérlettervezés

Az AI nem csak szöveget ír — képes kísérleti protokollokat is generálni, amelyek jó kiindulópontot adnak, különösen ha egy új területre lépsz be.

> **Prompt:** *„Tervezz egy kísérletet palackozott vízben lévő mikroplasztik mennyiségének vizsgálatára. Add meg: (1) a szükséges vegyszereket, fogyóeszközöket és műszereket, (2) a mintavételi protokollt, (3) a mintaelőkészítés lépéseit, (4) az azonosítási módszert, (5) a QA/QC lépéseket, (6) az adatelemzés módját."*

Han és szerzőtársai (2024) tesztjei szerint a GPT-4 egy ilyen promptra részletes, lépésről lépésre haladó protokollt adott, amely tartalmazta a reprezentatív termékek kiválasztását, a replikátumokat, a módszer-vak minták alkalmazását és a racionális adatrögzítési eljárásokat.

**De: a részletek számítanak.** A szerzők — mint szakterületi szakértők — azonnal észrevették a hiányosságokat:

- Az AI nem jelezte, hogy az infravörös/Raman spektroszkópia 100 mikron alatti részecskéknél speciális mikro-műszereket igényel.
- Polimer mikrofilteres membránt javasolt, ami zavarná a Raman-jelet — szervetlen membránra (alumínium-oxid, üvegszál) vagy fém bevonatosra van szükség.
- A szűrőmembrán felületi simasága kritikus mikrométer-skálájú analízisnél — ezt nem említette.

**Tanulság:** Az AI protokollja *csiszolt szöveg mögé rejti a hiányosságokat*. Szakterületi tudás nélkül nem vennéd észre, mi hiányzik. Mindig kérd a modellt, hogy adjon hivatkozásokat a „valóságellenőrzéshez" (reality check), és vesd össze a javasolt módszertant a hivatkozott cikkek protokolljaival.

**Munkafolyamat kísérlettervezéshez:**

1. Add meg a kutatási kérdést → kapj egy általános feladatlistát
2. Kérj részleteket a specifikus lépésekhez
3. Kérj releváns hivatkozásokat valóságellenőrzéshez
4. Opcionálisan: kérj beszerzési listát (reagensek, műszerek, védőfelszerelés, QA/QC)

### Kérdőív-készítés

A társadalomtudományi és környezet-egészségügyi kutatásban a kérdőíves felmérések alapvető módszerek. Az AI meglepően jó kérdőív-tervezésben:

> **Prompt:** *„Tervezz egy 30 kérdéses kérdőívet arról, hogy a COVID-19 alatt bevezetett maszkhasználat hogyan változtatta meg a kozmetikumok használati szokásait az USA-ban. A célcsoport felnőtt nők, 18-60 év. Tagold szekciókra: demográfia, maszkhasználati szokások, COVID előtti/utáni termékhasználat, termékpreferenciák, alkalmazási minták változása, általános vélemények."*

Az AI nem egyszerűen 30 kérdést listáz — szisztematikusan felépített kérdőívet készít, logikus szekciórenddel, formázással (félkövér szekciócímek, dőlt utasítások), és gyakran hozzáad a promptban nem kért elemeket is (pl. záró „általános vélemény" szekció).

**Továbbfejlesztés:** A kérdőív iteratív finomítása az egyik legjobb példa az AI-val való együttműködésre:

> *„Szűkítsd le a kérdőívet: (1) csak 18-60 éves nők, (2) kizárólag púderek és porzó kozmetikumok, (3) adj hozzá egy 10 kérdéses kiegészítő modult krónikus légúti betegeknek."*

Az AI a szűkített változatban 40 kérdést generált 8 szekcióban, beleértve egy orvosi szempontból is releváns almodult a légúti betegeknek.

---

## 3.9 A hivatkozás-hallucináció problémája

### Mi a probléma?

Az LLM-ek egyik legjól dokumentált és legveszélyesebb korlátja a hivatkozás-hallucináció: a modell meggyőzően formázott, létezőnek *tűnő*, de valójában *kitalált* hivatkozásokat generál. Ez nem „hiba" a szó hagyományos értelmében — ez az LLM működésének fundamentális következménye. A modell nem „tud" dolgokat — valószínűségi alapon generálja a következő tokent, és egy hivatkozás formailag hasonlít egy másik hivatkozásra.

A probléma súlyossága csökken: a korai modellekben (GPT-3.5) a hivatkozások 98%-a volt kitalált; a GPT-4-ben ez kb. 20%-ra csökkent (Mollick, 2024). De még 20% is elfogadhatatlanul magas a tudományos publikálásban, ahol egyetlen hamis hivatkozás a kézirat azonnali elutasításához vezethet.

### Hogyan ismerd fel a kitalált hivatkozásokat?

**Vörös zászlók:**

1. **A DOI nem létezik.** Ez a legegyszerűbb teszt: másold be a DOI-t a https://doi.org/ címbe. Ha nem talál semmit, a hivatkozás valószínűleg kitalált.

2. **A szerzők léteznek, de a cikk nem.** Az AI gyakran valós szerzőneveket kombinál kitalált cikkekkel. Ellenőrizd a szerző Google Scholar vagy ORCID profilján.

3. **A folyóiratnév kicsit „mellé van."** Például „Journal of Environmental Sciences" helyett „Journal of Environmental Science" — létezik ilyen folyóirat is, de nem az, amire a hivatkozás utal.

4. **Az évszám és a kötetszám nem stimmel.** Például a „Vol. 45, 2019" kombináció az adott folyóiratnál valójában 2018 volt.

5. **A cikk tartalma nem felel meg a hivatkozás kontextusának.** Ez a leginsidiosusabb: a hivatkozás létezik, de nem azt mondja, amit az AI állít róla — tehát az AI formailag jó hivatkozást ad, de *félreidézi*.

### Megelőzési stratégiák

**1. Soha ne bízz meg AI-generált hivatkozásban ellenőrzés nélkül.**

Ez nem opcionális jótanács — ez abszolút szabály. Minden egyes hivatkozást manuálisan ellenőrizz a Scopus-ban, Web of Science-ben vagy Google Scholar-ben.

**2. Válaszd szét a szövegírást és a hivatkozáskezelést.**

A legbiztonságosabb munkafolyamat:

1. Írd meg a szöveget az AI-val, de *hivatkozások nélkül* — használj helyőrzőket: [REF: mikroplasztik transzport folyóvízben].
2. A szöveg elkészülte után keresd meg te magad a releváns hivatkozásokat a szokásos adatbázisokban.
3. Helyettesítsd be a helyőrzőket a valós hivatkozásokkal.

**3. Ha az AI ad hivatkozásokat, használd őket kiindulópontként, nem végeredményként.**

> **Prompt:** *„Adj 5 releváns hivatkozást a mikroplasztik szezonális dinamikájáról édesvízben. Mindegyiknél add meg a szerzőket, évet, folyóiratot és DOI-t."*

Tedd utána:
- Ellenőrizd, létezik-e a DOI
- Ellenőrizd, stimmelnek-e a szerzők
- Olvasd el legalább az absztraktot — valóban releváns?

**4. Kérd az AI-t, hogy legyen önkritikus.**

> **Prompt:** *„A fenti hivatkozásaid közül melyiknél vagy bizonytalan a pontosságban? Jelöld meg azokat, amelyeket nem tudsz 100%-osan megerősíteni."*

A modellek egyre jobbak ebben az önreflexióban — jellemzően elismerik, ha egy hivatkozás „illustratív" vagy „nem garantáltan pontos."

**5. Használj referencia-kezelő szoftvert.**

A Zotero, Mendeley vagy EndNote rendszerekbe csak manuálisan ellenőrzött hivatkozásokat vigyél be. Ha az AI javasol egy hivatkozást, *először* keresd meg a Scopus-ban, és *onnan* importáld a referencia-kezelőbe.

### A Schwartz-eset tanulsága

2023-ban Steven Schwartz ügyvéd a ChatGPT-vel kerestetett jogi precedenseket, és a bíróságon hat teljesen kitalált bírósági döntésre hivatkozott — ellenőrzés nélkül. Az eset szankciókhoz vezetett. A tudományos világban a következmény hasonlóan súlyos lehet: a kézirat elutasítása, az adott folyóiratnál való „tiltólistára" kerülés, és ami a legrosszabb — a tudományos reputáció tartós sérülése.

---

## 3.10 Összefoglalás: a tudós marad a pilóta

Ez a fejezet a tudományos írás és kommunikáció teljes spektrumát átfogta: az irodalomáttekintéstől a kéziratíráson, a bírálói válaszokon és a pályázatokon át a tudománynépszerűsítésig és a kísérlettervezésig. Minden területen ugyanaz a minta rajzolódik ki:

**Az AI drámaian felgyorsítja a folyamatot, de nem helyettesíti a szakértőt.**

- Az irodalomáttekintésben az AI az előszűrést végzi el — de a kritikus értékelés a tiéd.
- A kéziratírásban az AI csiszolja a nyelvet és az érvelést — de a tudományos tartalom a tiéd.
- A bírálói válaszokban az AI megőrzi a professzionális hangnemet — de a stratégia a tiéd.
- A hivatkozásokban az AI javaslataival indulhatsz — de az ellenőrzés mindig manuális.
- A kísérlettervezésben az AI ad egy vázlatot — de a szakterületi mélyismeret nélkülözhetetlen.

Nóra, a nyitó jelenetünk kutatója, végül hajnali háromkor nem egyedül küzdött a kézirattal. Az AI javította a nyelvtanját, átstrukturálta a Discussion szekcióját, csiszolta a címet, és segített megfogalmazni a cover letter-t az editornak. De Nóra írta a tudományt — az AI csak segített elmondani.

---

> **📦 Etikai kérdések**
>
> A tudományos írásban használt AI számos etikai kérdést vet fel: Kinek a szellemi terméke az AI-val írt szöveg? Hol húzódik a határ a „segédeszköz" és a „ghostwriter" között? Hogyan kezeljék a folyóiratok az AI-val készült kéziratokat? Milyen felelőssége van a szerzőnek a kész szöveg minden állításáért?
>
> **Az etikai kérdések teljes tárgyalásáért lásd a 16. fejezetet.**

---

## Hivatkozások és források

- Baker, M. (2016). 1,500 scientists lift the lid on reproducibility. *Nature*, 533, 452–454.
- Han, J., Qiu, W., & Lichtfouse, E. (2024). *ChatGPT in Scientific Research and Writing: A Beginner's Guide*. Springer Nature.
- Mollick, E. (2024). *Co-Intelligence: Living and Working with AI*. Portfolio/Penguin.
- Noy, S., & Zhang, W. (2023). Experimental evidence on the productivity effects of generative artificial intelligence. *Science*, 381(6654), 187–192.
- OECD (2023). *Artificial Intelligence in Science: Challenges, Opportunities and the Future of Research*. OECD Publishing.
- Plaxco, K.W. (2010). The art of writing science. *Protein Science*, 19(12), 2261–2266.
- Pulverer, B. (2015). When things go wrong: correcting the scientific record. *EMBO Journal*, 34(20), 2483–2485.
