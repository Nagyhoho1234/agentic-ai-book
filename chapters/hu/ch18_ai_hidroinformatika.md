# 18. fejezet — AI a hidroinformatikában

> **Fejezet-információ**
> - **Kinek szól:** Hidrológusoknak, vízügyi mérnököknek és környezetkutatóknak
> - **Előismeretek:** 1-4. fejezet (AI alapok); a 5-12. fejezet hasznos, de nem kötelező
> - **Amit megtanulsz:**
>   - Az AI alkalmazása felszíni és felszín alatti vízmodellezésben
>   - Pipeline-ok, kódgenerálás és digitális ikrek vízügyi kontextusban
>   - Autonóm ágensek vízgyűjtő-szintű kalibrációra
> - **Szükséges eszközök:** Böngésző + terminál + Python
> - **Kapcsolódó fejezetek:** 6. fejezet (modellezés), 7. fejezet (pipeline-ok), 10. fejezet (digitális ikrek), 19. fejezet (térinformatika)

---

## Nyitó jelenet: A Tisza nem var

Képzeld el a következő helyzetet. 2024 marciusaban a kárpáti forrásvidéken harom egymást követő ciklonrendszer huz at. Az első nap 40 mm eso esik az ukran hegyvidéken, a második nap újabb 55 mm, a harmadikon a hóolvadás is beindul. A Tisza felso szakaszan Rahonal a vízszint órák alatt emelkedik, és az árhullám megkezdi útját lefele -- Tokaj, Tiszafured, Kiskor, Szolnok, Szeged fele. A magyar vízügyi szolgálatnak harom kérdésre kell válaszolnia, és gyorsan:

1. Milyen magasra emelkedik a viz Szolnoknal, és mikor érkezik a tetőszint?
2. A Nagy Magyar Alföldön a sekely talajvíz reagal-e az árhullámra, és ha igen, mely települések kutjai kerulnek veszélybe?
3. A Hortobagy vízmérlegében milyen változásokat okoz az esemeny a következő harom hónapban?

Tizenot evvel ezelott ezekre a kerdesekre három külön csapat dolgozott volna, három külön szoftverrel, háromféle adatforrásból. A felszíni vizesek HEC-HMS-t futtattak volna kezi paraméterezéssel. A talajvízesek MODFLOW-t építettek volna heti adat-frissítési ciklussal. A vízmérleg-elemzok Excel-tablazatokat toltogettenek. Az eredmenyek összefűzésére senki nem vállalkozott volna, mert az adatformátum-konverziók és az idoletezsi kihivasok következetesen meghaladták a rendelkezésre álló idot.

2026-ban az AI megváltoztatja ezt a kepet. Nem azert, mert a fizika lett egyszerűbb -- a Saint-Venant-egyenletek, a Boussinesq-egyenlet és a Richards-egyenlet ma is ugyanolyan bonyolultak, mint szaz eve. Hanem azert, mert az AI képessé teszi a hidrológust arra, hogy:

- **Automatizálja** az adatgyűjtést és minőség-ellenőrzést (7. fejezet pipeline-jai vízügyi kontextusban)
- **Generáltassa** a numerikus kódjait (5. fejezet kódolási asszisztensei vizmodellekre alkalmazva)
- **Taníttasson** gépi tanulási modelleket vízszint-előrejelzésre (6. fejezet modellezés)
- **Építsen** RAG-alapu chatbotokat vízügyi szabályozási dokumentumokra (9. fejezet)
- **Létrehozzon** digitális ikreket vízgyűjtő-szinten (10. fejezet)
- **Futtathasson** autonóm ágenseket, amelyek önállóan kalibrálják a modelleket (11--12. fejezet)

Ez a fejezet végigvezet azon, hogyan alkalmazható az Agentikus AI Tudosoknak konyvben tanult minden technika egyetlen konkrét szakterületen: a **hidroinformatikan** -- a víztudomány, a térinformatika, a számítási modellezés és az adattudomány metszetében álló tudományágon.

---

## 18.1 A víztudomány digitalis forradalma

> **🖼️ Ábra: A hidroinformatika öt pillére és az AI kapcsolódási pontjai**
> *Five-pillar diagram showing hydrology, GIS, computational modeling, data science, and real-time systems, with AI connection lines between all pillars, water-themed color palette*

### 18.1.1 Mitol hidroinformatika a hidroinformatika?

A hidroinformatika nem egyszerű vízügy plusz informatika. A vízproblémák eredendoen terbeliek (egy adott vízgyűjtőre, talajretegre, mederszelvenyre vonatkoznak), eredendoen idősorjellegúek (orak, napok, evszakok, evtizedek alatt fejlodnek), és eredendoen adatigenyesek (műholdas adatok, terepi meresek, időjárási modellek és demografiai adatbázisok osszekapcsolasat igenylik). Ez a harom jellemző egyutt magyarazza, miért különösen alkalmas a víztudomány az AI-ra: a feladatok többsége nagy mennyisegu, heterogen, térbeli-időbeli adat feldolgozásat és osszefuzeset igenylo, iteratív munka -- vagyis pontosan az, amiben az AI kituno.

A hidroinformatika ot pillerre epul:

| Piller | Lenyeg | AI-relevancia |
|--------|--------|---------------|
| **Hidrologia** | A viz korforgas fizikaja | Az AI leforditja az egyenleteket kodra (6. fejezet) |
| **Térinformatika (GIS)** | Térbeli adatok tarolasa, elemzése | Az AI generálja a DEM-feldolgozási szkripteket (5. fejezet) |
| **Szamitasi modellezés** | Numerikus szimuláció | Az AI autonóman kalibralja a modelleket (11--12. fejezet) |
| **Adattudomany** | Meresi adatok feldolgozása | Az AI epittet pipeline-okat (7. fejezet) |
| **Valos ideju rendszerek** | Operativ előrejelzés, monitoring | Az AI digitális ikreket futtat (10. fejezet) |

### 18.1.2 A kezi elemzéstol az autonóm modellezésig

A víztudomány fejlődése az elmult évtizedekben négy fázison ment at:

**1. fazis: Kézi elemzés (1950-es--1990-es evek).** A hidrológus kezi számításokkal, táblázatokkal és grafikus módszerekkel dolgozott. Egy vízgyűjtő lehatárolás napokat vett igénybe topográfiai térképen, vonalzoval és planiméterrel.

**2. fazis: GIS-alapu elemzés (1990-es--2010-es evek).** A térinformatika lehetővé tette a térbeli adatok digitális tárolását és elemzéset. Az ArcGIS és a QGIS eszközei automatizálták a terepfeldolgozást, de minden lépést kézzel kellett elkezdeni és vezérelni indítani.

**3. fazis: Szkript-alapu automatizalas (2010-es evek).** A Python, az R és a parancssor-alapú eszközök (TauDEM, WhiteboxTools) lehetővé tettek a munkafolyamatok megismételhető futtatását. Egyetlen szkript ezer vízgyűjtőt képet feldolgozni egyetlen éjszaka alatt -- de a szkriptet embernek kellett megírnia, debuggolnia és karbantartania.

**4. fazis: AI-támogatott és agentikus modellezés (2023-tol).** A nagy nyelvi modellek (LLM-ek) és az ágensrendszerek lehetővé teszik, hogy a hidrológus természetes nyelven fogalmazza meg a feladatot, az AI pedig generálja a kodot, futtatja a modellt, kiértékeli az eredményt, és iterál. A vízügy embere nem programozó -- víztudós, akinek az AI az asszisztense.

Ez a fejezet a negyedik fazisrol szol.

---

## 18.2 AI a hidrologiai adatgyűjtésben

> **🖼️ Ábra: Vízügyi adat-pipeline — az OVF vízmércéktől a riasztási rendszerig**
> *Flow diagram showing water data pipeline: gauging stations → data cleaning → transformation → analysis → dashboard/alerts, with Hungarian river map background, technical illustration*

### 18.2.1 A vízügyi adatok sokfélesége

Mielott bármi modellt építenél, adatokra van szükséged. A víztudományban az adatforrások szokatlanul sokfélék:

