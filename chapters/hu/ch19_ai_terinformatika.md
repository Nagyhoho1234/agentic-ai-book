# 19. fejezet — AI a terinformatikaban

> **Fejezet-informacio**
> - **Kinek szol:** Terinformatikusoknak, kornyezetkutatoknak es GIS-felhasznaloknak
> - **Eloismeretek:** 1-4. fejezet (AI alapok); a 5. es 9. fejezet ajanlott
> - **Amit megtanulsz:**
>   - AI-alapu muholdkep-feldolgozas es felszinboritas-osztalyozas
>   - Autonom GIS rendszerek: termeszetes nyelvu terinformatikai elemzes
>   - Magyar terinformatikai kontextus (EOV, Corine, Natura 2000)
> - **Szukseges eszkozok:** Browser + terminal + Python (QGIS + Google Earth Engine)
> - **Kapcsolodo fejezetek:** 5. fejezet (kodolas), 10. fejezet (digitalis ikrek), 17. fejezet (mezogazdasag), 18. fejezet (hidroinformatika)

---

## Nyito jelenet: Amikor a terkep "megtanul" gondolkodni

Kepzeld el a kovetkezo helyzetet. Szabo Anna kornyezetinformatikus vagy a Debreceni Egyetemen. A feladatod: felmerni, hogyan valtoztak a Tisza arteri elohelyek az elmult ot evben, milyen felszinboritasi valtozasok tortentek a Natura 2000 teruletek kornyeken, es hogy a varosias beruhazasok veszelyeztetik-e a vedett zonak pufferzoinajat. Ehhez szukseged van Sentinel-2 muholdfelvetelekre, Corine Land Cover adatokra, Natura 2000 poligonokra, Magyar EOV koordinatarendszerben levo parcellahatarokra es hidrografiai adatokra. Raadasul az eredmenyeket ossze kell vetned a vonatkozo jogszabalyokkal, es egy szakmai riportban kell osszefoglalnod.

Harom evvel ezelott ez a feladat harom honapnyi munka lett volna: adatok letoltese kulonbozo portalokrol, koordinata-rendszer harmonizacio, raszteres es vektoros adatok osszemetszese QGIS-ben, vizualis interpretacio, statisztikai osszesites Excelben, vegul a riport megirasa. Ma -- 2026-ban -- a munkafolyamat gyokeresen mas. Leirod a feladatot termeszetes nyelven egy AI agensnek, amely automatikusan megkeresi a relevanns muholdfelveteleket a STAC katalogusbol, letolti es elofeldolgozza a rasztereket, elvegzi a felszinboritas-osztályozast egy foundation modellel, kiszamitja a zonalis statisztikat a Natura 2000 poligonokra, osszeveti az eredmenyeket a jogszabalyi adatbazissal (RAG), es generäl egy terkepes riportot -- mindezt egyetlen del alatti munkaval.

Ez nem science fiction. Ez az **AI-alapu terinformatika** vilagaa, es ebben a fejezetben vegigvezetlek rajta: az adatfeldolgozastol a kodgenerälason at az autonom terinformatikai rendszerekig.

---

## 19.1 Hogyan alakitja at az AI a terinformatika minden szegmenset?

A terinformatika -- vagy geoinformatika -- az a tudomanyterulet, amely a foldi terben elhelyezkedo jelensegek digitalis rogzitesevel, modellezeseivel, elemzesevel es kommunikaciojaaval foglalkozik. A modern terinformatika harom oszlopon nyugszik: a **helyzeti komponens** (hol), az **attributum komponens** (mi) es az **idobeli komponens** (mikor). Az AI mindharom oszlopot forradalmasitja.

### 19.1.1 Az AI-GIS konvergencia hajtoeröi

Negy paarhuzamos trend talaalkozik napjainkban:

1. **Adatrobbanaans**: A Copernicus-program Sentinel muholdjainak napi adattermelese meghaladja a 12 terabajtot. A Planet Labs napi rendszeresseggel keszit 3--5 meteres felbontasu felveteleket a Fold teljes felszinerol. Az IoT-haálozatok -- meteorologiai allomäsok, vizszintmerok, legszennyezetteg-merok -- szinten napi milliardnyi merest generalnak. Ezt az adatmennyiseget emberi erovel mar lehetetlen feldolgozni.

2. **Szamitasi kapacitas**: A felhoalapu platformok (Google Earth Engine, Microsoft Planetary Computer, Copernicus Data Space Ecosystem) petabajtnyi adatot es gyakorlatilag korlätlan szamitasi kapacitast tesznek elerhetove egy bongeszöbol. Az "adat a szamitashoz megy" paradigma atadta helyet a "szamitas az adathoz megy" elvnek.

3. **AI modellek erettsege**: A konvolucios neuralis halozatok (CNN), a transzformer architekturak es a geospatial foundation modellek (Prithvi, Clay, SatCLIP) elertek azt a szintet, ahol a muholdkep-osztälyozas, a valtozasdetektalas es a terbeli predikciio pontossaga meghaladja az emberi vizualis interpretacioet.

4. **Nagy nyelvi modellek (LLM)**: A GPT-4, Claude, Gemini es tarsaik kepesek PostGIS SQL-t irni, Python GIS-szkripteket generalni, muholdkepeket ertelmezni es komplex elemzesi terveket kesziteni -- termineszetes nyelvű utasitasbol kiindulva.

Ezek a trendek egyuttesen hozzak letre azt, amit **autonom GIS-nek** (Autonomous GIS) nevez a szakirodalom: olyan rendszert, amelyben az AI nem passziv eszkoze, hanem aktiv partnere a terinformatikusnak. Ebben a fejezetben vegigjarjuk ezt a teljes spektrumot, es megallapitjuk, hogy a konyvunk korabbi fejezeteiböl tanultak -- az AI agensektol (11. fejezet) a RAG rendszerekig (9. fejezet), a kodolasi asszisztensektöl (5. fejezet) a digitalis ikrekig (10. fejezet) -- hogyan alkalmazhatoek a terinformatikaban.

### 19.1.2 A fejezet terkepe

A fejezet felcpitese a kovetkezo logikaat koveti:

| Alfejezet | Tema | Kapcsolodas a konyvhoz |
|-----------|------|----------------------|
| 19.2 | AI a terbelien adatfeldolgozasban | 4--5. fejezet (adatelemzes, kodolas) |
| 19.3 | AI kodolasi asszisztensek GIS-hez | 5. fejezet (kodolasi asszisztensek) |
| 19.4 | Gepi tanulas terbeli predikciohoz | 6. fejezet (matematikai modellezes) |
| 19.5 | Vizualis programozas GIS munkafolyamatokhoz | 8. fejezet (vizualis programozas) |
| 19.6 | RAG terinformatikai tudashoz | 9. fejezet (RAG) |
| 19.7 | 3D GIS es terbeli digitalis ikrek | 10. fejezet (digitalis ikrek) |
| 19.8 | Autonom GIS | 11--12. fejezet (agensek) |
| 19.9 | Big data es felhoalapu GIS | 14. fejezet (AI labor) |
| 19.10 | Magyar terinformatikai kontextus | -- |
| 19.11 | Gyakorlati feladatok | -- |

---

## 19.2 AI a terbeli adatfeldolgozasban

