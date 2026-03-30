# 6. fejezet: AI-támogatott matematikai modellezés és szimuláció

> **Fejezet-információ**
> - **Kinek szól:** Természettudósoknak és mérnököknek, akik matematikai modellekkel és szimulációkkal dolgoznak
> - **Előismeretek:** 5. fejezet (kódolási asszisztensek)
> - **Amit megtanulsz:**
>   - Kutatási kérdésből matematikai modell készítése AI segítségével
>   - Szimbolikus számítások (SymPy) és numerikus szimuláció AI-val
>   - Automatikus kalibráció és egyenletfelfedezés (PySR)
> - **Szükséges eszközök:** Böngésző + terminál + Python
> - **Kapcsolódó fejezetek:** 5. fejezet (kódolás), 7. fejezet (pipeline-ok), 10. fejezet (digitális ikrek)

## Bevezetés: Amikor az egyenletek élni akarnak kelni

> **🖼️ Ábra: A matematikai modellezés AI-támogatott munkafolyamata**
> *Körkörös diagram: Kutatási kérdés → Matematikai modell → Implementáció (AI-val) → Szimuláció → Kalibráció → Validáció → Új kérdések. Az AI szerepe minden lépésnél jelölve.*


Képzeld el a következő helyzetet. Kovács Márta környezetkutató a Debreceni Egyetem Környezettudományi Tanszékén dolgozik. Évek óta vizsgálja a Hortobágy vízháztartását: hogyan szivárog a csapadék a talajba, hogyan változik a talajvízszint az évszakokkal, hogyan hat a klímaváltozás a szikes tavak vízutánpótlására. A terepnapló tele van mérésekkel, a füzetében ott vannak a differenciálegyenletek -- de papírról nem fut szimuláció.

Marta ismeri a fizikai torvenyeket. Tudja, hogy a Darcy-torveny leirja a vizaramlast porszos kozegben, hogy a Richards-egyenlet megadja a telitetlen zona vizmozgasat. De nincs ideje megtanulni a numerikus modszereket a nullarol, es nem akar honapokat tolteni azzal, hogy Python kodot debuggoljon.

Pontosan ez az a pont, ahol az AI mint matematikai fordito belep a kepbe.

Ebben a fejezetben vegigvezetlek azon, hogyan hasznalhatod az AI-t arra, hogy:

- Kutatasi kerdest matematikai formaba ontsd
- Egyenleteket ellenorizz, egyszerusits, levezess
- Papirrol koddal futo szimulaciot keszits -- egyetlen beszelgetessel
- Szimbolikus szamitasokat vegezz SymPy-val
- Szimulaciot epits, kalibrald automatikusan
- Es ha akarod: az AI-val uj egyenleteket is felfedezz az adataidbol

---

## 6.1 Kutatasi kerdesbol matematikai modell -- AI-val

### A modellalkotasi folyamat

Minden szimulacio egy kutatasi kerdessel kezdodik:

> "Hogyan valtozik a talajvizszint a Hortobagy teruleten, ha a nyari csapadek 20%-kal csokken?"

Ezt a kerdest *matematikai modelle* kell alakitani, ami harom lepesbol all:

1. **Valtozok azonositasa**: Mi valtozik? (talajvizszint *h*, ido *t*, hely *x*, csapadek *P*)
2. **Torvenyek, osszefuggesek**: Milyen fizikai/kemiai/biologiai torveny kotik ossze oket?
3. **Feltetelrendszer**: Milyen kezdeti es peremfeltetelek vannak?

Az AI segitsege mar az elso lepesnel hasznos. Nezd meg a kovetkezo peldabeszelgetest:

---

**Te:**
> Egy sekely talajvizrendszert szeretnek modellezni a Hortobagyon. A bemenet a csapadek es a parologtatas, a kimenet a talajvizszint idobeli valtozasa. Milyen differencialeqyenletet hasznaljak erre egydimenziosan?

**Claude:**
> A legegyszerubb megkozelites egy 1D telitetlen-telitett zona modell, de ha csak a talajvizszint idobeli valtozasa erdekel (tehat vertikalisan integralt modell), akkor a **Boussinesq-egyenlet** linearizalt valtozata jo kiindulas:
>
> $$S_y \frac{\partial h}{\partial t} = T \frac{\partial^2 h}{\partial x^2} + R(t) - ET(t)$$
>
> ahol:
> - $h(x,t)$ a talajvizszint [m]
> - $S_y$ a fajlagos vizleadas (specific yield) [-]
> - $T$ a transzmisszivitas [m^2/s]
> - $R(t)$ a beszivargas (recharge) [m/s]
> - $ET(t)$ a talajvizbol valo parologtatas [m/s]
>
> Ez egy parabolikus PDE, ami a hoegyenlethez hasonlo, csak forrastaggal.
>
> Ha a teruletet homogennek tekinted es csak az idobeli valtozas erdekel (tehat nem a teri eloszlas), tovabb egyszerusitheted ODE-ve:
>
> $$S_y \frac{dh}{dt} = R(t) - ET(t) - \frac{T}{L^2}(h - h_0)$$
>
> ahol $L$ a jellemzo tavolsag a legkozelebbi allandofeju peremfelteteltol, $h_0$ a perem vizszintje.

---

Ez a beszelgetes par masodperc alatt megadta neked azt, amihez egyebkent szakkonyvek olvasasara lenne szukseged. Fontos: **mindig ellenorizd az eredmenyt!** Az AI neha hibas egyenletet ad, vagy elhagyja a peremfeltetelek reszleteit. A legjobb strategia:

1. Kerd az AI-t, hogy *vezesse le* az egyenletet, ne csak irja oda
2. Kerd meg, hogy **adjon meg forrasokat** (konyv, cikk) ahol ez az egyenlet szarmazik
3. Ellenorizd a dimenziot: mindket oldal egysege megegyezik-e?
4. Próbáld ki határeseteken: ha $R = 0$ es $ET = 0$, tényleg állandó marad-e $h$?

> **Ne csináld!**
> Ne fogadd el az AI altal javasolt egyenletet vagy modellt a dimenziok (mereteqysegek) ellenorzese nelkul. Az LLM-ek gyakran generalnak fizikailag helyes kinezettu, de dimenzionalisan inkonzisztens egyenleteket — peldaul baloldalon [m/s], jobboldalon [m]. Ha nem ellenorzod, a szimulacio "fuut", de az eredmenyek ertelmetlenek lesznek.

### Prompt-minta: Modell-kereses

Ime egy prompt, amit barmilyen tudomanyteruleten hasznalhatsz:

```
Kutatasom targyat [rovid leiras] differencialeqyenlettel szeretnem leirni.

Bemenet valtozok: [felsorolas, egyseggel]
Kimenet valtozo: [valtozo, egyseg]
Fontos fizikai/biologiai/kemiai torvenyek: [pl. megmaradasi torvenyek, Fick-torveny]
Egyszerusitesek, amiket elfogadok: [pl. 1D, stacioner, linearizalt]

Kerlek:
1. Ird fel a differencialeqyenletet minden taggal
2. Magyarazd el minden tag fizikai jelenteset
3. Add meg a tipikus peremfeltetelek fajtait
4. Adj forrasokat, ahol ez a modell reszletesen le van irva
5. Ellenorizd a dimenziokat
```

