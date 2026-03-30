# 19. fejezet — AI a térinformatikában

> **Fejezet-információ**
> - **Kinek szól:** Terinformatikusoknak, környezetkutatóknak és GIS-felhasználóknak
> - **Előismeretek:** 1-4. fejezet (AI alapok); a 5. és 9. fejezet ajánlott
> - **Amit megtanulsz:**
>   - AI-alapú műholdkép-feldolgozás és felszínborítás-osztályozás
>   - Autonóm GIS rendszerek: természetes nyelvű térinformatikai elemzés
>   - Magyar térinformatikai kontextus (EOV, Corine, Natura 2000)
> - **Szükséges eszközök:** Böngésző + terminál + Python (QGIS + Google Earth Engine)
> - **Kapcsolódó fejezetek:** 5. fejezet (kódolás), 10. fejezet (digitális ikrek), 17. fejezet (mezőgazdaság), 18. fejezet (hidroinformatika)

---

## 19.1 Nyitó jelenet: Amikor a térkép "megtanul" gondolkodni

Képzeld el a következő helyzetet. Szabó Anna környezetinformatikus vagy a Debreceni Egyetemen. A feladatod: felmérni, hogyan változtak a Tisza ártéri élőhelyek az elmúlt öt évben, milyen felszínborítási változások történtek a Natura 2000 területek környékén, és hogy a városias beruházások veszélyeztetik-e a védett zonak pufferzónáját. Ehhez szükséged van Sentinel-2 műholdfelvételekre, Corine Land Cover adatokra, Natura 2000 poligonokra, Magyar EOV koordináta-rendszerben levo parcellahatárokra és hidrográfiai adatokra. Ráadásul az eredmenyeket ossze kell vetned a vonatkozo jogszabalyokkal, és egy szakmai riportban kell osszefoglalnod.

Harom evvel ezelott ez a feladat harom honapnyi munka lett volna: adatok letöltése különböző portalokrol, koordináta-rendszer harmonizacio, raszteres és vektoros adatok osszemetszese QGIS-ben, vizualis interpretacio, statisztikai összesítés Excelben, vegul a riport megírása. Ma -- 2026-ban -- a munkafolyamat gyökeresen mas. Leírod a feladatot természetes nyelven egy AI ágensnek, amely automatikusan megkeresi a releváns műholdfelveteleket a STAC katalógusból, letolti és előfeldolgozza a rasztereket, elvegzi a felszínborítás-osztályozást egy foundation modellel, kiszámítja a zonális statisztikat a Natura 2000 poligonokra, osszeveti az eredmenyeket a jogszabályi adatbázissal (RAG), és generál egy térképes riportot -- mindezt egyetlen dél alatti munkaval.

Ez nem science fiction. Ez az **AI-alapú térinformatika** világa, és ebben a fejezetben végigvezetlek rajta: az adatfeldolgozástól a kódgeneráláson at az autonóm térinformatikai rendszerekig.

---

## 19.2 Hogyan alakitja at az AI a térinformatika minden szegmenset?

> **🖼️ 19.1. ábra: Az AI-GIS konvergencia négy hajtóereje — adatrobbanás, számítási kapacitás, AI-modellek, LLM-ek**
> *Four converging arrows diagram, each representing a driving force of AI-GIS convergence, meeting at a central "Autonomous GIS" hub, modern tech illustration*

A térinformatika -- vagy geoinformatika -- az a tudományterület, amely a foldi terben elhelyezkedo jelenségek digitális rögzítésével, modellezéseivel, elemzésevel és kommunikációjával foglalkozik. A modern térinformatika három oszlopon nyugszik: a **helyzeti komponens** (hol), az **attribútum komponens** (mi) és az **időbeli komponens** (mikor). Az AI mindhárom oszlopot forradalmasítja.

### 19.2.1 Az AI-GIS konvergencia hajtóerői

Négy párhuzamos trend találkozik napjainkban:

1. **Adatrobbanás**: A Copernicus-program Sentinel műholdjainak napi adattermelése meghaladja a 12 terabajtot. A Planet Labs napi rendszerességgel keszit 3--5 méteres felbontású felveteleket a Fold teljes felszínéről. Az IoT-hálózatok -- meteorológiai állomások, vízszintmerok, légszennyezettség-mérők -- szintén napi milliardnyi mérést generálnak. Ezt az adatmennyiséget emberi erővel mar lehetetlen feldolgozni.

2. **Szamitasi kapacitas**: A felhőalapú platformok (Google Earth Engine, Microsoft Planetary Computer, Copernicus Data Space Ecosystem) petabájtnyi adatot és gyakorlatilag korlátlan számítási kapacitast tesznek elérhetővé egy böngészőből. Az "adat a szamitashoz megy" paradigma átadta helyet a "szamitas az adathoz megy" elvnek.

3. **AI modellek érettsége**: A konvolúciós neurális hálózatok (CNN), a transzformer architektúrák és a geospatial foundation modellek (Prithvi, Clay, SatCLIP) elérték azt a szintet, ahol a műholdkép-osztályozás, a változásdetektálás és a térbeli predikció pontossága meghaladja az emberi vizuális interpretációét.

4. **Nagy nyelvi modellek (LLM)**: A GPT-4, Claude, Gemini és tarsaik képesek PostGIS SQL-t irni, Python GIS-szkripteket generálni, műholdkepeket értelmezni és komplex elemzési terveket kesziteni -- természetes nyelvű utasításból kiindulva.

Ezek a trendek együttesen hozzák létre azt, amit **autonóm GIS-nek** (Autonomous GIS) nevez a szakirodalom: olyan rendszert, amelyben az AI nem passziv eszkoze, hanem aktiv partnere a térinformatikusnak. Ebben a fejezetben végigjárjuk ezt a teljes spektrumot, és megállapítjuk, hogy a könyvünk korábbi fejezeteiből tanultak -- az AI ágensektől (11. fejezet) a RAG rendszerekig (9. fejezet), a kódolási asszisztensektől (5. fejezet) a digitális ikrekig (10. fejezet) -- hogyan alkalmazhatóek a térinformatikában.

### 19.2.2 A fejezet térképe

A fejezet felépítése a következő logikát követi:

| Alfejezet | Tema | Kapcsolodas a konyvhoz |
|-----------|------|----------------------|
| 19.2 | AI a térbeli adatfeldolgozásban | 4--5. fejezet (adatelemzés, kódolás) |
| 19.3 | AI kódolási asszisztensek GIS-hez | 5. fejezet (kódolási asszisztensek) |
| 19.4 | Gepi tanulas térbeli predikcióhoz | 6. fejezet (matematikai modellezés) |
| 19.5 | Vizualis programozas GIS munkafolyamatokhoz | 8. fejezet (vizuális programozás) |
| 19.6 | RAG térinformatikai tudashoz | 9. fejezet (RAG) |
| 19.7 | 3D GIS és térbeli digitális ikrek | 10. fejezet (digitális ikrek) |
| 19.8 | Autonóm GIS | 11--12. fejezet (ágensek) |
| 19.9 | Big data és felhőalapú GIS | 14. fejezet (AI labor) |
| 19.10 | Magyar térinformatikai kontextus | -- |
| 19.11 | Gyakorlati feladatok | -- |

---

## 19.3 AI a térbeli adatfeldolgozásban

> **🖼️ 19.2. ábra: Műholdkép-feldolgozási lánc AI-val — a nyers felvételtől a kész térképig**
> *Processing chain showing satellite image transformation: raw image → atmospheric correction → cloud masking → classification → thematic map, with AI icons at key steps*

