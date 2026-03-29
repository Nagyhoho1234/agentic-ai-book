# Az AI-val felszerelt kutatólabor

> *"A stratégia nélküli AI-adoptáció olyan, mint a GPS nélküli hajózás -- lehet, hogy haladunk, de nem biztos, hogy a jó irányba."*

Képzeld el a következő jelenetet. Hétfő reggel, csoportértekezlet. Te vagy a laborvezető -- egy tízfős kutatócsoport élén állsz, amelyik agrár-távérzékelésben, orvosi képfeldolgozásban, anyagtudományban, vagy bármilyen más szakterületen dolgozik. Az intézetvezető két hete azt mondta: "Készítsetek egy tervet, hogyan integráljátok az AI-t a munkátokba a következő évben. Költségvetés: korlátozott. Határidő: péntek."

Leülsz az asztalhoz, és elkezdesz gondolkodni. A doktoranduszaid már használják a ChatGPT-t irodalomkutatásra -- ki többet, ki kevesebbet, ki tudja, mennyire megbízhatóan. Az egyik posztdokod a múlt héten megkérdezte, használhatna-e Claude Code-ot az adatfeldolgozó szkriptek írásához. A szenior kutatód szkeptikus: "Az AI nem érti a fizikát." A technikusod lelkes: "Automatizáljunk mindent!" Te pedig ott ülsz a kettő között, és pontosan érzed, hogy a válasz valahol középen van -- de hol pontosan?

Ez a fejezet neked szól. Nem az egyéni kutatónak, aki egy chatbotot használ (az a Ch 2 volt), nem az ágensépítőnek (Ch 12), és nem az egyetemi vezetőnek, aki intézményi stratégiát tervez (Ch 15). Ez a fejezet a **kutatólabor szintjén** mutatja meg, hogyan építs fel egy működő, biztonságos, költséghatékony és fenntartható AI-infrastruktúrát a csoportod számára.

---

## A 2026-os tudományos AI stack: mi hova való

Az előző fejezetekben egyenként ismerted meg az eszközöket. Most lássuk, hogyan illeszkednek egymáshoz -- hogyan alkot egy működő egészet az, ami eddig különálló daraboknak tűnt.

### Az AI labor architektúrája

```
┌─────────────────────────────────────────────────────────────┐
│                    KUTATÓI MUNKAFOLYAMAT                     │
│                                                             │
│  ┌───────────────┐  ┌───────────────┐  ┌────────────────┐  │
│  │ Irodalom-      │  │ Adatelemzés   │  │ Publikáció     │  │
│  │ kutatás        │  │ & modellezés  │  │ & prezentáció  │  │
│  └──────┬────────┘  └──────┬────────┘  └──────┬─────────┘  │
│         │                  │                   │            │
│  ═══════╪══════════════════╪═══════════════════╪════════    │
│         │        INTERAKTÍV RÉTEG              │            │
│  ┌──────┴────────────────────────────────────────────────┐  │
│  │  Claude / ChatGPT / Gemini  (társalgás, ötletelés)    │  │
│  │  Claude Code / Cursor       (kódolás, szkriptelés)    │  │
│  │  PySR                       (egyenletfelfedezés)      │  │
│  └──────┬────────────────────────────────────────────────┘  │
│         │                                                   │
│  ═══════╪═══════════════════════════════════════════════     │
│         │        AUTOMATIZÁLÁSI RÉTEG                       │
│  ┌──────┴────────────────────────────────────────────────┐  │
│  │  CrewAI / LangGraph        (AI ágensek, többlépéses)  │  │
│  │  n8n / LangFlow            (vizuális workflow-k)      │  │
│  │  Dagster / Nextflow         (adat-pipeline-ok)        │  │
│  └──────┬────────────────────────────────────────────────┘  │
│         │                                                   │
│  ═══════╪═══════════════════════════════════════════════     │
│         │        KAPCSOLATI RÉTEG                           │
│  ┌──────┴────────────────────────────────────────────────┐  │
│  │  MCP (Model Context Protocol)                         │  │
│  │  → adatbázisok, műszerek, fájlrendszer, API-k        │  │
│  └──────┬────────────────────────────────────────────────┘  │
│         │                                                   │
│  ═══════╪═══════════════════════════════════════════════     │
│         │        SZÁMÍTÁSI RÉTEG                            │
│  ┌──────┴────────────────────────────────────────────────┐  │
│  │  Laptop → Felhő (AWS/Azure/GCP) → Komondor (HPC)     │  │
│  └───────────────────────────────────────────────────────┘  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Mi mire való -- rövid útmutató

**Interaktív réteg: az ember és az AI találkozása**

Ez az a réteg, ahol te, a kutató közvetlenül dolgozol az AI-val. Két alapvető használati mód létezik:

- **Társalgási AI** (Claude, ChatGPT, Gemini): irodalomkutatás, szövegírás, ötletelés, fordítás, összefoglalás. Erről szólt a Ch 2.
- **Kódolási asszisztensek** (Claude Code, Cursor): Python/R szkriptek írása, debugolás, adatfeldolgozás, vizualizáció. Erről szólt a Ch 5.
- **Egyenletfelfedezés** (PySR): szimbolikus regresszió -- az AI nem csak illeszti az adataidat, hanem értelmezhető matematikai egyenletet talál. Erről szólt a Ch 6.

**Automatizálási réteg: ami nélkül nem működik**

Amikor egy feladat nem egy kérdés-válasz, hanem többlépéses, összetett munkafolyamat, átlépsz az automatizálási rétegbe:

- **AI ágensek** (CrewAI, LangGraph): önálló "gondolkodó" programok, amelyek terveznek, döntéseket hoznak, eszközöket használnak. Többlépéses tudományos feladatokhoz ideálisak -- pl. "keress releváns cikkeket, szűrd le az elmúlt 3 évre, készíts összefoglalót, azonosítsd a kutatási réseket." Erről szólt a Ch 12.
- **Vizuális automatizálás** (n8n, LangFlow): drag-and-drop workflow-k, amelyekkel kód nélkül építhetsz automatizálásokat. Ha minden héten ugyanazt az adatfeldolgozást végzed, ez a megoldás. Erről szólt a Ch 8.
- **Adat-pipeline-ok** (Dagster, Nextflow): megbízható, ütemezett, reprodukálható adatfeldolgozási láncok. Ha a laborod napi vagy heti rendszerességgel kap műszeres adatokat, ezek biztosítják, hogy minden adat automatikusan feldolgozásra kerüljön. Erről szólt a Ch 7.

**Kapcsolati réteg: az MCP mint univerzális csatlakozó**

Az **MCP** (Model Context Protocol) az a szabvány, amely lehetővé teszi, hogy az AI eszközeid közvetlenül kommunikáljanak az adatforrásaiddal: adatbázisokkal, fájlrendszerekkel, műszerekkel, API-kkal. Gondolj rá úgy, mint az USB-re: egységes csatlakozó, amely bármit összeköt bármivel. Erről szólt a Ch 9.

**Számítási réteg: hol futnak a dolgok**

Ez a réteg határozza meg, mekkora feladatokat tudsz megoldani. A laptoptól a szuperszámítógépig terjed -- erről részletesebben a "Számítási erőforrások" részben.

### Hogyan válaszd ki, melyik réteg kell

Nem kell az egészet bevezetned egyszerre. Gondolkodj úgy, mint egy lépcsőn:

| Ha a feladatod... | Akkor... | Réteg |
|---|---|---|
| Egyedi kérdés, szöveg, ötlet | Használj társalgási AI-t | Interaktív |
| Kódolás, adatfeldolgozás, ábra | Használj kódolási asszisztenst | Interaktív |
| Többlépéses, ismétlődő munkafolyamat | Építs ágenst vagy workflow-t | Automatizálási |
| Napi/heti rendszeres adatfeldolgozás | Használj pipeline-t | Automatizálási |
| Az AI-nak hozzá kell férnie az adataidhoz | Konfiguráld az MCP-t | Kapcsolati |
| Nagy számítási igény (GPU, HPC) | Lépj feljebb a számítási szinten | Számítási |

---

## Költségmenedzsment: a nullától a szuperszámítógépig

Az AI-eszközök használata pénzbe kerül -- de nem feltétlenül sokba. A kulcs a **fokozatos skálázás**: kezdj az ingyenes szinten, és csak akkor lépj tovább, ha valóban szükséges.

### Az AI-költségek piramisa

```
          ▲
         / \
        / HPC \         Komondor: ingyenes kutatóknak
       /  pályázat \     (KIFU-n keresztül)
      /─────────────\
     / API-költségek \   Token-alapú: $5-50/hó/fő
    /   (pay-as-you-go) \
   /─────────────────────\
  / Előfizetések           \  Claude Pro, ChatGPT Plus:
 /   (subscriptions)        \  ~$20/hó/fő
