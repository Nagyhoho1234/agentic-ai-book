# 7. fejezet: Adat-pipeline-ok és automatizálás

## Minden reggel ugyanaz a tizenöt lépés

Képzeld el Annát, aki a Debreceni Egyetem Meteorológiai Tanszékén dolgozik. Minden munkanapja ugyanúgy kezdődik. Reggel fél nyolckor bejelentkezik a gépére, és elindítja azt a tizenöt lépést, amit az elmúlt két évben minden egyes nap elvégzett:

1. Letölti az éjszakai állomásadatokat az OMSZ FTP szerveréről.
2. Megnyitja az Excel-fájlt, és kézzel törli az üres sorokat.
3. Ellenőrzi, hogy a hőmérsékleti adatok -40 és +50 °C közé esnek-e.
4. Kikeresi azokat a sorokat, ahol a páratartalom-szenzor nem küldött adatot.
5. Az ilyen hiányokat az előző és következő óra átlagával tölti ki.
6. Az időbélyegeket átalakítja UTC-ből helyi időre.
7. Összevonja a különböző állomások fájljait egyetlen táblázatba.
8. Kiszámolja az aznapi minimumokat, maximumokat és átlagokat.
9. Készít három grafikont a napi jelentéshez.
10. PDF-be exportálja a grafikonokat és a statisztikát.
11. Elküldi e-mailben a tanszékvezetőnek és az Országos Meteorológiai Szolgálatnak.
12. Feltölti az adatot a tanszéki adatbázisba.
13. Megnézi, nincs-e szenzor-hiba a friss adatokban.
14. Ha van, beír egy hibajegyet a karbantartási rendszerbe.
15. Archíválja a nyers fájlokat a hálózati meghajtóra.

Anna minden lépést pontosan tud végrehajtani. A probléma nem a tudásával van, hanem azzal, hogy ez az egész folyamat minden reggel 45 percet vesz igénybe, és közben egyetlen alkotó gondolata sem születik. Ha egyszer elfelejtené az 5. lépést, az egész heti statisztika torzulna. Ha ketten csinálnák ugyanezt, valószínűleg kicsit másképp töltenék ki a hiányzó értékeket.

Ez a fejezet arról szól, hogyan alakíthatod az ilyen ismétlődő, kiszámítható, hibára hajlamos munkafolyamatokat automatizált **pipeline-okká** --- vagyis adatfeldolgozási csővezetékekké, amelyek egyszer megírod, aztán naponta, óránként vagy akár percenként, megbízhatóan és reprodukálhatóan futnak.

> **Definíció:** A **pipeline** (adatfeldolgozási csővezeték) lépések sorozata, amelyben az egyik lépés kimenete a következő lépés bemenete. Ahogy a víz átfolyik egy fizikai csővezetéken, úgy áramlik az adat a beviteltől a végtermékig --- automatikusan, emberi beavatkozás nélkül. A tudományos pipeline célja, hogy a nyers mérésből reprodukálható eredményt állítson elő.

---

## A pipeline koncepció: öt szakasz

Minden tudományos adat-pipeline öt alapvető szakaszra bontható. Egyes pipeline-ok egyszerűbbek (csak kettő-három szakasz), mások összetettebbek (egyes szakaszokon belül tucatnyi allépéssel), de az alapszerkezet mindig felismerhető.

### A pipeline öt szakasza

```
┌─────────────┐    ┌─────────────┐    ┌────────────────────┐    ┌────────────┐    ┌─────────────┐
│  1. BEVITEL  │───>│ 2. TISZTÍTÁS│───>│ 3. TRANSZFORMÁCIÓ  │───>│ 4. ELEMZÉS │───>│ 5. KIMENET  │
│  (Ingestion) │    │  (Cleaning) │    │ (Transformation)   │    │ (Analysis) │    │  (Output)   │
│              │    │             │    │                    │    │            │    │             │
│ - Fájlok     │    │ - Hiányzó   │    │ - Egységváltás     │    │ - Statiszt.│    │ - Táblázat  │
│ - API-k      │    │   értékek   │    │ - Összevonás       │    │ - Modell   │    │ - Grafikon  │
│ - Adatbázis  │    │ - Outlier-ek│    │ - Származtatott    │    │ - Trend    │    │ - PDF/HTML  │
│ - Szenzorok  │    │ - Formátum  │    │   változók         │    │ - Teszt    │    │ - Adatbázis │
│ - IoT        │    │ - Validáció │    │ - Szűrés           │    │            │    │ - E-mail    │
└─────────────┘    └─────────────┘    └────────────────────┘    └────────────┘    └─────────────┘
```

**1. Bevitel (Ingestion):** Az adat belép a rendszerbe. Ez lehet fájl letöltése, API-hívás, adatbázis-lekérdezés vagy szenzor-olvasás. A lényeg: a nyers adat strukturáltan elérhető lesz.

**2. Tisztítás (Cleaning):** A nyers adat mindig "piszkos". Hiányoznak értékek, vannak hibás mérések, inkonzisztens formátumok. Ebben a szakaszban javítjuk, validáljuk, és dokumentáljuk az adatminőséget.

**3. Transzformáció (Transformation):** A tiszta adatot átalakítjuk az elemzéshez szükséges formába. Egységeket váltunk, táblákat vonunk össze, új változókat számolunk, szűrünk.

**4. Elemzés (Analysis):** Itt történik a tényleges tudományos munka: statisztikák, modellek, trendek, hipotézisvizsgálatok.

**5. Kimenet (Output):** Az eredmények eljutnak a felhasználóhoz: riportok, grafikonok, frissített adatbázisok, értesítések.

Anna tizenöt lépése mind ebbe az öt szakaszba sorolható:

| Lépés | Szakasz |
|-------|---------|
| 1 (letöltés FTP-ről) | Bevitel |
| 2-5 (üres sorok, ellenőrzés, hiánypótlás) | Tisztítás |
| 6-7 (időzóna, összevonás) | Transzformáció |
| 8 (statisztikák) | Elemzés |
| 9-15 (grafikonok, PDF, e-mail, archiválás) | Kimenet |

Ha így bontod fel a saját munkafolyamatodat, azonnal láthatóvá válik, hol van automatizálási lehetőség --- és az a meglepő, hogy szinte mindenhol.

---

## Automatizálási lehetőségek azonosítása

Mielőtt nekiállnál pipeline-t építeni, érdemes végiggondolnod, mely feladataid érdemesek automatizálásra. Nem minden feladatot kell (vagy érdemes) automatizálni. Az alábbi ellenőrző lista segít a döntésben.

