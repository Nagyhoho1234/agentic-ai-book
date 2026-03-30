# 9. fejezet: RAG --- Tanítsuk meg az AI-t a saját adatainkra

> **Fejezet-információ**
> - **Kinek szól:** Kutatóknak, akik a saját dokumentumaikra, cikkeikre és adataikra építenének AI chatbotot
> - **Előismeretek:** 2. fejezet (promptolás), 5. fejezet (ajánlott a kódolási részekhez)
> - **Amit megtanulsz:**
>   - Mi a RAG (Retrieval-Augmented Generation) és miben különbözik a fine-tuningtól
>   - A RAG pipeline lépésről lépésre: dokumentumbetöltés, chunking, embedding, visszakeresés
>   - Saját tudásbázis építése és kiértékelése
> - **Szükséges eszközök:** Böngésző + terminál + Python
> - **Kapcsolódó fejezetek:** 2. fejezet (LLM működése), 7. fejezet (pipeline-ok), 13. fejezet (eszközök készítése)

---

## 9.1 Amikor a ChatGPT nem ismeri a kutatásodat

> **🖼️ Ábra: A RAG-pipeline lépései**
> *Vízszintes folyamatábra: Dokumentumok → Chunking (darabolás) → Embedding (vektorizálás) → Vektor-adatbázis → Keresés (retrieval) → LLM válaszgenerálás. Minden lépésnél rövid magyarázat.*


Képzeld el a következő jelenetet. Kati, harmadéves PhD-hallgató a Debreceni Egyetem Kémiai Intézetében, éjjel kettőkor ül a laptopja előtt. A disszertációja a Tisza vízgyűjtő területéről származó üledékminták nehézfém-speciációjáról szól --- egy rendkívül specifikus téma, amelyhez öt éve gyűjt adatokat. Beírja a ChatGPT-be:

> *„Mi a jelenlegi konszenzus a kadmium speciáció és a szerves anyag tartalom kapcsolatáról folyami üledékekben, különös tekintettel a Közép-Európai folyókra?"*

A válasz, amit kap, nem rossz. De nem is jó. Az LLM általános geokémiai ismereteket ad vissza, hivatkozik néhány 2019-es tanulmányra (amelyek közül kettő nem is létezik), és egyetlen szót sem ejt arról a hat saját publikációjáról, amelyet Kati és a csoportja az elmúlt három évben közölt. A válasz nem tud a laborjegyzeteiről, a kalibrációs protokolljaikról, a Tisza-specifikus háttérkoncentráció-adatbázisukról, és arról a kritikus módszertani vitáról sem, ami a legutóbbi csoportértekezleten zajlott.

Ez nem a ChatGPT hibája. Ez egy strukturális korlát.

**A nagy nyelvi modellek (LLM-ek) három alapvető korláttal rendelkeznek, amelyek a kutatói munkában különösen fájdalmasak:**

1. **Tudáshatár (knowledge cutoff).** Minden LLM-nek van egy dátuma, ameddig a tanítóadatai terjednek. Ami ezután jelent meg --- a legfrissebb publikációid, a múlt heti preprint, az idei konferencia-absztrakt --- az egyszerűen nem létezik a modell számára.

2. **A te szakterületed nem az ő szakterülete.** Az LLM egy generalista: tud egy kicsit mindenről, de a te specifikus kutatási részterületéről valószínűleg kevesebbet, mint egy elsőéves mesterszakos hallgató, aki éppen elolvasta az utolsó öt review cikket.

3. **A te terminológiád nem az ő terminológiája.** Minden kutatócsoport kifejleszt egy belső nyelvet: rövidítéseket, kódneveket, módszertani zsargont. A „BCR-módszer" vagy a „T3-minta" a te csoportod számára egyértelmű, de az LLM számára értelmezhetetlen.

A kérdés tehát nem az, hogy „hogyan kérdezzek jobban" (az a 2. fejezet témája volt), hanem az, hogy **hogyan adjuk meg az AI-nak a saját tudásunkat**, hogy az válaszaiban használni tudja.

Erre a kérdésre két fundamentálisan különböző válasz létezik, és ebben a fejezetben mindkettőt részletesen megismered.

---

## 9.2 RAG vs. fine-tuning: a két nagy stratégia

Mielőtt belevágnánk a részletekbe, definiáljuk a két kulcsfogalmat, amelyek köré ez a fejezet épül.

### RAG --- Retrieval-Augmented Generation (visszakeresés-kiegészített generálás)

A **RAG (Retrieval-Augmented Generation)** egy olyan architektúra, amelyben az LLM nem a saját „fejéből" válaszol, hanem először visszakeres releváns szövegrészleteket egy külső tudásbázisból, majd ezek kontextusában fogalmazza meg a választ. Olyan ez, mintha a diákod vizsgán használhatná a jegyzeteit: nem kell mindent fejből tudnia, de tudnia kell, hol keresse és hogyan értelmezze az információt.

### Fine-tuning (finomhangolás)

A **fine-tuning (finomhangolás)** ezzel szemben magát a modellt változtatja meg: további tanítópéldákat adunk neki, amelyekből megtanulja az adott terület nyelvét, struktúráját és mintáit. Ez olyan, mintha a diákot egy intenzív kurzusra küldenéd: utána már fejből tudja az anyagot, de a kurzus drága és időigényes.

### Mikor melyiket használd?

| Szempont | RAG | Fine-tuning |
|----------|-----|-------------|
| **Mikor ideális?** | Kérdés-válasz saját dokumentumokból; gyakran változó tudásbázis | Specifikus stílus/formátum megtanítása; osztályozási feladatok |
| **Adatigény** | Bármennyi dokumentum (néhánytól ezrekig) | Néhány tucat--néhány ezer annotált példa |
| **Frissítés** | Azonnal: új dokumentumot hozzáadsz a tudásbázishoz | Újra kell tanítani a modellt (órák/napok) |
| **Költség** | Alacsony--közepes (embedding + tárolás + API hívások) | Közepes--magas (GPU idő vagy API fine-tuning díj) |
| **Transzparencia** | Magas: pontosan látod, milyen forrásból generálta a választ | Alacsony: a modell „fejében" van a tudás, nehéz visszakövetni |
| **Hallucináció-kockázat** | Alacsonyabb: a kontextus korlátozza | Változó: a modell „kreatívan" interpolálhat |
| **Technikai komplexitás** | Közepes: pipeline-t kell építeni | Magas: adatelőkészítés, tanítás, kiértékelés |
| **Tipikus kutatói felhasználás** | „Chatelj a publikációimmal", irodalomkutatás, FAQ bot | Szövegosztályozás, metaadat-kinyerés, doménspecifikus generálás |