/───────────────────────────-\
/  Ingyenes szintek (free tiers) \  Claude.ai, ChatGPT Free,
/                                  \  Gemini Free: $0
```

### 1. szint: Ingyenes szintek ($0)

Szinte minden nagy AI-platform kínál ingyenes hozzáférést:

- **Claude.ai** (Anthropic): napi korlátozott használat, de a legtöbb társalgási feladatra elegendő
- **ChatGPT Free** (OpenAI): GPT-4o korlátozott használata
- **Gemini Free** (Google): Google-integrációval
- **GitHub Copilot Free**: korlátozott kódkiegészítés
- **PySR**: teljesen nyílt forráskódú, ingyenes
- **n8n Community Edition**: self-hosted, ingyenes
- **Dagster Open Source**: ingyenes
- **LangGraph**: nyílt forráskódú keretrendszer

**Mikor elég ez?** Ha a laborod tagjai egyénileg, alkalmanként használják az AI-t -- irodalomkutatásra, szövegszerkesztésre, egyszerű kódolási kérdésekre. Egy 5-10 fős labor első 1-2 hónapjára ez tökéletesen megfelel a "kipróbálás és tanulás" fázisban.

### 2. szint: Előfizetések ($20-30/hó/fő)

Amikor az ingyenes szintek korlátai zavaróvá válnak -- túl kevés üzenet, lassabb modellek, nincs prioritásos hozzáférés:

- **Claude Pro** ($20/hó): korlátlan hozzáférés a legújabb modellekhez, hosszabb kontextusablak
- **ChatGPT Plus** ($20/hó): GPT-4o teljes hozzáférés, DALL-E, Advanced Data Analysis
- **Cursor Pro** ($20/hó): AI-asszisztált kódszerkesztő korlátlan használata
- **Claude Code**: a Claude Pro előfizetés részeként elérhető

**Tipp a laborvezetőnek:** Nem kell mindenkinek ugyanaz az előfizetés. A kódolóknak Cursor Pro, a szövegíró-elemzőknek Claude Pro, a vizualizátoroknak ChatGPT Plus lehet az optimális. Készíts egy táblázatot arról, ki mit használ leggyakrabban, és ennek megfelelően oszd el az előfizetéseket.

**Éves költség egy 10 fős laborra:** 10 × $20 × 12 = **$2,400/év** -- nagyjából egy konferenciarészvétel költsége.

### 3. szint: API-költségek (változó, $5-200/hó/fő)

Amikor automatizálásokat építesz -- ágenseket, pipeline-okat, workflow-kat --, az előfizetések nem elégségesek. Az API (Application Programming Interface) hozzáférés token-alapú árazást használ:

- **Claude API**: ~$3/millió input token, ~$15/millió output token (Sonnet 4 modell, 2026 tavaszi árak)
- **OpenAI API**: hasonló nagyságrend
- **Google Vertex AI**: pay-as-you-go

**Hogyan becsüld meg a költséget?** Egy tipikus ágens-futtatás (pl. irodalomkutatás 20 cikkből) kb. 50,000-100,000 tokent használ, ami ~$0.15-0.50. Ha naponta 10 ilyen futtatást végzel, az ~$3-5/nap, azaz **$60-100/hó**.

**Költségkontroll-stratégiák:**

- **Állíts be havi API-költségkeretet** minden csoporttagnak (a legtöbb platform támogatja)
- **Használd a kisebb modelleket** rutinfeladatokra (Haiku olcsóbb, mint Opus)
- **Cache-eld az eredményeket** -- ne futtasd újra azt, amit már egyszer kiszámoltál
- **Naplózd a használatot** -- havi egy alkalom legyen, amikor átnézed, mi mennyibe került

### 4. szint: HPC és szuperszámítás

A legtöbb kutatólabornak ritkán, de időnként szüksége van nagy számítási kapacitásra: modell-finomhangolás, nagy adathalmazok feldolgozása, szimulációk. Magyarországon erre a **Komondor szuperszámítógép** a megoldás (részletesen lásd a következő szakaszban).

### Költségvetési sablon kutatólaboroknak

| Tétel | Havi költség (10 fős labor) | Éves költség |
|---|---|---|
| Ingyenes eszközök (PySR, n8n, LangGraph) | $0 | $0 |
| Pro előfizetések (5 fő × $20) | $100 | $1,200 |
| API-költségek (automatizálások) | $150-300 | $1,800-3,600 |
| Felhőszámítás (alkalmi GPU) | $50-200 | $600-2,400 |
| Komondor (KIFU-n keresztül) | $0* | $0* |
| **Összesen** | **$300-600** | **$3,600-7,200** |

\* A Komondor hozzáférés a magyar felsőoktatási és kutatóintézetek számára ingyenes a KIFU-n keresztül.

Ez az összeg tipikusan egy pályázat dologi költségkeretéből fedezhető, vagy akár az intézeti működési költségvetésből. Összehasonlításképpen: egyetlen műszeres méréssorozat vagy egy nemzetközi konferenciarészvétel gyakran ennek a többszörösébe kerül.

---

## Számítási erőforrások: a laptoptól a Komondorig

Az AI-feladatok számítási igénye hatalmas szóródást mutat. Egy egyszerű LLM-hívás néhány másodpercet vesz igénybe a laptopodról, míg egy modell-finomhangolás napokig futhat GPU-klaszteren. A jó stratégia: **a legkisebb elegendő erőforráson futtasd a feladatot**.

### A számítási lépcső

**1. lépcső: Laptop / munkaállomás**

| Mire alkalmas | Mire nem alkalmas |
|---|---|
| LLM API-hívások (a modell a felhőben fut) | LLM lokális futtatás (kivéve kis modellek) |
| Python/R szkriptek, adatelemzés | Nagy adathalmazok (>100 GB) |
| Kis modellek betanítása | GPU-igényes deep learning |
| PySR futtatás kis-közepes adaton | Nagy szimulációk |
| n8n/LangFlow workflow-k | Modell-finomhangolás |

A legtöbb AI-munka a kutatólaborban **laptopról történik**, mert az LLM-eket API-n keresztül éred el -- a nehéz számítás a felhőben történik, a te géped csak a kérést küldi és az eredményt fogadja.

**2. lépcső: Felhőszámítás (cloud computing)**

Amikor a laptop nem elég, a felhő a következő lépcső:

- **Google Colab**: ingyenes GPU hozzáférés (korlátozott), Pro verzió ~$10/hó
- **AWS SageMaker**, **Azure ML**, **Google Vertex AI**: pay-as-you-go GPU-bérlés
- **Lambda Cloud**, **Vast.ai**: olcsó GPU-bérlés ML-feladatokra
- **Hugging Face Spaces**: modell-hosting és inference

**Tipikus felhasználás:** Ha egy héten 2-3 alkalommal kell GPU-t használnod 1-2 órára (pl. képfeldolgozási modell finomhangolása), a felhő a legköltséghatékonyabb megoldás. Nem kell GPU-t venned, csak akkor fizetsz, amikor használod.

**3. lépcső: Komondor szuperszámítógép**

A **Komondor** Magyarország legerősebb szuperszámítógépe, a Debreceni Egyetem Kassai úti kampuszán található. HPE Cray EX architektúra, ~5-6 petaflops csúcsteljesítmény, 10 petabyte tárhely, és ami a legfontosabb: **dedikált AI és big data partícióval** rendelkezik speciális GPU egységekkel.

**Hozzáférés:** A KIFU (Kormányzati Informatikai Fejlesztési Ügynökség) üzemelteti, és **ingyenesen elérhető** a magyar felsőoktatási intézmények, kutatóintézetek és partnereik számára. A hozzáféréshez pályázatot kell benyújtani a KIFU-hoz -- a folyamat nem bürokratikus, de előre tervezést igényel.

**Mire alkalmas a Komondor:**
- Nagyméretű deep learning modellek betanítása
- Molekuladinamikai szimulációk
- Klímakutatási modellek futtatása
- Genomikai adatfeldolgozás
- Orvosi képfeldolgozás nagy adathalmazokon
- Anyagtudományi szimulációk

**Gyakorlati tanács:** Ne a Komondorra gondolj először. A legtöbb feladatod megoldható laptopról + API-ból. A Komondor azokra a feladatokra való, amelyek tényleg szuperszámítógépet igényelnek: hatalmas adathalmazok, napokig futó szimulációk, modelltanítás több száz GPU-n. Ha nem vagy biztos benne, hogy szükséged van-e rá, valószínűleg nincs.

### Döntési fa: hol futtassam?

```
A feladatod...
│
├── LLM-hívás (szöveg, kód, elemzés)?
│   └── → Laptop + API (felhőben fut az LLM)
│
├── Kis adathalmaz (<10 GB), egyszerű ML?
│   └── → Laptop
│
├── Közepes adathalmaz, GPU kell 1-2 órára?
│   └── → Google Colab / felhő GPU
│
├── Nagy adathalmaz, többnapos tanítás?
│   └── → Komondor (KIFU-pályázat)
│
└── Többhetes szimuláció, több száz GPU?
    └── → Komondor vagy EuroHPC (pl. LUMI)