| Adattipus | Forras | Idofelbontás | Térbeli lefedes |
|-----------|--------|--------------|-----------------|
| **Vizszint** | Automata vízmérceállomás (OVF hydroinfo.hu) | 15 perc -- 1 ora | Pontszeru (98 allomas Mo.-on) |
| **Csapadek** | Terepi csapadékmérők (OMSZ) | 10 perc -- 1 nap | Pontszeru (>200 allomas) |
| **Muholdas csapadek** | GPM IMERG, ERA5 reanalízis, Copernicus | 30 perc -- 1 nap | Racsos (0,1--0,25 fok) |
| **Talajvízszint** | Monitoring kutak (OVF) | Het -- honap | Pontszeru (>2000 kut) |
| **Időjárás-előrejelzés** | ECMWF, GFS, HRRR | 1--6 ora | Racsos (0,25--3 km) |
| **Távérzékelés** | Sentinel-2 (optikai), Sentinel-1 (radar) | 5--6 nap | 10--20 m felbontás |
| **Terepmodell (DEM)** | SRTM, Copernicus DEM, LiDAR | Statikus | 1--30 m felbontás |

A kihivas nem az, hogy ezek az adatok nem leterne -- hanem az, hogy mindegyik mas formatumban, mas koordináta-rendszerben, mas idofelbontással és mas minőségi szinttel érkezik. Az adategyesítés (data fusion) és a minőség-ellenőrzés (quality control) a hidrológus munkaidejanak jelentos reszet emészti fel.

### 18.2.2 Pipeline-ok a vízügyi adatgyűjtéshez

A 7. fejezetben megtanultad, hogyan epithetod fel az adat-pipeline-ok ot szakaszat: bevitel, tisztitas, transzformacio, elemzés, kimenet. A vízügyi kontextusban ez igy nez ki:

```
┌──────────────────┐    ┌────────────────┐    ┌──────────────────┐    ┌───────────────┐    ┌──────────────────┐
│  1. BEVITEL      │───>│  2. TISZTITAS  │───>│ 3. TRANSZFORMACIO│───>│  4. ELEMZES   │───>│  5. KIMENET      │
│ OVF API          │    │ Hibas ertekek  │    │ EOV -> WGS84     │    │ Statisztika   │    │ Dashboard        │
│ OMSZ FTP         │    │ Adathianyok    │    │ Idozóna-korr.    │    │ Trendek       │    │ Modell-bemenet   │
│ Copernicus CDS   │    │ Szenzorhiba    │    │ Ujramintavetelezes│   │ Anomaliak     │    │ Riasztas         │
│ ERA5 API         │    │ Dublikaciok    │    │ Terbeli aggreg.  │    │               │    │                  │
└──────────────────┘    └────────────────┘    └──────────────────┘    └───────────────┘    └──────────────────┘
```

Az AI segitsege mar a pipeline-tervezesnel megmutatkozik. Nezzuk, hogyan kerheted meg a Claude-ot vagy a ChatGPT-t, hogy segitsen az OVF vízszint-adatok automatikus letöltéseben:

---

**Te:**

> Irj egy Python scriptet, amely naponta reggel 6-kor automatikusan letolti az elmult 24 ora vízszintadatait a hydroinfo.hu API-jarol a Tisza folyo következő allomasaira: Tokaj, Tiszafured, Kiskor, Szolnok, Csongrad, Szeged. Az adatokat mentes el egy SQLite adatbázisba idősorformaban, és ha bármely allomasnál a vízszint meghaladja az I. fokú keszultsegi szintet, küldjon e-mail riasztast.

---

**AI valasz (roviditvee):**

```python
import requests
import sqlite3
import smtplib
from datetime import datetime, timedelta
from email.mime.text import MIMEText

# Allomások es keszultsegi szintek (cm)
STATIONS = {
    "Tokaj":      {"id": "2-0001", "alert_1": 650},
    "Tiszafured": {"id": "2-0005", "alert_1": 700},
    "Kiskor":     {"id": "2-0008", "alert_1": 750},
    "Szolnok":    {"id": "2-0012", "alert_1": 800},
    "Csongrad":   {"id": "2-0015", "alert_1": 750},
    "Szeged":     {"id": "2-0018", "alert_1": 800},
}

def fetch_water_levels(station_id, hours=24):
    """Az OVF API-ból letolti a vizszintadatokat."""
    end = datetime.utcnow()
    start = end - timedelta(hours=hours)
    url = f"https://hydroinfo.hu/api/v1/stations/{station_id}/measurements"
    params = {
        "start": start.isoformat(),
        "end": end.isoformat(),
        "parameter": "water_level"
    }
    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()
    return response.json()["data"]

def store_in_db(db_path, station_name, records):
    """SQLite adatbazisba menti az adatokat."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS water_levels (
            station TEXT,
            timestamp TEXT,
            level_cm REAL,
            PRIMARY KEY (station, timestamp)
        )
    """)
    for record in records:
        cursor.execute(
            "INSERT OR REPLACE INTO water_levels VALUES (?, ?, ?)",
            (station_name, record["time"], record["value"])
        )
    conn.commit()
    conn.close()

def check_alerts(db_path):
    """Ellenorzi, hogy valamelyik allomason I. foku keszultseg van-e."""
    alerts = []
    conn = sqlite3.connect(db_path)
    for name, info in STATIONS.items():
        cursor = conn.execute(
            "SELECT MAX(level_cm) FROM water_levels WHERE station = ? "
            "AND timestamp > datetime('now', '-24 hours')",
            (name,)
        )
        max_level = cursor.fetchone()[0]
        if max_level and max_level > info["alert_1"]:
            alerts.append(f"{name}: {max_level:.0f} cm (I. fok: {info['alert_1']} cm)")
    conn.close()
    return alerts
```

Ez a peldakod természetesen egyszerűsitett -- az eles rendszerben kezelni kell a halozati hibakat, az API rate limit-et, a hianyzo adatokat és a naplozast. A lenyeg az, hogy az AI képes percek alatt letrehozni egy mukodo pipeline-vazat, amelyet aztán te tesztelsz és finomitasz.

### 18.2.3 Minoseg-ellenorzes AI-val

A vízügyi mérések minőség-ellenőrzése (quality control, QC) kritikus fontossagu. Egy hibas szenzor, amely 999 cm-es vízszintet jelent, vagy egy lefagyott csapadekmerő, amely hetekig nullat küld, hamis riasztast valthat ki vagy -- ami rosszabb -- elmarado riasztast. A hagyományos QC szabalyalapu: ha az érték egy eloirt tartományba esik és az elterese az elozo merestol nem haladja meg a kuszoberteket, elfogadjuk.

Az AI ket szintén segithet:

1. **Anomalia-detektalas gepitanulassal.** Egy isolation forest vagy autoencoder-alapu modell a normalis szenzorviselkedest tanulja meg az elozmeny-adatokbol, és kijeloli azokat az értékeket, amelyek nem illeszkednek a mintazatba -- meg akkor is, ha azok formal szintén "szabalyosak". Peldaul egy vízszint, ami lassan, monoton no, mikozben a kornyezo allomasokon mar apadast mertek, statisztikailag anomalia.

2. **LLM-alapu minoseg-jelentes.** Az AI osszefoglalhatja az adatminosegi helyzetet természetes nyelven: "Az elmult heten a szolnoki allomas ket 15 perces adathianyt mutat marcius 12-en delutan. A kiskorei allomas csapadekmeroje marcius 14. ota nullat jelent, mikozben a szomszedos allomások 8-12 mm-t regisztraltak -- valoszinu szenzor-meghibasodas." Ez a fajta diagnosztikus összefoglaló pontosan az, amire a vízügyi ugyelet szüksegel -- és amire az LLM-ek kiválóan alkalmasak.

A 7. fejezet pipeline-architektúrájat alkalmazva a QC lépést a tisztitasi szakaszba (2. szakasz) epitjuk be, az anomalia-modellt pedig az elemzési szakaszba (4. szakasz).

---

## 18.3 AI-támogatott terepanalízis

### 18.3.1 A vízgyűjtő-lehatárolás mint kódgenerálási feladat

A 5. fejezetben megtanultad, hogyan használhatod az AI-t kódolási asszisztenskent. A víztudományban az egyik leggyakoribb feldolgozási lanc a vízgyűjtő-lehatárolás DEM-bol:

1. Melyedesek kitoltese (Fill)
2. Folyasirany szamitas (FlowDirection)
3. Folyasakkumulacio (FlowAccumulation)
4. Vizfolyashálózat meghatározása (kuszobertek-alapu)
5. Kiontesi pont kijelelese (SnapPourPoint)
6. Vizgyujto lehatárolás (Watershed)

