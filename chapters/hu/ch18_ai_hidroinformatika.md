# 18. fejezet -- AI a hidroinformatikaban

> **Fejezet-informacio**
> - **Kinek szol:** Hidrológusoknak, vizugyyi mernokoknek es kornyezetkutatoknak
> - **Eloismeretek:** 1-4. fejezet (AI alapok); a 5-12. fejezet hasznos, de nem kotelezo
> - **Amit megtanulsz:**
>   - Az AI alkalmazasa felszini es felszin alatti vizmodellezesbeen
>   - Pipeline-ok, kodgeneralas es digitalis ikrek vizugyi kontextusban
>   - Autonomv agensek vizgyujto-szintu kalibraciora
> - **Szukseges eszkozok:** Browser + terminal + Python
> - **Kapcsolodo fejezetek:** 6. fejezet (modellezes), 7. fejezet (pipeline-ok), 10. fejezet (digitalis ikrek), 19. fejezet (terinformatika)

---

## Nyito jelenet: A Tisza nem var

Kepzeld el a kovetkezo helyzetet. 2024 marciusaban a karpati forrasvideken harom egymast koveto ciklonrendszer huz at. Az elso nap 40 mm eso esik az ukran hegyvideken, a masodik nap ujabb 55 mm, a harmadikon a hoolvas is beindul. A Tisza felso szakaszan Rahonal a vizszint orank alatt emelkedik, es az arhullam megkezdi utjat lefele -- Tokaj, Tiszafured, Kiskor, Szolnok, Szeged fele. A magyar vizugyi szolgalatnak harom kerdesre kell valaszolnia, es gyorsan:

1. Milyen magasra emelkedik a viz Szolnoknal, es mikor erkezik a tetoszint?
2. A Nagy Magyar Alfoldon a sekely talajviz reagal-e az arhullamra, es ha igen, mely telepulesek kutjai kerulnek veszelybe?
3. A Hortobagy vizmerlegeben milyen valtozasokat okoz az esemeny a kovetkezo harom honapban?

Tizenot evvel ezelott ezekre a kerdesekre harom kulon csapat dolgozott volna, harom kulon szoftverrel, haromfele adatforrasbol. A felszini vizesek HEC-HMS-t futtattak volna kezi parameterezessel. A talajvizesek MODFLOW-t epitettek volna heti adat-frissitesi ciklussal. A vizmerleg-elemzok Excel-tablazatokat toltogettenek. Az eredmenyek osszefuzesere senki nem vallalkozott volna, mert az adatformatum-konverziok es az idoletezsi kihivasok kovetkezetesen meghaladtak a rendelkezesre allo idot.

2026-ban az AI megvaltoztatja ezt a kepet. Nem azert, mert a fizika lett egyszerubb -- a Saint-Venant-egyenletek, a Boussinesq-egyenlet es a Richards-egyenlet ma is ugyanolyan bonyolultak, mint szaz eve. Hanem azert, mert az AI kepesse teszi a hidrologust arra, hogy:

- **Automatizalja** az adatgyujtest es minoseg-ellenorzest (7. fejezet pipeline-jai vizugyi kontextusban)
- **Generaltassa** a numerikus kodjait (5. fejezet kodolasi asszisztensei vizmodellekre alkalmazva)
- **Tanittasson** gepitanulasi modelleket vizszint-elorejelzesre (6. fejezet modellezes)
- **Epitsen** RAG-alapu chatbotokat vizugyi szabalyozasi dokumentumokra (9. fejezet)
- **Letrehozzon** digitalis ikreket vizgyujto-szinten (10. fejezet)
- **Futtathasson** autonóm agenseket, amelyek onalloan kalibraljak a modelleket (11--12. fejezet)

Ez a fejezet vegigvezet azon, hogyan alkalmazhato az Agentikus AI Tudosoknak konyvben tanult minden technika egyetlen konkret szakteriuleten: a **hidroinformatikan** -- a viztudomany, a terinformatika, a szamitasi modellezes es az adattudomany metszeteben allo tudomanyagon.

---

## 18.1 A viztudomany digitalis forradalma

### 18.1.1 Mitol hidroinformatika a hidroinformatika?

A hidroinformatika nem egyszeru vizugy plusz informatika. A vizproblémak eredendoen terbeliek (egy adott vizgyujtore, talajretegre, mederszelvenyre vonatkoznak), eredendoen idosorjellegúek (orak, napok, evszakok, evtizedek alatt fejlodnek), es eredendoen adatigenyesek (muholdas adatok, terepi meresek, idojarasi modellek es demografiai adatbazisok osszekapcsolasat igenylik). Ez a harom jellemzo egyutt magyarazza, miert kulonosen alkalmas a viztudomany az AI-ra: a feladatok tobbsege nagy mennyisegu, heterogen, terbeli-idobeli adat feldolgozasat es osszefuzeset igenylo, iterativ munka -- vagyis pontosan az, amiben az AI kituno.

A hidroinformatika ot pillerre epul:

| Piller | Lenyeg | AI-relevancia |
|--------|--------|---------------|
| **Hidrologia** | A viz korforgas fizikaja | Az AI leforditja az egyenleteket kodra (6. fejezet) |
| **Terinformatika (GIS)** | Terbeli adatok tarolasa, elemzese | Az AI generálja a DEM-feldolgozasi szkripteket (5. fejezet) |
| **Szamitasi modellezes** | Numerikus szimulacio | Az AI autonoman kalibralja a modelleket (11--12. fejezet) |
| **Adattudomany** | Meresi adatok feldolgozasa | Az AI epittet pipeline-okat (7. fejezet) |
| **Valos ideju rendszerek** | Operativ elorejelzes, monitoring | Az AI digitalis ikreket futtat (10. fejezet) |

### 18.1.2 A kezi elemzestol az autonom modellezesig

A viztudomany fejlodese az elmult evtizedekben negy fazison ment at:

**1. fazis: Kezi elemzes (1950-es--1990-es evek).** A hidrológus kezi szamitasokkal, tablazatokkal es grafikus modszerekkel dolgozott. Egy vizgyujto lehatarolas napokat vett igenybe topokvafiai terkepen, vonalzoval es planimeeterrel.

**2. fazis: GIS-alapu elemzes (1990-es--2010-es evek).** A terinformatika lehetove tette a terbeli adatok digitalis tarolasat es elemzeset. Az ArcGIS es a QGIS eszkozei automatizaltak a terepfeldolgozast, de minden lepest kozzel kellett elkezdevezezeti indítani.

**3. fazis: Szkript-alapu automatizalas (2010-es evek).** A Python, az R es a parancssor-alapu eszkozok (TauDEM, WhiteboxTools) lehetove tettek a munkafolyamatok megismetelheto futtatását. Egyetlen szkript ezer vizgyujtot kepet feldolgozni egyetlen ejszaka alatt -- de a szkriptet embernek kellett megirnia, debuggolnia es karbantartania.

**4. fazis: AI-tamogatott es agentikus modellezes (2023-tol).** A nagy nyelvi modellek (LLM-ek) es az agensrendszerek lehetove teszik, hogy a hidrologus termeszetes nyelven fogalmazza meg a feladatot, az AI pedig generálja a kodot, futtatja a modellt, kiertekeli az eredmenyt, es iteral. A vizugy embere nem programozo -- viztudos, akinek az AI az asszisztense.

