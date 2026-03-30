# 5. fejezet: AI kódolási asszisztensek — Kód írása programozás nélkül

> **Fejezet-információ**
> - **Kinek szól:** Kutatóknak, akik ismétlődő adatfeldolgozási feladatokat szeretnének automatizálni
> - **Előismeretek:** 2. fejezet (promptolás), 4. fejezet (ajánlott)
> - **Amit megtanulsz:**
>   - Hogyan generáltass kódot AI-val természetes nyelvű utasításokkal
>   - A "rendező" mentalitás: te mondod meg mit, az AI írja a kódot
>   - Python, Git és futtató környezetek alapfogalmai nem-programozóknak
> - **Szükséges eszközök:** Böngésző + terminál (Python telepítése szükséges)
> - **Kapcsolódó fejezetek:** 4. fejezet (no-code elemzés), 7. fejezet (pipeline-ok), 8. fejezet (vizuális programozás)

---

## 5.1 Az 500 CSV-fájl problémája

> **🖼️ 5.1. ábra: A "rendező" mentalitás — te mondod meg mit, az AI írja a kódot**
> *Kétpaneles illusztráció: Bal oldalon egy kutató természetes nyelven ír utasítást; jobb oldalon az AI-asszisztens Python-kódot generál. Közöttük egy nyíl "természetes nyelv → kód" felirattal.*


Képzeld el a következő helyzetet.

Kovács Mária hidrológus vagy a Debreceni Egyetem Környezetgazdálkodási és Környezetpolitikai Intézetében. Az elmúlt három év során 500 mérőállomásról gyűjtöttél vízszint- és csapadékadatokat. Mindegyik állomás havonta egy CSV-fájlt küldött — az eredmény 500 darab táblázat, különböző formátumokkal, hiányzó adatokkal, elgépelt oszlopnevekkel.

Excelben próbáltad megoldani. Az első 10 fájl ment, a 11.-nél más volt az oszlopsorrend. A 47.-nél vessző helyett pontosvessző volt az elválasztó. A 128.-nál hiányzott egy teljes hónap. A 203.-nál "N/A" volt a hiányzó adat jelölése, a 340.-nél meg üres cella. Két hét után 80 fájlnál tartasz, és a diplomamunkád határideje közeledik.

Vagy: biológus vagy, és 2000 mikroszkópos kép fájlnevéből kell kinyerned a minta azonosítóját, a festési módszert és a nagyítást. Vagy: közgazdász, és az Eurostat API-jából kell letöltened 15 ország GDP-adatait 30 évre visszamenőleg. Vagy: vegyész, és 300 spektrum-fájlt kell összesítened egyetlen ábrává.

Mindegyik feladatnak van közös vonása: **ismétlődő, szabályos, gépi munkát igényel, amit egy pár soros program pillanatok alatt megoldana**. De te nem programozó vagy. Sosem tanultál kódolni. A "for ciklus" és a "változó deklarálás" idegen fogalmak.

2024 előtt ezen a ponton két választásod volt:
1. Megtanulsz programozni (hónapok, évek).
2. Keresel egy informatikust, aki megírja neked (hetek várakozás, félreértések, újabb hetek).

2026-ban van egy harmadik lehetőség: **elmondod egy AI-nak, hogy mit akarsz, és az megírja a kódot helyetted**.

Ez a fejezet erről szól. Nem arról, hogyan leszel programozó. Arról, hogyan leszel **rendező** egy olyan produkcióban, ahol az AI a kódíró. Te mondod meg, mit csináljon a program — az AI megírja, te lefuttatod, megnézed az eredményt, és ha nem jó, visszajelzel. Ennyi.

---

## 5.2 A paradigmaváltás: szintaxis helyett szándék

### 5.2.1 A régi világ

A hagyományos programozás tanulás így nézett ki:

1. Megtanulod, mi az a változó, ciklus, feltétel, függvény.
2. Megtanulod a Python (vagy R, vagy MATLAB) szintaxisát.
3. Megtanulod a releváns könyvtárakat (pandas, matplotlib, scipy).
4. Megtanulod a hibakeresést (debugging).
5. Végre megírod a programot.

Ez a folyamat hónapokat, gyakran éveket vett igénybe. A legtöbb tudós az 1-2. lépésnél feladta, mert a szintaxis megtanulása nem volt releváns a kutatási kérdéséhez.

### 5.2.2 Az új világ

Az AI kódolási asszisztensekkel a folyamat így néz ki:

1. **Leírod természetes nyelven**, mit akarsz ("Olvasd be az összes CSV-fájlt a mappából, egységesítsd az oszlopneveket, töröld a hiányzó sorokat, és mentsd el egy nagy táblázatba").
2. Az AI **generálja a kódot**.
3. **Lefuttatod** és megnézed az eredményt.
4. Ha nem jó, **visszajelzel** ("A dátumformátum nem jó, yyyy-mm-dd kell, nem mm/dd/yyyy").
5. Az AI **javítja** a kódot.

Ez a leírd → generáld → teszteld → finomítsd → ismételd ciklus percek alatt megtörténik, nem hónapok alatt.

### 5.2.3 A rendezői analógia

Gondolj egy filmrendezőre. A rendező nem operálja a kamerát, nem írja a zenét, nem varrja a jelmezeket. De pontosan tudja, mit akar: "Ebben a jelenetben a főszereplő háttal áll az ablaknak, kintről beárad a fény, és a zene lassan fokozódik." A szakemberek megvalósítják.

Te vagy a rendező. Az AI a kódíró. A te feladatod:
- **Pontosan megfogalmazni**, mit akarsz (milyen adatot, milyen formátumban, milyen ábrát).
- **Ellenőrizni az eredményt** (az ábra jól néz ki? Az értékek reálisak?).
- **Visszajelezni**, ha valami nem stimmel.

A szaktudás a tiéd — te tudod, hogy a vízszint nem lehet negatív, hogy a pH 0 és 14 között mozog, hogy a hőmérséklet decemberben Debrecenben nem 35°C. Az AI tudja, hogyan kell Python kódot írni. **Együtt vagytok hatékonyak.**

---

> **Ne csináld!**
> Ne futtass le vakon az AI altal generalt kodot anelkul, hogy legalabb atnezned, mit csinal. Nem kell minden sort ertened, de nezd meg: milyen fajlokat olvas/ir, torol-e valamit, kuld-e adatot a halozatra. Egy rosszul fogalmazott prompt eredmenyekeppen az AI generalhat olyan kodot, amely felulirja a meglevo adatfajljaidat vagy tobbe teszi oket olvashatatlanná.

## 5.3 Alapfogalmak — amit tudnod kell, mielőtt elkezdjük

Mielőtt belevágnánk, definiáljunk néhány fogalmat, amelyekre az egész könyvben hivatkozni fogunk. Nem kell őket mélyen megértened — elég, ha tudod, mire valók.

### 5.3.1 Python

A **Python** egy programozási nyelv. Nem a kígyó, hanem a Monty Python nevű brit komikuscsoportról kapta a nevét. Azért használjuk a tudományban, mert:
- **Egyszerű a szintaxisa** — közelebb áll az angol nyelvhez, mint más programozási nyelvek.
- **Hatalmas az ökoszisztémája** — több tízezer ingyenes kiegészítő csomag (library / könyvtár) létezik hozzá, a statisztikától a gépi tanulásig.
- **A tudomány de facto nyelve** — a Nature 2024-es felmérése szerint a kutatók 70%-a Pythont használ.
- **Ingyenes és nyílt forráskódú** — nem kell licencet venni, mint a MATLAB-hoz.

Fontos: **neked nem kell megtanulnod Pythonul programozni**. Az AI fogja írni a Python kódot. De tudnod kell, hogy a kódblokkok, amiket az AI generál, Python nyelven íródnak, és Python-nal kell őket futtatni.

### 5.3.2 Git és verziókezelés

A **Git** egy verziókezelő rendszer (version control system). Gondolj rá úgy, mint egy időgépre a fájljaidhoz. Minden alkalommal, amikor "mentesz" (a Git nyelvén: *commit*-olsz), a Git eltárol egy pillanatfelvételt a projektedről. Ha valami elromlik, visszaugorhatsz bármelyik korábbi állapothoz.

