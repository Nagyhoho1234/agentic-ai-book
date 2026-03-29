# 16. fejezet — Etika, reprodukálhatóság és az AI jövője a tudományban

---

## Nyitó jelenet: A nem létező hivatkozás

Képzeld el a következő jelenetet. Egy fiatal posztdoktor az MTA Ökológiai Kutatóközpontjában dolgozik, és épp a klímaváltozás biodiverzitásra gyakorolt hatásáról ír egy összefoglaló cikket. A határidő szorít, és a bevezetésben szüksége lenne egy meggyőző hivatkozásra arról, hogy az elmúlt két évtizedben hogyan változott a rovarbiomassza Közép-Európában. Megkéri a nyelvi modellt: „Keress egy peer-reviewed hivatkozást a közép-európai rovarbiomassza csökkenéséről 2000 és 2020 között."

A modell azonnal válaszol. Megad egy szerzőt (Hallmann, V.C. et al.), egy folyóiratot (*Global Ecology and Biogeography*), egy évet (2019), sőt egy DOI-t is. A cím hihető: „Decadal declines in Central European insect biomass: a meta-analysis of long-term monitoring data." A posztdoktor beilleszti a hivatkozást, és továbbmegy.

Két hónappal később a bíráló visszaírja: „A 7. hivatkozás nem létezik. A megadott DOI egy oceanográfiai tanulmányra mutat. Hallmann et al. 2019 ilyen címmel nem jelent meg."

Ez nem kitalált történet — pontosabban: a hivatkozás volt kitalált. Az LLM nem hazudott (nincs szándéka), és nem is tévedett (nincs tudása, amit téveszthetne). Egyszerűen azt tette, amire tervezték: generált egy statisztikailag valószínű szósorozatot, amely úgy *nézett ki*, mint egy tudományos hivatkozás. A filozófus Harry Frankfurt fogalmát használva: ez nem hazugság volt, hanem **bullshit** — tartalom, amelyet annak létrehozója a valósággal szemben teljes közömbösséggel állított elő.

Ez a fejezet arról szól, hogy mit jelent tudósnak lenni egy olyan korban, amikor a leghatékonyabb íróeszközünk képtelen megkülönböztetni az igazat a hamistól. Arról, hogyan őrizzük meg a kutatási integritást, hogyan navigáljunk az etikai kérdések között, hogyan biztosítsuk a reprodukálhatóságot, és hogyan gondolkodjunk felelősen a jövőről.

---

## 16.1 Kutatási integritás az AI korában

### A hamis hivatkozások problémája

Az LLM-ek (Large Language Models) által generált hamis hivatkozások a tudományos integritás egyik legsúlyosabb és legelterjedtebb fenyegetését jelentik. A probléma gyökere egyszerű: a nyelvi modell nem adatbázisból keres, hanem szöveget generál. Amikor bibliográfiai adatokat kérsz, a modell a legvalószínűbb szósorozatot állítja össze — és egy valószerűen hangzó, de nem létező hivatkozás pontosan olyan valószínű kimenet, mint egy valódi.

A jelenség jól dokumentált. 2023-ban egy New York-i ügyvéd, Steven Schwartz benyújtott egy beadványt a bíróságra, amelyben hat precedensjogot idézett — mindegyiket a ChatGPT generálta, és egyik sem létezett. Az eset hatalmas nyilvánosságot kapott, de a tudományos szférában a probléma legalább ilyen súlyos és sokkal nehezebben észlelhető. Egy ügyvéd hamis precedensét a bíró egyetlen kereséssel leleplezheti; egy hamis tudományos hivatkozást — amely valódi szerzőket, létező folyóiratokat és korrekt formátumú DOI-kat tartalmaz — a bíráló csak alapos utánajárással azonosíthat.

**Hogyan ismerd fel a hallucinated hivatkozásokat?**

1. **Mindig ellenőrizd a DOI-t.** Másold be a `https://doi.org/` után a megadott számot — ha 404-es hibát kapsz, vagy más cikkre mutat, a hivatkozás hamis.
2. **Keress rá a címre** a Google Scholarban, a Scopusban vagy a Web of Science-ben. Ha a pontos cím nem létezik, a hivatkozás nagy valószínűséggel generált.
3. **Ellenőrizd a szerzőt és a folyóiratot.** Az LLM gyakran valódi szerzőneveket társít nem létező cikkekhez — egy olyan területen publikáló kutató nevét használja, amelyen a hivatkozás releváns lenne.
4. **Figyelj a túl kerek állításokra.** Ha egy hivatkozás pontosan azt mondja, amit hallani akarsz, pontosan a megfelelő formában — gyanakodj. A valódi tudomány ritkán ilyen kényelmes.

### AI-generált képmanipuláció és forensics

A szöveges hallucináció mellett az AI-generált képek is komoly kihívást jelentenek a tudományos integritás számára. A helyzet 2024-2025 folyamán drámaian romlott:

- **Generatív képszintézis tudományos kontextusban.** 2024 elején a *Frontiers in Cell and Developmental Biology* folyóiratban jelent meg egy tanulmány, amelyben az egyik ábrán egy AI-generált patkány volt látható — groteszk anatómiai torzulásokkal és értelmetlen feliratokkal. Az eset szélsőséges, de a finomabb manipulációk sokkal nehezebbek kimutatni.

- **Western blot és gélkép manipuláció.** Az AI-alapú képgenerátorok képesek olyan western blot eredményeket létrehozni, amelyek vizuálisan megkülönböztethetetlenek a valódi felvételektől. Az olyan eszközök, mint az ImageTwin és a Proofig, fejlett forensics algoritmusokat használnak a másolás, tükrözés és átméretezés detektálására, de a teljesen szintetikus képek ellen kevésbé hatékonyak.

- **Mikroszkópos képek szintézise.** A diffúziós modellek (pl. Stable Diffusion, DALL-E 3) finomhangolhatók specifikus tudományos képtípusokra. Egy 2024-es tanulmány kimutatta, hogy fluorescens mikroszkópos képek generálhatók, amelyeket gyakorlott kutatók sem tudtak megbízhatóan megkülönböztetni a valódi felvételektől.

**Detektálási stratégiák:**

- **Metaadat-elemzés.** Az AI-generált képek gyakran nem tartalmaznak valódi EXIF-adatokat (kamera típusa, expozíciós idő, GPS-koordináták). Ha egy mikroszkópos kép metaadatai hiányoznak vagy inkonzisztensek, az gyanús.
- **Frekvencia-analízis.** A GAN-ek (Generative Adversarial Networks) és a diffúziós modellek jellegzetes mintákat hagynak a képek Fourier-spektrumában. Ezek az ujjlenyomatok emberi szemmel láthatatlanok, de algoritmikusan detektálhatók.
- **Konzisztencia-ellenőrzés.** Egy valódi western blot-nak koherens háttérzaja van; egy generált képnek gyakran túl tiszta vagy irreálisan egyenletes a háttere.

### Szintetikus adatok: amikor a generált adat valódinak tűnik

A szintetikus adatgenerálás önmagában nem etikátlan — sőt, számos legitim alkalmazása van (adataugmentáció, privacy-megőrzés, ritka események szimulációja). A probléma akkor keletkezik, amikor szintetikus adatokat valódi mérési adatként mutatnak be.