Ez a hat lépés manualis GIS-ben 20-30 percet vesz igénybe egyetlen vízgyűjtőre. Ezer vízgyűjtőre? A 12. fejezet (munkafolyamat-automatizalas) megmutatta, hogyan irunk erre Python-szkriptet. De mi van, ha nem akarsz szkriptet irni -- hanem az AI-val iratsz egyet?

---

**Te:**

> WhiteboxTools-t hasznalva irj egy Python szkriptet, amely (1) beolvas egy GeoTIFF DEM-et, (2) kitolti a melyedeseket, (3) D8 folyasiranyt szamol, (4) folyasakkumulaciot szamol, (5) egy megadott koordináta-pont korul lehataroja a vízgyűjtőt, és (6) exportalja a vízgyűjtő-hatart shapefile-kent. Az input DEM felbontása 10 meter, EOV koordináta-rendszerben van (EPSG:23700).

---

Az AI nehany masodperc alatt generálja a teljes szkriptet, beleertve az importokat, a fajlkezelest, a hibakezelest és a koordináta-transzformaciot. A különbség a hagyományos megközelítéstol:

| Hagyomanyos | AI-támogatott |
|-------------|---------------|
| Megtanulod a WhiteboxTools dokumentációt | Leírod, mit akarsz |
| Probalkozol a paraméterezéssel | Az AI ajánl paramétereket |
| Debuggolsz orakig | Az AI javitja a hibakat |
| Egyetlen vízgyűjtőre | Az AI ciklussa terjeszti ki |

### 18.3.2 LLM-ek a DEM-feldolgozás hibainak diagnosztizalasahoz

A terepfeldolgozás gyakori problémaja, hogy a vízgyűjtő-lehatárolás nem felel meg a varakozasoknak: tul kicsi, tul nagy, vagy "furcsaan" nez ki a terepen. Az LLM-ek kivaloan alkalmasak a hiba diagnosztizalasara:

---

**Te:**

> A vízgyűjtő-lehatárolás a Zala felso szakaszara egy 930 km2 helyett csak 47 km2-es terület adott. A DEM 10 m-es felbontású, az Copernicus GLO-30-bol szarmazik. Mi lehet a probléma?

---

**AI:**

> Négy valoszinu ok letezik, valoszinusegi sorrendben:
>
> 1. **A kiontesi pont koordinátaja pontatlan.** Ha a pont nem pontosan a medervonalra esik, a FlowAccumulation-raszteren kis akkumulacios érték tartozik hozza, és a lehatárolás csak a lokalis minimedencet ragadja meg. **Megoldas:** Hasznalj SnapPourPoint-ot 500 m-es illesztesi tavolsaggal.
>
> 2. **A DEM melyedesei nincsenek kitoltve.** A GLO-30 nyers DEM-ben hidak, épületek és mas mutargyak hamis melyedeseket hozhatnak letre, amelyek megszakitjak a folyasiranyokat. **Megoldas:** Ellenorizd, hogy a Fill lépés tenyleg lefutott-e, és noveld a z-limit erteket.
>
> 3. **Koordinata-rendszer hibas.** Ha a DEM WGS84-ben van, de a kiontesi pont EOV-ben (EPSG:23700), a koordináta-parok nem felelnek meg egymasnak. **Megoldas:** Ellenorizd, hogy mindket reteg azonos CRS-ben van-e.
>
> 4. **A DEM felbontása nem elegendő.** A 30 m-es GLO-30 a Zala szuk volgyeiben nem mindig ragadja meg a mederstrukurat. **Megoldas:** Provalj 10 m-es EU-DEM-et vagy LiDAR-alapu DEM-et.

Ez a fajta diagnosztikus gondolkodas -- amit a 24. fejezetben a HydroGIS konyv ágens AI-janal lattunk -- pontosan az, amire a tudos szükségel: nem újabb kodsort, hanem **megertesi tamogatast**.

### 18.3.3 Vizhalozat-kinyeres és jellemzes

A vízgyűjtő-lehatárolás után a vizhalozat kinyerese kovetkezik. Az AI itt is segit: generálhat szkriptet, amely TauDEM-mel vagy WhiteboxTools-szal:

- Kinyeri a vizhalozatot (StreamToFeature)
- Kiszamolja a Strahler-rendet
- Megmeeri a szakaszhosszakat és eseeseket
- Osszekapcsolja a vizhalozatot az OVF vízmérceallomásokkal
- Generalja a RAPID hullámtranszformációhoz szükséges kapcsolodasi tablakat

A lenyeg nem az, hogy az AI jobb programozó, mint te -- hanem az, hogy a feladat, amelyre eddig egy GIS-szakembernek harom napra volt szüksége, most egy delutan alatt elvegezeheto, a kutato természetes nyelvű utasitasaival.

---

## 18.4 Gepi tanulas a vízszint-előrejelzésben

### 18.4.1 Miért alkalmas az LSTM az arvizelőrejelzésre?

Az arvizelőrejelzés lenyegeben idősor-probléma: a mult csapadek- és vízszint-adataiból kell elojejelezni a jovobelieket. A 6. fejezetben általánosan targyaltuk az AI-támogatott modellezést; itt a hidrologiai alkalmazást vesszuk részletesen.

A Long Short-Term Memory (LSTM) halozat különösen alkalmas erre a feladatra, mert:

1. **Hosszu tavu fuggesegeket tanul meg.** A Tisza archullamja Rahotol Szolnokig 3-5 napig tart -- az LSTM cellaállapota kepegges ilyen időbeli kapcsolatokat megragadni.
2. **Tobbresu bemenetet kezel.** Csapadek, homerseklet, felso szakaszi vizallás, talajnedvesseg, hovas -- mind parhuzamosan epithetok a modellbe.
3. **Nem linearis osszefuggeset tanul.** A vízgyűjtő valasza a csapadekra nem linearis: szaraz talajon 10 mm eso alig okoz lefolyast, telitett talajon ugyanennyi arhullámot indithat.

### 18.4.2 Szamitasi példa: vízszint-előrejelzés a Tiszan

Vegyunk egy konkrét feladatot: napi vízszint-elojelezés a Tisza szolnoki szelvenyben, 1-3 napos eloretekentéssel.

**Bemeneti adatok:**
- Napi csapadek 10 meteorológiai allomasrol a felso vízgyűjtőrol (ERA5 reanalízis)
- Napi átlaghomerseklet (hoolvadas szamítasahoz)
- Vizszint-elozmeny Tokaj, Tiszafured, Kiskor allomasokon (kesleltetett bemenetek)
- Talajnedvessegi index (Copernicus Soil Moisture)
- Evszakon belüli nap (sin/cos kódolással)

**Architektura:**

| Parameter | Ertek |
|-----------|-------|
| Bemeneti jellemzők | 18 |
| Visszatekentesi ablak | 45 nap |
| LSTM-retegek | 2 |
| Rejtett egysegek rejtett | 128 |
| Dropout arany | 0,2 |
| Kimenet | 1--3 nap elore |
| Veszteségfuggveny | NSE-alapu |
| Tanitas | Adam, lr=0,001, korai leallas |

**Felkeszites promptja (a 6. fejezet stilusaban):**

---

**Te:**

> Epitts egy LSTM modellt PyTorch-ban, amely a Tisza szolnoki vízszintjet jelzi elore 1-3 napra. A bemeneti CSV tartalmaz 18 jellemzőt és 20 ev napi adatot (2003-2022). Osszd fel a datasort: 2003-2016 tanitas, 2017-2019 validalas, 2020-2022 teszt. Hasznalj 45 napos visszatekentesi ablakot, 2 LSTM-reteget 128 rejtett egyseggel, dropout=0,2, és NSE-alapu veszteségfuggvenyt. Abrazold a tesztev vízszint-elorejelezes és a megfigyelt értékek osszeveteset.

---

A 23. fejezet (HydroGIS) részletesen bemutatja, hogy egy ilyen LSTM-modell 0,87-os NSE-t erhet el a teszthalmazon -- jol megragadja az árvizi csúcsok idoziteset, bar szisztematikusan alulbecsuli a legnagyobb esemenyeket. Ez a korlat nem kizarolag az adatvezérelt megközelítésekre jellemző -- a fizikai alapu modellek is küszködnek a szélsőségekkel --, de az ML-modelleknkel különösen fontos felismerni, mert nincs fizikai korlat, amely megakadalyozna a valoszinütlen eredmenyeket.