**A gyakorlati szabály:** Kezdd RAG-gal. Az esetek 80%-ában ez elég. Fine-tuning-ra akkor térj át, ha a RAG nem ad elég jó eredményt --- és a fejezet végén megmutatom, mikor fordul ez elő.

---

> **Ne csináld!**
> Ne tedd be a teljes PDF-et valtoztatas nelkul a RAG tudaasbazisba. A fejlecek, lablecek, hivatkozaslistak es kepoldalak mind "zajkent" kerulnek be, es az LLM ezekbol is "tudast" generaal. Kulonosen veszelyes a hivatkozaslista bennhagyasa: az AI onnan "levezethet" nem letezo allitasokat. Mindig tisztitsd es strukturald a dokumentumokat a betoltes elott.

## 9.3 A RAG architektúra lépésről lépésre

A RAG nem egyetlen algoritmus, hanem egy **pipeline** --- lépések sorozata, amelyek együttesen teszik lehetővé, hogy az LLM a te adataidból válaszoljon. Nézzük végig minden egyes lépést.

### 9.3.1 Dokumentumbetöltés és előfeldolgozás

Az első lépés egyszerűnek tűnik: töltsd be a dokumentumaidat. A valóságban ez az egyik legkritikusabb pont, mert a „garbage in, garbage out" elv itt hatványozottan érvényesül.

**Milyen dokumentumokból állhat a tudásbázisod?**

- PDF-ek (publikációk, disszertációk, jelentések)
- Word-dokumentumok (laborjegyzetek, protokollok)
- Markdown vagy szöveges fájlok (kódkommentárok, README-k)
- Weboldalak (kari honlap, adatbázis-leírások)
- Prezentációk (PowerPoint)
- Táblázatok (Excel, CSV --- pl. mintaleíró táblázatok szöveges oszlopai)

**Az előfeldolgozás tipikus lépései:**

1. **Szövegkinyerés.** PDF-ből a szöveg kinyerése nem triviális: a kétoszlopos elrendezés, a fejlécek-láblécek, a táblázatok és az ábrák feliratai mind problémát okozhatnak. Olyan könyvtárak, mint a `PyMuPDF`, `pdfplumber` vagy az `unstructured` segítenek.

2. **Tisztítás.** Fejlécek, oldalszámok, hivatkozásblokkok eltávolítása vagy szeparálása. Ha a hivatkozáslistát bennhagyod, az LLM azokat is „tudásként" kezeli --- ami hamis hivatkozásokhoz vezethet.

3. **Metaadat-hozzárendelés.** Minden dokumentumhoz érdemes metaadatot csatolni: szerző, évszám, típus (cikk/jegyzet/protokoll), kulcsszavak. Később ezek alapján szűrhetsz a kereséskor.

4. **Nyelvi előfeldolgozás.** Ha vegyes nyelvű a korpuszod (magyar laborjegyzetek + angol cikkek), döntsd el, hogy külön kezeled-e őket, vagy egy többnyelvű embedding modellt használsz.

### 9.3.2 Chunking: a szöveg feldarabolása

Itt ismerkedjünk meg egy újabb kulcsfogalommal. A **chunk (szövegdarab)** és a **chunking (darabolás)** azt a folyamatot jelenti, amikor a dokumentumaidat kisebb, kereshető egységekre bontod. Ez azért szükséges, mert:

- Az LLM kontextusablaka véges (még ha ma már 128K--1M token is, a válasz minősége az ablak méretével nem lineárisan, hanem szublineárisan javul).
- A visszakeresés pontosabb, ha kisebb, koherens egységeket hasonlítunk össze a kérdéssel.
- A költség arányos a felhasznált tokenek számával.

**Chunking stratégiák:**

**1. Fix méretű chunking**

A legegyszerűbb: vágd a szöveget 500, 1000 vagy 2000 karakteres darabokra.

- *Előny:* Egyszerű, kiszámítható.
- *Hátrány:* A vágás mondat közepén, sőt szó közepén is történhet. Egy bekezdés két chunk-ba kerülhet, elveszítve a koherenciáját.

**2. Fix méretű chunking átfedéssel (overlap)**

Ugyanaz, mint az előző, de minden chunk tartalmazza az előző utolsó 50--200 karakterét is.

- *Előny:* Csökkenti az információveszteséget a határpontokon.
- *Hátrány:* Redundancia, nagyobb tároló- és számításigény.

**3. Mondat- vagy bekezdés-alapú chunking**

A szöveget természetes határpontokon --- mondat- vagy bekezdésvégeken --- vágjuk.

- *Előny:* Koherensebb egységek.
- *Hátrány:* Nagyon változó méretű chunk-ok keletkezhetnek.

**4. Szemantikai chunking**

A legfejlettebb megközelítés: egy embedding modell segítségével meghatározzuk, hol változik jelentősen a szöveg témája, és ott vágunk.

- *Előny:* Minden chunk egyetlen koherens gondolatot tartalmaz.
- *Hátrány:* Számításigényes, komplexebb pipeline.

**5. Dokumentum-struktúra alapú chunking**

Tudományos cikkeknél a fejezetek természetes határt adnak: Abstract, Introduction, Methods, Results, Discussion. Ezeket külön chunk-okként kezelve a struktúra megmarad.

- *Előny:* A legjobb tudományos szövegeknél.
- *Hátrány:* Csak jól strukturált dokumentumoknál működik.

**Gyakorlati javaslat kutatóknak:** Kezdd a fix méretű chunking-gal, 1000 karakter, 200 karakter átfedéssel. Ez az esetek 70%-ában elég jó. Ha a válaszok minősége nem kielégítő, kísérletezz szemantikai vagy struktúra-alapú chunking-gal.

### 9.3.3 Embedding: szövegből számok

Most érkeztünk a RAG szívéhez. Az **embedding (beágyazás)** az a folyamat, amelynek során egy szövegrészletet --- legyen az egy chunk vagy egy kérdés --- egy számvektorrá alakítunk. Ez a vektor nem véletlenszerű szám: a szöveg *jelentését* kódolja egy többszáz- vagy többezerdimenzós térben.