A terinformatika legidoigenresebb, leginkabb "munka-jellegu" feladatai az adatfeldolgozashoz kotodnek: muholdkepek eloofeldolgozasa, LiDAR pontfelhok osztälyozasa, vektoros adatok tisztitasa, koordinata-transzformaciok. Ezek pontosan azok a feladatok, ahol az AI -- akár kep-alapu melytanulaskent, akär kodgenerlako LLM-kent -- a legnagyobb hatast fejti ki.

### 19.2.1 Muholdkep-feldolgozas AI-val

A hagyomanyos muholdkep-feldolgozasi lanc a kovetkezo lepesekbol all: (1) letoltes, (2) legkori korrekcioo (atmoszferikus korrekcioo: a nyers reflektancia aatalakitasa felszini reflektanciaava), (3) geometriai korrekciio, (4) felhomaszkoolas, (5) mozaikolais es (6) kompozitkeszites. Ezeknek a lepeseknek a tobbsege ma mar automatizalt: a Sentinel-2 Level-2A (L2A) termek mar legkorilag korrigallt es geometriailag pontos felszini reflektanciat tartalmaz.

Az AI ezen felul harom ponton lep be:

**Felhodetektalas es felhomaszkoolas**: A hagyomanyos kuszobertekk-alapu felhodetektalas (mint a Sentinel-2 SCL savja) gyökran hibazik: a havat felhönak, a magas albedoju varosi feluleteket felhönek, a vekony cirrus-felhot pedig atlatszónak osztalyozza. A CNN-alapu felhodetektalas -- peldaul az S2Cloudless (Sentinel Hub) -- 95%+ pontossaggal osztälyozza a felhöpixeleket, es a Sentinel Hub platformon automatikusan alkalmazodik.

**Muholdfelvetelek szuperfelbontas-javitasa** (super-resolution): AI modellek kepesek a 20 meteres felbontasu Sentinel-2 savokat 10 meteres felbontasra javitani, vagy akär 2,5 meteres "szintetikus" felbontast generalini. Ez nem varazslat -- a modell a 10 meteres savokbol es a 20 meteres savok kozotti osszefuggesekbol tanulja meg a felbontas-javitast. A kornyezeti alkalmazasokban ez akkor hasznos, ha a 10 meteres felbontaas nem elegendo (peldaul varosi zoldfeluletek reszletes terkepezese), de kereskelmi nagyfelbontasu felvetelek nem elerheroek.

**Idosor-kompozitak intelligens eloallitasa**: A hagyomanyos median-kompozit az egyes pixelek egesz eves felveteleinek medianjabol szaamoloodik. Az AI-alapu megkozelites -- peldaul a Temporal Attention Encoder -- a felhos idoopontokat automatikusan alacsony sullyal kezeli, es a "legjobb pixelt" választja a vizualis minoseg es a tematikus pontossag alapjan.

> **Kapcsolodas a 4. fejezethez**: Ahogyan a 4. fejezetben (Adatelemzes kod nelkul) lattad, az AI-val vegzett adattisztitas es -elofeldolgozas dontoen csökkenti a rutinmunka mennyiseget. A teriinformatikaban ez megsokszorozodik: egyetlen Sentinel-2 jelenet 13 savbol, 109 millio pixelbol all, es egy orszagnyi elemzeshez evente tobb szaz jelenet feldolgozasa szuukseges.

### 19.2.2 LiDAR pontfelhö-feldolgozas

A lejzeres letapogatäs (LiDAR) suru haromdimenzios pontfelhoket allit elo, amelyekbol digitalis domborzatmodellek (DTM), digitalis felszinmodellek (DSM) es haromdimenzios epuletmodellek szarmaztathaatok. A nyers pontfelhö feldolgozasänak legidoigenryesebb lepeese az **osztälyozas**: minden pontrol eldonteni, hogy talajpont, vegetacio, epulet, vezetek vagy egyeb objektum.

A hagyomanyo szuroalgoritmusok (progressziv morfologiai szuros, csucshelyesiites) jol mukodnek sik terepen, de meredek domboldalon, suuru varosias kornyezetben vagy osszetett vegetacio mellett gyakran hibaznak. A **deep learning-alapu pontfelhö-osztälyozas** -- peldaul a PointNet++ vagy a RandLA-Net -- kozvetlenul a 3D pontokon dolgozik, es automatikusan tanulja meg a termeszetes es epitett kornyezet terbeli mintazatait.

A magyar LIDAR500 program -- amely az egesz orszag legifeelveteeles LiDAR-felmereset celozza -- tobb tiz terabäjtnyi pontfelhoet eredmenyez. Ennek a hatalmas adattomegnek a feldolgozasa AI nelkul eveket venne igenyebe; a melytanulasi modellekkel a munka henapokra csokkentheto.

### 19.2.3 Vektoros adatok es koordinata-transzformaciok

A vektoros adatok -- pontok, vonalak, poligonok -- tisztitasa es harmonizalasa szinten idoigenyes feladat. A tipikus probelimak: onmetszo poligonok (topologiai hibak), elteero koordinata-rendszerek (az EOV-ban levo kataszteri adatok es a WGS 84-ben levo GPS-merresek osszeveteese), hianyos attributumok es eltero osztälyozasi schemak.

Az AI itt elsösorban **kodgeneralocskent** segit: a feladat leirasaabol automatikusan general GeoPandas- vagy PostGIS-kodot a koordinata-transzformaciohoz, a topologiai javitashoz es az attributum-harmonizaciohoz. Errol reszletesen a 19.3 alfejezetben lesz szo.

> **Az EOV koordinata-rendszer felismerese**: A magyar geoinformatikaban az EOV (Egyseges Orszagos Vetuleti rendszer, EPSG:23700) a leggyakoribb vetuleti rendszer. Az EOV koordinatak felismerese **ertek-tartomany** alapjan lehetseges: a Northing ertekek 0 es 400 000 kozott, az Easting ertekek 400 000 es 1 000 000 kozott mozognak. Fontos: a fejlec-cimkek gyakran felrevezetoek (a "X" mezo tartalmazhatja a Northingot vagy az Eastinget is) -- mindig az ertektartomany az iranyadoo.

---

## 19.3 AI kodolasi asszisztensek GIS-hez

Az 5. fejezetben megtanultad, hogyan hasznalhatod az AI kodolasi asszisztenseket (Claude, ChatGPT, GitHub Copilot, Cursor) Python-szkriptek irasaahoz -- programozasi tapasztalat nelkul is. A terinformatikaban ez a kepesseg kulonosenn hatalmmas, mert a GIS-munka nagy resze automatizalhato Python-nel, de a GIS-Python okoszisztema (ArcPy, QGIS Processing, GeoPandas, rasterio, xarray) rendkivul szerteagazo es osszetett.

### 19.3.1 Python GIS-szkriptek generaalasa

Az LLM-ek a GIS-Python ökoszisztemaat jol ismerik, mert a tanito szovegekben boven talalhato GeoPandas, rasterio es PostGIS dokumentacio. A tipikus felhasznalasi mintak:

**Vektoros muveletek GeoPandas-szal:**

```
Prompt: "Ird meg Python-ban, hogyan olvassak be egy GeoPackage
fajlt GeoPandas-szal, szurjem a 'települes' oszlop alapjan
Debrecenre, keszitsek 500 meteres puffert, es mentsem el uj
GeoPackage-kent EOV vetuleetben (EPSG:23700)."
```