### Ellenőrző lista: automatizáljam-e?

Adj minden kérdésre 0-tól 2-ig pontot (0 = nem jellemző, 1 = részben, 2 = teljesen):

| # | Kérdés | Pontszám |
|---|--------|----------|
| 1 | **Ismétlődő?** Ugyanezt csinálom hetente vagy gyakrabban? | 0 / 1 / 2 |
| 2 | **Determinisztikus?** Ugyanazzal a bemenettel mindig ugyanazt az eredményt várom? | 0 / 1 / 2 |
| 3 | **Hibára hajlamos?** Könnyen rontok el egy lépést, ha fáradt vagyok? | 0 / 1 / 2 |
| 4 | **Időigényes?** Az egész folyamat több mint 10 percet vesz igénybe? | 0 / 1 / 2 |
| 5 | **Több forrást használ?** Különböző fájlokból, rendszerekből kell adatot összeszednem? | 0 / 1 / 2 |
| 6 | **Dokumentálható?** Le tudom írni a lépéseket úgy, hogy más is meg tudja csinálni? | 0 / 1 / 2 |
| 7 | **Skálázási igény?** Lehet, hogy a jövőben 10x vagy 100x annyi adatra kell alkalmaznom? | 0 / 1 / 2 |
| 8 | **Kommunikálok eredményt?** A végén riportot, grafikont, e-mailt készítek? | 0 / 1 / 2 |

**Értékelés:**
- **12--16 pont:** Azonnal automatizáld. Minden nap időt nyersz vissza.
- **8--11 pont:** Érdemes automatizálni, de priorizálj: kezdd a legfájdalmasabb lépéssel.
- **4--7 pont:** Részleges automatizálás (pl. csak a tisztítás és a riportolás).
- **0--3 pont:** Valószínűleg nem éri meg az automatizálási befektetés.

Anna feladatánál a pontszám 15/16 lenne. Az ő esetében az automatizálás nem luxus, hanem szükségszerűség.

### Tipikus tudományos feladatok, amelyek kiáltanak az automatizálásért

- **Napi/heti adatletöltés** külső forrásból (meteorológiai, hidrológiai, légszennyezettségi adatok)
- **Műszeres mérések feldolgozása** (spektrométer, kromatográf, mikroszkóp kimenet)
- **Kérdőív-adatok tisztítása** (ismétlődő kódolási szabályok)
- **Irodalomfigyelés** (új publikációk szűrése adott kulcsszavakra)
- **Jelentéskészítés** (heti/havi összefoglalók automatikus generálása)
- **Bioinformatikai munkafolyamatok** (szekvenálási adatok feldolgozása)
- **Szenzor-hálózatok monitorozása** (folyamatos adatfolyam, azonnali riasztás szükséges)

---

## Adatbevitel: honnan jön az adat?

A pipeline első lépése mindig a bevitel. A tudományos adatok sokféle forrásból érkezhetnek, és mindegyiknek megvan a maga sajátossága.

### Fájlok

A leggyakoribb eset: adatfájlok érkeznek valamilyen megosztott mappából, FTP szerverről, e-mail csatolmányként, vagy manuális letöltéssel.

**Tipikus formátumok:**
- **CSV** (Comma-Separated Values): a tudományos adatcsere *lingua franca*-ja. Egyszerű, szöveges, bármivel megnyitható. De vigyázz: a magyar CSV-kben gyakran pontosvessző a szeparátor és vessző a tizedes jel --- ez pont fordítva van, mint az angol konvenciónál!
- **Excel (.xlsx)**: kényelmes, de problémás automatizáláshoz. Az Excellel beolvasott gén-nevek automatikus dátummá alakulása (pl. a SEPT1 gén 2001. szeptember 1-jére) hírhedten sok bioinformatikai hibát okozott. Egy 2016-os tanulmány szerint a genomikai publikációk mintegy 20%-ában találtak ilyen konverziós hibát.
- **JSON**: API-k kedvenc formátuma, hierarchikus adatok tárolására kiváló.
- **NetCDF, HDF5**: nagy, többdimenziós tudományos adathalmazok (klímamodellek, műholdas adatok, szimulációk).
- **FASTA, FASTQ**: bioinformatikai szekvencia-adatok.
- **DICOM**: orvosi képalkotó adatok.
- **Egyedi szövegformátumok**: régi műszerek gyakran saját, dokumentálatlan formátumban exportálnak.

**Tipp:** Ha az AI kódolási asszisztensed (Ch 5) segítségével írsz beolvasó scriptet, mindig add meg a pontos formátumot. Például: *"Írj egy Python scriptet, ami beolvassa ezt a CSV-t, ahol a szeparátor pontosvessző, a tizedesjel vessző, és a dátum formátum ÉÉÉÉ.HH.NN."*

### Adatbázisok

Sok kutatócsoport saját adatbázist tart fenn --- vagy intézményi rendszerhez csatlakozik.

- **Relációs adatbázisok** (PostgreSQL, MySQL, SQLite): strukturált, táblázatos adatok. A Python `sqlalchemy` könyvtárával pár sor kóddal lekérdezhető.
- **Tudományos adatbázisok**: UniProt (fehérjék), PDB (proteinstruktúrák), GenBank (genetikai szekvenciák), GBIF (biodiverzitás). Ezeknek általában API-juk is van.
- **Intézményi repozitóriumok**: a Debreceni Egyetemen például a DEA (Debreceni Egyetemi Archívum) vagy a tanszéki fájlszerverek.

### API-k (Application Programming Interfaces)

Az API-t az 5. fejezetben definiáltuk: egy gép számára készült felület, amelyen keresztül programból kérdezhetsz le adatokat. A tudományos adatforrások egyre gyakrabban kínálnak API-t.

**Néhány fontos tudományos API:**

| API | Terület | Mit ad? |
|-----|---------|---------|
| NASA CMR (Common Metadata Repository) | Földtudományok | Műholdas mérési adatok, több ezer adatkészlet |
| Copernicus CDS (Climate Data Store) | Klíma | ERA5 reanalízis, szezonális előrejelzés |
| GBIF | Biodiverzitás | Fajmegfigyelési adatok, globálisan |
| UniProt | Biokémia | Fehérje-szekvenciák és annotációk |
| PubMed/NCBI E-utilities | Orvostudomány | Cikkek, szekvenciák, klinikai adatok |
| OpenWeatherMap | Meteorológia | Aktuális és előrejelzett időjárási adatok |
| OMSZ API | Magyar meteorológia | Magyar állomásadatok |