> **🌾 Szakterületi példa: GR4J csapadék-lefolyás modell és Oudin PET-képlet**
>
> A hidrológiai modellezésben a GR4J modell négy paraméterrel írja le a csapadék lefolyássá alakulását: a termelési tározó kapacitása ($x_1$), a talajvízcsere ($x_2$), az útvonalválasztási tározó ($x_3$) és az egységhidrográf időbázisa ($x_4$). A potenciális evapotranszpirációt az Oudin-képlet becsli: $PE = \frac{R_a}{\lambda \rho} \cdot \frac{T_a + 5}{100}$. Az AI-asszisztens képes ezeket a képleteket implementálni, a paraméterek fizikai jelentését magyarázni, és a kezdeti értékeket a vízgyűjtő jellemzőiből kiindulva becsülni — pontosan a fenti „kutatási kérdésből modell" munkafolyamatot követve.
>
> *Forrás: hidrogis 24.4.1 „A feladat beállítása" és 24.11.2 „Az ágenses kalibrálás végigvezetése"*

---

## 6.2 Egyenletekbol kód -- AI mint fordito

### 6.2.1 Kozonsegses differencialeqyenletek (ODE-k)

A leggyakrabban elofordulo feladat: van egy (vagy tobb) differencialeqyenleted, es szeretned idoben eloreleptetve megoldani. Ennek harom fo modja van:

**Euler-modszer** -- a legegyszerubb, de a legpontatlanabb:

$$y_{n+1} = y_n + h \cdot f(t_n, y_n)$$

**Runge-Kutta 4 (RK4)** -- a "svedjcskés" a numerikus modszerek kozott, kivalo pontossag/sebesseg aranyban:

$$y_{n+1} = y_n + \frac{1}{6}(k_1 + 2k_2 + 2k_3 + k_4)$$

**SciPy solvers** -- a gyakorlatban majdnem mindig ezeket hasznald, mert automatikusan valasztjak meg a lepeskOzt es kezelik a merev (stiff) rendszereket is.

### Dolgozott pelda: Talajvizszint-modell

Folytassuk Marta peldat. Van a leegyszerusitett ODE-nk:

$$S_y \frac{dh}{dt} = R(t) - ET(t) - \frac{T}{L^2}(h - h_0)$$

Ime a beszelgetes az AI-val:

---

**Te:**
> Meg szeretnem oldani a kovetkezo differencialeqyenletet Python-ban:
>
> S_y * dh/dt = R(t) - ET(t) - T/L^2 * (h - h0)
>
> ahol S_y = 0.15, T = 100 m^2/nap, L = 500 m, h0 = 85 m.
> R(t) es ET(t) havi felbontasu adatsorok (12 honapra).
> Kezdeti feltetel: h(0) = 86 m.
> Szimulalj 3 evet.
>
> Hasznald a scipy.integrate.solve_ivp fuggvenyt. Az eredmenyt abrazold.

**Claude:**

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Parameterek
S_y = 0.15          # fajlagos vizleadas [-]
T = 100.0           # transzmisszivitas [m^2/nap]
L = 500.0           # jellemzo tavolsag [m]
h0 = 85.0           # perem vizszint [m]

# Havi beszivargas es parologtatas [m/nap]
# (jan-dec, tipikus alföldi ertekek)
R_havi = np.array([0.0005, 0.0008, 0.0015, 0.0020, 0.0018,
                   0.0010, 0.0005, 0.0003, 0.0006, 0.0010,
                   0.0008, 0.0005])  # m/nap

ET_havi = np.array([0.0001, 0.0002, 0.0005, 0.0010, 0.0020,
                    0.0030, 0.0035, 0.0030, 0.0015, 0.0005,
                    0.0002, 0.0001])  # m/nap

def R_t(t):
    """Beszivargas interpolalasa idoponthoz."""
    honap = int(t % 365 / 30.44) % 12
    return R_havi[honap]

def ET_t(t):
    """Parologtatas interpolalasa idoponthoz."""
    honap = int(t % 365 / 30.44) % 12
    return ET_havi[honap]

def dhdt(t, h):
    """A differencialeqyenlet jobb oldala."""
    return (R_t(t) - ET_t(t) - T / L**2 * (h - h0)) / S_y

# Megoldas
t_span = (0, 3 * 365)  # 3 ev napokban
t_eval = np.linspace(0, 3 * 365, 1000)

sol = solve_ivp(dhdt, t_span, [86.0], t_eval=t_eval,
                method='RK45', rtol=1e-8)

# Abrazolas
fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(sol.t / 365, sol.y[0], 'b-', linewidth=2)
ax.axhline(y=h0, color='gray', linestyle='--', label=f'Perem ($h_0$ = {h0} m)')
ax.set_xlabel('Ido [ev]')
ax.set_ylabel('Talajvizszint [m]')
ax.set_title('Talajvizszint szimulacio -- Hortobagy')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('talajviz_szimulacio.png', dpi=150)
plt.show()
```

---

Nezd, mi tortent: egyetlen prompttal kaptunk egy teljes, futtathato szimulaciot. Az AI:

- A matematikai formulat leforditotta Python fuggvenyre
- Megvalasztotta a megfelelo solvert (`RK45`)
- Kezelte az idofuggo forcirozast (havi adatok interpolalasa)
- Letrehozott egy ertelmes vizualizaciot

**Fontos ellenorzesi pontok:**

- A `dhdt` fuggveny tenyleg az eredeti egyenletet implementalja-e? (Igen, ellenorizd tagrol tagra.)
- Az egysegek konzisztensek-e? (Minden m/nap-ban van, es `S_y` dimenzio nelkuli -- stimmel.)
- A `method='RK45'` megfelelo valasztas-e? (Igen, nem merev rendszernel ez a standard.)

### ODE-megoldok valasztasa -- gyors utmutato

| Szituacio | Ajanlott modszer | SciPy parameter |
|-----------|-----------------|-----------------|
| Altalanos, nem merev | Runge-Kutta 4-5 | `method='RK45'` |
| Merev rendszer (pl. kemiai kinetika) | Implicit modszer | `method='Radau'` vagy `'BDF'` |
| Nagyon pontos megoldas kell | 8. rendu | `method='DOP853'` |
| Tanulashoz / megerteshez | Euler, sajat implementacio | -- |

> **Tipp:** Ha nem tudod, merev-e a rendszered, probald RK45-tel. Ha nagyon lassu vagy instabil, valts `Radau`-ra. Vagy egyszeruen kerdezd meg az AI-t: "Ez a rendszer merev? Milyen solvert hasznaljak?"

### 6.2.2 Parciális differencialeqyenletek (PDE-k)

Amikor a megoldas nemcsak az idotol, hanem a helytol is fugg, PDE-kkel dolgozunk. A ket leggyakoribb numerikus megkozelites:

**Veges differencia modszer** -- a PDE-ben a derivaltakat differencia-hanyadosokkal kozelitjuk egy racson:

$$\frac{\partial u}{\partial t} \approx \frac{u_i^{n+1} - u_i^n}{\Delta t}, \qquad \frac{\partial^2 u}{\partial x^2} \approx \frac{u_{i+1}^n - 2u_i^n + u_{i-1}^n}{\Delta x^2}$$

**Veges elem modszer (FEM)** -- a megoldast bázisfuggvenyek linearis kombinaciojakeent keressuk. Ez rugalmasabban kezeli az osszetett geometriakat, de bonyolultabb implementalni.

### Dolgozott pelda: Hoteruletes diffuzio

Peldaul vizsgaljuk, hogyan terjed a ho egy vekony fem rudon:

$$\frac{\partial u}{\partial t} = \alpha \frac{\partial^2 u}{\partial x^2}$$

---

**Te:**
> Oldd meg az 1D hoegyenletet Python-ban veges differenciakkal.
> A rud hossza L = 1 m, a hodiffuzios egyutthato alpha = 0.01 m^2/s.
> Bal vegen 100 C, jobb vegen 0 C (Dirichlet peremfeltetel).
> Kezdetben a rud mindenhol 0 C (kiveve a bal veget).
> Szimulalj 2 masodpercet, animald az eredmenyt.

**Claude:**

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameterek
L = 1.0           # rud hossza [m]
alpha = 0.01      # hodiffuzios egyutthato [m^2/s]
nx = 50           # terlepcso szama
dx = L / (nx - 1) # terbeli lepcso [m]
dt = 0.4 * dx**2 / alpha  # idolepcso -- stabilitasi feltetel!
nt = int(2.0 / dt)  # osszesen ennyi idolepcso

# Kezdeti feltetel
u = np.zeros(nx)
u[0] = 100.0   # bal perem: 100 C

# Tarolás az animaciohoz
u_history = [u.copy()]

# Idoben eloreleptetes (explicit veges differencia)
for n in range(nt):
    u_new = u.copy()
    u_new[1:-1] = u[1:-1] + alpha * dt / dx**2 * (u[2:] - 2*u[1:-1] + u[:-2])
    u_new[0] = 100.0   # bal perem
    u_new[-1] = 0.0     # jobb perem
    u = u_new
    if n % 20 == 0:
        u_history.append(u.copy())

# Animacio
x = np.linspace(0, L, nx)
fig, ax = plt.subplots(figsize=(10, 5))
line, = ax.plot(x, u_history[0], 'r-', linewidth=2)
ax.set_xlim(0, L)
ax.set_ylim(-5, 105)
ax.set_xlabel('Pozicio [m]')
ax.set_ylabel(u'Homerseklet [\u00b0C]')
ax.set_title(u'Hoteruletes diffuzio -- veges differencia modszer')
ax.grid(True, alpha=0.3)

def update(frame):
    line.set_ydata(u_history[frame])
    ax.set_title(f'Hoteruletes diffuzio -- t = {frame * 20 * dt:.3f} s')
    return line,

ani = FuncAnimation(fig, update, frames=len(u_history), interval=50, blit=True)
plt.tight_layout()
plt.show()
```