A térinformatika legidőigényesebb, leginkabb "munka-jellegű" feladatai az adatfeldolgozáshoz kötődnek: műholdkepek előfeldolgozása, LiDAR pontfelhők osztályozása, vektoros adatok tisztítása, koordináta-transzformációk. Ezek pontosan azok a feladatok, ahol az AI -- akár kep-alapu mélytanulásként, akár kódgeneráló LLM-kent -- a legnagyobb hatást fejti ki.

### 19.3.1 Muholdkep-feldolgozás AI-val

A hagyományos műholdkép-feldolgozási lanc a következő lépésekből áll: (1) letöltés, (2) légköri korrekció (atmoszférikus korrekció: a nyers reflektancia átalakítása felszíni reflektanciává), (3) geometriai korrekció, (4) felhőmaszkolás, (5) mozaikolás és (6) kompozitkészítés. Ezeknek a lépéseknek a többsége ma mar automatizált: a Sentinel-2 Level-2A (L2A) termek mar legkorilag korrigált és geometriailag pontos felszini reflektanciat tartalmaz.

Az AI ezen felul három ponton lep be:

**Felhodetektalas és felhőmaszkolás**: A hagyományos küszöbérték-alapú felhodetektalas (mint a Sentinel-2 SCL savja) gyakran hibázik: a havat felhőnek, a magas albedójú varosi felületeket felhönek, a vékony cirrus-felhőt pedig átlátszónak osztályozza. A CNN-alapú felhodetektalas -- például az S2Cloudless (Sentinel Hub) -- 95%+ pontossaggal osztályozza a felhőpixeleket, és a Sentinel Hub platformon automatikusan alkalmazódik.

**Muholdfelvetelek szuperfelbontás-javítása** (super-resolution): AI modellek kepesek a 20 méteres felbontású Sentinel-2 savokat 10 méteres felbontásra javítani, vagy akár 2,5 méteres "szintetikus" felbontást generálni. Ez nem varázslat -- a modell a 10 méteres sávokból és a 20 méteres savok kozotti összefüggésekből tanulja meg a felbontás-javítást. A környezeti alkalmazásokban ez akkor hasznos, ha a 10 méteres felbontás nem elegendő (például varosi zoldfelületek részletes térképezese), de kereskedelmi nagyfelbontású felvetelek nem elérhetőek.

**Idősor-kompozitok intelligens előállítása**: A hagyományos medián-kompozit az egyes pixelek egész éves felvételeinek mediánjából számolódik. Az AI-alapú megközelítés -- például a Temporal Attention Encoder -- a felhős időpontokat automatikusan alacsony súllyal kezeli, és a "legjobb pixelt" választja a vizuális minőség és a tematikus pontosság alapján.

> **Kapcsolodas a 4. fejezethez**: Ahogyan a 4. fejezetben (Adatelemzés kod nélkül) láttad, az AI-val vegzett adattisztítás és -előfeldolgozás döntően csökkenti a rutinmunka mennyiségét. A térinformatikában ez megsokszorozódik: egyetlen Sentinel-2 jelenet 13 sávból, 109 millio pixelből áll, és egy országnyi elemzéshez évente több száz jelenet feldolgozása szükséges.

### 19.3.2 LiDAR pontfelhö-feldolgozás

A léjzeres letapogatás (LiDAR) sűrű háromdimenziós pontfelhőket allit elo, amelyekbol digitalis domborzatmodellek (DTM), digitalis felszínmodellek (DSM) és háromdimenziós épületmodellek származtathatóak. A nyers pontfelhö feldolgozásának legidőigényesebb lépése az **osztályozás**: minden pontrol eldönteni, hogy talajpont, vegetáció, épület, vezeték vagy egyéb objektum.

A hagyomanyo szűrőalgoritmusok (progresszív morfológiai szűrős, csúcshelyesítés) jol működnek sík terepen, de meredek domboldalon, sűrű városias környezetben vagy összetett vegetáció mellett gyakran hibáznak. A **deep learning-alapú pontfelhö-osztályozás** -- például a PointNet++ vagy a RandLA-Net -- közvetlenül a 3D pontokon dolgozik, és automatikusan tanulja meg a természetes és épített környezet térbeli mintázatait.

A magyar LIDAR500 program -- amely az egész ország légi felvételes LiDAR-felmérését célozza -- tobb tiz terabájtnyi pontfelhőt eredményez. Ennek a hatalmas adattömegnek a feldolgozása AI nélkül éveket venne igénybe; a mélytanulási modellekkel a munka hónapokra csökkenthető.

### 19.3.3 Vektoros adatok és koordináta-transzformációk

A vektoros adatok -- pontok, vonalak, poligonok -- tisztítása és harmonizálása szintén időigényes feladat. A tipikus problémák: önmetsző poligonok (topológiai hibák), eltérő koordináta-rendszerek (az EOV-ban levo kataszteri adatok és a WGS 84-ben levo GPS-mérések összevetése), hiányos attribútumok és eltérő osztályozási sémák.

Az AI itt elsősorban **kódgenerálóként** segit: a feladat leírásából automatikusan generál GeoPandas- vagy PostGIS-kodot a koordináta-transzformációhoz, a topológiai javításhoz és az attribútum-harmonizációhoz. Errol részletesen a 19.3 alfejezetben lesz szó.

> **Az EOV koordináta-rendszer felismerése**: A magyar geoinformatikaban az EOV (Egységes Országos Vetületi rendszer, EPSG:23700) a leggyakoribb vetületi rendszer. Az EOV koordináták felismerése **érték-tartomány** alapján lehetséges: a Northing értékek 0 és 400 000 kozott, az Easting értékek 400 000 és 1 000 000 kozott mozognak. Fontos: a fejléc-címkék gyakran félrevezetőek (a "X" mezo tartalmazhatja a Northingot vagy az Eastinget is) -- mindig az értéktartomány az irányadó.

---

## 19.4 AI kódolási asszisztensek GIS-hez

Az 5. fejezetben megtanultad, hogyan használhatod az AI kódolási asszisztenseket (Claude, ChatGPT, GitHub Copilot, Cursor) Python-szkriptek írásához -- programozási tapasztalat nélkül is. A térinformatikában ez a képesség különösenn hatalmas, mert a GIS-munka nagy resze automatizálható Python-nel, de a GIS-Python okoszisztema (ArcPy, QGIS Processing, GeoPandas, rasterio, xarray) rendkívül szerteágazó és összetett.

### 19.4.1 Python GIS-szkriptek generálása

Az LLM-ek a GIS-Python ökoszisztémát jol ismerik, mert a tanító szövegekben bőven található GeoPandas, rasterio és PostGIS dokumentáció. A tipikus felhasználási mintak:

**Vektoros muveletek GeoPandas-szal:**

```
Prompt: "Ird meg Python-ban, hogyan olvassak be egy GeoPackage
fajlt GeoPandas-szal, szurjem a 'települes' oszlop alapjan
Debrecenre, keszitsek 500 meteres puffert, es mentsem el uj
GeoPackage-kent EOV vetuleetben (EPSG:23700)."
```

Az AI által generált kod tipikusan:

```python
import geopandas as gpd

# Beolvasas
gdf = gpd.read_file("telepulesek.gpkg")

# Szures
debrecen = gdf[gdf["telepules"] == "Debrecen"]

# Vetuleti transzformacio EOV-ba (EPSG:23700) -- a puffer
# metrikus, ezert metrikus vetuletben kell szamolni
debrecen_eov = debrecen.to_crs(epsg=23700)

# Puffer (500 meter)
puffer = debrecen_eov.copy()
puffer["geometry"] = debrecen_eov.geometry.buffer(500)

# Mentes
puffer.to_file("debrecen_puffer_500m.gpkg", driver="GPKG")
```

**Raszteres szamitasok rasterio-val:**