Miért a biztonsági hálód?
- **Kísérletezés bátran**: kipróbálhatsz egy új megközelítést, és ha nem működik, egy paranccsal visszaállítod az előző állapotot.
- **Dokumentáció**: minden módosításhoz írsz egy rövid leírást ("hozzáadtam a pH-szűrőt"), így három hónap múlva is tudod, mit csináltál és miért.
- **Együttműködés**: ha társszerzővel dolgozol, a Git kezeli, ki mit módosított, és automatikusan összefésüli a változtatásokat.

A Git szorosan összefonódik a **GitHub**-bal, ami egy felhőalapú platform, ahol a Git-projektjeidet (repository-kat) tárolhatod és megoszthatod. Gondolj rá úgy: a Git a motor, a GitHub a garázs.

### 5.3.3 Jupyter notebook

A **Jupyter notebook** (kiejtve: "dzsúpiter") egy interaktív dokumentum, ami kódot, szöveget, képeket és grafikonokat tartalmaz egyetlen fájlban. A neve a három fő programozási nyelvből ered: **Ju**lia, **Py**thon, **R** (bár ma szinte kizárólag Pythonnal használják).

Gondolj rá úgy, mint egy digitális laboratóriumi naplóra:
- A felső cellába írod a hipotézist (szöveg).
- A következő cellába az adatbetöltő kódot (kód).
- Az eredmény rögtön alatta jelenik meg (grafikon, táblázat).
- A következő cellába az értelmezést (szöveg).

Ez a kód-szöveg-eredmény-értelmezés ritmusa teszi a Jupyter notebookot a tudósok kedvencévé. Az 5.10-es alfejezetben részletesen foglalkozunk vele.

### 5.3.4 API (Application Programming Interface)

Az **API** (alkalmazásprogramozási interfész) egy szabványos módszer, ahogy két program kommunikál egymással. Gondolj rá úgy, mint egy étterem pincérjére: te (a programod) leadod a rendelést (kérés / request), a konyha (a másik rendszer) elkészíti, és a pincér (az API) kihozza az eredményt (válasz / response).

Példák:
- A meteorológiai szolgálat API-ján keresztül letöltöd az aktuális időjárási adatokat.
- Az Eurostat API-ján keresztül lekérdezed az EU-tagországok GDP-adatait.
- A PubMed API-ján keresztül keresel tudományos cikkeket.

### 5.3.5 pip és virtuális környezet (virtual environment)

A **pip** a Python csomagkezelője (package manager). Amikor egy Python könyvtárra van szükséged (például matplotlib az ábrákhoz), a `pip install matplotlib` paranccsal telepíted. Gondolj rá úgy, mint egy alkalmazás-bolttra a Pythonhoz.

A **virtuális környezet** (virtual environment, röviden *venv*) egy elszigetelt Python-telepítés. Miért kell? Mert különböző projektjeid különböző csomagverziókat igényelhetnek. Ha az egyik projekt a pandas 1.5-öt használja, a másik meg a pandas 2.0-t, a virtuális környezet biztosítja, hogy ne keveredjenek. Gondolj rá úgy, mint egy külön fiókra a szerszámos szekrényben: minden projekthez saját fiók, saját szerszámkészlettel.

---

## 5.4 A munkakörnyezet beállítása — az AI segítségével

Most lépésről lépésre beállítjuk a munkakörnyezetedet. A jó hír: **az AI ebben is segít**. Nem kell mindent fejből tudnod — kérdezd meg az AI-t, ha elakadsz.

### 5.4.1 Python telepítése

**Windows:**
1. Nyisd meg a böngészőt és keresd meg: `python.org/downloads`
2. Kattints a "Download Python 3.x.x" gombra (2026 márciusában a legfrissebb a 3.13).
3. **FONTOS**: a telepítőben pipáld be az "Add Python to PATH" opciót! Ez kritikus — enélkül a rendszer nem találja meg a Pythont.
4. Kattints az "Install Now" gombra.
5. Ellenőrzés: nyiss egy terminált (Start menü → "cmd" → Enter) és írd be: `python --version`. Ha egy verziószámot látsz (pl. `Python 3.13.2`), sikerült.

**macOS:**
1. Nyisd meg a Terminal alkalmazást.
2. Írd be: `brew install python` (ha a Homebrew telepítve van) vagy töltsd le a python.org-ról.
3. Ellenőrzés: `python3 --version`

**Linux:**
A legtöbb disztribúción eleve telepítve van. Ellenőrzés: `python3 --version`

> **Tipp**: Ha bármelyik lépésnél elakadsz, másold be a hibaüzenetet egy AI chatbe (Claude, ChatGPT) és kérdezd meg: "Python telepítés közben ezt a hibát kaptam: [hibaüzenet]. Mit csináljak?" Az AI szinte mindig azonnal megoldja.

### 5.4.2 VS Code — a tudós szerkesztőprogramja

A **Visual Studio Code** (röviden VS Code) egy ingyenes, könnyű kódszerkesztő a Microsofttól. Nem egy nehéz fejlesztőkörnyezet — inkább egy okos jegyzettömb, ami érti a kódot.

Miért pont VS Code?
- **Ingyenes** és minden platformon fut (Windows, macOS, Linux).
- **Bővítményekkel testreszabható** — a Python támogatástól a Git integrációig minden elérhető.
- **Az AI kódolási eszközök mindegyike itt működik a legjobban** — a GitHub Copilot, a Cursor és a többi mind VS Code-ra épül vagy VS Code-kompatibilis.
- **Jupyter notebook támogatás** beépítve.

**Telepítés:**
1. Keresd meg: `code.visualstudio.com`
2. Töltsd le a rendszerednek megfelelő verziót.
3. Telepítsd.
4. Nyisd meg, és telepítsd a következő bővítményeket (Extensions → keresőmezőbe írd be):
   - **Python** (Microsoft): Python nyelvi támogatás, szintaxiskiemelés, hibakeresés.
   - **Jupyter** (Microsoft): Jupyter notebook támogatás közvetlenül VS Code-ban.
   - **GitHub Copilot** (GitHub): AI kódolási asszisztens (ha ezt választod, lásd 5.5).

### 5.4.3 pip és virtuális környezet beállítása

Nyiss egy terminált (VS Code-ban: Terminal → New Terminal, vagy `Ctrl+ö`) és írd be:

```bash
# Virtuális környezet létrehozása a "projekt" mappában
python -m venv kutatas_venv

# Aktiválás Windowson:
kutatas_venv\Scripts\activate

# Aktiválás macOS/Linux-on:
source kutatas_venv/bin/activate

# Mostantól minden pip install ebbe a környezetbe kerül
pip install numpy pandas matplotlib scipy scikit-learn jupyter
```

Ha a terminálban a sor elején megjelenik a `(kutatas_venv)` felirat, a virtuális környezet aktív. Minden csomag, amit most telepítesz, csak ehhez a projekthez tartozik.

> **Tipp**: Kérdezd meg az AI-t: "Készíts egy requirements.txt fájlt a hidrológiai adatfeldolgozó projektemhez." Az AI összeállítja a szükséges csomagok listáját, és egyetlen `pip install -r requirements.txt` paranccsal mindent telepíthetsz.

### 5.4.4 Git — a biztonsági hálód beállítása

A Git a legfontosabb eszköz, amiről a legtöbb kezdő tudós nem tud. **Ha egyetlen dolgot tanulsz meg ebből az alfejezetből, ez legyen az.**

**Telepítés:**
- **Windows**: töltsd le a `git-scm.com`-ról és telepítsd (az alapértelmezett beállítások jók).
- **macOS**: `brew install git` vagy `xcode-select --install`
- **Linux**: `sudo apt install git` (Ubuntu/Debian) vagy `sudo dnf install git` (Fedora)

**Első használat:**

```bash
# Állítsd be a neved és email-címed (egyszer kell, nem projektenként)
git config --global user.name "Kovács Mária"
git config --global user.email "maria.kovacs@example.com"

# Hozz létre egy új projektet
mkdir vizsszint_elemzes
cd vizszint_elemzes
git init

# Készíts egy mentéspontot (commit)
git add -A
git commit -m "Projekt indítása, üres struktúra"
```

**A négy parancs, amit ismerned kell:**