```

---

## Adatbiztonság és adatvédelem

Ez a fejezet legkritikusabb szakasza. Az AI használata a kutatásban szükségszerűen azt jelenti, hogy adatokat osztasz meg AI-rendszerekkel -- és ez komoly biztonsági és jogi kérdéseket vet fel.

### Mit szabad felhőbe küldeni, mit nem

Az alapszabály egyszerű: **ha kétség merül fel, ne küldd.**

A gyakorlatban három kategóriába sorold az adataidat:

**🟢 Szabadon küldhető felhő AI-nak:**
- Nyilvánosan elérhető adatok (publikált cikkek, nyilvános adatbázisok)
- Saját kód, amelyet úgyis nyílt forráskódúként publikálsz
- Általános kérdések, amelyek nem tartalmaznak érzékeny információt
- Szintetikus vagy anonimizált adathalmazok
- Általánosan elérhető módszertani kérdések

**🟡 Óvatosan, feltételekkel küldhető:**
- Kutatási adatok, amelyek még nem publikáltak (szellemi tulajdon kockázata)
- Aggregált, de nem egyéni szintű adatok
- Intézményi dokumentumok (ellenőrizd az intézmény AI-irányelveit)
- Pályázati szövegek (bizonyos pályázati kiírók tiltják az AI-használatot)

**🔴 Soha ne küldd felhő AI-nak:**
- Személyes adatok (nevek, TAJ-számok, lakcímek, betegadatok)
- Betegrekordok, klinikai adatok
- GDPR-védett adathalmazok
- Titkosított vagy biztonsági minősítésű kutatási adatok
- Ipari partnerektől kapott bizalmas adatok
- Etikai engedélyhez kötött, még feldolgozás alatt álló humán adatok

### Helyi AI-futtatás mint megoldás

Ha érzékeny adatokkal dolgozol, de AI-t szeretnél használni, van megoldás: **lokális (on-premises) modellek**. Kisebb, de egyre képesebb nyelvi modellek futtathatók a saját gépeden vagy az intézményi szerveren, anélkül, hogy bármilyen adat elhagyná a belső hálózatot:

- **Ollama + Llama 3** (Meta): nyílt forráskódú, lokálisan futtatható LLM
- **Mistral modellek**: hatékony, kisméretű modellek lokális futtatásra
- **Intézményi LLM-szerver**: a Komondor vagy más intézményi szerver felhasználható privát AI-szolgáltatás üzemeltetésére

A lokális modellek kisebb kapacitásúak, mint a felhőben futó nagy modellek, de az érzékeny kutatási területeken (orvostudomány, genetika, klinikai vizsgálatok) ez az egyetlen elfogadható megoldás.

### GDPR és kutatási adatok

> **GDPR (General Data Protection Regulation -- Általános Adatvédelmi Rendelet):** Az Európai Unió 2018 májusában hatályba lépett adatvédelmi rendelete (EU 2016/679), amely szabályozza a személyes adatok kezelését az EU-n belül és az EU-ból harmadik országokba történő adattovábbítást. A GDPR alapelvei: célhoz kötöttség, adattakarékosság, pontosság, korlátozott tárolás, integritás és bizalmasság, elszámoltathatóság. Megsértése akár 20 millió euró vagy az éves globális árbevétel 4%-ának megfelelő bírsággal is járhat.

A kutatási kontextusban a GDPR különösen fontos, mert a legtöbb tudományos kutatás -- a társadalomtudományoktól az orvostudományig -- személyes adatokkal dolgozik. A GDPR kutatási vonatkozásai:

**Mikor vonatkozik rád a GDPR?**

Ha a kutatásod bármilyen **személyes adatot** kezel -- beleértve a neveket, e-mail-címeket, helyadatokat, egészségügyi adatokat, genetikai adatokat, biometrikus adatokat, vagy bármilyen más információt, amelyből egy természetes személy azonosítható --, a GDPR szabályai alkalmazandók.

**A GDPR és az AI-eszközök metszéspontja:**

1. **Adattovábbítás harmadik országba:** Amikor kutatási adataidat egy felhőalapú AI-szolgáltatásnak küldöd (pl. Claude API, OpenAI API), az adataid jellemzően az USA-ban lévő szerverekre kerülnek. Ez a GDPR szempontjából **harmadik országba történő adattovábbítás**, amelyhez megfelelő garanciák szükségesek (pl. Standard Contractual Clauses -- SCC).

2. **Célhoz kötöttség:** A GDPR megköveteli, hogy az adatkezelés célja világos és meghatározott legyen. Ha a kutatási alanyaid az adatszolgáltatáshoz hozzájárultak, de az AI-feldolgozás nem volt az eredeti cél része, új hozzájárulást vagy jogalapot kell biztosítanod.

3. **Adattakarékosság:** Ne küldj több adatot az AI-rendszernek, mint ami feltétlenül szükséges. Ha a kérdésed megválaszolásához nem kell a teljes adathalmaz, anonimizálj vagy aggregálj először.

4. **Az érintett jogai:** A kutatási alanyaidnak joguk van tudni, hogy az adataikat AI-rendszer dolgozza fel, és bizonyos esetekben tiltakozhatnak ellene.

**Gyakorlati lépések a GDPR-megfelelőséghez AI-használat esetén:**

- **Anonimizálj, mielőtt AI-hoz nyúlsz.** Ha a kutatásod nem igényli az egyéni azonosítást, távolítsd el a személyes adatokat az AI-nak küldött adatokból.
- **Dokumentáld az AI-használatot** az adatkezelési tervben (Data Management Plan -- DMP). Tüntesd fel, melyik AI-szolgáltatást használod, milyen adatokat küldtél, és milyen garanciákat biztosítottál.
- **Ellenőrizd az AI-szolgáltató adatkezelési feltételeit.** A legtöbb nagy AI-szolgáltató (Anthropic, OpenAI, Google) külön kutatási/vállalati feltételeket kínál, amelyek garanciákat nyújtanak az adatok nem-betanítási célú felhasználására.
- **Kérj segítséget az intézményi adatvédelmi tisztviselőtől (DPO).** Ő segít felmérni, hogy a tervezett AI-használat GDPR-konform-e.
- **Használj lokális AI-t érzékeny adatokhoz.** Ha a GDPR-megfelelőség biztosítása túl bonyolult, futtasd a modellt helyben.

### EU AI Act: amit a kutatónak tudnia kell

> **EU AI Act (Az Európai Unió Mesterséges Intelligenciáról szóló Rendelete, EU 2024/1689):** A világ első átfogó AI-szabályozása, amelyet az Európai Parlament 2024 márciusában fogadott el. A rendelet kockázatalapú megközelítést alkalmaz: az AI-rendszereket az általuk hordozott kockázat szintje szerint kategorizálja, és ennek megfelelően különböző szintű kötelezettségeket ír elő a fejlesztőknek és a felhasználóknak (deployer-eknek). A szigorúbb szabályok 2026-ban lépnek hatályba.

**A kockázati szintek:**

| Kockázati szint | Leírás | Példa a kutatásban | Kötelezettség |
|---|---|---|---|
| **Elfogadhatatlan** | Tiltott felhasználás | Hallgatók érzelem-nyomon követése, szociális pontozás | **Tiltott** |
| **Magas kockázat** | Jelentős hatás személyekre | AI-alapú vizsgaértékelés, hallgatói hozzáférési döntések, adaptív tanulás | Szigorú követelmények: adatminőség, emberi felügyelet, naplózás, technikai dokumentáció |
| **Korlátozott kockázat** | Átláthatósági kötelezettség | Chatbotok (jelölni kell, hogy AI) | Tájékoztatási kötelezettség |
| **Minimális kockázat** | Nincs külön kötelezettség | Spamszűrő, keresőmotor-optimalizáció | Nincs külön szabály |

**Mi vonatkozik a kutatókra?**

A legtöbb kutatási célú AI-használat -- irodalomkutatás, adatelemzés, kódolási asszisztencia, egyenletfelfedezés -- a **minimális** vagy **korlátozott kockázat** kategóriába esik. Ezek esetén minimális vagy semmilyen jogi kötelezettséged nincs az AI Act alapján.

**De figyelem:** Ha az AI-t **oktatási kontextusban** használod (pl. hallgatók értékelésére, vizsgáztatásra, hozzáférési döntésekre), az **magas kockázatú** felhasználásnak minősülhet. Ez azt jelenti:

- A betanítási adatoknak magas minőségűeknek kell lenniük
- Emberi felügyeletet kell biztosítanod
- Naplózási kötelezettséged van
- Technikai dokumentációt kell készítened
- Az érintetteket tájékoztatnod kell

**Az AI Act és a kutatási kivétel:**

Az AI Act tartalmaz kutatási mentességeket: a kizárólag tudományos kutatási és fejlesztési célra használt AI-rendszerekre bizonyos kötelezettségek nem vonatkoznak. Azonban ez a mentesség **nem abszolút** -- ha a kutatási eredményt később gyakorlatba ülteted, a teljes szabályozás alkalmazandóvá válik.

**Szürke zónák:**

Ahogy az EUA (European University Association) jelentése rámutat: "Még mindig vannak szürke zónák az egyetemek számára azon a téren, hogy mely gyakorlatok AI Act-konformak és melyek nem." Az árnyékos IT (shadow IT) problémája -- amikor az oktatók személyesen, intézményi kontroll nélkül használnak AI-eszközöket vizsgákhoz, értékeléshez -- különösen kockázatos, mert ezek a könnyen elérhető modellek (ChatGPT, Copilot) nem feltétlenül felelnek meg a magas kockázatú felhasználás európai normáinak.

**Gyakorlati lépések kutatócsoportoknak:**

1. **Térképezd fel az AI-használatodat:** Készíts leltárt arról, milyen AI-rendszereket használsz, milyen célra, és milyen adatokkal.
2. **Azonosítsd a magas kockázatú használatokat:** Ha bármilyen oktatási értékelésben, hozzáférési döntésben vagy hallgatói monitoringban használsz AI-t, az valószínűleg magas kockázatú.
3. **Dokumentálj:** Még ha a jelenlegi használatod alacsony kockázatú is, a dokumentálás segít a későbbi megfelelőségben.
4. **Kövesd figyelemmel a 2026-os határidőket:** A szigorúbb szabályok 2026-ban lépnek hatályba.
5. **Vond be az intézményi jogászt:** Ha nem vagy biztos a kockázati besorolásban, kérj szakértői véleményt.

---

## AI-beszerzési útmutató kutatócsoportoknak

Amikor a laborodba új AI-eszközt vezetsz be, az nem egyszerűen egy szoftver letöltése. Különösen intézményi környezetben -- egyetemen, kutatóintézetben -- a beszerzésnek átgondoltnak és strukturáltnak kell lennie. Ebben a szakaszban négy keretrendszert mutatok be, amelyek segítenek.

### Platformválasztási szempontok

Mielőtt bármit vásárolnál, válaszold meg ezeket a kérdéseket:

**1. A probléma határozza meg az eszközt, nem fordítva**

A WEF (World Economic Forum) AI-beszerzési keretrendszere hangsúlyozza: "A szervezeteknek először meg kell határozniuk az üzleti céljaikat, majd ezekhez kell kötniük az AI-képességeket -- nem fordítva." Kutatási kontextusban: először fogalmazd meg, milyen kutatási kérdést akarsz megválaszolni, és csak utána keresd az AI-eszközt.

Kérdezd meg: **Megoldható-e ez AI nélkül is?** Sok egyetemi folyamat egyszerűbb automatizálással vagy javított munkafolyamatokkal is megoldható.

**2. Átláthatóság és magyarázhatóság**

A kutatásban a reprodukálhatóság alapkövetelmény. Követeld meg az AI-szállítótól:
- Milyen algoritmust és szoftverkönyvtárat használ?
- Képes-e érthetően elmagyarázni, hogyan működik a rendszer?
- Biztosít-e képzési anyagokat a csoportodnak?
- Ismeri és dokumentálja-e a korlátait?

**3. Visszacsatolás és adaptáció**

A kutatási adatminták változnak (új mérési módszerek, szezonális változások, módszertani frissítések). Az AI-eszköznek alkalmazkodnia kell:
- Van-e automatikus visszacsatolási/újratanítási mechanizmus?
- Hogyan méri a rendszer a teljesítményét?
- Hogyan segít a szállító, ha a modell váratlan eredményeket ad?

### Az EU MCC-AI (Model Contractual Clauses for AI)

Az Európai Bizottság modell-szerződésmintákat dolgozott ki az AI-beszerzéshez (**MCC-AI**), amelyek egységes jogi keretet biztosítanak az AI-rendszerek vásárlásakor. Ezek a minták különösen hasznosak egyetemi beszerzéseknél, mert:

- Szabályozzák az **adattulajdonlást** (ki tulajdonolja a betanított modellt, a derivált eredményeket?)
- Előírják az **átláthatósági kötelezettségeket** (a szállítónak dokumentálnia kell a rendszer működését)
- Meghatározzák a **felelősségi viszonyokat** adatszivárgás esetén
- Biztosítják az **AI Act-megfelelőséget** a szerződéses feltételekben

**Gyakorlati tipp:** Kérd az intézményi beszerzési osztálytól, hogy az AI-szoftverek vásárlásakor használják az MCC-AI sablonokat kiindulópontként.

### A WEF beszerzési keretrendszer öt pillére

A World Economic Forum 2024-ben publikálta "Empowering AI Leadership: AI C-Suite Toolkit" című dokumentumát, amely egy ötpilléres AI-beszerzési keretrendszert mutat be. A modell középpontjában az **etika** áll, amelyet öt egymással összefüggő pillér vesz körül:

**1. Üzleti stratégia (Business strategy)**
- Hogyan szolgálja az AI-megoldás a kutatási célokat?
- A szállító érti-e a kutatási kontextust?
- Mennyi egyedi fejlesztés szükséges?
- Skálázható-e a megoldás?

**2. Kereskedelmi stratégia (Commercial strategy)**
- Milyen licencmodellt kínál a szállító?
- Mi a teljes tulajdonlási költség (TCO)?
- Milyen garanciákat biztosít?
- Van-e vendor lock-in kockázat?

**3. Adatstratégia (Data strategy)**
- Milyen adatokra van szükség, és rendelkezésre állnak-e?
- Ki a tulajdonosa az adatoknak és a derivált modelleknek?
- Milyen adatvédelmi keretrendszert követ a szállító?
- Hol tárolja az adatokat, és milyen biztonsági intézkedéseket alkalmaz?

**4. Etika és fenntarthatóság (Ethics and sustainability)**
- Milyen etikai elveket követ a szállító?
- Hogyan kezeli a torzítást (bias)?
- Milyen a rendszer energiafogyasztása és szénlábnyoma?

**5. Irányítás, kockázat és megfelelőség (Governance, risk and compliance)**
- Megfelel-e a rendszer az AI Act követelményeinek?
- Van-e beépített kockázatkezelési mechanizmus?
- Hogyan kezeli a szállító az incidenseket?

### Az EDUCAUSE ellenőrzőlista európai adaptációja

Az EDUCAUSE (az amerikai felsőoktatási IT-szervezet) kidolgozott egy AI-beszerzési ellenőrzőlistát egyetemek számára. Ezt európai kontextusra adaptálva a következő pontokat érdemes ellenőrizned:

**Adatvédelem és jogi megfelelőség:**
- [ ] A szállító GDPR-konform adatkezelést biztosít?
- [ ] Az adatok EU-n belül maradnak, vagy van megfelelő adattovábbítási garancia (SCC)?
- [ ] Az AI Act szerinti kockázati besorolás megtörtént?
- [ ] Van Data Processing Agreement (DPA) a szállítóval?

**Biztonság:**
- [ ] Milyen titkosítást alkalmaz az adatátvitelhez és a tároláshoz?
- [ ] Van-e SOC 2 vagy ISO 27001 tanúsítványa?
- [ ] Hogyan kezeli az adatszivárgási incidenseket?
- [ ] A felhasználói adatokat felhasználja-e a modellek betanítására?

**Integráció és interoperabilitás:**
- [ ] Támogatja-e az MCP-t vagy más nyílt protokollt?
- [ ] Illeszkedik-e a meglévő intézményi rendszerekhez (NEPTUN, Moodle, intézményi adattárak)?
- [ ] Van-e API a testreszabáshoz?
- [ ] Milyen formátumokban exportálhatók az adatok és az eredmények?

**Oktatás és támogatás:**
- [ ] Biztosít-e képzést a csapat számára?
- [ ] Milyen szintű ügyfélszolgálatot kínál?
- [ ] Van-e dokumentáció és közösségi fórum?

**Fenntarthatóság:**
- [ ] Mi történik, ha a szállító megszűnik vagy megváltoztatja a feltételeket?
- [ ] Exportálhatók-e az adatok és a workflow-k más rendszerbe?
- [ ] Van-e hosszú távú árgarancia?

### A teljes tulajdonlási költség (TCO) elemzése

Az AI-eszközök ára nem csak a licencdíj. A **Total Cost of Ownership** tartalmazza:

| Költségelem | Tipikus arány | Példa |
|---|---|---|
| Licenc/előfizetés | 30-40% | Claude Pro: $240/év/fő |
| API-használat | 20-30% | Token-költségek, felhő-GPU |
| Bevezetés, testreszabás | 10-15% | MCP konfiguráció, workflow-építés |
| Képzés | 5-10% | Csapattagok betanítása |
| Karbantartás, frissítés | 5-10% | Prompt-ek finomhangolása, új verziók tesztelése |
| Elveszett produktivitás | 5-10% | Tanulási görbe, hibakeresés |

**Gyakorlati tipp:** Ha egy AI-eszköz $20/hó/fő, az éves TCO inkább $35-50/fő, ha beleszámítod a képzést, a testreszabást és a karbantartást. Tervezd be ezt a pályázati költségvetésbe.

---

## Csoportos együttműködés: workflow-k megosztása, kollégák képzése

Az AI bevezetése a laborban nem egyéni feladat. Ha mindenki más eszközt használ, más prompt-okat, más workflow-kat, az káosz. A cél: **közös tudásbázis és megosztott munkafolyamatok**.

### Az AI-tudás csoporton belüli szintjei

A tapasztalat azt mutatja, hogy egy tipikus kutatócsoport tagjai nagyon eltérő szinteken állnak:

| Szint | Jellemző | Ki? | Mit kell? |
|---|---|---|---|
| **Érdeklődő** | Hallott az AI-ról, de nem használja | Szenior kutatók, technikusok | Bemutatók, motiváció |
| **Kezdő** | Néha kérdez a ChatGPT-től | A legtöbb doktorandusz | Strukturált prompt-ek, best practice-ek |
| **Felhasználó** | Rendszeresen használ AI-t | Aktív kutatók | Automatizálás, workflow-k |
| **Építő** | Sajáto ágenseket, pipeline-okat épít | Kódolni tudó kutatók | API-hozzáférés, MCP, keretrendszerek |

### A "belső AI-bajnok" modell

Az EUA (European University Association) ajánlása szerint az AI-adoptáció sikerének kulcsa az, hogy **az intézményi közösség támogatottnak érezze magát, ne nyomás alattnak**. A laborod kontextusában ez azt jelenti:

1. **Nevezz ki egy AI-bajnokot:** Az a személy, aki a leglelkesebb és legtudásosabb az AI terén. Nem kell, hogy formális pozíció legyen -- egyszerűen az, akihez a többiek fordulnak kérdéseikkel.

2. **Heti 15 perces "AI-villám" bemutató:** Minden héten valaki bemutatja, hogyan használta az AI-t azon a héten. Nem kell, hogy nagy felfedezés legyen -- lehet egy hasznos prompt, egy automatizálás, egy megoldott probléma. A lényeg a rendszeresség és a megosztás.

3. **Közös prompt-könyvtár:** Készíts egy megosztott dokumentumot (Google Docs, Notion, Git repo), ahová mindenki beírja a bevált prompt-jait. Strukturáld feladattípus szerint: irodalomkutatás, statisztikai elemzés, ábrafelirat, recenzió-válasz stb.

4. **Közös workflow-tár:** Ha valaki épít egy n8n workflow-t vagy egy CrewAI ágenst, ossza meg a csoporttal. Használjatok közös Git repót az AI-workflow-k verziókezelésére.

### Amit meg kell beszélnetek csoportszinten

Mielőtt fejest ugranátok az AI-ba, tartsatok egy csoportértekezletet ezekről a témákról:

**1. Mire használjuk, mire nem?**
- Milyen feladatokhoz használunk AI-t?
- Van-e olyan feladat, ahol tudatosan nem akarunk AI-t használni?
- Hogyan kezeljük az AI-generált szöveg/kód jelölését a publikációkban?

**2. Milyen eszközöket használunk?**
- Egységesítsük-e az eszközöket, vagy mindenki használhatja, amit akar?
- Ki fizeti az előfizetéseket?
- Hogyan osztjuk el az API-költségvetést?

**3. Adatbiztonság**
- Milyen adatokat szabad felhő AI-nak küldeni?
- Hogyan biztosítjuk a GDPR-megfelelőséget?
- Hogyan kezeljük az érzékeny kutatási adatokat?

**4. Reprodukálhatóság**
- Hogyan dokumentáljuk az AI-használatot a kutatási folyamatban?
- Hogyan biztosítjuk, hogy az AI-val generált eredmények reprodukálhatók legyenek?
- Milyen verziószámot és prompt-ot rögzítsünk?

### A fokozatos bevezetés terve

Az EUA "mikro-ambiciózus" megközelítését a laborodra alkalmazva:

**1. hónap: Felfedezés**
- Mindenki regisztrál ingyenes AI-fiókokat (Claude, ChatGPT)
- Heti AI-villám bemutatók indulnak
- A laborvezető elkészíti az "Amit szabad / amit nem" irányelveket

**2. hónap: Strukturálás**
- A legaktívabb felhasználók Pro előfizetést kapnak
- Közös prompt-könyvtár létrehozása
- Első közös workflow építése (pl. heti irodalomfigyelés)

**3. hónap: Automatizálás**
- API-hozzáférés beállítása
- Első ágensek vagy n8n workflow-k élesben
- MCP konfiguráció a labor adatforrásaihoz

**4-6. hónap: Optimalizálás**
- Költségek elemzése, optimalizálás
- Workflow-k finomhangolása a visszajelzések alapján
- Új csapattagok betanítása a kialakult rendszerbe
- Az AI-hatás első mérése (lásd a következő szakaszt)

---

## Az AI hatásának mérése

Hogyan tudod megmutatni az intézetvezetőnek (vagy a pályázati bírálónak), hogy az AI-befektetés megtérül? Három dimenzióban mérd:

### 1. Idő-megtakarítás

Ez a legkönnyebben mérhető. Készíts egy egyszerű táblázatot:

| Feladat | Idő AI nélkül | Idő AI-val | Megtakarítás |
|---|---|---|---|
| Irodalomkutatás (20 cikk áttekintése) | 8 óra | 2 óra | 75% |
| Python szkript írása (adattisztítás) | 4 óra | 45 perc | 81% |
| Ábrák készítése publikációhoz | 3 óra | 1 óra | 67% |
| Recenzió-válasz első vázlat | 6 óra | 1.5 óra | 75% |
| Statisztikai elemzés kiválasztása és futtatása | 2 óra | 30 perc | 75% |

**Hogyan mérd:** Kérd a csapattagjaidat, hogy egy hónapig vezessenek naplót arról, milyen feladatokat oldottak meg AI-val, és mennyi időt takarítottak meg. Ez anekdotikus, de meggyőző.

**Fontos:** Ne a teljes munkaidő-megtakarítást kommunikáld, hanem azt, hogy **a felszabaduló időt milyen értékesebb feladatokra fordítottátok** -- ez az, ami a döntéshozókat meggyőzi.

### 2. Minőségjavulás

Nehezebben mérhető, de legalább ilyen fontos:

- **Kevesebb hiba a kódban:** Mérd a debugolásra fordított időt AI-asszisztált kódolás előtt és után.
- **Jobb statisztikai elemzés:** Az AI segít a megfelelő statisztikai teszt kiválasztásában -- kevesebb a visszautasított cikk a reviewerek statisztikai kifogásai miatt.
- **Átfogóbb irodalomáttekintés:** Az AI több cikket képes feldolgozni, mint amit emberileg lehetséges lenne -- csökken az esélye, hogy egy fontos referenciát kihagysz.
- **Jobb ábrák és vizualizációk:** Az AI-asszisztált kódolás lehetővé teszi, hogy bonyolultabb, informatívabb ábrákat készíts.

### 3. Új képességek

A legizgalmasabb dimenzió: mit tudsz most, amit korábban nem tudtál?

- **Szimbolikus regresszió (PySR):** Értelmezhető egyenleteket találsz az adataidban -- nem csupán black-box modelleket.
- **Többnyelvű irodalomkutatás:** Az AI segítségével olyan nyelvű cikkeket is feldolgozhatsz, amelyeket korábban nem tudtál olvasni.
- **Automatizált adatfeldolgozás:** Napi/heti rendszerességgel futó pipeline-ok, amelyek emberi beavatkozás nélkül dolgozzák fel az új adatokat.
- **Ágens-alapú kutatási asszisztens:** Egy CrewAI ágens, amelyik minden héten átnézi a legújabb preprint-eket a szakterületeden és összefoglalót készít.
- **Interdiszciplináris együttműködés:** Az AI segít áthidalni a szakterületi nyelvi akadályokat -- egy biológus és egy informatikus könnyebben kommunikál, ha az AI "fordít" a szakterületi zsargonok között.

### Egyszerű mérési keretrendszer

Negyedévente töltsd ki a következő értékelőlapot a csoportod számára:

```
AI HATÁS NEGYEDÉVES ÉRTÉKELÉS
═══════════════════════════════