**Miért van erre szükség?**

A számítógépek nem tudnak közvetlenül „jelentést" összehasonlítani. Nem tudják megmondani, hogy a „kadmium speciáció" és a „Cd frakcionálás" ugyanarról szólnak. De ha mindkét kifejezést számvektorrá alakítjuk, amelyben a hasonló jelentésű szövegek egymáshoz közeli pontokba kerülnek, akkor a hasonlóság egyszerű matematikai művelettel mérhető: a két vektor közötti szög koszinusza (cosine similarity).

**Intuitív magyarázat:**

Gondolj egy könyvtárra, ahol a könyveket nem betűrendben, és nem is Dewey-osztályozás szerint rendezik, hanem *jelentés szerint*. A „Talajkémia" és a „Szedimentológia" egymás mellé kerülnének, mert hasonló dolgokról szólnak, hiába kezdődnek más betűvel. Az „Asztrofizika" távol lenne mindkettőtől. Az embedding pontosan ezt teszi: egy „jelentésteret" hoz létre, ahol a hasonló tartalmú szövegek egymáshoz közel vannak.

**Hogyan történik a gyakorlatban?**

Egy előre betanított embedding modell (pl. OpenAI `text-embedding-3-large`, Cohere `embed-multilingual-v3`, vagy a nyílt forráskódú `sentence-transformers` modellek) veszi a szövegedet, és egy fix hosszúságú számvektort ad vissza. Például:

```
"kadmium speciáció folyami üledékben"
    → [0.0234, -0.1456, 0.0891, ..., 0.0567]  (1536 dimenzió)
```

Minden egyes chunk-odat átfuttatod ezen a modellen, és eltárolod a kapott vektorokat. Amikor jön egy kérdés, azt is vektorrá alakítod, és megkeresed a legközelebbi chunk-vektorokat.

**Fontos szempontok kutatóknak:**

- **Többnyelvű modellek.** Ha magyar és angol szövegeid is vannak, válassz többnyelvű embedding modellt (pl. Cohere `embed-multilingual-v3` vagy `multilingual-e5-large`). Ezek képesek megérteni, hogy a „nehézfém-szennyezés" és a „heavy metal contamination" ugyanaz.
- **Domain-specifikus modellek.** Általános célú embedding modellek jól működnek a legtöbb tudományos szöveggel, de ha nagyon speciális a terminológiád (pl. orvosi, jogi, kémiai nómenklatúra), léteznek szakterület-specifikus modellek is (pl. `BiomedBERT`, `SciBERT`).
- **Dimenzionalitás.** Több dimenzió általában jobb minőséget jelent, de nagyobb tárhelyet és lassabb keresést. Az 1536 dimenziós OpenAI embedding vagy a 768 dimenziós nyílt modellek a legtöbb kutatási felhasználásra megfelelőek.

### 9.3.4 Vektor-tár: ahol a tudásod „lakik"

A **vektor-tár (vector store)** egy speciális adatbázis, amelyet nagy mennyiségű vektor hatékony tárolására és keresésére optimalizáltak. Amikor a chunk-jaidat vektorrá alakítottad, ezeket kell valahol eltárolnod, és gyorsan kereshetővé tenned.

**Miért nem elég egy sima adatbázis?**

Egy hagyományos adatbázis (SQL) szöveges egyezés alapján keres: `WHERE title LIKE '%kadmium%'`. Ez nem találja meg a „Cd frakcionálás"-t. A vektor-tár viszont *jelentés alapján* keres: megtalálja az összes szemantikailag hasonló chunk-ot, még ha egyetlen közös szó sincs bennük.

**A legfontosabb vektor-tár opciók:**

| Vektor-tár | Típus | Ideális felhasználás | Ár |
|------------|-------|---------------------|----|
| **FAISS** (Facebook AI Similarity Search) | Lokális könyvtár | Kutatói laptop, prototípus, offline munka | Ingyenes, nyílt forráskódú |
| **ChromaDB** | Lokális / szerver | Kis--közepes méretű projektekhez, fejlesztés | Ingyenes, nyílt forráskódú |
| **Pinecone** | Felhőszolgáltatás | Éles, skálázható alkalmazások | Freemium |
| **Weaviate** | Lokális / felhő | Hibrid keresés (vektor + kulcsszó) | Nyílt forráskódú / managed |
| **Milvus** | Lokális / felhő | Nagy méretű, ipari alkalmazások | Nyílt forráskódú |
| **pgvector** | PostgreSQL kiterjesztés | Ha már van PostgreSQL adatbázisod | Ingyenes |

**Gyakorlati javaslat kutatóknak:**

- **Egyedül dolgozol, saját gépen?** Használj **ChromaDB**-t vagy **FAISS**-t. Telepítés: `pip install chromadb` vagy `pip install faiss-cpu`. Nincs szükség szerverre, felhőre, regisztrációra.
- **Csoportos projekt, megosztott tudásbázis?** **Weaviate** vagy **Pinecone** jó választás, mert webes felületen is kezelhetők.
- **Már van adatbázisod?** A **pgvector** kiterjesztés lehetővé teszi, hogy a meglévő PostgreSQL adatbázisodba integráld a vektorkeresést.

**Hogyan működik a tárolás?**

Minden egyes bejegyzés a vektor-tárban három részből áll:

1. **A vektor** (pl. 1536 szám listája).
2. **A szöveg** (az eredeti chunk).
3. **Metaadatok** (szerző, évszám, dokumentum neve, chunk sorszáma stb.).

```python
# Példa: chunk hozzáadása ChromaDB-hez
collection.add(
    documents=["A kadmium mobilitása savanyú kémhatású üledékekben..."],
    metadatas=[{"source": "Kovacs_2024.pdf", "section": "Results"}],
    ids=["kovacs_2024_chunk_042"]
)
```

### 9.3.5 Visszakeresés: a megfelelő chunk-ok megtalálása

Amikor felteszed a kérdésedet, a következő történik:

1. A kérdésedet ugyanazzal az embedding modellel vektorrá alakítjuk.
2. A vektor-tárban megkeressük az *N* legközelebbi vektort (tipikusan N = 3--10).
3. Visszaadjuk az ezekhez tartozó szöveg-chunk-okat.

**A visszakeresés finomhangolása:**