### 18.4.3 Talalajvízszint-elojelezés

A talajvízszint-előrejelzés mas jellegú probléma. A felszin alatti vízszint változásai lassabbak (hetek-honapok), a bemeneti adatok ritkabbak (heti-havi meresek), és a fizikai osszefuggesek bonyolultabbak (a Darcy-torveny háromdimenziós heterogen kozegben ervenyes). Megis, a gepi tanulas itt is eredmenyes:

**Random forest/gradient boosting modell a talajvízszintre:**
- Bemenetek: csapadek, evapotranszspiracio, Duna/Tisza vízszint, elozmenybeli talajvízszint, felszinhaszalat, talajfizikai parameteerek
- Kimenet: talajvízszint-változás a következő honapra
- Alkalmazas: az Alfold 2000+ monitoring kutja

A 6. fejezet modellezési keretrendszeret koveteve:

1. **Adatelokeszites:** pipeline (7. fejezet) az OVF talajvíz-adatbázisbol
2. **Feature engineering:** az AI javasol új jellemzőket (pl. 30/60/90 napos kummulatív csapadek, talajvízszint trendkomponens)
3. **Modelltanitas:** scikit-learn gradient boosting vagy XGBoost
4. **Kiertekeles:** R2, RMSE, és -- ami különösen fontos -- a szaraz nyari kisviz-időszakok helyes elojelzesee

### 18.4.4 Fizika-informalt gepi tanulas (PIML)

A legigéeretesebb fejlemeny a fizika-informalt gepi tanulas (Physics-Informed Machine Learning, PIML), amely a fizikai egyenleteket a neuralis halozat veszteségfuggvenyebe epiti be. Ahelyett, hogy az LSTM szabadon tanulna tetszoleges osszefuggeseket, a veszeségfuggvenyben butetjuk azokat a megoldásokat, amelyek fizikailag lehetetlenek:

$$\mathcal{L} = \mathcal{L}_{\text{adat}} + \lambda \cdot \mathcal{L}_{\text{fizika}}$$

ahol:
- $\mathcal{L}_{\text{adat}}$ a megfigyelt és szimulalt értékek közötti elteres (pl. MSE)
- $\mathcal{L}_{\text{fizika}}$ a fizikai torveny serteseenek merteke (pl. a vízmérleg-megmaradas hianya)
- $\lambda$ a ket tag kozötti sulyozas

Peldaul a vízgyűjtő vízmérlegere:

$$P - ET - Q - \Delta S = 0$$

ahol $P$ a csapadek, $ET$ az evapotranszspiracio, $Q$ a lefolyas, $\Delta S$ a tarolasváltozás. Ha az LSTM olyan vízszint-elojelzest produkalna, amely a vízmérleg-egyenlettel inkonzisztens, a veszteségfuggveny bunteti.

Ez a megközelítés ot az 5. fejezet (AI-támogatott kódgenerálás) és a 6. fejezet (matematikai modellezés) metszeteben all: az AI segít megirni a fizika-informalt veszteségfuggvenyt, az LLM diagnosztizalja, hogy miért nem konvergal a tanitas, és az ágens autonóman hangolja a $\lambda$ hiperparamétert.

---

## 18.5 Matematikai modellezés AI-val: egyenletektol a kodig

> **🖼️ Ábra: A Tisza digitális ikre — valós idejű árhullám-szimuláció**
> *3D visualization of the Tisza river basin digital twin, showing flood wave propagation with color-coded water levels, holographic style on dark background*

### 18.5.1 A víztudomány alapegyenletei

A hidrologianak harom alapveto parciális differencialegyenlete van, amelyekkel a kutato rendszeresen talalkozik:

**1. Saint-Venant-egyenletek** (felszini aramlás nyilt mederben):

Kontinuitasi egyenlet:
$$\frac{\partial A}{\partial t} + \frac{\partial Q}{\partial x} = q_L$$

Impulzusegyenlet:
$$\frac{\partial Q}{\partial t} + \frac{\partial}{\partial x}\left(\frac{Q^2}{A}\right) + gA\frac{\partial h}{\partial x} = gA(S_0 - S_f)$$

ahol $A$ a mederkeresztmetszet, $Q$ a vizhozam, $q_L$ az oldaliranyú betaplálás, $g$ a gravitacios gyorsulas, $h$ a vízszint, $S_0$ a medereseés és $S_f$ a surlodasi esesés.

**2. Richards-egyenlet** (telitetlen zona vízmozgas):

$$\frac{\partial \theta}{\partial t} = \frac{\partial}{\partial z}\left[K(\theta)\left(\frac{\partial h}{\partial z} + 1\right)\right]$$

ahol $\theta$ a terfogoatos viztatralom, $K(\theta)$ a telitettsegtol fuggo szivargasi tenyezo, $h$ a szivasi nyomasmagassag.

**3. Boussinesq-egyenlet** (felszín alatti vizaramlas):

$$S_y \frac{\partial h}{\partial t} = \frac{\partial}{\partial x}\left(K h \frac{\partial h}{\partial x}\right) + \frac{\partial}{\partial y}\left(K h \frac{\partial h}{\partial y}\right) + W$$

ahol $S_y$ a fajlagos hozam, $h$ a vízszint, $K$ a szivargasi tenyezo, $W$ a forras/nyelo tagok (utanpotlas, szivattyas).

### 18.5.2 AI mint matematikai fordító

A 6. fejezet bemutatta, hogyan hasznalhato az AI arra, hogy kutatasi kerdest matematikai formaba, majd kodra fordítson. A víztudományban ez igy nez ki a gyakorlatban:

---

**Te:**

> A Hortobagy területen szeretnem modellezni, hogyan valtozik a talajvízszint, ha a nyari csapadek 20%-kal csokken. A terüulet 50 km x 50 km, a vizado homokos, a szivargasi tenyezo K = 5 m/nap, a fajlagos hozam Sy = 0,15. A peremfeltetelek: nyugaton a Tisza allandonizszintje 82 m, keleten nulla-flux hatar. Az utanpotlas az eves csapadek 15%-a. Irj egy Python szimulációt veges differenciaval, 500 m-es racssal, és abrazold a talajvízszint-változást 10 ev mulva.

---

Az AI a Boussinesq-egyenlet 2D veges differencia diszkretizaciojat generálja, a megadott paramétererekkel, és Matplotlib abrakat keszit. A 6. fejezet útmutatasa szerint:

1. **Ne fogadd el vakon a kodot.** Ellenorizd az egyenlet-diszkretizaciot, a peremfelteeteleket és a numerikus stabilitas.
2. **Kerd meg az AI-t, magyarazza el a lepeseket.** "Miért eztet az idolepest valasztottad? Mi tortenik, ha a szivargasi tenyezo terben valtozik?"
3. **Validald egyszerű esettel.** Kerd meg az AI-t, hogy futtasson egy egydimenziós analitikus megoldással osszevetheto tesztesetet.

### 18.5.3 A Saint-Venant-egyenletek numerikus implementacioja

A Saint-Venant-egyenletek numerikus megoldásanak generálasa az egyik legösszetettebb feladat, amelyet LLM-től kerhetsz. A teljes egyenletrendszer (dinamikus hullam) numerikusan instabil lehet, ezert a vízügyben gyakran egyszerűsitett valtozatokat használnak:

| Kozelites | Elhanyagolt tagok | Alkalmazas |
|-----------|-------------------|------------|
| Kinematikus hullam | Lokalis és advektiv gyorsulas, nyomasgradiens | Meredek leftu patakok |
| Diffuz hullam | Lokalis és advektiv gyorsulas | Lapos artéri áramlas |
| Dinamikus hullam | Semmi (teljes egyenlet) | Vizlepcsok, arapaly |

Az AI segithet abban, hogy eldöntsd, melyik kozelites alkalmas a te feladatodra. Peldaul:

---

**Te:**

> A Tisza Szolnok alatti szakaszaran (nagyon lapos, 0,00005 m/m esés) modellezni akarom egy árhullám terjedeset. Melyik Saint-Venant kozeliteset hasznaljam?

---

**AI:**