A NASA CMR különösen érdekes példa: a NASA LLM Cookbook-ja bemutatja, hogyan lehet természetes nyelvű kéréseket CMR API-lekérdezésekké alakítani. Például: *"Keress Landsat 8 műholdas felvételeket a Hortobágy felett 2025 júliusából"* --- ezt egy LLM-alapú ágens automatikusan lefordítja a megfelelő CMR API-hívásra, beleértve a földrajzi koordinátákat és az időszűrőt. Bár ez már az ágensek területe (Ch 11-12), az alapkoncepció --- hogy programból kérdezel le adatot, nem kézzel böngészel weboldalakat --- a pipeline-ok sarokköve.

### Szenzorok és IoT

A tudományos mérőállomások egyre intelligensebbek. A modern IoT (Internet of Things) eszközök közvetlenül a felhőbe vagy egy helyi szerverre streamelnek adatot.

**Tipikus forgatókönyvek:**

- **Meteorológiai állomások**: hőmérséklet, páratartalom, szélsebesség, csapadék 10 percenként.
- **Vízminőségi szenzorok**: pH, vezetőképesség, oldott oxigén folyamatos mérése folyókban.
- **Talajnedvesség-mérők**: mezőgazdasági kísérleti parcellákon, 15 perces mintavétellel.
- **Laboratóriumi műszerek**: automatizált spektrométerek, kromatográfok, amelyek közvetlenül fájlba vagy adatbázisba írnak.
- **Akusztikus szenzorok**: madárhang-monitorozás természetvédelmi területeken.

Debrecenben és a Tiszántúlon különösen releváns az agrár-IoT: a precíziós mezőgazdaságban alkalmazott szenzor-hálózatok óriási mennyiségű adatot termelnek, amelyet valós időben kell feldolgozni az öntözési, trágyázási vagy növényvédelmi döntésekhez.

**Kihívások szenzor-adatoknál:**
- **Folyamatos adatfolyam**: nem kötegelt fájlok, hanem végtelen stream.
- **Hálózati kiesések**: az adatkapcsolat megszakadhat, lyukak keletkeznek.
- **Szenzor-drift**: a műszer fokozatosan pontatlanná válik kalibrálás nélkül.
- **Óriási mennyiség**: egy szenzor-hálózat naponta gigabájtokat termelhet.

---

## Tisztítás, validáció és minőségértékelés

Az OECD tudományos AI-ról szóló jelentése és a National Academies adatminőségről szóló fejezete egyaránt hangsúlyozza: az adatminőség a tudományos AI-alkalmazások alapja. A mondás --- *"garbage in, garbage out"* --- sehol sem igazabb, mint az automatizált pipeline-okban. Ha a tisztítás rosszul működik, az elemzés is hibás lesz, és ami még rosszabb: automatikusan és észrevétlenül lesz hibás.

### Hiányzó értékek

A hiányzó értékek (*missing values*) a tudományos adatok leggyakoribb problémája. Szenzor leáll, beteg kihagyja a kontrollvizsgálatot, kérdőív-kitöltő kihagy egy kérdést.

**Stratégiák hiányzó értékekre:**

| Stratégia | Mikor használd? | Mikor NE használd? |
|-----------|-----------------|---------------------|
| **Törlés** (sor vagy oszlop elhagyása) | Ha kevés a hiányzó adat (<5%) és véletlenszerű a mintázata | Ha szisztematikus a hiány (pl. mindig éjjel hiányzik) |
| **Előző érték átvitele** (forward fill) | Idősoroknál, ahol az érték lassan változik | Gyorsan változó méréseknél |
| **Interpoláció** (lineáris vagy spline) | Idősoroknál, ahol a hiány rövid | Hosszú lyukaknál (>10% az ablaknak) |
| **Átlaggal/mediánnal pótlás** | Egyszerű elemzéseknél, ha a hiány véletlen | Ha a hiányzó minta korrelál a változóval |
| **Modell-alapú imputáció** (k-NN, MICE) | Ha sok változó van és fontos a pontosság | Ha nagyon kevés az adat |
| **Jelölés és meghagyás** (hiányzó marad hiányzó) | Ha az elemzés kezeli a NA-t natívan | Ha az elemzés nem tud NA-val dolgozni |

**Gyakorlati szabály:** Mindig dokumentáld, melyik stratégiát alkalmaztad és hány értéket pótoltál. Ez a reprodukálhatóság alapja.

**AI-asszisztált megközelítés:** Megkérheted az AI kódolási asszisztenst, hogy elemezze a hiányzó értékek mintázatát: *"Készíts egy hőtérképet, ami megmutatja, melyik szenzornál, melyik napszakban hiányzik a legtöbb adat. Használj missingno könyvtárat."* Ez segít eldönteni, hogy véletlenszerű-e a hiány, vagy szisztematikus probléma áll mögötte (pl. egy adott szenzor minden éjjel 2 és 4 óra között nem küld adatot).

### Outlier-ek (kiugró értékek)

Az outlier-ek kezelése tudományosan delikát kérdés. Egy kiugró érték lehet valódi tudományos felfedezés --- vagy lehet szenzor-hiba.

**Detektálási módszerek:**

- **Statisztikai küszöbök**: 3 szórás (sigma) szabály, IQR (interkvartilis terjedelem) módszer.
- **Fizikai küszöbök**: a hőmérséklet nem lehet -80 °C Debrecenben (a legalacsonyabb mért érték -35 °C volt). A páratartalom nem haladhatja meg a 100%-ot. Ezek domain-specifikus szabályok, amelyeket neked kell megadnod.
- **Idősor-alapú detektálás**: ha egy érték drasztikusan eltér az előző és következő méréstől (pl. a hőmérséklet 20 °C-ról 85 °C-ra ugrik, majd visszaesik).
- **Gépi tanulás alapú detektálás**: Isolation Forest, Local Outlier Factor. Ezek többdimenziós adatokban is megtalálják a szokatlan pontokat.

**Stratégiák outlier-ek kezelésére:**

1. **Jelöld meg, de ne töröld automatikusan.** Készíts egy `quality_flag` oszlopot a táblázatban, amely jelzi: `ok`, `suspect`, `invalid`.
2. **Vizsgáld meg a kontextust.** Ha a hőmérsékleti szenzor 85 °C-ot mutat, de a szomszédos szenzorok 22 °C-ot, az szenzor-hiba. Ha mind 85 °C-ot mutat, az valami más.
3. **Dokumentáld a döntést.** A pipeline naplójába írd bele, hány outlier-t detektáltál, és mit csináltál velük.
4. **Légy konzervatív.** Inkább hagyd benne a gyanúsat, és a végén az elemzésnél szűrd ki, mint hogy elveszíts egy valódi jelenséget.