**Top-K paraméter.** Hány chunk-ot kérünk vissza? Kevesebb (K=3): fókuszáltabb, de lehet, hogy kimarad fontos információ. Több (K=10): teljesebb kép, de zajosabb, és több tokent fogyaszt.

**Hasonlósági küszöb (threshold).** Ne adjunk vissza chunk-ot, ha a hasonlósági pontszám egy küszöb alatt van. Ez megakadályozza, hogy irreleváns szövegrészletek kerüljenek a kontextusba.

**Hibrid keresés.** A legjobb rendszerek kombinálják a szemantikai (vektor) keresést a hagyományos kulcsszavas kereséssel. Így a „BCR-módszer" pontos egyezéssel is megtalálható (kulcsszó), és a „szekvenciális kémiai extrakció" szemantikailag is (vektor).

**Metaadat-szűrés.** „Csak a 2023 utáni publikációkból keress" vagy „Csak a Methods szekciókból keress" --- a metaadatok lehetővé teszik a keresés szűkítését.

**Újrarangsorolás (re-ranking).** Egy kétlépéses megközelítés: először gyorsan visszakeresünk 20--50 chunk-ot, majd egy finomabb modell (pl. Cohere Reranker, `cross-encoder/ms-marco-MiniLM`) újrarendezi ezeket relevancia szerint, és csak a legjobb 3--5-öt küldjük tovább az LLM-nek.

### 9.3.6 Generálás: válasz szintetizálása kontextussal

Az utolsó lépés: a visszakeresett chunk-okat és az eredeti kérdést együtt adjuk az LLM-nek, amely ezek alapján fogalmazza meg a választ.

A háttérben a következő prompt épül fel (egyszerűsítve):

```
Rendszer: Te egy kutatási asszisztens vagy. Csak az alábbi kontextus
alapján válaszolj. Ha a kontextus nem tartalmaz elég információt,
mondd meg őszintén.

Kontextus:
[Chunk 1: "A kadmium mobilitása savanyú kémhatású üledékekben
jelentősen megnő pH 5 alatt... (Kovács et al., 2024)"]
[Chunk 2: "A BCR-módszerrel végzett szekvenciális extrakció
eredményei azt mutatják... (Kovács et al., 2023)"]
[Chunk 3: "A Tisza középső szakaszán gyűjtött üledékminták
nehézfém-koncentrációi... (Nagy et al., 2023)"]

Kérdés: Mi a kadmium speciáció és a szerves anyag tartalom
kapcsolata a Tisza üledékeiben?
```

Az LLM most nem a saját általános tudásából válaszol, hanem a te specifikus kutatási eredményeidből szintetizál. A válasz hivatkozhat a forrásokra, idézhet számadatokat, és pontosan a te terminológiádat használja.

**A teljes RAG pipeline tehát:**

```
Kérdés
  ↓
[Embedding] → kérdés-vektor
  ↓
[Vektor-tár keresés] → top-K chunk
  ↓
[Prompt összeállítás] → kérdés + kontextus
  ↓
[LLM generálás] → válasz forrásokkal
```

> **🗺️ Szakterületi példa: Térbeli RAG környezeti hatásvizsgálathoz**
>
> A geoinformatikában a térbeli RAG a felhasználó kérdéséhez nemcsak szöveges dokumentumokat, hanem releváns téradatokat, korábbi elemzési eredményeket és szabályozási szövegeket is visszakeres — például egy környezeti hatásvizsgálathoz az adott területre vonatkozó Natura 2000 szabályokat és korábbi monitoring eredményeket. A RAG koncepció térbeli kiterjesztése vektor- és gráf-alapú visszakereséssel működik, ahol a szöveges hasonlóság mellett a térbeli közelség is szempont a releváns dokumentumok kiválasztásánál. Ez a megközelítés különösen hasznos, amikor a szabályozási környezet térben változik.
>
> *Forrás: gis ch22, 21.6 „Térbeli RAG: vektor és gráf visszakeresés szakterületi GIS tudáshoz"*

---

## 9.4 Építsünk kutatási dokumentum chatbotot

Most, hogy értjük az elméletet, építsünk valami hasznosat. Három egyre komplexebb felhasználási esetet mutatunk be.

### 9.4.1 „Chatelj a saját publikációiddal"

Ez a leggyakoribb és leghasznosabb kutatói RAG alkalmazás: feltöltöd a saját cikkeidet, disszertáció-fejezeteidet, laborjegyzeteidet, és természetes nyelven kérdezhetsz róluk.

**Tipikus kérdések, amiket egy ilyen rendszernek feltehetsz:**

- „Milyen mintaelőkészítési protokollt használtunk a 2023-as Tisza kampányban?"
- „Melyik cikkünkben írtunk a pH-függő kadmium adszorpcióról, és mit találtunk?"
- „Összegezd a laborjegyzetek alapján, hogyan változott az ICP-MS kalibrációs protokollunk az elmúlt két évben."
- „Van-e ellentmondás a 2022-es és a 2024-es eredményeink között a cink speciációban?"

**A megvalósítás lépései Python-ban (LangChain keretrendszerrel):**

```python
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA

# 1. Dokumentumok betöltése
loader = PyPDFDirectoryLoader("./my_papers/")
documents = loader.load()

# 2. Chunking
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    separators=["\n\n", "\n", ". ", " "]
)
chunks = splitter.split_documents(documents)

# 3. Embedding és vektor-tár létrehozása
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
vectorstore = Chroma.from_documents(
    chunks,
    embeddings,
    persist_directory="./my_research_db"
)

# 4. RAG lánc összeállítása
llm = ChatOpenAI(model="gpt-4o", temperature=0)
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever(
        search_kwargs={"k": 5}
    ),
    return_source_documents=True
)

# 5. Kérdezés
result = qa_chain.invoke(
    "Milyen pH-tartományban figyeltük meg a kadmium
     mobilizációját az üledékmintákban?"
)
print(result["result"])
for doc in result["source_documents"]:
    print(f"  Forrás: {doc.metadata['source']}, "
          f"oldal: {doc.metadata.get('page', '?')}")
```

**Amit ez a 30 sor kód csinál:**