---

Figyeld meg a `dt = 0.4 * dx**2 / alpha` sort -- ez a **CFL stabilitasi feltetel**. Explicit veges differencia modszernel az idolepcso nem lehet tetszOlegesen nagy, kulonben a megoldas felrobban. Az AI altalaban tudja ezt, de **mindig kerdezz ra**:

> "Milyen stabilitasi feltetele van ennek a numerikus semanak? Teljesul a kodomban?"

### 6.2.3 Optimalizalas es algebrai rendszerek

Nem minden problema differencialeqyenlet. Gyakran kell:

- **Minimalizalni vagy maximalizalni** egy celoveny: pl. "Milyen osszetetu legyen az otvozet, hogy a szilardság maximalis?"
- **Algebrai egyenletrendszert megoldani**: pl. kemiai egyensúlyi rendszerek
- **Illeszkedes**: parametereket beallitani, hogy a modell a meresekre illeszkedjen

```python
from scipy.optimize import minimize, fsolve, curve_fit

# Pelda: nemlinearis egyenletrendszer megoldasa
# Kemiai egyensuly: 2 reakcio, 2 ismeretlen koncentracio
def equations(c):
    c1, c2 = c
    eq1 = c1 * c2 - 0.5 * (1 - c1)    # egyensulyi feltetel 1
    eq2 = c1**2 - 0.3 * c2              # egyensulyi feltetel 2
    return [eq1, eq2]

solution = fsolve(equations, x0=[0.5, 0.5])
print(f"c1 = {solution[0]:.4f}, c2 = {solution[1]:.4f}")
```

### Az AI mint fordito -- osszefoglalo minta

A legfontosabb uzenet ebben a szekcioban: **az AI kiválo forditoként mukodik az egyenletek es a kod kozott.** Ime a minta, amit kovethetsz:

```
Van egy egyenletem / modellom:
[ird le a matematikai formulat, szoveggel vagy LaTeX-ben]

A parameterek:
[ertek, egyseggel]

A feltetelrendszer:
[kezdeti feltetelek, peremfeltetelek]

Kerlek:
1. Implementald Python-ban [scipy / sajat solver / FEniCS]
2. Futtasd [ennyi idore / ilyen feltetelek mellett]
3. Abrazold az eredmenyt
4. Ellenorizd a stabilitast / pontossagot
```

---

## 6.3 Szimbolikus szamitas SymPy-val

Eddig numerikus megoldasokrol beszeltunk -- szamitogep szamol, kozelito eredmenyt kapsz. De mi van, ha **exakt, kepletalaku** megoldast szeretnel? Erre valo a szimbolikus szamitas.

A **SymPy** Python konyvtar a Mathematica es a Maple ingyenes alternativaja. Az AI-val kombinálva rendkivul hatekonyan hasznalhato.

### Mit tud a SymPy?

| Feladat | SymPy fuggveny | Pelda |
|---------|---------------|-------|
| Derivalt | `diff(expr, x)` | $\frac{d}{dx}\sin(x^2) = 2x\cos(x^2)$ |
| Integral | `integrate(expr, x)` | $\int x e^x dx = (x-1)e^x$ |
| Egyszerusites | `simplify(expr)` | Komplex toredekek egyszerusitese |
| Egyenletmegoldas | `solve(eq, x)` | $x^3 - 6x + 4 = 0$ gyokei |
| ODE megoldas | `dsolve(eq, f(x))` | Analitikus megoldas, ha letezik |
| Taylor-sor | `series(expr, x, 0, n)` | Kozelites polinom |
| Matrixmuveletek | `Matrix(...).eigenvals()` | Sajatértekek, determinans |

### Dolgozott pelda: Egyenlet-levezetés es ellenorzes

Tegyuk fel, hogy Marta szeretne ellenorizni: a linearizalt Boussinesq-egyenletnek van-e analitikus megoldasa allandó forcirozas eseten.

---

**Te:**
> SymPy-val oldd meg a kovetkezo ODE-t analitikusan:
> S_y * dh/dt = R - ET - T/L^2 * (h - h0)
> ahol R, ET, S_y, T, L, h0 mind allando parameterek.
> Kezdeti feltetel: h(0) = h_init

**Claude:**

```python
from sympy import *

# Szimbolikus valtozok definiálása
t = symbols('t')
h = Function('h')
S_y, R, ET, T_param, L, h0, h_init = symbols(
    'S_y R ET T L h_0 h_init', positive=True
)

# Differencialeqyenlet felirasa
ode = Eq(S_y * h(t).diff(t),
         R - ET - T_param / L**2 * (h(t) - h0))

print("Az egyenlet:")
pprint(ode)

# Megoldas
sol = dsolve(ode, h(t), ics={h(0): h_init})
print("\nAltalanos megoldas:")
pprint(sol)

# Egyszerusites
sol_simplified = simplify(sol)
print("\nEgyszerusitett alak:")
pprint(sol_simplified)

# Stacioner megoldas (t -> vegtelen)
h_steady = limit(sol.rhs, t, oo)
print(f"\nStacioner vizszint: h_inf = {simplify(h_steady)}")
```