> Ilyen lapos esesneel a kinematikus hullam **nem** alkalmas, mert elhanyagolja a nyomasgradienst, amely az alacsony esésú medrekneel a meghaterozo erohatás. A **diffuz hullam** kozelites javasolt: figyelembe veszi a nyomasgradienst, de elhanyagolja a teheetlensegi tagokat, amelyek csak hirtelen változásoknal (gatzakadas, zsilipnyitas) lenyegesek. Ha gatzakadas-szcennariora is szükseg van, a **teljes dinamikus hullam** kell.

Ez a fajta fizikai konzultació -- amit a 23. fejezet (HydroGIS) "MI mint a hidrológus asszisztense" cimu fejezetben részletesen targyalunk -- az AI egyik legertekesebb alkalmazása a víztudományban.

---

## 18.6 Adat-pipeline-ok a hidrologiai monitoringhoz

### 18.6.1 Az operativ monitoring kihívásai

Egy operativ vízügyi monitoring-rendszer nem egyszeri elemzés -- folyamatosan, automatikusan, megbizhataon kell mukodnie. A 7. fejezet pipeline-koncepcioját a vízügyi kontextusra alkalmazva az operativ pipeline-nak a következő kovetelményeknek kell megfelelnie:

| Kovetelmeny | Megvalostias |
|-------------|--------------|
| **Folyamatos bemenet** | Szenzor-adatok 15 percenkent, műholdas adatok napi frissitessel |
| **Minoseg-ellenorzes** | Automatikus anomalia-detektalas + emberi jovahagy vahagy |
| **Latesedelmentseg** | Ertesites < 5 perc a szenzor-leolvasas után |
| **Megbizhatsag** | 99,9% uptime, automatikus ujraindulas hiba eseten |
| **Skálazhatosag** | 100+ allomas, 10+ paraméter, eseemennyalapú felskalazas |

### 18.6.2 A vízügyi monitoring pipeline felépítese

Egy teljes vízügyi monitoring pipeline a 7. fejezet architektúrájat követi, de domain-specifikus elemekkel:

```python
# Pelda: vizugyi monitoring pipeline vazlata (pseudokod)

class HydroMonitoringPipeline:
    """
    Teljes vizugyi monitoring pipeline,
    amely a 7. fejezet elveit alkalmazza.
    """

    def ingest(self):
        """1. szakasz: adatbevitel"""
        self.water_levels = fetch_ovf_api(stations=TISZA_STATIONS)
        self.precipitation = fetch_omsz_api(stations=PRECIP_STATIONS)
        self.satellite_precip = fetch_era5(bbox=TISZA_BASIN, hours=24)
        self.groundwater = fetch_groundwater_db(wells=ALFOLD_WELLS)

    def clean(self):
        """2. szakasz: tisztitas"""
        self.water_levels = remove_duplicates(self.water_levels)
        self.water_levels = detect_anomalies(self.water_levels,
                                              method="isolation_forest")
        self.precipitation = fill_gaps(self.precipitation,
                                        method="idw_neighbors")

    def transform(self):
        """3. szakasz: transzformacio"""
        self.all_data = merge_timeseries(
            self.water_levels,
            self.precipitation,
            self.satellite_precip,
            self.groundwater,
            target_crs="EPSG:23700",  # EOV
            target_freq="1H"           # orankenent
        )

    def analyze(self):
        """4. szakasz: elemzes"""
        self.flood_forecast = run_lstm_forecast(
            self.all_data, model_path="models/tisza_lstm_v3.pt")
        self.gw_forecast = run_gw_model(
            self.all_data, model_path="models/alfold_xgboost_v2.pkl")
        self.alerts = check_thresholds(self.flood_forecast, ALERT_LEVELS)

    def output(self):
        """5. szakasz: kimenet"""
        update_dashboard(self.flood_forecast, self.gw_forecast)
        if self.alerts:
            send_alerts(self.alerts, recipients=DUTY_OFFICERS)
        archive_to_database(self.all_data, db="hydro_archive.db")
```

A pipeline-t a 7. fejezet segedprogramjaival (cron job, Airflow, Prefect) utemezed -- például órákeneti futatassal, külön napi batch-futatassal a műholdas adatokhoz.

### 18.6.3 AI a pipeline-generálsaban

Az igazi attores az, amikor nem te irod a pipeline-t, hanem az AI-val iratod:

---

**Te:**

> Epits egy Prefect-alapu pipeline-t, amely órákennt letolti a Tisza ot fó allomasanak vízszintadatait az OVF API-jarol, futtat egy elotre betanitott LSTM modellt 24 oras előrejelzésre, és ha barmely allomasnál az elorejelzett vízszint meghaladja az I. fokú keszultsegi szintet, Slack-üzenetet kuld a "flood-alerts" csatornara. A pipeline log-oljon minden lepest, és ha az API nem valaszol 30 masodpercen belül, hasznaljon cache-elt adatot.

---

Az AI generálja a teljes Prefect-flow-t, a dekoratorokkal, a hibakezeléssel és a Slack-integrációval. Te az eredményt teszteled, validálod és eles koraárnyezealbe viszed.

---

## 18.7 RAG a vízügyi szabalyozashoz

### 18.7.1 A vízügyi jogi környezes bonyolultsaga

A vízügyi munka nem csak fizika és modellezés -- a szabályozási koernyezt is ismerni kell. Magyarországon és az EU-ban a vízügyi jogszabalyok tobb retegu rendszert alkotnak:

| Szint | Jogszabaly | Terjedelem |
|-------|-----------|------------|
| **EU** | Viz Keretiranyelv (2000/60/EK) | ~100 oldal + mellekletek |
| **EU** | Arvizi Iranyelv (2007/60/EK) | ~30 oldal |
| **EU** | Talajviz Iranyelv (2006/118/EK) | ~25 oldal |
| **Magyar** | 1995. evi LVII. torveny a vizgazdálkodásrol | ~80 oldal |
| **Magyar** | 232/1996. (XII. 26.) Korm. rendelet (vízügyi hat. eljaras) | ~40 oldal |
| **Magyar** | Vizgyujto-gazdálkodási Tervek (VGT2, VGT3) | 1000+ oldal |
| **Magyar** | Kornyezeti hatasvalgazalasi dokumentumok | Projekt-specifikus |

Egy kutato, aki vízgyűjtő-gazdálkodási tervet keszit, vagy környezeti hatastanulmanyt ir, rendszeresen kell hivatkoznia ezekre a dokumentumokra. A hagyományos megközelítés: PDF-eket bongeszni, Ctrl+F-fel keresni. Ez lassúu és hibara hajlamos.

### 18.7.2 RAG-rendszer vízügyi dokumentumokra

A 9. fejezetben megtanultad, hogyan epithetoz RAG (Retrieval-Augmented Generation) rendszert. A vízügyi alkalmazás pontosan követi az ott leirt architektuarat:

**1. Dokumentumok begyüjtése:**
- EU Viz Keretiranyelv (magyar forditas)
- Arvizi Iranyelv
- Magyar vizgazdálkodási torveny
- VGT3 (Vizgyujto-gazdálkodási Terv)
- OVF szakmai utmutatok
- Vonatkozo EIA (környezeti hatasvalgazalaási) dokumentumok

**2. Chunk-olas és embedding:**
- A dokumentumokat 500-1000 tokenes darabokra bontjuk
- Embedding-vektorokat szamitatunk (pl. OpenAI text-embedding-3-large vagy Cohere multilingual)
- A vektorokat ChromaDB vagy Qdrant adatbázisba taroljuk

**3. Kerdezes:**

---

**Te (a RAG chatbotnak):**

> A Tisza vízgyűjtőjen tervezett egy új termelokkut-telep engedelyezteesi eljaarasahoz milyen feltételeknek kell megfelelni a Viz Keretiranyelv 4. cikkelye szerint?

---

**RAG chatbot:**

> A Viz Keretiranyelv 4. cikkely (7) bekezdes szerint új tevekeenysegek engedelyezesekor biztositani kell, hogy az nem okozza a viztest allapotanak romlasaat ("no deterioration" elv). Konkretant:
>
> 1. Az új kitermel nem okozhatja a talajvíztest mennyisegi állapotanak romlasát [VKI 4. cikk (1)(b)(i)]
> 2. Nem veszelyeztetheti a kapcsolodo felszini vizek okologiai allapotat [VKI 4. cikk (1)(a)(i)]
> 3. A magyar vizgazdálkodási torveny (1995:LVII. tv.) 15. § szerint vizjogi engedelyt kell kerni...
>
> **Forrasok:** VKI_4_cikkely.pdf (chunk 23), Vizgazd_tv_15.pdf (chunk 7), VGT3_Tisza_II_4.pdf (chunk 145)