| Parancs | Mit csinál | Analógia |
|---------|-----------|----------|
| `git add -A` | Előkészíti a módosításokat mentésre | Bepakolod a dobozt |
| `git commit -m "leírás"` | Ment egy pillanatfelvételt | Ráírod a dobozra, mi van benne |
| `git log --oneline` | Megmutatja a mentéspontok listáját | Megnézed a dobozok címkéit |
| `git checkout <hash>` | Visszaállít egy régebbi állapotot | Előkeresed a régi dobozt |

**Miért a biztonsági hálód?**

Tegyük fel, hogy az AI generál egy kódot, ami feldolgozza az adataidat. Lefuttatod, és az eredmény nagyszerű. `git commit -m "500 CSV feldolgozva, eredmények rendben"`. Másnap az AI egy "javított" verziót generál, ami véletlenül felülírja az eredeti fájlokat. Pánik? Nem. `git checkout` — és visszakaptad az előző verziót.

> **Aranyszabály**: Minden sikeres lépés után commitolj. Az AI kódolási asszisztensek egyik veszélye, hogy gyorsan generálnak sok kódot — a Git biztosítja, hogy bármikor visszaléphess.

---

## 5.5 AI kódolási eszközök 2026-ban — a teljes áttekintés

Ez a könyv egyetlen helye, ahol részletesen összehasonlítjuk az összes főbb AI kódolási eszközt. Ha a 6., 7. vagy 12. fejezetben azt olvasod, hogy "kérd meg az AI kódolási asszisztenst", itt találod meg, melyiket és hogyan.

### 5.5.1 Claude Code — a terminál-alapú ágentikus kódoló

A **Claude Code** az Anthropic parancssori (terminal-based) AI kódolási eszköze. Nincs grafikus felülete — egy terminálban fut, ahol természetes nyelven írod le, mit akarsz, és a Claude közvetlenül szerkeszti a fájljaidat, futtatja a kódot, és javítja a hibákat.

**Hogyan működik:**
1. Megnyitod a terminált a projekted mappájában.
2. Beírod: `claude`
3. Természetes nyelven leírod a feladatot: "Olvasd be az összes CSV-fájlt a data/ mappából, egységesítsd az oszlopneveket, és mentsd el egy összesített fájlba."
4. A Claude megtervezi a lépéseket, megírja a kódot, lefuttatja, és ha hibát talál, magától javítja.

**Miért szeretik a tudósok:**
- **Ágentikus működés**: nem csak kódot generál, hanem végrehajtja is. Létrehozza a fájlokat, telepíti a csomagokat, lefuttatja a teszteket.
- **A teljes projektet látja**: nem csak a megnyitott fájlt, hanem az egész mappát, a fájlstruktúrát, a konfigurációkat.
- **Nincs IDE-függőség**: bárhol működik, ahol van terminál.
- **A legújabb Stack Overflow felmérés (2025) szerint a fejlesztők 46%-a "legkedveltebb" AI kódolási eszköznek választotta** — ez a legmagasabb arány az összes eszköz közül.

**Korlátai:**
- Terminálban fut, ami kezdőknek ijesztő lehet (de pont ez a fejezet segít áthidalni ezt).
- Fizetős: a Claude Pro előfizetés (20 USD/hó) vagy API-használat szükséges.

**Mikor válaszd:** Ha komplex, többlépéses feladataid vannak (pl. "dolgozd fel az összes fájlt, készíts grafikonokat, és generálj egy összefoglaló riportot"), és nem bánod a terminált.

### 5.5.2 GitHub Copilot — a vállalati szabvány

A **GitHub Copilot** a GitHub (Microsoft) AI kódolási asszisztense, amely közvetlenül a VS Code szerkesztőbe épül. Három fő módja van:

1. **Inline javaslatok (ghost text)**: Ahogy gépelsz, a Copilot szürkített szöveggel javasolja a következő sort vagy blokkot. Tab-bal elfogadod, Esc-kel elveted.
2. **Chat mód**: Egy oldalsó panelen természetes nyelven beszélgethetsz a Copilottal. Kérdezhetsz a kódról, kérhetsz módosításokat, vagy magyarázatot.
3. **Agent mód**: A legújabb és leghatékonyabb mód — leírod a célt, és a Copilot önállóan tervez, kódol, futtat teszteket, és javít. Létrehozhat fájlokat, telepíthet csomagokat, és iteratívan dolgozik, amíg a feladat kész nincs.

**Számok:**
- **4,7 millió előfizető** világszerte (2025 végén).
- Elérhető több AI modellel: GPT-4o, Claude Sonnet, Gemini — te választod, melyiket használod.
- VS Code-ban, JetBrains IDE-kben és a GitHub weboldalán is működik.

**Mikor válaszd:** Ha VS Code-ban dolgozol, és szeretnéd, hogy az AI folyamatosan "súgjon" gépelés közben. Különösen jó ismétlődő minták felismerésére (pl. ha megírod az első adatbetöltő függvényt, a másodikat már a Copilot ajánlja).

### 5.5.3 Cursor — az AI-natív IDE

A **Cursor** egy teljes fejlesztőkörnyezet (IDE), ami a VS Code kódbázisára épül, de az AI-t az első pillanattól beépítve tartalmazza. Nem egy bővítmény, hanem maga az IDE is AI-központú.

**Fő jellemzői:**
- **Composer**: leírod természetes nyelven, mit akarsz, és a Cursor több fájlban egyszerre módosít.
- **Kódbázis-ismeret**: a Cursor indexeli az egész projektedet, és kontextusként használja a válaszokhoz.
- **Inline szerkesztés**: kijelölsz egy kódblokkot, leírod, mit akarsz változtatni, és a Cursor átírja.
- **Többmodell támogatás**: választhatsz Claude, GPT-4o, Gemini és más modellek között.

**Mikor válaszd:** Ha szereted a VS Code-ot, de még mélyebb AI-integrációt akarsz, és nem bánsz egy új alkalmazást telepíteni.

### 5.5.4 Windsurf és Codex — alternatívák

**Windsurf** (korábban Codeium) egy ingyenes AI kódolási eszköz, ami az alapfunkciókat (inline javaslatok, chat) díjmentesen kínálja. Jó választás, ha még csak ismerkedsz az AI kódolási asszisztensekkel és nem akarsz azonnal fizetni.

**OpenAI Codex** a ChatGPT mögött álló OpenAI kódolási ágense. Hasonlóan a Claude Code-hoz, ez is ágentikus: leírod a feladatot, és a Codex önállóan dolgozik rajta. A ChatGPT Plus / Pro előfizetéssel érhető el.

### 5.5.5 Összehasonlító táblázat

| Jellemző | Claude Code | GitHub Copilot | Cursor | Windsurf | Codex |
|----------|-------------|----------------|--------|----------|-------|
| **Típus** | Terminál-ágens | IDE-bővítmény + ágens | AI-natív IDE | IDE-bővítmény | Felhő-ágens |
| **Működési mód** | Parancssor | VS Code beépülő | Önálló IDE | VS Code beépülő | Webes + CLI |
| **Inline javaslatok** | Nem | Igen | Igen | Igen | Nem |
| **Chat** | Igen (terminál) | Igen (panel) | Igen (panel) | Igen (panel) | Igen (web) |
| **Ágentikus mód** | Igen (alap) | Igen (Agent Mode) | Igen (Composer) | Korlátozott | Igen (alap) |
| **Fájlszerkesztés** | Közvetlen | Közvetlen | Közvetlen | Közvetlen | Sandbox |
| **Kód futtatás** | Igen | Igen (Agent) | Igen | Korlátozott | Igen (sandbox) |
| **Ár (2026)** | $20/hó (Pro) | $10/hó (Individual) | $20/hó (Pro) | Ingyenes alap | $20/hó (Plus) |
| | $100/hó (Max) | $19/hó (Business) | $40/hó (Business) | $10/hó (Pro) | $200/hó (Pro) |
| **AI modellek** | Claude (Anthropic) | GPT-4o, Claude, Gemini | Claude, GPT-4o, Gemini | Saját + nyílt | GPT-4o, o3 |
| **Erősség** | Komplex, többlépéses feladatok | Folyamatos kódolási támogatás | Mély kódbázis-integráció | Ingyenes belépő | Autonóm végrehajtás |
| **Ideális, ha...** | Nagyobb projekteket építesz | Napi kódoláshoz, csapatban | AI-központú fejlesztést akarsz | Kipróbálnád ingyen | ChatGPT-felhasználó vagy |
| **Tudósoknak ajánlott?** | Haladó | Mindenkinek | Középhaladó | Kezdő | Középhaladó |