Ez a fejezet a negyedik fazisrol szol.

---

## 18.2 AI a hidrologiai adatgyujtesben

### 18.2.1 A vizugyi adatok sokfelesege

Mielott barmi modellt epitenenel, adatokra van szukseged. A viztudomanyban az adatforrások szokatlanul sokfélék:

| Adattipus | Forras | Idofelbontas | Terbeli lefedes |
|-----------|--------|--------------|-----------------|
| **Vizszint** | Automata vizmerceallomas (OVF hydroinfo.hu) | 15 perc -- 1 ora | Pontszeru (98 allomas Mo.-on) |
| **Csapadek** | Terepi csapadekmerok (OMSZ) | 10 perc -- 1 nap | Pontszeru (>200 allomas) |
| **Muholdas csapadek** | GPM IMERG, ERA5 reanalízis, Copernicus | 30 perc -- 1 nap | Racsos (0,1--0,25 fok) |
| **Talajvizszint** | Monitoring kutak (OVF) | Het -- honap | Pontszeru (>2000 kut) |
| **Idojaras-elorejelzes** | ECMWF, GFS, HRRR | 1--6 ora | Racsos (0,25--3 km) |
| **Taverzekeles** | Sentinel-2 (optikai), Sentinel-1 (radar) | 5--6 nap | 10--20 m felbontas |
| **Terepmodell (DEM)** | SRTM, Copernicus DEM, LiDAR | Statikus | 1--30 m felbontas |

A kihivas nem az, hogy ezek az adatok nem leterne -- hanem az, hogy mindegyik mas formatumban, mas koordinata-rendszerben, mas idofelbontassal es mas minosegi szinttel erkezik. Az adategyesites (data fusion) es a minoseg-ellenorzes (quality control) a hidrologus munkaidejanak jelentos reszet emeszti fel.

### 18.2.2 Pipeline-ok a vizugyi adatgyujteshez

A 7. fejezetben megtanultad, hogyan epithetod fel az adat-pipeline-ok ot szakaszat: bevitel, tisztitas, transzformacio, elemzes, kimenet. A vizugyi kontextusban ez igy nez ki:

```
┌──────────────────┐    ┌────────────────┐    ┌──────────────────┐    ┌───────────────┐    ┌──────────────────┐
│  1. BEVITEL      │───>│  2. TISZTITAS  │───>│ 3. TRANSZFORMACIO│───>│  4. ELEMZES   │───>│  5. KIMENET      │
│ OVF API          │    │ Hibas ertekek  │    │ EOV -> WGS84     │    │ Statisztika   │    │ Dashboard        │
│ OMSZ FTP         │    │ Adathianyok    │    │ Idozóna-korr.    │    │ Trendek       │    │ Modell-bemenet   │
│ Copernicus CDS   │    │ Szenzorhiba    │    │ Ujramintavetelezes│   │ Anomaliak     │    │ Riasztas         │
│ ERA5 API         │    │ Dublikaciok    │    │ Terbeli aggreg.  │    │               │    │                  │
└──────────────────┘    └────────────────┘    └──────────────────┘    └───────────────┘    └──────────────────┘
```

Az AI segitsege mar a pipeline-tervezesnel megmutatkozik. Nezzuk, hogyan kerheted meg a Claude-ot vagy a ChatGPT-t, hogy segitsen az OVF vizszint-adatok automatikus letöltéseben:

---

**Te:**

> Irj egy Python scriptet, amely naponta reggel 6-kor automatikusan letolti az elmult 24 ora vizszintadatait a hydroinfo.hu API-jarol a Tisza folyo kovetkezo allomasaira: Tokaj, Tiszafured, Kiskor, Szolnok, Csongrad, Szeged. Az adatokat mentes el egy SQLite adatbazisba idosorformaban, es ha bármely allomasnál a vizszint meghaladja az I. fokú keszultsegi szintet, küldjon e-mail riasztast.

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

Ez a peldakod termeszetesen egyszerusitett -- az eles rendszerben kezelni kell a halozati hibakat, az API rate limit-et, a hianyzo adatokat es a naplozast. A lenyeg az, hogy az AI kepes percek alatt letrehozni egy mukodo pipeline-vazat, amelyet aztán te tesztelsz es finomitasz.

### 18.2.3 Minoseg-ellenorzes AI-val

A vizugyi meresek minoseg-ellenorzese (quality control, QC) kritikus fontossagu. Egy hibas szenzor, amely 999 cm-es vizszintet jelent, vagy egy lefagyott csapadekmerő, amely hetekig nullat küld, hamis riasztast valthat ki vagy -- ami rosszabb -- elmarado riasztast. A hagyomanyos QC szabalyalapu: ha az ertek egy eloirt tartomanyba esik es az elterese az elozo merestol nem haladja meg a kuszoberteket, elfogadjuk.

Az AI ket szinten segithet:

1. **Anomalia-detektalas gepitanulassal.** Egy isolation forest vagy autoencoder-alapu modell a normalis szenzorviselkedest tanulja meg az elozmeny-adatokbol, es kijeloli azokat az ertekeket, amelyek nem illeszkednek a mintazatba -- meg akkor is, ha azok formal szinten "szabalyosak". Peldaul egy vizszint, ami lassan, monoton no, mikozben a kornyezo allomasokon mar apadast mertek, statisztikailag anomalia.

2. **LLM-alapu minoseg-jelentes.** Az AI osszefoglalhatja az adatminosegi helyzetet termeszetes nyelven: "Az elmult heten a szolnoki allomas ket 15 perces adathianyt mutat marcius 12-en delutan. A kiskorei allomas csapadekmeroje marcius 14. ota nullat jelent, mikozben a szomszedos allomások 8-12 mm-t regisztraltak -- valoszinu szenzor-meghibasodas." Ez a fajta diagnosztikus osszefoglalo pontosan az, amire a vizugyi ugyelet szüksegel -- es amire az LLM-ek kiválóan alkalmasak.

A 7. fejezet pipeline-architekturajat alkalmazva a QC lepest a tisztitasi szakaszba (2. szakasz) epitjuk be, az anomalia-modellt pedig az elemzesi szakaszba (4. szakasz).

---

## 18.3 AI-tamogatott terepanalízis

### 18.3.1 A vizgyujto-lehatarolas mint kodgeneralasi feladat

A 5. fejezetben megtanultad, hogyan hasznalhatod az AI-t kodolasi asszisztenskent. A viztudomanyban az egyik leggyakoribb feldolgozasi lanc a vizgyujto-lehatarolas DEM-bol:

1. Melyedesek kitoltese (Fill)
2. Folyasirany szamitas (FlowDirection)
3. Folyasakkumulacio (FlowAccumulation)
4. Vizfolyashálózat meghatározása (kuszobertek-alapu)
5. Kiontesi pont kijelelese (SnapPourPoint)
6. Vizgyujto lehatarolas (Watershed)

Ez a hat lepes manualis GIS-ben 20-30 percet vesz igenybe egyetlen vizgyujtore. Ezer vizgyujtore? A 12. fejezet (munkafolyamat-automatizalas) megmutatta, hogyan irunk erre Python-szkriptet. De mi van, ha nem akarsz szkriptet irni -- hanem az AI-val iratsz egyet?

---

**Te:**