A RAG-rendszer erteke nem az, hogy tokeletes jogi tanacsot ad -- hanem az, hogy masodpercek alatt megtalálja a releváns jogszabaly-helyet, és a kutato ellenorizheti a hivatkozott forrast. A 9. fejezet osszes figyelmeztetese itt is ervenyes: a RAG-rendszer hallucinalgat, és jogi kerdesekben soha nem szabad vakon elfogadni az AI valaszat.

---

## 18.8 Hidrologiai digitális ikrek

### 18.8.1 Mi a digitális iker a víztudományban?

A 10. fejezet bevezette a digitalis iker (digital twin) fogalmat: egy fizikai rendszer virtualis masata, amely valos ideju szenzor-adatokkal szinkronban fut. A víztudományban a digitalis iker egy vízgyűjtő-szintű szimuláció, amely:

1. **Tukrozi** a valos rendszert: a terep, a vizhalozat, a vizadok, az időjárás
2. **Szinkronban van** a valos szenzorokkal: vízmérceek, csadekmerok, talajvíz-monitoring kutak
3. **Elorejeelez:** "mi tortenik, ha...?" kerdesekre valaszol
4. **Tanul:** minden új mérés javitja a modell pontossagat

### 18.8.2 Egy vízgyűjtő-szintű digitalis iker felépítése

Peldakent vegyuk a **Zala vízgyűjtő** -- a Balaton legnagyobb mellekfollyjaat --, amelyet a HydroGIS koonyv 24. fejezete is példaként hasznalt az agens-alapú kalibrálashoz.

A digitális iker komponensei (a 10. fejezet architektúrája szerint):

```
┌─────────────────────────────────────────────────────────────────┐
│                    DIGITALIS IKER: ZALA VIZGYUJTO               │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────┐    ┌──────────────┐    ┌────────────────────┐ │
│  │  FIZIKAI    │    │   MODELLEK   │    │    SZENZOR-RETEG   │ │
│  │  RETEG      │───>│              │<───│                    │ │
│  │             │    │ Csapadék-    │    │ 5 vizmerceallomás  │ │
│  │ DEM 10m     │    │ lefolyas     │    │ 12 csapadékmero    │ │
│  │ Talaj       │    │ (GR4J)       │    │ 8 talajvíz-kút     │ │
│  │ Felszínbor. │    │              │    │ Sentinel-2 (5 nap) │ │
│  │ Vízhálózat  │    │ Talajvíz     │    │ ERA5 (óránként)    │ │
│  │             │    │ (Boussinesq) │    │                    │ │
│  └─────────────┘    │              │    └────────────────────┘ │
│                     │ Hullámtransz.│                           │
│                     │ (Muskingum)  │                           │
│                     └──────────────┘                           │
│                            │                                   │
│                     ┌──────────────┐                           │
│                     │  AI-RETEG    │                           │
│                     │              │                           │
│                     │ LSTM elore-  │                           │
│                     │ jelzes       │                           │
│                     │ Anomália-    │                           │
│                     │ detektalas   │                           │
│                     │ Automat.     │                           │
│                     │ kalibracio   │                           │
│                     └──────────────┘                           │
│                            │                                   │
│                     ┌──────────────┐                           │
│                     │  DASHBOARD   │                           │
│                     │ Valos ideju  │                           │
│                     │ terkep+grafik│                           │
│                     └──────────────┘                           │
└─────────────────────────────────────────────────────────────────┘
```

A digitalis iker erteke a "mi tortenik, ha?" kerdesek megválaszolasaaban rejlik:

- **Mi tortenik, ha a Zala felso szakaszan 80 mm eso esik 24 ora alatt?** A modell futtatja a csapadek-lefolyas modult, a hullámtranszformaciott, és elojelzi a vízszintet minden szelvenyben.
- **Mi tortenik, ha a Balaton szintje 20 cm-rel emelkedik?** A modell a megvaltozott peremfeltetelbol szamolja a hatteráramlást a Zala alluvilialis vizadojaaban.
- **Mi tortenik, ha új termelokutat telepitenek Zalaegerszeg mellé?** A talajvíz-modul szamolja a leszivast és annak hatasát a Zala alaphozamara.

### 18.8.3 Az AI szerepe a digitalis ikerben

A 10. fejezetben targyalt digitalis iker elveket a vízgyűjtőra alkalmazva az AI harom szintén mukodik:

1. **Adataszimilacio:** Az LSTM-modell a valós ideju szenzor-adatokat használja az elorejelezsesi allapot frissítesere (a Kalman-szuro analogiaja, de neurális halozattal).

2. **Automatikus kalibráció:** Ha az elojelzett és a megfigyelt vízszint elterese noovekszik, az ágens AI (lased 18.9. szakasz) automatikusan ujrakalibralja a modellt.

3. **Természetes nyelvu lekerdeezes:** A vízügyi ugyelet természetes nyelven kerdezhet a digitalis ikertol: "Mi az erojelzett vízszint Szolnoknal holnaputan?" -- és az LLM a modell eredmenyebol generálja a választ.

---

## 18.9 AI ágensek az autonóm hidrologiai modellezésben

### 18.9.1 A kalibrációs probléma mint agens-feladat

A HydroGIS konyv 24. fejezete részletesen bemutatja, hogyan alkalmazható az ágens AI a hidrologiai modellek autonómo modellezésere. A lenyeget a kovetkezőkben foglaljuk ossze, és osszekapcsoljuk az "Agentikus AI Tudosoknak" koonyv 11. és 12. fejezetenek agens-architekturájaval.

A hidrologiai modellek kalibrációja a következő lépésekből áll:

1. Adatok beolvasasa és ellenorzese
2. Kezdeti paraméterek becslese (szaktudas alapján)
3. Modell futtatasa
4. Eredmenyek kiertékelese (NSE, KGE, PBIAS, vizualis ellenorzes)
5. Parameterek módositasa a diagnozis alappjan
6. Ismetles konvergenciaig

Ez pontosan az a **tervezes--vegrehajas--ertekelés--iteráció** ciklus, amelyet a 11. fejezetben az ágens AI alappkent ismertettünk:

| Agens-komponens (11. fejezet) | Hidrologiai megfelelo |
|-------------------------------|------------------------|
| **Cel** | "Kalibrald a GR4J modellt NSE > 0,7-re" |
| **Tervezes** | Parametertertományok meghatarozasa, stratégia valasztas |
| **Eszkozok** | Modellfuttato, adatolvasoo, kiertekelo, vizualizalo |
| **Vegrehajas** | Modell futtatasa adott paraméterkeszlettel |
| **Ertekeles** | NSE, KGE szamitas + vizsgálgorbe diagnosztika |
| **Memoria** | Korabbi paraméterkeszletek és teljesitmenyuk naploja |
| **Iteracio** | Parametermodositas a diagnozis alapján |

### 18.9.2 A HydroGIS 24. fejezet pelda-agense

A HydroGIS konyv 24. fejezete egy teljes peldaval szemlelteti az agens-alapu kalibrációt: a **Zala folyo zalaegerszegi** vízgyűjtőjere alkalmazva a GR4J modellt. A pelda kovetkezményei az AI-ágensek megértése szemontjabol (11--12. fejezet):

**1. lepes: Az ágens beolvassa és megvizsgalja az adatokat.**

Az ágens nem egyszereuen betolti az adatokat -- *megvizsgalja* oket. Kiszamolja a lefolyasi tenyezot (0,23), osszeveti a regiiora jellemző értékekkel, ellenorzi az adathiányokat. Ez a "gondolkodo" (reasoner) szint, amelyet a 11. fejezet a 2. szintén targyalt.

**2. lepes: Az ágens hidrologiai tudast hasznal a kezdeti paramétervalasztashoz.**

Ahelyett, hogy a paraméter-tartomány veletllenszeru pontjaról indulna (mint az SCE-UA optimalizalo), az ágens a vízgyűjtő jellemzői -- agyagos-homokos talaj, 0,23-as lefolyas tenyezo, 930 km2 terület -- alapján becsüli a kezdeti paramétereket. A HydroGIS szerzoi ezt "diagnosztiakus gondolkodasnak" nevezik.