Kimenet (egyszerusitve):

$$h(t) = h_0 + \frac{(R - ET) L^2}{T} + \left(h_{init} - h_0 - \frac{(R - ET) L^2}{T}\right) e^{-\frac{T}{S_y L^2} t}$$

Ez rendkivul hasznos eredmeny! Ebbol rogtOn latod, hogy:

- A rendszer **exponencialisan** tart egy egyensulyhoz
- Az egyensulyi vizszint: $h_\infty = h_0 + (R - ET) L^2 / T$
- A jellemzo idoskala: $\tau = S_y L^2 / T$

Ezeket az osszefuggeseket szamszeruen is kiertekelheted:

```python
# Numerikus kiertekeles
params = {S_y: 0.15, T_param: 100, L: 500, h0: 85, R: 0.001, ET: 0.0015}

tau = (0.15 * 500**2) / 100  # nap
print(f"Jellemzo idoskala: {tau:.0f} nap ({tau/365:.1f} ev)")

h_inf = 85 + (0.001 - 0.0015) * 500**2 / 100
print(f"Egyensulyi vizszint: {h_inf:.2f} m")
```

### SymPy + AI: a gyakorlatban

A leghatekonyabb hasznalati mod: kerd az AI-t, hogy **SymPy koddal vegezze el** a levezetest, ne csak kepleteket irjon. Igy:

1. Ellenorizheted a lepeseket (lefuttatod a kodot)
2. Modosithatod a felteteleket (mas peremfeltetel, mas egyszerusites)
3. A numerikus es szimbolikus megoldast ossze tudod hasonlitani

> **Tipp:** Ha a SymPy `dsolve` nem tud megoldani egy egyenletet (komplex nemlinearis rendszereknel elofordul), kerdezd meg az AI-t: "Milyen kozelito analitikus modszer letezik erre? Perturbacio-szamitas? WKB? Linearizalas?"

---

## 6.4 Szimulaciotipusok: Melyiket valaszd?

Nem minden szimulacio differencialeqyenlet-megoldas. Az alabbiakban attekintjuk a harom fo szimulaciotipust es azt, mikor melyiket erdemes valasztani.

### 6.4.1 Determinisztikus modellek

Adott bemenet eseten mindig ugyanazt az eredmenyt adjak. Ilyen a legtobb klasszikus fizikai modell: megoldod az egyenletet, megkapod az eredmenyt.

**Mikor hasznald:** Jol ismert fizikai torvenyek, alacsony zaj, kevés bizonytalansag a parameterekben.

### 6.4.2 Sztochasztikus es Monte Carlo modellek

**Monte Carlo szimulacio:** a bemeneti parametereket veletlen eloszlasbol huzod, es sokszor futtatod a modellt. Az eredmeny nem egyetlen szam, hanem **eloszlas**.

Ez rendkivul hasznos, ha a parametereidben bizonytalansag van -- es az szinte mindig van.

```python
import numpy as np
from scipy.integrate import solve_ivp

def run_simulation(S_y, T, R_mean, ET_mean, h_init):
    """Egyetlen szimulacio futtatas."""
    def dhdt(t, h):
        R = R_mean + 0.0003 * np.sin(2 * np.pi * t / 365)
        ET = ET_mean + 0.001 * np.sin(2 * np.pi * t / 365)
        return (R - ET - T / 500**2 * (h - 85.0)) / S_y

    sol = solve_ivp(dhdt, (0, 3*365), [h_init], t_eval=np.linspace(0, 3*365, 500))
    return sol.t, sol.y[0]

# Monte Carlo: 1000 futtatas veletlenszeru parameterekkel
np.random.seed(42)
n_runs = 1000
results = []

for _ in range(n_runs):
    S_y_rand = np.random.normal(0.15, 0.03)       # 20% bizonytalansag
    T_rand = np.random.lognormal(np.log(100), 0.3) # log-normal eloszlas
    R_rand = np.random.normal(0.001, 0.0002)
    ET_rand = np.random.normal(0.0015, 0.0003)
    h_init_rand = np.random.normal(86.0, 0.5)

    t, h = run_simulation(S_y_rand, T_rand, R_rand, ET_rand, h_init_rand)
    results.append(h)

results = np.array(results)

# Abrazolas: mediab es konfidencia-sav
import matplotlib.pyplot as plt

t_plot = np.linspace(0, 3*365, 500) / 365
median = np.median(results, axis=0)
p5 = np.percentile(results, 5, axis=0)
p95 = np.percentile(results, 95, axis=0)

fig, ax = plt.subplots(figsize=(12, 5))
ax.fill_between(t_plot, p5, p95, alpha=0.3, color='blue', label='90% konfidencia')
ax.plot(t_plot, median, 'b-', linewidth=2, label='Median')
ax.set_xlabel('Ido [ev]')
ax.set_ylabel('Talajvizszint [m]')
ax.set_title('Monte Carlo szimulacio -- parameter-bizonytalansag')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

Ez a megkozelites azonnal megmutatja, mennyire erzekeny a modelled az egyes parameterekre -- es megadja az eredmeny bizonytalansagat, amit a determinisztikus megoldas onmagaban nem tud.

### 6.4.3 Agens-alapu modellek (ABM)

Az agens-alapu modellezesnel a rendszert **egyedek** (agensek) egyuttmukodesekeent irjuk le, nem egyenletekkel. Minden agens sajat szabalyok szerint viselkedik, es a rendszer emergens viselkedese "alurol felfelé" alakul ki.

Pelda alkalmazasok:
- **Okologia:** egyedek mozgasa, szaporodasa, kompeticioja egy elohelyen
- **Jarvabytan:** SIR-szeru modellek, ahol minden szemely onallo agens
- **Mezogazdasag:** parcellak, gazdak dontesi -- hogyan terjed egy uj vetomag

Az AI kitunoen segit ABM-ek generälasaban, mert a szabalyokat termeszetes nyelven irod le, es az AI leforditja koddá. A legnepszerubb Python csomag erre a **Mesa**:

```python
# Agens-alapu modell vazlata Mesa-val
# (Az AI konnyen generalja a teljes kodot, ha a szabalyokat leirod)
from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid

class FarmerAgent(Agent):
    """Egy gazda, aki dontest hoz a vetesrol."""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.crop = 'buza'       # jelenlegi nOveny
        self.profit = 0

    def step(self):
        # Megnezi a szomszedok nyeresegessegét
        neighbors = self.model.grid.get_neighbors(self.pos, moore=True)
        # Ha a szomszedok tobsege napraforgot termel es jobban jar...
        # ...o is valt (egyszerusitett dontes)
        pass  # Az AI kitolti a reszleteket