> WhiteboxTools-t hasznalva irj egy Python szkriptet, amely (1) beolvas egy GeoTIFF DEM-et, (2) kitolti a melyedeseket, (3) D8 folyasiranyt szamol, (4) folyasakkumulaciot szamol, (5) egy megadott koordinata-pont korul lehataroja a vizgyujtot, es (6) exportalja a vizgyujto-hatart shapefile-kent. Az input DEM felbontasa 10 meter, EOV koordinata-rendszerben van (EPSG:23700).

---

Az AI nehany masodperc alatt generálja a teljes szkriptet, beleertve az importokat, a fajlkezelest, a hibakezelest es a koordinata-transzformaciot. A kulonbseg a hagyomanyos megkozelitestol:

| Hagyomanyos | AI-tamogatott |
|-------------|---------------|
| Megtanulod a WhiteboxTools dokumentációt | Leirod, mit akarsz |
| Probalkozol a parameterezessel | Az AI ajánl parametereket |
| Debuggolsz orakig | Az AI javitja a hibakat |
| Egyetlen vizgyujtore | Az AI ciklussa terjeszti ki |

### 18.3.2 LLM-ek a DEM-feldolgozas hibainak diagnosztizalasahoz

A terepfeldolgozas gyakori problemaja, hogy a vizgyujto-lehatarolas nem felel meg a varakozasoknak: tul kicsi, tul nagy, vagy "furcsaan" nez ki a terepen. Az LLM-ek kivaloan alkalmasak a hiba diagnosztizalasara:

---

**Te:**

> A vizgyujto-lehatarolas a Zala felso szakaszara egy 930 km2 helyett csak 47 km2-es terulet adott. A DEM 10 m-es felbontasu, az Copernicus GLO-30-bol szarmazik. Mi lehet a problema?

---

**AI:**

> Negy valoszinu ok letezik, valoszinusegi sorrendben:
>
> 1. **A kiontesi pont koordinataja pontatlan.** Ha a pont nem pontosan a medervonalra esik, a FlowAccumulation-raszteren kis akkumulacios ertek tartozik hozza, es a lehatarolas csak a lokalis minimedencet ragadja meg. **Megoldas:** Hasznalj SnapPourPoint-ot 500 m-es illesztesi tavolsaggal.
>
> 2. **A DEM melyedesei nincsenek kitoltve.** A GLO-30 nyers DEM-ben hidak, epuletek es mas mutargyak hamis melyedeseket hozhatnak letre, amelyek megszakitjak a folyasiranyokat. **Megoldas:** Ellenorizd, hogy a Fill lepes tenyleg lefutott-e, es noveld a z-limit erteket.
>
> 3. **Koordinata-rendszer hibas.** Ha a DEM WGS84-ben van, de a kiontesi pont EOV-ben (EPSG:23700), a koordinata-parok nem felelnek meg egymasnak. **Megoldas:** Ellenorizd, hogy mindket reteg azonos CRS-ben van-e.
>
> 4. **A DEM felbontasa nem elegendo.** A 30 m-es GLO-30 a Zala szuk volgyeiben nem mindig ragadja meg a mederstrukurat. **Megoldas:** Provalj 10 m-es EU-DEM-et vagy LiDAR-alapu DEM-et.

Ez a fajta diagnosztikus gondolkodas -- amit a 24. fejezetben a HydroGIS konyv agens AI-janal lattunk -- pontosan az, amire a tudos szuksegel: nem ujabb kodsort, hanem **megertesi tamogatast**.

### 18.3.3 Vizhalozat-kinyeres es jellemzes

A vizgyujto-lehatarolas utan a vizhalozat kinyerese kovetkezik. Az AI itt is segit: generálhat szkriptet, amely TauDEM-mel vagy WhiteboxTools-szal:

- Kinyeri a vizhalozatot (StreamToFeature)
- Kiszamolja a Strahler-rendet
- Megmeeri a szakaszhosszakat es eseeseket
- Osszekapcsolja a vizhalozatot az OVF vizmerceallomásokkal
- Generalja a RAPID hullámtranszformációhoz szukseges kapcsolodasi tablakat

A lenyeg nem az, hogy az AI jobb programozo, mint te -- hanem az, hogy a feladat, amelyre eddig egy GIS-szakembernek harom napra volt szuksege, most egy delutan alatt elvegezeheto, a kutato termeszetes nyelvu utasitasaival.

---

## 18.4 Gepi tanulas a vizszint-elorejelzesben

### 18.4.1 Miert alkalmas az LSTM az arvizelorejelzesre?

Az arvizelorejelzes lenyegeben idosor-problema: a mult csapadek- es vizszint-adataiból kell elojejelezni a jovobelieket. A 6. fejezetben altalanosan targyaltuk az AI-tamogatott modellezest; itt a hidrologiai alkalmazast vesszuk reszletesen.

A Long Short-Term Memory (LSTM) halozat kulonosen alkalmas erre a feladatra, mert:

1. **Hosszu tavu fuggesegeket tanul meg.** A Tisza archullamja Rahotol Szolnokig 3-5 napig tart -- az LSTM cellaállapota kepegges ilyen idobeli kapcsolatokat megragadni.
2. **Tobbresu bemenetet kezel.** Csapadek, homerseklet, felso szakaszi vizallás, talajnedvesseg, hovas -- mind parhuzamosan epithetok a modellbe.
3. **Nem linearis osszefuggeset tanul.** A vizgyujto valasza a csapadekra nem linearis: szaraz talajon 10 mm eso alig okoz lefolyast, telitett talajon ugyanennyi arhullámot indithat.

### 18.4.2 Szamitasi pelda: vizszint-elorejelzes a Tiszan

Vegyunk egy konkret feladatot: napi vizszint-elojelezés a Tisza szolnoki szelvenyben, 1-3 napos eloretekentéssel.

**Bemeneti adatok:**
- Napi csapadek 10 meteorologiai allomasrol a felso vizgyujtorol (ERA5 reanalízis)
- Napi átlaghomerseklet (hoolvadas szamítasahoz)
- Vizszint-elozmeny Tokaj, Tiszafured, Kiskor allomasokon (kesleltetett bemenetek)
- Talajnedvessegi index (Copernicus Soil Moisture)
- Evszakon beluli nap (sin/cos kodolassal)

**Architektura:**

| Parameter | Ertek |
|-----------|-------|
| Bemeneti jellemzok | 18 |
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

> Epitts egy LSTM modellt PyTorch-ban, amely a Tisza szolnoki vizszintjet jelzi elore 1-3 napra. A bemeneti CSV tartalmaz 18 jellemzot es 20 ev napi adatot (2003-2022). Osszd fel a datasort: 2003-2016 tanitas, 2017-2019 validalas, 2020-2022 teszt. Hasznalj 45 napos visszatekentesi ablakot, 2 LSTM-reteget 128 rejtett egyseggel, dropout=0,2, es NSE-alapu veszteségfuggvenyt. Abrazold a tesztev vizszint-elorejelezes es a megfigyelt ertekek osszeveteset.

---

