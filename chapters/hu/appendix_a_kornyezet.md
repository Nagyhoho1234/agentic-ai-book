# Függelék A: AI kutatási környezet beállítása

Ez a függelék lépésről lépésre végigvezet minden szükséges eszköz telepítésén és beállításán. A fejezetek példáinak futtatásához ezekre az eszközökre lesz szükséged. Ne ijedj meg a hosszú listától — nem kell mindent egyszerre telepíteni. Kezdd az 1–4. pontokkal (Python, VS Code, Git, virtuális környezet), és a többit akkor telepítsd, amikor az adott fejezethez érsz.

> **Tipp:** Ha elakadsz, a 13. pont (Gyakori problémák) szinte biztosan tartalmazza a megoldást.

---

## A.1 Python telepítés

A Python az AI-kutatás lingua francája. A könyv minden kódpéldája Python 3.10 vagy újabb verziót igényel.

### Windows

1. Nyisd meg a böngészőt, és navigálj a [python.org/downloads](https://www.python.org/downloads/) oldalra.
2. Kattints a sárga **"Download Python 3.12.x"** gombra (vagy az aktuálisan legújabb 3.12+ verzióra).
3. Futtasd a letöltött telepítőt (`python-3.12.x-amd64.exe`).
4. **KRITIKUSAN FONTOS:** Az első képernyőn pipáld be az **"Add python.exe to PATH"** jelölőnégyzetet! Ez a leggyakoribb hiba, amit a hallgatók elkövetnek.
5. Kattints az **"Install Now"** gombra.
6. Várd meg, amíg a telepítés befejeződik, majd kattints a **"Close"** gombra.

Ellenőrzés — nyiss egy új terminált (Windows Terminal vagy PowerShell):

```bash
python --version
```

Várt kimenet: `Python 3.12.x` (vagy újabb).

```bash
pip --version
```

Várt kimenet: `pip 24.x from ...`

> **Megjegyzés:** Ha a `python` parancs nem működik, próbáld a `python3` változatot. Ha az sem, a PATH beállítás maradt ki — lásd az A.13 hibaelhárítás részt.

### macOS

1. Telepítsd a Homebrew csomagkezelőt, ha még nincs (terminálban):

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

2. Telepítsd a Pythont:

```bash
brew install python@3.12
```

3. Ellenőrzés:

```bash
python3 --version
pip3 --version
```

> **Megjegyzés macOS felhasználóknak:** A macOS tartalmaz egy előtelepített Python 2.7-et (régebbi verziók) vagy egy rendszer-Pythont. Ezt **soha ne használd** kutatási célra, mindig a `python3` parancsot használd.

### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

Ellenőrzés:

```bash
python3 --version
pip3 --version
```

### Linux (Fedora/RHEL)

```bash
sudo dnf install python3 python3-pip
```

### Miniconda alternatíva (minden platformon)

Ha adattudományi csomagokkal (NumPy, SciPy, pandas) fogsz dolgozni, a Miniconda telepítés kényelmesebb lehet:

1. Töltsd le a Minicondát: [docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html)
2. Futtasd a telepítőt.
3. Ellenőrzés:

```bash
conda --version
python --version
```

> **Melyiket válaszd?** Ha egyszerű Python-szkripteket és AI API-kat fogsz használni, a sima Python telepítés elég. Ha numerikus számításokat, szimulációkat futtatsz (6., 10. fejezet), a Miniconda kényelmesebb lehet a tudományos csomagok kezelésében.

---

## A.2 VS Code telepítés és beállítás

![VS Code felület tudományos Python projekttel — tipikus elrendezés](images/appendix_a_vscode_layout.png)

A Visual Studio Code (VS Code) egy ingyenes, nyílt forráskódú kódszerkesztő, amely kiválóan alkalmas AI-támogatott fejlesztésre.

### Telepítés

1. Navigálj a [code.visualstudio.com](https://code.visualstudio.com/) oldalra.
2. Töltsd le a platformodnak megfelelő verziót (Windows / macOS / Linux).
3. Futtasd a telepítőt.
   - **Windows:** A telepítőben pipáld be az **"Add to PATH"** és az **"Open with Code"** opciókat.
   - **macOS:** Húzd a VS Code ikont az Applications mappába. Ezután nyisd meg a VS Code-ot, nyomd meg a `Cmd+Shift+P` billentyűkombinációt, írd be: `shell command`, és válaszd az **"Install 'code' command in PATH"** lehetőséget.

4. Ellenőrzés terminálban:

```bash
code --version
```

### Alapvető kiterjesztések telepítése

Nyisd meg a VS Code-ot, majd a bal oldali sávban kattints az Extensions ikonra (vagy `Ctrl+Shift+X`). Keresd meg és telepítsd a következőket:

| Kiterjesztés | Azonosító | Mire jó |
|---|---|---|
| **Python** | `ms-python.python` | Python nyelvi támogatás, IntelliSense, hibakeresés |
| **Jupyter** | `ms-toolsai.jupyter` | Jupyter notebookok futtatása VS Code-ban |
| **GitHub Copilot** | `github.copilot` | AI kódkiegészítés (részletek az A.7 pontban) |
| **GitHub Copilot Chat** | `github.copilot-chat` | AI chat a kódbázisról |
| **Python Environment Manager** | `donjayamanne.python-environment-manager` | Virtuális környezetek kezelése |
| **indent-rainbow** | `oderwat.indent-rainbow` | Behúzások vizualizálása (hasznos Pythonban) |

Telepítés parancssorból (az összes egyszerre):

```bash
code --install-extension ms-python.python
code --install-extension ms-toolsai.jupyter
code --install-extension github.copilot
code --install-extension github.copilot-chat
code --install-extension donjayamanne.python-environment-manager
code --install-extension oderwat.indent-rainbow
```

### VS Code beállítások tudományos munkához

Nyisd meg a beállításokat (`Ctrl+,`), majd kattints a jobb felső sarokban lévő `{}` ikonra a JSON nézethez. Add hozzá:

```json
{
    "editor.fontSize": 14,
    "editor.wordWrap": "on",
    "editor.formatOnSave": true,
    "python.analysis.typeCheckingMode": "basic",
    "files.autoSave": "afterDelay",
    "files.autoSaveDelay": 1000,
    "jupyter.askForKernelRestart": false
}
```

---

## A.3 Git alapok

A Git egy verziókezelő rendszer. Miért fontos ez kutatóknak?

- **Visszafordíthatóság:** Ha egy kísérlet rosszul sül el, visszatérhetsz a korábbi állapothoz.
- **Dokumentáció:** Minden változás automatikusan naplózva van — ki, mit, mikor módosított.
- **Együttműködés:** Több kutató dolgozhat párhuzamosan ugyanazon a projekten.
- **Reprodukálhatóság:** A kód pontos állapota bármikor visszaállítható (pl. egy publikáció idején).

### Git telepítés

**Windows:**

1. Töltsd le a Git for Windows-t: [git-scm.com/download/win](https://git-scm.com/download/win)
2. Futtasd a telepítőt. Az alapértelmezett beállítások megfelelők, de figyelj a következőkre:
   - **Default editor:** válaszd a "Use Visual Studio Code as Git's default editor" opciót.
   - **PATH environment:** válaszd a "Git from the command line and also from 3rd-party software" opciót.

**macOS:**

```bash
brew install git
```

Vagy: a terminálban írd be `git --version` — ha nincs telepítve, a rendszer felajánlja az Xcode Command Line Tools telepítését.

**Linux:**

```bash
sudo apt install git          # Ubuntu/Debian
sudo dnf install git          # Fedora/RHEL
```

### Alapbeállítás (egyszeri, minden platformon)

```bash
git config --global user.name "Neved"
git config --global user.email "email@example.com"
```

### Az 5 legfontosabb Git parancs

**1. Új projekt inicializálása:**

```bash
cd ~/projektek/uj_kutatas
git init
```

Ez létrehoz egy `.git` mappát, ami a teljes verziótörténetet tárolja.

**2. Fájlok hozzáadása a követéshez:**

```bash
git add script.py              # egyetlen fájl hozzáadása
git add *.py                   # minden Python fájl
git add -A                     # minden változás
```

**3. Változások mentése (commit):**

```bash
git commit -m "Első verzió: adatbeolvasás implementálva"
```

A commit üzenet legyen informatív! Nem jó: `"update"`. Jó: `"Gauss-illesztés hozzáadása a spektrumadatokhoz"`.

**4. Állapot ellenőrzése:**

```bash
git status
```

Ez megmutatja, mely fájlok változtak, melyek vannak „staged" állapotban, és melyek nincsenek követve.

**5. Előzmények megtekintése:**

```bash
git log --oneline
```

### Tipikus munkafolyamat

```bash
# 1. Módosítod a kódot
# 2. Megnézed, mi változott
git status

# 3. Hozzáadod a változásokat
git add -A

# 4. Mentesz egy pillanatképet
git commit -m "Kalibráció: R² = 0.97, 200 iteráció után"

# 5. Tovább dolgozol...
```

### GitHub fiók létrehozása

1. Navigálj a [github.com](https://github.com) oldalra.
2. Kattints a **"Sign up"** gombra.
3. Add meg az email címed, válassz egy felhasználónevet és jelszót.
4. Egyetemi email cím esetén igényelj **GitHub Education** csomagot: [education.github.com](https://education.github.com) — ez ingyenes GitHub Copilot hozzáférést ad!

### Projekt feltöltése GitHubra

Miután létrehoztad a repository-t a GitHub weboldalán:

```bash
git remote add origin https://github.com/felhasznalonev/repo-neve.git
git branch -M main
git push -u origin main
```

### .gitignore fájl

Hozz létre egy `.gitignore` fájlt a projekt gyökerében, hogy a Git ne kövesse a felesleges fájlokat:

```
# Python
__pycache__/
*.pyc
*.pyo
.venv/
venv/

# Jupyter
.ipynb_checkpoints/

# Környezeti változók (API kulcsok!)
.env

# Adatfájlok (ha túl nagyok)
*.csv
*.hdf5
data/raw/

# OS fájlok
.DS_Store
Thumbs.db

# IDE
.vscode/
.idea/
```

> **FONTOS:** Az `.env` fájlt (API kulcsok) **soha** ne commitold! Lásd az A.8 részt.

---

## A.4 Virtuális környezetek

### Miért kellenek virtuális környezetek?

Képzeld el, hogy van két projekted:
- **Projekt A** igényli a `numpy==1.24` verziót.
- **Projekt B** igényli a `numpy==2.0` verziót.

Ha mindkettőt a rendszer-Pythonba telepíted, konfliktus lesz. A virtuális környezet egy izolált Python-telepítés, ami csak az adott projekthez tartozik.

**Tudományos reprodukálhatóság szempontjából is kritikus:** ha leírod, hogy pontosan milyen csomagverziókkal kaptad az eredményeidet, más kutatók pontosan reprodukálhatják a kísérleted.

### Virtuális környezet létrehozása

```bash
# Navigálj a projekt mappájába
cd ~/projektek/uj_kutatas

# Hozd létre a virtuális környezetet (.venv nevű mappában)
python -m venv .venv
```

> **Megjegyzés:** Linuxon és macOS-en `python3 -m venv .venv` lehet szükséges.

### Aktiválás

**Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
.venv\Scripts\activate.bat
```

**Windows (Git Bash / MSYS2):**
```bash
source .venv/Scripts/activate
```

**macOS / Linux:**
```bash
source .venv/bin/activate
```

Ha sikerült, a terminál prompt elé kiíródik a `(.venv)` prefix:

```
(.venv) felhasznalo@gep:~/projektek/uj_kutatas$
```

### Csomagok telepítése a virtuális környezetbe

```bash
# Egyetlen csomag
pip install numpy

# Több csomag egyszerre
pip install numpy pandas matplotlib scipy

# Konkrét verzió
pip install numpy==1.26.4
```

### requirements.txt létrehozása és használata

A `requirements.txt` fájl rögzíti a projekt összes függőségét pontos verziószámmal.

**Létrehozás (a jelenlegi környezetből):**

```bash
pip freeze > requirements.txt
```

**Telepítés (másik gépen vagy új környezetben):**

```bash
pip install -r requirements.txt
```

Példa `requirements.txt` tartalomra:

```
numpy==1.26.4
pandas==2.2.0
matplotlib==3.8.2
scipy==1.12.0
scikit-learn==1.4.0
anthropic==0.18.0
openai==1.12.0
python-dotenv==1.0.1
```

### Deaktiválás

```bash
deactivate
```

### VS Code integráció

A VS Code automatikusan felismeri a `.venv` mappát. Ha mégsem:

1. Nyomd meg a `Ctrl+Shift+P` billentyűkombinációt.
2. Írd be: `Python: Select Interpreter`.
3. Válaszd ki a `.venv` mappában lévő Python értelmezőt.

---

## A.5 Claude Code telepítés és beállítás

A Claude Code az Anthropic hivatalos parancssori eszköze, amely lehetővé teszi, hogy Claude közvetlenül a terminálodból dolgozzon a kódoddal.

### Előfeltételek

- **Node.js 18+** szükséges. Ha még nincs telepítve:

**Windows:**
1. Töltsd le a Node.js-t: [nodejs.org](https://nodejs.org/) (LTS verzió ajánlott).
2. Futtasd a telepítőt, az alapértelmezett beállításokkal.

**macOS:**
```bash
brew install node
```

**Linux:**
```bash
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs
```

Ellenőrzés:

```bash
node --version    # Várt: v20.x vagy újabb
npm --version     # Várt: 10.x vagy újabb
```

### Claude Code telepítés

```bash
npm install -g @anthropic-ai/claude-code
```

> **Windows-megjegyzés:** Ha „permission denied" hibát kapsz, futtasd a terminált rendszergazdaként, vagy használd:
> ```bash
> npm install -g @anthropic-ai/claude-code --prefix "$HOME/.npm-global"
> ```
> Majd add hozzá a `$HOME/.npm-global/bin` útvonalat a PATH-hoz.

### API kulcs beállítása

1. Szerezz egy Anthropic API kulcsot (lásd A.8 rész).
2. Állítsd be környezeti változóként:

**Windows (PowerShell, ideiglenes):**
```powershell
$env:ANTHROPIC_API_KEY = "sk-ant-api03-..."
```

**Windows (tartós, PowerShell):**
```powershell
[System.Environment]::SetEnvironmentVariable("ANTHROPIC_API_KEY", "sk-ant-api03-...", "User")
```

**macOS / Linux:**
```bash
export ANTHROPIC_API_KEY="sk-ant-api03-..."
```

Tartós beállításhoz add hozzá a `~/.bashrc` vagy `~/.zshrc` fájlhoz:

```bash
echo 'export ANTHROPIC_API_KEY="sk-ant-api03-..."' >> ~/.bashrc
source ~/.bashrc
```

> **Jobb megoldás:** Használj `.env` fájlt — lásd az A.8 részt.

### Első használat

```bash
# Navigálj a projektedbe
cd ~/projektek/uj_kutatas

# Indítsd el a Claude Code-ot
claude
```

A Claude Code interaktív módban indul. Próbáld ki:

```
> Hozz létre egy Python szkriptet, ami beolvassa a data.csv fájlt és kirajzolja az első oszlop hisztogramját.
```

### Hasznos Claude Code parancsok

```bash
claude                          # Interaktív mód
claude "kérdés a kódról"       # Egyszeri kérdés
claude -p "feladat leírása"    # Print mód (nem interaktív)
```

Interaktív módban:

| Parancs | Funkció |
|---|---|
| `/help` | Súgó megjelenítése |
| `/clear` | Beszélgetés törlése |
| `/cost` | Eddigi API-költség |
| `Ctrl+C` | Kilépés |

---

## A.6 Cursor telepítés

A Cursor egy VS Code-alapú kódszerkesztő, amely natív AI-integrációval rendelkezik. Ha már ismered a VS Code-ot, otthon fogod érezni magad.

### Telepítés

1. Navigálj a [cursor.com](https://www.cursor.com/) oldalra.
2. Kattints a **"Download"** gombra.
3. Futtasd a telepítőt.
4. Az első indítás során a Cursor felajánlja a VS Code beállítások és kiterjesztések importálását — fogadd el.

### Beállítás

1. **Bejelentkezés:** A Cursor kéri, hogy hozz létre egy fiókot vagy jelentkezz be. Ez szükséges az AI funkciókhoz.
2. **Modell kiválasztása:** A `Ctrl+Shift+P` → `Cursor Settings` menüben kiválaszthatod, melyik AI-modellt használod:
   - **Claude Sonnet / Opus** — kiváló kódértéshez és generáláshoz
   - **GPT-4o** — jó általános célokra
   - Saját API kulcsot is megadhatsz (Settings → Models)

### Legfontosabb Cursor funkciók

| Billentyű | Funkció |
|---|---|
| `Ctrl+K` | AI-utasítás a kijelölt kódra (szerkesztés, javítás, magyarázat) |
| `Ctrl+L` | AI chat megnyitása (kérdezz a kódbázisról) |
| `Ctrl+I` | Composer — összetett feladatok, több fájl egyidejű módosítása |
| `Tab` | AI kódkiegészítés elfogadása |

### Saját API kulcs használata

Ha saját Anthropic vagy OpenAI API kulcsod van:

1. Nyisd meg: `File` → `Preferences` → `Cursor Settings` → `Models`
2. Add meg az API kulcsot a megfelelő mezőben.
3. Válaszd ki az alapértelmezett modellt.

> **Tipp:** A Cursor ingyenes szintje korlátozott számú kérést enged. Egyetemi kutatáshoz érdemes a Pro előfizetést (`$20/hó`) vagy a saját API kulcsot fontolóra venni.

---

## A.7 GitHub Copilot beállítás

A GitHub Copilot egy AI-alapú kódkiegészítő, amely közvetlenül a VS Code-ban (és más szerkesztőkben) működik.

### Előfizetés

1. Navigálj a [github.com/features/copilot](https://github.com/features/copilot) oldalra.
2. Válaszd az **Individual** tervet ($10/hó vagy $100/év).
3. **Egyetemi hallgatók és oktatók:** A [GitHub Education](https://education.github.com/) program keretében **ingyenesen** használhatod! Regisztrálj `.edu` email címmel.

### VS Code kiterjesztés telepítése

Ha még nem tetted meg az A.2 lépésnél:

```bash
code --install-extension github.copilot
code --install-extension github.copilot-chat
```

Vagy a VS Code-ban: `Ctrl+Shift+X` → keress rá: "GitHub Copilot" → Install.

### Bejelentkezés

1. A telepítés után a VS Code bal alsó sarkában megjelenik a GitHub Copilot ikon.
2. Kattints rá, majd válaszd a **"Sign in to GitHub"** lehetőséget.
3. A böngészőben engedélyezd a hozzáférést.

### Használat

A Copilot automatikusan működik gépelés közben:

- Írj egy kommentet, ami leírja, mit szeretnél:
  ```python
  # Olvasd be a CSV fájlt és számítsd ki az oszlopok átlagát
  ```
  A Copilot felajánlja a kódot — nyomd meg a `Tab`-ot az elfogadáshoz.

- **Copilot Chat** (`Ctrl+Shift+I`): Kérdéseket tehetsz fel a kódról természetes nyelven.

- **Inline chat** (`Ctrl+I`): Jelölj ki kódrészletet, és kérd a Copilot-ot, hogy javítsa, magyarázza meg, vagy optimalizálja.

### Beállítások finomhangolása

`Ctrl+,` → keress rá: "copilot":

- **Enable/Disable languages:** Kiválaszthatod, mely nyelvekhez legyen aktív.
- **Inline suggestions:** Be/ki kapcsolás.

---

## A.8 API kulcsok kezelése

Az AI-modellek használatához API kulcsokra van szükséged. Ez a rész bemutatja, hogyan szerezheted meg és hogyan kezeld biztonságosan őket.

### Claude API (Anthropic)

1. Navigálj a [console.anthropic.com](https://console.anthropic.com/) oldalra.
2. Regisztrálj vagy jelentkezz be.
3. Kattints a bal oldali menüben az **"API Keys"** elemre.
4. Kattints a **"Create Key"** gombra.
5. Adj nevet a kulcsnak (pl. `kutatas-2026`).
6. **Másold ki azonnal** — a kulcs többé nem jelenik meg!

A kulcs formátuma: `sk-ant-api03-...`

**Árazás (2026 tavaszi árak, tájékoztató jellegű):**

| Modell | Input (1M token) | Output (1M token) |
|---|---|---|
| Claude Sonnet 4 | $3 | $15 |
| Claude Opus 4 | $15 | $75 |
| Claude Haiku 3.5 | $0.80 | $4 |

> **Tipp:** Kutatási célokra a Sonnet az ár-érték bajnok. Az Opus-t akkor használd, ha komplex érvelésre van szükség.

### OpenAI API

1. Navigálj az [platform.openai.com](https://platform.openai.com/) oldalra.
2. Regisztrálj vagy jelentkezz be.
3. Bal oldali menü → **"API keys"** → **"Create new secret key"**.
4. Másold ki a kulcsot.

A kulcs formátuma: `sk-proj-...`

### Google Gemini API

1. Navigálj a [aistudio.google.com](https://aistudio.google.com/) oldalra.
2. Kattints a **"Get API key"** gombra.
3. Válassz egy Google Cloud projektet (vagy hozz létre újat).
4. Másold ki a kulcsot.

A kulcs formátuma: `AIza...`

### API kulcsok biztonságos tárolása (.env fájl)

**SOHA ne írd bele az API kulcsot közvetlenül a kódba!** Ez a legnagyobb biztonsági hiba, amit elkövethetsz.

**1. Hozd létre a `.env` fájlt a projekt gyökerében:**

```
# .env - EZT A FÁJLT SOHA NE COMMITOLD!
ANTHROPIC_API_KEY=sk-ant-api03-ide-a-te-kulcsod
OPENAI_API_KEY=sk-proj-ide-a-te-kulcsod
GOOGLE_API_KEY=AIzaide-a-te-kulcsod
```

**2. Add hozzá a `.gitignore` fájlhoz:**

```
.env
```

**3. Telepítsd a `python-dotenv` csomagot:**

```bash
pip install python-dotenv
```

**4. Használat Python kódban:**

```python
import os
from dotenv import load_dotenv

load_dotenv()  # Betölti a .env fájl tartalmát

api_key = os.getenv("ANTHROPIC_API_KEY")
```

### Költségek nyomon követése

- **Anthropic:** [console.anthropic.com/settings/billing](https://console.anthropic.com/settings/billing)
- **OpenAI:** [platform.openai.com/usage](https://platform.openai.com/usage)
- **Google:** [console.cloud.google.com/billing](https://console.cloud.google.com/billing)

**Költségkeret beállítása:**

Minden platformon beállíthatsz havi költségkeretet (spending limit). **Mindenképpen állíts be egyet!** Egy végtelen ciklusban futó API-hívás rövid idő alatt több száz dollárt költhet.

- Anthropic: Console → Settings → Billing → Spending limit
- OpenAI: Platform → Settings → Billing → Usage limits

> **Tipp kutatóknak:** Egy tipikus kutatási nap 1–5 dollárba kerül Sonnet-tel. Ha 10 dollár felett vagy naponta, valószínűleg optimalizálhatod a promptjaidat (rövidebb kontextus, kevesebb felesleges hívás).

---

## A.9 Komondor szuperszámítógép hozzáférés

A Debreceni Egyetem kutatói és hallgatói hozzáférhetnek a KIFÜ (Kormányzati Informatikai Fejlesztési Ügynökség) által üzemeltetett **Komondor** szuperszámítógéphez. Ez különösen hasznos nagy számítási igényű feladatokhoz: gépi tanulás betanítása, nagy szimulációk, párhuzamos feldolgozás.

### Regisztráció

1. Navigálj a [hpc.kifu.hu](https://hpc.kifu.hu/) oldalra.
2. Kattints a **"Regisztráció"** vagy **"Hozzáférés igénylése"** gombra.
3. Töltsd ki az űrlapot:
   - Intézmény: Debreceni Egyetem
   - Témavezető adatai
   - Projekt leírása (röviden, 2-3 mondat elég)
4. Várd meg a jóváhagyást (általában 1-5 munkanap).

### SSH hozzáférés beállítása

**SSH kulcspár generálása (ha még nincs):**

```bash
ssh-keygen -t ed25519 -C "email@example.com"
```

Nyomd meg az Entert az alapértelmezett helyre mentéshez (`~/.ssh/id_ed25519`). Adj meg egy jelszót (passphrase).

**A publikus kulcs feltöltése:**

```bash
cat ~/.ssh/id_ed25519.pub
```

Másold ki a kimenetet, és töltsd fel a KIFÜ portálon a felhasználói profilodba.

**Csatlakozás:**

```bash
ssh felhasznalonev@komondor.hpc.kifu.hu
```

**SSH config beállítása (kényelmi):** Add hozzá a `~/.ssh/config` fájlhoz:

```
Host komondor
    HostName komondor.hpc.kifu.hu
    User felhasznalonev
    IdentityFile ~/.ssh/id_ed25519
```

Ezután elég ennyi:

```bash
ssh komondor
```

### A modularendszer

A Komondoron a szoftvereket **modulokkal** kezeled:

```bash
# Elérhető modulok listázása
module avail

# Python modul betöltése
module load python/3.11

# CUDA betöltése (GPU-s számításokhoz)
module load cuda/12.2

# Betöltött modulok listázása
module list

# Modul eltávolítása
module unload python/3.11
```

### Python környezet a Komondoron

```bash
# Modul betöltése
module load python/3.11

# Virtuális környezet létrehozása
python -m venv ~/venvs/kutatas

# Aktiválás
source ~/venvs/kutatas/bin/activate

# Csomagok telepítése
pip install numpy scipy pandas matplotlib anthropic
```

> **FONTOS:** A login node-on ne futtass számításigényes feladatokat! Mindig a SLURM job rendszert használd.

### SLURM job küldés

Hozz létre egy job szkriptet (`job.sh`):

```bash
#!/bin/bash
#SBATCH --job-name=ai_kutatas
#SBATCH --partition=gpu
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G
#SBATCH --time=04:00:00
#SBATCH --output=output_%j.log
#SBATCH --error=error_%j.log

module load python/3.11
module load cuda/12.2
source ~/venvs/kutatas/bin/activate

python train_model.py
```

**Job küldés:**

```bash
sbatch job.sh
```

**Job állapot ellenőrzése:**

```bash
squeue -u $USER              # Saját jobok listázása
scancel <job_id>             # Job törlése
sacct -j <job_id> --brief   # Befejezett job statisztikái
```

### Fájlok másolása

```bash
# Helyi gépről a Komondorra
scp adatok.csv komondor:~/projektek/

# Komondorról a helyi gépre
scp komondor:~/projektek/eredmeny.csv ./

# Egész mappa másolása
scp -r komondor:~/projektek/output/ ./eredmenyek/
```

> **Tipp:** Nagyobb fájlok átviteléhez használd az `rsync` parancsot:
> ```bash
> rsync -avz --progress ./nagy_adat/ komondor:~/projektek/nagy_adat/
> ```

---

## A.10 Docker alapok

A Docker lehetővé teszi, hogy az alkalmazásodat és annak minden függőségét egy „konténerbe" csomagold. Ez a reprodukálhatóság arany standardja.

### Miért fontos a konténerizáció?

Képzeld el: írsz egy Python szkriptet, ami tökéletesen fut a gépeden. Elküldöd egy kollégának, és nála nem működik — más Python verzió, hiányzó rendszerkönyvtár, eltérő operációs rendszer. A Docker ezt a problémát oldja meg: a konténer tartalmazza az operációs rendszert, a Pythont, minden csomagot, és pontosan úgy fut bárhol.

**Analógia:** A virtuális környezet (venv) csak a Python csomagokat izolálja. A Docker az **egész operációs rendszert** izolálja.

### Docker Desktop telepítés

**Windows:**

1. **Előfeltétel:** Engedélyezd a WSL 2-t (Windows Subsystem for Linux):
   ```powershell
   wsl --install
   ```
   Indítsd újra a gépet.

2. Töltsd le a Docker Desktop-ot: [docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop/)
3. Futtasd a telepítőt.
4. Az első indítás során válaszd a **"Use WSL 2 based engine"** opciót.

**macOS:**

```bash
brew install --cask docker
```

Vagy töltsd le a Docker Desktop-ot a weboldalról.

**Linux (Ubuntu):**

```bash
# Hivatalos Docker repository hozzáadása
sudo apt update
sudo apt install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Docker futtatása sudo nélkül
sudo usermod -aG docker $USER
newgrp docker
```

**Ellenőrzés:**

```bash
docker --version
docker run hello-world
```

### Alapfogalmak

| Fogalom | Jelentés |
|---|---|
| **Image** | Egy „pillanatkép" — az operációs rendszer + szoftver + kód sablona |
| **Container** | Egy futó példánya az image-nek |
| **Dockerfile** | Recept az image elkészítéséhez |
| **Docker Hub** | Online „áruház" kész image-ekhez |

### Alapvető parancsok

```bash
# Image letöltése a Docker Hub-ról
docker pull python:3.12-slim

# Konténer indítása interaktív módban
docker run -it python:3.12-slim bash

# Konténer indítása a jelenlegi mappa csatolásával
docker run -it -v $(pwd):/app -w /app python:3.12-slim bash

# Futó konténerek listázása
docker ps

# Minden konténer (futó és leállított)
docker ps -a

# Konténer leállítása
docker stop <container_id>

# Letöltött image-ek listázása
docker images

# Takarítás (nem használt image-ek, konténerek törlése)
docker system prune
```

### Dockerfile készítése tudományos projekthez

Hozz létre egy `Dockerfile` nevű fájlt a projekt gyökerében:

```dockerfile
# Alap image
FROM python:3.12-slim

# Munkamappa beállítása
WORKDIR /app

# Függőségek másolása és telepítése
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Projekt fájlok másolása
COPY . .

# Alapértelmezett parancs
CMD ["python", "main.py"]
```

**Image építése:**

```bash
docker build -t kutatas-projekt .
```

**Futtatás:**

```bash
docker run kutatas-projekt
```

**Futtatás interaktív módban, adatmappa csatolásával:**

```bash
docker run -it -v $(pwd)/data:/app/data kutatas-projekt bash
```

### Docker Compose több szolgáltatáshoz

Ha a projekted több komponensből áll (pl. adatbázis + API + elemzés), hozz létre egy `docker-compose.yml` fájlt:

```yaml
version: "3.9"
services:
  analysis:
    build: .
    volumes:
      - ./data:/app/data
      - ./results:/app/results
    environment:
      - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}

  jupyter:
    image: jupyter/scipy-notebook
    ports:
      - "8888:8888"
    volumes:
      - ./notebooks:/home/jovyan/work
```

Indítás:

```bash
docker compose up
```

---

## A.11 pip csomagolás

Ha írsz egy hasznos Python eszközt (pl. egy adatfeldolgozó könyvtárat), érdemes úgy csomagolni, hogy más kutatók is egyszerűen telepíthessék: `pip install az-en-csomagom`.

### Minimális projektstruktúra

```
az_en_csomagom/
├── pyproject.toml          # Csomag metaadatai
├── README.md               # Leírás
├── LICENSE                  # Licenc
├── src/
│   └── az_en_csomagom/
│       ├── __init__.py     # Csomag inicializáló
│       └── core.py         # Fő kód
├── tests/
│   └── test_core.py        # Tesztek
└── requirements.txt        # Függőségek
```

### pyproject.toml

Ez a modern Python csomagolás központi fájlja (a régi `setup.py`-t váltotta le):

```toml
[build-system]
requires = ["setuptools>=68.0", "wheel"]
build-backend = "setuptools.backends._legacy:_Backend"

[project]
name = "az-en-csomagom"
version = "0.1.0"
description = "Rövid leírás a csomagról"
readme = "README.md"
license = {text = "MIT"}
requires-python = ">=3.10"
authors = [
    {name = "Neved", email = "email@example.com"}
]
dependencies = [
    "numpy>=1.24",
    "pandas>=2.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "black>=23.0",
]

[project.scripts]
az-en-parancs = "az_en_csomagom.core:main"
```

### `__init__.py`

```python
"""Az én csomagom — rövid leírás."""

from .core import main_function

__version__ = "0.1.0"
```

### Helyi telepítés fejlesztési módban

```bash
pip install -e .
```

Ez „szerkeszthető" módban telepíti a csomagot — ha módosítod a forráskódot, a változások azonnal érvényre jutnak, nem kell újratelepíteni.

### Csomag építése és feltöltése a PyPI-ra

```bash
# Építő eszközök telepítése
pip install build twine

# Csomag építése
python -m build

# Ez létrehozza a dist/ mappát:
# dist/az_en_csomagom-0.1.0-py3-none-any.whl
# dist/az_en_csomagom-0.1.0.tar.gz

# Feltöltés a Test PyPI-ra (teszt célból)
twine upload --repository testpypi dist/*

# Feltöltés az éles PyPI-ra
twine upload dist/*
```

> **Előfeltétel:** Regisztrálj a [pypi.org](https://pypi.org/) oldalon, és hozz létre egy API tokent.

Ezután bárki telepítheti:

```bash
pip install az-en-csomagom
```

---

## A.12 Ajánlott hardver

### Minimális konfiguráció (fejezetek 1–5, 7–9)

Ez elegendő az AI API-k használatához, adatelemzéshez és alapvető kódoláshoz:

| Komponens | Minimum |
|---|---|
| **Processzor** | Intel i5 / AMD Ryzen 5 (4+ mag) |
| **Memória** | 8 GB RAM |
| **Tárhely** | 256 GB SSD |
| **GPU** | Nem szükséges (a számítás a felhőben történik) |
| **Internet** | Stabil kapcsolat (az API-hívásokhoz szükséges) |

### Ajánlott konfiguráció (minden fejezet, helyi modellek futtatásához)

| Komponens | Ajánlott |
|---|---|
| **Processzor** | Intel i7/i9 vagy AMD Ryzen 7/9 (8+ mag) |
| **Memória** | 32 GB RAM (64 GB ideális) |
| **Tárhely** | 1 TB NVMe SSD |
| **GPU** | NVIDIA RTX 4070 vagy jobb (12+ GB VRAM) |
| **Internet** | Stabil, 50+ Mbps |

### GPU szempontok

Ha helyi gépi tanulási modelleket szeretnél futtatni:

- **NVIDIA GPU szükséges** — az AMD és Intel GPU-k támogatása még korlátozott a gépi tanulásban.
- **VRAM a meghatározó:**
  - 8 GB VRAM: Kis modellek (7B paraméter)
  - 12 GB VRAM: Közepes modellek (13B paraméter)
  - 24 GB VRAM: Nagy modellek (30B+ paraméter)
- **CUDA telepítés szükséges:** [developer.nvidia.com/cuda-downloads](https://developer.nvidia.com/cuda-downloads)

> **Megjegyzés:** A könyv legtöbb példája felhő-alapú AI API-kat használ (Claude, GPT, Gemini), amelyekhez **nem kell GPU**. A GPU csak helyi modellekhez és nagy szimulációkhoz szükséges.

### Felhő alternatívák

Ha nincs erős géped, a felhő kiváló megoldás:

**Google Colab (ingyenes / $10/hó Pro):**
- [colab.research.google.com](https://colab.research.google.com)
- Ingyenes szinten: T4 GPU, 12 GB RAM
- Pro szinten: A100 GPU, 52 GB RAM
- Jupyter notebook felület, Google Drive integráció
- **Ideális:** Gyors prototípusokhoz, kisebb kísérletekhez

**Vast.ai (pay-per-use):**
- [vast.ai](https://vast.ai)
- Olcsó GPU bérlés ($0.10–1.00/óra)
- **Ideális:** Hosszabb betanítási feladatokhoz

**AWS / Azure / GCP:**
- Professzionális felhő platformok
- Bonyolultabb beállítás, de maximális rugalmasság
- Egyetemi kredit programok elérhetők (AWS Educate, Azure for Students, GCP for Education)

**Lightning.ai:**
- [lightning.ai](https://lightning.ai)
- GPU-s fejlesztői környezet a felhőben
- VS Code felület böngészőből
- **Ideális:** Ha nem akarsz helyi GPU-val bajlódni

---

## A.13 Gyakori problémák és megoldások

### Python nem található (PATH probléma)

**Tünet:** `python: command not found` vagy `'python' is not recognized`

**Megoldás Windows-on:**

1. Keresd meg a Python telepítési helyét (általában `C:\Users\<neved>\AppData\Local\Programs\Python\Python312\`).
2. Nyisd meg a rendszerbeállításokat: Start → „Rendszerkörnyezeti változók szerkesztése" → Környezeti változók.
3. A „Path" változóhoz add hozzá:
   - `C:\Users\<neved>\AppData\Local\Programs\Python\Python312\`
   - `C:\Users\<neved>\AppData\Local\Programs\Python\Python312\Scripts\`
4. Nyiss egy **új** terminált (a régi nem fogja látni a változást).

**Megoldás macOS/Linux-on:**

```bash
# Ellenőrizd, hol van a Python
which python3

# Ha megtalálta, hozz létre alias-t
echo 'alias python=python3' >> ~/.bashrc
echo 'alias pip=pip3' >> ~/.bashrc
source ~/.bashrc
```

### pip nem működik

**Tünet:** `pip: command not found`

**Megoldás:**

```bash
# Használd a Python modulként
python -m pip install csomagnev

# Ha ez sem működik, telepítsd a pip-et
python -m ensurepip --upgrade
```

### Permission denied (engedély megtagadva)

**Tünet:** `ERROR: Could not install packages due to an EnvironmentError: [Errno 13] Permission denied`

**Megoldás:** Soha ne használj `sudo pip install`-t! Helyette:

```bash
# Használj virtuális környezetet (ajánlott!)
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows
pip install csomagnev

# VAGY telepíts felhasználói szintre
pip install --user csomagnev
```

### SSL tanúsítvány hiba

**Tünet:** `SSL: CERTIFICATE_VERIFY_FAILED` vagy `SSLCertVerificationError`

**Megoldás macOS-on:**

```bash
# Futtasd a tanúsítvány-telepítőt
/Applications/Python\ 3.12/Install\ Certificates.command
```

**Megoldás Windows-on / vállalati hálózaton:**

```bash
# Ideiglenes megoldás (nem biztonságos, csak tesztelésre!)
pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org csomagnev
```

Ha ez segít, a probléma a vállalati proxy/tűzfal. Kérd az IT osztályt, hogy adja hozzá a `pypi.org` domaint az engedélyezett listához.

### Proxy beállítás

**Tünet:** A pip, git, vagy API-hívások nem érik el az internetet, „connection timed out" hibával.

**Megoldás:**

```bash
# pip proxy beállítás
pip install --proxy http://proxy.egyetem.hu:8080 csomagnev

# Tartós beállítás — hozd létre/szerkeszd a pip.conf fájlt
# Linux/macOS: ~/.config/pip/pip.conf
# Windows: %APPDATA%\pip\pip.ini
```

```ini
[global]
proxy = http://proxy.egyetem.hu:8080
trusted-host = pypi.org
               pypi.python.org
               files.pythonhosted.org
```

```bash
# Git proxy beállítás
git config --global http.proxy http://proxy.egyetem.hu:8080
git config --global https.proxy http://proxy.egyetem.hu:8080

# Python kódban (API hívásoknál)
import os
os.environ["HTTP_PROXY"] = "http://proxy.egyetem.hu:8080"
os.environ["HTTPS_PROXY"] = "http://proxy.egyetem.hu:8080"
```

### Tűzfal blokkolja az API-hívásokat

**Tünet:** `ConnectionError`, `TimeoutError`, vagy `403 Forbidden` API hívásoknál.

**Lehetséges okok és megoldások:**

1. **Vállalati/egyetemi tűzfal:** Kérd az IT osztályt, hogy engedélyezze a következő domaineket:
   - `api.anthropic.com` (Claude)
   - `api.openai.com` (GPT)
   - `generativelanguage.googleapis.com` (Gemini)
   - `github.com`, `raw.githubusercontent.com` (Git)
   - `pypi.org`, `files.pythonhosted.org` (pip)

2. **VPN:** Néhány egyetemi hálózaton VPN-en keresztül működnek az API-k. Ellenőrizd, hogy a VPN aktív-e.

3. **Windows tűzfal:** Start → „Windows Defender tűzfal" → „Alkalmazás engedélyezése a tűzfalon" → Engedélyezd a Python és a Node.js számára.

### Jupyter notebook kernel nem indul

**Tünet:** „Kernel not found" vagy „Dead kernel" a VS Code-ban.

**Megoldás:**

```bash
# Győződj meg róla, hogy a virtuális környezet aktív
source .venv/bin/activate

# Telepítsd az ipykernel-t
pip install ipykernel

# Regisztráld a kernelt
python -m ipykernel install --user --name kutatas --display-name "Kutatás (Python 3.12)"
```

Ezután a VS Code-ban válaszd ki ezt a kernelt: jobb felső sarok → „Select Kernel" → „Kutatás (Python 3.12)".

### Git push elutasítva

**Tünet:** `error: failed to push some refs to 'origin'`

**Megoldás:**

```bash
# Először húzd le a távoli változásokat
git pull origin main --rebase

# Majd próbáld újra
git push origin main
```

### Docker „permission denied" (Linux)

**Tünet:** `Got permission denied while trying to connect to the Docker daemon socket`

**Megoldás:**

```bash
sudo usermod -aG docker $USER
newgrp docker
```

Ha ez nem segít, jelentkezz ki és vissza.

### „No space left on device"

**Tünet:** Telepítés vagy Docker build közben: `No space left on device`

**Megoldás:**

```bash
# Docker takarítás
docker system prune -a

# pip cache takarítás
pip cache purge

# Conda takarítás
conda clean --all
```

### npm / Node.js verzió probléma (Claude Code-hoz)

**Tünet:** `npm ERR! engine` vagy `Unsupported engine`

**Megoldás:**

```bash
# Ellenőrizd a verziót
node --version

# Ha régi, frissítsd
# Windows: töltsd le az új verziót a nodejs.org-ról
# macOS:
brew upgrade node
# Linux:
sudo apt update && sudo apt upgrade nodejs
```

Ha több Node.js verziót kell kezelned, telepítsd az **nvm**-et (Node Version Manager):

```bash
# Linux/macOS
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
source ~/.bashrc
nvm install 20
nvm use 20

# Windows: használd az nvm-windows-t
# https://github.com/coreybutler/nvm-windows
```

---

![Fejezetek és szükséges eszközök — vizuális áttekintés](images/appendix_a_chapter_tools_map.png)

## Összefoglalás: Mi kell az egyes fejezetekhez?

| Fejezet | Szükséges eszközök |
|---|---|
| **1. AI forradalom** | Csak böngésző |
| **2. Társalgási AI** | Böngésző + API kulcs (A.8) |
| **3. Tudományos írás** | Böngésző + API kulcs |
| **4. Adatelemzés** | Python (A.1) + VS Code (A.2) + venv (A.4) |
| **5. Kódolási asszisztensek** | VS Code + Copilot (A.7) vagy Cursor (A.6) |
| **6. Matematikai modellezés** | Python + tudományos csomagok |
| **7. Adat pipeline** | Python + Git (A.3) |
| **8. Vizuális programozás** | Python + API kulcs |
| **9. RAG rendszerek** | Python + API kulcs |
| **10. Digitális ikrek** | Python + (opcionális: Docker, A.10) |
| **11. AI ágensek** | Python + API kulcs + Claude Code (A.5) |
| **12. Ágensek építése** | Python + Claude Code + Git |
| **13. Eszközök készítése** | Python + pip csomagolás (A.11) + Docker (A.10) |
| **14. AI labor** | Minden fenti eszköz |
| **15. AI az egyetemen** | Böngésző + API kulcs |
| **16. Etika és jövő** | Csak böngésző |

> **Utolsó tipp:** Ne próbálj mindent egyszerre telepíteni és megtanulni. Kezdd az 1. fejezettel, és fokozatosan haladj előre. Minden fejezet elején jelezzük, ha új eszközre van szükség, és visszahivatkozunk erre a függelékre.