### 5.5.6 Mit válassz?

Ha most kezded és nincs tapasztalatod:

1. **Telepítsd a VS Code-ot** és a **GitHub Copilot** bővítményt. Az ingyenes szint (Copilot Free) havi korlátozott kérésszámmal, de működik. Az inline javaslatok és a chat azonnal elérhetők.
2. **Próbáld ki a Copilot Agent módot**: írd le természetes nyelven a feladatodat a chat panelen, válaszd az "Agent" módot, és hagyd dolgozni.
3. **Ha komolyabb projektjeid lesznek**, próbáld ki a **Claude Code**-ot: telepítsd (`npm install -g @anthropic-ai/claude-code`), és a terminálban írd be: `claude`. A Claude Code különösen erős a többlépéses, komplex tudományos feladatokban.

> **Fontos**: Ne próbáld egyszerre mindet megtanulni. Válassz egyet, használd két hétig, és ha nem tetszik, válts. Az AI kódolási eszközök közötti váltás egyszerű — a Python kód ugyanaz marad, csak az eszköz változik.

---

## 5.6 Az első AI-val írt Python szkriptek

Most jön a lényeg: **konkrét, teljes példák**, amelyeket az AI-val együtt hozol létre. Minden példánál megmutatom, mit mondanál az AI-nak (a promptot), és milyen kódot kapsz (az eredményt). A kódot nem kell megértened sorról sorra — elég, ha lefuttatod és megnézed az eredményt.

### 5.6.1 Rendetlen adathalmaz beolvasása és tisztítása

**A helyzet:** Van egy CSV-fájlod (`vizszint_2024.csv`), ami így néz ki:

```
Állomás;Dátum;Vízszint (cm);Hőmérséklet
Debrecen;2024-01-15;234;-2.5
Hajdúszoboszló;2024-01-15;189;-3.1
Debrecen;2024-02-15;N/A;1.2
Hajdúszoboszló;2024-02-15;201;
Debrecen;2024-03-15;245;8.7
Nyíregyháza;15/03/2024;198;7.3
```

Problémák: pontosvessző elválasztó, "N/A" mint hiányzó adat, üres cellák, eltérő dátumformátum.

**A prompt az AI-nak:**

> Olvasd be a `vizszint_2024.csv` fájlt. Figyelj arra, hogy pontosvessző az elválasztó. A hiányzó adatokat ("N/A" és üres cella) jelöld NaN-nak. A dátumokat egységesítsd yyyy-mm-dd formátumra. Adj egy összefoglalót: hány sor van, hány hiányzó adat oszloponként. Végül mentsd el a tisztított adatot `vizszint_2024_tiszta.csv`-ként.

**Az AI által generált kód:**

```python
import pandas as pd

# Beolvasás pontosvessző elválasztóval, hiányzó értékek kezelése
df = pd.read_csv('vizszint_2024.csv', sep=';', na_values=['N/A', ''])

# Dátum egységesítés (többféle formátum kezelése)
df['Dátum'] = pd.to_datetime(df['Dátum'], format='mixed', dayfirst=True)
df['Dátum'] = df['Dátum'].dt.strftime('%Y-%m-%d')

# Összefoglaló
print(f"Összes sor: {len(df)}")
print(f"\nHiányzó adatok oszloponként:")
print(df.isnull().sum())
print(f"\nElső 5 sor:")
print(df.head())

# Tisztított fájl mentése
df.to_csv('vizszint_2024_tiszta.csv', index=False)
print("\nTisztított fájl elmentve: vizszint_2024_tiszta.csv")
```

**Kimenet:**
```
Összes sor: 6
Hiányzó adatok oszloponként:
Állomás               0
Dátum                 0
Vízszint (cm)         1
Hőmérséklet           1

Első 5 sor:
          Állomás       Dátum  Vízszint (cm)  Hőmérséklet
0       Debrecen  2024-01-15          234.0         -2.5
1  Hajdúszoboszló  2024-01-15          189.0         -3.1
2       Debrecen  2024-02-15            NaN          1.2
3  Hajdúszoboszló  2024-02-15          201.0          NaN
4       Debrecen  2024-03-15          245.0          8.7

Tisztított fájl elmentve: vizszint_2024_tiszta.csv
```

Öt sor kód, és megoldottad, amivel Excelben egy órát szórakoztál volna. És a kulcs: **a kódot nem neked kellett megírni** — az AI írta, te csak elmondtad, mit akarsz.

### 5.6.2 Publikáció-minőségű ábra készítése matplotlib-tel

**A helyzet:** Az előbbi adatokból szeretnél egy ábrát, ami elég szép egy folyóiratcikkhez.

**A prompt az AI-nak:**

> A `vizszint_2024_tiszta.csv` adataiból készíts egy ábrát. Az x-tengely a dátum, az y-tengely a vízszint (cm). Minden állomás külön színnel és jelölővel. Az ábra legyen publikáció-minőségű: 300 DPI, 10x6 hüvelyk, Times New Roman betűtípus, 12-es betűméret, rács a háttérben. Mentsd el `vizszint_abra.png` és `vizszint_abra.pdf` formátumban is. A tengely feliratok legyenek magyarul.

**Az AI által generált kód:**

```python
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Adatok beolvasása
df = pd.read_csv('vizszint_2024_tiszta.csv')
df['Dátum'] = pd.to_datetime(df['Dátum'])

# Ábra beállítások
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman'],
    'font.size': 12,
    'axes.linewidth': 1.2,
    'figure.dpi': 150
})

fig, ax = plt.subplots(figsize=(10, 6))

# Állomásonkénti ábrázolás
markers = ['o', 's', '^']
colors = ['#2166ac', '#b2182b', '#4dac26']

for i, (station, group) in enumerate(df.groupby('Állomás')):
    ax.plot(group['Dátum'], group['Vízszint (cm)'],
            marker=markers[i % 3],
            color=colors[i % 3],
            linewidth=2,
            markersize=8,
            label=station)

# Tengelyek formázása
ax.set_xlabel('Dátum', fontsize=14, fontweight='bold')
ax.set_ylabel('Vízszint (cm)', fontsize=14, fontweight='bold')
ax.set_title('Vízszintváltozás a mérőállomásokon (2024)', fontsize=16, fontweight='bold')

ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
ax.xaxis.set_major_locator(mdates.MonthLocator())
fig.autofmt_xdate()

ax.legend(frameon=True, fancybox=True, shadow=True, fontsize=11)
ax.grid(True, linestyle='--', alpha=0.7)
ax.set_axisbelow(True)

plt.tight_layout()

# Mentés publikáció-minőségben
fig.savefig('vizszint_abra.png', dpi=300, bbox_inches='tight')
fig.savefig('vizszint_abra.pdf', bbox_inches='tight')
print("Ábrák elmentve: vizszint_abra.png és vizszint_abra.pdf")
plt.show()
```

Az eredmény egy professzionális ábra, amit azonnal beilleszthetsz a cikkedbe. 300 DPI, PDF formátum — a legtöbb folyóirat ezt kéri. Ha nem tetszik a szín, a betűméret vagy a jelölő, egyszerűen szólsz az AI-nak: "Változtasd a színeket passzív kék-narancs-szürke palettára" — és módosítja.

### 5.6.3 Modellillesztés kísérleti adatokhoz (scipy.optimize)

**A helyzet:** Mérési adataid vannak, és egy exponenciális görbét szeretnél illeszteni rájuk.

**A prompt az AI-nak:**

> Van egy adatsorom: az x értékek [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], az y értékek [2.1, 2.9, 4.3, 7.1, 10.8, 17.2, 25.1, 40.3, 58.2, 90.1]. Illessz egy exponenciális görbét (y = a * exp(b * x) + c) az adatokra scipy.optimize.curve_fit segítségével. Rajzold ki az adatpontokat és az illesztett görbét. Írd ki az illesztett paramétereket és az R² értéket.

**Az AI által generált kód:**

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score

# Mérési adatok
x_data = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
y_data = np.array([2.1, 2.9, 4.3, 7.1, 10.8, 17.2, 25.1, 40.3, 58.2, 90.1])