Az AI altal generalt kod tipikusan:

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

### 19.3.2 ArcPy es QGIS Processing

Ha ArcGIS Pro kornyezetben dolgozol, az ArcPy az automatizalas eszkoze. Az LLM-ek az ArcPy-t is ismerik:

```
Prompt: "ArcPy-val futtasd le a Spatial Join muveleteet
az 'epuletek' es a 'arvizkockazat' retegek kozott, es
szamold ki, hany epulet esik magas kockazatu teruuletre."
```

QGIS Processing eseteen a `processing.run()` fuggvenyhivasok generalasa szinten jol mukodik:

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

### 19.3.3 PostGIS terbeli lekerdezesek

Az AI kodolasi asszisztensek a PostGIS terbeli SQL-t is megbiizhatoan generaljak. Ez kulonosen ertekes, mert a PostGIS fuggvenykonyvtar rendkivul kiterjedt (tobb szaz terbeli fuggveny), es a helyes hasznalat mellyrehatö terbeli gondolkodast igenyel.

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

> **Tipikus hibaforrasok**: Az LLM-ek a GIS-kodgeneeralasnaal a kovetkezo hibakat kovetik el leggyakrabban: (1) **CRS-hiba** -- EOV helyett WGS 84-et felteteleznek, mert az a leggyakoribb a tanitoszovegekben (az esetek 25--35%-aban); (2) **szemantikai hiba** -- rossz oszlopnevet vagy osztalykodot hasznalnak; (3) **topologiai hiba** -- nem kezelik az onmetszo poligonokat (ST_MakeValid hianya). A 12. fejezetben tanult validaacios lepesek (onselfcheck, iterativ javitas) itt kulonosenn fontosak.

---

## 19.4 Gepi tanulas terbeli predikciohoz

A 6. fejezetben (Matematikai modellezes) megismerkedsz a gepi tanulas alapjaival. A terinformatikaban a gepi tanulas harom fo feladattipusban jelenik meg: felszinboritas-osztälyozas, geostatisztikai modellezes es terbeli interpolacio.

### 19.4.1 Felszinboritas-osztälyozas

A felszinboritas-osztälyozas a taverzekeles "Hello World" feladata: muholdfelvetelbol automatikusan meghataarozni, hogy a Fold felszinenn hol van erdoo, mezogazdasagi terulet, vizfelulet, epitett terulet stb. Az elmult evtizedek fejlodese:

| Korszak | Modszer | Tipikus pontossag | Jellemzo |
|---------|---------|-------------------|----------|
| 1970--1990 | Maximum Likelihood | 70--80% | Normalis eloszlas feltevezes |
| 2000--2015 | Random Forest | 80--90% | Nem feltetelaz eloszlast, sok jellemzo |
| 2015--2020 | U-Net (CNN) | 85--95% | Automatikus jellemzoetanulas |
| 2020-- | Foundation modellek (Prithvi, Clay) | 90--97% | Elotanitott, keves cimkezeiett adat kell |

A **U-Net** architektura -- amelyet a 6. fejezetben az encoder-decoder halozatok kozott emlitettunk -- a terbeli szegmentalas (szemantikus szegmentalas) alapeszkoze: minden pixelt osztalyhoz rendel, figyelembe veve a terbeli kontextust. A U-Net kulcsinnovacioja az atugrasi kapcsolat (skip connection), amely a reszletes terbeli informaciot kozvetiti az alacsony szintu retegekbol a magas szintu retegekbe.

A legujabb fejlemeny a **geospatial foundation modellek**: a Prithvi (NASA/IBM, 2023) es a Clay (Radiant Earth, 2024) hatalmas mennyisegu cimkezetlen muholdkepen elotanitott modellek, amelyeket keves cimkezett mintaval finomhangolhatunk specifikus feladatokra. Ez a transfer learning paradigma -- amelyet a 6. fejezetben taargyaltunk -- a taverzekelesben kulonosen hatekony, mert a cimkezett tanitoadat eloallitaasa rendkivul draaga es iodoigenyes.

### 19.4.2 Geostatisztikai modellezes es terbeli interpolacio

A geostatisztika a terben mintazott adatok statisztikai elemzesenek es az optimalis terbeli interpolacionak a modszertana. Az alapelv Tobler elso foldrajzi torvenye: *"Minden mindennel osszefugg, de a kozelebbi dolgok jobban osszefuggenek, mint a tavoliak."*

A klasszikus geostatisztikai munkafolyamat:

1. **Variogram-szamitas**: Megvizsgaaljuk, hogyan no az erttekkülonbsegek varianciaja a mintapontok kozotti tavolsag fuggvenyeben
2. **Variogram-modell illesztese**: Szferikus, exponencialis vagy Gauss-modellt illesztunk
3. **Kriging**: Az illesztett variogram alapjan optimalis, minimalis varianciaju linearis becslest vegzunk a mintapontoek kozotti teruletekre

A variogram harom kulcsparametere:
- **Roghatas (nugget)**: A mikro-skaläju valtozekonysag es a meresi hiba
- **Teto (sill)**: A teljes variancia
- **Hatotavossag (range)**: Az a tavolsag, amelyen belul a pontok teerben korrelältak

Az **AI belepesi pontja** a geostatisztikaba tobbfele:

**Automatikus variogram-illesztes**: Az LLM-ek kepesek Python-kodot generalni a variogram szamitasahoz es illesztsehez (a `scikit-gstat` vagy `pykrige` konyvtarakkal), beleertve a modellszelekcios es a cross-validacios leepeseket is.

**Hibrid modellek**: A Random Forest Kriging (RFK) es a Gradient Boosting + Kriging hibrid modszerek a nem-terbeli prediktorok (domborzat, talaj, klimaado) es a terbeli autokorrelacioo elonyeit egyszerre hasznossitjak. Peldaul a Duna-Tisza kozi talajvizszint predikciojahoz: a Random Forest a domborzatbol, a meteorologiai adatokbol es a talaj tipus obol becsuli a talajvizszintet, majd a kriging a reziduumok (maradekok) terbeli korrelaciojat modelleezi.

**Deep learning-alapu terbeli interpolacio**: A graf neuralis halozatok (GNN) a mintaveli pontokat grafkent kezelik, es a message passing mechanizmussal a szomszedos pontok informaciojat integraljaak. Ez kulonosen hatekony szbalytalan mintaveteeli elrendezeseknel, ahol a klasszikus kriging kuszobertekekre es lag-beallitasokra erzekeny.

### 19.4.3 Peldaa: Talajvizszint-becslees a Duna-Tisza kozen

Vegyuk a Duna-Tisza kozi homokhaatsag talajvizszint-becsleset -- egy klasszikus magyar geoinformatikai pelda. A monitoring kutak szama nehany szaz, de a terulet tobb ezer negyzetkilometerss. A feladat: megbizhato terkepet kesziteni a kutak kozotti teruletekre.

**Hagyomanyos megkozelites**: Ordinary kriging a kutadatokra. A hatotavolsag tipikusan 8--15 km, ami meghataarozza a monitoring-halozat szuukseges suruseget.

**AI-tamogatott megkozelites**:

1. A Random Forest prediktorai: Copernicus DEM domborzati valtozoi (lejtoszog, topografiai nedvessegindex), Sentinel-2-bol szarmaztatott vegetacios indexek (az aktiv vegetacio a felszinkoozeli talajviz jelenletere utal), talajterkep, meteorologiai adatok
2. Az RF predikcioja a determinisztikus komponens
3. A kriging a reziduumokra: a maradek terbeli mintazat modellezeese
4. Eredmeny: 100 meteres felbontäsu talajvizszint-terkep, amely a hagyomanyos kriginggel szemben 15--25%-kal alacsonyabb becsleesi hibaval rendelkezik

> **Kapcsolodas a 6. fejezethez**: A hibrid modellezes logikaja megegyezik a 6. fejezetben tanult ensemble megkozelitessel: tobb modell kombinälasa jobb eredmenyt ad, mint barmelyik modell onmagaban.

---

## 19.5 Vizualis programozas GIS munkafolyamatokhoz

A 8. fejezetben (Vizualis programozas) megismerkedtel a KNIME-val es az n8n-nel -- ket vizualis munkafolyamat-szerkesztovel, amelyekkel kod nelkul epithetrol osszetett adatfeldolgozasi lancokat. A terinformatikaban mindket eszkoz rendkivul hatekony.

### 19.5.1 KNIME terbeli adatelemzeshez

A KNIME Analytics Platform a Geospatial Analytics Extension reveln terbeli adatokat is kezel. A tipikus felhasznalasi mintak:

**Terbeli adatok beolvasasa es vizualizacioja**: A KNIME GeoPackage, Shapefile, GeoJSON es CSV (koordinatakkal) formasatumokat olvas, es a beepitett Geospatial View nodeokkal interaktiv terkepeeket jelenjet meg.

**Geostatisztikai munkafolyamat KNIME-ban**:
1. *GeoFile Reader* node: monitoring kutadatok beolvasasa
2. *Row Filter*: idoszaki szures (pl. 2025. oktober)
3. *Math Formula*: elooszamitasok
4. *Python Script* node: variogram szamitas es kriging a `pykrige` konyvtarral
5. *Geospatial View*: az eredmeny-terkep megjelenitese
6. *GeoFile Writer*: eredmeny mentese GeoPackage-kent

A KNIME elonye a GIS-munkaban, hogy a munkafolyamat **vizuaalaisan dokumentalt es reprodukalhato** -- a 8. fejezetben tanult elonyok itt kulonoesen fontosak, mert a terbeli elemzesek reprodukalhatosaga a tudomanyos kutatasban alapkoveteelmeny.

### 19.5.2 n8n automatizalt terkepkesziteshez

Az n8n -- a 8. fejezetben megismert automatizaaciios platform -- a terkepkeszites automatizalasaara hasznalhato:

**Automatizalt havi NDVI-terkep munkafolyamat**:
1. *Schedule Trigger*: minden honap 5-en elindul
2. *HTTP Request* node: STAC API lekerdeses a Sentinel-2 felvetelekert (az elozo honap, felhoboritals < 20%)
3. *Code* node: NDVI szamitas Python-ban (rasterio)
4. *Code* node: terkep generalas Matplotlib-tel
5. *Email Send* node: a terkep elküldese a kutatocsoportnak
6. *Webhook* node: riasztas, ha az NDVI anomalisan alacsony (aszalyjel)

Ez a munkafolyamat egyszer letrehozva honaprol honapra automatikusan fut -- a kutatos emberi beavatkozas nelkul kap friss vegetacios terkeeppeket.

> **Kapcsolodas a 8. fejezethez**: A 8. fejezet reszletesen bevezeti a KNIME es n8n hasznaalataat. Ha meg nem olvastad, erdemes visszalapozni -- az ott tanultak kozvetlenul alkalmazhatoek a GIS munkafolyamatokra.

---

## 19.6 RAG terinformatikai tudashoz

A 9. fejezetben (RAG -- Tanitsuk meg az AI-t a sajaat adatainkra) megtanultad, hogyan epitsz Retrieval-Augmented Generation rendszert, amely a sajat dokumentumaidbol keres ki relevanss informaciot, es az LLM ezek alapjan valaszol. A terinformatikaban a RAG harom kiemelt alkalmazasi teruulettel rendelkezik.

### 19.6.1 Chatbot terbeli adatbazisok felett

Kepzeld el, hogy egy PostGIS adatbaazisban tobb szaz terbeli reteg van: felszinboritas, hidrografia, talaj, domborzat, koezigazgatasi hatarok, Natura 2000 teruuuletek, MePAR parcellak. A RAG-rendszer lehetove teszi, hogy **termeszetes nyelven kerdezz** errol az adatbaaziisrol:

- "Mekkora terulet szantoo Hajdu-Bihar megyeben a Natura 2000 teruletekeen belul?"
- "Melyik telepulesek vannak 5 km-en belul a Tisza arvizi nagyvizi medreetol?"
- "Hogyan valtoozott a Hortobagyi Nemzeti Park felszinboritasa 2018 es 2024 kozott?"

A rendszer a kerdesbol PostGIS SQL-t generaal, vegrehajta az adatbaazison, es az eredmenyt szovegesen osszefoglalja. A **terbeli RAG** speciaalitaasa, hogy a relevancia nemcsak szoveges, hanem **terbeli** is: egy Balatonra vonatkozo kerdes a Balaton kornyeki dokumentumokat is relevansnak tekinti, meg ha a "Balaton" szo expliciten nem is szerepel bennuk.

A megvaalositas technikai vallaza:
- **pgvector + PostGIS** egyazon adatbazisban: a pgvector a szoveges embedding-eket, a PostGIS a geometriakat indexeli, es egyetlen SQL-lekerdezesben kombinalhato a szemantikus es a terbeli kereses
- **Few-shot learning**: nehany pelda-lekerdezez az LLM kontextusaban javitja a generalt SQL minosseget
- **Self-correction**: ha a generalt SQL hibat dob vagy ertelmetleg eredmenyt ad, a hibaüzenet visszaadodik az LLM-nek, amely javitott verziiot generaal

### 19.6.2 Metaadat-kataloguusok es az INSPIRE iranyelvv

Az EU INSPIRE iranyyelve (2007/2/EK) megkooveteli a tagallamoktol a terbeli adatok interoperabilis metaadatokkal valo ellaataasat es haaaloozati szolgaltatasokon (WMS, WFS, ATOM) keresztuli hozzaaferhetooseget. A gyakorlatban a metaadatok gyakran hianyosak vagy pontatlanok -- ez a "metaadat-hezag".

A RAG itt ket modon segit:
1. **Metaadat-generalas**: A multimodaalis LLM-ek (amelyekre a 2. fejezetben hivatkoztunk) kepesek egy terbeli adatreteg tartalmaat automatikusan leirni: a reteg temaja, a terbeli kiterjedese, az attributumok jellege, a feltetelezett koordinata-rendszer
2. **INSPIRE-kompatibilis kereses**: A RAG rendszer az INSPIRE metaadat-kataloogus felett mukodoö chatbot-kent szolgal: a kutato termeszetes nyelven kerdez ("Van-e 10 meteres felbontaasu feelszyinboritas-terkep Magyarorszagra 2024-bol?"), es a rendszer az INSPIRE Discovery Service-bol keresi ki a valaszt

### 19.6.3 Jogszabalyi tudasbaazis terbeli kontextusban

