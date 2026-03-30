# Függelék C: Források és további olvasmányok

> *"A jó kutató nem mindent tud, hanem tudja, hol keresse."*

Ez a függelék a könyv témáihoz kapcsolódó legfontosabb forrásokat gyűjti össze: könyveket, tanulmányokat, online kurzusokat, közösségeket és magyar nyelvű erőforrásokat. A lista nem törekszik teljességre -- az AI világa olyan gyorsan változik, hogy bármely kimerítő bibliográfia a megjelenés pillanatában elavulna. Ehelyett a **tartós értékű, megalapozó művekre** koncentrálunk, amelyek keretrendszereket és gondolkodásmódokat adnak, nem csupán technikai részleteket.

Az annotációk minden könyvnél jelzik, hogy milyen típusú olvasó számára a leghasznosabb, és mit érdemes belőle elsőként elolvasni.

---

![Ajánlott olvasmányok szakterület szerint — vizuális útmutató](images/appendix_c_reading_map.png)

## C.1 Ajánlott könyvek (annotált lista)

### Általános AI-stratégia és gondolkodásmód

**Ethan Mollick: *Co-Intelligence: Living and Working with AI*** (Portfolio/Penguin, 2024)
A könyv legfontosabb üzenete: az AI nem eszköz, hanem *együttműködő partner*, és a sikeres használathoz meg kell változtatnunk a munkáról alkotott elképzeléseinket. Mollick a Wharton Business School professzora, aki több ezer órát töltött az LLM-ek kísérletezésével. **Kezdd a 3. fejezettel** ("Be the human in the loop"), amely a gyakorlati keretrendszert adja az emberi-AI együttműködéshez. A könyv különösen erős az oktatási alkalmazások és a kreatív felhasználás területén -- ezért is hivatkozunk rá a könyv több fejezetében.
→ https://www.oneusefulthing.org/

**Arvind Narayanan & Sayash Kapoor: *AI Snake Oil: What Artificial Intelligence Can Do, What It Can't, and How to Tell the Difference*** (Princeton University Press, 2024)
A kritikus gondolkodás bibliája az AI-korszakban. A szerzők -- Princeton professzora és doktorandusza -- rendszeresen leleplezik a túlzó AI-állításokat a blogjaikon, és ez a könyv ezt a munkát foglalja keretrendszerbe. **Minden tudósnak kötelező olvasmány**, különösen a 2. rész ("AI as Snake Oil"), amely megtanítja, hogyan ismerjük fel a megbízhatatlan AI-alapú predikciós rendszereket. A 4. fejezet a generatív AI kockázatairól különösen releváns a tudományos kontextusban.
→ https://www.aisnakeoil.com/

### Tudományos írás és kutatás

**Hanning Han & Simon Qiu: *ChatGPT in Scientific Research: A Practical Guide to Using AI in Academic Writing, Data Analysis, and Research Methodologies*** (Springer, 2025)
A legátfogóbb gyakorlati útmutató az LLM-ek tudományos kutatásban való alkalmazásához. Különösen értékes az irodalomkutatási fejezet (Chapter 3) és az adatelemzési munkafolyamatok leírása (Chapter 5). **Kezdd a "Prompt Engineering for Researchers" fejezettel** -- ez a könyv leginkább alkalmazható része. A szerzők reálisan tárgyalják a korlátokat is: mikor *ne* használj AI-t a kutatásban.

### Ágensek és automatizálás

**Xin Huang: *Agentic AI: Theories and Practices*** (Packt, 2025)
A könyv legfőbb erőssége az ágens-architektúrák rendszerezett bemutatása: ReAct, Plan-and-Execute, multi-agent rendszerek. **A 11-12. fejezetünk technikai hátteréhez nélkülözhetetlen referencia.** Különösen ajánlott a 4. fejezet (tool use) és a 7. fejezet (multi-agent collaboration). A kódpéldák Python és LangChain alapúak, de a koncepciókat bármely keretrendszerre alkalmazhatod.