Időszak: ________

1. HASZNÁLAT
   Aktív AI-felhasználók a csoportban: ___/___
   Leggyakrabban használt eszközök: ________________
   Havi AI-költség: ___________

2. IDŐ-MEGTAKARÍTÁS
   Becsült heti megtakarítás összesen: ___ óra
   Legtöbb időt megtakarító feladat: ________________

3. MINŐSÉG
   AI-asszisztált publikációk száma: ___
   Új módszertanok AI-nak köszönhetően: ___

4. ÚJ KÉPESSÉGEK
   Korábban lehetetlen feladatok, amelyeket most megoldunk:
   ________________________________________________

5. PROBLÉMÁK
   AI-hibák, amelyekből tanultunk: ________________
   Biztonsági vagy adatvédelmi incidensek: ___

6. KÖVETKEZŐ NEGYEDÉV TERVEI
   ________________________________________________
```

### A mérés korlátai

Az EUA jelentése óva int: "Előrehozott lenne olyan stratégiákat fejleszteni, amelyek az AI-alapú produktivitásnövekedésre építenek." Ne ígérj olyat, amit nem tudsz bizonyítani. Az AI nem csodaszer, és a hatása függ a szakterülettől, a feladat típusától és az egyéni kompetenciáktól. Légy őszinte a méréseiddel -- a hitelesség fontosabb, mint a szép számok.

---

## Összefoglalás: tíz lépés az AI-képes laborhoz

1. **Mérd fel a kiindulópontot.** Hol áll a csapatod az AI-használatban? Ki használ mit, milyen szinten?

2. **Határozd meg a célokat.** Milyen kutatási problémákat akarsz AI-val megoldani? Kezdj a legfájdalmasabb időnyelőkkel.

3. **Kezdj az ingyenes szinttel.** Az első hónapban senkinek nem kell fizetős eszköz. Fedezzétek fel, mit tudnak az ingyenes AI-platformok.

4. **Építsd fel a stack-et fokozatosan.** Interaktív réteg → automatizálási réteg → kapcsolati réteg. Ne akarj mindent egyszerre.

5. **Állítsd be a költségkeretet.** Tervezd meg a havi AI-költségvetést, és tartsd be. Az API-költségek meglepetéseket okozhatnak, ha nem figyelsz.

6. **Oldd meg az adatbiztonságot.** Készíts egyértelmű "zöld/sárga/piros" listát arról, milyen adatokat szabad és milyeneket tilos felhő AI-nak küldeni.

7. **Ismerd meg a jogi kereteket.** GDPR és AI Act: tudd, mi vonatkozik rád, és dokumentáld a megfelelőséget.

8. **Oszd meg a tudást.** Heti AI-villám bemutatók, közös prompt-könyvtár, közös workflow-tár.

9. **Mérd az eredményeket.** Negyedéves értékelés: idő-megtakarítás, minőségjavulás, új képességek.

10. **Iterálj.** Az AI-eszközök és a legjobb gyakorlatok gyorsan változnak. Amit ma csinálsz, fél év múlva lehet, hogy másképp csinálnád. Legyél nyitott a változásra.

---

## Etikai szempontok

Az AI-val felszerelt kutatólabor működtetése számos etikai kérdést vet fel: az AI-generált szöveg jelölésétől a szerzőségi kérdéseken át a torzítás kezeléséig. Ezeket a kérdéseket részletesen a **Ch 16** tárgyalja -- itt csak annyit jegyzünk meg, hogy az etikai keretrendszer nem utólagos kiegészítés, hanem az AI-stratégia szerves része kell legyen. Ahogy a WEF keretrendszere fogalmaz: az etika nem a beszerzési folyamat végén lévő jelölőnégyzet, hanem az alap, amelyre minden más pillér épül.

> **Lásd Ch 16** -- Az AI-etika a tudományos kutatásban: szerzőség, torzítás, felelősség és az AI-használat átlátható dokumentálása.

---

## Hivatkozások és további olvasmányok

- **EUA (2026).** *Adopting Artificial Intelligence in Universities.* European University Association Task-and-Finish Group on AI. -- Intézményi stratégiák, szabályozási kérdések, érettségi modellek.
- **World Economic Forum (2024).** *Empowering AI Leadership: AI C-Suite Toolkit -- Procurement.* -- Az ötpilléres beszerzési keretrendszer.
- **EU AI Act (2024).** Regulation (EU) 2024/1689 of the European Parliament. -- A teljes rendelet szövege az EUR-Lex-en elérhető.
- **GDPR (2016).** Regulation (EU) 2016/679 -- General Data Protection Regulation. -- Az Európai Unió adatvédelmi rendelete.
- **EU MCC-AI.** Model Contractual Clauses for AI. European Commission. -- Modell-szerződésminták AI-beszerzéshez.
- **EDUCAUSE.** AI Procurement Checklist for Higher Education. -- Eredetileg amerikai kontextusra, de adaptálható európai egyetemekre.
- **Jisc AI Maturity Model for Education.** -- Ötfokozatú érettségi modell az AI intézményi bevezetésének mérésére.
- **KIFU -- Komondor szuperszámítógép.** https://docs.hpc.dkf.hu/ -- Hozzáférési információk és dokumentáció.
- **Debreceni Egyetem AI-irányelvek.** *Irányelvek a mesterséges intelligencia alapú rendszerek használatához a Debreceni Egyetemen.* -- Az intézményi AI-használati szabályzat.