1. Betölti az összes PDF-et a `my_papers` mappából.
2. Feldarabolja őket 1000 karakteres chunk-okra, 200 karakter átfedéssel, természetes szöveghatárokon vágva.
3. Minden chunk-ot vektorrá alakít és eltárol egy ChromaDB adatbázisban.
4. Létrehoz egy kérdés-válasz láncot, amely a legközelebbi 5 chunk alapján válaszol.
5. Megválaszolja a kérdést, és megmutatja, melyik dokumentumból, melyik oldalról származik a válasz.

**Első futtatáskor** a 3. lépés (embedding) percekig tarthat, ha sok dokumentumod van. De a `persist_directory` paraméternek köszönhetően az adatbázis a lemezre mentődik, és legközelebb másodpercek alatt betöltődik.

### 9.4.2 Kutatócsoport FAQ bot

A következő szint: egy megosztott tudásbázis az egész kutatócsoportodnak. Ide kerülhetnek:

- A csoport összes publikációja
- Belső protokollok és SOP-ok (Standard Operating Procedures)
- Korábbi PhD-disszertációk
- Gyakran ismételt kérdések és válaszok az új csoporttagoknak
- Műszer-kezelési útmutatók
- Etikai bizottsági jóváhagyások szövegei
- Pályázati szövegek és beszámolók

**Miért hasznos ez?**

Minden kutatócsoport-vezető ismeri a helyzetet: az új PhD-hallgató ugyanazokat a kérdéseket teszi fel, amelyeket a három évvel ezelőtti is feltett. A protokollok három különböző Word-dokumentumban vannak, amelyek közül kettő elavult. A „hogyan kalibrálom az ICP-MS-t" kérdésre senki sem emlékszik pontosan, mert az, aki bevezette a protokollt, már máshol dolgozik.

Egy FAQ bot, amely a teljes csoporttudásból válaszol, nem csak időt takarít meg --- biztosítja a tudás kontinuitását.

**Gyakorlati tippek a csoportos tudásbázis felépítéséhez:**

1. **Dokumentumok kurálása.** Ne tölts be mindent válogatás nélkül. Jelöld meg az elavult dokumentumokat, vagy adj nekik alacsonyabb súlyt a metaadatokon keresztül.

2. **Metaadat-séma.** Definiálj egységes metaadat-sémát: `{type: "protocol|paper|thesis|manual", year: 2024, author: "...", status: "current|deprecated"}`. Ez lehetővé teszi, hogy a keresés szűrhető legyen.

3. **Rendszeres frissítés.** Állíts be egy egyszerű folyamatot (akár egy mappafigyelőt), amely automatikusan feldolgozza az újonnan hozzáadott dokumentumokat.

4. **Feedback mechanizmus.** Legyen egy „Ez a válasz hasznos volt? Igen/Nem" gomb. A negatív visszajelzések segítenek azonosítani, hol kell javítani a chunking-ot, a promptot vagy a dokumentumokat.

### 9.4.3 Szemantikai keresés kontrollált szótárak felett

Ez a felhasználási eset közvetlenül a NASA LLM Cookbook-ból ered, és különösen hasznos olyan kutatóknak, akik nemzetközi adatbázisokkal dolgoznak.

**A probléma:** Sok tudományos adatbázis hierarchikus, kontrollált szótárat (controlled vocabulary) használ az adatok kategorizálására. Például a NASA GCMD (Global Change Master Directory) kulcsszavai, az MeSH (Medical Subject Headings) az orvosi irodalomban, vagy a GeoRef thesaurus a földtudományokban. Ahhoz, hogy hatékonyan keress ezekben az adatbázisokban, ismerned kell a pontos kulcsszavakat --- ami ritkán triviális.

**A megoldás:** Embedding-eld a teljes kontrollált szótárat, és keresd szemantikailag.

```python
# A NASA Cookbook gpt_embedder.py adaptációja
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

# 1. Kontrollált szótár betöltése
keywords = [
    "EARTH SCIENCE > SOLID EARTH > GEOCHEMISTRY > TRACE ELEMENTS",
    "EARTH SCIENCE > HYDROSPHERE > SURFACE WATER > WATER QUALITY",
    "EARTH SCIENCE > LAND SURFACE > SOILS > HEAVY METALS",
    # ... több ezer bejegyzés
]

# 2. Embedding és indexelés
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
keyword_store = FAISS.from_texts(keywords, embeddings)

# 3. Szemantikai keresés természetes nyelven
query = "kadmium szennyezés folyóvizekben"
results = keyword_store.similarity_search(query, k=5)
for r in results:
    print(r.page_content)

# Eredmény:
# EARTH SCIENCE > HYDROSPHERE > SURFACE WATER > WATER QUALITY
# EARTH SCIENCE > SOLID EARTH > GEOCHEMISTRY > TRACE ELEMENTS
# EARTH SCIENCE > LAND SURFACE > SOILS > HEAVY METALS
```

Látod? A természetes nyelvű, magyar kérdést is megérti a rendszer, és megtalálja a releváns angol kulcsszavakat. Nem kell fejből tudnod, hogy a „kadmium szennyezés" a GCMD rendszerben a „TRACE ELEMENTS" vagy a „HEAVY METALS" kategóriába tartozik-e.

**Az OECD „Finding Relevant Research" jelentés** pontosan erről ír: naponta több mint 4000 biomedikai cikk jelenik meg, és a hagyományos kulcsszavas keresés egyre kevésbé elég. A szemantikai keresés különösen a *multidiszciplináris kutatóknál* hoz áttörést, mert különböző szakterületek eltérő szókinccsel írják le ugyanazt a jelenséget. Az embedding-alapú keresés áthidalja ezt a terminológiai szakadékot.

---

## 9.5 A RAG minőségének kiértékelése

Építettél egy RAG rendszert, kérdezgeted, és a válaszok „jónak tűnnek". De honnan tudod, hogy *tényleg* jók? A „jónak tűnik" nem elég --- különösen nem tudományos kontextusban, ahol a pontosság kritikus.

A NASA OSDR (Open Science Data Repository) kiértékelési keretrendszere egy kiváló minta, amelyet adaptálhatunk.

### 9.5.1 Visszakeresési metrikák: megtaláljuk-e a megfelelő dokumentumokat?

A RAG pipeline első felét --- a visszakeresést --- külön kell értékelni. Hiába jó az LLM, ha rossz chunk-okat kap.

**Recall (fedés):** Az összes releváns chunk közül hányat találtunk meg?