### Oktatás és egyetemi alkalmazás

**José Antonio Bowen & C. Edward Watson: *Teaching with AI: A Practical Guide to a New Era of Human Learning*** (Johns Hopkins University Press, 2024)
Az egyetemi oktatók számára írt legteljesebb útmutató az AI-korszakhoz. A szerzők nem a technológiára, hanem a **pedagógiára** koncentrálnak: hogyan tervezzünk kurzusokat, vizsgákat és feladatokat úgy, hogy az AI eszköz legyen, ne pedig a csalás eszköze. **Kezdd a 6. fejezettel** ("Assessment in the Age of AI"), amely a leggyakrabban felmerülő kérdésekre ad gyakorlati válaszokat. A 15. fejezetünk egyik fő forrása.
→ https://teachingwithai.org/

**Sal Khan: *Brave New Words: How AI Will Revolutionize Education (and Why That's a Good Thing)*** (Viking, 2024)
A Khan Academy alapítójának víziója az AI-ról az oktatásban. Kevésbé akadémikus, mint Bowen & Watson, de **inspiráló és hozzáférhető olvasmány**, amely a Khanmigo fejlesztési tapasztalatain keresztül mutatja be az AI-tutoring lehetőségeit. A 4-6. fejezetek a személyre szabott tanulásról különösen relevánsak az egyetemi kontextusban.

### Programozás és adattudomány

**Simon Lynch: *Python for Scientific Computing*** (Cambridge University Press, 2024)
Nem AI-könyv, hanem **a Python nyelv tudósok számára írt legjobb bevezetése**. Ha a könyv kódpéldáit szeretnéd megérteni és adaptálni, ez az alapmű. Különösen erős a NumPy, SciPy és Matplotlib fejezetekben. **Kezdd a 3. fejezettel** (NumPy), mert a legtöbb tudományos AI-munkafolyamat erre épül.

**Leo Porter & Daniel Zingaro: *Learn AI-Assisted Python Programming: With GitHub Copilot and ChatGPT*** (Manning, 2024)
Kifejezetten nem programozóknak írt könyv arról, hogyan használj AI-t a kódoláshoz. **Ha egyetlen programozási könyvet olvasol el, ez legyen az.** A szerzők (mindketten egyetemi informatika-oktatók) a "prompt-first" megközelítést tanítják: először természetes nyelven fogalmazd meg, amit akarsz, aztán az AI generálja a kódot. Az 5. fejezetünk filozófiája nagyrészt erre a könyvre épül.

### Szakterület-specifikus AI

**Gustau Camps-Valls et al. (eds.): *Deep Learning for the Earth Sciences: A Comprehensive Approach to Remote Sensing, Climate Science, and Geosciences*** (Wiley, 2021)
A földtudományok és távérzékelés területén ez a **standard referenciamű** a mélytanulás alkalmazásához. Bár 2021-es kiadás, az alapelvek (konvolúciós hálók térbeli adatokon, idősor-elemzés LSTM-mel, fizikai korlátok beépítése) ma is érvényesek. **A 9. fejezetünk olvasóinak különösen ajánlott** a remote sensing fejezet (Part II).

**Peter Lee, Carey Goldberg & Isaac Kohane: *The AI Revolution in Medicine: GPT-4 and Beyond*** (Pearson, 2023)
Az első átfogó mű arról, hogyan változtatják meg az LLM-ek az orvostudományt. Peter Lee a Microsoft Research elnöke, Isaac Kohane a Harvard orvosi informatikai tanszékének vezetője -- tehát a könyv mind az ipari, mind az akadémiai perspektívát hozza. **Különösen értékes a diagnosztikai esettanulmányok fejezete** és az orvos-beteg kommunikáció AI-támogatásáról szóló rész.

### Vizuális adattudomány és no-code eszközök

**Frank Acito: *Predictive Analytics with KNIME: Analytics for Citizen Data Scientists*** (Springer, 2023)
A KNIME platformot bemutató **legjobb angol nyelvű könyv**, amely nem informatikusoknak, hanem "citizen data scientist"-eknek szól -- pontosan a mi célközönségünknek. A 8. fejezetünk KNIME-munkafolyamatainak megértéséhez ez a legjobb kiegészítő forrás. **Kezdd a 4. fejezettel** (Classification), amely a legtöbb tudományos alkalmazás alapja.
→ https://www.knime.com/knime-textbook

### Digitális ikrek

**Manu Mitra, Hiren Kumar Thakker & Halil Pervez: *Digital Twin: A Comprehensive Guide to Building, Deploying, and Scaling*** (Packt, 2024)
A digitálisiker-technológia **gyakorlati kézikönyve**, amely az elmélet mellett konkrét megvalósítási lépéseket is tartalmaz. A 10. fejezetünk kontextusában különösen értékes a "Digital Twin Architecture" és a "Data Integration" fejezet. A könyv gyengesége, hogy erősen IoT-fókuszú -- a tudományos digitális ikrek (pl. klímamodellek, ökoszisztéma-modellek) kevesebb figyelmet kapnak.

### Szabályozás és kormányzás

**Justin B. Bullock, Yu-Che Chen, Johannes Himmelreich, Valerie M. Hudson, Anton Korinek, Matthew M. Young & Baobao Zhang (eds.): *The Oxford Handbook of AI Governance*** (Oxford University Press, 2024)
Az AI-szabályozás és -kormányzás **enciklopédikus referenciája**: 60+ fejezet a világ vezető szakértőitől. Nem kell elejétől a végéig olvasni -- használd kézikönyvként. **A 16. fejezetünk olvasóinak különösen ajánlott** a tudományos AI-etika fejezete és az EU AI Act elemzése.
→ https://academic.oup.com/edited-volume/56777

---

## C.2 Kulcscikkek és tanulmányok

### Tudományos AI-módszertan

**Poldrack, R.A. et al.: "Ten Simple Rules for AI-Assisted Coding in Science"** (PLOS Computational Biology, 2025)
Tíz egyszerű, azonnal alkalmazható szabály az AI-asszisztált kódoláshoz a tudományban. A cikk különösen erős a reprodukálhatóság és a kódvalidáció területén. **Ha egyetlen cikket olvasol el ebből a listából, ez legyen az.**
→ https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1012857

**"Agentic AI for Scientific Discovery: A Survey"** (ICLR 2025 Workshop Paper)
Az ágentikus AI tudományos alkalmazásainak első átfogó felmérése. A cikk rendszerezi az irodalmat: hipotézis-generálás, kísérlettervezés, adatelemzés és publikálás. **A 11-12. fejezeteink tudományos háttere.**

### Szakpolitikai dokumentumok

**OECD: *Artificial Intelligence in Science: Challenges, Opportunities and the Future of Research*** (OECD Publishing, 2023)
Az OECD 2023-as jelentése a mesterséges intelligencia tudományos kutatásra gyakorolt hatásáról. **A legátfogóbb szakpolitikai elemzés**, amely 40+ ország adatait szintetizálja. Különösen értékes az Open Science és az AI kapcsolatát tárgyaló fejezet.
→ https://www.oecd.org/publications/artificial-intelligence-in-science-a8d820bd-en.htm

**European University Association (EUA): *Adopting AI that Serves Universities: The EUA Approach*** (EUA, 2026)
Az Európai Egyetemi Szövetség legfrissebb iránymutatása az AI egyetemi bevezetéséhez. **A 15. fejezetünk egyik kulcsforrása**, különösen az intézményi stratégia és a minőségbiztosítás területén.
→ https://eua.eu/

**National Academies of Sciences, Engineering, and Medicine: *The Age of AI in Life Sciences*** (The National Academies Press, 2025)
Az Egyesült Államok Nemzeti Akadémiáinak konszenzus-tanulmánya az AI élettudomány-beli alkalmazásairól. **Különösen értékes a "responsible AI" keretrendszer** és a kutatási prioritások meghatározása.
→ https://nap.nationalacademies.org/

**National Academies of Sciences, Engineering, and Medicine: *Foundational Research Gaps and Future Directions for Digital Twins*** (The National Academies Press, 2024)
A digitális ikrek kutatási hiányosságainak és jövőbeli irányainak elemzése. **A 10. fejezetünk ajánlott kiegészítő olvasmánya**, különösen a modellvalidáció és az adatintegráció területén.
→ https://nap.nationalacademies.org/catalog/26894/

### Gyakorlati útmutatók

**NASA: *LLM Cookbook for Open Science*** (NASA Transform to Open Science)
A NASA nyílt tudományhoz készített LLM-útmutatója, amely konkrét recepteket ("recipes") ad az LLM-ek tudományos munkafolyamatokba való integrálásához. **Gyakorlatias és azonnal alkalmazható.**
→ https://github.com/nasa/

**World Economic Forum: *AI Procurement Guidelines*** (WEF, 2023)
Az AI-beszerzés irányelvei -- releváns minden kutató számára, aki intézményi szinten dönt AI-eszközök vásárlásáról. **A 14. fejezetünk költségvetési tervezéséhez hasznos keretrendszer.**
→ https://www.weforum.org/publications/ai-procurement-in-a-box/

---

## C.3 Online kurzusok és tanúsítványok

### Ingyenes bevezető kurzusok

| Kurzus | Platform | Nyelv | Szint | Időtartam |
|--------|----------|-------|-------|-----------|
| **Elements of AI** | University of Helsinki / MinnaLearn | angol (+ 25 nyelv) | kezdő | 30 óra |
| **AI for Everyone** | Coursera (Andrew Ng) | angol (felirattal) | kezdő | 10 óra |
| **Google AI Essentials** | Coursera (Google) | angol | kezdő | 15 óra |
| **Introduction to Generative AI** | Google Cloud Skills Boost | angol | kezdő | 1 óra |
| **ChatGPT Prompt Engineering for Developers** | DeepLearning.AI | angol | kezdő-haladó | 2 óra |

**Elements of AI** — A Helsinki Egyetem és a MinnaLearn közös projektje, amely ingyenesen elérhető és **több mint 25 nyelven** (sajnos magyarul nem) tanítja az AI alapjait. Nem technikai hátteret igényel, és kifejezetten nem programozóknak készült. **Minden tudósnak ajánlott kiindulópont**, aki még nem mélyedt el az AI-ban.
→ https://www.elementsofai.com/

**Google AI Essentials** — A Google által készített, ingyenes kurzus, amely a generatív AI alapjait és gyakorlati alkalmazásait mutatja be. **Különösen hasznos a prompting technikák** elsajátításához, és a kurzus végén Google-tanúsítványt kapsz.
→ https://grow.google/ai-essentials/

### Haladó és szakmai kurzusok

| Kurzus | Platform | Szint | Ár (kb.) |
|--------|----------|-------|-----------|
| **Agentic AI Certificate** | Johns Hopkins University | haladó | $2,500 |
| **NVIDIA Deep Learning Institute (DLI)** | NVIDIA | közép-haladó | ingyenes–$100/kurzus |
| **Practical Deep Learning for Coders** | fast.ai | haladó | ingyenes |
| **AI for Science Specialization** | Coursera (többféle) | közép | $49/hó |
| **Machine Learning Specialization** | Coursera (Stanford/DeepLearning.AI) | közép | $49/hó |
| **Professional Certificate in TinyML** | edX (Harvard) | közép-haladó | $149 |

**Johns Hopkins University — Agentic AI Certificate** — Az első akkreditált egyetemi tanúsítvány kifejezetten az ágentikus AI területén. A program az ágens-architektúrákat, a tool use-t és a multi-agent rendszereket tárgyalja. **A 11-13. fejezeteink olvasóinak ideális következő lépés.**
→ https://ep.jhu.edu/

**NVIDIA Deep Learning Institute (DLI)** — Az NVIDIA saját kurzusplatformja, amely GPU-gyorsított mélytanulást tanít. A kurzusok egy része ingyenes, és **minden hallgató felhőalapú GPU-hozzáférést kap** a gyakorlatokhoz. Különösen ajánlott: "Fundamentals of Deep Learning" és "Building RAG Agents with LLMs".
→ https://www.nvidia.com/en-us/training/

**fast.ai — Practical Deep Learning for Coders** — Jeremy Howard legendás kurzusa, amely a "top-down" megközelítéssel tanítja a mélytanulást: **először a gyakorlat, aztán az elmélet**. Teljesen ingyenes, és a könyv (is ingyenesen elérhető) az egyik legjobb mélytanulás-bevezető.
→ https://www.fast.ai/

---

## C.4 Közösségek és fórumok

### Technikai közösségek

**Hugging Face Community**
A nyílt forráskódú AI-modellek és adatkészletek legnagyobb platformja. A Hugging Face Hub több mint 500 000 modellt és 100 000 adatkészletet tartalmaz. **Ide töltsd fel a kutatási modelljeidet és adataidat** -- ez a tudományos AI nyílt ökoszisztémájának központja.
→ https://huggingface.co/

**Stack Overflow — AI/ML Tags**
A programozói kérdések klasszikus fóruma. Az `[artificial-intelligence]`, `[machine-learning]`, `[large-language-model]` és `[langchain]` tagek a legaktívabbak. **Konkrét technikai problémák esetén ez a legjobb kiindulópont.**
→ https://stackoverflow.com/questions/tagged/large-language-model

**KNIME Community Forum**
A KNIME vizuális adattudomány-platform közösségi fóruma. A 8. fejezetben bemutatott no-code munkafolyamatokhoz itt találsz segítséget és példákat.
→ https://forum.knime.com/

**n8n Community**
Az n8n automatizálási platform közössége. A 7. fejezetben bemutatott adat-pipeline-okhoz és a 12. fejezetben leírt ágensépítéshez hasznos forrás.
→ https://community.n8n.io/

### Közösségi platformok és vitafórumok

**Reddit — r/MachineLearning**
Az AI/ML kutatás legnagyobb Reddit-közössége (3M+ tag). **Az új cikkek és kutatási eredmények leggyorsabb megjelenési helye** a szakfolyóiratokon kívül. A heti "What are you reading?" és "Simple Questions" szálak különösen hasznosak.
→ https://www.reddit.com/r/MachineLearning/

**Reddit — r/LocalLLaMA**
A helyi (lokális) LLM-futtatás közössége. **Ha a 14. fejezetben leírt on-premises AI-labor érdekel**, itt találod a legfrissebb információkat a modellekről, kvantálási technikákról és hardverkövetelményekről.
→ https://www.reddit.com/r/LocalLLaMA/

**Discord — Claude Code Community**
Az Anthropic Claude Code eszközének közössége, ahol a fejlesztők és felhasználók tapasztalataikat osztják meg. **A könyvben használt Claude-alapú munkafolyamatokhoz hasznos forrás.**

**Discord — Cursor Community**
A Cursor AI-kódszerkesztő közössége. Az 5. fejezetben bemutatott AI-asszisztált kódoláshoz kapcsolódó kérdésekre itt kapsz választ.

---

## C.5 Magyar nyelvű AI-források

### Magyar nyelvi AI-modellek és NLP-eszközök

**PULI GPT — Magyar nagy nyelvi modellek**
A BME Méréstechnika és Információs Rendszerek Tanszékén fejlesztett PULI GPT modellek a **legnagyobb nyíltan elérhető magyar nyelvű LLM-ek**. A modellek a Hugging Face-en elérhetők, és a magyar nyelvű szöveggenerálás, összefoglalás és válaszadás területén a legjobbak közé tartoznak. A kutatási célú felhasználás szabadon engedélyezett.
→ https://huggingface.co/NYTK

**HuSpaCy — Magyar nyelvű NLP-könyvtár**
A spaCy keretrendszerre épülő, **kifejezetten magyar nyelvre optimalizált** természetesnyelv-feldolgozó könyvtár. Szófaji elemzés, névelemfelismerés, mondatelemzés és lemmatizálás magyarul. **Nélkülözhetetlen minden magyar szövegeket feldolgozó kutatási projekthez.**
→ https://github.com/huspacy/huspacy

### Intézmények és szervezetek

**MI Koalíció (Mesterséges Intelligencia Koalíció)**
Magyarország legnagyobb AI-szakmai szervezete, **több mint 400 taggal** (vállalatok, egyetemek, kutatóintézetek, startupok). Az MI Koalíció munkacsoportjai az oktatástól az egészségügyig, az ipartól a közigazgatásig minden területet lefednek. Rendszeres konferenciáik és webinárjaik a **legfontosabb magyar nyelvű AI-szakmai találkozók**.
→ https://digitalisjoletprogram.hu/hu/tartalom/mesterseges-intelligencia-koalicio

**MILAB — Mesterséges Intelligencia Nemzeti Laboratórium**
A Magyar Tudományos Akadémia (HUN-REN) keretében működő nemzeti laboratórium, amely az **alapkutatástól az alkalmazott kutatásig** fedi le az AI-t. Kutatási területeik: számítógépes látás, természetes nyelvfeldolgozás, autonóm rendszerek, egészségügyi AI. **Pályázati együttműködésekre nyitottak.**
→ https://mi.nemzetilabor.hu/

**HUN-REN Kutatóhálózat — AI-kezdeményezések**
A Magyar Kutatási Hálózat (HUN-REN) keretében számos intézetben folyik AI-kutatás. A **Számítástechnikai és Automatizálási Kutatóintézet (SZTAKI)** és a **Rényi Alfréd Matematikai Kutatóintézet** a legaktívabb szereplők. Az intézethálózat nyílt adatplatformjain keresztül kutatási adatokhoz is hozzáférhetsz.
→ https://www.hun-ren.hu/

### Magyar AI-oktatás

**Debreceni Egyetem — "Korszerű MI" kurzus**
A Debreceni Egyetem Informatikai Karán elérhető kurzus, amely a **modern AI-technológiákat** mutatja be hallgatóknak és kutatóknak. A kurzus anyaga szabadon elérhető, és a gyakorlati alkalmazásokra helyezi a hangsúlyt.

**AI Expert posztgraduális szak (Debreceni Egyetem, Informatikai Kar)**
Magyarország első **kifejezetten AI-ra specializált posztgraduális képzése**. A szak a mesterséges intelligencia elméletét és gyakorlatát egyaránt lefedi, és kutatóknak, mérnököknek és döntéshozóknak szól. A képzés blended (jelenléti + online) formában érhető el.
→ https://inf.unideb.hu/

### Számítási infrastruktúra

**Komondor szuperszámítógép (KIFU)**
A Kormányzati Informatikai Fejlesztési Ügynökség (KIFU) üzemeltetésében működő **Komondor szuperszámítógép** Magyarország legnagyobb számítási kapacitása. GPU-klaszterekkel rendelkezik, amelyek kifejezetten AI/ML-feladatokhoz alkalmasak. **Magyar kutatók és egyetemi hallgatók számára pályázati úton elérhető.**
→ https://kifu.gov.hu/

### Stratégiai dokumentumok

**Magyar AI Stratégia 2025–2030**
Magyarország nemzeti mesterséges intelligencia stratégiája, amely a **kutatás, oktatás, ipar és közigazgatás** területén határozza meg a fejlesztési irányokat. A stratégia kiemelt területei: egészségügy, mezőgazdaság, közlekedés és gyártás. **Minden magyar kutatónak érdemes ismernie**, különösen pályázati kontextusban.
→ https://kormany.hu/

---

## C.6 Szakterület-specifikus könyvajánlók

Az alábbi lista szakterületenként ajánl 2-3 könyvet és forrást azok számára, akik az AI-t egy konkrét tudományterületen szeretnék alkalmazni.

### Orvostudomány és egészségügy

- **Peter Lee, Carey Goldberg & Isaac Kohane: *The AI Revolution in Medicine*** (Pearson, 2023) — Lásd a C.1 részletes leírását. Az orvostudomány és az LLM-ek kapcsolatának alapműve.
- **Eric Topol: *Deep Medicine: How Artificial Intelligence Can Make Healthcare Human Again*** (Basic Books, 2019) — Bár korábbi kiadás, Topol víziója a "deep empathy"-ről és az AI-orvos munkamegosztásról **ma is releváns és inspiráló**.
- **Alvin Rajkomar et al.: "Machine Learning in Medicine"** (New England Journal of Medicine, 2019) — Az orvosi AI **legidézettebb áttekintő cikke**, amely tömören és érthetően foglalja össze az alapokat.
→ https://doi.org/10.1056/NEJMra1814259

### Mezőgazdaság és élelmiszertudomány

- **Akinola Habila Tanimu et al. (eds.): *Artificial Intelligence and Smart Agriculture*** (Springer, 2024) — Az AI precíziós mezőgazdasági alkalmazásainak átfogó bemutatása: drónos távérzékelés, talajmonitoring, hozambecslés.
- **Álvaro Barbero: *AI for Earth Observation*** (Wiley, 2024) — A műholdas és drónos adatok AI-alapú elemzése, **különösen releváns a magyar agrár-távérzékelési kutatásokhoz**.
- **OECD: *Digital Opportunities for Better Agricultural Policies*** (2019) — Szakpolitikai keretrendszer az adatvezérelt mezőgazdasághoz.
→ https://www.oecd.org/agriculture/topics/technology/

### Környezettudomány és ökológia

- **Gustau Camps-Valls et al.: *Deep Learning for the Earth Sciences*** (Wiley, 2021) — Lásd a C.1 részletes leírását. A földtudományi mélytanulás standard referenciája.
- **David Rolnick et al.: "Tackling Climate Change with Machine Learning"** (ACM Computing Surveys, 2022) — A klímaváltozás elleni küzdelemben alkalmazható ML-technikák **enciklopédikus áttekintése**: energiarendszerek, közlekedés, épületek, ipar, erdészet, mezőgazdaság.
→ https://www.climatechange.ai/
- **Markus Reichstein et al.: "Deep Learning and Process Understanding for Data-Driven Earth System Science"** (Nature, 2019) — Az adatvezérelt és fizikai modellek **integrálásának úttörő cikke**.
→ https://doi.org/10.1038/s41586-019-0912-1

### Mérnöki tudományok

- **Manu Mitra et al.: *Digital Twin: A Comprehensive Guide*** (Packt, 2024) — Lásd a C.1 részletes leírását. A digitális ikrek mérnöki alkalmazásainak kézikönyve.
- **National Academies: *Foundational Research Gaps and Future Directions for Digital Twins*** (2024) — A digitális ikrek kutatási irányainak legfrissebb áttekintése.
- **Karen Willcox et al.: "The Imperative of Physics-Based Modeling and Inverse Theory in Computational Science"** (Nature Computational Science, 2021) — A fizikailag konzisztens modellek fontosságáról az AI-korszakban. **Minden mérnöknek kötelező olvasmány.**

### Társadalomtudományok

- **Matthew Salganik: *Bit by Bit: Social Research in the Digital Age*** (Princeton University Press, 2018; open access) — A digitális korszak társadalomtudományi módszertanának **legjobb bevezetése**. Ingyenesen elérhető online.
→ https://www.bitbybitbook.com/
- **Dirk Hovy & Shannon Spruit: "The Social Impact of Natural Language Processing"** (ACL, 2016) — A nyelvi modellek társadalmi hatásairól szóló **úttörő tanulmány**, amely a torzítások és az igazságosság kérdéseit tárgyalja.
- **SAGE Handbook of AI in the Social Sciences** (megjelenés előtt, 2026) — Az AI társadalomtudományi alkalmazásainak átfogó kézikönyve.

### Kémia és anyagtudomány

- **Alpha M. Lee et al.: "Machine Learning for Molecular and Materials Science"** (Nature, 2018) — A gépi tanulás molekuláris és anyagtudományi alkalmazásainak **legidézettebb áttekintő cikke**.
→ https://doi.org/10.1038/s41586-018-0337-2
- **Google DeepMind: AlphaFold és GNoME** — Az AlphaFold fehérjeszerkezet-jóslásai és a GNoME anyagfelfedezési eredményei **a kémiai AI legjelentősebb áttörései**. Az adatbázisok szabadon elérhetők.
→ https://alphafold.ebi.ac.uk/
→ https://deepmind.google/discover/blog/millions-of-new-materials-discovered-with-deep-learning/
- **Weininger, D.: "SMILES, a Chemical Language"** (J. Chem. Inf. Comput. Sci., 1988) — A kémiai nyelvi modellek alapja: a SMILES-jelölés, amelyet az AI-modellek használnak molekulák reprezentálásához.

### Biológia és élettudomány

- **National Academies: *The Age of AI in Life Sciences*** (2025) — Lásd a C.2 részletes leírását.
- **Jumper, J. et al.: "Highly Accurate Protein Structure Prediction with AlphaFold"** (Nature, 2021) — Az AlphaFold eredeti közleménye, amely **megváltoztatta a strukturális biológiát**. A legfontosabb AI-tudományos áttörés a 2020-as években.
→ https://doi.org/10.1038/s41586-021-03819-2
- **Elana J. Fertig et al. (eds.): *Open-Source AI Cookbook for Life Sciences*** (előkészületben) — A nyílt forráskódú AI-eszközök élettudomány-beli alkalmazásainak gyakorlati útmutatója.

---

## Hogyan maradj naprakész?

Az AI-irodalom olyan gyorsan változik, hogy a hagyományos könyvek és cikkek mellett **aktív információkövetési stratégiára** van szükséged. Íme a javaslatunk:

1. **Heti 30 perc**: Nézd át az arXiv.org cs.AI és cs.CL kategóriáit, vagy használd a Semantic Scholar AI-ajánlórendszerét (https://www.semanticscholar.org/).
2. **RSS/hírlevél**: Iratkozz fel az alábbi hírlevelekre:
   - **The Batch** (DeepLearning.AI, Andrew Ng) → https://www.deeplearning.ai/the-batch/
   - **Import AI** (Jack Clark) → https://importai.substack.com/
   - **One Useful Thing** (Ethan Mollick) → https://www.oneusefulthing.org/
   - **AI Tidbits** (magyar válogatás) → keress rá a Substacken
3. **Konferenciák figyelése**: NeurIPS, ICML, ICLR, AAAI — az elfogadott cikkek listáit az OpenReview.net-en találod.
4. **Magyar események**: MI Koalíció konferenciák, NJSZT rendezvények, HUN-REN workshopok.
5. **Közösségi szűrés**: A Reddit r/MachineLearning és a Hugging Face blog a közösség által "előszűrt" tartalmakat kínál.

> **Tipp:** Használd magát az AI-t az AI-irodalom követésére! Állíts be egy RAG-alapú rendszert (lásd 9. fejezet), amely heti rendszerességgel összefoglalja a szakterületedhez releváns új publikációkat.

---

*Ez a forráslista 2026 márciusában frissült utoljára. A legfrissebb linkekért és ajánlásokért látogass el a könyv online kiegészítő oldalára.*