A kornyezetvedelmii hataasvizsgalatoknan es terulet-rendezesi tervek keszitesekor a terbeli elemzes es a jogi hatter osszekötese kritikus. Peldaul: "Milyen korlatozasok vonatkoznak egy tervezett naapelempark helyszinere, ha az egy Natura 2000 terulet 500 meteres pufferzoonajaba esik?"

A **terbeli RAG** a kovetkezo lepeseket hajtja vegre:
1. A tervezett helyszin geometriajjanak betöltese
2. 500 meteres puffer generalasa
3. Metszees a Natura 2000 retteggel -- van-e atfedes?
4. Ha igen: a RAG komponens megkeresi a relevaaans jogszabalyokat (275/2004. Korm. rendelet, a teruletre vonatkozo kezelesi terv)
5. Az LLM osszefoglalja az eredmenyt: "A tervezett helyszin a Hortobaagyi Nemzeti Park (HUDI30001) 500 meteres pufferzoonajaba esik. A 275/2004. Korm. rendelet alapjan..."

> **Kapcsolodas a 9. fejezethez**: Ez a pelda a 9. fejezet RAG architekturajanak terbeli kiteerjeszteese. A kulonbseg: a retriever nemcsak szoveges hasonlosag, hanem **terbeli kozelseg** alapjan is keres.

---

## 19.7 3D GIS es terbeli digitalis ikrek

A 10. fejezetben (Digitalis ikrek) megtanultad, hogy a digitalis iker egy fizikai rendszer virtuallis, valoos ideju, ketiranyuu adataaramlas altal szinkronizalt masaa. A terinformatikaban ez a koncepció a **terbeli digitalis ikerben** (spatial digital twin) öllt testet: egy varos, egy vizgyujto, egy erdoterulet haromdimenzios, szenzor-szinkronizalt virtuallis modellje.

### 19.7.1 3D adatmodellek

A haromdimenzios terinformatika alapvetoen öt adatmodellel dolgozik:

| Modell | Leiras | Alkalmazas |
|--------|--------|------------|
| **Voxel** | 3D racs (a raszter 3D megfeleloje) | Geologia, szennyezes, meteorologia |
| **Mesh** | Haromszoghalos felszin | Vizualizacio, FEM szimulacio |
| **Oktafa** (octree) | Adaptiv 3D racs | Pontfelho-tarolas, LOD |
| **B-rep** | Hataarolo felszinek | CAD, BIM |
| **CSG** | Primitiv testek + Boole-muveletek | Parametrikus tervezes |

A **CityGML** (OGC szabvaany) a varosi 3D modellek szemaantikus adatmodellje, öt reszletessegi szinttel (LOD):
- **LoD0**: Regionalis modell (2.5D felszin + 2D alapterulet)
- **LoD1**: Tomb-modell (extrudalt alapterulet, lapos teto)
- **LoD2**: Tetomodell (tetogeometria, fal/teto/talaj szemantika) -- a legtöbb varosi digitalis iker ezen a szinten mukodik
- **LoD3**: Architekturalis modell (homlokzati reszletek)
- **LoD4**: Belso terek (szobak, folyosok) -- BIM-GIS integracio

A **3D Tiles** (Cesium, OGC szabvaany) a nagy terbeli adathalmazok webes streamingjeenek formátuma, amelyet a CesiumJS es a Google Maps 3D Tiles API hasznaal.

### 19.7.2 Varosi digitalis ikrek

A varosi digitalis iker egy varos haromdimenzios, szenzor-szinkronizalt modellje, amely a kovetkezo retegeket integralja:

- **Epuletgeometria**: LoD2 vagy LoD3 CityGML modell, LiDAR-bol vagy fotogrammetriabol szaarmaztatva
- **Szenzor-adatok**: meteorologiai allomäsok, legosiineneseg-merok, forgalomszaamlalook, energiafogyasztas -- valoos idejuu adataaramlaassal
- **Szimulaacioos modellek**: hosziget-szimulacio, zaj-terjedes, arvizi modell, energetikai modell
- **AI reteg**: anomalia-detektalas a szenzor-adatokon, prediktiv karbantartas az infrastrukturan, optimalizacioos javaslatok

Pelda: **Budapest hosziget-szimulacio**. A 3D epuletmodellbol (LoD2), a felszinboritas-retegbol, a meteorologiai adatokbol es az utcaszinti homerseklet-meresekbol a digitalis iker szimulaalja a varosi hosziget hatasaat. Az AI reteg azonositja a legkritikusabb teruleteket (ahol a nyari ejszakai homerseklet 5+ fokkal meghaladja a kulvarosi erteket), es javaslatot tesz a beavatkoozasra: zoldfellueelet-fejlesztes, albedo-novelö tetofeluletek, vizfeluletek.

### 19.7.3 Infrastruktura-monitoring

A digitalis ikrek az infrastruktura-monitoringban is kulcsszerepuek. Egy hid, egy gaatrendszer vagy egy csatornahalozat digitalis ikre a szerkezeti allapotot szenzor-adatokbol (gyorsulasmero, szintezo, homerseklet) valoos ideeben kooveti, es az AI prediktiv karbantarttaasi modellekkel jeleezi eloroe a beavatkozasi igenyt.

A **BIM-GIS integracio** a kulcs: az epitmeny BIM modellje (IFC formaatumban) a reszletes szerkezeti adatokat, a GIS a kornyyezeti kontextust (domborzat, talaj, vizrajz, szeiszmikus kockazat) szolgaltatja. A ket modell osszekapesolaasa lehetove teszi, hogy az infrastruktura allapotaat a terbeli kornyezetteel egyutt vizsgaaljuk.

> **Kapcsolodas a 10. fejezethez**: A 10. fejezet altalanos ertelemben targyaalja a digitalis ikreket. A terbeli digitalis iker ezeknek egy specifikus, de rendkivul fontos alkalmazasa, ahol a haromdimenzios geometria es a foldrajzi kontextus a meghataarozo.

---

## 19.8 Autonom GIS: AI agensek a terinformatikaban

A 11. fejezetben (Az AI agensek megertese) es a 12. fejezetben (AI agensek epitese) megtanultad, mi az AI agens, hogyan mukodik a ReAct ciklus, es hogyan epithetrol tobbagenses rendszereeket. Az **autonom GIS** (Autonomous GIS) ezeknek az elveknek a terinformatikai alkalmazasa -- es egyben a terinformatika legforradalmib fejlemenye.

### 19.8.1 Mi az autonom GIS?

A terinformatika tortenete soran a felhasznalo es a rendszer viszonya fokozatosan alakult at:

| Korszak | Paradigma | A felhasznalo szerepe |
|---------|-----------|---------------------|
| 1960--1990 | Nagygeepes GIS | Programozo |
| 1990--2010 | Asztali GIS (ArcGIS, QGIS) | Szakerto felhasznalo |
| 2010--2020 | Felhoalapu GIS (GEE) | Szkriptiiro |
| 2020--2025 | AI-tamogatott GIS | Prompt-fogalmazo |
| 2025-- | **Autonom GIS** | **Feladat-meghataarozo** |

Az autonom GIS-ben a felhasznalo **nem azt mondja, hogyan** (nyisd meg ezt a reteget, alkalmazz puffert, vegezz join-t), hanem **azt mondja, mit** akar (melyik telepulesek vannak 500 meteren belul az arvizveeszelyes teruletektol?) -- es a rendszer maga tervezi meg es hajtja vegre az elemzest.

