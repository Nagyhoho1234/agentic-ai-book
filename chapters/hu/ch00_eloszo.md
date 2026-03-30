# Előszó

## Kinek szól ez a könyv

Ez a könyv mindenkinek szól, aki a tudományos kutatásban, az egyetemi oktatásban vagy a kutatásszervezésben dolgozik, és szeretné megérteni, hogyan alakítja át a mesterséges intelligencia ezeket a területeket. Nem kell értened a Pythonhoz, nem kell tudnod, mi az a Docker, és nem kell ismerned a gépi tanulás matematikai alapjait. Elég, ha van egy kutatási kérdésed, egy adathalmazod, egy tantárgyad, amelyet jobbá akarsz tenni — és nyitott vagy arra, hogy egy új típusú eszközzel dolgozz.

Ez a könyv arról szól, hogyan használd az AI-t hatékonyan a saját kutatásodban, oktatásodban és intézményi munkádban anélkül, hogy szoftvermérnökké kellene válnod.

## Mit jelent a „nem-programozó"

Tisztázzunk valamit rögtön az elején. Amikor „nem-programozóról" beszélek, nem azt értem, hogy kevesebbet tudsz, mint egy informatikus. Épp ellenkezőleg: te a saját szakterületed szakértője vagy. Ismered a talajkémia, a genomika, a közgazdaságtan, a nyelvészet vagy az anyagtudomány belső logikáját olyan mélységben, amit egy programozó soha nem fog elérni.

Lehet, hogy Excelben dolgozol, talán SPSS-ben vagy R-ben futtatsz statisztikákat, esetleg GIS-szoftvereket használsz. Lehet, hogy írtál már néhány sort MATLAB-ban vagy Pythonban, de nem érzed magadénak. Ez teljesen rendben van. Ez a könyv pontosan azért született, mert 2026-ban az AI megírja helyetted a kódot — neked csak azt kell tudnod, mit akarsz csinálni és hogyan kérd el.

## Miért most

Az AI világa 2024 és 2026 között alapvetően megváltozott. Nem csupán arról van szó, hogy a chatbotok okosabbak lettek. Egy minőségileg új kategória jelent meg: az **ágentikus AI**. Olyan rendszerek, amelyek nem csak válaszolnak a kérdéseidre, hanem önállóan terveznek, eszközöket használnak, kódot írnak, fájlokat kezelnek, és lépésről lépésre megoldják a feladataidat.

Olyan eszközök, mint a Claude Code, a Cursor, a GitHub Copilot Workspace és a különféle ágens-keretrendszerek lehetővé teszik, hogy egy kutató — programozói háttér nélkül — olyan feladatokat oldjon meg, amelyekhez két éve még egy dedikált szoftverfejlesztőre volt szükség: adatpipeline-okat építsen, szimulációkat futtasson, interaktív vizualizációkat készítsen, vagy akár egy komplett digitális ikret hozzon létre a laborjáról.

Az időzítés intézményi szempontból is ideális. Magyarország 2025–2030-as AI Stratégiája konkrét lendületet ad az egyetemi AI-alkalmazásoknak. A Debreceni Egyetem rendelkezik az infrastruktúrával — a Komondor szuperszámítógéphez való hozzáférés, az NVIDIA Deep Learning Institute együttműködés, a BMW és más ipari partnerségek mind adottak. Ami hiányzik, az egy gyakorlati útmutató, amely megmutatja a kutatóknak és oktatóknak, hogyan használják ezeket az erőforrásokat a mindennapjaikban.

Ez a könyv ezt az űrt tölti be.

## Hogyan épül fel a könyv

![A könyv felépítése — 5 rész, 16 fejezet áttekintő ábrája](images/ch00_book_structure.png)

A könyv 5 részből és 16 fejezetből áll, fokozatosan növekvő komplexitással:

- **I. rész (1–4. fejezet): Alapok** — Az AI-forradalom kontextusa, a társalgási AI elsajátítása, tudományos írás AI-val, adatelemzés kód nélkül. Ezek a fejezetek mindenki számára kötelezők.
- **II. rész (5–8. fejezet): Kód és számítás** — Kódolási asszisztensek, matematikai modellezés, adat-pipeline-ok, vizuális programozás. Itt az AI már kódot ír neked.
- **III. rész (9–10. fejezet): Tudáskezelés** — RAG-rendszerek és digitális ikrek. Az AI a saját adataidon és dokumentumaidon dolgozik.
- **IV. rész (11–13. fejezet): Ágensek** — AI-ágensek megértése, építése, és saját eszközök készítése. A könyv csúcspontja.
- **V. rész (14–16. fejezet): Intézményi szint** — Az AI a laborban, az egyetemen, és az etikai-jövőbeli kérdések.

**Olvasási útvonalak:** A 4. fejezet után nem kell lineárisan haladnod. A könyv elején találsz szakterület-specifikus olvasási útvonalakat — ha biológus vagy, ha közgazdász, ha mérnök, mindegyikhez más fejezetsorrend az optimális.

Minden fejezetben megtalálod:
- **„A te szakterületeden"** dobozokat, amelyek konkrét példákat adnak különböző tudományterületekről
- **Gyakorlatokat**, amelyeket azonnal kipróbálhatsz
- **Hibaelhárítás** szekciót, mert az AI nem mindig működik elsőre — és fontos tudnod, mit csinálj ilyenkor

## A társwebhely és kódtár

A könyvhöz tartozik egy nyilvános GitHub-repository, amely tartalmazza:

- Az összes kódpéldát futtatható formában
- Prompt-sablonokat, amelyeket azonnal használhatsz a saját munkádban
- Jupyter-notebookokat lépésről lépésre végigvezető gyakorlatokkal
- Rendszeresen frissített tartalmakat, ahogy az eszközök fejlődnek

Az AI-eszközök villámgyorsan változnak. Egy nyomtatott könyv hat hónapon belül elavulhat — a társwebhely biztosítja, hogy mindig naprakész maradj.

## Mollick négy szabálya

![Mollick négy szabálya — vizuális összefoglaló](images/ch00_mollick_rules.png)

Ethan Mollick, a Wharton School professzora négy alapszabályt fogalmazott meg az AI hatékony használatához. Ez a négy szabály végigvonul az egész könyvön, mint vezérfonal:

1. **Mindig hívd meg az AI-t az asztalhoz** — Minden új feladatnál kérdezd meg magadtól: „Hogyan segíthetne itt az AI?"
2. **Te vagy a felelős ember a rendszerben** — Az AI javasol, te döntesz. A szakmai ítéleted pótolhatatlan.
3. **Ne mondd el senkinek** — vagyis ne áruld el előre, mire képes és mire nem. Próbáld ki magad, mert a határok napról napra változnak.
4. **Kezeld úgy, mint egy gyakornokot** — Adj neki konkrét utasításokat, ellenőrizd a munkáját, és legyél türelmes, de igényes.

Ezek a szabályok nem elvont elvek — a gyakorlatban fogod látni, hogyan alkalmazhatók a kutatói munka minden fázisában.

## Köszönetnyilvánítás

*[A szerző köszönetnyilvánítása a végleges verzióban kerül ide.]*

## Hogyan készült ez a könyv

Végül egy fontos megjegyzés az átláthatóság jegyében. Ez a könyv AI-eszközök segítségével készült — a tervezéstől a vázlaton át a szövegezésig. A Claude, a ChatGPT és a Codex egyaránt szerepet kaptak a folyamatban. Ez nem szégyen, hanem demonstráció: a könyv maga is bizonyítéka annak a tézisnek, amelyet képvisel — hogy az AI társintelligenciaként (*co-intelligence*) működhet a tudományos munkában.

Ez nem azt jelenti, hogy egy robot írta a könyvet. Minden tényt ellenőriztem. Minden ajánlást kipróbáltam. Minden hivatkozott keretrendszert és eszközt valós kutatási környezetben teszteltem. Az AI felgyorsította a munkát, de a felelősség, a szakmai ítélet és a minőségbiztosítás végig emberi maradt — pontosan úgy, ahogy a könyv maga is javasolja.

Ha ez a megközelítés furcsa számodra, az rendben van. A 16. fejezet végére valószínűleg másként gondolsz majd rá.

---

*Debrecen, 2026*