Ha van 10 chunk, amely tartalmazza a választ, és a rendszer ebből 7-et visszaad: recall = 70%.

**Precision (pontosság):** A visszaadott chunk-ok közül hány releváns valóban?

Ha 5 chunk-ot kaptunk vissza, és ebből 3 releváns: precision = 60%.

**Hogyan mérd a gyakorlatban?**

1. Készíts 20--50 teszt kérdés-válasz párt a saját anyagodból.
2. Minden kérdéshez jelöld be, melyik dokumentumok (vagy chunk-ok) tartalmazzák a helyes választ.
3. Futtasd a visszakeresést, és számold ki a recall-t és precision-t.
4. Kísérletezz a paraméterekkel: változtasd a chunk méretet, az átfedést, a top-K értéket, a hasonlósági küszöböt.

**A NASA OSDR kiértékelési notebook** pontosan ezt csinálja: parametrikus söprést (parametric sweep) hajt végre a top-K és a hasonlósági küszöb felett, és ábrákon mutatja, melyik kombináció adja a legjobb eredményt. A tanulság: **a visszakeresési recall és a válaszminőség két független dimenzió** --- lehet, hogy megtalálod a megfelelő chunk-okat, de az LLM rosszul szintetizálja a választ, és fordítva.

### 9.5.2 Válaszminőség metrikák

A pipeline második felét --- az LLM által generált választ --- is mérni kell.

**BERTScore:** Két szöveg szemantikai hasonlóságát méri embedding-ek segítségével. Nem szóegyezést néz, hanem jelentésbeli hasonlóságot. Értéke 0 és 1 között van (1 = tökéletes egyezés).

```python
from bert_score import score

references = ["A kadmium mobilitása pH 5 alatt megnő."]
candidates = ["Savanyú közegben a Cd mobilizációja fokozódik."]

P, R, F1 = score(candidates, references, lang="en")
print(f"BERTScore F1: {F1.item():.3f}")
# Kimenet: BERTScore F1: 0.847
```

Látod: a két mondat egyetlen közös szót nem tartalmaz (ha eltekintünk a névelőktől), mégis magas BERTScore-t kap, mert szemantikailag ugyanazt mondják.

**ROUGE (Recall-Oriented Understudy for Gisting Evaluation):** N-gram átfedés alapú metrika, eredetileg összefoglaló-kiértékelésre fejlesztve. ROUGE-1 (unigram), ROUGE-2 (bigram) és ROUGE-L (leghosszabb közös részsorozat) változatai vannak.

**METEOR (Metric for Evaluation of Translation with Explicit ORdering):** Figyelembe veszi a szinonimákat és a morfológiai változatokat is. Kifinomultabb, mint a ROUGE, de lassabb.

**Mikor melyiket használd?**

| Metrika | Mire jó | Mire nem jó |
|---------|---------|-------------|
| BERTScore | Szemantikai hasonlóság; parafrázisok felismerése | Ha a szó szerinti pontosság fontos (számok, nevek) |
| ROUGE | Gyors, egyszerű összehasonlítás; reprodukálhatóság | Nem érti a szinonimákat |
| METEOR | Kiegyensúlyozott mérés szinonimákkal | Lassabb, komplexebb beállítás |

### 9.5.3 A háromszintű kiértékelés

A NASA Environmental Justice (EJ) notebook egyik legfontosabb tanulsága a **háromszintű kiértékelési keretrendszer**, amelyet minden komoly RAG rendszernél érdemes alkalmazni:

**1. szint: Programmatikus kiértékelés**

Automatikus, kódból futtatható ellenőrzések:

- Van-e válasz egyáltalán? (Nem üres-e?)
- A válasz tartalmazza-e a kulcsszavakat, amelyeket a referencia-válasz is tartalmaz?
- A BERTScore, ROUGE, METEOR értékek egy küszöb felett vannak-e?
- A forrás-hivatkozások létező dokumentumokra mutatnak-e?
- A válasz a megadott formátumban van-e? (Ha JSON-t kértünk, JSON-t kaptunk?)

*Előny:* Gyors, skálázható, reprodukálható. Minden tesztkérdésre lefuttatható.

**2. szint: LLM-bíró (LLM-as-judge)**

Egy másik LLM értékeli a választ --- tipikusan egy erősebb modell, mint amelyik a választ generálta:

```
Értékeld a következő választ 1-5 skálán az alábbi szempontok szerint:
1. Faktikus pontosság (a kontextusnak megfelelő-e?)
2. Teljesség (minden releváns információt tartalmaz-e?)
3. Koherencia (logikus, jól szervezett-e?)
4. Forrás-hűség (csak a kontextusból származó információt
   használ-e, vagy „hallucinál"?)

Kontextus: [...]
Kérdés: [...]
Válasz: [...]
```

*Előny:* Szemantikusan értékel, megérti a parafrázisokat, részletes indoklást adhat.
*Hátrány:* Nem teljesen megbízható --- az LLM-bíró is tévedhet. Ezért kell a 3. szint.

**3. szint: Emberi kiértékelés**

Végül a szakértő (te!) átnéz egy mintát a válaszokból. Ez a legmegbízhatóbb, de a legdrágább és leglassabb módszer.

*Gyakorlati javaslat:* Ne nézd át mind az 500 teszt-választ. Válassz ki 20--30-at, amelyek a programmatikus kiértékelésben a legproblémásabbnak tűntek (alacsony BERTScore, az LLM-bíró alacsony pontszámot adott, stb.), és azokat nézd át kézzel.

**A háromszintű kiértékelés mint tölcsér:**

```
Szint 1: Programmatikus    → 100% lefedettség, alacsony mélység
Szint 2: LLM-bíró         → 100% lefedettség, közepes mélység
Szint 3: Emberi            → 5-10% lefedettség, maximális mélység
```

### 9.5.4 Iterálás: hogyan javítsunk?

A kiértékelés nem egyszeri tevékenység, hanem egy ciklus. Ha az eredmények nem kielégítőek, a következő „csavarokat" forgathatod:

**Ha a visszakeresés gyenge (nem a jó chunk-ok jönnek vissza):**

- Változtasd a chunk méretet (próbálj kisebbet vagy nagyobbat).
- Növeld az átfedést.
- Próbálj más embedding modellt (pl. váltás `text-embedding-ada-002`-ről `text-embedding-3-large`-ra).
- Adj hozzá metaadat-szűrést.
- Próbálj hibrid keresést (vektor + kulcsszó).
- Alkalmazz re-ranking-et.