```

> **Tipp:** Mondd az AI-nak: "Szeretnek egy agens-alapu modellt Mesa-val, ahol [a szabalyokat ird le termeszetes nyelven]." Az AI legeneralja a teljes implementaciot.

### Melyik szimulaciotipust valaszd?

| Kerdes | Valasz | Ajanlott tipus |
|--------|--------|----------------|
| Ismert-e a fizikai torveny? | Igen | Determinisztikus ODE/PDE |
| Fontosak-e az egyedi kulonbsegek? | Igen | Agens-alapu |
| Van-e jelentos parameter-bizonytalansag? | Igen | Monte Carlo |
| A viselkedes "alurol" alakul ki? | Igen | Agens-alapu |
| Gyors valaszra van szukseg? | Igen | Determinisztikus |

> **🌾 Szakterületi példa: Növénynövekedési modellek mint DSS-eszközök**
>
> A mezőgazdasági döntéstámogatásban a folyamat-alapú növénynövekedési modellek (DSSAT CERES, APSIM) matematikai egyenletekkel szimulálják a növény fejlődését — a fotoszintézistől a biomassza-felhalmazódáson át a szemtelítődésig. Ezek a determinisztikus modellek fizikai és fiziológiai törvényekre építenek, és a növény válaszát a környezeti tényezőkre (hőmérséklet, sugárzás, vízellátás) írják le. Az AI-asszisztens segíthet a modell felállításában, a számos paraméter beállításában és az eredmények értelmezésében, különösen ott, ahol a fizikai modell nem adekvát és gépi tanulási kiegészítés szükséges.
>
> *Forrás: precagri 16.3 „Növénynövekedési modellek mint döntéstámogató eszközök"*

---

## 6.5 Automatikus modell-kalibracio

Az egyik legidoigenyesebb feladat a modellezesben: **a parametereket ugy beallitani, hogy a modell a meresekre illeszkedjen.** Ezt hívjuk *kalibraciőnak* vagy *inverz modellezesnek*.

Hagyomanyosan ezt "szemre" vagy szisztematikus racs-keresessel (grid search) csinálják -- de sokkal jobb modszerek leteznek.

### 6.5.1 Optuna -- automatikus hiperparameter-optimalizalas

Az **Optuna** egy Python konyvtar, amit eredetileg gepi tanulashoz fejlesztettek, de barmelyik modell kalibralasara kivaloan hasznalhato. Bayesi optimalizalast hasznal: tanulja meg, hogy a parameterter melyik resze az igéretes, és oda koncentralja a keresest.

### Dolgozott pelda: Talajvizmodell kalibracioja Optuna-val

Tegyuk fel, hogy Martanak vannak mert talajvizszint-adatai (havi felbontasban, 3 evre), es szeretne az $S_y$, $T$, es $h_0$ parametereket ugy beallitani, hogy a modell illeszkedjen a meresekre.

---

**Te:**
> Van egy talajvizszint-modellem (ODE) es mert adataim. Szeretnem a modell parametereit (S_y, T, h0) automatikusan kalibralni Optuna-val, minimalizalva az RMSE-t a mert es modellezett vizszintek kozott. Irj komplett kodot.

**Claude:**

```python
import numpy as np
import optuna
from scipy.integrate import solve_ivp

# Szintetikus "mert" adatok (a gyakorlatban: valós meresek)
np.random.seed(123)
t_mert = np.linspace(0, 3 * 365, 36)  # havi pontok, 3 ev
h_mert = 85.5 + 0.8 * np.sin(2 * np.pi * t_mert / 365) + \
         np.random.normal(0, 0.1, len(t_mert))

# Havi forcirozas (ismert)
R_havi = np.array([0.0005, 0.0008, 0.0015, 0.0020, 0.0018,
                   0.0010, 0.0005, 0.0003, 0.0006, 0.0010,
                   0.0008, 0.0005])
ET_havi = np.array([0.0001, 0.0002, 0.0005, 0.0010, 0.0020,
                    0.0030, 0.0035, 0.0030, 0.0015, 0.0005,
                    0.0002, 0.0001])

def simulate(S_y, T, h0):
    """Futtasd a modellt adott parameterekkel."""
    def dhdt(t, h):
        honap = int(t % 365 / 30.44) % 12
        R = R_havi[honap]
        ET = ET_havi[honap]
        return (R - ET - T / 500**2 * (h[0] - h0)) / S_y

    sol = solve_ivp(dhdt, (0, 3*365), [86.0], t_eval=t_mert, method='RK45')
    return sol.y[0]

def objective(trial):
    """Optuna celoevenyfuggveny."""
    S_y = trial.suggest_float('S_y', 0.01, 0.40)
    T = trial.suggest_float('T', 10, 500, log=True)
    h0 = trial.suggest_float('h0', 80, 90)

    h_modell = simulate(S_y, T, h0)

    if h_modell is None or len(h_modell) != len(h_mert):
        return 1e6  # sikertelen szimulacio buntetest kap

    rmse = np.sqrt(np.mean((h_modell - h_mert)**2))
    return rmse

# Optimalizalas
optuna.logging.set_verbosity(optuna.logging.WARNING)
study = optuna.create_study(direction='minimize')
study.optimize(objective, n_trials=200)

# Eredmenyek
print(f"Legjobb RMSE: {study.best_value:.4f} m")
print(f"Legjobb parameterek:")
for key, value in study.best_params.items():
    print(f"  {key} = {value:.4f}")

# Abrazolas: mert vs. kalibralt modell
import matplotlib.pyplot as plt

h_best = simulate(**study.best_params)

fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(t_mert / 365, h_mert, 'ko', markersize=5, label='Mert')
ax.plot(t_mert / 365, h_best, 'r-', linewidth=2, label='Kalibralt modell')
ax.set_xlabel('Ido [ev]')
ax.set_ylabel('Talajvizszint [m]')
ax.set_title('Automatikus modell-kalibracio Optuna-val')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

> **🌾 Szakterületi példa: Az LSTM-cella matematikája az árvíz-előrejelzésben**
>
> Az árvíz-előrejelzésben az LSTM-hálózat kapu-mechanizmusa (felejtő-, bemeneti és kimeneti kapu) lehetővé teszi, hogy a hálózat a gyors felszíni lefolyást és a lassú alapvízhozam-komponenst egyszerre tanulja meg. A felejtő kapu egyenlete: $f_t = \sigma(W_f \cdot [h_{t-1}, x_t] + b_f)$, a cellaállapot frissítése: $C_t = f_t \odot C_{t-1} + i_t \odot \tilde{C}_t$. A kalibrációs célfüggvény az NSE-veszteségfüggvény, amely az árvízi csúcsokra fókuszálja a tanítást. Ez a matematikai struktúra az automatikus kalibrációval (mint az Optuna fent) kombinálva hatékony eszközt ad a hidrológus kezébe.
>
> *Forrás: hidrogis 23.1.1 „Miért alkalmasak a rekurrens hálózatok a vízhozam-előrejelzésre?"*

---

### 6.5.2 Erzekenyseqvizsgalat

A kalibracio utan a kovetkezo kerdes: **melyik parameterre a legerzekenyebb a modell?** Ez megmutatja, hol erdemes pontosabb mereseket vegezni, es melyik parameterek bizonytalansaga a legkritikusabb.

A **SALib** (Sensitivity Analysis Library) konyvtar implementalja a legnepszerubb modszereket:

```python
from SALib.sample import saltelli
from SALib.analyze import sobol

# Parameter-definicio
problem = {
    'num_vars': 3,
    'names': ['S_y', 'T', 'h0'],
    'bounds': [[0.05, 0.35], [20, 400], [82, 88]]
}

# Mintak generalasa (Sobol-sorozat)
param_values = saltelli.sample(problem, 1024)

# Modell futtatasa minden mintapontra
Y = np.array([
    np.sqrt(np.mean((simulate(p[0], p[1], p[2]) - h_mert)**2))
    for p in param_values
])

# Sobol-indexek szamitasa
Si = sobol.analyze(problem, Y)

print("Elsorendu erzekenysg-indexek (S1):")
for name, s1 in zip(problem['names'], Si['S1']):
    print(f"  {name}: {s1:.3f}")

print("\nTeljes hatas (ST):")
for name, st in zip(problem['names'], Si['ST']):
    print(f"  {name}: {st:.3f}")
```

A **Sobol-indexek** ertelmezese:
- **S1** (elsorendu): a parameter onmagaban hany %-at magyarazza a kimenet varianciajanak
- **ST** (teljes hatas): a parameter es osszes kolcsonhatasa egyutt

> Ha S1 kozel van ST-hez, a parameter onalloan hat. Ha ST >> S1, fontos kolcsonhatasok vannak mas parameterekkel.

### 6.5.3 Bayesi kalibracio

A Bayesi megkozelites **nem egyetlen legjobb parameterkeszletet** ad, hanem a parameterek **posteriori eloszlasat** -- megmutatja, milyen parameterertekek osszeegyeztethetok a meresekkel.

Erre a **PyMC** konyvtar a legjobb valasztas:

```python
import pymc as pm

with pm.Model() as model:
    # Prior eloszlasok (elozetes tudasunk a parameterekrol)
    S_y = pm.TruncatedNormal('S_y', mu=0.15, sigma=0.05, lower=0.01, upper=0.5)
    T = pm.Lognormal('T', mu=np.log(100), sigma=0.5)
    h0 = pm.Normal('h0', mu=85, sigma=2)

    # Modell futtatas (egyszerusitett pelda)
    h_eq = h0 + (0.001 - 0.0015) * 500**2 / T
    h_pred = h_eq + (86 - h_eq) * pm.math.exp(-T / (S_y * 500**2) * t_mert)

    # Likelihood: a meresek zajosak
    sigma_obs = pm.HalfNormal('sigma', sigma=0.5)
    obs = pm.Normal('obs', mu=h_pred, sigma=sigma_obs, observed=h_mert)

    # Mintavetel
    trace = pm.sample(2000, tune=1000, cores=4)

# Eredmenyek
pm.summary(trace, var_names=['S_y', 'T', 'h0'])
pm.plot_posterior(trace, var_names=['S_y', 'T', 'h0'])
```

**Mikor melyiket hasznald?**

| Modszer | Erosseg | Mikor hasznald |
|---------|---------|----------------|
| Optuna | Gyors, robust, konnyu | Legjobb illesztes kell, sok parameter |
| Bayesi (PyMC) | Bizonytalansagot is ad | Fontos a parameter-bizonytalansag |
| SALib | Erzekenyseqet mutatja | Melyik parameter szamit leginkabb? |

---

## 6.6 Osszefoglalo: A modellezesi munkafolyamat AI-val

Fogalmazzuk meg a teljes munkafolyamatot, amit ebben a fejezetben megtanultal:

```
1. KERDES       --> "Hogyan viselkedik a rendszerem?"
      |
2. MODELL       --> AI segit az egyenlet megtalálásában, levezetesben
      |              (prompt: "Milyen egyenlet irja le...?")
      |
3. ELLENORZES   --> SymPy: dimenzioelemzes, analitikus ellenorzes
      |              (prompt: "Ellenorizd az egyenletet SymPy-val")
      |
4. IMPLEMENTACIO --> AI leforditja koddá
      |              (prompt: "Implementald Python-ban solve_ivp-vel")
      |
5. KALIBRACIO   --> Optuna / PyMC illesztes mert adatokra
      |              (prompt: "Kalibráld a modellt Optuna-val")
      |
6. ERZEKENYSG   --> SALib Sobol-indexek
      |              (prompt: "Melyik parameter a legfontosabb?")
      |
7. FUTATAS       --> Monte Carlo, szcenariok
                     (prompt: "Futtass 1000 Monte Carlo szimulaciot")
```

Ebben a munkafolyamatban az AI nem helyettesit -- **segit**. Te mondod meg, mi a kerdes, milyen fizika van mogotte, es mi a celod. Az AI fordit, implemental, es ellenorz. A szakmai dontes mindig a tied.

---

---

# Halado szekciok

---

## :microscope: Haladornak: Egyenlet-felfedezes PySR-rel

> *Ez a szekció azoknak szol, akik mar jartasak a modellezesben es szeretnenek az AI-t nem csak implementalasra, hanem uj osszefuggesek felfedezesere hasznalni. Nyugodtan ugord at, ha a fejezet elso resze eleg neked.*

### A problema

Mi van, ha **nem ismered az egyenletet**, ami leirja a rendszeredet? Vannak adataid (meres, szimulacio), es szeretned megtalalni a legegyszerubb matematikai formulat, ami reprodukalja oket.

Ez a **szimbolikus regresszio**: ahelyett, hogy egy adott formaju fuggvenyt illesztel (pl. linearis regresszio), az algoritmus **maga keresi a fuggveny formajat** is.

### PySR: evolucionalisan keres matematikai kifejezeseket

A **PySR** (Python Symbolic Regression) Miles Cranmer csomagja, ami genetikus programozast hasznal: "kifejezéseket tenyeszt" -- kiválogatja a jol teljesitőket, mutálja és keveri oket, mig egyre jobb formulakat talal.

```python
from pysr import PySRRegressor
import numpy as np

# Pelda: Kepler harmadik torvenye adatokbol
# T^2 = (4*pi^2 / GM) * r^3
np.random.seed(42)
r = np.random.uniform(0.5, 10, 100)
GM = 4 * np.pi**2  # normalizalt egysegek
T = np.sqrt(r**3 / GM) * (1 + np.random.normal(0, 0.01, 100))

# PySR futtatasa
model = PySRRegressor(
    niterations=50,
    binary_operators=["+", "-", "*", "/"],
    unary_operators=["sqrt", "square", "cube"],
    populations=20,
    maxsize=20,
    loss="loss(prediction, target) = (prediction - target)^2",
)

model.fit(r.reshape(-1, 1), T)

# Eredmeny: a legjobb talalt kifejezesek
print(model)
# Tipikus eredmeny:
# Complexity  Loss      Equation
# 1           0.245     sqrt(x0)
# 3           0.0012    0.159 * x0^1.5
# 5           0.00001   sqrt(x0^3) / 6.28
```

A PySR **Pareto-frontra** rendezi az eredmenyeket: megmutatja a kompromisszumot a **pontossag** es az **egyszerseg** kozott. A legegyszerubb jo formula altalaban a fizikailag ertelmes.

### Mikor hasznos a PySR?

- **Felfedező tudomany:** uj osszefuggesek keresese meresekbol
- **Modell-egyszerusites:** egy komplex szimulacio eredmenyet egyszerub keplettel kozelited
- **Ismeretlen fizika:** fenomenologikus osszefuggesek azonositasa
- **Dimenzio-elemzes alternativaja:** az algoritmus megtalálja a fizikailag helyes kombinaciokat