# Exponenciális modell
def exp_model(x, a, b, c):
    return a * np.exp(b * x) + c

# Görbeillesztés
popt, pcov = curve_fit(exp_model, x_data, y_data, p0=[1, 0.5, 0])
a, b, c = popt

# R² számítás
y_pred = exp_model(x_data, *popt)
r2 = r2_score(y_data, y_pred)

# Eredmények kiírása
print(f"Illesztett paraméterek:")
print(f"  a = {a:.4f}")
print(f"  b = {b:.4f}")
print(f"  c = {c:.4f}")
print(f"  R² = {r2:.6f}")
print(f"\nModell: y = {a:.4f} * exp({b:.4f} * x) + ({c:.4f})")

# Ábra
x_smooth = np.linspace(0, 9, 200)
y_smooth = exp_model(x_smooth, *popt)

plt.figure(figsize=(8, 5))
plt.scatter(x_data, y_data, color='red', s=80, zorder=5, label='Mérési adatok')
plt.plot(x_smooth, y_smooth, 'b-', linewidth=2, label=f'Illesztés: R² = {r2:.4f}')
plt.xlabel('x', fontsize=13)
plt.ylabel('y', fontsize=13)
plt.title('Exponenciális görbeillesztés', fontsize=15)
plt.legend(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('gorbeillesztes.png', dpi=300)
plt.show()
```

**Kimenet:**
```
Illesztett paraméterek:
  a = 1.9532
  b = 0.4312
  c = 0.2187
  R² = 0.999834

Modell: y = 1.9532 * exp(0.4312 * x) + (0.2187)
```

Az R² = 0.9998 — kiváló illeszkedés. Ezt a kódot a scipy.optimize dokumentáció olvasása nélkül kaptad meg, egyetlen prompt alapján.

### 5.6.4 500 fájl kötegelt feldolgozása

Visszatérünk Mária problémájához. 500 CSV-fájl a `data/` mappában.

**A prompt az AI-nak:**

> A `data/` mappában 500 CSV-fájl van, mindegyik egy mérőállomás havi adatait tartalmazza. A fájlnév formátuma: `allomas_NNNN.csv` (pl. `allomas_0001.csv`). Minden fájlban van egy "Dátum", "Vízszint" és "Csapadék" oszlop, de néhol más az oszlopnév (pl. "vizszint", "Vizszint_cm", "Water_Level"). A feladat: olvasd be az összes fájlt, egységesítsd az oszlopneveket, szűrd ki a fizikailag lehetetlen értékeket (vízszint < 0 vagy > 1000 cm, csapadék < 0), és mentsd el egy összesített fájlba (`osszesitett.csv`) az állomás azonosítójával kiegészítve. Írd ki, hány fájl volt sikeres, hány hibás, és melyek a hibás fájlok.

**Az AI által generált kód:**

```python
import pandas as pd
import os
import re
from pathlib import Path

data_dir = Path('data')
all_data = []
errors = []

# Oszlopnév-egységesítő szótár
column_mapping = {
    'vizszint': 'Vízszint',
    'vizszint_cm': 'Vízszint',
    'water_level': 'Vízszint',
    'vízszint': 'Vízszint',
    'dátum': 'Dátum',
    'datum': 'Dátum',
    'date': 'Dátum',
    'csapadék': 'Csapadék',
    'csapadek': 'Csapadék',
    'precipitation': 'Csapadék',
    'rainfall': 'Csapadék',
}

csv_files = sorted(data_dir.glob('allomas_*.csv'))
print(f"Talált fájlok száma: {len(csv_files)}")

for filepath in csv_files:
    try:
        # Állomás azonosító kinyerése a fájlnévből
        station_id = re.search(r'allomas_(\d+)', filepath.stem).group(1)

        # Beolvasás (próbálkozás különböző elválasztókkal)
        try:
            df = pd.read_csv(filepath, sep=',', na_values=['N/A', 'NA', '-', ''])
        except:
            df = pd.read_csv(filepath, sep=';', na_values=['N/A', 'NA', '-', ''])

        # Oszlopnevek egységesítése (kisbetűsre, majd szótárból)
        df.columns = [column_mapping.get(col.lower().strip(), col) for col in df.columns]

        # Ellenőrzés: szükséges oszlopok megvannak?
        required = ['Dátum', 'Vízszint', 'Csapadék']
        missing = [col for col in required if col not in df.columns]
        if missing:
            errors.append((filepath.name, f"Hiányzó oszlopok: {missing}"))
            continue

        # Fizikailag lehetetlen értékek szűrése
        before = len(df)
        df = df[(df['Vízszint'].isna()) | ((df['Vízszint'] >= 0) & (df['Vízszint'] <= 1000))]
        df = df[(df['Csapadék'].isna()) | (df['Csapadék'] >= 0)]
        removed = before - len(df)

        if removed > 0:
            print(f"  {filepath.name}: {removed} lehetetlen érték eltávolítva")

        # Állomás azonosító hozzáadása
        df['Állomás_ID'] = station_id

        all_data.append(df)

    except Exception as e:
        errors.append((filepath.name, str(e)))

# Összesítés
if all_data:
    result = pd.concat(all_data, ignore_index=True)
    result.to_csv('osszesitett.csv', index=False)
    print(f"\nSikeres fájlok: {len(all_data)}")
    print(f"Hibás fájlok: {len(errors)}")
    print(f"Összes sor az összesített fájlban: {len(result)}")
else:
    print("Egyetlen fájl sem volt beolvasható!")

if errors:
    print(f"\nHibás fájlok listája:")
    for filename, error in errors:
        print(f"  {filename}: {error}")
```

Ez a szkript percek alatt feldolgozza az 500 fájlt, amit Mária kézzel hetekig csinált volna. És figyeld meg: **a domain-tudás beépült a promptba** — te tudod, hogy a vízszint nem lehet negatív vagy 1000 cm fölötti, az AI pedig ezt programozási logikává alakította.

> **🌾 Szakterületi példa: Vízgyűjtő-lehatárolási szkript automatizálása**
>
> A hidrológiai térinformatikában a vízgyűjtő-lehatárolás 6-8 egymásra épülő GIS-lépésből áll: DEM feltöltés, folyásirány-meghatározás, folyásfelhalmozás, küszöbérték-alkalmazás, vízgyűjtő-lehatárolás, és végül vektorizálás. Az AI-kódolási asszisztens egyetlen promptból generálja a teljes ArcPy- vagy PyQGIS-szkriptet, amely akár 23 866 részvízgyűjtőt is feldolgoz egyetlen éjszaka alatt. A kötegelt feldolgozás ugyanazt a „for ciklus a bemeneti fájlokon" logikát követi, mint a fenti 500 CSV-s példa — csak itt DEM-ek az inputok és vízgyűjtő-poligonok az outputok.
>
> *Forrás: hidrogis 12.7 „Vízgyűjtő-lehatárolási szkript felépítése lépésről lépésre"*

### 5.6.5 Kapcsolódás adatbázishoz vagy API-hoz

**A helyzet:** Le akarod tölteni a napi meteorológiai adatokat az Open-Meteo API-ról Debrecenre.

**A prompt az AI-nak:**

> Töltsd le a 2024-es napi átlaghőmérsékletet és csapadékösszeget Debrecenre (47.53°N, 21.63°E) az Open-Meteo API-ról. Mentsd el CSV-be, és rajzolj egy kettős y-tengelyű ábrát (hőmérséklet bal oldalon, csapadék jobb oldalon).

**Az AI által generált kód:**

```python
import requests
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Open-Meteo API lekérés (ingyenes, regisztráció nélkül)
url = "https://archive-api.open-meteo.com/v1/archive"
params = {
    "latitude": 47.53,
    "longitude": 21.63,
    "start_date": "2024-01-01",
    "end_date": "2024-12-31",
    "daily": ["temperature_2m_mean", "precipitation_sum"],
    "timezone": "Europe/Budapest"
}

response = requests.get(url, params=params)
data = response.json()

# DataFrame készítése
df = pd.DataFrame({
    'Dátum': pd.to_datetime(data['daily']['time']),
    'Átlaghőmérséklet (°C)': data['daily']['temperature_2m_mean'],
    'Csapadék (mm)': data['daily']['precipitation_sum']
})

# CSV mentés
df.to_csv('debrecen_meteo_2024.csv', index=False)
print(f"Adatok letöltve: {len(df)} nap")
print(df.describe())

# Kettős tengelyű ábra
fig, ax1 = plt.subplots(figsize=(14, 6))

color_temp = '#d73027'
ax1.plot(df['Dátum'], df['Átlaghőmérséklet (°C)'],
         color=color_temp, linewidth=1, alpha=0.8)
ax1.set_xlabel('Dátum', fontsize=13)
ax1.set_ylabel('Átlaghőmérséklet (°C)', color=color_temp, fontsize=13)
ax1.tick_params(axis='y', labelcolor=color_temp)

ax2 = ax1.twinx()
color_prec = '#4575b4'
ax2.bar(df['Dátum'], df['Csapadék (mm)'],
        color=color_prec, alpha=0.4, width=1)
ax2.set_ylabel('Csapadék (mm)', color=color_prec, fontsize=13)
ax2.tick_params(axis='y', labelcolor=color_prec)

ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
ax1.xaxis.set_major_locator(mdates.MonthLocator())
fig.autofmt_xdate()

plt.title('Debrecen napi meteorológiai adatai (2024)', fontsize=15, fontweight='bold')
plt.tight_layout()
plt.savefig('debrecen_meteo_2024.png', dpi=300)
plt.show()
```

Három dolgot figyeld meg:
1. **Nem kellett regisztrálnod** az Open-Meteo API-hoz — ingyenes és nyílt.
2. **A koordinátákat te adtad meg** — ez a domain-tudásod, amit az AI nem tudhat.
3. **Az eredmény azonnal vizualizálva van** — nem kell külön grafikont rajzolni.

---

## 5.7 A visszacsatolási ciklus: leírd → generáld → teszteld → finomítsd

Az AI kódolási asszisztenssel való munka nem "prompt → kész kód" egyenes vonal. Ez egy **ciklus**, ahol te és az AI folyamatosan finomítjátok az eredményt. Nézzünk egy valósághű párbeszédet.

### 5.7.1 Egy teljes példa-párbeszéd

**1. kör — Az első prompt:**

> **Te:** Készíts egy Python szkriptet, ami beolvassa a `mintak.xlsx` Excel-fájlt, és minden mintához kiszámolja a pH átlagot és szórást.

> **AI:** [Generálja a kódot pandas-szal, pd.read_excel, groupby, mean, std]

**Lefuttatod. Hiba:**

```
ModuleNotFoundError: No module named 'openpyxl'
```

**2. kör — Hibajelzés:**

> **Te:** Ezt a hibát kaptam: ModuleNotFoundError: No module named 'openpyxl'

> **AI:** Az openpyxl csomag kell az Excel-fájlok olvasásához. Telepítsd: `pip install openpyxl`. [Módosított kód, ami ellenőrzi, hogy a csomag telepítve van-e.]

**Lefuttatod. Működik, de nem jó az eredmény:**

```
Minta_ID  pH_átlag  pH_szórás
A-001     7.23      0.15
A-002     NaN       NaN
A-003     12.85     2.31
```

**3. kör — Domain-tudás alkalmazása:**

> **Te:** Az A-002 mintánál NaN az eredmény — valószínűleg hiányzó adatok vannak. Szűrd ki a hiányzó értékeket az átlagszámítás előtt. Az A-003 mintánál a pH szórása 2.31, ami gyanúsan magas — írd ki figyelmeztetésként, ha a szórás > 1.0. Továbbá a pH nem lehet 14-nél nagyobb, szűrd ki az ilyen értékeket.

> **AI:** [Módosított kód: dropna() a groupby előtt, figyelmeztetés magas szórásnál, pH > 14 szűrés]

**Lefuttatod. Most jó:**

```
Minta_ID  pH_átlag  pH_szórás
A-001     7.23      0.15
A-002     6.89      0.08        (3 hiányzó érték kiszűrve)
A-003     7.12      0.43        (2 outlier kiszűrve: pH > 14)

⚠ Nincs figyelmeztetés: minden szórás < 1.0
```

**4. kör — Vizualizáció kérése:**

> **Te:** Készíts egy boxplotot az összes minta pH-eloszlásáról, és jelöld pirossal azokat a mintákat, ahol volt outlier.

> **AI:** [Boxplot kód matplotlib-tel, piros kerettel az outlier-t tartalmazó mintáknál]

**5. kör — Finomítás:**

> **Te:** A boxploton a minta azonosítók nem férnek el az x-tengelyen. Forgasd el őket 45 fokkal, és csökkentsd a betűméretet.

> **AI:** [Módosított ábra: `plt.xticks(rotation=45, ha='right', fontsize=9)`]

Figyeld meg a mintázatot:
1. **Te mondod meg, mit akarsz** (prompt).
2. **Az AI generálja a kódot**.
3. **Te futtatod és értékeled** — a szaktudásoddal.
4. **Visszajelezel** — hibaüzenet, rossz eredmény, vagy finomítási kérés.
5. **Az AI javít**.

Ebben a ciklusban a **te tudásod a szűk keresztmetszet, nem a programozási képességed**. Ha tudod, hogy a pH 0-14 között van, ezt be tudod építeni. Ha tudod, hogy Debrecenben januárban nem eshet 200 mm csapadék, ezt is. Az AI a technikai megvalósítást intézi.

> **🌾 Szakterületi példa: NDVI-számítás és vegetációs index kódgenerálás**
>
> A geoinformatikában az AI-kódolási asszisztens teljes rasterio-szkriptet generál: Sentinel-2 felvétel betöltése, NDVI-számítás (NDVI = (NIR - Red) / (NIR + Red)), maszkolt zonális statisztika, eredmény mentése GeoTIFF-be. Ha a kód hibás, a hibaüzenet alapján 2-3 iterációban javítja — pontosan a „leírd, generáld, teszteld, finomítsd" ciklust követve. A GeoPandas-, rasterio- és Google Earth Engine-munkafolyamatok tipikus mintáit az LLM-ek már jól ismerik, így a sandbox végrehajtás és iteratív javítás gyorsan eredményre vezet.
>
> *Forrás: gis 21.4.2 „Kódgenerálás: rugalmasság és kockázat"*

---

## 5.8 A prompt-írás művészete kódoláshoz

A kódolási promptok írásának vannak bevált mintázatai. Íme a legfontosabbak tudósok számára.

### 5.8.1 1. Légy konkrét az input-output formátumról

**Rossz prompt:**
> Dolgozd fel az adatfájlokat.

**Jó prompt:**
> A `data/` mappában CSV-fájlok vannak, pontosvessző elválasztóval. Minden fájlban van egy "Datum" (yyyy-mm-dd formátum) és egy "Ertek" (lebegőpontos szám) oszlop. Olvasd be az összeset egy pandas DataFrame-be, adj hozzá egy "Forras" oszlopot a fájlnévvel, és mentsd el `összesített.parquet` formátumban.

### 5.8.2 2. Add meg a szakterületi korlátokat

**Rossz prompt:**
> Szűrd ki a hibás adatokat.

**Jó prompt:**
> Szűrd ki a fizikailag lehetetlen értékeket: hőmérséklet < -50°C vagy > 50°C, páratartalom < 0% vagy > 100%, szélsebesség < 0 m/s. A kiszűrt sorokról készíts egy log-fájlt a fájlnévvel, sorszámmal és az eredeti értékkel.

### 5.8.3 3. Kérd az AI-t, hogy magyarázzon

Ha nem érted, mit csinál a kód, vagy miért úgy csinálja:

> Írd bele a kódba kommentként, hogy mit csinál minden fő lépés, magyarul.

Vagy:

> Magyarázd el egyszerűen, mit csinál a `groupby('Állomás').agg({'Vízszint': ['mean', 'std']})` sor.

### 5.8.4 4. Kérj hibakezelést

> Ha egy fájl nem olvasható, ne álljon le az egész szkript — írd ki a hibás fájlnevet és a hibaüzenetet, és folytassa a következő fájllal.

### 5.8.5 5. Kérj reprodukálható eredményt

> Állíts be random seed-et (42), hogy a eredmények megismételhetők legyenek. Írd ki a használt csomagok verzióit.

---

## 5.9 Gyakori hibák és hogyan kezeld őket

Az AI kódolási asszisztensek nem tökéletesek. Íme a leggyakoribb problémák és megoldásaik.

### 5.9.1 "ModuleNotFoundError: No module named 'xyz'"

**Mit jelent:** Egy csomag nincs telepítve.
**Megoldás:** `pip install xyz` — vagy másold be a hibaüzenetet az AI-nak, és megmondja, mit kell telepíteni.

### 5.9.2 "FileNotFoundError: No such file or directory"

**Mit jelent:** A program nem találja a fájlt.
**Megoldás:** Ellenőrizd az elérési utat. Gyakori hiba, hogy a szkript más mappában fut, mint ahol a fájl van. Mondd az AI-nak: "A fájl a `C:/Users/maria/data/` mappában van, a szkript a `C:/Users/maria/scripts/` mappában fut."

### 5.9.3 Az AI hallucinálja a csomag nevét

Néha az AI egy nem létező csomagot vagy függvényt ajánl. Ha a `pip install` nem találja, kérdezd meg: "A `xyz` csomag valóban létezik? Mi a helyes neve?"

### 5.9.4 A kód lefut, de az eredmény rossz

Ez a legveszélyesebb — **a kód nem dob hibát, de az eredmény értelmetlen**. Ezért kritikus a domain-tudásod. Mindig ellenőrizd:
- Az értékek reális tartományban vannak?
- A sorok/oszlopok száma stimmel?
- Az ábra trendjei logikusak?
- Egyezik a kézi ellenőrzéssel (néhány értéket számolj ki kézzel is)?

### 5.9.5 Az AI "elfelejtette" a korábbi kontextust

Ha egy hosszú beszélgetés közben az AI mintha nem emlékezne a korábbi kéréseidre, a kontextusablak (context window) telítődhetett. Megoldás: kezdj új beszélgetést, és az elején foglald össze, hol tartasz.

---

## 5.10 Jupyter notebook — a digitális laborfüzet

### 5.10.1 Mi az a Jupyter notebook?

Ahogy az 5.3-as alfejezetben említettük, a Jupyter notebook egy interaktív dokumentum, ami **cellákból** áll. Minden cella vagy **kód** (amit lefuttathatsz), vagy **szöveg** (Markdown formátumban, amit formázottan jelenít meg). A cellák sorrendje tetszőleges, és minden kódcella alatt megjelenik az eredménye — legyen az szám, táblázat, grafikon vagy hibaüzenet.

### 5.10.2 Miért szeretik a tudósok?

1. **Lineáris narratíva**: A notebook felülről lefelé olvasható, mint egy cikk. Hipotézis → adatok → elemzés → eredmény → értelmezés.
2. **Azonnali visszajelzés**: A kódcella lefuttatása után az eredmény (grafikon, táblázat) azonnal megjelenik alatta. Nem kell külön ablakban keresni.
3. **Reprodukálhatóság**: Ha megosztod a notebookot egy kollégával, ő lefuttathatja ugyanazt a kódot és (ugyanazokkal az adatokkal) ugyanazt az eredményt kapja.
4. **Dokumentáció és kód egy helyen**: Nem kell külön Word-dokumentumot és külön szkriptet karbantartani.
5. **AI-kompatibilitás**: A GitHub Copilot és más AI eszközök natívan támogatják a Jupyter notebookokat VS Code-ban.

### 5.10.3 Hogyan indítsd el?

```bash
# Ha még nem telepítetted:
pip install jupyter

# Indítás:
jupyter notebook
```

Ez megnyitja a böngészőben a Jupyter felületet. Alternatíva: VS Code-ban is megnyithatsz `.ipynb` fájlokat közvetlenül — sőt, VS Code-ban a Copilot is működik a notebookban.

### 5.10.4 Egy tipikus tudományos notebook felépítése

```
[Markdown cella]
# Debreceni vízminőség-elemzés, 2024
**Szerző:** Kovács Mária
**Dátum:** 2024-03-15

## 1. Adatok betöltése

[Kód cella]
import pandas as pd
df = pd.read_csv('vizminoseg_debrecen_2024.csv')
df.head()

[Eredmény: az első 5 sor táblázatként]

[Markdown cella]
## 2. Leíró statisztikák

[Kód cella]
df.describe()

[Eredmény: min, max, átlag, szórás stb. minden oszlopra]

[Markdown cella]
## 3. pH-eloszlás vizualizáció

[Kód cella]
import matplotlib.pyplot as plt
df['pH'].hist(bins=20, edgecolor='black')
plt.xlabel('pH')
plt.ylabel('Gyakoriság')
plt.title('pH-eloszlás a mintákban')
plt.show()

[Eredmény: hisztogram közvetlenül a cella alatt]

[Markdown cella]
## 4. Következtetések
A pH-értékek normális eloszlást mutatnak, 6.8-7.4 tartományban...
```

### 5.10.5 Jupyter notebook és AI együtt

A legerősebb kombináció: **Jupyter notebook + AI kódolási asszisztens**. A workflow így néz ki:

1. Írsz egy Markdown cellát a szöveges leírással (mit akarsz elemezni, miért).
2. A következő kódcellában az AI kiegészíti a kódot — akár a Copilot inline javaslatával, akár a chat panelen kérve.
3. Lefuttatod a cellát, az eredmény megjelenik.
4. Ha módosítani kell, kijelölöd a cellát és kérsz az AI-tól módosítást.
5. A következő Markdown cellában dokumentálod az eredményt.

Ez a módszer nemcsak hatékony, hanem **automatikusan dokumentálja az elemzésedet** — a kész notebook egy teljes kutatási napló.

---

## 5.11 A legfontosabb Python könyvtárak tudósoknak

Nem kell megtanulnod ezeket a könyvtárakat — az AI fogja használni őket helyetted. De hasznos, ha tudod, mire valók, mert így **pontosabb promptokat írhatsz**.

### 5.11.1 NumPy — a számolás alapja

**Mire való:** Numerikus számítások, vektorok, mátrixok, matematikai műveletek.

**Mikor hivatkozz rá a promptban:** Ha tömbökkel, mátrixokkal vagy matematikai számításokkal dolgozol.

**Tipikus promptok:**
- "NumPy-val számold ki a mátrix sajátértékeit."
- "Generálj 1000 véletlen számot normális eloszlásból, átlag=0, szórás=1."
- "Számold ki a két vektor közötti koszinusz-hasonlóságot."

NumPy a Python numerikus számításainak az alapja — szinte minden más tudományos könyvtár erre épül. Az AI szinte minden tudományos szkriptben használni fogja, még ha te nem is kéred kifejezetten.

### 5.11.2 SciPy — a tudományos svájcibicska

**Mire való:** Tudományos és mérnöki számítások: optimalizálás, interpoláció, integrálás, statisztika, jelfeldolgozás.

**Mikor hivatkozz rá a promptban:** Ha görbeillesztés, optimalizálás, statisztikai tesztek, interpoláció vagy Fourier-analízis kell.

**Tipikus promptok:**
- "Illessz egy Gauss-görbét az adataimra scipy.optimize.curve_fit-tel."
- "Végezz Kolmogorov-Szmirnov tesztet a két minta összehasonlítására."
- "Interpoláld az adatokat kubikus spline-nal."
- "Számold ki a jel FFT-jét (Fast Fourier Transform)."

### 5.11.3 Pandas — az adatkezelés bajnoka

**Mire való:** Táblázatos adatok betöltése, szűrése, átalakítása, összesítése. Gondolj rá úgy, mint egy programozható Excel.

**Mikor hivatkozz rá a promptban:** Ha CSV, Excel vagy adatbázis-adatokkal dolgozol — szűrés, csoportosítás, összesítés, pivot-táblák.

**Tipikus promptok:**
- "Olvasd be a CSV-t pandas-szal, és szűrd ki a 2024 januári sorokat."
- "Csoportosítsd állomásonként és számold ki az átlagot."
- "Készíts egy pivot-táblát: sorok = hónapok, oszlopok = állomások, értékek = átlagos vízszint."
- "Egyesítsd (merge) a két DataFrame-et az 'ID' oszlop alapján."

A Pandas a legtöbbet használt Python könyvtár a tudományos adatelemzésben. Ha táblázatos adataid vannak (és a legtöbb tudósnak vannak), a Pandas lesz a legjobb barátod.

### 5.11.4 Matplotlib — a grafikonok királya

**Mire való:** Ábrák, grafikonok, diagramok készítése — a vonaldiagramtól a 3D felületig.

**Mikor hivatkozz rá a promptban:** Ha bármilyen vizualizációt akarsz — vonaldiagram, szórásdiagram, hisztogram, boxplot, hőtérkép, 3D ábra.

**Tipikus promptok:**
- "Rajzolj egy vonaldiagramot az idősoros adatokból."
- "Készíts egy 2x3-as subplot-elrendezést, minden mérőállomásnak egy ábra."
- "Készíts egy hőtérképet a korrelációs mátrixról."
- "Mentsd el az ábrát 300 DPI-ben, PDF formátumban."

Fontos: a matplotlib kiegészítő könyvtára, a **seaborn**, szebb alapbeállításokat ad. Ha az ábráid "csúnyábbak", mint szeretnéd, kérd: "Használj seaborn stílust."

### 5.11.5 scikit-learn — gépi tanulás egyszerűen

**Mire való:** Gépi tanulás: osztályozás, regresszió, klaszterezés, dimenziócsökkentés.

**Mikor hivatkozz rá a promptban:** Ha mintázatokat keresel az adatokban, osztályozni akarsz, vagy prediktív modellt építesz.

**Tipikus promptok:**
- "Végezz lineáris regressziót a hőmérséklet és a vízszint között."
- "Klaszterezd a mintákat K-means algoritmussal, k=3."
- "Válaszd szét az adatokat tanító (80%) és teszt (20%) halmazra, majd illessz egy random forest modellt."
- "Számold ki a modell R², MAE és RMSE értékeit."

A scikit-learn a "beléptető" a gépi tanulás világába. Nem a legújabb deep learning keretrendszer, de a legtöbb tudományos feladathoz bőven elég, és az API-ja egyszerű, konzisztens.

### 5.11.6 Összefoglaló táblázat

> **🖼️ 5.2. ábra: Python tudományos ökoszisztéma — a legfontosabb csomagok és kapcsolataik**
> *Hálózati diagram: központban a Python logó, körülötte a pandas, numpy, matplotlib, scipy, scikit-learn csomagok, nyilak mutatják a tipikus adatáramlást közöttük.*


| Könyvtár | Fő felhasználás | Mikor kérd az AI-tól |
|----------|----------------|---------------------|
| **NumPy** | Numerikus számítások, tömbök | Matematikai műveletek, mátrixok |
| **SciPy** | Tudományos számítások | Görbeillesztés, statisztikai tesztek, optimalizálás |
| **Pandas** | Táblázatos adatkezelés | CSV/Excel beolvasás, szűrés, összesítés |
| **Matplotlib** | Vizualizáció | Ábrák, grafikonok, publikáció-minőségű képek |
| **scikit-learn** | Gépi tanulás | Osztályozás, regresszió, klaszterezés |

---

## 5.12 Haladó tippek: ha már magabiztosan használod az AI kódolási asszisztenst

### 5.12.1 Kommentek mint promptok

A GitHub Copilot és a Cursor esetében a kódfájlban elhelyezett **kommentek a legjobb promptok**. Ha a Python-fájlod tetejére írod:

```python
# Ez a szkript beolvassa a data/ mappa összes .xlsx fájlját,
# kiszámítja az átlagos pH-t és vezetőképességet mintánként,
# és exportálja az eredményt egy összefoglaló CSV-be.
```

...a Copilot a következő sorokban már a megfelelő kódot fogja javasolni. Minél részletesebb a komment, annál pontosabb a javaslat.

### 5.12.2 Mintaadás (few-shot prompting a kódban)

Ha megírod az első adatfeldolgozó függvényt, a Copilot a második, harmadik, negyedik hasonló függvényt már önállóan ajánlja. Ez a **mintafelismerés** (pattern matching) — a Copilot megtanulja a stílusodat és a konvencióidat.

### 5.12.3 Kontextus-fájlok

Mind a Claude Code, mind a Copilot támogat kontextus-fájlokat:
- **Claude Code**: `CLAUDE.md` fájl a projekt gyökerében — ide írhatod: "Ez egy hidrológiai projekt. A koordináták EOV rendszerben vannak. Az adatok CSV formátumúak, pontosvessző elválasztóval."
- **Copilot**: `.github/copilot-instructions.md` — hasonló célra.

Ezek a fájlok biztosítják, hogy az AI **minden promptnál tudja a kontextust**, anélkül hogy újra elmondanád.

### 5.12.4 Verziókezelés az AI-val generált kóddal

Emlékszel a Git-re? Az AI kódolási asszisztensek mellett a Git duplán fontos:

1. **Commitolj minden sikeres lépés után**. Ha az AI generált egy működő szkriptet, azonnal `git add` + `git commit`.
2. **Brancheket** használj kísérletezéshez. Ha az AI egy teljesen új megközelítést javasol, hozz létre egy új branchet (`git checkout -b uj_megkozelites`), próbáld ki, és ha nem jó, egyszerűen dobd el.
3. **A commit-üzenet legyen informatív**: "pH-szűrő hozzáadva, outlier-ek eltávolítása 14 fölötti pH-nál" — nem "update".

---

## 5.13 Összefoglalás: a paradigmaváltás térképe

> **🖼️ 5.3. ábra: A kódolási paradigmaváltás — hagyományos vs. AI-támogatott fejlesztés**
> *Előtte/utána összehasonlítás: bal oldalon a hagyományos kódolás (kézikönyv olvasás → kódírás → hibakeresés → Stack Overflow), jobb oldalon az AI-támogatott (feladat leírás → AI-generált kód → ellenőrzés → iteráció).*


Ebben a fejezetben megtanultad, hogy:

1. **Nem kell programozóvá válnod** ahhoz, hogy programokat használj a kutatásodban. Te a rendező vagy, az AI a kódíró.

2. **A munkakörnyezet beállítása egyszerű**: Python + VS Code + Git + egy AI kódolási asszisztens. Négy komponens, egyenként 10-15 perc telepítés.

3. **Öt AI kódolási eszköz közül választhatsz**: Claude Code (komplex feladatokhoz), GitHub Copilot (mindennapokra), Cursor (mély integrációhoz), Windsurf (ingyenes belépőhöz), Codex (ChatGPT-felhasználóknak).

4. **Az AI konkrét, működő kódot generál** adattisztításra, vizualizációra, görbeillesztésre, kötegelt feldolgozásra és API-kapcsolódásra.

5. **A visszacsatolási ciklus** (leírd → generáld → teszteld → finomítsd) a kulcs — nem az egyetlen tökéletes prompt, hanem az iteratív finomítás.

6. **A Jupyter notebook** a tudós legjobb barátja: kód, szöveg és eredmények egyetlen dokumentumban.

7. **Öt Python könyvtár** fedi le a legtöbb tudományos feladatot: NumPy, SciPy, Pandas, Matplotlib, scikit-learn.

8. **A Git a biztonsági hálód** — commitolj minden sikeres lépés után.

### 5.13.1 Mi jön ezután?

A következő fejezetekben építünk erre az alapra:
- A **6. fejezetben** az AI-val segített matematikai modellezéssel foglalkozunk — differenciálegyenletek, szimulációk, numerikus módszerek.
- A **7. fejezetben** automatizálási csővezetékeket (pipeline) építünk, amelyek a teljes adatfeldolgozási folyamatot kezelik.
- A **8. fejezetben** a vizuális (no-code) programozási eszközöket mutatjuk be azoknak, akik teljesen kód nélkül akarnak dolgozni.

De ha most azonnal el akarsz kezdeni: nyisd meg a VS Code-ot, aktiváld a Copilotot, és írd be kommentként:

```python
# Olvasd be a mérési adataimat a data.csv fájlból,
# és rajzolj egy vonaldiagramot az idősorról.
```

A Tab billentyű nyomása után az AI írni kezd. Ennyi.

---

> **A fejezet kulcsüzenete**: A programozás megtanulása hónapokba telt. Az AI kódolási asszisztens megtanulása napokba telik. A különbség nem a kód minőségében van — hanem abban, hogy te is megteheted, most rögtön.