**Ha a visszakeresés jó, de a válasz gyenge:**

- Finomítsd a rendszer-promptot (legyen specifikusabb az elvárt válaszformátumot illetően).
- Változtasd a top-K értéket (talán túl sok irreleváns chunk zavarba hozza az LLM-et).
- Próbálj erősebb LLM-et (pl. `gpt-4o` helyett `claude-sonnet-4`, vagy fordítva).
- Add hozzá a prompthoz: „Ha a kontextus nem tartalmaz elég információt, mondd meg, ahelyett hogy kitalálnál valamit."

**Ha egyes témakörökben jó, másokban gyenge:**

- Nézd meg, milyen dokumentumok hiányoznak a tudásbázisból.
- Lehet, hogy bizonyos dokumentumok rosszul konvertálódtak (pl. táblázatok, képletek).
- Próbálj domain-specifikus chunking-ot az adott témakörre.

---

## 9.6 Fine-tuning, amikor a RAG nem elég

Most térjünk rá a fejezet másik nagy témájára: mikor és hogyan használjunk fine-tuning-ot.

### 9.6.1 Mikor van szükség fine-tuning-ra?

A válasz: **ritkábban, mint gondolnád**. A RAG + jó prompting az esetek túlnyomó többségében elegendő. De vannak helyzetek, ahol a fine-tuning a jobb --- vagy az egyetlen --- megoldás:

**1. Osztályozási feladatok (encoder fine-tuning)**

Amikor szövegeket kell kategóriákba sorolni: „Ez a cikk melyik kutatási témakörbe tartozik?", „Ez a mintaleírás melyik geológiai formációt jellemzi?", „Ez a betegjelentés melyik diagnózis-csoportba esik?"

Itt a fine-tuning nem egy nagy generatív modellt hangol, hanem egy kisebb, hatékonyabb **encoder modellt** (pl. DistilBERT, RoBERTa) tanít meg a specifikus osztályozásra.

**2. Strukturált metaadat-kinyerés (decoder fine-tuning)**

Amikor szabadon szöveges leírásokból strukturált adatokat kell kinyerni, és a RAG + prompting nem ad elég pontos eredményt. Például: egy weboldal szövegéből kinyerni a szerzőt, a dátumot, a földrajzi területet, a módszertant és az adattípust egy előre definiált séma szerint.

**3. Specifikus stílus vagy formátum megtanítása**

Amikor az LLM-nek egy nagyon specifikus stílusban vagy formátumban kell generálnia (pl. szabadalmi leírások, klinikai jelentések, specifikus XML/JSON sémák).

**4. Konzisztencia és sebesség**

Fine-tuning után a modell gyorsabban és konzisztensebben válaszol, mert nem kell minden alkalommal a prompt-ban elmagyarázni, mit és hogyan csináljon.

### 9.6.2 Encoder fine-tuning osztályozáshoz

A NASA EJ (Environmental Justice) notebook egyik legmeggyőzőbb eredménye az encoder fine-tuning előnye osztályozási feladatokban.

**A feladat:** Környezeti igazságosság adathalmazok szöveges leírásait 8 klímaindikátor-kategóriába kellett sorolni.

**Az összehasonlítás:**

| Módszer | Pontosság | Sebesség |
|---------|-----------|----------|
| GPT-3.5 zero-shot (prompting, tanítás nélkül) | 54% | 2 minta/mp |
| GPT-3.5 few-shot (néhány példa a promptban) | 62% | 2 minta/mp |
| Fine-tuned DistilBERT | **96%** | **69 minta/mp** |

A különbség drámai: a fine-tuned kis modell **majdnem kétszer olyan pontos** és **35-ször gyorsabb**, mint a nagy generatív modell prompting-gal. Ráadásul a DistilBERT futtatható a saját gépeden, nincs API-költség, és az adatok nem hagyják el a gépet.

**Mikor érdemes encoder fine-tuning-ot alkalmazni?**

- Van legalább 50--100 annotált példád (ideálisan 200+).
- A feladat jól definiált kategóriákba sorolás.
- Fontos a sebesség (sok szöveget kell feldolgozni).
- Fontos az adatvédelem (nem akarsz mindent API-n küldeni).

**A gyakorlati lépések:**

1. Gyűjts annotált példákat: szöveg + helyes kategória.
2. Oszd fel: 80% tanítás, 20% tesztelés.
3. Válassz alapmodellt: `distilbert-base-uncased` (angol) vagy `bert-base-multilingual-cased` (többnyelvű).
4. Fine-tune-olj a HuggingFace `Trainer` API-val (általában 3--5 epoch elég).
5. Értékeld ki a teszt halmazon.

### 9.6.3 Decoder fine-tuning generáláshoz

Amikor nem osztályozni, hanem *generálni* akarsz --- szöveget, metaadatot, összefoglalót --- egy specifikus formátumban és stílusban, a decoder (generatív) modell fine-tuning-ja a megfelelő eszköz.

**A NASA EJ fine-tuning notebook** a GPT-3.5-turbo modellt fine-tune-olta metaadat-kinyerésre. A folyamat:

1. **Tanítóadatok előkészítése JSONL formátumban:**

```json
{"messages": [
  {"role": "system", "content": "Extract metadata from the following dataset description."},
  {"role": "user", "content": "The EJSCREEN dataset provides environmental and demographic data for census block groups across the United States..."},
  {"role": "assistant", "content": "{\"title\": \"EJSCREEN\", \"spatial_coverage\": \"United States\", \"temporal_coverage\": \"2015-2023\", \"data_type\": \"environmental indicators\"}"}
]}
```

2. **Fine-tuning az OpenAI API-n keresztül:**

```python
from openai import OpenAI
client = OpenAI()

# Tanítófájl feltöltése
file = client.files.create(
    file=open("training_data.jsonl", "rb"),
    purpose="fine-tune"
)

# Fine-tuning indítása
job = client.fine_tuning.jobs.create(
    training_file=file.id,
    model="gpt-4o-mini-2024-07-18"
)
```

3. **A fine-tuned modell használata** ugyanúgy, mint bármely más OpenAI modellt, csak a modell nevét kell kicserélni.

### 9.6.4 Kis adathalmaz, nagy hatás: a NASA 40 példás leckéje