A 23. fejezet (HydroGIS) reszletesen bemutatja, hogy egy ilyen LSTM-modell 0,87-os NSE-t erhet el a teszthalmazon -- jol megragadja az árvizi csúcsok idoziteset, bar szisztematikusan alulbecsuli a legnagyobb esemenyeket. Ez a korlat nem kizarolag az adatvezérelt megkozelitesekre jellemzo -- a fizikai alapu modellek is küszködnek a szélsőségekkel --, de az ML-modelleknkel kulonosen fontos felismerni, mert nincs fizikai korlat, amely megakadalyozna a valoszinütlen eredmenyeket.

### 18.4.3 Talalajvízszint-elojelezés

A talajvizszint-elorejelzes mas jellegú problema. A felszin alatti vizszint valtozasai lassabbak (hetek-honapok), a bemeneti adatok ritkabbak (heti-havi meresek), es a fizikai osszefuggesek bonyolultabbak (a Darcy-torveny haromdimenzios heterogen kozegben ervenyes). Megis, a gepi tanulas itt is eredmenyes:

**Random forest/gradient boosting modell a talajvizszintre:**
- Bemenetek: csapadek, evapotranszspiracio, Duna/Tisza vizszint, elozmenybeli talajvízszint, felszinhaszalat, talajfizikai parameteerek
- Kimenet: talajvizszint-valtozas a kovetkezo honapra
- Alkalmazas: az Alfold 2000+ monitoring kutja

A 6. fejezet modellezesi keretrendszeret koveteve:

1. **Adatelokeszites:** pipeline (7. fejezet) az OVF talajviz-adatbazisbol
2. **Feature engineering:** az AI javasol uj jellemzoket (pl. 30/60/90 napos kummulatív csapadek, talajvizszint trendkomponens)
3. **Modelltanitas:** scikit-learn gradient boosting vagy XGBoost
4. **Kiertekeles:** R2, RMSE, es -- ami kulonosen fontos -- a szaraz nyari kisviz-idoszakok helyes elojelzesee

### 18.4.4 Fizika-informalt gepi tanulas (PIML)

A legigéeretesebb fejlemeny a fizika-informalt gepi tanulas (Physics-Informed Machine Learning, PIML), amely a fizikai egyenleteket a neuralis halozat veszteségfuggvenyebe epiti be. Ahelyett, hogy az LSTM szabadon tanulna tetszoleges osszefuggeseket, a veszeségfuggvenyben butetjuk azokat a megoldasokat, amelyek fizikailag lehetetlenek:

$$\mathcal{L} = \mathcal{L}_{\text{adat}} + \lambda \cdot \mathcal{L}_{\text{fizika}}$$

ahol:
- $\mathcal{L}_{\text{adat}}$ a megfigyelt es szimulalt értékek közötti elteres (pl. MSE)
- $\mathcal{L}_{\text{fizika}}$ a fizikai torveny serteseenek merteke (pl. a vizmerleg-megmaradas hianya)
- $\lambda$ a ket tag kozötti sulyozas

Peldaul a vizgyujto vizmerlegere:

$$P - ET - Q - \Delta S = 0$$

ahol $P$ a csapadek, $ET$ az evapotranszspiracio, $Q$ a lefolyas, $\Delta S$ a tarolasvaltozas. Ha az LSTM olyan vizszint-elojelzest produkalna, amely a vizmerleg-egyenlettel inkonzisztens, a veszteségfuggveny bunteti.

Ez a megkozelites ot az 5. fejezet (AI-tamogatott kodgeneralas) es a 6. fejezet (matematikai modellezes) metszeteben all: az AI segit megirni a fizika-informalt veszteségfuggvenyt, az LLM diagnosztizalja, hogy miert nem konvergal a tanitas, es az agens autonoman hangolja a $\lambda$ hiperparametert.

---

## 18.5 Matematikai modellezes AI-val: egyenletektol a kodig

### 18.5.1 A viztudomany alapegyenletei

A hidrologianak harom alapveto parciális differencialegyenlete van, amelyekkel a kutato rendszeresen talalkozik:

**1. Saint-Venant-egyenletek** (felszini aramlás nyilt mederben):

Kontinuitasi egyenlet:
$$\frac{\partial A}{\partial t} + \frac{\partial Q}{\partial x} = q_L$$

Impulzusegyenlet:
$$\frac{\partial Q}{\partial t} + \frac{\partial}{\partial x}\left(\frac{Q^2}{A}\right) + gA\frac{\partial h}{\partial x} = gA(S_0 - S_f)$$

ahol $A$ a mederkeresztmetszet, $Q$ a vizhozam, $q_L$ az oldaliranyú betaplálás, $g$ a gravitacios gyorsulas, $h$ a vizszint, $S_0$ a medereseés es $S_f$ a surlodasi esesés.

**2. Richards-egyenlet** (telitetlen zona vízmozgas):

$$\frac{\partial \theta}{\partial t} = \frac{\partial}{\partial z}\left[K(\theta)\left(\frac{\partial h}{\partial z} + 1\right)\right]$$

ahol $\theta$ a terfogoatos viztatralom, $K(\theta)$ a telitettsegtol fuggo szivargasi tenyezo, $h$ a szivasi nyomasmagassag.

**3. Boussinesq-egyenlet** (felszín alatti vizaramlas):

$$S_y \frac{\partial h}{\partial t} = \frac{\partial}{\partial x}\left(K h \frac{\partial h}{\partial x}\right) + \frac{\partial}{\partial y}\left(K h \frac{\partial h}{\partial y}\right) + W$$

ahol $S_y$ a fajlagos hozam, $h$ a vizszint, $K$ a szivargasi tenyezo, $W$ a forras/nyelo tagok (utanpotlas, szivattyas).

### 18.5.2 AI mint matematikai fordító

A 6. fejezet bemutatta, hogyan hasznalhato az AI arra, hogy kutatasi kerdest matematikai formaba, majd kodra fordítson. A viztudomanyban ez igy nez ki a gyakorlatban:

---

**Te:**

> A Hortobagy teruleten szeretnem modellezni, hogyan valtozik a talajvizszint, ha a nyari csapadek 20%-kal csokken. A terüulet 50 km x 50 km, a vizado homokos, a szivargasi tenyezo K = 5 m/nap, a fajlagos hozam Sy = 0,15. A peremfeltetelek: nyugaton a Tisza allandonizszintje 82 m, keleten nulla-flux hatar. Az utanpotlas az eves csapadek 15%-a. Irj egy Python szimulaciot veges differenciaval, 500 m-es racssal, es abrazold a talajvizszint-valtozast 10 ev mulva.

---

Az AI a Boussinesq-egyenlet 2D veges differencia diszkretizaciojat generalja, a megadott parametererekkel, es Matplotlib abrakat keszit. A 6. fejezet útmutatasa szerint:

1. **Ne fogadd el vakon a kodot.** Ellenorizd az egyenlet-diszkretizaciot, a peremfelteeteleket es a numerikus stabilitas.
2. **Kerd meg az AI-t, magyarazza el a lepeseket.** "Miert eztet az idolepest valasztottad? Mi tortenik, ha a szivargasi tenyezo terben valtozik?"
3. **Validald egyszerű esettel.** Kerd meg az AI-t, hogy futtasson egy egydimenziós analitikus megoldassal osszevetheto tesztesetet.

### 18.5.3 A Saint-Venant-egyenletek numerikus implementacioja

A Saint-Venant-egyenletek numerikus megoldasanak generálasa az egyik legosszetettebb feladat, amelyet LLM-től kerhetsz. A teljes egyenletrendszer (dinamikus hullam) numerikusan instabil lehet, ezert a vizugyben gyakran egyszerusitett valtozatokat hasznalnak:

| Kozelites | Elhanyagolt tagok | Alkalmazas |
|-----------|-------------------|------------|
| Kinematikus hullam | Lokalis es advektiv gyorsulas, nyomasgradiens | Meredek leftu patakok |
| Diffuz hullam | Lokalis es advektiv gyorsulas | Lapos artéri áramlas |
| Dinamikus hullam | Semmi (teljes egyenlet) | Vizlepcsok, arapaly |

Az AI segithet abban, hogy eldöntsd, melyik kozelites alkalmas a te feladatodra. Peldaul:

---

**Te:**

> A Tisza Szolnok alatti szakaszaran (nagyon lapos, 0,00005 m/m esés) modellezni akarom egy arhullam terjedeset. Melyik Saint-Venant kozeliteset hasznaljam?

---

**AI:**

> Ilyen lapos esesneel a kinematikus hullam **nem** alkalmas, mert elhanyagolja a nyomasgradienst, amely az alacsony esésú medrekneel a meghaterozo erohatás. A **diffuz hullam** kozelites javasolt: figyelembe veszi a nyomasgradienst, de elhanyagolja a teheetlensegi tagokat, amelyek csak hirtelen valtozasoknal (gatzakadas, zsilipnyitas) lenyegesek. Ha gatzakadas-szcennariora is szükseg van, a **teljes dinamikus hullam** kell.

Ez a fajta fizikai konzultació -- amit a 23. fejezet (HydroGIS) "MI mint a hidrologus asszisztense" cimu fejezetben reszletesen targyalunk -- az AI egyik legertekesebb alkalmazása a viztudomanyban.

---

## 18.6 Adat-pipeline-ok a hidrologiai monitoringhoz

### 18.6.1 Az operativ monitoring kihívásai

Egy operativ vizugyi monitoring-rendszer nem egyszeri elemzes -- folyamatosan, automatikusan, megbizhataon kell mukodnie. A 7. fejezet pipeline-koncepcioját a vizugyi kontextusra alkalmazva az operativ pipeline-nak a kovetkezo kovetelményeknek kell megfelelnie:

| Kovetelmeny | Megvalostias |
|-------------|--------------|
| **Folyamatos bemenet** | Szenzor-adatok 15 percenkent, muholdas adatok napi frissitessel |
| **Minoseg-ellenorzes** | Automatikus anomalia-detektalas + emberi jovahagy vahagy |
| **Latesedelmentseg** | Ertesites < 5 perc a szenzor-leolvasas utan |
| **Megbizhatsag** | 99,9% uptime, automatikus ujraindulas hiba eseten |
| **Skálazhatosag** | 100+ allomas, 10+ parameter, eseemennyalapú felskalazas |

### 18.6.2 A vizugyi monitoring pipeline felépítese

Egy teljes vizugyi monitoring pipeline a 7. fejezet architekturajat koveti, de domain-specifikus elemekkel:

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

A pipeline-t a 7. fejezet segedprogramjaival (cron job, Airflow, Prefect) utemezed -- peldaul orankeneti futatassal, külön napi batch-futatassal a muholdas adatokhoz.

### 18.6.3 AI a pipeline-generalsaban

Az igazi attores az, amikor nem te irod a pipeline-t, hanem az AI-val iratod:

---

**Te:**

> Epits egy Prefect-alapu pipeline-t, amely orankennt letolti a Tisza ot fó allomasanak vizszintadatait az OVF API-jarol, futtat egy elotre betanitott LSTM modellt 24 oras elorejelzesre, es ha barmely allomasnál az elorejelzett vizszint meghaladja az I. fokú keszultsegi szintet, Slack-üzenetet kuld a "flood-alerts" csatornara. A pipeline log-oljon minden lepest, es ha az API nem valaszol 30 masodpercen belul, hasznaljon cache-elt adatot.

---

Az AI generálja a teljes Prefect-flow-t, a dekoratorokkal, a hibakezeléssel es a Slack-integrációval. Te az eredmenyt teszteled, validálod es eles koraárnyezealbe viszed.

---

## 18.7 RAG a vizugyi szabalyozashoz

### 18.7.1 A vizugyi jogi környezes bonyolultsaga

A vizugyi munka nem csak fizika es modellezes -- a szabalyozasi koernyezt is ismerni kell. Magyarorszagon es az EU-ban a vizugyi jogszabalyok tobb retegu rendszert alkotnak:

| Szint | Jogszabaly | Terjedelem |
|-------|-----------|------------|
| **EU** | Viz Keretiranyelv (2000/60/EK) | ~100 oldal + mellekletek |
| **EU** | Arvizi Iranyelv (2007/60/EK) | ~30 oldal |
| **EU** | Talajviz Iranyelv (2006/118/EK) | ~25 oldal |
| **Magyar** | 1995. evi LVII. torveny a vizgazdalkodasrol | ~80 oldal |
| **Magyar** | 232/1996. (XII. 26.) Korm. rendelet (vizugyi hat. eljaras) | ~40 oldal |
| **Magyar** | Vizgyujto-gazdalkodasi Tervek (VGT2, VGT3) | 1000+ oldal |
| **Magyar** | Kornyezeti hatasvalgazalasi dokumentumok | Projekt-specifikus |

Egy kutato, aki vizgyujto-gazdalkodasi tervet keszit, vagy kornyezeti hatastanulmanyt ir, rendszeresen kell hivatkoznia ezekre a dokumentumokra. A hagyomanyos megkozelites: PDF-eket bongeszni, Ctrl+F-fel keresni. Ez lassúu es hibara hajlamos.

### 18.7.2 RAG-rendszer vizugyi dokumentumokra

A 9. fejezetben megtanultad, hogyan epithetoz RAG (Retrieval-Augmented Generation) rendszert. A vizugyi alkalmazas pontosan koveti az ott leirt architektuarat:

**1. Dokumentumok begyüjtése:**
- EU Viz Keretiranyelv (magyar forditas)
- Arvizi Iranyelv
- Magyar vizgazdalkodasi torveny
- VGT3 (Vizgyujto-gazdalkodasi Terv)
- OVF szakmai utmutatok
- Vonatkozo EIA (kornyezeti hatasvalgazalaási) dokumentumok

**2. Chunk-olas es embedding:**
- A dokumentumokat 500-1000 tokenes darabokra bontjuk
- Embedding-vektorokat szamitatunk (pl. OpenAI text-embedding-3-large vagy Cohere multilingual)
- A vektorokat ChromaDB vagy Qdrant adatbazisba taroljuk

**3. Kerdezes:**

---

**Te (a RAG chatbotnak):**

> A Tisza vizgyujtojen tervezett egy uj termelokkut-telep engedelyezteesi eljaarasahoz milyen feltételeknek kell megfelelni a Viz Keretiranyelv 4. cikkelye szerint?

---

**RAG chatbot:**