### 19.8.2 Az autonom GIS szintjei

A jarmuipari autonom vezetes analogiajaara epitvee ot szint kulonboztetheto meg:

| Szint | Megnevezes | Leiras | Pelda |
|-------|-----------|--------|-------|
| 0 | Nincs automatizalas | Minden muveletet kezzel vegez a felhasznalo | Hagyomanyos asztali GIS |
| 1 | Asszisztens automatizaalas | Az AI egyszeruu muveleteket vegez utasitasra | Siri/Alexa szintu GIS-parancsok |
| 2 | Resszleges automatizaalas | Az AI tobb muveletet lancolva hajt vegre, emberi felugyeletteel | AI-kodgenerallas QGIS-ben |
| 3 | Felteteles automatizaalas | Az AI tervet keszit, a felhasznalo jovahagyja, az AI vegrehajt | Plan-and-Execute agens |
| 4 | Magas szintu automatizaalas | Az AI onalloan vegez osszetett elemzeseket, emberi ellenoorzes az eredmenyen | ReAct agens GIS eszkozokkel |
| 5 | Teljes automatizaalas | Az AI onalloan tervez, vegrehajt, ellenoriiz, iteraal | Jovoobeli cel |

A 2026-os gyakorlatban a 2--3. szint a realis: az AI nagyon hateekonyan kodot generäl es elemzesi terveket keszit, de az eredmenyek **emberi validäciot igenyeelnek** -- kulonosen a CRS-kezeeles, a topologiai muhveletekk es a szemantikai ertelmeezes teruleten.

### 19.8.3 A ReAct ciklus a terinformatikaban

A 11. fejezetben megismert ReAct (Reasoning + Acting) keretrendszer a terinformatikaban a kovetkezokeeppen mukodik. Vegyunk egy konkret peldat:

**Felhasznaloi kerdes**: "Melyik Natura 2000 teruleteken nott a beepitettseg 2020 ota?"

**1. Gondolat** (Reasoning): "Szuuksegem van a Natura 2000 terurletek poligonjaira es ket idopontra vonatkozo felszinboritas-adatokra. A beepitettseg-noovekedeshez ki kell szamolnom a beepitett terulet aranyat minden Natura 2000 poligonon belul 2020-ban es 2024-ben."

**2. Cselekves** (Acting): STAC API lekerdezes az ESA WorldCover 2020 es 2024 raszterekre, Natura 2000 reteg letoltese.

**3. Megfigyelees** (Observation): "A STAC API visszaadta a rasztereket. A Natura 2000 reteg letoltheto GeoPackage formaaatumban."

**4. Gondolat**: "Zonalis statisztikat kell szamolnom: a beepitett pixel-araany minden Natura 2000 poligonra, mindkeet evre. A retegeket kozos CRS-be kell hoznom."

**5. Cselekves**: Python-kod generaalasa (rasterio + GeoPandas + rasterstats), vegrehajtaas.

**6. Megfigyelees**: "Az eredmeny egy tablazat: beepitett_arany_2020 es beepitett_arany_2024 minden teruletre. 12 teruleten nott."

**7. Gondolat**: "Ellenoorzom: a beepitett arany ertekei 0 es 1 kozott vannak-e? A 12 terulet szaama realis-e Magyarorszaag kb. 480 Natura 2000 teruletere? Igen, konzisztens."

**8. Cselekves**: Eredmeny prezentaalaasa: terkep + tablazat + szoveges osszefoglalo.

### 19.8.4 Tobbagenses GIS-architektura

A 11. fejezetben tanult tobbagenses rendszerek a GIS-ben kulonoosen hatekonykak, mert a terbeli elemzes tobb markánsan eltero szakkompetenciat igenyel:

- **Adat-keresoo agens**: Ismeri a STAC katalogusokat, WFS szolgaltatasokat, PostGIS adatbazisokat. Ha a felhasznalo "erdooboritast" ker, o donti el: ESA WorldCover, Corine Land Cover vagy Sentinel-2-alapu egyedi osztälyozas?
- **GIS-analizator agens**: SQL-t es Python-kodot ir, kezeli a CRS-t, a topologiat es a geometriai muveleteket
- **Kartografus agens**: Az eredmeny vizualizaciiojaert felel -- szinvalasztas, szimbolizacio, jelmagyarazat, terkeepleptek
- **Kritikus agens**: Az eredmenyt erttekeli: ellenoorzi a statisztikai konzisztenciat, a CRS-helyesseeget, a topologiai errvenyesseget

A negy agens uzeneteeken keresztul kommunikaal, es iteralhat: ha a Kritikus agens CRS-hibbat talal, visszakuldi a feladatot a GIS-analizator agensnek.

> **Kapcsolodas a 11--12. fejezethez**: Az agensek epiteesenek technikai reszletei a 12. fejezetben talalhaatok. Itt a GIS-specifikus eszkozvalasztast es az eszkoztar kialakitasat emeljuk ki -- a terinformatikaban tipikusan 15--30 eszkoz (STAC kereses, puffereeles, zonalis statisztika, terkepgeneralas stb.) az optimalis.

---

## 19.9 Big data es felhoalapu GIS AI-val

A 14. fejezetben (AI labor) megismerkedtel a felhoalapu szamitasi kornyezetekkel. A terinformatikaban a felhoalapu platformok a petabajtos muuholdfelveetel-archivumok feldolgozasaahoz nelkülözhetetlenek.

### 19.9.1 Google Earth Engine (GEE)

A Google Earth Engine a terinformatika "nagy durrantasa" volt 2010-ben: petabajtnyi muholdfelvetelt es szamitasi kapacitast tett elerhetove egyetlen boengeeszobol. A GEE Python API-val (a `ee` konyvtaaronn keresztul) planetaris lepteeku elemzeseket futtathatsz nehany sor koddal:

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

Az AI itt ket szinten segit:
1. **Kodgeneralas**: Az LLM a természetes nyelvu leiraasbol GEE Python-kodot generäl
2. **Eredmennyertelmezees**: Az LLM az exportalt NDVI-terkeep statistikait elemzi es szovegesen osszefoglalja

### 19.9.2 Microsoft Planetary Computer es Copernicus Data Space

A **Planetary Computer** a nyilt STAC szabvanyra epit, es a felhonativ formatumokat (Cloud Optimized GeoTIFF, Zarr, GeoParquet) tamogatja. A **Copernicus Data Space Ecosystem** az EU Copernicus-program teljes adatarchivumaht teszi elerhetove, openEO API-val.

A lenyegi kulonbseg a GEE-vel szemben: nagyobb szabadsaag az eszkozvalaaasztaasban (tetszoleges Python kornyezet hasznalhato, nem csak a GEE API), es a STAC szabvany alkalmazaaasa, amely az adatkereeseest szabvaanyositja.

### 19.9.3 Felhonatihv formatumok

A felhoalapu terinformatika nem egyszeerusen azt jelenti, hogy a regi formatumokat felhoszerverre masoljuk. A felhonativ formatumok kifejezetten a halozati hozzaaferesre lettek optimalizalva:

| Formatuum | Tipus | Lenyeg |
|-----------|-------|--------|
| **Cloud Optimized GeoTIFF (COG)** | Raszter | Csempeezett, piramisos GeoTIFF; HTTP range request-ekkel szelektiven olvashaato |
| **Zarr** | Tobbdimenzios tömb | Chunked array formatumm idosorokhoz es 3D adatokhoz |
| **GeoParquet** | Vektor | Oszlop-orientalt, gyors szureesu vektoros formatuum |
| **STAC** | Metaadat | JSON-alapu ter-ido metaadat-szabvaany es keresesi protokoll |

> **Kapcsolodas a 14. fejezethez**: A 14. fejezet reszletesen taaargyalja a felhoalapu munkakornyezeteket. A terinformatikaban a felhoalapu platformok azert kulonosen fontosak, mert az adatmennyiseg (petabajtok) fizikailag leehetetlenne teszi a lokalis feldolgozast.

---

## 19.10 Magyar terinformatikai kontextus

A terinformatika Magyarorszagon gazdag hagyomanyokkal es sajatos intezmenyi, technologiai kereetrendszerrel rendelkezik. Ebben az alfejezetben osszefoglaljuk azokat a magyar specifikus elemeket, amelyeket az AI-alaapuu terinformatikai munkaban ismerni kell.

### 19.10.1 Intezmenyi hatter

**Lechner Tudaskoozpont** (korrabban FOMI -- Foldmeresugyi es Taverzekeelesi Intezet): A magyar allaami terinformatika kozponti intezmenye. A Lechner Kozpont kezeli az orszagos geoodeziai alaphaalozatot, a kataszteri nyilvanntartast, a topograafiai terkepezestt es a mmuholdfelvetelek hazai forgalmazasat.

**MePAR** (Mezogazdasagi Parcella Azonosito Rendszer): Az Europai Unio Kozos Agrarppolitikajanak (KAP) tamogatasi rendszereehez kapcsolodo parcella-nyilvantartas. A MePAR referencia-parcellakat tartalmaz, amelyeekeet muholdfelvetelekbol frissitenek -- ez az egyik elso magyar operativ alkalmazasa a taverzzekelesnek a kozigazgaatasban. Az AI-alapu felszinboritas-osztälyozas a MePAR frissiteseet draamaian felgyorsithatja.

**Nemzeti Teriiinformaacios Infrastruktura** (NTI): Az INSPIRE iranyelvv magyar megvaalositaasa. Az NTI celjaa a magyar terbeli adatok interoperaabiilis, szabbvaanyos hozzaaferhetosegenek biztositaasa.

### 19.10.2 Az EOV koordinata-rendszer

Az **Egyseges Orszagos Vetuleti rendszer** (EOV, EPSG:23700) a magyar teriinformatika alap-vetuleti rendszere. Ismertetoje:

- **Vetuleti tipus**: Ferdetengelyu Mercator (oblique Mercator)
- **Datum**: HD72 (Hungarian Datum 1972)
- **Kozeppont**: Gellert-hegy (47d 06' 35.36" N, 19d 02' 54.96" E)
- **Ertektartomanyok**:
  - Northing (Y): 0 -- 400 000 meter
  - Easting (X): 400 000 -- 1 000 000 meter

**Fontos**: A fejlec-cimkek gyakran felrevezetoek! Sok adatfajlban az "X" oszlop az Easting-et, az "Y" az Northing-ot tartalmazza -- de elofordul az ellenkezoje is. Az ertektartomany-alapu azonositas a megbizhato modszer:
- Ha egy ertek 0 es 400 000 kozott van: **Northing**
- Ha egy ertek 400 000 es 1 000 000 kozott van: **Easting**

Az AI kodgeneralo eszkozooket is erre kell "megtanitani" -- a prompt-ban mindig erdemes megadni: "A koordinatak EOV-ban vannak (EPSG:23700), a Northing 0--400k, az Easting 400k--1M."

### 19.10.3 Magyar terbeli adatforrasok

| Adatforras | Tipus | Hozzaaferes |
|------------|-------|-------------|
| Lechner ortofotok | Legifelvetel (0.2--0.4 m) | Korlatozottan nyilt |
| Copernicus DEM (GLO-30) | Domborzatmodelll (30 m) | Nyilt |
| Sentinel-2 | Muholdfelveetel (10 m) | Nyilt (Copernicus) |
| OpenStreetMap | Vektoros kozossegi terkep | Nyilt |
| MePAR | Mezogazdasagi parcellak | Korlatozottan nyilt |
| CORINE Land Cover | Felszinboritas | Nyilt (EEA) |
| LIDAR500 | LiDAR pontfelho | Korlatozottan nyilt |
| e-kataszter | Tulajdoni adatbazis | Korlatozott |

### 19.10.4 Debreceni GIS-kutatas

A Debreceni Egyetem szaamos terinformatikai kutatoocsoporttal rendelkezik:

- **Kornyezetgazdaalkodasi es Kornyezetpoolitikai Intezet**: Terbeli kornyezeti modellezes, vizgyujto-szintu elemzesek, talajviz-monitoring
- **Termanat Laboratorium**: Taverzekeelesi adatfeldolgoezaas, vegetaacio-monitoring, precizios mezogazdasag
- **Informatikai Kar**: Geoinformatikai szoftveerfejlesztes, terbeli adatbaazisok, webes terkepszolgaltatasok

A debreceni kutataaas kiemelt temateruleetei: az Alföld talajvizszint-valtoozaasainak monitoringja, a Hortobagyi Nemzeti Park vegetaciojaanak taverrzekeleesi elemzese, es a precizios mezogazdasagi alkalmazaaasok az Alföld agrarterlulletein.

---

## 19.11 Gyakorlati feladatok

### 19.11.1 Feladat: NDVI-terkep keszitese AI-val

**Cel**: Sentinel-2 felvetelbol NDVI (Normalized Difference Vegetation Index) terkepet kesziteni egy valasztott magyar teruletre.

**Eszkozok**: Claude vagy ChatGPT + Python (rasterio, matplotlib)

**Lepesek**:
1. Valassz egy teruletet (pl. Hortobaagy, Balaton-felvidek, Budapest agglomeraacioo)
2. Kerjedd az AI-t, hogy irjon Python-kodot a kovetkezo feladatokra:
   - Sentinel-2 L2A adatok letoltese a Copernicus Data Space-bol (vagy hasznalj egy mar letoltott minta-allomaaanyt)
   - B04 (voros) es B08 (NIR) savok beolvasaasa
   - NDVI szamitas: $NDVI = (NIR - Red) / (NIR + Red)$
   - Felhomaszkolas az SCL sav alapjan
   - Az eredmeny vizualizacioja matplotlib-tel
   - Mentes Cloud Optimized GeoTIFF-kent
3. Futtasd a kodot, es ertelmezd az eredmenyt: hol magas az NDVI (suiru vegetacio), hol alacsony (epitett terület, vizfelullet)?

**Bonusz**: Keszits ket idopont (pl. 2020 juulius es 2024 julius) NDVI-terkepeeet, es szamitsd ki a kulonbseget -- hol valtozott a vegetacioo?

### 19.11.2 Feladat: Terbeli lekerdezees termeszetes nyelven

**Cel**: Termeszetes nyelvu kerdesekbol PostGIS SQL-t generaaltatni.

**Eszkozok**: Claude vagy ChatGPT

**Lepesek**:
1. Definiald a kovetkezo adatbazis-semat az AI szamara:
   ```
   Tablak:
   - telepulesek (nev TEXT, lakos INTEGER, geom GEOMETRY, SRID 23700)
   - vizfolyasok (nev TEXT, tipus TEXT, geom GEOMETRY, SRID 23700)
   - natura2000 (terulet_nev TEXT, kod TEXT, geom GEOMETRY, SRID 23700)
   ```
2. Tedd fel a kovetkezo kerdeseket, es kerd az AI-t SQL-re forditasra:
   - "Melyik telepulesek vannak 10 km-en belul a Tiszatol?"
   - "Mekkora a Natura 2000 teruletek osszes kiterjedese Hajdu-Bihar megyeben hektarban?"
   - "Melyik a legkoozelebbi telepules a Hortobagyi Nemzeti Parkhoz, es milyen tavolsagra van?"
3. Ellenorizd a generalt SQL-t: helyes-e a CRS (EPSG:23700)? Hasznaalja-e az ST_Transform-ot, ha szukkseges? A teruletszamitas m2-ben joon, es elosztja-e 10000-rel a hektarhoz?

### 19.11.3 Feladat: Automatizalt terkepkeszites n8n-nel

**Cel**: n8n munkafolyamatot epiteni, amely automatikusan havi terkeeppet generaal.

**Eszkozok**: n8n (telepitett vagy felhoalapu) + Python

**Lepesek**:
1. Hozz letre egy n8n munkafolyamatot a kovetkezo node-okkal:
   - *Schedule Trigger*: minden honap elsejen
   - *HTTP Request*: STAC API lekerdezes a Sentinel-2 felvetelekert
   - *Code* (Python): NDVI szamitas es terkep generalas
   - *Email*: az eredmeny elkuldese
2. Teszteld a munkafolyamatot manuaalisan (a Schedule Trigger helyett Manual Trigger-rel)
3. Dokumentald a munkafolyamatot -- mentsd el, es exportald JSON-kent

### 19.11.4 Feladat: Kriging Python-ban AI segitseggel

**Cel**: Terbeli interpolaciot vegezni pontszeru adatokbol.

**Eszkozok**: Claude vagy ChatGPT + Python (pykrige, matplotlib)

**Lepesek**:
1. Keszits egy minta-adathalmazt: 20 fiktiv monitoring kut EOV koordinatakkal (Northing: 200000--260000, Easting: 700000--760000) es talajvizszint-ertekekkel (80--90 m aB. -- ahol "aB." = a Balti-tenger felett)
2. Kerd az AI-t, hogy irjon Python-kodot a kovetkezo feladatokra:
   - Empirikus variogram szamitasa es abrazolasa
   - Szferikus variogram-modell illesztese
   - Ordinary kriging futtatasa a `pykrige` konyvtarral
   - A kriging-eredmeny (becsolt ertek es kriging-variancia) vizualizacioja ket terkepen
3. Ertelmezd az eredmenyt: hol nagy a kriging-variancia (= hol bizonytalan a becsles)? Hova erdemes uj monitoring kutat telepiteni?

### 19.11.5 Feladat: AI agens terbeli elemzeshez

**Cel**: Egy egyszeru AI agenst epiteni, amely terbeli kerdesre terbeli elemzessel valaszol.

**Eszkozok**: Claude API (lasd 12. fejezet) + GeoPandas

**Lepesek**:
1. Definiaalj 3--4 "eszkoozt" (Python fuggvenyt), amelyet az agens hasznaalhat:
   - `load_layer(path)`: GeoPackage reteg betoltese
   - `buffer(gdf, distance)`: puffer generalasa
   - `spatial_join(gdf1, gdf2)`: terbeli join
   - `calculate_area(gdf)`: teruletszamitas hektarban
2. A 12. fejezetben tanult mintara epitvee keszits egy egyszeruu ReAct agenst, amely:
   - Megkapja a felhasznalo kerdeset (pl. "Hány epulet esik a Tisza 1 km-es puffeerzonajaaba?")
   - Gondolkodik: milyen retegekre van szuuukseg, milyen muveleteket kell vegezni
   - Cselekszik: meghivja a megfeleloo eszkozoket
   - Megfigyel: ellenorzi az eredmenyt
   - Valaszol
3. Teszteld a rendszert tobbfele kerdessel, es dokumentald a sikeres es sikertelen eseteket

---

## Összefoglalás

Ebben a fejezetben vegigjarttuk, hogyan hatja at az AI a terinformatika minden szegmenseeet:

- **Adatfeldolgozas** (19.2): A muholdkep-feldolgozas, a LiDAR-osztälyozas es a vektoros adattisztitas az AI altal nagyseagrendekkel felgyorsul
- **Kodgeneralas** (19.3): Az LLM-ek meggbiizhatoan generalnak ArcPy, QGIS Processing, GeoPandas, rasterio es PostGIS kodot -- a terinformatikus termeszetes nyelven fogalmazza meg a feladatot
- **Terbeli predikcioo** (19.4): A CNN-ek, a foundation modellek es a hibrid geostatisztikai modellek a felszinboritas-osztälyozastol a talajvizszint-becslesig forradalmasitjak a terbeli predikciot
- **Vizualis programozas** (19.5): A KNIME es az n8n a GIS-munkafolyamatokat vizualisan dokumentalttaa es automatizalttta teszik
- **Terbeli RAG** (19.6): A terbeli adatbazisok, metaadat-katalosgusok es jogszabalyi tudasbaazisok felett termeszetes nyelvu kerdesfelteves valik lehetovvee
- **3D GIS es digitalis ikrek** (19.7): A varosi es infrastrukturalis digitalis ikrek a kliimaadaptacio es a prediktiv karbantaartas eszkozei
- **Autonom GIS** (19.8): Az AI agensek a termeszetes nyelvu utasitasbol kinndulva onalloan tervezik es hajtjak vegre a terbeli elemzest
- **Felhoalapu GIS** (19.9): A Google Earth Engine, a Planetary Computer es a Copernicus Data Space a petabajtos adatarchivumok AI-alapu feldolgozaasat teszik lehetove
- **Magyar kontextus** (19.10): Az EOV koordinata-rendszer, a Lechner Kozpont, a MePAR es a magyar terbeli adatinfrastruktura a hazai alkalmazasok kerete

A terinformatika nem oncellu technologia -- a kornyezeti problemak megertesenek es kezeeleesenek egyik leghateekonyabb eszkozrendszere. Az AI ezt az eszkozrendszert tiz-szazszoros hatekonyeaggal erositi meg: amit korabban honapokig tartott, az ma napok alatti elvegeezheto. A kulcs azonban valtoozatlan: a terbeli gondolkodas, a kornyezeti szaktudas es az eredmenyek kritikus ertekeleese megmarad az ember feladataanak. Az AI nem helyettesiti a terinformatikust -- de az AI-t hasznaalo terinformatikus mar most hateekonyabb, mint a nelkuule dolgozo.

---

> **Ajanlott kovetkezo lepesek**:
> - Ha a kodgeneralast szeretned melyiteni: teerj vissza az **5. fejezethez**
> - Ha az agensek epiteese erdekel: a **12. fejezet** reszletes utmutaast nyuujt
> - Ha a RAG rendszert szeretned kiprobalni sajat terbeli adataiddal: a **9. fejezet** lepesrol lepesre bevezet
> - Ha a felhoalapu munkaakornyezetekrool szeretnel tobbet tudni: a **14. fejezet** a kiindulaspont