A NASA EJ notebook egyik legfontosabb tanulsága: **akár ~40 tanítópélda is elegendő lehet** egy hasznos fine-tuned modellhez.

Ez ellentmond annak a széles körben elterjedt tévhitnek, hogy a fine-tuning-hoz hatalmas adathalmazok kellenek. A valóság árnyaltabb:

**Mikor elég kevés példa?**

- Amikor a feladat jól definiált és szűk (pl. egy specifikus metaadat-séma kinyerése).
- Amikor az alapmodell már „majdnem tudja" --- csak a specifikus formátumot és doméntudást kell megtanulni.
- Amikor a példák változatosak és jó minőségűek (nem 40-szer ugyanaz, hanem 40 különböző eset).

**Mikor kell több adat?**

- Sok kategória (20+) esetén.
- Zajos, inkonzisztens szövegeknél.
- Amikor az alapmodell messze van a céltól (pl. egy általános modell nagyon specifikus orvosi terminológiával).

**Gyakorlati tanács:** Kezdd 30--50 gondosan válogatott és annotált példával. Fine-tune-olj, értékelj, és csak akkor gyűjts további adatot, ha az eredmény nem kielégítő. Ne ess abba a csapdába, hogy „előbb gyűjtsünk 10 000 példát, aztán tanítunk" --- iteratív megközelítéssel sokkal hatékonyabb.

---

## 9.7 Összefoglalás: a tudásgazdagítás döntési fája

> **🖼️ Ábra: RAG vs. Fine-tuning vs. Prompt Engineering döntési fa**
> *Döntési fa: "Van saját dokumentumgyűjteményed?" → "Változik-e gyakran?" → "Mekkora a költségvetésed?" Leveleken: RAG, Fine-tuning, Prompt Engineering, és azok kombinációi.*


Amikor az általános LLM nem elég, és a saját adataidra van szükséged, a következő döntési fát kövesd:

```
A feladat: az LLM a saját adataimból válaszoljon
│
├─ Kérdés-válasz saját dokumentumokból?
│  └─ → RAG (ez a fejezet fő témája)
│
├─ Szövegosztályozás (kategorizálás)?
│  └─ → Encoder fine-tuning (DistilBERT, RoBERTa)
│
├─ Strukturált kinyerés specifikus formátumban?
│  ├─ Próbáld először RAG + prompting-gal
│  └─ Ha nem elég pontos → Decoder fine-tuning
│
├─ Specifikus stílus/formátum generálása?
│  └─ → Decoder fine-tuning
│
└─ Nem vagy biztos?
   └─ → Kezdd RAG-gal. Mindig.
```

**Az arany szabály:** A RAG olcsóbb, gyorsabb, transzparensebb és rugalmasabb, mint a fine-tuning. Csak akkor lépj tovább a fine-tuning felé, ha a RAG-ot már kipróbáltad és kiértékelted, és az eredmény nem kielégítő.

> **🌾 Szakterületi példa: LLM-ek és a mezőgazdasági szakterminológia**
>
> A mezőgazdasági RAG-rendszereknél a legnagyobb kihívás, hogy az általános célú LLM-ek nem ismerik a helyi szakterminológiát (pl. belvíz, szikes talaj, őszi búza fajtanevek) — a RAG a helyi agrártudásbázissal egészíti ki a modellt. A mezőgazdasági nyelv rendkívül specializált, olyan szakterminológiával és helyi növénynevekkel, amelyek nem feltétlenül szerepelnek megfelelően az általános célú nyelvi modellek betanítási adataiban. A RAG-alapú megközelítés itt különösen hatékony, mert a helyi tudásbázist anélkül teszi elérhetővé az LLM számára, hogy a modellt magát kellene finomhangolni.
>
> *Forrás: precagri ch15, 15.7.3 „Kihívások és korlátok"*

---

## 9.8 Kulcsfogalmak összefoglalása

> **🖼️ Ábra: A RAG-rendszer komponensei és azok kapcsolatai**
> *Rendszer-architektúra diagram: Felhasználói kérdés → Retriever → Vektor-adatbázis → Releváns chunk-ok → LLM → Válasz (forrás-hivatkozásokkal). Feedback-hurok jelölve.*


| Fogalom | Definíció |
|---------|-----------|
| **RAG (Retrieval-Augmented Generation)** | Visszakeresés-kiegészített generálás: az LLM külső tudásbázisból visszakeresett szövegrészletek kontextusában generálja a választ, nem a saját „fejéből" |
| **Embedding (beágyazás)** | Szöveg átalakítása fix méretű számvektorrá, amely a szöveg jelentését kódolja egy többdimenziós térben; hasonló jelentésű szövegek hasonló vektorokat kapnak |
| **Vektor-tár (vector store)** | Speciális adatbázis, amely vektorok hatékony tárolására és hasonlóság-alapú keresésére optimalizált (pl. FAISS, ChromaDB, Pinecone) |
| **Fine-tuning (finomhangolás)** | A modell paramétereinek további tanítása saját példák alapján, hogy az adott feladatra specializálódjon |
| **Chunk / chunking** | Szövegdarab / a szöveg kisebb, kereshető egységekre bontásának folyamata; a RAG pipeline alapvető lépése |

---

## 9.9 Amit ebben a fejezetben nem tárgyaltunk

- **Általános prompting technikák** --- lásd a 2. fejezetet.
- **Vizuális RAG építés LangFlow-val** --- lásd a 8. fejezetet, ahol kód nélkül, drag-and-drop felületen építhetsz RAG pipeline-t.
- **Ágens rendszerek**, amelyek a RAG-ot eszközként használják komplex, többlépéses feladatokhoz --- lásd a 11--12. fejezetet.
- **Etikai kérdések**, adatvédelem, reprodukálhatóság --- lásd a 16. fejezetet.

---

## Irodalom és további olvasmányok

- Lewis, P. et al. (2020). Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks. *NeurIPS*.
- NASA SMD AI Initiative (2024). LLM Cookbook for Open Science. GitHub repository.
- Rafols, I. et al. (2023). Finding relevant research more efficiently with semantic analysis. In: *OECD, Artificial Intelligence in Science*.
- Gentemann, C. et al. (2021). Science storms the cloud. *AGU Advances*, 2(2).
- Sanh, V. et al. (2019). DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter. *arXiv:1910.01108*.