> A Viz Keretiranyelv 4. cikkely (7) bekezdes szerint uj tevekeenysegek engedelyezesekor biztositani kell, hogy az nem okozza a viztest allapotanak romlasaat ("no deterioration" elv). Konkretant:
>
> 1. Az uj kitermel nem okozhatja a talajviztest mennyisegi állapotanak romlasát [VKI 4. cikk (1)(b)(i)]
> 2. Nem veszelyeztetheti a kapcsolodo felszini vizek okologiai allapotat [VKI 4. cikk (1)(a)(i)]
> 3. A magyar vizgazdalkodasi torveny (1995:LVII. tv.) 15. § szerint vizjogi engedelyt kell kerni...
>
> **Forrasok:** VKI_4_cikkely.pdf (chunk 23), Vizgazd_tv_15.pdf (chunk 7), VGT3_Tisza_II_4.pdf (chunk 145)

A RAG-rendszer erteke nem az, hogy tokeletes jogi tanacsot ad -- hanem az, hogy masodpercek alatt megtalálja a releváns jogszabaly-helyet, es a kutato ellenorizheti a hivatkozott forrast. A 9. fejezet osszes figyelmeztetese itt is ervenyes: a RAG-rendszer hallucinalgat, es jogi kerdesekben soha nem szabad vakon elfogadni az AI valaszat.

---

## 18.8 Hidrologiai digitalis ikrek

### 18.8.1 Mi a digitális iker a viztudomanyban?

A 10. fejezet bevezette a digitalis iker (digital twin) fogalmat: egy fizikai rendszer virtualis masata, amely valos ideju szenzor-adatokkal szinkronban fut. A viztudomanyban a digitalis iker egy vizgyujto-szintu szimulacio, amely:

1. **Tukrozi** a valos rendszert: a terep, a vizhalozat, a vizadok, az idojaras
2. **Szinkronban van** a valos szenzorokkal: vizmerceek, csadekmerok, talajviz-monitoring kutak
3. **Elorejeelez:** "mi tortenik, ha...?" kerdesekre valaszol
4. **Tanul:** minden uj meres javitja a modell pontossagat

### 18.8.2 Egy vizgyujto-szintu digitalis iker felepitese

Peldakent vegyuk a **Zala vizgyujto** -- a Balaton legnagyobb mellekfollyjaat --, amelyet a HydroGIS koonyv 24. fejezete is peldakent hasznalt az agens-alapú kalibrálashoz.

A digitális iker komponensei (a 10. fejezet architekturaja szerint):

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

- **Mi tortenik, ha a Zala felso szakaszan 80 mm eso esik 24 ora alatt?** A modell futtatja a csapadek-lefolyas modult, a hullámtranszformaciott, es elojelzi a vizszintet minden szelvenyben.
- **Mi tortenik, ha a Balaton szintje 20 cm-rel emelkedik?** A modell a megvaltozott peremfeltetelbol szamolja a hatteráramlást a Zala alluvilialis vizadojaaban.
- **Mi tortenik, ha uj termelokutat telepitenek Zalaegerszeg mellé?** A talajviz-modul szamolja a leszivast es annak hatasát a Zala alaphozamara.

### 18.8.3 Az AI szerepe a digitalis ikerben

A 10. fejezetben targyalt digitalis iker elveket a vizgyujtora alkalmazva az AI harom szinten mukodik:

1. **Adataszimilacio:** Az LSTM-modell a valós ideju szenzor-adatokat használja az elorejelezsesi allapot frissítesere (a Kalman-szuro analogiaja, de neurális halozattal).

2. **Automatikus kalibracio:** Ha az elojelzett es a megfigyelt vizszint elterese noovekszik, az agens AI (lased 18.9. szakasz) automatikusan ujrakalibralja a modellt.

3. **Természetes nyelvu lekerdeezes:** A vizugyi ugyelet természetes nyelven kerdezhet a digitalis ikertol: "Mi az erojelzett vizszint Szolnoknal holnaputan?" -- es az LLM a modell eredmenyebol generalja a választ.

---

## 18.9 AI agensek az autonóm hidrologiai modellezesben

### 18.9.1 A kalibracios probléma mint agens-feladat

A HydroGIS konyv 24. fejezete reszletesen bemutatja, hogyan alkalmazhato az agens AI a hidrologiai modellek autonomo modellezesere. A lenyeget a kovetkezőkben foglaljuk ossze, és osszekapcsoljuk az "Agentikus AI Tudosoknak" koonyv 11. es 12. fejezetenek agens-architekturájaval.

A hidrologiai modellek kalibracioja a kovetkezo lepesekbol all:

1. Adatok beolvasasa es ellenorzese
2. Kezdeti parameterek becslese (szaktudas alapjan)
3. Modell futtatasa
4. Eredmenyek kiertékelese (NSE, KGE, PBIAS, vizualis ellenorzes)
5. Parameterek módositasa a diagnozis alappjan
6. Ismetles konvergenciaig

Ez pontosan az a **tervezes--vegrehajas--ertekelés--iteracio** ciklus, amelyet a 11. fejezetben az agens AI alappkent ismertettünk:

| Agens-komponens (11. fejezet) | Hidrologiai megfelelo |
|-------------------------------|------------------------|
| **Cel** | "Kalibrald a GR4J modellt NSE > 0,7-re" |
| **Tervezes** | Parametertertományok meghatarozasa, strategia valasztas |
| **Eszkozok** | Modellfuttato, adatolvasoo, kiertekelo, vizualizalo |
| **Vegrehajas** | Modell futtatasa adott parameterkeszlettel |
| **Ertekeles** | NSE, KGE szamitas + vizsgálgorbe diagnosztika |
| **Memoria** | Korabbi parameterkeszletek es teljesitmenyuk naploja |
| **Iteracio** | Parametermodositas a diagnozis alapjan |

### 18.9.2 A HydroGIS 24. fejezet pelda-agense

A HydroGIS konyv 24. fejezete egy teljes peldaval szemlelteti az agens-alapu kalibraciot: a **Zala folyo zalaegerszegi** vizgyujtojere alkalmazva a GR4J modellt. A pelda kovetkezményei az AI-agensek megertese szemontjabol (11--12. fejezet):

**1. lepes: Az agens beolvassa es megvizsgalja az adatokat.**

Az agens nem egyszereuen betolti az adatokat -- *megvizsgalja* oket. Kiszamolja a lefolyasi tenyezot (0,23), osszeveti a regiiora jellemzo ertekekkel, ellenorzi az adathiányokat. Ez a "gondolkodo" (reasoner) szint, amelyet a 11. fejezet a 2. szinten targyalt.

**2. lepes: Az agens hidrologiai tudast hasznal a kezdeti parametervalasztashoz.**

Ahelyett, hogy a parameter-tartomany veletllenszeru pontjaról indulna (mint az SCE-UA optimalizalo), az agens a vizgyujto jellemzoi -- agyagos-homokos talaj, 0,23-as lefolyas tenyezo, 930 km2 terulet -- alapjan becsüli a kezdeti parametereket. A HydroGIS szerzoi ezt "diagnosztiakus gondolkodasnak" nevezik.

**3. lepes: Futtatás, értékeles, iteráció.**

Az agens futtatja a modellt, kiszamolja az NSE-t (0,59 az elso iteracioban), megvizsgálja a vizsgalgorbeet ("a csúcsok tul magasak es túl korán jelentkeznek"), es ennek alapjan modositja a parametereket. 8 iteracio utaán eleri az NSE = 0,74 erteket.

**Az agens eronye a hagyomanyos optimalizalassal szemben:**