**3. lepes: Futtatás, értékeles, iteráció.**

Az ágens futtatja a modellt, kiszamolja az NSE-t (0,59 az első iterációban), megvizsgálja a vizsgalgorbeet ("a csúcsok tul magasak és túl korán jelentkeznek"), és ennek alapján modositja a paramétereket. 8 iteráció utaán eleri az NSE = 0,74 erteket.

**Az ágens eronye a hagyományos optimalizalassal szemben:**

| Jellemzo | SCE-UA (hagyományos) | Agens AI |
|----------|----------------------|----------|
| Modell-futtatások szama | 5 000--50 000 | 50--200 |
| Diagnosztikus gondolkodás | Nincs | Van (LLM) |
| Fizikai korlaátok | Csak paraméter-hatarok | Gondolkodas + hatarok |
| Dokumentalas | Keresesi naplo | Ervelesi naplo (természetes nyelven) |
| Elfogadhato megoldás eléresi ideje | Orak | Percek |

### 18.9.3 Agens epites a 12. fejezet keretrendszerevel

A 12. fejezetben megtanultad, hogyan epitesz AI ágenseket. A hidrologiai modellezési ágens a következő eszkozkeszlettel mukodik:

```python
# Hidrologiai kalibracios agens eszkozei (sematikus)

tools = [
    Tool(
        name="load_data",
        description="Betolti a vizgyujto csapadek-, PET- es vizszint-adatait",
        function=load_hydrological_data
    ),
    Tool(
        name="run_model",
        description="Futtatja a GR4J modellt adott parameterekkel",
        function=run_gr4j_simulation
    ),
    Tool(
        name="evaluate",
        description="Szamolja az NSE, KGE, PBIAS mutatokat",
        function=calculate_metrics
    ),
    Tool(
        name="plot_hydrograph",
        description="Abrázolja a megfigyelt es szimulalt vizhozamgorbeket",
        function=plot_hydrograph
    ),
    Tool(
        name="diagnose",
        description="A vizsgalgorbe-eltérések fizikai okat azonosítja",
        function=diagnose_hydrograph_errors
    ),
]

# Rendszer-prompt a hidrologiai agensnek
SYSTEM_PROMPT = """
Te egy tapasztalt hidrologus-asszisztens vagy. A feladatod egy
csapadek-lefolyas modell kalibralasa.

Szabalyok:
1. Minden parametervaltoztatas elott indokold a dontesed.
2. Ne probalkozz vakon -- diagnosztizald a hibasmintakat.
3. Ha az NSE 5 iteracion at nem javul, kerdezd meg az embert.
4. Tartsd nyilvan az osszes parameterkeszletet es teljesitmenyet.
5. A vegso eredmenyt osszefoglalo jelentes formajaban add ki.
"""
```

A 12. fejezet lepesei szerint: (1) definiald az eszközöket, (2) ird meg a rendszer-promptot, (3) allitsd be a memoria-kezelest, (4) futtasd az agens-hurkot, (5) ellenorizd az eredményt.

### 18.9.4 Multi-ágens rendszerek a vízgyűjtő-modellezésben

A 11. fejezet targyalta a multi-ágens rendszereket, ahol tobb ágens dolgozik egyutt. A vizgyujtö-modellezésben ez igy nez ki:

- **Adat-agens:** letolti és elokesziti a bemeneti adatokat
- **Kalibracios agens:** kalibralja a modellt
- **Validaciaos agens:** fuggetlenul ellenorzi az eredményt a validációs időszakon
- **Jelentes-agens:** osszefooglalo dokuumentumot ir az eredmenyekrol

A négy ágens parhuzamosan és szekvencialisan dolgozik (az adat-ágens kesziti elo a bemeneteket, a kalibrációs ágens dolgozik rajta, a validációs ágens ellenorzi, a jelentes-ágens dokumentaalja). Ez a munkamegosztas tukrozi a 11. fejezetben targyalt "speciaalizalt ágensek csapata" architektuurat.

---

## 18.10 Magyar vizttudomanyi kontextus

### 18.10.1 Magyarország egyedi hidrologiai helyzete

Magyarország vízügyi szemponttbol kulönleges helyzettben van:

- **Alvizi fekvés:** A felszini vizek 95%-a a hatarokon tulrol érkezik. A Duna vízgyűjtője 19 országra terjed ki, a Tiszáé 5-re.
- **Lapos terepp:** Az Alfold a Karpat-medence legalacsonyabb pontjaan fekszik. A Tisza esese Szolnoktool Szegeedikig minddossze 0,00005 m/m.
- **Kettoos veszelyeztettettseg:** Arviz és aszaly egyidejuleg fenyeget -- a Tisza hullámtereben arvizi vedekezes zajlik, mikozben az Alfold belesejeeben aszaly uralkodik.
- **Töltesrendszer:** Toöbb mint 4200 km elsödleges arvizveedelmi töoltes -- Europa egyik legsürübb rendszere.
- **Talajvizfuggöseg:** Az Alfold telepuleseinek jelentős resze a sekely talajvízbol nyeri az ivovizet.

### 18.10.2 A Tisza: Europá egyik legkomplexebb folyorendszere

A Tisza vízgyűjtője (157 186 km2) Ukrajna, Romania, Szlovakia, Magyarország és Szerbia területere terjed ki. Az archullamok a kárpáti forrasvidekrol erkeznek, és a lapos magyar szakaszon lassan, de annál pusztitobban vonulnak vegig.

AI-alkalmazási lehetőségek a Tiszan:

| Alkalmazas | AI-technika | Hivatkozott fejezet |
|------------|-------------|---------------------|
| Arvizielőrejelzés Szolnoknal | LSTM + fizikai korlatok | 6. fejezet (modellezés) |
| Hullámtér-elontesi térkép | DEM-feldolgozás + HAND | 5. fejezet (kodgeneeralas) |
| Hataron atnnyulo adatcseere | Pipeline EFAS/GloFAS-hoz | 7. fejezet (pipeline) |
| Vizgyujto-gazdálkodási terv | RAG a VGT3-hoz | 9. fejezet (RAG) |
| Operativ elojelzesi rendszser | Digitalis iker | 10. fejezet (digitalis iker) |
| Modell-kalibráció | Agens AI | 11--12. fejezet (ágensek) |

### 18.10.3 A Duna és Budapest

Budapest ivoviz-ellatásának mintegy felet parti szuresü kutak biztositjak a Duna menten. Ezek a rendszerek a felszíni és felszín alatti vizmodellezés osszekapcsolasat igenylik -- pontosan az a feladat, amelyre a digitalis iker (18.8. szakasz) alkalmas.

A 2013-as dunai árviz Budapestneel 891 cm-es tetöszintet produkalt. Az AI-támogatott elojelzesi rendszer ezt az esemenyt a következőkeppen kezeli:

1. **ECMWF ensemble-elojelzes** feldolgozása pipeline-nal (7. fejezet)
2. **LSTM-elojelzes** a Duna budapesti szelvenere, 72 oras horizonttal
3. **HAND-szamitas** (terepfeldolgozás, 5. fejezet) az elontesi zonakra
4. **RAG-lekerdezees** a katasztrofaveedelmi protokollokrol (9. fejezet)
5. **Agens** az elorejelezes és a töltés-terhelees összevetesere (11. fejezet)

### 18.10.4 A Hortobagy és az Alfold talajvíze

A Hortobagy -- UNESCO Vilagöoroksegi Helyszin -- a sekely talajvíztol fugg, amely fenntartja szikes mocsarait és pusztait. A víztudomány számára ket kulcskerdes:

1. **Hogyan hat az eghajlatváltozás a talajvízutanpotlasra?** A 6. fejezet Boussinesq-modellje, AI-val paramétereezve.
2. **Hogyan hat a mezőgazdasági kitermeles a vizes eloohelyekre?** MODFLOW-szimuláció, ágens AI-val kalibraalva (18.9. szakasz).

A Debreceni Egyetem környezettudomaanyi kutatásainak kontextusa (amelyet a 6. fejezetben Kovacs Marta peldajan szemleltettunk) pontosan ez: a Hortobagy vizhaztartasat vizsgaalni az AI eszkozoeivel.