```
Prompt: "Szamitsd ki az NDVI-t ket Sentinel-2 savbol (B04 es B08),
maszkold ki a felhot az SCL sav alapjan, es mentsd el Cloud
Optimized GeoTIFF formaaatumban."
```

```python
import rasterio
import numpy as np

with rasterio.open("B04.tif") as red_src, \
     rasterio.open("B08.tif") as nir_src, \
     rasterio.open("SCL.tif") as scl_src:

    red = red_src.read(1).astype(float)
    nir = nir_src.read(1).astype(float)
    scl = scl_src.read(1)

    # Felhomaszkolas: SCL 8 es 9 = felho
    mask = np.isin(scl, [8, 9])

    # NDVI szamitas
    ndvi = np.where(
        (nir + red) > 0,
        (nir - red) / (nir + red),
        np.nan
    )
    ndvi[mask] = np.nan

    # Mentes COG-kent
    profile = red_src.profile.copy()
    profile.update(dtype="float32", driver="GTiff",
                   compress="deflate", tiled=True,
                   blockxsize=512, blockysize=512)

    with rasterio.open("ndvi_cog.tif", "w", **profile) as dst:
        dst.write(ndvi.astype(np.float32), 1)
```

### 19.4.2 ArcPy és QGIS Processing

Ha ArcGIS Pro környezetben dolgozol, az ArcPy az automatizalas eszkoze. Az LLM-ek az ArcPy-t is ismerik:

```
Prompt: "ArcPy-val futtasd le a Spatial Join muveleteet
az 'epuletek' es a 'arvizkockazat' retegek kozott, es
szamold ki, hany epulet esik magas kockazatu teruuletre."
```

QGIS Processing eseteen a `processing.run()` fuggvenyhivasok generálasa szintén jol mukodik:

```
Prompt: "QGIS Processing-gel keszits domborzat-arnyekolast
(hillshade) a Copernicus DEM GeoTIFF-bol, 315 fokos
megvilagitasi szog es 45 fokos magassagi szog mellett."
```

```python
import processing

processing.run("native:hillshade", {
    'INPUT': '/path/to/copernicus_dem.tif',
    'Z_FACTOR': 1,
    'AZIMUTH': 315,
    'V_ANGLE': 45,
    'OUTPUT': '/path/to/hillshade.tif'
})
```

### 19.4.3 PostGIS térbeli lekerdezesek

Az AI kódolási asszisztensek a PostGIS térbeli SQL-t is megbiizhatoan generáljak. Ez különösen ertekes, mert a PostGIS fuggvenykonyvtar rendkívül kiterjedt (több száz térbeli fuggveny), és a helyes használat mellyrehatö térbeli gondolkodast igenyel.

```
Prompt: "Ird meg PostGIS SQL-ben: hany hektar szantoterulet
(CLC kodok 211, 212, 213) van Hajdu-Bihar megyyeben?
A retegek EOV-ban vannak."
```

```sql
SELECT SUM(ST_Area(ST_Intersection(f.geom, m.geom))) / 10000
    AS hektar
FROM felszinboritas f
JOIN megyek m ON ST_Intersects(f.geom, m.geom)
WHERE m.nev = 'Hajdu-Bihar'
  AND f.clc_kod IN ('211', '212', '213');
```

> **Tipikus hibaforrasok**: Az LLM-ek a GIS-kodgeneeralasnaal a következő hibakat követik el leggyakrabban: (1) **CRS-hiba** -- EOV helyett WGS 84-et felteteleznek, mert az a leggyakoribb a tanitoszovegekben (az esetek 25--35%-aban); (2) **szemantikai hiba** -- rossz oszlopnevet vagy osztalykodot használnak; (3) **topológiai hiba** -- nem kezelik az önmetsző poligonokat (ST_MakeValid hianya). A 12. fejezetben tanult validaacios lépések (onselfcheck, iteratív javitas) itt különösenn fontosak.

---

## 19.5 Gepi tanulas térbeli predikcióhoz

A 6. fejezetben (Matematikai modellezés) megismerkedsz a gepi tanulas alapjaival. A térinformatikában a gepi tanulas harom fo feladattipusban jelenik meg: felszínborítás-osztályozás, geostatisztikai modellezés és térbeli interpoláció.

### 19.5.1 Felszinboritas-osztályozás

A felszínborítás-osztályozás a távérzékelés "Hello World" feladata: műholdfelvetelbol automatikusan meghataarozni, hogy a Fold felszinenn hol van erdoo, mezőgazdasági terület, vizfelület, epitett terület stb. Az elmult evtizedek fejlődése:

| Korszak | Modszer | Tipikus pontossag | Jellemzo |
|---------|---------|-------------------|----------|
| 1970--1990 | Maximum Likelihood | 70--80% | Normalis eloszlas feltevezes |
| 2000--2015 | Random Forest | 80--90% | Nem feltetelaz eloszlast, sok jellemző |
| 2015--2020 | U-Net (CNN) | 85--95% | Automatikus jellemzőetanulas |
| 2020-- | Foundation modellek (Prithvi, Clay) | 90--97% | Elotanitott, keves cimkezeiett adat kell |

A **U-Net** architektura -- amelyet a 6. fejezetben az encoder-decoder halozatok kozott emlitettunk -- a térbeli szegmentalas (szemantikus szegmentalas) alapeszkoze: minden pixelt osztalyhoz rendel, figyelembe veve a térbeli kontextust. A U-Net kulcsinnovacioja az atugrasi kapcsolat (skip connection), amely a részletes térbeli információt kozvetiti az alacsony szintű retegekbol a magas szintű retegekbe.

A legujabb fejlemeny a **geospatial foundation modellek**: a Prithvi (NASA/IBM, 2023) és a Clay (Radiant Earth, 2024) hatalmas mennyisegu cimkezetlen műholdkepen elotanitott modellek, amelyeket keves cimkezett mintaval finomhangolhatunk specifikus feladatokra. Ez a transfer learning paradigma -- amelyet a 6. fejezetben taargyaltunk -- a távérzékelésben különösen hatekony, mert a cimkezett tanitoadat eloallitaasa rendkívül draaga és iodoigenyes.

### 19.5.2 Geostatisztikai modellezés és térbeli interpoláció

A geostatisztika a terben mintazott adatok statisztikai elemzésenek és az optimalis térbeli interpolációnak a módszertana. Az alapelv Tobler első foldrajzi torvenye: *"Minden mindennel osszefugg, de a kozelebbi dolgok jobban osszefuggenek, mint a távoliak."*

A klasszikus geostatisztikai munkafolyamat:

1. **Variogram-szamitas**: Megvizsgaaljuk, hogyan no az erttekkülonbsegek varianciaja a mintapontok kozotti tavolsag fuggvenyeben
2. **Variogram-modell illesztese**: Szferikus, exponencialis vagy Gauss-modellt illesztunk
3. **Kriging**: Az illesztett variogram alapján optimalis, minimalis varianciaju linearis becslest vegzunk a mintapontoek kozotti területekre

A variogram harom kulcsparamétere:
- **Roghatas (nugget)**: A mikro-skaläju valtozekonysag és a mérési hiba
- **Teto (sill)**: A teljes variancia
- **Hatotavossag (range)**: Az a tavolsag, amelyen belül a pontok teerben korrelältak

Az **AI belepesi pontja** a geostatisztikaba tobbfele:

**Automatikus variogram-illesztes**: Az LLM-ek kepesek Python-kodot generálni a variogram szamitasahoz és illesztsehez (a `scikit-gstat` vagy `pykrige` konyvtarakkal), beleertve a modellszelekcios és a cross-validációs leepeseket is.