| Jellemzo | SCE-UA (hagyomanyos) | Agens AI |
|----------|----------------------|----------|
| Modell-futtatások szama | 5 000--50 000 | 50--200 |
| Diagnosztikus gondolkodás | Nincs | Van (LLM) |
| Fizikai korlaátok | Csak parameter-hatarok | Gondolkodas + hatarok |
| Dokumentalas | Keresesi naplo | Ervelesi naplo (termeszetes nyelven) |
| Elfogadhato megoldas eléresi ideje | Orak | Percek |

### 18.9.3 Agens epites a 12. fejezet keretrendszerevel

A 12. fejezetben megtanultad, hogyan epitesz AI agenseket. A hidrologiai modellezesi agens a kovetkezo eszkozkeszlettel mukodik:

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

A 12. fejezet lepesei szerint: (1) definiald az eszkozoket, (2) ird meg a rendszer-promptot, (3) allitsd be a memoria-kezelest, (4) futtasd az agens-hurkot, (5) ellenorizd az eredmenyt.

### 18.9.4 Multi-agens rendszerek a vizgyujto-modellezesben

A 11. fejezet targyalta a multi-agens rendszereket, ahol tobb agens dolgozik egyutt. A vizgyujtö-modellezesben ez igy nez ki:

- **Adat-agens:** letolti es elokesziti a bemeneti adatokat
- **Kalibracios agens:** kalibralja a modellt
- **Validaciaos agens:** fuggetlenul ellenorzi az eredmenyt a validacios idoszakon
- **Jelentes-agens:** osszefooglalo dokuumentumot ir az eredmenyekrol

A negy agens parhuzamosan es szekvencialisan dolgozik (az adat-agens kesziti elo a bemeneteket, a kalibracios agens dolgozik rajta, a validacios agens ellenorzi, a jelentes-agens dokumentaalja). Ez a munkamegosztas tukrozi a 11. fejezetben targyalt "speciaalizalt agensek csapata" architektuurat.

---

## 18.10 Magyar vizttudomanyi kontextus

### 18.10.1 Magyarorszag egyedi hidrologiai helyzete

Magyarorszag vizugyi szemponttbol kulönleges helyzettben van:

- **Alvizi fekvés:** A felszini vizek 95%-a a hatarokon tulrol erkezik. A Duna vizgyujtoje 19 orszagra terjed ki, a Tiszáé 5-re.
- **Lapos terepp:** Az Alfold a Karpat-medence legalacsonyabb pontjaan fekszik. A Tisza esese Szolnoktool Szegeedikig minddossze 0,00005 m/m.
- **Kettoos veszelyeztettettseg:** Arviz es aszaly egyidejuleg fenyeget -- a Tisza hullámtereben arvizi vedekezes zajlik, mikozben az Alfold belesejeeben aszaly uralkodik.
- **Töltesrendszer:** Toöbb mint 4200 km elsödleges arvizveedelmi töoltes -- Europa egyik legsürübb rendszere.
- **Talajvizfuggöseg:** Az Alfold telepuleseinek jelentős resze a sekely talajvizbol nyeri az ivovizet.

### 18.10.2 A Tisza: Europá egyik legkomplexebb folyorendszere

A Tisza vizgyujtoje (157 186 km2) Ukrajna, Romania, Szlovakia, Magyarorszag es Szerbia teruletere terjed ki. Az archullamok a karpati forrasvidekrol erkeznek, es a lapos magyar szakaszon lassan, de annál pusztitobban vonulnak vegig.

AI-alkalmazasi lehetosegek a Tiszan:

| Alkalmazas | AI-technika | Hivatkozott fejezet |
|------------|-------------|---------------------|
| Arvizielorejelzes Szolnoknal | LSTM + fizikai korlatok | 6. fejezet (modellezes) |
| Hullámtér-elontesi terkep | DEM-feldolgozas + HAND | 5. fejezet (kodgeneeralas) |
| Hataron atnnyulo adatcseere | Pipeline EFAS/GloFAS-hoz | 7. fejezet (pipeline) |
| Vizgyujto-gazdalkodasi terv | RAG a VGT3-hoz | 9. fejezet (RAG) |
| Operativ elojelzesi rendszser | Digitalis iker | 10. fejezet (digitalis iker) |
| Modell-kalibracio | Agens AI | 11--12. fejezet (agensek) |

### 18.10.3 A Duna es Budapest

Budapest ivoviz-ellatásának mintegy felet parti szuresü kutak biztositjak a Duna menten. Ezek a rendszerek a felszini es felszin alatti vizmodellezes osszekapcsolasat igenylik -- pontosan az a feladat, amelyre a digitalis iker (18.8. szakasz) alkalmas.

A 2013-as dunai árviz Budapestneel 891 cm-es tetöszintet produkalt. Az AI-tamogatott elojelzesi rendszer ezt az esemenyt a kovetkezokeppen kezeli:

1. **ECMWF ensemble-elojelzes** feldolgozasa pipeline-nal (7. fejezet)
2. **LSTM-elojelzes** a Duna budapesti szelvenere, 72 oras horizonttal
3. **HAND-szamitas** (terepfeldolgozas, 5. fejezet) az elontesi zonakra
4. **RAG-lekerdezees** a katasztrofaveedelmi protokollokrol (9. fejezet)
5. **Agens** az elorejelezes es a töltés-terhelees összevetesere (11. fejezet)

### 18.10.4 A Hortobagy es az Alfold talajvize

A Hortobagy -- UNESCO Vilagöoroksegi Helyszin -- a sekely talajviztol fugg, amely fenntartja szikes mocsarait es pusztait. A viztudomany szamara ket kulcskerdes:

1. **Hogyan hat az eghajlatvaltozas a talajvizutanpotlasra?** A 6. fejezet Boussinesq-modellje, AI-val parametereezve.
2. **Hogyan hat a mezogazdasagi kitermeles a vizes eloohelyekre?** MODFLOW-szimulacio, agens AI-val kalibraalva (18.9. szakasz).

A Debreceni Egyetem kornyezettudomaanyi kutatásainak kontextusa (amelyet a 6. fejezetben Kovacs Marta peldajan szemleltettunk) pontosan ez: a Hortobagy vizhaztartasat vizsgaalni az AI eszkozoeivel.

### 18.10.5 Vizugyi intezmenyek es adatforrások

| Intezmeny | Adatforrás | AI-alkalmazas |
|-----------|------------|---------------|
| OVF (Orszagos Vizugyi Foigazgatosag) | hydroinfo.hu valós ideju vizszint | Pipeline, LSTM |
| OMSZ (Orszagos Meteorologiai Szolgalat) | Csapadek, hopmerseklet | Pipeline, ERA5 validáció |
| Vizgyujto-gazdalkodasi igazgatosagok | VGT, monitoring adatok | RAG, agens |
| Copernicus (EU) | DEM, talajnedvesseg, muholdkep | Terepanalizis, taverzekeles |
| ECMWF | ERA5, idojaras-elojelzes | Modell-bemenet |

---

## 18.11 Gyakorlati feladatok

### 18.11.1 Feladat: Vizszint-monitoring pipeline

**Cel:** Epits egy automatzalt pipeline-t, amely letolti es feldolgozza a Tisza harom allomasanak (Tokaj, Szolnok, Szeged) vizszintadatait.

**Lepesek:**