### Formátum-standardizálás és séma-validáció

A "formátum-pokol" minden adatfeldolgozó rémálma. Íme a tipikus szituációk:

- **Dátumformátumok**: `2025.03.15`, `03/15/2025`, `15-Mar-2025`, `2025-03-15T08:00:00Z`. Ugyanaz a dátum, négyféleképpen.
- **Kódolás**: az ékezetes karakterek (`á`, `é`, `ő`, `ű`) különböző kódolásokban (UTF-8, Latin-2, Windows-1250) másképp néznek ki --- és ha rosszul olvasod be, értelmezhetetlen szöveget kapsz.
- **Egységek**: hőmérséklet Celsiusban vagy Fahrenheitben? Koordináták WGS84-ben, EOV-ban (HD72), vagy valami másban?
- **Oszlopnevek**: `Hőmérséklet`, `homerseklet`, `T_air`, `temp`, `TEMP_C` --- mind ugyanaz, de a gép nem tudja.
- **Szeparátorok**: tabulátor, vessző, pontosvessző, szóköz.

**Séma-validáció** azt jelenti, hogy formálisan leírod, milyen az "érvényes" adat:

- Milyen oszlopok kellenek?
- Milyen típusúak (szám, szöveg, dátum)?
- Milyen értéktartományba esnek?
- Van-e kötelező mező?

Ezt a sémát (schema) a pipeline elején alkalmazod: ha az új adat nem felel meg a sémának, a pipeline megáll és riaszt, ahelyett hogy hibás adattal dolgozna tovább.

**Példa séma-leírásra (pszeudokód):**

```
Állomás-adat séma:
  - station_id: szöveg, kötelező, 5 karakter
  - timestamp: dátum, kötelező, ISO 8601 formátum
  - temperature_c: szám, kötelező, -50.0 ... +55.0
  - humidity_pct: szám, opcionális, 0.0 ... 100.0
  - wind_speed_ms: szám, opcionális, 0.0 ... 80.0
  - precipitation_mm: szám, opcionális, >= 0.0
```

Ha a bejövő adatban a `temperature_c` oszlopban 999.9 jelenik meg (sok régi műszer így jelöli a hiányzó értéket), a séma-validáció elkapja, mert kívül esik a megengedett tartományon. Kézzel ezt könnyen elnézed --- automatikusan soha.

### Automatikus adatminőségi riportok

Egy jól felépített pipeline minden futás végén generál egy rövid minőségi riportot:

```
═══════════════════════════════════════════════════
  ADATMINŐSÉGI RIPORT — 2026-03-29 07:45:12 UTC
═══════════════════════════════════════════════════

  Forrás:         OMSZ FTP / 12 állomás
  Időszak:        2026-03-28 00:00 – 23:59 UTC
  Beolvasott sorok: 17,280

  HIÁNYZÓ ÉRTÉKEK:
    temperature_c:    23 (0.13%) — interpolálva
    humidity_pct:     156 (0.90%) — Debrecen-Kelet szenzor kiesés 02:00–04:30
    wind_speed_ms:    0 (0.00%)
    precipitation_mm: 0 (0.00%)

  OUTLIER-EK:
    temperature_c:    2 megjelölve (station HB003, 18:15 és 18:30)
    humidity_pct:     0

  SÉMA-VALIDÁCIÓ:    PASSED

  ÖSSZESÍTÉS:        MINŐSÉG: 98.97% — ELFOGADHATÓ
═══════════════════════════════════════════════════
```

Ez a riport automatikusan generálódik, elmenthető fájlba, elküldhető e-mailben, és hónapok, évek múlva is visszakereshető. Ha egy kolléga megkérdezi: "A márciusi adatodban volt szenzor-kiesés?" --- nem kell emlékezned, hanem visszanézed a riportot.

### AI-asszisztált anomália-detektálás

Az eddig leírt módszerek --- statisztikai küszöbök, fizikai korlátok, séma-validáció --- szabály-alapúak. Előre megmondod a gépnek, mit keressen. De mi van azokkal az anomáliákkal, amelyeket nem tudsz előre definiálni?

Itt jön képbe az AI-asszisztált anomália-detektálás. A gépi tanulás (*machine learning*) képes megtanulni, milyen a "normális" adat, és jelezni, ha valami eltér a megszokottól --- akkor is, ha nem tudsz explicit szabályt írni rá.

**Példák:**

- **Szenzor-drift**: a hőmérsékleti szenzor fokozatosan, napról napra fél fokkal többet mutat. Egyetlen napon belül nem tűnik fel, de egy hét alatt már 3.5 °C az eltérés. Egy autoencoderrel vagy egyszerű ARIMA-modellel detektálható a trend.
- **Szokatlan mintázatok**: egy biodiverzitási felmérésben az egyik megfigyelő minden fajból pontosan 10 egyedet jelent minden héten. Ez statisztikailag nagyon valószínűtlen --- felmerül a gyanú, hogy az adatot kitalálta.
- **Kontextuális anomáliák**: 25 °C hőmérséklet januárban Debrecenben anomália. Júliusban normális. Az AI figyelembe tudja venni az időbeli kontextust.

A National Academies jelentése kiemeli az adatproveniencia (data provenance) fontosságát: minden adatnál dokumentálni kell, ki, mikor, milyen eszközzel és milyen feldolgozási lépésekkel állította elő. Ez az automatizált pipeline-oknak "ingyen" jön: a pipeline-kód maga a dokumentáció, és a futtatási naplók a proveniencia-rekordok.

---

## Kötegelt feldolgozás nagy mennyiségben

Anna 12 állomás egynapos adatát dolgozza fel. De mi van, ha:

- 500 mérőállomásod van az egész országban?
- 30 év napi adatát kell újrafeldolgoznod, mert javítottad a kalibráló algoritmust?
- 10,000 mikroszkópfelvételt kell feldolgoznod és klasszifikálnod?
- 2,000 kérdőívet kell kódolnod és tisztítanod?

Ekkor már nem elég egy "script, ami végigmegy a fájlokon". Kötegelt feldolgozásra (*batch processing*) van szükség, és itt az automatizálás nem luxus, hanem az egyetlen lehetőség.

### A kötegelt feldolgozás alapelvei

**1. Mappaalapú szervezés**

Használj egyértelmű mappastruktúrát:

```
projekt/
├── raw/           ← nyers adat (SOHA ne írd felül!)
│   ├── 2026-03-28/
│   └── 2026-03-29/
├── processed/     ← feldolgozott adat
│   ├── 2026-03-28/
│   └── 2026-03-29/
├── reports/       ← minőségi riportok
├── logs/          ← futtatási naplók
└── failed/        ← hibás fájlok (manuális ellenőrzésre)
```

**Aranyszabály: a nyers adatot soha ne módosítsd.** A `raw/` mappa szentség. Ha újra kell futtatnod a pipeline-t, a nyers adatból mindig reprodukálhatod az eredményt.

**2. Fájl-szintű hibakezelés**

Kötegelt feldolgozásnál előfordul, hogy 500 fájlból 3 hibás. A pipeline-nak nem szabad megállnia emiatt. Az egészséges viselkedés:

1. Feldolgozza az érvényes fájlokat.
2. A hibásakat átmásolja a `failed/` mappába.
3. A naplóba beírja, melyik fájl miért bukott.
4. A végén összesít: "497 sikeres, 3 hibás --- részletek a naplóban."

**3. Párhuzamos feldolgozás**

Ha 10,000 fájl mindegyikét egymás után dolgozod fel, és mindegyikre 2 másodperc jut, az 5.5 óra. Ha 16 szálon párhuzamosítod, az 20 perc. Egy modern gépen (amilyen a te AMD 9950X processzorod 32 szállal, vagy a Debreceni Egyetem Komondor szuperszámítógépe) ez hatalmas különbség.

A Python `multiprocessing` könyvtára és a `concurrent.futures` modul lehetővé teszi, hogy az AI asszisztenseddel gyorsan írhatsz párhuzamosan futó pipeline-okat. Nem kell értened a párhuzamos programozás elméletét --- elég annyit mondanod: *"Alakítsd át ezt a scriptet, hogy egyszerre 16 fájlt dolgozzon fel párhuzamosan."*

**4. Ellenőrzőpont (checkpoint)**

Hosszú futásoknál (pl. 30 éves adatsor újrafeldolgozása) érdemes ellenőrzőpontokat tenni: a pipeline minden tizedik nap feldolgozása után elmenti az állapotát. Ha a 247. napnál valamiért leáll (áramszünet, memória-hiba), nem kell elölről kezdenie, hanem a 240. naptól folytatja.

### Esettanulmány: 30 éves meteorológiai archívum újrafeldolgozása

Tegyük fel, hogy Anna tanszéke kidolgozott egy javított kalibrációs algoritmust a régi hőmérsékleti szenzorokhoz. Ezt visszamenőlegesen alkalmazni kell az elmúlt 30 év összes adatára: 10,950 napi fájl, egyenként 1,440 mérés (10 perces felbontás), 12 állomás. Összesen: közel 190 millió mérés.

Kézzel? Lehetetlen. Egy egyszerű Python scripttel, sorosan? Napokig futna. Egy jól megírt pipeline-nal, 16 szálon párhuzamosítva, ellenőrzőpontokkal? Néhány óra.

A pipeline lépései:

1. **Fájllista összeállítása**: minden napi fájl elérési útja a `raw/` mappából.
2. **Párhuzamos feldolgozás**: 16 szálon, minden szál egy-egy napot dolgoz fel.
3. **Minden napra**: beolvasás → régi kalibráció eltávolítása → új kalibráció alkalmazása → validáció → mentés a `processed/` mappába.
4. **Checkpoint**: minden 100. nap után mentés.
5. **Végső riport**: összesen hány mérés, hány javítva, mekkora a maximális eltérés a régi és új kalibráció között.

---

## Ütemezett feladatok és monitorozás

A pipeline megvan --- de ki indítja el? Ha Anna minden reggel kézzel, akkor nem automatizáltunk semmit, csak a lépéseket kódoltuk le. Az igazi automatizálás az, amikor a pipeline magától fut.

### Ütemezett futtatás: cron job

A `cron` (Linux/macOS) és a Task Scheduler (Windows) rendszerszintű ütemezők, amelyek időzítve indítanak programokat.

**Néhány tipikus cron ütemezés:**

| Ütemezés | Cron kifejezés | Mikor fut? |
|----------|---------------|------------|
| Minden reggel 7:00 | `0 7 * * *` | Naponta egyszer |
| Minden óra elején | `0 * * * *` | 24-szer naponta |
| Minden hétfőn 6:00 | `0 6 * * 1` | Hetente egyszer |
| Minden hónap 1-jén | `0 0 1 * *` | Havonta egyszer |
| Minden 15 percben | `*/15 * * * *` | 96-szor naponta |

Anna pipeline-ja például így ütemezett: `0 7 * * * python /home/anna/pipeline/run_daily.py`

Ez annyit jelent: minden nap reggel 7:00-kor a rendszer automatikusan elindítja a pipeline-t. Annának nem kell ott lennie. Ha szabadságon van, a pipeline akkor is fut. Ha beteget jelent, a pipeline akkor is fut.

### Fájlfigyelők (watchdog)

Néha nem időzítve akarod indítani a pipeline-t, hanem akkor, amikor új adat érkezik. A "watchdog" (fájlfigyelő) monitorozza egy adott mappát, és ha új fájl jelenik meg benne, automatikusan elindítja a feldolgozást.

**Tipikus forgatókönyv:** A laboratóriumi spektrométer minden mérés végén kiír egy `.csv` fájlt a `C:\spectrometer\output\` mappába. A watchdog figyeli ezt a mappát. Amint megjelenik egy új fájl, a pipeline automatikusan beolvassa, feldolgozza, és az eredményt beteszi az adatbázisba. A kutató a mérés befejezése után 30 másodperccel már látja az eredményt a webes dashboardon.

### Monitorozás és riasztás

Az automatizált pipeline legnagyobb veszélye a *"csendben rosszul működés"*. A pipeline fut, nem ad hibát, de az eredmény rossz --- mert megváltozott az adatforrás formátuma, vagy egy szenzor tönkrement, és a hiánypótlás elfedte a problémát.

**Három szintű monitorozás:**

**1. Futtatási napló (log)**

Minden pipeline-futás részletes naplót ír:
- Mikor indult?
- Hány fájlt dolgozott fel?
- Hány hibát talált?
- Mennyi ideig tartott?
- Sikeresen befejeződött-e?

**2. Automatikus e-mail riasztás**

A pipeline küld e-mailt, ha:
- Hibával állt meg.
- Az adatminőség egy küszöb alá esik (pl. <95%).
- Nem kapott adatot (a forrás nem elérhető).
- Szokatlanul sok outlier-t talált.

**Példa riasztó e-mail:**

```
Tárgy: [PIPELINE RIASZTÁS] Debrecen-Kelet szenzor adathiány