**Hibrid modellek**: A Random Forest Kriging (RFK) és a Gradient Boosting + Kriging hibrid módszerek a nem-térbeli prediktorok (domborzat, talaj, klimaado) és a térbeli autokorrelacioo előnyeit egyszerre hasznossitjak. Peldaul a Duna-Tisza kozi talajvízszint predikciójahoz: a Random Forest a domborzatbol, a meteorológiai adatokbol és a talaj tipus obol becsuli a talajvízszintet, majd a kriging a reziduumok (maradekok) térbeli korrelaciojat modelleezi.

**Deep learning-alapu térbeli interpoláció**: A graf neurális hálózatok (GNN) a mintaveli pontokat grafkent kezelik, és a message passing mechanizmussal a szomszedos pontok információjat integraljaak. Ez különösen hatekony szbalytalan mintaveteeli elrendezeseknel, ahol a klasszikus kriging kuszobértékekre és lag-beállításokra erzekeny.

### 19.5.3 Peldaa: Talajvízszint-becslees a Duna-Tisza kozen

Vegyuk a Duna-Tisza kozi homokhaatsag talajvízszint-becsleset -- egy klasszikus magyar geoinformatikai pelda. A monitoring kutak szama nehany szaz, de a terület tobb ezer negyzetkilometerss. A feladat: megbizhato térképet kesziteni a kutak kozotti területekre.

**Hagyomanyos megközelítés**: Ordinary kriging a kutadatokra. A hatotavolsag tipikusan 8--15 km, ami meghataarozza a monitoring-halozat szükséges sűrűseget.

**AI-támogatott megközelítés**:

1. A Random Forest prediktorai: Copernicus DEM domborzati valtozoi (lejtoszog, topografiai nedvessegindex), Sentinel-2-bol szarmaztatott vegetációs indexek (az aktiv vegetáció a felszinkoozeli talajvíz jelenletere utal), talajtérkép, meteorológiai adatok
2. Az RF predikciója a determinisztikus komponens
3. A kriging a reziduumokra: a maradek térbeli mintazat modellezeese
4. Eredmeny: 100 méteres felbontäsu talajvízszint-térkép, amely a hagyományos kriginggel szemben 15--25%-kal alacsonyabb becsleesi hibaval rendelkezik

> **Kapcsolodas a 6. fejezethez**: A hibrid modellezés logikaja megegyezik a 6. fejezetben tanult ensemble megközelítéssel: tobb modell kombinälasa jobb eredményt ad, mint barmelyik modell onmagaban.

---

## 19.6 Vizualis programozas GIS munkafolyamatokhoz

A 8. fejezetben (Vizualis programozas) megismerkedtel a KNIME-val és az n8n-nel -- ket vizualis munkafolyamat-szerkesztovel, amelyekkel kod nélkül epithetrol összetett adatfeldolgozási lancokat. A térinformatikában mindket eszkoz rendkívül hatekony.

### 19.6.1 KNIME térbeli adatelemzéshez

A KNIME Analytics Platform a Geospatial Analytics Extension reveln térbeli adatokat is kezel. A tipikus felhasználási mintak:

**Térbeli adatok beolvasasa és vizualizációja**: A KNIME GeoPackage, Shapefile, GeoJSON és CSV (koordinátakkal) formasatumokat olvas, és a beepitett Geospatial View nodeokkal interaktív térképeeket jelenjet meg.

**Geostatisztikai munkafolyamat KNIME-ban**:
1. *GeoFile Reader* node: monitoring kutadatok beolvasasa
2. *Row Filter*: időszaki szures (pl. 2025. oktober)
3. *Math Formula*: elooszamitasok
4. *Python Script* node: variogram szamitas és kriging a `pykrige` konyvtarral
5. *Geospatial View*: az eredmeny-térkép megjelenitese
6. *GeoFile Writer*: eredmeny mentese GeoPackage-kent

A KNIME előnye a GIS-munkaban, hogy a munkafolyamat **vizuaalaisan dokumentalt és reprodukalhato** -- a 8. fejezetben tanult előnyok itt kulonoesen fontosak, mert a térbeli elemzések reprodukálhatósága a tudományos kutatasban alapkoveteelmeny.

### 19.6.2 n8n automatizált térképkesziteshez

Az n8n -- a 8. fejezetben megismert automatizaaciios platform -- a térképkeszites automatizalasaara hasznalhato:

**Automatizalt havi NDVI-térkép munkafolyamat**:
1. *Schedule Trigger*: minden honap 5-en elindul
2. *HTTP Request* node: STAC API lekerdeses a Sentinel-2 felvetelekert (az elozo honap, felhoboritals < 20%)
3. *Code* node: NDVI szamitas Python-ban (rasterio)
4. *Code* node: térkép generálas Matplotlib-tel
5. *Email Send* node: a térkép elküldese a kutatócsoportnak
6. *Webhook* node: riasztas, ha az NDVI anomalisan alacsony (aszalyjel)

Ez a munkafolyamat egyszer letrehozva honaprol honapra automatikusan fut -- a kutatos emberi beavatkozas nélkül kap friss vegetációs terkeeppeket.

> **Kapcsolodas a 8. fejezethez**: A 8. fejezet részletesen bevezeti a KNIME és n8n hasznaalataat. Ha meg nem olvastad, érdemes visszalapozni -- az ott tanultak közvetlenül alkalmazhatóek a GIS munkafolyamatokra.

---

## 19.7 RAG térinformatikai tudashoz

A 9. fejezetben (RAG -- Tanitsuk meg az AI-t a sajaat adatainkra) megtanultad, hogyan epitsz Retrieval-Augmented Generation rendszert, amely a saját dokumentumaidbol keres ki relevanss információt, és az LLM ezek alapján valaszol. A térinformatikában a RAG harom kiemelt alkalmazási teruulettel rendelkezik.

### 19.7.1 Chatbot térbeli adatbázisok felett

Képzeld el, hogy egy PostGIS adatbaazisban több száz térbeli reteg van: felszínborítás, hidrografia, talaj, domborzat, koezigazgatasi hatarok, Natura 2000 teruuuletek, MePAR parcellak. A RAG-rendszer lehetővé teszi, hogy **természetes nyelven kerdezz** errol az adatbaaziisrol:

- "Mekkora terület szantoo Hajdu-Bihar megyében a Natura 2000 területekeen belül?"
- "Melyik települések vannak 5 km-en belül a Tisza arvizi nagyvizi medreetol?"
- "Hogyan valtoozott a Hortobagyi Nemzeti Park felszínborítása 2018 és 2024 kozott?"

A rendszer a kerdesbol PostGIS SQL-t generaal, vegrehajta az adatbaazison, és az eredményt szovegesen osszefoglalja. A **térbeli RAG** speciaalitaasa, hogy a relevancia nemcsak szoveges, hanem **terbeli** is: egy Balatonra vonatkozo kerdes a Balaton kornyeki dokumentumokat is relevansnak tekinti, meg ha a "Balaton" szo expliciten nem is szerepel bennuk.

A megvaalositas technikai vallaza:
- **pgvector + PostGIS** egyazon adatbázisban: a pgvector a szoveges embedding-eket, a PostGIS a geometriakat indexeli, és egyetlen SQL-lekerdezesben kombinalhato a szemantikus és a térbeli kereses
- **Few-shot learning**: nehany pelda-lekerdezez az LLM kontextusaban javitja a generált SQL minosseget
- **Self-correction**: ha a generált SQL hibat dob vagy ertelmetleg eredményt ad, a hibaüzenet visszaadodik az LLM-nek, amely javitott verziiot generaal

### 19.7.2 Metaadat-kataloguusok és az INSPIRE iranyelvv