### 18.10.5 Vizugyi intezmenyek és adatforrások

| Intezmeny | Adatforrás | AI-alkalmazás |
|-----------|------------|---------------|
| OVF (Országos Vízügyi Főigazgatóság) | hydroinfo.hu valós idejű vízszint | Pipeline, LSTM |
| OMSZ (Országos Meteorológiai Szolgálat) | Csapadék, hőmérséklet | Pipeline, ERA5 validáció |
| Vízgyűjtő-gazdálkodási igazgatóságok | VGT, monitoring adatok | RAG, ágens |
| Copernicus (EU) | DEM, talajnedvesség, műholdkép | Terepanalízis, távérzékelés |
| ECMWF | ERA5, időjárás-előrejelzés | Modell-bemenet |

---

## 18.11 Gyakorlati feladatok

### 18.11.1 Feladat: Vízszint-monitoring pipeline

**Cél:** Építs egy automatizált pipeline-t, amely letölti és feldolgozza a Tisza három állomásának (Tokaj, Szolnok, Szeged) vízszintadatait.

**Lépések:**

1. Használd a 7. fejezet pipeline-architektúráját.
2. Kérd meg az AI-t (Claude, ChatGPT vagy Copilot), hogy generáljon egy Python-szkriptet, amely:
   - Letölti az elmúlt 30 nap adatait az OVF API-járól (vagy szimulált adatokból, ha az API nem elérhető)
   - Kitölti az adathiányokat lineáris interpolációval
   - Kiszámolja a napi min/max/átlag vízszintet
   - Idősor-grafikonon ábrázolja a három állomást egyetlen ábrán
   - Pirossal jelöli a I. fokú készültségi szintet meghaladó napokat
3. Teszteld a szkriptet, és kérd meg az AI-t, hogy javítsa a talált hibákat.
4. Bővítsd: adj hozzá e-mail riasztást, ha a készültségi szintet túllépik.

**Kapcsolódás korábbi fejezetekhez:** 5. fejezet (kódgenerálás), 7. fejezet (pipeline).

---

### 18.11.2 Feladat: Vízgyűjtő-lehatárolás AI-val

**Cél:** AI-asszisztens segítségével határolj le egy vízgyűjtőt DEM-ből.

**Lépések:**

1. Tölts le egy DEM-szelvényt a Copernicus GLO-30 adatbázisból a Zagyva vízgyűjtőjére (kb. 47.5°N, 19.8°E).
2. Kérd meg az AI-t, hogy generáljon egy WhiteboxTools-alapú Python-szkriptet a vízgyűjtő lehatárolásához (Fill -> FlowDirection -> FlowAccumulation -> SnapPourPoint -> Watershed).
3. Futtasd a szkriptet.
4. Ha az eredménybeli vízgyűjtő nem felel meg a várakozásaidnak, kérd meg az AI-t, hogy diagnosztizálja a problémát (lásd 18.3.2. szakasz).
5. Iterálj, amíg helyes eredményt kapsz.

**Kapcsolódás korábbi fejezetekhez:** 5. fejezet (kódgenerálás).

---

### 18.11.3 Feladat: LSTM vízszint-előrejelzés

**Cél:** Építs egy egyszerű LSTM modellt, amely a Tisza szolnoki vízszintjét jelzi előre.

**Lépések:**

1. Kérd meg az AI-t, hogy generáljon szintetikus tanító-adatokat (ha valós adatod nincs): 10 év napi vízszint + csapadék idősor, szinuszos szezonalitással és véletlenszerű árvízi eseményekkel.
2. Kérd meg az AI-t, hogy építsen egy LSTM modellt PyTorch-ban vagy TensorFlow-ban:
   - 30 napos visszatekintési ablak
   - 1 LSTM-réteg, 64 rejtett egység
   - 1 napos előrejelzés
3. Tanítsd be a modellt (70% tanítás, 15% validálás, 15% teszt).
4. Ábrázold a megfigyelt és előrejelzett vízszintet a teszthalmazon.
5. Számold ki az NSE-t és az RMSE-t.
6. Kérd meg az AI-t: "Hogyan javíthatnám a modellt?" -- és kövesd a javaslatait.

**Kapcsolódás korábbi fejezetekhez:** 6. fejezet (modellezés).

---

### 18.11.4 Feladat: RAG chatbot vízügyi jogszabalyokhoz

**Cél:** Építs egy egyszerű RAG-rendszert a Víz Keretirányelv szövegére.

**Lépések:**

1. Tölts le a Víz Keretirányelv magyar fordítását (PDF).
2. A 9. fejezet útmutatása szerint:
   - Bontsd chunk-okra (500 token)
   - Számíts embedding-vektorokat
   - Töltsd ChromaDB-be
3. Kérd meg az AI-t, hogy generálja a RAG-lekérdezési kódot.
4. Tesztelj három vízügyi kérdést:
   - "Mi a jó ökológiai állapot definíciója?"
   - "Milyen kivételek léteznek a 4. cikkely alatt?"
   - "Hogyan kell figyelembe venni a klímaváltozást a vízgyűjtő-gazdálkodási tervben?"
5. Ellenőrizd, hogy a RAG a helyes chunk-okat kereste-e vissza.

**Kapcsolódás korábbi fejezetekhez:** 9. fejezet (RAG).

---

### 18.11.5 Feladat: Hidrológiai kalibrációs ágens

**Cél:** Építs egy egyszerű ágens-hurkot, amely egy csapadék-lefolyás modellt kalibrál.

**Lépések:**

1. Használj egy egyszerű kéttározós modellt (két tartály sorozatkapcsolásban): az első a talajnedvességet reprezentálja, a második a felszíni lefolyást. Két paraméter: talajkapacitás (mm) és lefolyási tényező.
2. Generáltass szintetikus "megfigyelt" adatokat ismert paraméterekkel (pl. talajkapacitás=200 mm, lefolyási tényező=0,3).
3. A 12. fejezet keretrendszere szerint építs egy ágenshurkot:
   - Az ágens választ kezdeti paramétereket
   - Futtatja a modellt
   - Kiszámolja az NSE-t
   - Diagnosztizálja a hibákat (vizuális elemzés az LLM-mel)
   - Módosítja a paramétereket
   - Ismétli, amíg NSE > 0,8
4. Naplózd az ágens minden gondolkodási lépését és paraméterváltoztatását.
5. Hasonlítsd össze: hány iterációra volt szükség az ágensnek vs. egy egyszerű véletlenszerű keresnek?

**Kapcsolódás korábbi fejezetekhez:** 11. fejezet (ágensek), 12. fejezet (ágensek építése), 6. fejezet (modellezés).

---

## Összefoglalás

Ebben a fejezetben a könyv teljes eszköztárát a víztudományra alkalmaztuk:

| Fejezet | AI-technika | Vízügyi alkalmazás |
|---------|-------------|---------------------|
| 5. fejezet | Kódolási asszisztensek | DEM-feldolgozás, vízgyűjtő-lehatárolás |
| 6. fejezet | Matematikai modellezés | Saint-Venant, Boussinesq, Richards -> kód |
| 7. fejezet | Adat-pipeline-ok | Vízszint-monitoring, szenzor-adatfeldolgozás |
| 9. fejezet | RAG | Víz Keretirányelv chatbot, vízügyi jog |
| 10. fejezet | Digitális ikrek | Vízgyűjtő-szintű szimuláció valós idejű adattal |
| 11. fejezet | AI ágensek | Autonóm kalibráció, diagnosztikus gondolkodás |
| 12. fejezet | Ágensek építése | Hidrologiai modellezo ágens implementalasa |

A víztudomány az egyik legizgalmasabb alkalmazási területe az agentikus AI-nak, mert a feladatok természete -- iteratív, adatigényes, térbeli-időbeli, fizikai törvényekkel korlátozott -- pontosan megfelel annak, amiben az AI kiváló. A Tisza árhullámai nem várnak: az AI segít, hogy te sem kelljen.

---

> **Kulcsüzenet:** Az AI nem helyettesíti a hidrológust -- hanem lehetővé teszi, hogy a hidrológus arra összpontosítson, amiben az ember egyedülállóan jó: a fizikai megértés, a kreatív problémamegoldás és a döntéshozás. Az adatgyűjtés, a kódolás, a kalibráció és a dokumentálás egyre inkább az AI dolga.