A napi meteorológiai pipeline a 2026-03-29-i futás során
a következő problémát észlelte:

  Állomás:     Debrecen-Kelet (HB003)
  Probléma:    Nincs adat 02:00–06:30 UTC között
  Érintett:    27 mérési ciklus (4.5 óra)
  Hatás:       Napi átlag megbízhatósága csökkent

  Automatikus kezelés: interpoláció alkalmazva
  Javasolt teendő:     Szenzor-ellenőrzés szükséges

  Részletek: /data/reports/2026-03-29_quality.html
```

**3. Dashboard (opcionális)**

Ha több pipeline-od fut párhuzamosan, érdemes egy egyszerű webes dashboardot felállítani, ahol egy pillantással látod:
- Melyik pipeline futott utoljára?
- Melyik sikerült, melyik nem?
- Hogyan alakul az adatminőség az elmúlt 30 napban?

Ez már a haladóbb kategória, de az AI asszisztenssel egy egyszerű Streamlit dashboard (Ch 13) néhány perc alatt összerakható.

---

## Pipeline-eszközök: az egyszerűtől a komplexig

A pipeline-építés eszköztára rendkívül széles. A kulcs: mindig a legegyszerűbb eszközzel kezdj, és csak akkor lépj tovább, ha valóban szükséges.

### Első szint: egyszerű Python scriptek

**Mikor elég?**
- Egy kutató, egy projekt, néhány tucat fájl.
- Lineáris pipeline (A → B → C → D), nincs elágazás.
- Ritkán változik (heti vagy havi futtatás).
- Nincs szükség párhuzamos futtatásra több gépen.

**Hogyan épül fel?**

Egy tipikus egyszerű pipeline egyetlen Python fájl, amely függvényekre van bontva:

```
run_pipeline.py
├── load_data()          ← Bevitel
├── clean_data()         ← Tisztítás
├── validate_schema()    ← Validáció
├── transform_data()     ← Transzformáció
├── analyze()            ← Elemzés
├── generate_report()    ← Kimenet
└── main()               ← Orchestráció
```

Ezt a `main()` függvény hívja sorrendben, és ha bármelyik lépés hibát dob, a `try/except` blokk elkapja és naplózza.

**Előnyök:**
- Egyszerű, átlátható, egy fájlban van minden.
- Nincs külön rendszer telepítendő.
- Az AI kódolási asszisztens percek alatt megírja.

**Korlátok:**
- Ha egy lépés elszáll, az egész pipeline-t újra kell futtatni.
- Párhuzamos futtatás nehézkes.
- Nincs beépített monitoring, ütemezés, retry.
- Nehéz nyomon követni, melyik lépés mikor futott.

**Anna napi pipeline-ja tökéletesen megvalósítható egyetlen Python scripttel.** A legtöbb kutató számára ez az optimális szint.

### Második szint: Dagster --- modern adat-orkesztrátor

**Mikor kell Dagster?**
- Több, egymásra épülő pipeline van egy projekten belül.
- Fontos, hogy egy lépés megismételhető legyen anélkül, hogy az egészet újra futtatnád.
- Fontos a vizuális követhetőség: melyik lépés futott, melyik nem.
- A projekt nő, és több ember dolgozik rajta.

**Mi a Dagster?**

A Dagster egy nyílt forráskódú adatorchestration platform. A pipeline-t "asset"-ekre (adategységekre) bontod: minden asset egy jól definiált adattermék, amelynek megvan a saját előállítási logikája. A Dagster automatikusan felépíti a függőségi gráfot (melyik asset függ melyiktől), és csak azokat a lépéseket futtatja újra, amelyek szükségesek.

**A Dagster megközelítése:**

Hagyományos script:
```
"Futtasd az A, B, C, D lépéseket ebben a sorrendben."
```

Dagster:
```
"Van négy adattermék: A, B, C, D.
 B függ A-tól. C függ B-től. D függ B-től és C-től.
 Tartsd ezeket naprakészen."
```

A különbség az, hogy a Dagster tudja: ha csak A változott, elég B-t, C-t és D-t újraszámolnia. Ha C-ben találtál egy hibát és kijavítottad, elég C-t és D-t újra futtatni --- A-t és B-t nem.

**Dagster felhasználói felülete:**

A Dagster egy webes felületet (Dagit) ad, ahol:
- Látod a pipeline gráfját (melyik asset hova vezet).
- Elindíthatsz futtatásokat.
- Megnézheted a futtatási történetet és a naplókat.
- Beállíthatsz ütemezőt (a cron helyettesítése).

**Mikor NEM kell Dagster?**

Ha egy egyszerű Python script elég, ne bonyolítsd Dagsterrel. A Dagster telepítése, tanulása és karbantartása többlet-erőforrás. Csak akkor éri meg, ha a pipeline-jaid komplexitása és a csapatmunka valóban igényli.

### Harmadik szint: Nextflow --- tudományos munkafolyamatok

**Mikor kell Nextflow?**
- Bioinformatikai pipeline (szekvenálási adatok feldolgozása).
- A pipeline lépései különböző szoftvereket igényelnek (nem csak Python).
- HPC (szuperszámítógép) vagy felhő-erőforrásokat használsz.
- A pipeline-nak konténerben (Docker/Singularity) kell futnia.

**Mi a Nextflow?**

A Nextflow egy munkafolyamat-kezelő rendszer, amelyet kifejezetten tudományos, elsősorban bioinformatikai pipeline-okra terveztek. Különlegessége, hogy a pipeline lépései ("process"-ek) futhatnak különböző gépeken, konténerekben, vagy felhőben --- a Nextflow automatikusan kezeli az ütemezést, az erőforrás-allokációt, és a hibakezelést.

**A Nextflow ökoszisztémája:**

- **nf-core**: a bioinformatikai közösség által karbantartott, minőségbiztosított pipeline-gyűjtemény. Több mint 100 pipeline áll rendelkezésre, a teljes genom szekvenálástól az RNS-seq elemzésen át a metagenomikáig.
- **Nextflow Tower**: webes felület a futtatások monitorozásához.

**Példa nf-core pipeline-ok:**
| Pipeline | Funkció |
|----------|---------|
| nf-core/rnaseq | RNS szekvenálás teljes elemzése |
| nf-core/sarek | Szomatikus és csíravonal variáns-hívás |
| nf-core/ampliseq | 16S/ITS amplikonszekvenálás (mikrobiom) |
| nf-core/fetchngs | Adatletöltés SRA/ENA-ból |

**Mikor NEM kell Nextflow?**

Ha a pipeline-od teljesen Python-alapú, egyetlen gépen fut, és nem bioinformatikai --- akkor a Nextflow feleslegesen komplex. Használj egyszerű scriptet vagy Dagstert.

### A megfelelő eszköz kiválasztása

```
                    ┌─────────────────────┐
                    │ A pipeline lineáris │
                    │ és egyszerű?        │
                    └───────┬─────────────┘
                            │
                      Igen ─┤─ Nem
                            │     │
                 ┌──────────▼──┐  │
                 │ Egyszerű    │  │
                 │ Python      │  │
                 │ script      │  │
                 └─────────────┘  │
                                  │
                    ┌─────────────▼─────────┐
                    │ Több ember dolgozik   │
                    │ rajta, vagy komplex   │
                    │ függőségek vannak?    │
                    └───────┬───────────────┘
                            │
                      Igen ─┤─ Nem (hanem HPC/bio)
                            │     │
                 ┌──────────▼──┐  │
                 │ Dagster     │  │
                 └─────────────┘  │
                                  │
                         ┌────────▼─────────┐
                         │ Nextflow         │
                         └──────────────────┘