Az EU INSPIRE iranyyelve (2007/2/EK) megkooveteli a tagallamoktol a térbeli adatok interoperabilis metaadatokkal valo ellaataasat és haaaloozati szolgaltatasokon (WMS, WFS, ATOM) keresztuli hozzaaferhetooseget. A gyakorlatban a metaadatok gyakran hiányosak vagy pontatlanok -- ez a "metaadat-hezag".

A RAG itt ket modon segit:
1. **Metaadat-generálas**: A multimodaalis LLM-ek (amelyekre a 2. fejezetben hivatkoztunk) kepesek egy térbeli adatreteg tartalmaat automatikusan leirni: a reteg temaja, a térbeli kiterjedese, az attribútumok jellege, a feltetelezett koordináta-rendszer
2. **INSPIRE-kompatibilis kereses**: A RAG rendszer az INSPIRE metaadat-kataloogus felett mukodoö chatbot-kent szolgal: a kutato természetes nyelven kerdez ("Van-e 10 méteres felbontásu feelszyinboritas-térkép Magyarországra 2024-bol?"), és a rendszer az INSPIRE Discovery Service-bol keresi ki a valaszt

### 19.7.3 Jogszabalyi tudasbaazis térbeli kontextusban

A környezetvedelmii hataasvizsgálatoknan és terület-rendezesi tervek készítésekor a térbeli elemzés és a jogi hatter osszekötese kritikus. Peldaul: "Milyen korlatozasok vonatkoznak egy tervezett naapelempark helyszinere, ha az egy Natura 2000 terület 500 méteres pufferzoonajaba esik?"

A **térbeli RAG** a következő lepeseket hajtja vegre:
1. A tervezett helyszin geometriajjanak betöltese
2. 500 méteres puffer generálasa
3. Metszees a Natura 2000 retteggel -- van-e atfedes?
4. Ha igen: a RAG komponens megkeresi a relevaaans jogszabalyokat (275/2004. Korm. rendelet, a területre vonatkozo kezelesi terv)
5. Az LLM osszefoglalja az eredményt: "A tervezett helyszin a Hortobaagyi Nemzeti Park (HUDI30001) 500 méteres pufferzoonajaba esik. A 275/2004. Korm. rendelet alapján..."

> **Kapcsolodas a 9. fejezethez**: Ez a pelda a 9. fejezet RAG architektúrájanak térbeli kitérjeszteese. A kulonbseg: a retriever nemcsak szoveges hasonlosag, hanem **térbeli kozelseg** alapján is keres.

---

## 19.8 3D GIS és térbeli digitális ikrek

A 10. fejezetben (Digitális ikrek) megtanultad, hogy a digitalis iker egy fizikai rendszer virtuallis, valoos ideju, ketiranyuu adataaramlas által szinkronizalt masaa. A térinformatikában ez a koncepció a **térbeli digitális ikerben** (spatial digital twin) öllt testet: egy varos, egy vízgyűjtő, egy erdoterület háromdimenziós, szenzor-szinkronizalt virtuallis modellje.

### 19.8.1 3D adatmodellek

A háromdimenziós térinformatika alapvetoen öt adatmodellel dolgozik:

| Modell | Leiras | Alkalmazas |
|--------|--------|------------|
| **Voxel** | 3D racs (a raszter 3D megfeleloje) | Geologia, szennyezes, meteorologia |
| **Mesh** | Haromszoghalos felszin | Vizualizacio, FEM szimuláció |
| **Oktafa** (octree) | Adaptiv 3D racs | Pontfelho-tarolas, LOD |
| **B-rep** | Hataarolo felszinek | CAD, BIM |
| **CSG** | Primitiv testek + Boole-muveletek | Parametrikus tervezes |

A **CityGML** (OGC szabvaany) a varosi 3D modellek szemaantikus adatmodellje, öt részletessegi szinttel (LOD):
- **LoD0**: Regionalis modell (2.5D felszin + 2D alapterület)
- **LoD1**: Tomb-modell (extrudalt alapterület, lapos teto)
- **LoD2**: Tetomodell (tetogeometria, fal/teto/talaj szemantika) -- a legtöbb varosi digitalis iker ezen a szintén mukodik
- **LoD3**: Architekturalis modell (homlokzati reszletek)
- **LoD4**: Belso terek (szobak, folyosok) -- BIM-GIS integráció

A **3D Tiles** (Cesium, OGC szabvaany) a nagy térbeli adathalmazok webes streamingjeenek formátuma, amelyet a CesiumJS és a Google Maps 3D Tiles API hasznaal.

### 19.8.2 Varosi digitális ikrek

A varosi digitalis iker egy varos háromdimenziós, szenzor-szinkronizalt modellje, amely a következő retegeket integralja:

- **Epuletgeometria**: LoD2 vagy LoD3 CityGML modell, LiDAR-bol vagy fotogrammetriabol szaarmaztatva
- **Szenzor-adatok**: meteorológiai állomások, legosiineneseg-merok, forgalomszaamlalook, energiafogyasztas -- valoos idejuu adataaramlaassal
- **Szimulaacioos modellek**: hosziget-szimuláció, zaj-terjedes, arvizi modell, energetikai modell
- **AI reteg**: anomalia-detektalas a szenzor-adatokon, prediktiv karbantartas az infrastruktúran, optimalizációos javaslatok

Példa: **Budapest hosziget-szimuláció**. A 3D épületmodellbol (LoD2), a felszínborítás-retegbol, a meteorológiai adatokbol és az utcaszinti homerseklet-meresekbol a digitalis iker szimulaalja a varosi hosziget hatasaat. Az AI reteg azonositja a legkritikusabb területeket (ahol a nyari éjszakai homerseklet 5+ fokkal meghaladja a kulvarosi erteket), és javaslatot tesz a beavatkoozasra: zoldfellueelet-fejlesztes, albedo-novelö tetofelületek, vizfelületek.

### 19.8.3 Infrastruktúra-monitoring

A digitális ikrek az infrastruktúra-monitoringban is kulcsszerepuek. Egy hid, egy gaatrendszer vagy egy csatornahalozat digitalis ikre a szerkezeti allapotot szenzor-adatokbol (gyorsulasmero, szintezo, homerseklet) valoos ideeben kooveti, és az AI prediktiv karbantarttaasi modellekkel jeleezi eloroe a beavatkozasi igenyt.

A **BIM-GIS integráció** a kulcs: az epitmeny BIM modellje (IFC formaatumban) a részletes szerkezeti adatokat, a GIS a kornyyezeti kontextust (domborzat, talaj, vizrajz, szeiszmikus kockazat) szolgaltatja. A ket modell osszekapesolaasa lehetővé teszi, hogy az infrastruktúra allapotaat a térbeli környezetteel egyutt vizsgaaljuk.

> **Kapcsolodas a 10. fejezethez**: A 10. fejezet általános ertelemben targyaalja a digitális ikreket. A térbeli digitális iker ezeknek egy specifikus, de rendkívül fontos alkalmazása, ahol a háromdimenziós geometria és a foldrajzi kontextus a meghataarozo.

---

## 19.9 Autonóm GIS: AI ágensek a térinformatikában

> **🖼️ 19.3. ábra: Autonóm GIS — természetes nyelvű utasítás térinformatikai elemzéssé alakítva**
> *Illustration showing a text prompt on the left transforming into a GIS map analysis on the right, with an AI agent in the middle orchestrating the process, futuristic hologram style*

A 11. fejezetben (Az AI ágensek megértése) és a 12. fejezetben (AI ágensek építése) megtanultad, mi az AI ágens, hogyan működik a ReAct ciklus, és hogyan epithetrol tobbagenses rendszereeket. Az **autonóm GIS** (Autonomous GIS) ezeknek az elveknek a térinformatikai alkalmazása -- és egyben a térinformatika legforradalmib fejlemenye.