1. Hasznald a 7. fejezet pipeline-architekturaaját.
2. Kerd meg az AI-t (Claude, ChatGPT vagy Copilot), hogy generaljon egy Python-szkriptet, amely:
   - Letolti az elmult 30 nap adatait az OVF API-jarol (vagy szimulalt adatokbol, ha az API nem elerheto)
   - Kitolti az adathianyokat linearis interpolacioval
   - Kiszamolja a napi min/max/atlag vizszintet
   - Idosor-grafikon abrázolja a harom allomast egyetlen abran
   - Pirossal jeloli a I. foku keszultsegi szintet meghalado napokat
3. Teszteld a szkriptet, es kerd meg az AI-t, hogy javitsa a talalt hibakat.
4. Bövitsd: adj hozza e-mail riasztast, ha a keszultsegi szintet tullepik.

**Kapcsolodas korabbi fejezetekhez:** 5. fejezet (kodgeneralas), 7. fejezet (pipeline).

---

### 18.11.2 Feladat: Vizgyujto-lehatarolas AI-val

**Cel:** AI-asszisztens segitsegevel hatarolj le egy vizgyujtot DEM-bol.

**Lepesek:**

1. Tolts le egy DEM-szelvényt a Copernicus GLO-30 adatbazisból a Zagyva vizgyujtojere (kb. 47.5°N, 19.8°E).
2. Kerd meg az AI-t, hogy generáljon egy WhiteboxTools-alapu Python-szkriptet a vizgyujto lehatarolarasahoz (Fill -> FlowDirection -> FlowAccumulation -> SnapPourPoint -> Watershed).
3. Futtasd a szkriptet.
4. Ha az eredmenybeli vizgyujto nem felel meg a varakozasaidnak, kerd meg az AI-t, hogy diagnosztizalja a problemat (lásd 18.3.2. szakasz).
5. Iteralj, amig helyes eredmenyt kapsz.

**Kapcsolodas korabbi fejezetekhez:** 5. fejezet (kodgeneralas).

---

### 18.11.3 Feladat: LSTM vizszint-elojelzes

**Cel:** Epits egy egyszeru LSTM modellt, amely a Tisza szolnoki vizszintjet jelzi elore.

**Lepesek:**

1. Kerd meg az AI-t, hogy generáljon szintetikus tanito-adatokat (ha valos adatod nincs): 10 ev napi vizszint + csapadek idosor, szinuszos szezonalitassal es veletlensszeru arvizi esemenyekkel.
2. Kerd meg az AI-t, hogy epitsen egy LSTM modellt PyTorch-ban vagy TensorFlow-ban:
   - 30 napos visszatekintesi ablak
   - 1 LSTM-reteg, 64 rejtett egyseg
   - 1 napos elojelzes
3. Tanitsd be a modellt (70% tanitas, 15% validalas, 15% teszt).
4. Abrazold a megfigyelt es elojelzett vizszintet a teszthalmazon.
5. Szamold ki az NSE-t es az RMSE-t.
6. Kerd meg az AI-t: "Hogyan javithatnam a modellt?" -- es kovessed a jaavaslatait.

**Kapcsolodas korabbi fejezetekhez:** 6. fejezet (modellezes).

---

### 18.11.4 Feladat: RAG chatbot vizugyi jogszabalyokhoz

**Cel:** Epits egy egyszeru RAG-rendszert a Viz Keretiranyelv szovegere.

**Lepesek:**

1. Tolts le a Viz Keretiranyelv magyar forditasat (PDF).
2. A 9. fejezet utmutatasa szerint:
   - Bontsd chunk-okra (500 token)
   - Szamits embedding-vektorokat
   - Töltsd ChromaDB-be
3. Kerd meg az AI-t, hogy generalja a RAG-lekerdezesi kodot.
4. Tesztelj harom vizugyi kérdest:
   - "Mi a jó okologiai allapot definicioja?"
   - "Milyen kivetelek leteznek a 4. cikkely ala?"
   - "Hogyan kell figyelembe venni a klimavaltozast a vizgyujto-gazdalkodasi tervben?"
5. Ellenorizd, hogy a RAG a helyes chunk-okat kereste-e vissza.

**Kapcsolodas korabbi fejezetekhez:** 9. fejezet (RAG).

---

### 18.11.5 Feladat: Hidrologiai kalibracios agens

**Cel:** Epits egy egyszeru agens-hurkat, amely egy csapadek-lefolyas modellt kalibral.

**Lepesek:**

1. Hasznalj egy egyszeru keettaroazoos modellt (ket tartaly sorozatkapcsolasban): az elso a talajnedvesseget repreezentalja, a masodik a felszini lefolyast. Ket parameter: talajkapacitas (mm) es lefolyasi tenyezo.
2. Generaltass szintetikus "megfigyelt" adatokat ismert parameterekkel (pl. talajkapacitas=200 mm, lefolyasi tenyezo=0,3).
3. A 12. fejezet keretrendszere szerint epits egy agensuurkot:
   - Az agens valaszt kezdeti parametereket
   - Futtatja a modellt
   - Kiszamolja az NSE-t
   - Diagnosztizalja a hibakat (vizualis elemzes az LLM-mel)
   - Modositja a parametereket
   - Ismetli, amig NSE > 0,8
4. Naplozd az agens minden gondolkodasi lepeset es parametervaaltoztatasat.
5. Hasonlitsd ossze: hany iteraciora volt szukseg az agensnek vs. egy egyszerú veletlenszeru keresnek?

**Kapcsolodas korabbi fejezetekhez:** 11. fejezet (agensek), 12. fejezet (agensek epitese), 6. fejezet (modellezes).

---

## Osszefoglalas

Ebben a fejezetben a koonyv teljes eszkozaarat a viztudomanyra alkalmaztuk:

| Fejezet | AI-technika | Vizugyi alkalmazas |
|---------|-------------|---------------------|
| 5. fejezet | Kodolasi asszisztensek | DEM-feldolgozas, vizgyujto-lehatarolas |
| 6. fejezet | Matematikai modellezes | Saint-Venant, Boussinesq, Richards -> kod |
| 7. fejezet | Adat-pipeline-ok | Vizszint-monitoring, szenzor-adatfeldolgozas |
| 9. fejezet | RAG | Viz Keretiranyelv chatbot, vizugyi jog |
| 10. fejezet | Digitalis ikrek | Vizgyujto-szintu szimulacio valos ideju adattal |
| 11. fejezet | AI agensek | Autonom kalibracio, diagnosztikus gondolkodas |
| 12. fejezet | Agensek epitese | Hidrologiai modellezo agens implementalasa |

A viztudomany az egyik legizgalmasabb alkalmazasi teruleteee az agentikus AI-nak, mert a feladatok termeszete -- iterativ, adatigényes, terbeli-idöbeli, fizikai törvényekkel korlátozott -- pontosan megfelel annak, amiben az AI kiváló. A Tisza archullamai nem varnak: az AI segit, hogy te sem kelljen.

---

> **Kulcsuuzenet:** Az AI nem helyettesiti a hidrologust -- hanem lehetove teszi, hogy a hidrologus arra osszpontositson, amiben az ember egyedulaaalloan jo: a fizikai megértes, a kreatív problemamegoldas es a dönteshozas. Az adatgyujtes, a kodolas, a kalibraalas es a dokumentalas egyre inkabb az AI dolga.