### Gyakorlati tippek

1. **Normalizald az adatokat:** a PySR jobban mukodik, ha a valtozok nagysagrendje hasonlo
2. **Add meg a fizikai operatorokat:** ha tudod, hogy gyokvonas / negyzeteles / hatvanyozas fontos, add meg unary_operators-kent
3. **Hasznald a `select_k_features` parametert** sok valtozo eseten, hogy elOszor kivalogasson
4. **Eredmenyt mindig ellenorizd:** a talalt formula fizikailag ertelmes-e? Dimenzio stimmel-e?

---

## :microscope: Haladornak: LLM-vezérelt szimbolikus regresszio fizikai prior-okkal

### Az otlet

A PySR "vakon" keres -- nem tud a fizikai torvenyekrol. De mi van, ha az LLM **elozetes fizikai tudasat** kombinalod a szimbolikus keresessel?

A legujabb megkozelites (2024-2025):

1. **LLM javasol kepletformakat:** "A gravitacio valoszinuleg hatvanytorveny a tavolsag fuggvenyeben"
2. **Szimbolikus regresszio finomit:** a javasolt formakbol kiindulva keresi a pontos egyutthatokat es kitevOket
3. **LLM ertelmez:** "Ez a Kepler harmadik torvenye, ami kovetkezik Newton gravitacios torvenyebol"

### Gyakorlatban

```
# Prompt az LLM-nek:
Van egy adatsorom: [x: tavolsag a csillaptol, y: keringesi ido].
Az adatokra a kovetkezo kifejezeseket illesztettem PySR-rel:
  - y = 0.159 * x^1.5
  - y = sqrt(x^3) / 6.28

Kerdes:
1. Van-e ismert fizikai torveny, ami ezt az osszefuggest predikalja?
2. Mi a 6.28 fizikai jelentese?
3. Milyen egyeb valtozokat erdemes bevonnom, hogy pontosabb legyen?
```

Az LLM valasza azonnal megmondja: "Ez Kepler harmadik torvenye, a 6.28 = 2*pi, es a GM = 4*pi^2 ertekbol szarmazik normalizalt egysegekben."

Ez a **kozbeszuros megkozelites** (human-in-the-loop, de LLM-in-the-loop) robban a szimbolikus regresszió hatekonysagat, mert:

- Szukiti a keresesi teret fizikailag ertelmes iranyokba
- Dimenzio-konzisztenciat kenyszerit ki
- Fizikai ertelmet ad a numerikus konstansoknak

---

## :microscope: Haladornak: Fizika-informalt neuralis halozatok (PINNs)

### Mi az a PINN?

A **Physics-Informed Neural Network** (PINN) egy meroenleg masfelé megkozelites: ahelyett, hogy a PDE-t numerikusan discretizalod (veges differenciák, veges elemek), egy **neurálist halozatot tanitasz ugy, hogy teljesitse a differencialeqyenletet**.

Hogyan mukodik:

1. A halozat bemenete: $(x, t)$ koordinatak
2. A halozat kimenete: $u(x, t)$ -- a megoldas
3. A veszteségfuggveny harom reszbol all:
   - **PDE rezidum:** beteszed a halozat kimenetét a differencialeqyenletbe (automatikus differencialassal kiszamolod a derivaltakat), es buntetéd, ha nem nulla
   - **Peremfelteteli hiba:** a halozat kimenete a pereméken egyezzen a feltetelekkel
   - **Adatillesztes:** (opcionalis) mert pontokban egyezzen a meresekkel

$$\mathcal{L} = \underbrace{\frac{1}{N_r} \sum_{i=1}^{N_r} |f(x_i, t_i)|^2}_{\text{PDE rezidum}} + \underbrace{\frac{1}{N_b} \sum_{j=1}^{N_b} |u(x_j, t_j) - g_j|^2}_{\text{Peremfeltetel}} + \underbrace{\frac{1}{N_d} \sum_{k=1}^{N_d} |u(x_k, t_k) - u_k^{obs}|^2}_{\text{Meresek}}$$

### Pelda: Diffuzio-egyenlet PINN-nel

```python
import torch
import torch.nn as nn

class PINN(nn.Module):
    def __init__(self, layers=[2, 64, 64, 64, 1]):
        super().__init__()
        self.net = nn.Sequential()
        for i in range(len(layers) - 1):
            self.net.append(nn.Linear(layers[i], layers[i+1]))
            if i < len(layers) - 2:
                self.net.append(nn.Tanh())

    def forward(self, x, t):
        inputs = torch.cat([x, t], dim=1)
        return self.net(inputs)

def physics_loss(model, x, t, alpha=0.01):
    """A PDE-t kenyszeritjuk ki."""
    x.requires_grad_(True)
    t.requires_grad_(True)

    u = model(x, t)

    # Elso es masodik deriváltak automatikus differencialassal
    u_t = torch.autograd.grad(u, t, grad_outputs=torch.ones_like(u),
                               create_graph=True)[0]
    u_x = torch.autograd.grad(u, x, grad_outputs=torch.ones_like(u),
                               create_graph=True)[0]
    u_xx = torch.autograd.grad(u_x, x, grad_outputs=torch.ones_like(u_x),
                                create_graph=True)[0]

    # PDE rezidum: u_t - alpha * u_xx = 0
    residual = u_t - alpha * u_xx
    return torch.mean(residual**2)

# Tanitas (vazlat)
model = PINN()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

for epoch in range(10000):
    # Veletlenszeru kollokacios pontok a tartomanyban
    x_coll = torch.rand(1000, 1)
    t_coll = torch.rand(1000, 1) * 2.0

    # Peremfeltetel-pontok
    x_bc_left = torch.zeros(100, 1)
    t_bc = torch.rand(100, 1) * 2.0
    u_bc_left = torch.ones(100, 1) * 100.0  # bal perem: 100 C

    # Veszteseg
    loss_pde = physics_loss(model, x_coll, t_coll)
    loss_bc = torch.mean((model(x_bc_left, t_bc) - u_bc_left)**2)

    loss = loss_pde + 10 * loss_bc
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
```

### Mikor hasznos a PINN?

| Szituacio | PINN elonye |
|-----------|------------|
| **Inverz problema:** ismert a PDE de ismeretlen parameterek | A PINN egyszerre oldja meg es kalibrálja |
| **Hianyos adatok:** nehany mert pont + fizikai torveny | A PDE kiegesziti az adatot |
| **Komplex geometria:** ahol a racs generalasa nehez | Mesh-free: veletlenszeru pontokban ertekeli |
| **Multi-fizika:** tobb csatolt egyenlet | Termeszetesen kezeli a csatolast |

### Korlatok

- A tanitas nem triviáls: gyakran kell a vesztesegfuggveny sulyozasat hangolni
- Nem helyettesiti a klasszikus solvereket egyszerubb feladatoknal
- Skálazhatosag nagy 3D problemaknal meg kerdéses
- A meresek helyen pontos, de tavolabb pontatlanabb lehet

> **Tipp az AI hasznalatahoz:** A PINN implementacio komplex. Kerd az AI-t, hogy a **DeepXDE** vagy **NVIDIA Modulus** konyvtarat hasznalja -- ezek sokkal egyszerubbre redukalják a feladatot:
>
> "Implementálj egy PINN-t DeepXDE-vel, ami megoldja az 1D hoegyenletet alpha = 0.01-gyel, Dirichlet peremfeltételekkel."