### 19.9.1 Mi az autonóm GIS?

A térinformatika tortenete soran a felhasználó és a rendszer viszonya fokozatosan alakult at:

| Korszak | Paradigma | A felhasználó szerepe |
|---------|-----------|---------------------|
| 1960--1990 | Nagygeepes GIS | Programozo |
| 1990--2010 | Asztali GIS (ArcGIS, QGIS) | Szakerto felhasználó |
| 2010--2020 | Felhoalapu GIS (GEE) | Szkriptiiro |
| 2020--2025 | AI-támogatott GIS | Prompt-fogalmazo |
| 2025-- | **Autonóm GIS** | **Feladat-meghataarozo** |

Az autonóm GIS-ben a felhasználó **nem azt mondja, hogyan** (nyisd meg ezt a reteget, alkalmazz puffert, vegezz join-t), hanem **azt mondja, mit** akar (melyik települések vannak 500 meteren belül az arvizveeszelyes területektol?) -- és a rendszer maga tervezi meg és hajtja vegre az elemzést.

### 19.9.2 Az autonóm GIS szintjei

A jarmuipari autonóm vezetes analogiajaara epitvee ot szint kulonboztetheto meg:

| Szint | Megnevezes | Leiras | Pelda |
|-------|-----------|--------|-------|
| 0 | Nincs automatizalas | Minden muveletet kezzel vegez a felhasználó | Hagyomanyos asztali GIS |
| 1 | Asszisztens automatizaalas | Az AI egyszerűu muveleteket vegez utasitasra | Siri/Alexa szintű GIS-parancsok |
| 2 | Resszleges automatizaalas | Az AI tobb muveletet lancolva hajt vegre, emberi felügyeletteel | AI-kodgenerállas QGIS-ben |
| 3 | Felteteles automatizaalas | Az AI tervet keszit, a felhasználó jovahagyja, az AI vegrehajt | Plan-and-Execute ágens |
| 4 | Magas szintű automatizaalas | Az AI önállóan vegez összetett elemzéseket, emberi ellenoorzes az eredmenyen | ReAct ágens GIS eszközökkel |
| 5 | Teljes automatizaalas | Az AI önállóan tervez, vegrehajt, ellenoriiz, iteraal | Jovoobeli cél |

A 2026-os gyakorlatban a 2--3. szint a realis: az AI nagyon hateekonyan kodot generál és elemzési terveket keszit, de az eredmenyek **emberi validäciot igenyeelnek** -- különösen a CRS-kezeeles, a topológiai muhveletekk és a szemantikai ertelmeezes területen.

### 19.9.3 A ReAct ciklus a térinformatikában

A 11. fejezetben megismert ReAct (Reasoning + Acting) keretrendszer a térinformatikában a következőkeeppen mukodik. Vegyunk egy konkrét peldat:

**Felhasználói kerdes**: "Melyik Natura 2000 területeken nott a beepitettseg 2020 ota?"

**1. Gondolat** (Reasoning): "Szuuksegem van a Natura 2000 terurletek poligonjaira és ket idopontra vonatkozo felszínborítás-adatokra. A beepitettseg-noovekedeshez ki kell szamolnom a beepitett terület aranyat minden Natura 2000 poligonon belül 2020-ban és 2024-ben."

**2. Cselekves** (Acting): STAC API lekerdezes az ESA WorldCover 2020 és 2024 raszterekre, Natura 2000 reteg letöltése.

**3. Megfigyelees** (Observation): "A STAC API visszaadta a rasztereket. A Natura 2000 reteg letoltheto GeoPackage formaaatumban."

**4. Gondolat**: "Zonalis statisztikat kell szamolnom: a beepitett pixel-araany minden Natura 2000 poligonra, mindkeet evre. A retegeket kozos CRS-be kell hoznom."

**5. Cselekves**: Python-kod generálása (rasterio + GeoPandas + rasterstats), vegrehajtaas.

**6. Megfigyelees**: "Az eredmeny egy tablazat: beepitett_arany_2020 és beepitett_arany_2024 minden területre. 12 területen nott."

**7. Gondolat**: "Ellenoorzom: a beepitett arany ertekei 0 és 1 kozott vannak-e? A 12 terület szaama realis-e Magyarorszaag kb. 480 Natura 2000 területere? Igen, konzisztens."

**8. Cselekves**: Eredmeny prezentaalaasa: térkép + tablazat + szoveges összefoglaló.

### 19.9.4 Tobbagenses GIS-architektura

A 11. fejezetben tanult tobbagenses rendszerek a GIS-ben kulonoosen hatekonykak, mert a térbeli elemzés tobb markánsan eltérő szakkompetenciat igenyel:

- **Adat-keresoo agens**: Ismeri a STAC katalogusokat, WFS szolgaltatasokat, PostGIS adatbázisokat. Ha a felhasználó "erdooboritast" ker, o donti el: ESA WorldCover, Corine Land Cover vagy Sentinel-2-alapu egyedi osztályozás?
- **GIS-analizator agens**: SQL-t és Python-kodot ir, kezeli a CRS-t, a topologiat és a geometriai muveleteket
- **Kartografus agens**: Az eredmeny vizualizaciiojaert felel -- szinvalasztas, szimbolizacio, jelmagyarazat, terkeepleptek
- **Kritikus agens**: Az eredményt erttekeli: ellenoorzi a statisztikai konzisztenciat, a CRS-helyesseeget, a topológiai errvenyesseget

A négy ágens uzeneteeken keresztul kommunikaal, és iterálhat: ha a Kritikus ágens CRS-hibbat talal, visszakuldi a feladatot a GIS-analizator ágensnek.

> **Kapcsolodas a 11--12. fejezethez**: Az ágensek építésenek technikai reszletei a 12. fejezetben talalhaatok. Itt a GIS-specifikus eszkozvalasztast és az eszköztar kialakitasat emeljuk ki -- a térinformatikában tipikusan 15--30 eszkoz (STAC kereses, puffereeles, zonális statisztika, térképgenerálas stb.) az optimalis.

---

## 19.10 Big data és felhőalapú GIS AI-val

A 14. fejezetben (AI labor) megismerkedtel a felhőalapú számítási környezetekkel. A térinformatikában a felhőalapú platformok a petabajtos muuholdfelveetel-archivumok feldolgozásaahoz nelkülözhetetlenek.

### 19.10.1 Google Earth Engine (GEE)

A Google Earth Engine a térinformatika "nagy durrantasa" volt 2010-ben: petabájtnyi műholdfelvetelt és számítási kapacitast tett elérhetővé egyetlen boengeeszobol. A GEE Python API-val (a `ee` konyvtaaronn keresztul) planetaris lepteeku elemzéseket futtathatsz nehany sor koddal:

```python
import ee
ee.Initialize()

# Sentinel-2 gyujtemeny szurese Magyarorszagra, 2024
s2 = (ee.ImageCollection("COPERNICUS/S2_SR_HARMONIZED")
      .filterDate("2024-04-01", "2024-09-30")
      .filterBounds(ee.Geometry.Rectangle([16.1, 45.7, 22.9, 48.6]))
      .filter(ee.Filter.lt("CLOUDY_PIXEL_PERCENTAGE", 20)))

# NDVI median kompozit
ndvi = s2.map(lambda img: img.normalizedDifference(["B8", "B4"])
              .rename("NDVI")).median()

# Exportalas
task = ee.batch.Export.image.toDrive(
    image=ndvi, description="hungary_ndvi_2024",
    scale=10, region=ee.Geometry.Rectangle([16.1, 45.7, 22.9, 48.6]),
    maxPixels=1e13
)
task.start()
```

