# 13. fejezet — Saját programok és eszközök készítése

---

## 13.1 Nyitó jelenet: Amikor az elemzés zseniális, de senki nem tudja használni

Képzeld el a következő helyzetet.

Tóth András geokémikus vagy az ELTE-n. Az elmúlt hat hónapban egy fantasztikus Python-szkriptet írtál — pontosabban az AI kódolási asszisztenseddel íratod meg (ahogy az 5. fejezetben tanultad). A szkript betölti a terepi XRF-méréseid CSV-fájljait, automatikusan korrigálja a mátrixhatásokat, összeveti az adatokat a referenciaadatbázissal, és gyönyörű háromszögdiagramokat rajzol, amelyek azonnal megmutatják, melyik minta melyik kőzettípusba sorolható.

A szkript zseniális. A te gépeden.

Aztán bemutatod a csoport meetingjén, és a kollégáid szeme felcsillan. „Ezt nekem is kéne!" — mondja Eszter, a doktorandusz. „Meg tudod csinálni az én adataimra is?" — kérdezi a konzulensed. „Ez kéne a terepgyakorlathoz!" — szól Péter, a laborvezető.

Elküldöd nekik a szkriptet. Három nap múlva jön az első e-mail: „Nem tudtam telepíteni a pandas-t." Aztán a következő: „ModuleNotFoundError: No module named 'scipy'." Majd: „Milyen Python-verzió kell ehhez?" Végül: „Inkább küld el nekem CSV-ben az eredményeket."

Ez a pillanat minden kutatóval előfordul, aki valaha írt egy hasznos programot. A kód megvan, az eredmény megvan — de az utolsó mérföld, a „hogyan juttatom el a kollégáimhoz", az hiányzik.

Ez a fejezet pontosan erről szól. Nem arról, hogyan leszel szoftverfejlesztő. Arról, hogyan alakítod a már meglévő szkriptjeidet olyan eszközökké, amelyeket:

- **Bárki használhat** a csapatodban, Python nélkül, böngészőből
- **Bárki elérheti** a helyi hálózaton vagy az internetről
- **Akár egy AI is meghívhat** automatikusan, mint szolgáltatást

Három technológiát fogunk megismerni: a **Streamlit** webalkalmazás-keretrendszert, a **Gradio** interaktív interfész-építőt, és az **MCP-szervereket**, amelyekkel az adataidat és eszközeidet AI-hozzáférhetővé teheted.

---

## 13.2 Mikor van szükséged saját eszközre?

Mielőtt belevágunk a technikai részletekbe, érdemes átgondolni, mikor éri meg saját eszközt építeni, és mikor van egyszerűbb megoldás. Nem minden problémára kell webalkalmazást fejleszteni.

### Döntési ellenőrzőlista

Tedd fel magadnak ezeket a kérdéseket:

**1. Ismétlődik a feladat?**
Ha a kollégáid havonta, hetente vagy naponta kérik, hogy „futtasd le az elemzést az új adataikra", akkor érdemes eszközt építeni. Ha egyszer kérték, küld el nekik az eredményt.

**2. Többen használnák?**
Ha legalább 2-3 ember rendszeresen használná, megéri. Ha csak te magad, maradj a szkriptnél.

**3. A felhasználók telepítenének Python-t?**
Ha igen → maradj a szkriptnél, add hozzá egy README-t. Ha nem → Streamlit vagy Gradio webalkalmazás kell.

**4. Az adatok valós időben változnak?**
Ha igen (szenzor, műszer, monitoring) → Streamlit dashboard. Ha statikus fájlokkal dolgozol → Streamlit vagy Gradio egyaránt jó.

**5. Egy AI-nak is hozzá kellene férnie?**
Ha azt akarod, hogy a Claude, ChatGPT vagy más AI-eszköz automatikusan lekérdezze az adataidat → MCP-szerver.

**6. A felhasználónak interaktívan kell paramétert állítania?**
Ha csúszkákkal, legördülő menükkel akarod vezérelni az elemzést → Gradio különösen erős ebben.

### Az eszközválasztás összefoglalása

| Helyzet | Megoldás |
|---------|----------|
| Csak te használod, saját gépen | Maradj a Python-szkriptnél |
| 2-3 kolléga, adatfeltöltés és eredmény | **Streamlit** webalkalmazás |
| Valós idejű monitoring, dashboard | **Streamlit** dashboard |
| Modell vagy egyenlet interaktív felfedezése | **Gradio** interfész |
| AI-eszközöknek akarod elérhetővé tenni | **MCP-szerver** |
| Mindez egyszerre | Kombináld — ezek nem zárják ki egymást |

---

## 13.3 Streamlit: Python-szkriptből webalkalmazás 10 perc alatt

### Mi az a Streamlit?

A Streamlit egy Python-könyvtár, amellyel webalkalmazásokat hozhatsz létre **kizárólag Python-kóddal**. Nincs szükséged HTML-re, CSS-re, JavaScriptre vagy bármilyen webfejlesztési tudásra. Írsz egy Python-fájlt, lefuttatod a `streamlit run` paranccsal, és megnyílik a böngészőben egy interaktív webalkalmazás.

A Streamlit 2019-ben indult, 2022-ben a Snowflake felvásárolta, és azóta a tudományos közösség egyik legkedveltebb eszközévé vált. 2026-ban több mint 100 000 nyilvánosan elérhető Streamlit-alkalmazás fut a világon, és az akadémiai szférában különösen népszerű, mert:

- **Nulla webfejlesztési tudást igényel** — ha tudsz pandas-t használni, tudsz Streamlit-alkalmazást írni
- **Az adatmegjelenítés natív** — táblázatok, grafikonok, térképek beépítettek
- **Ingyenes hosting** — a Streamlit Community Cloud-on ingyen telepítheted
- **Az AI kódolási asszisztensek ismerik** — ha leírod, mit akarsz, a Claude vagy a Copilot megírja a Streamlit-kódot

### Telepítés

A Streamlit telepítése egyetlen parancs:

```bash
pip install streamlit
```

Ha az 5. fejezetben beállított Conda-környezetedet használod:

```bash
conda activate research
pip install streamlit
```

Ellenőrizd, hogy működik:

```bash
streamlit hello
```

Ez megnyit a böngészőben egy demó alkalmazást. Ha ezt látod, minden rendben.

### Az első Streamlit-alkalmazásod: „Hello, Labor!"

Mielőtt a komolyabb példákra térünk, nézzük meg a Streamlit alaplogikáját. Hozz létre egy fájlt `hello_labor.py` néven:

```python
import streamlit as st

st.title("Hello, Labor!")
st.write("Ez az első Streamlit alkalmazásom.")

nev = st.text_input("Mi a neved?")
if nev:
    st.write(f"Üdv, {nev}! Készen állsz a kutatásra.")

szam = st.slider("Válassz egy számot", 0, 100, 50)
st.write(f"A választott szám négyzete: {szam ** 2}")
```

Futtasd:

```bash
streamlit run hello_labor.py
```

A böngészőben megjelenik egy oldal címmel, szövegmezővel és csúszkával. Amikor módosítasz valamit, az alkalmazás automatikusan újrafut. Ez a Streamlit lényege: **minden interakció újrafuttatja a szkriptet felülről lefelé**, és a megváltozott bemenetekkel újra kirajzolja az oldalt.

Ez elsőre furcsának tűnhet, de pont ez teszi egyszerűvé: nem kell callback-eket írni, nem kell állapotot kezelni — csak írd a Python-kódot felülről lefelé, és a Streamlit megoldja a többit.

### A Streamlit legfontosabb elemei

Mielőtt a nagyobb példákra térnénk, itt egy áttekintés a leggyakrabban használt Streamlit-komponensekről:

**Bemenet (input):**
| Komponens | Kód | Mire jó |
|-----------|-----|---------|
| Szövegmező | `st.text_input("Címke")` | Név, fájlnév, keresőkifejezés |
| Szám | `st.number_input("Címke")` | Paraméter megadása |
| Csúszka | `st.slider("Címke", min, max, default)` | Tartomány kiválasztása |
| Legördülő | `st.selectbox("Címke", opciók)` | Módszer kiválasztása |
| Többes választás | `st.multiselect("Címke", opciók)` | Több oszlop kiválasztása |
| Jelölőnégyzet | `st.checkbox("Címke")` | Opció be/ki |
| Fájlfeltöltés | `st.file_uploader("Címke", type=["csv"])` | Adatfájl betöltése |

**Kimenet (output):**
| Komponens | Kód | Mire jó |
|-----------|-----|---------|
| Szöveg | `st.write(...)` | Bármi megjelenítése |
| Táblázat | `st.dataframe(df)` | Pandas DataFrame megjelenítése |
| Grafikon | `st.line_chart(df)` / `st.bar_chart(df)` | Egyszerű ábrák |
| Matplotlib | `st.pyplot(fig)` | Saját matplotlib-ábra |
| Metrika | `st.metric("Címke", érték, delta)` | KPI kártya |
| Letöltés | `st.download_button(...)` | Eredmény letöltése |

**Elrendezés:**
| Komponens | Kód | Mire jó |
|-----------|-----|---------|
| Oldalsáv | `st.sidebar.xyz()` | Beállítások oldalt |
| Oszlopok | `col1, col2 = st.columns(2)` | Egymás melletti elemek |
| Fülek | `tab1, tab2 = st.tabs(["A", "B"])` | Váltható nézetek |
| Kinyitható | `with st.expander("Részletek"):` | Elrejthető szekció |