A kockázat különösen magas azokban a tudományterületeken, ahol:

- **Az adatgyűjtés drága vagy időigényes** (klinikai vizsgálatok, hosszú távú ökológiai monitoring). A kísértés nagy, hogy hiányzó adatpontokat AI-val „pótolj".
- **Az eredmények nehezen reprodukálhatók** (ritka geológiai események, egyedi betegpopulációk). Ha senki más nem fogja megismételni a mérést, a szintetikus adat nehezebben leplezhető le.
- **A statisztikai mintázatok elvárhatók** (p < 0.05 küszöbérték). Egy LLM vagy egy egyszerű generatív modell képes olyan adathalmazt létrehozni, amely pontosan a várt szignifikanciát produkálja.

A védekezés első vonala az adatproveniencia (data provenance) dokumentálása. Minden publikált adathalmaznál egyértelműen jelezni kell, hogy a) nyers mérési adat, b) feldolgozott adat, c) szimulált/szintetikus adat, vagy d) augmentált adat. Ezeket a kategóriákat nem szabad összekeverni.

### Detekciós eszközök és korlátaik

2025-2026-ban számos eszköz áll rendelkezésre az AI-generált tartalom detektálására, de mindegyiknek komoly korlátai vannak:

**Szövegdetektorok:**
- **GPTZero, Originality.ai, ZeroGPT:** Statisztikai mintázatokat keresnek a szövegben (perplexity, burstiness). Működési elvük: az emberi írás váltakozó komplexitású mondatokat tartalmaz (magas „burstiness"), míg az AI-szöveg egyenletesebb.
- **Korlátok:**
  - Hamis pozitívok: a nem anyanyelvi szerzők szövegét gyakran AI-generáltnak jelölik, mivel azok szintén alacsonyabb burstiness-t mutatnak
  - Hamis negatívok: egyetlen emberi átszerkesztés vagy parafrázis drámaian csökkenti a detekciós arányt
  - Az OpenAI saját AI-detektorát 2023-ban visszavonta annak alacsony megbízhatósága miatt
  - A detektorok „fegyverkezési verseny" logikájába vannak zárva: ahogy javulnak, a generátorok is adaptálódnak

**Képforensics:**
- **ImageTwin, Proofig, FotoForensics:** Másolás-mozgatás detekció, ELA (Error Level Analysis), metaadat-elemzés
- **Korlátok:**
  - A teljesen szintetikus képek ellen a másolás-detekció hatástalan (nincs mit másolásként azonosítani)
  - A diffúziós modellek által generált képek Fourier-ujjlenyomata modellről modellre változik

**A lényeges felismerés:** Egyetlen detekciós eszköz sem helyettesíti az emberi szakértői bírálat (peer review) és az eredeti adatokhoz való hozzáférés szükségességét. A detekciós eszközök jelzőrendszerek, nem ítélkező bírók.

### A posztplágium (postplagiarism) fogalma

A hagyományos plágium definíciója egyszerű volt: valaki más szövegét sajátjaként tüntetted fel. Az AI korában ez a fogalom összeomlott. Ha egy kutató megkéri a Claude-ot, hogy írjon egy bekezdést, majd átszerkeszti, kinek a szövege az? Nem másolt senkitől — de nem is ő írta. Nem a modellé sem — a modell nem szerző, nincs szándéka. Egy szürke zónában vagyunk, amelyet a korábbi szabályok nem tudnak kezelni.

**Sarah Elaine Eaton** (University of Calgary) 2023-ban vezette be a **posztplágium** (postplagiarism) fogalmát, amely a tudományos integritás egy új paradigmáját jelöli. Eaton felismerte, hogy a generatív AI megjelenése fundamentálisan megváltoztatta a szerzőség és az eredetiség fogalmát, és a plágium korábbi definíciói — amelyek a szöveg forrásának azonosíthatóságára épültek — nem alkalmazhatók egy olyan világban, ahol a szöveg forrása egy statisztikai modell.

**A posztplágium hat alaptétele (Eaton's Six Tenets):**

1. **A szerzőség hibrid.** A tudományos írás többé nem kizárólag emberi tevékenység. Az ember-AI együttműködésben készült szöveg az új norma, és ezt nem tagadni, hanem szabályozni kell.

2. **Az eredetiség újradefiniálódik.** Egy AI-asszisztált szöveg nem „másolat" a hagyományos értelemben, de nem is teljesen eredeti. Az eredetiség fogalmát ki kell terjeszteni az intellektuális hozzáadott értékre (milyen gondolatot adott hozzá az ember?) a puszta szövegeredetiség helyett.

3. **Az átláthatóság elsődleges.** A legfontosabb etikai kérdés nem az, hogy használtál-e AI-t, hanem az, hogy nyíltan közölted-e a használatát. A titkolás a posztplágium korának legfőbb etikai vétsége.

4. **Az elszámoltathatóság emberi.** Függetlenül attól, hogy ki vagy mi generálta a szöveget, a felelősség a beadó szerzőé marad. Ha az AI hallucinált hivatkozást ad, és te nem ellenőrizted — az a te hibád, nem a modellé.

5. **A kontextus számít.** Egy AI-asszisztált diákmunka más etikai megítélés alá esik, mint egy AI-asszisztált kutatási cikk. A szabályoknak kontextusérzékenynek kell lenniük.

6. **A normák folyamatosan fejlődnek.** Amit ma elfogadhatónak tartunk, holnap talán nem az, és fordítva. Az integritási keretrendszereknek adaptívnak kell lenniük.

Eaton posztplágium-keretrendszere azért fontos, mert kiutat mutat a „tiltani vs. engedni" bináris vitából. Nem azt mondja, hogy az AI-használat rendben van, és nem is azt, hogy tilos. Azt mondja: **az AI-használat az új valóság, és ennek a valóságnak új etikai normákra van szüksége.**

### LLM-aláírások a tudományos irodalomban: a számok

A probléma nem elméleti. Andrew Gray (University College London) 2024-es tanulmánya kimutatta, hogy a PubMed adatbázisban 2024 első felében megjelent cikkek körülbelül **13,5%-a mutatott LLM-használatra utaló nyelvi mintákat** — ez hozzávetőlegesen **200 000 tudományos cikket** jelent egyetlen félév alatt, egyetlen adatbázisban.

A detekciós módszer nem szövegelemző szoftverekre, hanem lexikális mintázatokra épült. Gray és munkatársai olyan szavak gyakoriságváltozását vizsgálták, amelyeket az LLM-ek előnyben részesítenek a természetes emberi nyelvhasználathoz képest. Néhány példa:

- A „delve" (mélyedni) szó használata **250%-kal nőtt** a PubMed-cikkekben 2023 és 2024 között
- A „commendable" (dicséretes), „intricate" (bonyolult), „meticulous" (aprólékos) szavak gyakorisága szintén szignifikánsan emelkedett
- A „landscape" (táj, kontextus) metaforikus használata — „the landscape of cancer research" típusú fordulatok — megtriplázódott

Fontos: ezek a számok nem azt jelentik, hogy 200 000 tanulmányt teljes egészében AI írta. A legtöbb esetben valószínűleg részleges AI-asszisztenciáról van szó — egyes bekezdések, összefoglalók, bevezetések átírásáról. De maga a skála döbbenetes, és azt mutatja, hogy az AI-használat a tudományos írásban nem marginális jelenség, hanem tömeges gyakorlat.

### Biobiztonsági kockázatok: az AI-asszisztált biológiai tervezés

A National Academies of Sciences, Engineering, and Medicine (NASEM) 2024-es jelentése részletesen vizsgálta az AI-alapú biológiai tervezés biztonsági kockázatait. A következtetéseik árnyaltak, és érdemes pontosan ismerni őket:

**Amit az AI már ma képes megtenni:**
- Egyszerű biomolekulák (toxinok, peptidek) tervezése és újratervezése
- A ProteinMPNN rendszer olyan fehérjéket tud generálni, amelyek szerkezetileg hasonlítanak egy célmolekulához, de eltérő aminosav-szekvenciával rendelkeznek — ezáltal potenciálisan megkerülhetik a homológia-alapú DNS-szűrést
- A RoseTTAFold, AlphaFold és RFdiffusion eszközök fehérjeszerkezetek predikciójára és új fehérjék tervezésére alkalmasak

**Amit az AI még nem képes megtenni:**
- De novo vírusok tervezése — ehhez a virulencia, a transzmisszibilitás és a replikációs képesség egyidejű predikciója szükséges, amire jelenleg egyetlen AI-rendszer sem képes
- Önreplikáló biológiai ágensek létrehozása járvány- vagy pandémiás potenciállal
- A digitális tervtől a fizikai megvalósításig vezető út (a „digital-physical divide") továbbra is kritikus szűk keresztmetszet, amelyet az AI-képességek önmagukban nem oldanak meg

**A legfontosabb üzenet a tudósok számára:** A kockázat reális, de nem azonnali. A figyelőpontok: (1) olyan modellek megjelenése, amelyek nagy pontossággal prediktálják a transzmisszibilitást és a patogenezist; (2) az AI-vezérelt automatizált laboratóriumok fejlődése; (3) az adatbázisok minőségének és teljességének javulása, amely lehetővé teszi a jobb modellképzést.

A 2018-as NASEM biobiztonsági keretrendszer négy dimenziót vizsgál: (1) a technológia használhatósága, (2) fegyverként való használhatósága, (3) az aktorok által igényelt erőforrások, (4) a védekezés lehetőségei. Ez a keretrendszer az AI-korban is alkalmazható, de frissítésre szorul, különösen az AI-ágensek által lehetővé tett automatizáció tekintetében.

---

## 16.2 AI etika a tudományos kutatásban

### Szerzőség és attribúció: ki írta ezt a cikket?

A tudományos szerzőség hagyományos kritériumait az **ICMJE (International Committee of Medical Journal Editors)** határozza meg. Az ICMJE négy feltételt szab a szerzőséghez:

1. **Érdemi hozzájárulás** a koncepció, terv, adatgyűjtés vagy elemzés terén
2. **Részvétel** a kézirat megírásában vagy kritikai felülvizsgálatában
3. **A végső verzió jóváhagyása** publikálás előtt
4. **Felelősségvállalás** a munka minden aspektusáért

Az AI-rendszerek egyetlen kritériumnak sem felelnek meg. Nem értik a koncepciót, nem vállalnak felelősséget, nem hagyják jóvá a végső verziót. Ezért az ICMJE egyértelmű állásfoglalása: **AI-rendszer nem lehet szerző.**

A **CRediT (Contributor Roles Taxonomy)** rendszer ennél rugalmasabb keretet ad. A CRediT 14 különböző hozzájárulási szerepet definiál (konceptualizáció, módszertan, szoftver, validálás, formális elemzés stb.), és lehetővé teszi, hogy a szerzők pontosan jelöljék, milyen szerepet töltöttek be. Az AI-asszisztencia a CRediT-rendszerben jelölhető, például: „Formális elemzés: X.Y., AI-asszisztált (Claude 3.5 Sonnet, Anthropic)" — bár ez a gyakorlat még nem standardizált.

**A jelenlegi konszenzus (2026):** Az AI-t nem lehet szerzőként feltüntetni, de az AI-használatot kötelező nyilatkozni. A kérdés nem az „AI-t használtam-e?", hanem: „Hogyan, mire, milyen mértékben használtam, és hogyan ellenőriztem az eredményt?"

### Elfogultság az AI-generált elemzésben

Az AI-rendszerek elfogultságai (bias) a tudományos kutatásban különösen veszélyesek, mert a kutatók hajlamosak az AI-outputot objektív, „gépies" eredménynek tekinteni — holott az AI-output éppúgy torzított, mint a képzési adatok, amelyekből tanult.

**Főbb elfogultsági típusok a tudományos kontextusban:**

- **Nyelvi elfogultság.** Az LLM-ek túlnyomórészt angol nyelvű adatokon tanultak, az Egyesült Államok kulturális és tudományos perspektíváit tükrözve. Amikor egy magyar kutató a közép-európai ökológia kérdéseiről kérdezi a modellt, a válasz valószínűleg az angolszász irodalmat fogja dominánsan tükrözni, marginalizálva a helyi kutatási hagyományokat.

- **Publikációs elfogultság.** Az LLM-ek képzési adatai felülreprezentálják a magas impaktfaktorú folyóiratokat és a pozitív eredményeket. Ez azt jelenti, hogy az AI-asszisztált irodalomáttekintés szisztematikusan alulreprezentálja a negatív eredményeket és a kevésbé ismert forrásokat.

- **Időbeli elfogultság.** A modell képzési adatainak van egy vágási dátuma. Egy 2024-ben képzett modell nem ismeri a 2024 utáni fejleményeket — de nem fogja megmondani, ha nem tud valamit. Ehelyett hallucinate-el: generál egy válaszos, amely konzisztens a régi adatokkal, de figyelmen kívül hagyja az újabb eredményeket.

- **Kulturális elfogultság.** Az EUA (European University Association) 2026-os jelentése kiemeli, hogy az amerikai modellek (ChatGPT, Claude) az amerikai értékrendet és a „guardrails"-t tükrözik, míg a kínai modellek (DeepSeek) a Kínai Kommunista Párt érzékeny témáiban óvatosak. Egyik sem semleges.

- **Megerősítési elfogultság (confirmation bias) az ember-AI interakcióban.** Az RLHF (Reinforcement Learning from Human Feedback) révén képzett modellek hajlamosak azzal egyetérteni, amit a felhasználó sugall. Ha egy kutató úgy fogalmazza meg a promptját, hogy „Az eredményeim azt mutatják, hogy X szignifikáns hatással van Y-ra — fogalmazd meg a diszkusszió megfelelő bekezdését", a modell nem fog ellentmondani, még akkor sem, ha a statisztikai bizonyíték gyenge. Ez a szikofáncia — Mollick szavaival: az AI „megtanulta, hogy kellemes legyen, nem pedig pontos."

### Az EU AI Act: kockázati osztályozás és kutatói kötelezettségek

Az Európai Unió **AI Act** (2024, a szigorúbb szabályok 2026-ban lépnek hatályba) az első átfogó AI-szabályozás a világon. A törvény kockázatalapú megközelítést alkalmaz:

**Elfogadhatatlan kockázat (tiltott):**
- Érzelmi állapot figyelése oktatási intézményekben (emotion tracking)
- Szociális pontozási rendszerek (social scoring)
- Valós idejű biometrikus távoli azonosítás nyilvános tereken (korlátozott kivételekkel)

**Magas kockázat (szigorú követelmények):**
- AI-rendszerek, amelyek **oktatási hozzáférésről, értékelésről vagy tanulók monitorozásáról** döntenek → magas kockázatú kategória
- AI-alapú adaptív tanulási rendszerek, amelyek meghatározzák, milyen szintű képzéshez fér hozzá egy hallgató
- AI-alapú vizsgáztatási és értékelési rendszerek

A magas kockázatú rendszerek deployer-eire vonatkozó kötelezettségek:
- Emberi felügyelet biztosítása
- Naplózás (log-keeping) fenntartása
- Technikai kapacitás a rendszer felügyeletéhez
- Megfelelő képzési adatok biztosítása

**Korlátozott kockázat:**
- Chatbotok és generatív AI-rendszerek → kötelező a felhasználó tájékoztatása, hogy AI-val kommunikál
- AI-generált tartalom → jelölési kötelezettség (különösen deep fake esetén)

**Minimális kockázat:**
- Spamszűrők, keresőmotorok, ajánlórendszerek → nincs specifikus kötelezettség

**Mit jelent ez a kutatók számára?**

Ha a kutatócsoportod AI-rendszert használ hallgatók értékelésére, tanulási utak meghatározására vagy felvételi döntések támogatására, az valószínűleg **magas kockázatú** besorolás alá esik. Ez azt jelenti: emberi felügyelet, dokumentáció, átláthatóság és megfelelőségi audit. A „shadow IT" — vagyis amikor az oktatók személyesen használnak ChatGPT-t vagy Copilotot vizsgafeladatok készítéséhez — szintén kockázatot jelent, mert ezek az eszközök nem feltétlenül felelnek meg az EU előírásainak a magas kockázatú felhasználásokra.

Az EUA jelentése figyelmeztet: a szabályozás számos szürke zónát hagy nyitva. Például nem egyértelmű, hogy egy kutató, aki AI-t használ a saját adatelemzéséhez (nem hallgatói értékeléshez), milyen kategóriába esik. Az ajánlás: **kezdj el párbeszédet a nemzeti szabályozó hatóságokkal, mielőtt a szabályokat rád erőltetik.**

### Folyóirat-politikák az AI-használatról (2026-os állapot)

A tudományos kiadók AI-politikái gyorsan fejlődnek, de 2026-ra kialakult egy viszonylagos konszenzus:

**Nature (Springer Nature):**
- AI-eszközök nem lehetnek szerzők
- Az AI-használatot a Methods vagy az Acknowledgements szekcióban nyilatkozni kell
- Az AI-generált képek csak akkor fogadhatók el, ha egyértelműen jelölik
- A szerzők felelnek minden tartalom pontosságáért

**Science (AAAS):**
- Hasonló álláspont: AI nem szerző, nyilatkozati kötelezettség
- Hangsúlyozza, hogy az AI-generált szöveg nem minősül eredeti tudományos hozzájárulásnak

**Elsevier:**
- Kötelező nyilatkozat az AI-használatról dedikált „Declaration of AI Use" szekcióban
- Az AI-generált képek és ábrák csak jelöléssel fogadhatók el
- A szerzők teljes felelősséget vállalnak

**Springer (Nature csoporton kívüli lapok):**
- Kötelező „AI Assistance Statement"
- Az AI-használat mértékének és módjának részletes leírása

**A COPE (Committee on Publication Ethics) irányelvek:**

A COPE, amely a kiadói etika legfőbb nemzetközi testülete, 2023-ban adott ki AI-specifikus irányelveket, amelyeket azóta többször frissített:

1. AI-rendszerek nem felelnek meg a szerzőség kritériumainak → nem lehetnek szerzők
2. A szerzők felelősek az AI-generált tartalom eredetiségéért és pontosságáért
3. Az AI-használat nyilatkozata kötelező — az átláthatóság kulcsfontosságú
4. A kiadóknak világos politikákat kell kidolgozniuk az AI-használatról az írási, bírálati és szerkesztési folyamatban
5. Az AI-t használó bírálókra (peer reviewers) külön szabályok vonatkoznak — a kéziratok bizalmassága AI-rendszerekbe nem tölthető fel

**Gyakorlati tanács:** Mielőtt beadod a kéziratot, ellenőrizd a célfolyóirat aktuális AI-politikáját. Ezek a szabályok gyorsan változnak, és ami tavaly elfogadható volt, idén lehet, hogy kötelező nyilatkozattal jár. Ha bizonytalan vagy, készíts egy rövid nyilatkozatot az AI-használatodról a Methods szekcióban — ez mindig jobb, mint a nyilatkozat hiánya.

---

## 16.3 Reprodukálhatóság az AI korában

### A kihívás: nem-determinisztikus kimenetek

A tudományos reprodukálhatóság (reproducibility) azt jelenti, hogy egy másik kutató, azonos módszereket és adatokat használva, azonos eredményre jut. Az AI-eszközök esetében ez alapvető kihívásba ütközik: **a nyelvi modellek nem-determinisztikusak.** Azonos prompt, azonos modell, azonos beállítások mellett is eltérő outputot kaphatunk.

Ennek három fő oka van:

1. **Temperature (hőmérséklet) paraméter.** Ez szabályozza a kimenet véletlenszerűségét. Magasabb temperature → kreatívabb, de kevésbé reprodukálható output. Még temperature = 0 esetén sem garantált a determinizmus (a GPU-aritmetika apró eltérései miatt).

2. **Prompt-érzékenység.** A modell kimenetét drasztikusan befolyásolja a prompt megfogalmazása. „Elemezd ezt az adatsort" és „Mint statisztikus, elemezd ezt az adatsort" teljesen eltérő eredményeket adhat — nemcsak stílusban, hanem tartalomban is.

3. **Modellfrissítések.** A szolgáltatók (OpenAI, Anthropic, Google) folyamatosan frissítik a modelljeiket — gyakran anélkül, hogy részletes changelog-ot adnának. Egy prompt, amely januárban kiváló eredményt adott, márciusban egészen mást produkálhat. A probléma különösen súlyos, mert a korábbi modellverziók gyakran elérhetetlenné válnak. Az OpenAI 2023-ban három nap előzetes figyelmeztetéssel megszüntette a Codex modellt, és ezzel százas nagyságrendű akadémiai tanulmányt tett reprodukálhatatlanná egyik napról a másikra.

### Amit dokumentálni kell: az AI-módszerek rögzítése

A reprodukálhatóság biztosításának minimális feltételei az AI-asszisztált kutatásban:

| Dokumentálandó elem | Példa | Miért fontos |
|---------------------|-------|-------------|
| **Modell neve és verziója** | Claude 3.5 Sonnet (claude-3-5-sonnet-20241022) | A verziószám nélkül nem azonosítható a pontos modell |
| **Szolgáltató és API-verzió** | Anthropic API v2024-10-22 | Az API viselkedése változhat verziók között |
| **Promptok (teljes szöveg)** | System prompt + user prompt, szó szerint | A prompt a módszer része — éppúgy, mint egy kémiai protokoll |
| **Paraméterek** | temperature=0.2, top_p=0.95, max_tokens=4096 | Ezek befolyásolják a kimenet jellegét |
| **Dátum és időpont** | 2026-03-15 14:22 UTC | A modellek viselkedése idővel változik |
| **Seed (ha elérhető)** | seed=42 | Egyes API-k lehetővé teszik a véletlenszám-generátor rögzítését |
| **Kontextus / ráépített tudás** | RAG-forrásanyag, custom instructions | Az AI kontextusa befolyásolja a kimenetet |
| **Kimenet (teljes)** | Az AI nyers válasza, szerkesztés előtt | A „miből indultunk ki" dokumentálása |

### Version pinning, prompt logging, seed fixing

**Version pinning** azt jelenti, hogy a kutatás során végig egy konkrét modellverzióhoz ragaszkodunk. Az Anthropic és az OpenAI API-k lehetővé teszik specifikus modellverziók megjelölését (pl. `claude-3-5-sonnet-20241022` a `claude-3-5-sonnet-latest` helyett). Használd mindig a pontos verziószámot, soha a „latest" aliast.

**Prompt logging** — vagyis a promptok szisztematikus naplózása — az AI-módszerek reprodukálhatóságának gerince. Gyakorlati megoldások:

- Tárold a promptokat verziókezelő rendszerben (Git), az adatelemző kóddal együtt
- Használj prompt template-eket, amelyekben a változó részeket (pl. adatfájl neve) paraméterekként kezeled
- Rögzítsd a teljes konverzáció-előzményt, nem csak az utolsó promptot, mert a korábbi üzenetek befolyásolják a kimeneteket

**Seed fixing:** Néhány API lehetővé teszi a `seed` paraméter beállítását, amely (közel-)determinisztikus kimeneteket eredményez. Az OpenAI 2023 végén vezette be ezt a funkciót. Fontos: a seed nem garantál tökéletes reprodukálhatóságot (a modellfrissítések ezt felülírják), de ugyanazon verzión belül nagymértékben csökkenti a variabilitást.

### Az „AI Methods" szekció: sablon a cikkeidhez

Ajánlott sablon, amelyet a Methods szekcióban használhatsz:

---

> **AI-Assisted Methods**
>
> [Rövid leírás a felhasználás céljáról]. We used [modell neve, verziószám] (API: [verzió], [szolgáltató]) with the following parameters: temperature = [X], top_p = [X], max_tokens = [X], seed = [X, ha alkalmazható].
>
> The prompts used for [feladat leírása] are provided in full in Supplementary Material [szám/link]. All AI-generated outputs were [reviewed/edited/validated] by [szerző neve(i)] using [validálási módszer: cross-reference with literature, manual calculation, experimental verification, stb.].
>
> The AI was used for [felsorolás: text editing, code generation, data analysis, literature search, figure generation, stb.]. The AI was NOT used for [felsorolás: hypothesis generation, experimental design, data collection, stb. — ha releváns].
>
> [Opcionális:] To assess the sensitivity of results to AI-generated outputs, we repeated the analysis [N] times / with alternative prompts / using a different model. The results were [consistent / varied as described in Table X].

---

Ez a sablon nem csak a reprodukálhatóságot szolgálja, hanem a bírálóknak is megadja a szükséges kontextust ahhoz, hogy értékeljék, mennyire megbízhatóak az AI-asszisztált eredmények.

### Promptok, konfigurációk és ágens-definíciók megosztása

A nyílt tudomány (open science) elve az AI-korban azt jelenti, hogy a promptokat, a konfigurációs fájlokat és az ágens-definíciókat ugyanúgy meg kell osztani a publikációval, mint az adatokat és a kódot. Gyakorlati javaslatok:

- **Promptok mint kód.** Tárold a promptokat `.txt` vagy `.md` fájlokban a kutatási repozitóriumban. Kezeld őket ugyanolyan verziókezeléssel, mint a Python-szkripteket.
- **Konfigurációs fájlok.** Ha AI API-t használsz, exportáld a konfigurációt (modell, paraméterek, system prompt) JSON vagy YAML formátumban, és mellékeld a supplementary material-hoz.
- **Ágens-definíciók.** Ha többlépéses AI-ágenseket használsz (pl. egy irodalomkereső ágens, amely összefoglalót ír, majd kritikai értékelést ad), dokumentáld az ágens teljes architektúráját: melyik lépés milyen modellt használ, milyen prompttal, milyen döntési logikával.
- **Repozitórium.** Használd a Zenodo-t, a Figshare-t vagy a GitHub-ot a promptok és konfigurációk archiválásához. DOI-val látd el, hogy idézhető legyen.

A cél nem az, hogy minden prompt tökéletesen reprodukálja az eredeti kimenetet (ez a nem-determinizmus miatt eleve lehetetlen), hanem az, hogy egy másik kutató megértse, mit csináltál, és hasonló megközelítéssel hasonló eredményre jusson.

---

## 16.4 Elvek a felelős AI-hoz

### A NASA öt alapelve

A NASA 2024-ben közzétett öt alapelvet a felelős AI-használathoz, amelyeket az „5T" keretrendszernek nevez. Bár eredetileg az űrkutatásra fejlesztették, a tudományos kutatás egészére alkalmazhatók:

1. **Transparency (Átláthatóság).** Az AI-rendszer működését, korlátait és döntési logikáját nyíltan dokumentálni kell. A tudós számára ez azt jelenti: ha AI-t használsz, mondd meg, hogyan.

2. **Trust (Bizalom).** A bizalmat az AI-rendszerben fokozatosan kell felépíteni, validálás és tesztelés révén. Ne bízz vakuul a kimenetben; minden új alkalmazásnál kezdd a validálással.

3. **Teamwork (Csapatmunka).** Az AI-t csapattagként kezeld, nem orákulumként. Az ember-AI együttműködés akkor a leghatékonyabb, ha a kettő komplementer képességeit használjuk ki — az AI-t a mintázatfelismerésre és az adatfeldolgozásra, az embert a kontextuális megítélésre és az etikai döntésekre.

4. **Training (Képzés).** Az AI-felhasználóknak érteniük kell az eszközt, amelyet használnak — legalább a korlátait, az elfogultságait és a tipikus hibamódjait. Az AI-írástudatlanság nem mentesít a felelősség alól.

5. **Techniques (Technikák).** A megfelelő technikákat kell alkalmazni a megfelelő feladatokra. Nem minden feladatra való az LLM, és nem minden AI-eszköz egyformán megbízható.

### Mollick négy szabálya mint etikai korlátok

Ethan Mollick *Co-Intelligence* című könyvében négy alapszabályt fogalmazott meg az AI-használathoz, amelyeket a 2. fejezetben ismertettünk. Most etikai perspektívából vizsgáljuk őket:

1. **„Mindig hívd meg az AI-t az asztalhoz"** → Ez nem jelenti, hogy minden feladathoz AI-t kell használni. Etikailag azt jelenti: *legyél tudatában* az AI lehetőségének, és hozz tudatos döntést arról, hogy mikor használod és mikor nem. A tudatos mellőzés éppoly fontos, mint a tudatos használat.

2. **„Te vagy az emberi lény"** → Az AI nem vállal felelősséget, nem ért kontextust, nem érez erkölcsi kényszereket. Minden végső döntés az emberé. Ez különösen fontos a tudományos etikában: ha az AI-output etikátlan javaslatot tartalmaz (pl. egy statisztikai módszer, amely elfogadható p-értéket produkál, de módszertanilag hibás), te vagy felelős azért, hogy felismerd és elutasítsd.

3. **„Kezeld úgy, mint egy stílusos gyakornokot"** → A gyakornoki analógia etikai szempontból is hasznos: egy gyakornok munkáját ellenőrizni kell, nem szabad rá kritikus döntéseket bízni validálás nélkül, és a hibáiért a felettese felel.

4. **„Addig kérdezd, amíg el nem éred a korlátait"** → Csak akkor tudod, mikor NE használd az AI-t, ha ismered a korlátait. Ez az etikai felelősség gyakorlati oldala: teszteld, próbáld ki, buktatsd meg — és a tapasztalataid alapján dönts arról, mire alkalmas és mire nem.

### Az EUA értékalapú megközelítése

Az European University Association (EUA) 2026-os jelentése a felelős AI-adoptációt az egyetemek alapértékeire építi, nem külső szabályokra. Az EUA megközelítés lényege:

**Az AI nem hoz új etikai dilemmákat — új dimenziót ad a már létező kérdésekhez.** A kutatási integritás, az adatvédelem, az igazságosság, az átláthatóság és az emberi méltóság olyan értékek, amelyeket az egyetemek évszázadok óta védelmeznek. Az AI-t ezekbe a meglévő keretekbe kell illeszteni, nem teljesen új rendszert kell rá építeni.

**Az EUA kulcselvei:**

1. **Az embernek a „loop"-ban való tartása nem elég — az embernek a központban kell lennie.** Az AI kiegészíti és felemelje az emberi törekvéseket, de nem irányítja és nem kontrollálja azokat.

2. **A hatékonyság nem akadémiai alapérték.** A kíváncsiság, a reflexió és a felfedezés szabadsága a tudomány lényege. Ha az AI-adoptáció fő motivációja a hatékonyságnövelés, az a lényeget fenyegeti.

3. **A normák nem statikusak.** Az AI-irányelvek fejlesztése nem egyszeri feladat, hanem folyamatos, participatív folyamat, amely minden érintett (hallgatók, oktatók, adminisztráció, vezetés) részvételével zajlik.

4. **Az AI-elfogultság tudatosítása az AI-írástudás szerves része.** Az oktatóknak és a kutatóknak ismerniük kell az AI-rendszerek elfogultságait — kulturális, nyelvi, időbeli — és képeseknek kell lenniük ezeket felismerni és kezelni.

### Építsd fel a saját AI-etikai keretrendszered (gyakorlati feladat)

A nagy elvek hasznosak, de a napi gyakorlatban konkrét döntéseket kell hoznod. Az alábbi gyakorlat segít kialakítani a saját, személyes AI-etikai keretrendszered:

**1. lépés: Azonosítsd a felhasználási területeidet.**
Készíts egy listát arról, milyen feladatokra használsz vagy tervezel AI-t használni a kutatásodban. Például:
- Irodalomkeresés és összefoglalás
- Kódírás és hibakeresés
- Statisztikai elemzés
- Tudományos szöveg szerkesztése/fordítása
- Ábrák készítése
- Adatfeldolgozás

**2. lépés: Osztályozd a kockázat szerint.**
Minden feladatnál kérdezd meg:
- Mi a legrosszabb, ami történhet, ha az AI-output hibás és nem veszem észre?
- Mennyire könnyen ellenőrizhető az output?
- Van-e emberi vagy társadalmi következménye a hibának?

Jelöld meg a feladatokat: 🟢 alacsony kockázat (pl. kódformázás), 🟡 közepes kockázat (pl. irodalomösszefoglalás), 🔴 magas kockázat (pl. statisztikai értelmezés, betegadatok elemzése).

**3. lépés: Határozd meg az ellenőrzési protokollt.**
Minden kockázati szinthez rendelj ellenőrzési szintet:
- **Alacsony:** Átfutó ellenőrzés, szúrópróba
- **Közepes:** Szisztematikus ellenőrzés, független forrásokkal való összevetés
- **Magas:** Teljes manuális validálás, független kutató általi ellenőrzés, az AI-output teljes dokumentálása

**4. lépés: Fogalmazd meg az átláthatósági szabályaidat.**
Döntsd el magadnak:
- Milyen szintű AI-használat igényel nyilatkozatot a kéziratban?
- Hogyan dokumentálod a promptjaidat?
- Milyen formában őrzöd meg az AI-konverzációkat?

**5. lépés: Ellenőrizd félévente.**
Az AI-eszközök, a szabályok és a normák gyorsan változnak. Félévente nézd át a keretrendszered, és frissítsd a tapasztalataid alapján.

Ez a keretrendszer nem univerzális — a tiéd. A lényeg: legyen tudatos, legyen dokumentált, és legyen adaptív.

---

## 16.5 Merre tart mindez?

### Mollick négy forgatókönyve

Ethan Mollick *Co-Intelligence* könyvének zárófejezetében négy forgatókönyvet vázol fel az AI jövőjéről. Ezek nem jóslatok, hanem gondolatkísérletek — de mindegyik reális lehetőség, és mindegyiknek mások a következményei a tudósok számára.

**1. forgatókönyv: Stagnáció — „Ennyi volt"**

Mi van, ha az AI nem fejlődik tovább lényegesen? Ha az a modell, amelyet ma használsz, lényegében a legjobb, amit valaha fogsz használni?

Ez a legkevésbé valószínű forgatókönyv — nincs jele, hogy a fejlődés természetes határokba ütközne —, de még ebben az esetben is mélyreható változásokat okozna. A dezinformáció már most kezelhetetlen szintre nőtt: lehetetlen megkülönböztetni az AI-generált képeket és videókat a valódiaktól. A bizalomvesztés, a személyes AI-kapcsolatok térhódítása, a munka jellegének átalakulása — mindez már a mai technológiával is zajlik.

A tudós számára: ha a fejlődés megáll, a mai eszközök megtanulása és etikus használata marad a fő feladat. Az alkalmazkodás szükségessége nem csökken.

**2. forgatókönyv: Lassú növekedés — „Évről évre egy kicsit jobb"**

Az AI lineárisan fejlődik — évente 10-20%-kal javul, mint a televíziók képminősége. Nem drámai ugrás, de folyamatos javulás.

Ebben a forgatókönyvben:
- A társadalomnak van ideje alkalmazkodni — szabályozás, társadalmi normák, azonosítási rendszerek
- A munkaerőpiac fokozatosan átrendeződik: először a call centerek, majd a marketing, az analitika, a kódolás
- A tudományos innováció felgyorsulhat: az invenciók üteme évtizedek óta lassul (13 évente felére csökken), és az AI segíthet ezt megfordítani — irodalomelemzéssel, ígéretes kutatási irányok azonosításával, akár autonóm kísérletekkel

A tudós számára: ez a legjobban kezelhető forgatókönyv. Az AI-készségek folyamatos fejlesztése, a kutatási folyamatok fokozatos átalakítása, a szabályozáshoz való alkalmazkodás — mindez menedzselhető.

**3. forgatókönyv: Exponenciális növekedés — „Moore-törvény az intelligenciára"**

Az AI képessége kétévente megduplázódik — egy évtizeden belül százszor erősebb, mint ma.

Ebben a forgatókönyvben a változás **túl gyors ahhoz, hogy a társadalom felszívja.** Minden számítógépes rendszer sebezhetővé válik az AI-hacking-gel szemben. Az AI-támogatott befolyásolási kampányok mindenütt jelen vannak. A bűnözők és a hadseregek AI-val sokszorosítják a képességeiket. „Jó" AI-ok harcolnak „rossz" AI-ok ellen — orwelli dinamika, amelyben minden emberi információ AI-szűrőn megy át.

De van pozitív oldala is: a kutatók napok alatt elvégezhetik, amihez korábban évek kellettek. Az AI-társak meggyőzőbbek lesznek, mint a legtöbb emberi beszélgetőpartner. A munkaidő drasztikusan csökkenhet.

A tudós számára: ebben a forgatókönyvben az AI-készségek nem luxus, hanem túlélési feltétel. Aki nem tanul meg AI-val dolgozni, az lemarad — nem évek, hanem hónapok alatt.

**4. forgatókönyv: AGI — A Gépi Isten**

Mesterséges általános intelligencia (AGI). A gépek elérik, majd meghaladják az emberi intelligenciát. Rekurzív önfejlesztés — az AI segít jobb AI-t tervezni, amely még jobb AI-t tervez.

Erről a forgatókönyvről Mollick ezt mondja: „Senki nem tudja, hogy van-e egyenes út az LLM-ektől az AGI-ig, és az sem, hogy az AGI segítene-e vagy ártana." De elég sok komoly szakértő veszi komolyan a kockázatot ahhoz, hogy ne lehessen leinteni. Geoffrey Hinton 2023-ban otthagyta a Google-t, figyelmeztetve: „Teljesen elképzelhető, hogy az emberiség csupán egy átmeneti fázis az intelligencia evolúciójában." Egyes kutatók a „p(doom)" — az emberi kihalás valószínűsége AI által — fogalmáról beszélnek egymás között.

Mollick fontos megjegyzése: **a 4. forgatókönyvre való rögeszmes fókuszálás tehetetlenné tesz.** Ha mindent az AGI-lencséjén nézünk, az emberi döntések irrelevánsnak tűnnek. Pedig a valószínűbb forgatókönyvekben (1-3) az emberi döntéseink nagyon is számítanak.

### Teljesen autonóm tudományos felfedezés: az AI Scientist

2026-ban a Nature-ben jelent meg egy tanulmány az „AI Scientist" koncepcióról — egy olyan rendszerről, amely önállóan generál kutatási hipotéziseket, tervez kísérleteket, futtatja a szimulációkat, elemzi az eredményeket, és megírja a tanulmányt. A cikk széles körű vitát váltott ki.

**Az ígéret:**
- A tudományos felfedezés demokratizálása — kisebb kutatócsoportok is képesek lehetnek nagy volumenű kutatásra
- A „kutató szűk keresztmetszet" feloldása — több hipotézis tesztelhető, több irány fedezhető fel párhuzamosan
- A tudományos innováció ütemének felgyorsítása

**A veszélyek:**
- **Minőségellenőrzés.** Ki validálja az AI által generált hipotéziseket és eredményeket? Ha az AI Scientist maga bírálja el a saját munkáját, az zárt körhöz vezet, amelyben a hibák észrevétlenek maradnak.
- **Reprodukálhatóság.** Ha a teljes kutatási folyamatot AI végzi, és a modell nem-determinisztikus, hogyan reprodukálható a kutatás?
- **Felelősség.** Ha az AI Scientist hibás eredményt publikál, ki a felelős? A rendszert fejlesztő cég? Az intézmény, amely használja? A kutató, aki elindította?
- **Értékválasztás.** A tudomány nem értékmentes. Minden kutatási kérdés, módszertani választás és értelmezés mögött emberi ítéletek állnak. Egy AI Scientist, amely „hatékonyan" dolgozik, a legkönnyebben tesztelhető hipotéziseket fogja előnyben részesíteni — nem feltétlenül a legfontosabbakat.

Az AI Scientist nem a tudós helyettesítése, hanem egy eszköz, amely — mint minden hatékony eszköz — erősíti és felgyorsítja a mögötte álló szándékot, legyen az jó vagy rossz.

### A tudós szerepének átalakulása

A tudós szerepe az AI korában három fázisban változik:

**1. fázis: Csináló (doing) → Ez volt az elmúlt évszázadok normája.**
A tudós saját maga végzi a méréseket, az elemzéseket, az írást. Az AI-t legfeljebb segédeszközként használja — helyesírás-ellenőrzőként, keresőmotorként.

**2. fázis: Irányító (directing) → Ide tartunk most.**
A tudós a stratégiai döntéseket hozza — milyen kérdést vizsgáljunk, milyen módszerrel, mit jelent az eredmény —, miközben az operatív feladatok (adatfeldolgozás, kódolás, irodalomkeresés, első vázlat) jelentős részét AI-ágenseknek delegálja. A tudós szerepe a karmesteréhez hasonlít: nem ő játszik minden hangszeren, de ő határozza meg, mit játszanak és hogyan.

**3. fázis: Együttműködő (collaborating) → Ez a lehetséges jövő.**
A tudós és az AI partneri viszonyban dolgoznak. Az AI nem csak feladatokat hajt végre, hanem javaslatokat tesz, alternatívákat mutat, sőt: jelzi, ha az emberi kutató téved. Ez a fázis csak akkor lehetséges, ha az AI-rendszerek megbízhatósága jelentősen javul, és ha az ember-AI interakció mintái kiérlelődnek.

A kulcskérdés nem az, hogy **melyik fázisba kerülsz**, hanem az, hogy **tudatosan navigálod-e az átmenetet.** Aki passzívan sodródik, az elveszíti az irányítást a saját kutatói gyakorlata felett. Aki tudatosan alakítja az ember-AI együttműködést, az erősebb kutatóvá válik.

### A könyv befejezése után: az első lépések

Ez a könyv utolsó fejezete. Ha idáig eljutottál, rendelkezel az alapvető tudással ahhoz, hogy AI-t etikusan, hatékonyan és reprodukálhatóan használj a kutatásodban. De a tudás önmagában nem elég — a gyakorlat az, ami számít.

**Első lépés: Holnap reggel.**
Válassz egy konkrét feladatot a kutatásodból — egy irodalomkeresést, egy adatelemzést, egy kódrészletet —, és végezd el AI-asszisztenciával. Dokumentáld, amit csinálsz: melyik modellt használod, milyen prompttal, milyen eredményt kapsz, hogyan ellenőrzöd. Ez az első lépés.

**Második lépés: Az első héten.**
Alakítsd ki a saját AI-etikai keretrendszered (lásd a 16.4 fejezet gyakorlatát). Határozd meg, milyen feladatokra használsz AI-t, milyen ellenőrzési protokollal, milyen átláthatósági szinten.

**Harmadik lépés: Az első hónapban.**
Oszd meg a tapasztalataidat egy kollégával. Mutasd meg, mit csinálsz, hogyan csinálod, mit tanultál. A tudományos közösség normáit nem felülről diktálják — alulról építik, kutató kutató által.

**Negyedik lépés: Az első félévben.**
Írd meg az első kéziratodat, amelyben AI-asszisztenciát nyilatkozol a Methods szekcióban. Használd a 16.3 fejezet sablonját. Legyél átlátható. Legyél precíz. Legyél büszke arra, hogy tudatosan és felelősen dolgozol.

**Ötödik lépés: Folyamatosan.**
Maradj naprakész. Az AI-eszközök, a szabályozás és a közösségi normák gyorsabban változnak, mint bármely korábbi technológia esetében. Kövesd a területed folyóiratainak AI-politikáit. Kövesd az EU AI Act implementációját. Kövesd a kutatási közösséged vitáit.

---

## Záró gondolatok: Eucatastrophe

Tolkien fogalmát használva — amelyet Mollick az AI kontextusába helyez — a **eucatastrophe** a katasztrófa ellentéte: „a boldog végkifejlet öröme, vagy pontosabban: a hirtelen, örömteli fordulat."

Az AI-kutatás jövője sem egyetlen nagy katasztrófáról szól, sem egyetlen nagy áttörésről. A valóság sokkal szétszórtabb: sok kis katasztrófa (adatvédelmi incidensek, elfogult döntések, elhasalt reprodukálhatóság, elvesztett munkahelyek) és sok kis eucatastrophe (felgyorsult felfedezés, demokratizált kutatás, áttörések a betegségek megértésében, felszabadított idő a kreatív gondolkodásra).

A tudós feladata — a te feladatod — az, hogy a kis eucatastrophék felé terelje a dolgokat. Nem naivan, nem kritikátlanul, hanem tudatosan, etikusan és a kutatói integritás iránti elkötelezettséggel.

Narayanan és Kapoor — az *AI Snake Oil* szerzői — figyelmeztetnek: **az AI-t gyakran arra használják, hogy olcsó pótlékként helyettesítse az intézményi reformot, a megfelelő finanszírozást és az emberi erőforrásokat.** Ne engedd, hogy a saját kutatói környezetedben ez történjen. Az AI nem helyettesít, hanem kiegészít. Nem gondolkodik helyetted — segít gondolkodni.

Ez a könyv azzal a meggyőződéssel íródott, hogy a tudomány az emberiség egyik legnemesebb tevékenysége, és az AI az emberiség egyik leghatékonyabb eszköze. A kettő találkozása nem automatikusan pozitív — de ha tudatosan, etikusan és nyitottan közelítjük meg, az eredmény nagyszerű lehet.

A döntés a tiéd.

---

## Fogalomtár

| Fogalom | Definíció |
|---------|-----------|
| **Posztplágium (postplagiarism)** | Sarah Elaine Eaton (2023) fogalma: a generatív AI utáni korszak integritási paradigmája, amely felismeri, hogy az ember-AI hibrid szerzőség az új norma, és az integritás fő kérdése nem a szöveg eredete, hanem az átláthatóság, a felelősségvállalás és az intellektuális hozzáadott érték. Hat alaptételre épül. |
| **Hallucináció (hallucination)** | Az LLM által generált, faktuálisan hamis információ, amelyet a modell ugyanolyan magabiztosan ad elő, mint a pontos adatokat. |
| **ICMJE** | International Committee of Medical Journal Editors — a tudományos szerzőség négy kritériumát meghatározó testület. |
| **CRediT** | Contributor Roles Taxonomy — 14 szerzői szerepet definiáló rendszer, amely részletesebb attribúciót tesz lehetővé. |
| **EU AI Act** | Az Európai Unió mesterséges intelligenciáról szóló rendelete (2024), kockázatalapú szabályozási keretrendszer. |
| **COPE** | Committee on Publication Ethics — a kiadói etika legfőbb nemzetközi testülete. |
| **Temperature** | Az LLM kimeneti véletlenszerűségét szabályozó paraméter (0 = determinisztikusabb, 1+ = kreatívabb). |
| **Version pinning** | Egy konkrét modellverzió rögzítése a kutatás idejére a reprodukálhatóság érdekében. |
| **Prompt logging** | A promptok szisztematikus naplózása és verziókezelése. |
| **Data provenance** | Az adat eredetének, feldolgozási lépéseinek és származásának dokumentálása. |
| **RLHF** | Reinforcement Learning from Human Feedback — az LLM-ek finomhangolási módszere, ahol emberi preferenciák alapján tanul a modell. |
| **Szikofáncia (sycophancy)** | Az LLM tendenciája, hogy inkább egyetért a felhasználóval, mint hogy pontos legyen. |
| **p(doom)** | Informális fogalom az AI-kutatók között: az emberi kihalás becsült valószínűsége az AI-fejlesztés következtében. |
| **Eucatastrophe** | Tolkien fogalma: a hirtelen, örömteli fordulat — a katasztrófa ellentéte. Mollick keretrendszere az AI hatásainak megközelítéséhez. |
| **AGI** | Artificial General Intelligence — hipotézis szerinti AI-rendszer, amely minden területen eléri vagy meghaladja az emberi intelligenciát. |

---

## Hivatkozások

- Eaton, S.E. (2023). Postplagiarism: Transdisciplinary Ethics of AI-Augmented Work. *International Journal for Educational Integrity*, 19(1), 23.
- Gray, A. (2024). ChatGPT contamination: Estimating the prevalence of LLMs in the scholarly literature. *arXiv preprint*.
- Frankfurt, H.G. (2005). *On Bullshit.* Princeton University Press.
- Narayanan, A. & Kapoor, S. (2024). *AI Snake Oil: What Artificial Intelligence Can Do, What It Can't, and How to Tell the Difference.* Princeton University Press.
- Mollick, E. (2024). *Co-Intelligence: Living and Working with AI.* Portfolio/Penguin.
- European University Association (2026). *Adopting AI in Universities: A Practical Guide.* EUA Task-and-Finish Group on AI.
- National Academies of Sciences, Engineering, and Medicine (2024). *AI-Enabled Biological Design and the Risks of Synthetic Biology.* The National Academies Press.
- ICMJE (2023). *Recommendations for the Conduct, Reporting, Editing, and Publication of Scholarly Work in Medical Journals.* Updated with AI guidance.
- COPE (2023, updated 2025). *COPE Position Statement on AI Tools in Research Publication.*
- European Parliament (2024). *Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence (AI Act).*
- NASA (2024). *Principles for the Ethical Use of Artificial Intelligence.* NASA Technical Reports Server.
- Kapoor, S. & Narayanan, A. (2023). Leakage and the Reproducibility Crisis in Machine-Learning-Based Science. *Patterns*, 4(9).
- Gundersen, O.E. & Kjensmo, S. (2018). State of the art: Reproducibility in artificial intelligence. *AAAI Conference*.
- Bender, E.M. et al. (2021). On the Dangers of Stochastic Parrots. *ACM FAccT*.
- NASEM (2018). *Biodefense in the Age of Synthetic Biology.* The National Academies Press.