Az AI itt ket szintén segit:
1. **Kodgenerálas**: Az LLM a természetes nyelvu leiraasbol GEE Python-kodot generál
2. **Eredmennyertelmezees**: Az LLM az exportalt NDVI-terkeep statistikait elemzi és szovegesen osszefoglalja

### 19.10.2 Microsoft Planetary Computer és Copernicus Data Space

A **Planetary Computer** a nyilt STAC szabvanyra epit, és a felhonativ formatumokat (Cloud Optimized GeoTIFF, Zarr, GeoParquet) tamogatja. A **Copernicus Data Space Ecosystem** az EU Copernicus-program teljes adatarchivumaht teszi elérhetővé, openEO API-val.

A lenyegi különbség a GEE-vel szemben: nagyobb szabadsaag az eszkozvalaaasztaasban (tetszoleges Python környezet hasznalhato, nem csak a GEE API), és a STAC szabvany alkalmazaaasa, amely az adatkereeseest szabvaanyositja.

### 19.10.3 Felhonatihv formatumok

A felhőalapú térinformatika nem egyszeerusen azt jelenti, hogy a régi formatumokat felhőszerverre masoljuk. A felhonativ formatumok kifejezetten a halozati hozzaaferesre lettek optimalizalva:

| Formatuum | Tipus | Lenyeg |
|-----------|-------|--------|
| **Cloud Optimized GeoTIFF (COG)** | Raszter | Csempeezett, piramisos GeoTIFF; HTTP range request-ekkel szelektiven olvashaato |
| **Zarr** | Tobbdimenzios tömb | Chunked array formatumm idősorokhoz és 3D adatokhoz |
| **GeoParquet** | Vektor | Oszlop-orientalt, gyors szureesu vektoros formatuum |
| **STAC** | Metaadat | JSON-alapu ter-ido metaadat-szabvaany és keresesi protokoll |

> **Kapcsolodas a 14. fejezethez**: A 14. fejezet részletesen taaargyalja a felhőalapú munkakörnyezeteket. A térinformatikában a felhőalapú platformok azert különösen fontosak, mert az adatmennyiseg (petabajtok) fizikailag leehetetlenne teszi a lokalis feldolgozást.

---

## 19.11 Magyar térinformatikai kontextus

A térinformatika Magyarországon gazdag hagyomanyokkal és sajatos intézményi, technológiai kereetrendszerrel rendelkezik. Ebben az alfejezetben osszefoglaljuk azokat a magyar specifikus elemeket, amelyeket az AI-alaapuu térinformatikai munkaban ismerni kell.

### 19.11.1 Intezmenyi hatter

**Lechner Tudaskoozpont** (korrabban FOMI -- Foldmeresugyi és Taverzekeelesi Intezet): A magyar allaami térinformatika kozponti intezmenye. A Lechner Kozpont kezeli az országos geoodeziai alaphaalozatot, a kataszteri nyilvanntartast, a topograafiai térképezestt és a mműholdfelvetelek hazai forgalmazasat.

**MePAR** (Mezogazdasagi Parcella Azonosito Rendszer): Az Europai Unio Kozos Agrarppolitikajanak (KAP) tamogatasi rendszereehez kapcsolodo parcella-nyilvantartas. A MePAR referencia-parcellakat tartalmaz, amelyeekeet műholdfelvetelekbol frissitenek -- ez az egyik első magyar operativ alkalmazása a taverzzekelesnek a kozigazgaatasban. Az AI-alapú felszínborítás-osztályozás a MePAR frissiteseet draamaian felgyorsithatja.

**Nemzeti Teriiinformaacios Infrastruktúra** (NTI): Az INSPIRE iranyelvv magyar megvaalositaasa. Az NTI celjaa a magyar térbeli adatok interoperaabiilis, szabbvaanyos hozzaaferhetosegenek biztositaasa.

### 19.11.2 Az EOV koordináta-rendszer

Az **Egységes Országos Vetületi rendszer** (EOV, EPSG:23700) a magyar teriinformatika alap-vetületi rendszere. Ismertetoje:

- **Vetületi tipus**: Ferdetengelyu Mercator (oblique Mercator)
- **Datum**: HD72 (Hungarian Datum 1972)
- **Kozeppont**: Gellert-hegy (47d 06' 35.36" N, 19d 02' 54.96" E)
- **Ertektartományok**:
  - Northing (Y): 0 -- 400 000 meter
  - Easting (X): 400 000 -- 1 000 000 meter

**Fontos**: A fejléc-címkék gyakran félrevezetőek! Sok adatfajlban az "X" oszlop az Easting-et, az "Y" az Northing-ot tartalmazza -- de előfordul az ellenkezoje is. Az értéktartomány-alapu azonositas a megbizhato módszer:
- Ha egy érték 0 és 400 000 kozott van: **Northing**
- Ha egy érték 400 000 és 1 000 000 kozott van: **Easting**

Az AI kodgenerálo eszkozooket is erre kell "megtanitani" -- a prompt-ban mindig érdemes megadni: "A koordinátak EOV-ban vannak (EPSG:23700), a Northing 0--400k, az Easting 400k--1M."

### 19.11.3 Magyar térbeli adatforrások

| Adatforras | Tipus | Hozzaaferes |
|------------|-------|-------------|
| Lechner ortofotok | Legifelvetel (0.2--0.4 m) | Korlatozottan nyilt |
| Copernicus DEM (GLO-30) | Domborzatmodelll (30 m) | Nyilt |
| Sentinel-2 | Muholdfelveetel (10 m) | Nyilt (Copernicus) |
| OpenStreetMap | Vektoros kozossegi térkép | Nyilt |
| MePAR | Mezogazdasagi parcellak | Korlatozottan nyilt |
| CORINE Land Cover | Felszinboritas | Nyilt (EEA) |
| LIDAR500 | LiDAR pontfelho | Korlatozottan nyilt |
| e-kataszter | Tulajdoni adatbázis | Korlatozott |

### 19.11.4 Debreceni GIS-kutatas

A Debreceni Egyetem szaamos térinformatikai kutatoocsoporttal rendelkezik:

- **Környezetgazdálkodási és Környezetpolitikai Intézet**: Térbeli környezeti modellezés, vízgyűjtő-szintű elemzések, talajvíz-monitoring
- **Termanat Laboratórium**: Távérzékelési adatfeldolgozás, vegetáció-monitoring, precíziós mezőgazdaság
- **Informatikai Kar**: Geoinformatikai szoftverfejlesztés, térbeli adatbázisok, webes térképszolgáltatások

A debreceni kutatás kiemelt tématerületei: az Alföld talajvízszint-változásainak monitoringja, a Hortobágyi Nemzeti Park vegetációjának távérzékelési elemzése, és a precíziós mezőgazdasági alkalmazások az Alföld agrárterületein.

---

## 19.12 Gyakorlati feladatok

### 19.12.1 Feladat: NDVI-térkép készítése AI-val

**Cél**: Sentinel-2 felvételből NDVI (Normalized Difference Vegetation Index) térképet készíteni egy választott magyar területre.

**Eszközök**: Claude vagy ChatGPT + Python (rasterio, matplotlib)

**Lépések**:
1. Válassz egy területet (pl. Hortobágy, Balaton-felvidék, Budapest agglomeráció)
2. Kérd meg az AI-t, hogy írjon Python-kódot a következő feladatokra:
   - Sentinel-2 L2A adatok letöltése a Copernicus Data Space-ből (vagy használj egy már letöltött minta-állományt)
   - B04 (vörös) és B08 (NIR) sávok beolvasása
   - NDVI számítás: $NDVI = (NIR - Red) / (NIR + Red)$
   - Felhőmaszkolás az SCL sáv alapján
   - Az eredmény vizualizációja matplotlib-tel
   - Mentés Cloud Optimized GeoTIFF-ként
3. Futtasd a kódot, és értelmezd az eredményt: hol magas az NDVI (sűrű vegetáció), hol alacsony (épített terület, vízfelület)?

**Bónusz**: Készíts két időpont (pl. 2020 július és 2024 július) NDVI-térképét, és számítsd ki a különbséget -- hol változott a vegetáció?

### 19.12.2 Feladat: Térbeli lekérdezés természetes nyelven

**Cél**: Természetes nyelvű kérdésekből PostGIS SQL-t generáltatni.

**Eszközök**: Claude vagy ChatGPT

**Lépések**:
1. Definiáld a következő adatbázis-sémát az AI számára:
   ```
   Táblák:
   - telepulesek (nev TEXT, lakos INTEGER, geom GEOMETRY, SRID 23700)
   - vizfolyasok (nev TEXT, tipus TEXT, geom GEOMETRY, SRID 23700)
   - natura2000 (terulet_nev TEXT, kod TEXT, geom GEOMETRY, SRID 23700)
   ```
2. Tedd fel a következő kérdéseket, és kérd az AI-t SQL-re fordításra:
   - "Melyik települések vannak 10 km-en belül a Tiszától?"
   - "Mekkora a Natura 2000 területek összes kiterjedése Hajdú-Bihar megyében hektárban?"
   - "Melyik a legközelebbi település a Hortobágyi Nemzeti Parkhoz, és milyen távolságra van?"
3. Ellenőrizd a generált SQL-t: helyes-e a CRS (EPSG:23700)? Használja-e az ST_Transform-ot, ha szükséges? A területszámítás m2-ben jön, és elosztja-e 10000-rel a hektárhoz?

### 19.12.3 Feladat: Automatizált térképkészítés n8n-nel

**Cél**: n8n munkafolyamatot építeni, amely automatikusan havi térképet generál.

**Eszközök**: n8n (telepített vagy felhőalapú) + Python

**Lépések**:
1. Hozz létre egy n8n munkafolyamatot a következő node-okkal:
   - *Schedule Trigger*: minden hónap elsején
   - *HTTP Request*: STAC API lekérdezés a Sentinel-2 felvételekért
   - *Code* (Python): NDVI számítás és térkép generálás
   - *Email*: az eredmény elküldése
2. Teszteld a munkafolyamatot manuálisan (a Schedule Trigger helyett Manual Trigger-rel)
3. Dokumentáld a munkafolyamatot -- mentsd el, és exportáld JSON-ként

### 19.12.4 Feladat: Kriging Python-ban AI segítséggel

**Cél**: Térbeli interpolációt végezni pontszerű adatokból.

**Eszközök**: Claude vagy ChatGPT + Python (pykrige, matplotlib)

**Lépések**:
1. Készíts egy minta-adathalmazt: 20 fiktív monitoring kút EOV koordinátákkal (Northing: 200000--260000, Easting: 700000--760000) és talajvízszint-értékekkel (80--90 m aB. -- ahol "aB." = a Balti-tenger felett)
2. Kérd az AI-t, hogy írjon Python-kódot a következő feladatokra:
   - Empirikus variogram számítása és ábrázolása
   - Szférikus variogram-modell illesztése
   - Ordinary kriging futtatása a `pykrige` könyvtárral
   - A kriging-eredmény (becsült érték és kriging-variancia) vizualizációja két térképen
3. Értelmezd az eredményt: hol nagy a kriging-variancia (= hol bizonytalan a becslés)? Hova érdemes új monitoring kutat telepíteni?

### 19.12.5 Feladat: AI ágens térbeli elemzéshez

**Cél**: Egy egyszerű AI ágenst építeni, amely térbeli kérdésre térbeli elemzéssel válaszol.

**Eszközök**: Claude API (lásd 12. fejezet) + GeoPandas

**Lépések**:
1. Definiálj 3--4 "eszközt" (Python függvényt), amelyet az ágens használhat:
   - `load_layer(path)`: GeoPackage réteg betöltése
   - `buffer(gdf, distance)`: puffer generálása
   - `spatial_join(gdf1, gdf2)`: térbeli join
   - `calculate_area(gdf)`: területszámítás hektárban
2. A 12. fejezetben tanult mintára építve készíts egy egyszerű ReAct ágenst, amely:
   - Megkapja a felhasználó kérdését (pl. "Hány épület esik a Tisza 1 km-es pufferzónájába?")
   - Gondolkodik: milyen rétegekre van szükség, milyen műveleteket kell végezni
   - Cselekszik: meghívja a megfelelő eszközöket
   - Megfigyel: ellenőrzi az eredményt
   - Válaszol
3. Teszteld a rendszert többféle kérdéssel, és dokumentáld a sikeres és sikertelen eseteket

---

## 19.13 Összefoglalás

Ebben a fejezetben végigjártuk, hogyan hatja át az AI a térinformatika minden szegmensét:

- **Adatfeldolgozás** (19.2): A műholdkép-feldolgozás, a LiDAR-osztályozás és a vektoros adattisztítás az AI által nagyságrendekkel felgyorsul
- **Kódgenerálás** (19.3): Az LLM-ek megbízhatóan generálnak ArcPy, QGIS Processing, GeoPandas, rasterio és PostGIS kódot -- a térinformatikus természetes nyelven fogalmazza meg a feladatot
- **Térbeli predikció** (19.4): A CNN-ek, a foundation modellek és a hibrid geostatisztikai modellek a felszínborítás-osztályozástól a talajvízszint-becslésig forradalmasítják a térbeli predikciót
- **Vizuális programozás** (19.5): A KNIME és az n8n a GIS-munkafolyamatokat vizuálisan dokumentálttá és automatizálttá teszik
- **Térbeli RAG** (19.6): A térbeli adatbázisok, metaadat-katalógusok és jogszabályi tudásbázisok felett természetes nyelvű kérdésfeltevés válik lehetővé
- **3D GIS és digitális ikrek** (19.7): A városi és infrastrukturális digitális ikrek a klímaadaptáció és a prediktív karbantartás eszközei
- **Autonóm GIS** (19.8): Az AI ágensek a természetes nyelvű utasításból kiindulva önállóan tervezik és hajtják végre a térbeli elemzést
- **Felhőalapú GIS** (19.9): A Google Earth Engine, a Planetary Computer és a Copernicus Data Space a petabájtos adatarchívumok AI-alapú feldolgozását teszik lehetővé
- **Magyar kontextus** (19.10): Az EOV koordináta-rendszer, a Lechner Központ, a MePAR és a magyar térbeli adatinfrastruktúra a hazai alkalmazások kerete

A térinformatika nem öncélú technológia -- a környezeti problémák megértésének és kezelésének egyik leghatékonyabb eszközrendszere. Az AI ezt az eszközrendszert tíz-százszoros hatékonysággal erősíti meg: amit korábban hónapokig tartott, az ma napok alatt elvégezhető. A kulcs azonban változatlan: a térbeli gondolkodás, a környezeti szaktudás és az eredmények kritikus értékelése megmarad az ember feladatának. Az AI nem helyettesíti a térinformatikust -- de az AI-t használó térinformatikus már most hatékonyabb, mint a nélküle dolgozó.

---

> **Ajánlott következő lépések**:
> - Ha a kódgenerálást szeretnéd mélyíteni: térj vissza az **5. fejezethez**
> - Ha az ágensek építése érdekel: a **12. fejezet** részletes útmutatást nyújt
> - Ha a RAG rendszert szeretnéd kipróbálni saját térbeli adataiddal: a **9. fejezet** lépésről lépésre bevezet
> - Ha a felhőalapú munkakörnyezetekről szeretnél többet tudni: a **14. fejezet** a kiindulópont