Nem kell mindet megjegyezned — a lényeg, hogy tudd, ezek léteznek. Amikor az AI asszisztensednek leírod, mit akarsz („rakj egy csúszkát a mintaszám kiválasztásához az oldalsávba"), az ismeri ezeket az elemeket és beépíti a kódba.

---

### 13.3.1 Gyakorlati példa: Scientific Data Explorer

Most nézzük meg az első komolyabb alkalmazást. Ez egy általános adatfelfedező, amelybe a kollégáid feltölthetik a CSV-fájljaikat, és azonnal kapnak statisztikákat, grafikonokat és hipotézisvizsgálatot — mindezt anélkül, hogy egyetlen sor kódot írnának.

A teljes forráskód a könyv `examples/ch13_streamlit_gradio/01_data_explorer.py` fájljában található. Itt lépésről lépésre végigmegyünk a felépítésén.

#### 1. lépés: Alapbeállítás és fájlfeltöltés

```python
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Scientific Data Explorer", layout="wide")
st.title("Scientific Data Explorer")
st.markdown("Upload your CSV data and explore it — no coding required.")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv", "txt"])
```

Az `st.set_page_config` beállítja az oldal címét és az elrendezést (`layout="wide"` széles nézetben jeleníti meg, ami táblázatokhoz ideális). Az `st.file_uploader` egy drag-and-drop feltöltő mezőt rajzol, amely csak CSV- és TXT-fájlokat fogad el.

#### 2. lépés: Adat betöltése és áttekintés

```python
if uploaded_file is not None:
    sep = st.sidebar.selectbox("Separator", [",", ";", "\t", " "], index=0)
    df = pd.read_csv(uploaded_file, sep=sep)

    st.subheader(f"Dataset: {uploaded_file.name}")
    st.write(f"**{df.shape[0]} rows × {df.shape[1]} columns**")

    with st.expander("Preview Data", expanded=True):
        st.dataframe(df.head(50), use_container_width=True)
```

Figyeld meg a `st.sidebar.selectbox`-ot: az elválasztó karakter kiválasztása az oldalsávba kerül, hogy ne zavarja a fő tartalmat. Az `st.expander` egy kinyitható/becsukható szekciót hoz létre — a felhasználó dönthet, hogy látni akarja-e az adatokat vagy sem.

#### 3. lépés: Leíró statisztikák

```python
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

    st.subheader("Descriptive Statistics")
    if numeric_cols:
        st.dataframe(df[numeric_cols].describe().round(4),
                     use_container_width=True)
```

A `df.describe()` a pandas beépített függvénye, amely kiszámolja az átlagot, szórást, minimum/maximum értékeket és a kvartiliseket. Az `st.dataframe` ezt azonnal egy interaktív, rendezhető, kereshető táblázatként jeleníti meg.

#### 4. lépés: Vizualizáció

```python
    st.subheader("Quick Visualization")
    col1, col2 = st.columns(2)

    with col1:
        plot_type = st.selectbox("Plot type",
                                 ["Histogram", "Scatter", "Box Plot", "Line"])
    with col2:
        x_col = st.selectbox("X axis", numeric_cols, index=0)

    if plot_type == "Histogram":
        bins = st.slider("Bins", 5, 100, 30)
        st.bar_chart(df[x_col].value_counts(bins=bins).sort_index())

    elif plot_type == "Scatter":
        y_col = st.selectbox("Y axis", numeric_cols,
                             index=min(1, len(numeric_cols) - 1))
        st.scatter_chart(df, x=x_col, y=y_col)
```

Két oszlopos elrendezés (`st.columns(2)`) — balra a diagramtípus, jobbra a tengely kiválasztása. A felhasználó kattint, és a grafikon azonnal frissül.

#### 5. lépés: Korrelációs mátrix

```python
    if len(numeric_cols) >= 2:
        st.subheader("Correlation Matrix")
        corr = df[numeric_cols].corr().round(3)
        st.dataframe(
            corr.style.background_gradient(cmap="RdBu_r", vmin=-1, vmax=1),
            use_container_width=True
        )
```

Ez a szekció automatikusan megjelenik, ha legalább két numerikus oszlop van. A `background_gradient` színezi a cellákat: az erős pozitív korreláció piros, az erős negatív kék, a nulla fehér. Egy pillantás alatt látod a mintázatokat.

#### 6. lépés: Hipotézisvizsgálat

```python
    from scipy import stats

    col_a = st.selectbox("Group A", numeric_cols, index=0, key="ha")
    col_b = st.selectbox("Group B", numeric_cols,
                         index=min(1, len(numeric_cols) - 1), key="hb")

    test_type = st.radio("Test", ["t-test (independent)",
                                   "Mann-Whitney U",
                                   "Pearson correlation"])

    if test_type == "t-test (independent)":
        stat, p = stats.ttest_ind(data_a, data_b)
        st.write(f"t-statistic: **{stat:.4f}**, p-value: **{p:.4e}**")

    if p < 0.05:
        st.success(f"Statistically significant (p = {p:.4e} < 0.05)")
    else:
        st.info(f"Not statistically significant (p = {p:.4e} >= 0.05)")
```

Ez talán a legértékesebb rész egy kutató számára. A felhasználó kiválaszt két oszlopot, egy statisztikai tesztet, és azonnal megkapja az eredményt, zöld pipával (szignifikáns) vagy kék információs jelzéssel (nem szignifikáns). Nincs szükség R-re, SPSS-re vagy kézi számolásra.

#### 7. lépés: Eredmény letöltése

```python
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("Download processed CSV", csv,
                       "processed_data.csv", "text/csv")
```

Egy gomb, egy kattintás, és a feldolgozott adat letölthető. Ez fontos: a felhasználók szeretik, ha az eredményt ki tudják vinni az alkalmazásból.

#### Az alkalmazás futtatása

Mentsd el a fájlt, futtasd:

```bash
streamlit run 01_data_explorer.py
```

A terminálban megjelenik egy cím, például `http://localhost:8501`. Nyisd meg a böngészőben, húzz rá egy CSV-fájlt, és kész. Ezt a linket elküldheted a kollégáidnak is, ha ugyanazon a hálózaton vagytok — erről a 13.3.3 fejezetben lesz szó.

> **Tipp:** Az egész alkalmazás ~120 sor Python. Ha az 5. fejezetben megtanult módon a Claude Code-dal vagy a GitHub Copilot-tal íratod, a promptod ennyiből áll: *„Készíts egy Streamlit alkalmazást, amelybe CSV-t lehet feltölteni, és automatikusan leíró statisztikákat, grafikonokat és hipotézisvizsgálatot ad."* Percek alatt megkapod a kész kódot.

---

### 13.3.2 Gyakorlati példa: Szenzor Dashboard

A második Streamlit-alkalmazás egy egészen más felhasználási esetet mutat be: **valós idejű monitoring dashboardot**. Ez nem adatfeltöltésről szól, hanem élő adatok folyamatos megjelenítéséről.

Mikor van erre szükséged?

- **Laboreszköz-monitoring:** Hőmérséklet, páratartalom, nyomás a klímatizált szobában
- **Terepi állomás:** Vízszint, csapadék, szélsebesség
- **Kísérleti berendezés:** Reaktor hőmérséklete, áramlási sebesség, koncentráció
- **Üvegházi monitoring:** Hőmérséklet, fényintenzitás, CO₂-szint, talajnedvesség

A teljes kód az `examples/ch13_streamlit_gradio/03_sensor_dashboard.py` fájlban található. A demonstrációs verzió szimulált adatokat használ, de a kódban megjegyzésben megmutatjuk, hogyan cserélheted ki valós adatforrásra.

#### Az adatforrás cseréje

A példakód egy `get_sensor_data()` függvényt definiál, amelyet a `@st.cache_data(ttl=5)` dekorátorral lát el — ez 5 másodpercenként frissíti az adatokat. A szimulált adatokat egyetlen sor módosításával cserélheted valósra:

```python
@st.cache_data(ttl=5)  # 5 másodpercenként frissít
def get_sensor_data():
    # Szimulált verzió (töröld és cseréld valamelyikre):

    # CSV-fájlból:
    # return pd.read_csv("latest_sensor_data.csv")

    # SQL-adatbázisból:
    # return pd.read_sql(
    #     "SELECT * FROM sensor_readings ORDER BY timestamp DESC LIMIT 200",
    #     conn
    # )

    # REST API-ból:
    # return pd.DataFrame(
    #     requests.get("https://your-api/sensors/latest").json()
    # )

    # MQTT-szenzorfolyamból:
    # (paho-mqtt kliens használata)
```

A lényeg: a dashboard logikája (KPI kártyák, grafikonok, riasztások) ugyanaz marad, akárhonnan jönnek az adatok. Csak az adatforrást kell kicserélni.

#### KPI kártyák

```python
col1, col2, col3, col4 = st.columns(4)

latest = df.iloc[-1]
prev = df.iloc[-2]

col1.metric("Temperature",
            f"{latest['temperature_C']:.1f} °C",
            f"{latest['temperature_C'] - prev['temperature_C']:.2f} °C")

col2.metric("Humidity",
            f"{latest['humidity_pct']:.1f} %",
            f"{latest['humidity_pct'] - prev['humidity_pct']:.2f} %")
```

Az `st.metric` komponens egy nagy számot jelenít meg az aktuális értékkel, alatta egy kis nyíllal, amely megmutatja a változás irányát (felfelé/lefelé) az előző méréshez képest. Négy ilyen kártya egymás mellett — egy pillantás alatt látod a rendszer állapotát.

#### Riasztások

```python
alerts = []
if latest["temperature_C"] > alert_temp:
    alerts.append(f"Temperature ({latest['temperature_C']:.1f}°C) "
                  f"exceeds threshold ({alert_temp}°C)")

if alerts:
    for alert in alerts:
        st.error(f"ALERT: {alert}")
else:
    st.success("All readings within normal range.")
```

A riasztási küszöbértékeket a felhasználó az oldalsávban állíthatja csúszkákkal. Ha valamelyik szenzor meghaladja a küszöböt, piros figyelmeztető doboz jelenik meg. Ha minden rendben van, zöld „minden OK" üzenet látható.

#### Idősoros diagramok

```python
tab1, tab2, tab3, tab4 = st.tabs(["Temperature", "Humidity",
                                    "Pressure", "CO₂"])

with tab1:
    st.line_chart(df.set_index("timestamp")["temperature_C"])
with tab2:
    st.line_chart(df.set_index("timestamp")["humidity_pct"])
```

Füles elrendezés — a felhasználó kattintással válthat a különböző szenzorok idősoros grafikonjai között. Az `st.line_chart` automatikusan kezeli az x tengely időformázását.

#### Automatikus frissítés

A `@st.cache_data(ttl=5)` biztosítja, hogy az adatok 5 másodpercenként frissüljenek. A felhasználó az oldalsávban állíthatja a frissítési gyakoriságot (5, 10, 30, 60 másodperc). Az oldal alján megjelenik az utolsó frissítés időpontja.

> **Fontos:** Ezzel a dashboarddal már majdnem digitális árnyéknál tartunk — ahogy a 10. fejezetben láttuk, a digitális ikrek hierarchiájában ez a második szint. Ha visszacsatolást is építesz bele (pl. a riasztás alapján automatikusan módosít egy beállítást), akkor digitális ikerré válik.

---

### 13.3.3 Streamlit-alkalmazás megosztása a csapatoddal

Megírtad az alkalmazást, fut a gépeden — de hogyan juttatod el a kollégáidhoz? Három megoldás van, egyre szélesebb körre.

#### 1. módszer: Helyi hálózat (legegyszerűbb)

Ha te és a kollégáid ugyanazon a hálózaton vagytok (egyetemi hálózat, irodai WiFi), egyetlen plusz flag elég:

```bash
streamlit run 01_data_explorer.py --server.address 0.0.0.0
```

A `--server.address 0.0.0.0` azt jelenti, hogy az alkalmazás nemcsak a te gépedről, hanem a hálózat bármely gépéről elérhető. A terminálban megjelenik valami ilyesmi:

```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.1.42:8501
```

A „Network URL"-t küld el a kollégáidnak. Ők a böngészőjükbe beírják, és ugyanazt az alkalmazást látják, mint te — Python telepítése nélkül.

**Korlátai:** A te gépednek bekapcsolva kell lennie. Ha leállítod a Streamlit-et, az alkalmazás elérhetetlenné válik. VPN-en keresztül általában nem működik.

#### 2. módszer: Streamlit Community Cloud (ingyen, nyilvános)

A Streamlit Community Cloud egy ingyenes hosting szolgáltatás, amellyel a GitHub-repódban lévő Streamlit-alkalmazásokat egy kattintással telepítheted az internetre.

A lépések:

1. **Hozz létre egy GitHub-repót** az alkalmazásoddal (erről a 13.6 fejezetben részletesen is lesz szó)
2. A repóban legyen egy `requirements.txt` fájl a függőségekkel:
   ```
   streamlit
   pandas
   scipy
   matplotlib
   ```
3. Menj a [share.streamlit.io](https://share.streamlit.io) oldalra
4. Jelentkezz be a GitHub-fiókoddal
5. Válaszd ki a repót, a branchet és a fő Python-fájlt
6. Kattints a „Deploy" gombra

Pár perc múlva kapsz egy publikus URL-t, például:
```
https://your-username-data-explorer-01-data-explorer-abc123.streamlit.app
```

Ezt a linket bárki megnyithatja a világon. Ingyenes, korlátlan ideig fut, és a GitHub-repó frissítésekor automatikusan újratelepíti magát.

**Korlátai:** Az alkalmazás publikus (bárki láthatja). Az ingyenes szinten korlátozott az erőforrás (1 GB RAM, lassú CPU). Ha érzékeny adatokkal dolgozol, használd a helyi hálózatos megoldást vagy a Streamlit Teams fizetős verzióját.

#### 3. módszer: Egyetemi/intézeti szerver

Ha van egy szervered (akár egy régi PC, akár egy felhőben bérelt gép), a Streamlit-et háttérfolyamatként futtathatod:

```bash
nohup streamlit run 01_data_explorer.py \
    --server.port 8501 \
    --server.address 0.0.0.0 \
    > streamlit.log 2>&1 &
```

Ez elindul, és akkor is fut, ha kijelentkezel a szerverről. A `nohup` biztosítja, hogy ne álljon le, amikor bezárod a terminált.

Egy lépéssel tovább mehetsz, ha az intézeti IT-vel kérsz egy aldomain-t (pl. `data-explorer.geokemia.elte.hu`) és egy reverse proxy-t (nginx vagy Apache) — ezt az IT-s kollégák 5 perc alatt beállítják, és máris egy „rendes" URL-en érhető el az alkalmazásod.

---

## 13.4 Gradio: Interaktív felületek modellekhez és egyenletekhez

### Mi a Gradio, és mikor válaszd a Streamlit helyett?

A Gradio a Hugging Face által karbantartott Python-könyvtár, amellyel szintén webes felületeket építhetsz Python-kóddal. Első pillantásra hasonlít a Streamlit-re, de a filozófiája más.

| Szempont | Streamlit | Gradio |
|----------|-----------|--------|
| **Fókusz** | Általános adatalkalmazás, dashboard | Modell-interfész, bemenet-kimenet párok |
| **Felépítés** | Szkript felülről lefelé | Függvény + bemenetek + kimenetek |
| **Interaktivitás** | Újrafuttatja az egész szkriptet | Csak a megadott függvényt hívja |
| **Csúszkák/paraméterek** | Kézzel definiálod | Automatikusan generálja a függvényparaméterekből |
| **Sharing** | Streamlit Cloud | `share=True` → ideiglenes publikus URL |
| **ML-modell integráció** | Lehetséges, de több munka | Natív Hugging Face integráció |
| **Ideális felhasználás** | Dashboard, adatfeltöltés, monitoring | Modell tesztelése, egyenlet vizsgálata, demo |

**Hüvelykujjszabály:** Ha az alkalmazásod lényege „tölts fel adatot, nézd meg az eredményt, böngéssz" → Streamlit. Ha az alkalmazásod lényege „állíts be paramétereket, nézd meg, mi változik" → Gradio.

### Telepítés

```bash
pip install gradio
```

### A Gradio alaplogikája

A Gradio alapötlete rendkívül egyszerű: van egy **Python-függvényed**, van hozzá **bemenet** (szövegmező, csúszka, fájl) és **kimenet** (szöveg, kép, ábra). A Gradio automatikusan generál egy webes felületet, ahol a felhasználó kitölti a bemeneteket, megnyomja a „Submit" gombot, és megkapja a kimenetet.

```python
import gradio as gr

def koszont(nev):
    return f"Üdvözöllek, {nev}! Készen állsz a kutatásra?"

demo = gr.Interface(
    fn=koszont,
    inputs=gr.Textbox(label="A neved"),
    outputs=gr.Textbox(label="Üdvözlés"),
    title="Labor Üdvözlő"
)

demo.launch()
```

Ez az öt sor létrehoz egy webes felületet szövegmezővel, gombbal és eredménnyel. A `demo.launch()` elindítja a helyi webszervert, és megnyitja a böngészőt.

### A Gradio legfontosabb elemei

**Bemeneti komponensek:**
| Komponens | Kód | Mire jó |
|-----------|-----|---------|
| Szövegmező | `gr.Textbox()` | Egyenlet, prompt, fájlnév |
| Csúszka | `gr.Slider(min, max, value, step)` | Paraméter |
| Szám | `gr.Number()` | Pontosérték |
| Legördülő | `gr.Dropdown(choices=[...])` | Módszer kiválasztása |
| Jelölőnégyzet | `gr.Checkbox()` | Opció be/ki |
| Fájl | `gr.File()` | Fájl feltöltése |
| Kép | `gr.Image()` | Képfeltöltés |

**Kimeneti komponensek:**
| Komponens | Kód | Mire jó |
|-----------|-----|---------|
| Szöveg | `gr.Textbox()` | Szöveges eredmény |
| Markdown | `gr.Markdown()` | Formázott eredmény |
| Ábra | `gr.Plot()` | Matplotlib/Plotly ábra |
| Kép | `gr.Image()` | Generált kép |
| Fájl | `gr.File()` | Letölthető eredmény |
| DataFrame | `gr.DataFrame()` | Táblázat |

---

### 13.4.1 Gyakorlati példa: Equation Plotter interaktív csúszkákkal

Ez a példa a Gradio erejét mutatja be: a felhasználó beír egy matematikai egyenletet, csúszkákkal állítja a paramétereket, és azonnal látja a grafikont és a függvény tulajdonságait.

A teljes kód a könyv `examples/ch13_streamlit_gradio/02_equation_solver.py` fájljában található. Nézzük meg a kulcselemeket.

#### A központi függvény

```python
def solve_and_plot(equation_str, x_min, x_max, num_points,
                   param_a, param_b, param_c):
    """Parse and plot a mathematical equation with parameters a, b, c."""
    x = np.linspace(x_min, x_max, int(num_points))
    a, b, c = param_a, param_b, param_c

    safe_dict = {
        "x": x, "a": a, "b": b, "c": c,
        "sin": np.sin, "cos": np.cos, "tan": np.tan,
        "exp": np.exp, "log": np.log, "log10": np.log10,
        "sqrt": np.sqrt, "abs": np.abs,
        "pi": np.pi, "e": np.e,
        "np": np,
    }
    y = eval(equation_str, {"__builtins__": {}}, safe_dict)
```

A függvény kap egy egyenlet-sztringet (pl. `"a * sin(b * x) + c"`) és hat numerikus paramétert. A `safe_dict` biztosítja, hogy a felhasználó csak matematikai műveleteket használhasson — nincs rendszerhozzáférés, nincs fájlkezelés. Az `eval` kiértékeli az egyenletet a megadott paraméterekkel.

#### Az interfész összeállítása

```python
demo = gr.Interface(
    fn=solve_and_plot,
    inputs=[
        gr.Textbox(
            value="a * sin(b * x) + c",
            label="Equation (use x, a, b, c, sin, cos, exp, log, sqrt, pi, e)",
        ),
        gr.Slider(-20, 0, value=-10, label="x min"),
        gr.Slider(0, 20, value=10, label="x max"),
        gr.Slider(50, 2000, value=500, step=50, label="Number of points"),
        gr.Slider(-10, 10, value=1, step=0.1, label="Parameter a"),
        gr.Slider(-10, 10, value=2, step=0.1, label="Parameter b"),
        gr.Slider(-10, 10, value=0, step=0.1, label="Parameter c"),
    ],
    outputs=[
        gr.Plot(label="Plot"),
        gr.Markdown(label="Properties"),
    ],
    title="Equation Plotter & Solver",
    examples=[
        ["a * x**2 + b * x + c", -5, 5, 500, 1, -2, -3],
        ["a * exp(-b * x**2)", -5, 5, 500, 1, 0.5, 0],
        ["a * sin(b * x) * exp(-c * abs(x))", -10, 10, 1000, 1, 3, 0.1],
        ["a / (1 + exp(-b * (x - c)))", -10, 10, 500, 1, 1, 0],
    ],
)
```

Figyeld meg a felépítést:

- **Egy függvény** (`solve_and_plot`) — ez tartalmazza az összes logikát
- **Bemenetek listája** — a Gradio automatikusan generálja a szövegmezőt és a csúszkákat
- **Kimenetek listája** — egy ábra és egy Markdown szöveges összefoglaló
- **Példák** — előre definiált paraméter-kombinációk, amelyekre kattintva a felhasználó azonnal kipróbálhatja az alkalmazást

#### Automatikus zérushelykeresés

```python
    # Find zeros (sign changes)
    sign_changes = np.where(np.diff(np.sign(y)))[0]
    if len(sign_changes) > 0:
        zeros = [f"{x[i]:.4f}" for i in sign_changes[:10]]
        info += f"\n**Approximate zeros:** {', '.join(zeros)}"
```

Ez egy csinos extra: a függvény automatikusan megkeresi az egyenlet közelítő zérushelyeit (ahol a függvény előjelet vált), és kiírja az eredmények közé. A kutatónak nem kell külön kérnie — egyszerűen megkapja.

#### Futtatás

```bash
python 02_equation_solver.py
```

Megnyílik a böngészőben (alapértelmezetten `http://localhost:7860`), és azonnal használható.

#### Azonnali publikus megosztás

A Gradio egyik legnagyobb előnye a Streamlit-tel szemben: egyetlen paramétert módosítva ideiglenes publikus URL-t kapsz, amely 72 óráig elérhető:

```python
demo.launch(share=True)
```

A terminálban megjelenik valami ilyesmi:

```
Running on public URL: https://abc123def456.gradio.live
```

Ezt a linket bárki megnyithatja a világon, Python telepítése nélkül. Ideális konferencia-demóhoz, témavezetői megbeszéléshez, vagy ha gyorsan meg akarod mutatni valakinek az eredményt.

---

### 13.4.2 Gyakorlati példa: Modell-inferencia felület

Az Equation Plotter egy általános matematikai eszköz volt. De a Gradio igazi ereje akkor mutatkozik meg, amikor egy gépi tanulási modellt csomagolsz be felhasználóbarát felülettel.

Képzeld el, hogy betanítottál egy modellt, amely mikroszkópos képek alapján osztályozza a kőzettípust. A modell egy `.pkl` vagy `.pt` fájl. A kollégáid nem fogják megtanulni, hogyan kell betölteni és futtatni — de ha van egy weboldaluk, ahova feltöltik a képet és megkapják az eredményt, azt használni fogják.

Íme egy példa egy képosztályozó Gradio-felületre:

```python
import gradio as gr
import numpy as np

# A modell betöltése (itt egy egyszerűsített példa)
# A valóságban: model = torch.load("rock_classifier.pt")
# vagy: model = joblib.load("rock_classifier.pkl")

def classify_rock(image):
    """Kőzettípus osztályozása mikroszkópos kép alapján."""
    # A valóságban itt fut a modell-inferencia
    # predictions = model.predict(preprocess(image))

    # Demonstrációs eredmény:
    results = {
        "Gránit": 0.72,
        "Bazalt": 0.15,
        "Andezit": 0.08,
        "Riolit": 0.05,
    }
    return results

demo = gr.Interface(
    fn=classify_rock,
    inputs=gr.Image(type="numpy", label="Mikroszkópos kép"),
    outputs=gr.Label(num_top_classes=4, label="Osztályozás"),
    title="Kőzettípus Osztályozó",
    description="Tölts fel egy mikroszkópos vékonycsiszolat-képet, "
                "és a modell megadja a valószínű kőzettípust.",
    examples=["example_granite.jpg", "example_basalt.jpg"],
)

demo.launch()
```

A `gr.Image` bemenetnél a felhasználó feltölt egy képet (drag-and-drop vagy fájlválasztó). A `gr.Label` kimenetnél egy szép sávdiagram jelenik meg a valószínűségekkel. Az egész összesen 20 sor kód.

Ez a minta alkalmazható bármilyen modellre:

- **Spektrum-osztályozó:** Feltölt egy spektrumfájlt → kap egy anyag-azonosítást
- **Idősor-előrejelző:** Feltölt történeti adatot → kap egy előrejelzést grafikonnal
- **Szöveg-elemző:** Beír egy szöveget → kap entitásfelismerést, téma-osztályozást
- **Anomália-detektor:** Feltölt szenzor-adatot → kap egy riasztást vagy „normális" jelzést

A Gradio Hugging Face Spaces-en is telepíthető ingyen, ami különösen akkor hasznos, ha a modelled is a Hugging Face-en van.

---

## 13.5 MCP-szerverek: Az adataid és eszközeid AI-hozzáférhetővé tétele

### Mi az az MCP?

Az MCP (Model Context Protocol) egy nyílt szabvány, amelyet az Anthropic 2024-ben publikált. A legegyszerűbb analógia: **az MCP az USB-csatlakozó az AI-eszközök világában**.

Gondolj bele: az USB előtt minden perifériához (nyomtató, billentyűzet, egér, kamera) más kábel és más illesztőprogram kellett. Az USB szabványosította a csatlakozást — egy kábel, egy csatlakozó, és minden működik.

Az MCP ugyanezt teszi az AI-eszközök számára. Ahelyett, hogy minden AI-hoz (Claude, ChatGPT, Copilot) külön integrációt írnál, egyszer létrehozol egy MCP-szervert, és bármely MCP-kompatibilis AI-eszköz automatikusan felfedezi és használja az adataidat és eszközeidet.

### Mit tud egy MCP-szerver?

Három dolgot:

1. **Erőforrásokat kínál (Resources):** „Ezek az adatok elérhetők" — adatbázis-táblák, fájlok, mérési eredmények
2. **Eszközöket kínál (Tools):** „Ezeket a műveleteket végre tudom hajtani" — adatlekérdezés, számítás futtatása, fájl létrehozása
3. **Biztonságosan kommunikál (Transport):** Szabványos kérések, hitelesítés, hibakezelés

Az AI-eszköz (pl. Claude Code) automatikusan felfedezi, hogy a szervered mit tud, és természetes nyelvi parancsokra hívja meg a megfelelő eszközt.

### Miért érdekes ez egy kutatónak?

Képzeld el a következő helyzetet: van egy SQLite-adatbázisod 10 év terepi mérési adatával. Amikor a Claude Code-ban dolgozol, szeretnéd megkérdezni:

> „Melyik mintavételi helyen volt a legmagasabb ólomkoncentráció 2023-ban?"

MCP-szerver nélkül: ki kell másolnod az adatokat, be kell illesztened a chatbe, vagy SQL-lekérdezéseket kell írnod.

MCP-szerverrel: a Claude Code közvetlenül lekérdezi az adatbázist, és természetes nyelven válaszol.

### Egyszerű példa: Adatbázis mint MCP-szerver

Az alábbi példa egy minimális MCP-szervert mutat be, amely egy SQLite-adatbázist tesz elérhetővé AI-eszközök számára. A szerver az `mcp` Python-könyvtárat használja:

```bash
pip install mcp
```

A szerver kódja:

```python
from mcp.server.fastmcp import FastMCP
import sqlite3

# MCP-szerver létrehozása
mcp = FastMCP("Research Database")

# Adatbázis-kapcsolat
DB_PATH = "field_measurements.db"

@mcp.tool()
def query_measurements(sql: str) -> str:
    """Execute a read-only SQL query on the field measurements database.

    The database has these tables:
    - samples (id, site_name, date, latitude, longitude)
    - measurements (id, sample_id, element, concentration_ppm, method)
    - sites (name, region, geology, description)

    Only SELECT queries are allowed.
    """
    if not sql.strip().upper().startswith("SELECT"):
        return "Error: Only SELECT queries are allowed."

    conn = sqlite3.connect(DB_PATH)
    try:
        cursor = conn.execute(sql)
        columns = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        # Formázott eredmény
        result = " | ".join(columns) + "\n"
        result += "-" * 40 + "\n"
        for row in rows:
            result += " | ".join(str(v) for v in row) + "\n"
        return result
    except Exception as e:
        return f"SQL Error: {e}"
    finally:
        conn.close()

@mcp.tool()
def list_tables() -> str:
    """List all tables and their columns in the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table'"
    )
    tables = cursor.fetchall()
    result = []
    for (table,) in tables:
        cols = conn.execute(f"PRAGMA table_info({table})").fetchall()
        col_names = [c[1] for c in cols]
        result.append(f"{table}: {', '.join(col_names)}")
    conn.close()
    return "\n".join(result)

@mcp.tool()
def get_summary_stats(table: str, column: str) -> str:
    """Get summary statistics (count, mean, min, max, std)
    for a numeric column."""
    conn = sqlite3.connect(DB_PATH)
    try:
        stats = conn.execute(f"""
            SELECT
                COUNT({column}) as count,
                AVG({column}) as mean,
                MIN({column}) as min,
                MAX({column}) as max,
                STDEV({column}) as std
            FROM {table}
        """).fetchone()
        return (f"Count: {stats[0]}, Mean: {stats[1]:.4f}, "
                f"Min: {stats[2]}, Max: {stats[3]}, Std: {stats[4]}")
    except Exception as e:
        return f"Error: {e}"
    finally:
        conn.close()

if __name__ == "__main__":
    mcp.run()
```

Ez a szerver három eszközt kínál:
- `query_measurements` — tetszőleges SELECT lekérdezés futtatása
- `list_tables` — az adatbázis struktúrájának listázása
- `get_summary_stats` — leíró statisztikák egy oszlopra

A `@mcp.tool()` dekorátor és a docstring a lényeg: az AI-eszköz a docstring alapján érti meg, mire való az eszköz és hogyan kell használni. Nem kell API-dokumentációt írni — a docstring maga az API-leírás.

### Csatlakoztatás Claude Code-hoz

Miután a szervered kész, csatlakoztatnod kell a Claude Code-hoz. Ehhez egy konfigurációs fájl szükséges. Hozd létre a projekt gyökérkönyvtárában a `.mcp.json` fájlt:

```json
{
  "mcpServers": {
    "research-db": {
      "command": "python",
      "args": ["mcp_server.py"],
      "cwd": "/path/to/your/project"
    }
  }
}
```

Ezután, amikor a Claude Code-ban megnyitod a projektet, automatikusan elindul az MCP-szerver, és természetes nyelven kérdezhetsz:

- *„Melyik helyszínen volt a legmagasabb ólomkoncentráció?"*
- *„Készíts egy összefoglalót a 2023-as mérésekről régiónként."*
- *„Van-e szignifikáns különbség az északi és a déli minták cinkkoncentrációjában?"*

A Claude Code meghívja a megfelelő MCP-eszközt, megkapja az adatot, és természetes nyelven válaszol.

### Csatlakoztatás VS Code-hoz (Copilot)

Ha a VS Code-ban a GitHub Copilot-tal dolgozol, az MCP-szerver konfigurációja hasonló. A VS Code `settings.json` fájljába kell felvenni:

```json
{
  "mcp": {
    "servers": {
      "research-db": {
        "command": "python",
        "args": ["mcp_server.py"]
      }
    }
  }
}
```

A Copilot Chat Agent Mode-ban (a `@` karakter használatával) ezután közvetlenül eléred az MCP-szervered eszközeit.

### Csatlakoztatás Cursor-hoz

A Cursor szintén támogatja az MCP-szervereket. A projekt gyökerében hozd létre a `.cursor/mcp.json` fájlt:

```json
{
  "mcpServers": {
    "research-db": {
      "command": "python",
      "args": ["mcp_server.py"]
    }
  }
}
```

A logika mindenhol ugyanaz: egyszer megírod a szervert, és bármely MCP-kompatibilis AI-eszközből eléred.

### Helyi vs. távoli MCP-szerverek

Az eddigi példánk **helyi** (local) MCP-szerver volt — a te gépeden fut. Ez tökéletes prototípushoz és egyéni munkához. De ha a csapatod minden tagja el akarja érni ugyanazt az adatbázist, két megoldás van:

**Helyi szerver (local):**
- A te gépeden fut
- Csak te éred el
- Titkok (jelszavak, API-kulcsok) a gépeden maradnak
- Nem kell hálózat
- Ideális: egyéni kutatómunka, prototípus

**Távoli szerver (remote):**
- Egy központi szerveren fut (egyetemi szerver, felhő)
- Mindenki eléri, aki jogosult
- Központi hitelesítés és naplózás
- Stabil hálózat szükséges
- Ideális: csapatmunka, megosztott adatbázis

A távoli MCP-szerver konfigurálása annyit jelent, hogy a `command` és `args` helyett egy URL-t adsz meg:

```json
{
  "mcpServers": {
    "research-db": {
      "url": "https://mcp.geokemia.elte.hu/research-db",
      "headers": {
        "Authorization": "Bearer ${MCP_TOKEN}"
      }
    }
  }
}
```

### Biztonsági szempontok

Az MCP-szervereknél mindig gondolj a biztonságra:

1. **Csak olvasási hozzáférés:** A fenti példában a `query_measurements` csak SELECT lekérdezéseket engedélyez. Soha ne adj írási hozzáférést, hacsak nem szándékos.
2. **Hitelesítés:** Távoli szervereknél mindig használj tokenalapú hitelesítést.
3. **Jóváhagyás:** A Claude Code és a VS Code is kér megerősítést, mielőtt egy MCP-eszközt először meghív — mindig nézd meg, mit fog csinálni.
4. **Naplózás:** Tartsd számon, ki mikor mit kérdezett — ez kutatási etikai szempontból is fontos.

### Gyakorlati ötletek MCP-szerverekre

Néhány ötlet, hogyan teheted AI-hozzáférhetővé a kutatási infrastruktúrádat:

| Adatforrás | MCP-szerver funkció |
|-----------|-------------------|
| SQLite/PostgreSQL mérési adatbázis | SQL lekérdezések, statisztikák |
| CSV-fájlok mappája | Fájllistázás, oszlopinformáció, szűrt letöltés |
| Laborjegyzetkönyv (Markdown/JSON) | Keresés, dátum szerinti szűrés |
| Meteorológiai API | Időjárás-lekérdezés adott helyre és időszakra |
| Műszer-logfájlok | Utolsó mérés, hibakeresés, állapot-ellenőrzés |
| Irodalomjegyzék (BibTeX) | Referencia-keresés, idézet formázása |

---

## 13.6 Megosztás GitHub-on dokumentációval

Megírtad az alkalmazásodat (Streamlit, Gradio, vagy MCP-szerver) — most hogyan juttatod el a világba? A legjobb módszer: **tedd fel GitHub-ra**, és adj hozzá egy egyszerű dokumentációt.

### Miért GitHub?

- A kollégáid egyetlen paranccsal letölthetik: `git clone`
- A Streamlit Community Cloud közvetlenül GitHub-repóból telepít
- A kód verziózott — ha elrontasz valamit, visszaállítható
- A `README.md` fájl automatikusan megjelenik a repó főoldalán
- Ha publikálsz cikket, hivatkozhatsz a repóra

### A minimális projekt-struktúra

Egy jól megosztható projekt így néz ki:

```
my-data-explorer/
├── README.md              # Mit csinál, hogyan kell futtatni
├── requirements.txt       # Függőségek listája
├── app.py                 # A fő alkalmazás
├── mcp_server.py          # (opcionális) MCP-szerver
├── .gitignore             # Amit NEM kell feltölteni
└── example_data/          # (opcionális) Tesztadatok
    └── sample.csv
```

### A README.md tartalma

A README az első dolog, amit a felhasználó lát. Legyen rövid, konkrét és másolható:

```markdown
# Scientific Data Explorer

Upload a CSV, get instant statistics, plots, and hypothesis tests.

## Quick Start

```bash
pip install -r requirements.txt
streamlit run app.py
```

Then open http://localhost:8501 in your browser.

## Features

- Descriptive statistics for all numeric columns
- Histograms, scatter plots, box plots, correlation matrix
- t-test, Mann-Whitney U, Pearson correlation
- CSV download

## Requirements

- Python 3.9+
- See requirements.txt
```

A lényeg: valaki, aki először látja a repót, **30 másodpercen belül futtatni tudja** az alkalmazást.

### A requirements.txt

Ez a fájl felsorolja a Python-függőségeket:

```
streamlit>=1.30
pandas>=2.0
scipy>=1.10
matplotlib>=3.7
numpy>=1.24
```

A `>=` jelölés azt jelenti, hogy legalább ennyi kell, de a legfrissebb is jó. Ez rugalmasabb, mint ha pontos verziót adnál meg.

### A .gitignore

Ez a fájl megmondja a Git-nek, mit **ne** töltsön fel. Kutatási projektekhez:

```
__pycache__/
*.pyc
.env
*.db
*.sqlite
data/          # Nagy adatfájlok ne kerüljenek a repóba
.DS_Store
*.tmp
```

Fontos: **soha ne tölts fel jelszavakat, API-kulcsokat, vagy érzékeny adatokat** a GitHub-ra. Ha az adatbázisod jelszóval védett, a jelszót `.env` fájlban tárold, és a `.gitignore`-ba vedd fel.

### Feltöltés GitHub-ra

Ha még nincs GitHub-fiókod, regisztrálj a [github.com](https://github.com)-on (ingyenes). Ezután:

```bash
cd my-data-explorer
git init
git add -A
git commit -m "Initial commit: data explorer app"
```

A GitHub weboldalán hozz létre egy új repót (New Repository), és kövesd az utasításokat:

```bash
git remote add origin https://github.com/felhasznalonev/my-data-explorer.git
git branch -M main
git push -u origin main
```

Kész. A repó publikus URL-jét (`https://github.com/felhasznalonev/my-data-explorer`) elküldheted a kollégáidnak, beírhatsz a cikkedbe, vagy csatolhatsz a konferencia-előadásodhoz.

### A megosztás teljes menete — összefoglalás

1. **Fejlesztés:** Megírod az alkalmazást (AI asszisztenssel, ahogy az 5. fejezetben tanultad)
2. **Tesztelés:** Kipróbálod a saját gépeden
3. **Dokumentáció:** Írsz egy README-t és egy requirements.txt-t
4. **GitHub:** Feltöltöd a repóba
5. **Hosting:** Streamlit Cloud-ra telepíted (vagy helyi hálózaton osztod meg)
6. **Értesítés:** Elkülded a linket a csapatodnak

Ez az egész folyamat — az AI asszisztenssel való kódíratástól a megosztásig — akár egy délután alatt véghezhető.

---

## 13.7 Összefoglalás: A kutató mint eszközkészítő

Ebben a fejezetben három technológiát ismertünk meg, amelyekkel a Python-szkriptjeidet mások számára is használható eszközökké alakíthatod:

### Streamlit

- Python-kódból webalkalmazást hoz létre
- Ideális: adatfeltöltés, dashboard, monitoring, interaktív riport
- Megosztás: helyi hálózat, Streamlit Community Cloud, saját szerver
- Erősségek: táblázatok, grafikonok, fájlkezelés, valós idejű frissítés

### Gradio

- Python-függvényből interaktív felületet generál
- Ideális: modell tesztelése, egyenlet vizualizálása, paraméter-érzékenység vizsgálata
- Megosztás: `share=True` → 72 órás publikus link, Hugging Face Spaces
- Erősségek: automatikus csúszka-generálás, példák, egyszerű kép/szöveg/fájl I/O

### MCP-szerverek

- Az adataidat és eszközeidet AI-hozzáférhetővé teszik
- Ideális: adatbázis-lekérdezés természetes nyelvvel, kutatási infrastruktúra integrálása AI-ba
- Csatlakoztatás: Claude Code, VS Code (Copilot), Cursor
- Erősségek: szabványos protokoll, egyszer megírod — mindenhol használod

### A nagy kép

```
Python-szkript (csak te használod)
       │
       ├── Streamlit  → Kollégák használják böngészőből
       ├── Gradio     → Bárki kipróbálja a modelled
       └── MCP-szerver → AI-eszközök közvetlenül elérik az adataidat
```

A közös nevező: **nem kell szoftverfejlesztővé válnod**. Az 5. fejezetben megtanultad, hogyan írasd meg a kódot AI-val. Ebben a fejezetben megtanultad, hogyan csomagold be az eredményt, hogy mások is használhassák. A kettő együtt egy hatalmas szupererő: az ötlettől a megosztott eszközig akár egyetlen nap alatt eljuthatsz.

A következő fejezetben a könyv záró gondolataival foglalkozunk: hogyan maradj naprakész az AI rohamos fejlődésében, és hogyan építsd be ezeket az eszközöket a hosszú távú kutatási gyakorlatodba.

---

> **A fejezet kódpéldái:** `examples/ch13_streamlit_gradio/` mappában találod a teljes, futtatható forráskódot mindhárom alkalmazáshoz (Data Explorer, Equation Plotter, Sensor Dashboard).