```

**Praktikus összefoglaló:**

| Szempont | Python script | Dagster | Nextflow |
|----------|--------------|---------|----------|
| Tanulási küszöb | Alacsony | Közepes | Magas |
| Telepítés | Nincs extra | `pip install dagster` | Java + Nextflow |
| Vizuális felület | Nincs | Dagit (web) | Tower (web) |
| Ütemezés | Cron | Beépített | Beépített |
| Párhuzamosítás | Kézi | Automatikus | Automatikus |
| HPC/felhő | Nem | Lehetséges | Natív |
| Konténerizáció | Opcionális | Opcionális | Natív |
| Közösségi pipeline-ok | Nincs | Kevés | nf-core (100+) |
| Ideális méret | 1 kutató, 1 projekt | Csapat, több pipeline | Bioinf., HPC |

**A legjobb tanács:** Kezdj egyszerű Python scripttel. Ha kinövöd, lépj Dagsterre. Ha HPC-re vagy bioinformatikára kell, nézd meg a Nextflow-t. Ne a legkomplexebb eszközt válaszd "mert úgy professzionálisabb" --- válaszd azt, ami a feladathoz passzol.

---

## Reprodukálhatóság: hogy a pipeline holnap is ugyanazt csinálja

A tudományos kutatás egyik legfontosabb alapelve a reprodukálhatóság: ha valaki más (vagy te magad egy év múlva) megismétli az elemzésedet, ugyanarra az eredményre kell jutnia. A pipeline-ok ebben hatalmas segítséget nyújtanak --- de csak akkor, ha tudatosan kezeled a környezetet, a dokumentációt és a függőségeket.

### A "működik a gépemen" probléma

Tipikus szituáció: megírod a pipeline-t a saját laptopodra. Minden működik. Egy év múlva a kollegád megpróbálja futtatni, és nem megy, mert:

- Frissítettél egy Python könyvtárat, és az új verzió másképp működik.
- A te gépeden van telepítve egy rendszerszintű program (pl. `ffmpeg`, `gdal`), amit a kollegád gépén nem találsz.
- A te géped Windows, a szervered Linux.
- A Python verziód 3.11 volt, most 3.13 van, és valami megváltozott.

### 1. Környezetkezelés: virtuális környezetek és requirements

A legegyszerűbb lépés: használj virtuális környezetet (*virtual environment*) és rögzítsd az összes függőséget.

A Python `venv` modulja elkülönített környezetet hoz létre, ahol a könyvtárak nem keverednek a rendszer többi projektjével.

Ami feltétlenül kell a pipeline mellé:

- **`requirements.txt`**: az összes Python könyvtár pontos verziója. Nem `pandas`, hanem `pandas==2.2.1`. Nem "a legújabb", hanem "pontosan ez a verzió".
- **Python verzió dokumentálása**: a `README`-ben vagy egy `.python-version` fájlban.
- **Operációs rendszer és rendszerfüggőségek**: ha a pipeline Linux-specifikus, írd le.

### 2. Dokumentáció: amit nem írsz le, azt elfelejted

Egy jó pipeline mellé a következő dokumentáció kell:

**a) README fájl**

Tartalmazza:
- Mit csinál a pipeline?
- Hogyan telepíted és futtatod?
- Milyen bemeneti adatot vár, milyen formátumban?
- Milyen kimenetet ad?
- Kik a szerzők, mikor készült?

**b) Változásnapló (changelog)**

Ha módosítasz valamit a pipeline-on, jegyezd fel:
- Mikor?
- Mit változtattál?
- Miért?

Ez különösen fontos, ha az eredmények megváltoznak --- vissza kell tudnod keresni, melyik módosítás okozta.

**c) A pipeline-kód maga a dokumentáció**

Ha a kódot jól írtad meg (érthető változónevek, kommentek a kulcspontokon), maga a kód dokumentálja az adatfeldolgozás logikáját. Ez sokkal megbízhatóbb, mint egy külön Word-dokumentum, ami könnyen elavulttá válik.

### 3. Verziókezelés: Git

Az 5. fejezetben bevezettük a Git verziókezelő rendszert. A pipeline-kód verziókezelése nem opcionális --- kötelező.

- **Minden változtatás nyomon követhető**: ki, mikor, mit módosított.
- **Visszaállítható**: ha az új verzió hibás, egy paranccsal visszaállhatsz a régi verzióra.
- **Elágazások (branch-ek)**: kipróbálhatsz egy új tisztítási algoritmust anélkül, hogy a működő pipeline-t elrontanád.

### 4. Konténerizáció: a végső megoldás

Ha a virtuális környezet és a `requirements.txt` nem elég (mert rendszerszintű függőségek is vannak, vagy különböző operációs rendszerek között kell futtatni), a konténerizáció a megoldás. Ennek részleteit az A függelékben (Appendix A) tárgyaljuk, de az alapkoncepció fontos:

Egy **konténer** (container) az alkalmazásod teljes futtatási környezetét csomagolja össze: operációs rendszer, Python, könyvtárak, rendszer-programok, a pipeline-kódod --- mindent. Aki megkapja a konténer-leírást (Dockerfile), bármilyen gépen pontosan ugyanazt a környezetet tudja előállítani.

**Gondolj rá úgy, mint egy csomagküldő dobozra**: a pipeline benne van, az összes függőségével együtt, és akárhova elküldöd, ugyanaz lesz benne, mint amikor becsomagoltad.

---

## Gyakorlati útmutató: pipeline építése lépésről lépésre

Foglaljuk össze a fejezet tanulságait egy gyakorlati útmutatóban. Ha holnap szeretnéd elkezdeni az első pipeline-odat, kövesd ezeket a lépéseket:

**1. Írd le a munkafolyamatodat.**
Számozd meg a lépéseket, ahogy Anna is tette. Ne hagyj ki semmit --- beleértve a "kézzel megnyitom a fájlt" jellegű lépéseket is.

**2. Sorold be minden lépést az öt szakasz egyikébe.**
Bevitel, tisztítás, transzformáció, elemzés, kimenet.

**3. Töltsd ki az automatizálási ellenőrző listát.**
Ha 8+ pont, érdemes automatizálni.

**4. Kezdd a legfájdalmasabb lépéssel.**
Nem kell az egészet egyszerre automatizálni. Válaszd ki azt az egy-két lépést, ami a legtöbb időt vagy a legtöbb hibát okozza, és azzal kezdj.

**5. Kérd meg az AI asszisztensedet.**
Pl.: *"Írj egy Python scriptet, ami beolvassa az összes CSV fájlt a raw/ mappából, kiszűri azokat a sorokat, ahol a hőmérséklet hiányzik vagy 50 fok felett van, és elmenti az eredményt a processed/ mappába. Készítsen naplót a kiszűrt sorokról."*

**6. Tesztelj valós adattal.**
Ne szintetikus példa-adattal tesztelj, hanem az igazi fájljaiddal. A probléma mindig a valós adatban van: a váratlan formátum, a hiányzó oszlop, a furcsa kódolás.

**7. Automatizáld a futtatást.**
Ha a script működik, ütemezd cron-nal vagy watchdog-gal.

**8. Állíts be monitorozást.**
Legalább egy e-mail riasztás, ha a pipeline hibával áll meg.

**9. Verziókezeld a kódot.**
`git init`, `git add`, `git commit` --- minden módosítás után.

**10. Rögzítsd a környezetet.**
`pip freeze > requirements.txt` --- minden telepítés után.

---

## Debreceni esettanulmány: a Tisza vízminőségi monitorozása

A Debreceni Egyetem Környezettudományi Tanszékén egy kutatócsoport a Tisza vízminőségét monitorozza. Négy mérőállomásról érkeznek 15 perces adatok: vízhőmérséklet, pH, vezetőképesség, oldott oxigén, zavarosság. A nyers adatok egy helyi szerverre töltődnek fel FTP-n.

**A régi munkafolyamat (manuális):**
- Egy doktorandusz hetente letöltötte a fájlokat.
- Excelben összevonta őket egyetlen táblázatba.
- Kézzel ellenőrizte a fizikai tartományokat (pH 0-14, hőmérséklet -5...+35 °C).
- Készített egy heti grafikont és e-mailben elküldte a témavezetőjének.
- Átlagosan 3 óra/hét.

**Az automatizált pipeline:**
1. **Bevitel**: cron job óránként ellenőrzi az FTP szervert, és letölti az új fájlokat a `raw/` mappába.
2. **Tisztítás**: séma-validáció (oszlopok és típusok ellenőrzése), fizikai tartomány-ellenőrzés, hiányzó értékek jelölése.
3. **Anomália-detektálás**: Isolation Forest modell figyeli a szokatlan mintázatokat (pl. hirtelen pH-csökkenés, ami szennyezésre utalhat).
4. **Transzformáció**: egységesített idősorba rendezés, 15 perces → óránkénti → napi aggregálás.
5. **Kimenet**: automatikus heti riport (PDF), anomália-riasztás e-mailben (azonnal), frissített adatbázis.

**Eredmény:**
- 3 óra/hét → 0 óra/hét manuális munka.
- Riasztás perceken belül (korábban legrosszabb esetben egy hétig nem vették észre a problémát).
- Teljes reprodukálhatóság: minden futtatás naplózva, a nyers adat érintetlen.
- A doktorandusz végre arra tudja fordítani az idejét, amire jött: kutatni.

---

## Összefoglalás

- A **pipeline** (adatfeldolgozási csővezeték) az ismétlődő adatfeldolgozási lépések automatizált láncolata: bevitel → tisztítás → transzformáció → elemzés → kimenet.
- Az automatizálás nem csak időt takarít meg, hanem **csökkenti a hibákat** és **biztosítja a reprodukálhatóságot**.
- Az **adatminőség** nem magától jön: hiányzó értékek, outlier-ek, formátum-problémák kezelése tudatos tervezést igényel.
- **AI-asszisztált anomália-detektálás** olyan mintázatokat is felfedezhet, amelyeket szabály-alapú rendszerek nem.
- Az **ütemezés** (cron) és a **monitorozás** (naplók, e-mail riasztások) teszi a pipeline-t igazán autonómmá.
- Az eszközválasztás legyen **progresszív**: egyszerű Python script → Dagster → Nextflow, mindig a feladathoz mérten.
- A **reprodukálhatóság** alapfeltétele: verziókezelés (Git), környezetrögzítés (`requirements.txt`), és dokumentáció.
- A nyers adatot **soha ne módosítsd** --- mindig őrizd meg az eredeti verziót.

> A következő fejezetben (Ch 8) a vizuális programozás és a no-code automatizálás felé lépünk tovább: az n8n, KNIME és más eszközökkel olyan munkafolyamatokat építhetsz, amelyekhez egyáltalán nem kell kódot írnod.

---

*Irodalomjegyzék:*

- Gentemann, C. L., et al. (2021). "Science Storms the Cloud." *AGU Advances*, 2(2). --- A tudósok 80%-os adatrendezési problémájáról.
- Wilkinson, M. D., et al. (2016). "The FAIR Guiding Principles for Scientific Data Management and Stewardship." *Scientific Data*, 3(1):160018.
- Ziemann, M., Eren, Y., & El-Osta, A. (2016). "Gene name errors are widespread in the scientific literature." *Genome Biology*, 17(1):177. --- Az Excel gén-név konverziós probléma.
- National Academies of Sciences (2025). *AI in the Life Sciences.* Ch 5: Importance of Data. --- Adatminőség, proveniencia, FAIR elvek.
- OECD (2023). *AI in Science.* Ch 15: AI for Earth and Environmental Sciences.
- Di Tommaso, P., et al. (2017). "Nextflow enables reproducible computational workflows." *Nature Biotechnology*, 35(4):316--319.