---

## :microscope: Haladornak: Szurrogat modellek draga szimulációkhoz

### A problema

Van egy komplex szimulacod (pl. elementes modell, CFD, klimamodell), ami egyetlen futassal orat vagy napokat vesz igenybe. Es neked ezer futásra lenne szukséged (Monte Carlo, kalibracio, erzekenysgvizsgalat).

### A megoldasas: szurrogat modell

A **szurrogát modell** (surrogate model, emulator, metamodel) a draga szimulacio *olcso kozelitese*:

1. Futtasd a draga szimulaciot nthany szaz vagy ezer "treningpontra" (gondosan valasztott parameterekkel)
2. Tanitsd a szurrogat modellt ezekre a pontokra
3. Hasznald a szurrogatot a tobb ezres/milliós kivaluálasokhoz

### Tipikus szurrogat-architekturak

| Modszer | Mikor hasznald |
|---------|---------------|
| **Gauss-folyamat regresszio (GPR)** | Keves treningpont (<500), bizonytalansag-becslés kell |
| **Neuralis halozat** | Sok treningpont, gyors kivaluálas kell |
| **Polinom kaosz-kifejtés (PCE)** | Erzekenysgvizsgálathoz, alacsony dimenzioban |
| **Random forest / XGBoost** | Gyors es robust, de nem ad gradienst |

### Pelda: Gauss-folyamat szurrogat

```python
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import Matern
import numpy as np

# "Draga szimulacio" -- a gyakorlatban ez a tenyleges modell
def expensive_simulation(params):
    S_y, T, h0 = params
    # ... (a teljes ODE megoldas ide jon) ...
    # Visszaad egy skalart: pl. az RMSE-t vagy az atlagos vizszintet
    result = h0 + (0.001 - 0.0015) * 500**2 / T  # egyszerusitett pelda
    return result

# Treningpontok Latin Hypercube mintavetelezéssel
from scipy.stats.qmc import LatinHypercube
sampler = LatinHypercube(d=3, seed=42)
sample = sampler.random(n=100)

# Skálázás a fizikai tartomanyra
bounds = np.array([[0.05, 0.35], [20, 400], [82, 88]])
X_train = sample * (bounds[:, 1] - bounds[:, 0]) + bounds[:, 0]
y_train = np.array([expensive_simulation(x) for x in X_train])

# Gauss-folyamat illesztes
kernel = Matern(nu=2.5)
gpr = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=10)
gpr.fit(X_train, y_train)

# Predikcio (milliszekundumok a draga szimulácio orai helyett)
X_test = np.array([[0.15, 100, 85]])
y_pred, y_std = gpr.predict(X_test, return_std=True)
print(f"Predikcio: {y_pred[0]:.3f} +/- {y_std[0]:.3f}")
```

A **Gauss-folyamat szurrogat** kulonosen ertékes, mert:
- Megadja a predikcio **bizonytalansagat** ($\pm \sigma$)
- Ahol nagy a bizonytalansag, ott erdemes ujabb treningpontot futtatni (**aktiv tanulás**)
- Alacsonydimenzioban (5-10 parameter) kivaloan mukodik

### Szurrogat modellek AI-val

Az AI segitsege itt is nagy:

```
Van egy draga szimulacióm, ami [x] parameterből [y] kimenetet szamol.
Egy futtatas [z] percig/oraig tart. Osszesen [n] futast engedhetek meg.

Kerlek:
1. Tervezz Latin Hypercube mintavetelezest
2. Epitsd a szurrogatot Gauss-folyamat regresszioval
3. Validáld: mennyire pontos a szurrogatat?
4. Hasznald Monte Carlo szimulaciohoz
```

---

## Összefoglalás és továbblépés

> **🖼️ Ábra: A fejezet modellezési technikáinak döntési fája**
> *Döntési fa: "Milyen típusú a problémád?" → Analitikus megoldás (SymPy) / Numerikus szimuláció (SciPy) / Kalibráció (scipy.optimize) / Érzékenységvizsgálat (SALib) / Egyenletfelfedezés (PySR). Minden ágon példa-probléma.*


Ebben a fejezetben megismerted, hogyan hasznalhatod az AI-t a teljes matematikai modellezesi folyamatban:

- **Modell-keresés:** az AI segit megtalalni a megfelelo egyenletet a kutatasi kerdesedhez
- **Szimbolikus ellenorzes:** SymPy-val levezeted, egyszerusited, dimenziot ellenorzod
- **Numerikus implementacio:** az AI leforditja az egyenletet Python kodra (ODE: `solve_ivp`, PDE: veges differenciák, optimalizalas: `scipy.optimize`)
- **Szimulacio:** determinisztikus, Monte Carlo, vagy agens-alapu -- a kerdes dönti el
- **Kalibracio:** Optuna automatikus parameter-optimalizalas, SALib erzekenysgvizsgalat, PyMC Bayesi módszerek
- A halado szekcsiokban latkattad, hogyan fedezhet fel az AI **uj egyenleteket** (PySR), hogyan epithetők **fizika-informalt neuralis halozatok** (PINN), es hogyan gyorsitod meg a szimulaciot **szurrogat modellekkel**.

A kovetkezo fejezetben (7. fejezet: Adat-pipeline-ok és automatizálás) megtanulod, hogyan epitsd be ezeket a szimulaciookat automatizalt munkafolyamatokba -- hogy ne kézzel kelljen futtatni minden egyes szcenariot.

---

## Hasznos csomagok és források

> **🖼️ Ábra: A tudományos Python-csomagok kapcsolati térképe modellezéshez**
> *Hálózati diagram: SymPy, SciPy, NumPy, Matplotlib, SALib, PySR, Mesa, DeepXDE csomagok és azok tipikus felhasználási területei, összekötő vonalakkal.*


| Csomag | Cel | Telepites |
|--------|-----|-----------|
| **SciPy** | ODE/PDE megoldas, optimalizalas | `pip install scipy` |
| **SymPy** | Szimbolikus szamitas | `pip install sympy` |
| **Optuna** | Automatikus kalibracio | `pip install optuna` |
| **SALib** | Érzékenységvizsgalat | `pip install SALib` |
| **PyMC** | Bayesi kalibracio | `pip install pymc` |
| **Mesa** | Agens-alapu modellezes | `pip install mesa` |
| **PySR** | Szimbolikus regresszio | `pip install pysr` |
| **DeepXDE** | PINNs egyszeruen | `pip install deepxde` |

**Konyvek es cikkek:**

- Cranmer, M. (2023). *Interpretable Machine Learning for Science with PySR and SymbolicRegression.jl.* arXiv:2305.01582
- Raissi, M., Perdikaris, P., Karniadakis, G.E. (2019). *Physics-informed neural networks.* Journal of Computational Physics, 378, 686-707.
- Akiba, T. et al. (2019). *Optuna: A Next-generation Hyperparameter Optimization Framework.* KDD 2019.
- Herman, J., Usher, W. (2017). *SALib: An open-source Python library for Sensitivity Analysis.* JOSS, 2(9), 97.
- Meurer, A. et al. (2017). *SymPy: symbolic computing in Python.* PeerJ Computer Science, 3, e103.
