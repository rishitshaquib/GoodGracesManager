# Good Grace's Cafe: Recipes and Drink Diagrams

Grace Hopper College, Entryway D. Updated October 22, 2026.

This file has two parts. Part 1 is every recipe on the bar sheets, written out step by step with cost and margin. Part 2 is the code that adds a **Drink diagrams** section to the Management Portal (`index.html` in this folder): a button for every drink on the menu that opens its cup diagram when clicked.

Recipes come from the bar sheets (iced, hot, batch prep and cup codes). Costs come from the COGS model: WebstaurantStore invoices, BJ's shelf prices for dairy, cider, strawberries and sugar, and house syrups at the average Monin invoice rate. Every cost per cup includes the cup, lid and napkin, plus a sleeve on hot drinks.

---

## Part 1: Recipes

### How every drink is built

Every drink is a base build with one or two slots swapped. A specialty drink keeps the structure of its base and changes an ingredient: the Banana Bread Latte is an iced latte with house syrup in the syrup slot, the Strawberry Matcha is an iced matcha with purée under the ice. Because the structure stays the same, a new specialty drink only needs its swapped ingredient costed.

| Base build | Order, bottom of the cup to the top |
|:--|:--|
| Iced espresso | Syrup, espresso, ice, milk or water to the line |
| Iced shaker | Syrup and espresso (or concentrate) in the shaker with milk or ice, pour, top off |
| Iced matcha | Ice, milk to a little under the line, matcha mix weighed in last |
| Hot espresso | Syrup, espresso, steamed milk |
| Hot tea or concentrate | Syrup or concentrate, hot water or tea, steamed milk |

Cups: 16 oz clear cup for iced, 12 oz double wall cup for hot.

### Before you build

1. Read the whole label: drink, syrup, milk, add-ons.
2. No milk code means 2% milk. `/O` is oat, `/A` is almond.
3. Added syrup on any iced drink is 2 pumps.
4. `+CF` cold foam goes on top, last. It contains dairy, even on an oat or almond drink.
5. `+SP` strawberry purée goes in the cup first.
6. Match the drink to the label before handoff.
7. Allergies: tell the bar and the shift lead directly. A milk code does not flag an allergy.

### Cup codes

Write codes in clear capital letters in this order: **drink, syrup, milk, add-ons**.

| Drink | Code | | Syrup | Code | | Milk and add-ons | Code |
|:--|:--|:--|:--|:--|:--|:--|:--|
| Espresso | ESP | | Vanilla | +V | | Regular 2% | none |
| Latte | LAT | | Brown sugar | +B | | Oat | /O |
| Cappuccino | CAP | | Pumpkin spice | +P | | Almond | /A |
| Americano | AME | | Hazelnut | +H | | Cold foam (dairy) | +CF |
| Brown sugar oat shaken espresso | BSOE | | Caramel | +C | | Strawberry purée | +SP |
| Banana bread latte | BBL | | Simple syrup | +S | | | |
| Chai | CHAI | | | | | | |
| Matcha | MAT | | | | | | |
| Strawberry matcha | SMAT | | | | | | |
| London fog | FOG | | | | | | |
| Caramel apple cider | CID | | | | | | |

Examples: `LAT +V /O +CF` is a vanilla latte with oat milk and cold foam. `BSOE +CF` is a shaken espresso with cold foam (BSOE already includes brown sugar and oat milk). `LAT +V` is a vanilla latte with regular 2% milk.

### Iced drinks

Steps are numbered in the order you do them.

#### Iced Latte (plain or flavored)

1. 2 pumps syrup (flavored only; skip for a plain latte)
2. Espresso shot
3. 2 scoops ice
4. Milk to the line

$4.50 · cost $0.92 · margin 79.6%

#### Iced Americano

1. Espresso shot
2. 2 scoops ice
3. Water to the line
4. Splash of milk if requested

Leave room above the line for milk. $3.50 · cost $0.72 · margin 79.6%

#### Brown Sugar Oat Shaken Espresso (BSOE)

In the shaker:
1. 2 pumps brown sugar syrup
2. Espresso shot over the syrup
3. 2.5 scoops ice and 1 shake of cinnamon
4. Shake until foamy, pour all of it into the cup

Then:
5. Top with oat milk to the line

$5.00 · cost $1.34 · margin 73.3%

#### Banana Bread Latte (BBL)

In the shaker:
1. 20 g banana bread syrup
2. Espresso shot over the syrup, stir to dissolve
3. 250 mL milk
4. Pour into the cup

Then:
5. Add ice last

The syrup is thick, so stir before adding milk. $5.00 · cost $1.09 · margin 78.1%

#### Iced Chai

1. 2 scoops ice in the cup first

In the shaker:
2. 150 mL chai concentrate
3. 100 mL milk
4. Mix, then pour over the ice

$4.50 · cost $1.31 · margin 70.8%

#### Iced Matcha

1. 2 scoops ice first
2. Milk to a little under the line
3. Zero the scale, add 50 g matcha mix

Zero the scale after the milk, then weigh in the matcha. $5.00 · cost $0.98 · margin 80.4%

#### Strawberry Matcha (SMAT)

1. 30 g strawberry purée
2. 2 scoops ice
3. Milk to a little under the line
4. Zero the scale, add 50 g matcha mix

$5.50 · cost $1.11 · margin 79.8%

### Hot drinks

Lattes use 8 oz of cold milk, steamed. Start every steam with cold milk.

#### Hot Latte (plain or flavored)

1. 2 pumps syrup (flavored only; skip for a plain latte)
2. Espresso shot
3. Steam 8 oz cold milk, pour over the shot

$4.50 · cost $1.02 · margin 77.4%

#### Cappuccino

1. Espresso shot
2. Steam 6 oz milk; it foams up to fill the cup
3. Pour the milk and foam over the shot

$4.00 · cost $0.97 · margin 75.9%

#### Hot Americano

1. Espresso shot
2. Hot water, heated in the kettle
3. Splash of milk if requested

$3.50 · cost $0.81 · margin 76.8%

#### Hot Matcha Latte

1. 50 g matcha mix in the cup
2. Steam 8 oz milk until hot
3. Pour the steamed milk over the matcha

$5.00 · cost $1.13 · margin 77.5%

#### London Fog

1. 1 pump vanilla
2. 3 oz hot water
3. Add the Earl Grey tea bag, let it steep
4. Foam 6 oz milk while it steeps
5. Add the foamed milk

Steep time is still blank on the sheet. $3.50 · cost $0.80 · margin 77.2%

#### Hot Chai

1. 6 oz chai concentrate (room temperature)
2. Steam 6 oz milk (extra hot)
3. Pour the milk over the chai

$4.50 · cost $1.68 · margin 62.8%

#### Caramel Apple Spice Cider (specialty)

1. 1 pump cinnamon syrup
2. Steam 8 oz apple cider, pour in
3. 2 oz cold foam
4. Caramel drizzle

Cold foam contains dairy. This drink is off the hot sheet as a specialty but stays in the portal. $4.50 · cost $0.97 · margin 78.4%

#### Espresso shot

18 g double shot. $1.00 · cost $0.58 · margin 41.7%

### Steaming milk

Start with cold milk. Purge the wand first. When done, steam off, wipe and purge.

- **More foam (cappuccino, London Fog):** tip just under the surface, close to the side of the pitcher. You should hear a steady hiss. Lower the pitcher slowly as the foam rises.
- **Less foam, more heat (lattes, chai):** hiss for only 1 to 2 seconds, then raise the pitcher so the tip sits deeper and off center. The milk should spin quietly.

### Add-ons

| Add-on | Charge | Serving | Cost |
|:--|--:|:--|--:|
| Flavor syrup | $0.25 | 2 pumps (vanilla) | $0.13 |
| Oat milk, hot latte | $0.50 | 8 oz, replaces 2% | $0.71 more than 2% |
| Oat milk, hot chai | $0.50 | 6 oz, replaces 2% | $0.53 more than 2% |
| Oat milk, iced matcha | $0.50 | 175 mL, replaces 2% | $0.52 more than 2% |
| Vanilla cold foam | $0.50 | 2 oz from the batch | $0.21 |
| Strawberry purée | | 30 g | $0.14 |

The $0.50 oat charge loses money on a hot latte and roughly breaks even on chai and iced matcha.

### Batch prep (the day before the weekend)

Checklist:
- Make 2 batches of matcha
- Cook any specialty syrups for the week
- Start the strawberry purée (it sits overnight)
- Batch cold foam (1 container)
- Charge the Clover terminal and the kitchen scales
- Label every prepared item for 2-day expiration: matcha, strawberry, cold foam, specialty syrups

Every label has three lines: **item, prepped, discard**. Discard date is the prep date plus 2 days.

#### Matcha mix (about 700 mL per 50 g)

1. Add 50 g matcha to the shaker slowly through the sieve.
2. Add 200 mL room-temperature water and mix to a paste. Get up the undissolved powder from the bottom.
3. Add 300 mL water to reach 500 mL. Keep mixing until fully mixed.
4. Pour into the matcha squeeze bottle.
5. Add 200 mL water to the shaker to rinse out the excess. Stir again.
6. Pour the rinse into the squeeze bottle.

One batch makes about 14 drinks at 50 g each.

#### Strawberry purée (starts a day early)

Day before:
1. Put 300 g frozen strawberries and 200 g white sugar in a deli container.
2. Leave it overnight.

Next day:
3. Blend with the emulsion blender.
4. Transfer to the squeeze bottle with the cut top.

Used for strawberry matcha (30 g per drink) and `+SP`.

#### Cold foam (one batch = 875 mL)

500 mL heavy cream, 325 mL 2% milk, 50 mL vanilla syrup.

1. Combine the cream, milk and vanilla syrup.
2. Mix using the approved batch method.
3. Transfer to clean, approved containers big enough for 875 mL.
4. Refrigerate and label.

The foaming method is still blank on the sheet.

**Sunday close:** pour out syrups, purées, matcha and cold foam, then wash their containers.

---

## Part 2: Drink diagrams in the Management Portal

### What it does

A **Drink diagrams** tile on the *Menu and recipes* tab shows one button per drink on the menu. Clicking a button opens a dialog with that drink's cup diagram, drawn from data the same way as the bar sheets: layers stacked from the bottom of the cup, numbered steps on the right, an arrow from each step to the layer it lands in, ice cubes, foam, the iced fill line, and the shaker steps bracketed. A drink with both versions shows iced and hot side by side, each with price, cost and margin. A drink with no diagram data shows a disabled button that reads "No diagram yet".

The diagrams are inline SVG drawn with `currentColor`, so outlines and text follow the portal's theme, including dark mode. Drink colors (espresso, milk, matcha) stay fixed.

### How it fits the existing code

The portal is one file, `index.html`, with vanilla JS. The code below uses the helpers it already has: `$` (get by id), `esc` (escape HTML), `norm` (lowercase, letters and digits only), `F.usd2` (money), `S.drinks` (the live menu), and the single `document.addEventListener("click", …)` handler that routes on `data-act`.

Drinks are matched to diagrams by `norm(name)`, so "Chai Latte" finds `chailatte`. Names that differ between the menu and the sheets go in `aliases`. The portal's "Brown Sugar Shaken Espresso" matches the sheet's "Brown Sugar Oat Shaken Espresso" this way.

### Step 1: CSS

Paste before `</style>` (line 669):

```css
.diag-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:8px}
.diag-btn{display:flex;flex-direction:column;align-items:flex-start;gap:2px;text-align:left}
.diag-btn[disabled]{opacity:.45;cursor:default}
.diag-dlg{border:none;border-radius:16px;padding:0;width:min(860px,calc(100vw - 32px));max-height:calc(100vh - 48px);background:var(--tile);color:var(--label);box-shadow:0 10px 40px rgba(0,0,0,.25)}
.diag-dlg::backdrop{background:rgba(0,0,0,.35)}
#diagBody{padding:16px 20px 20px}
.diag-h{display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:8px}
.diag-h h2{margin:0;font-size:20px}
.diag-builds{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,400px));gap:16px;justify-content:center}
.diag-b{border:1px solid var(--sep);border-radius:12px;padding:12px;min-width:0}
.diag-b h3{margin:0 0 6px;font-size:13px;letter-spacing:.06em;text-transform:uppercase;color:var(--label2)}
.cupsvg{width:100%;height:auto;display:block;color:var(--brand);font-family:var(--font)}
.diag-m{display:flex;flex-wrap:wrap;gap:6px 14px;margin-top:8px;font-size:13px;color:var(--label2);font-variant-numeric:tabular-nums}
```

### Step 2: HTML

Paste inside `<section class="pane" id="pane-menu">` (line 1041), as its own tile wherever it should sit in the column:

```html
<div class="sec">
  <div class="tile-h"><h2>Drink diagrams</h2></div>
  <p class="hint" style="margin-top:0">Click a drink to see how it is built.</p>
  <div class="diag-grid" id="diagGrid"></div>
</div>
<dialog id="diagDlg" class="diag-dlg" aria-label="Drink diagram"><div id="diagBody"></div></dialog>
```

### Step 3: JavaScript

Paste after `renderDrinkGrid()` (around line 2545). It holds the recipe data and the drawing code.

```js
/* ---------- drink diagrams (Menu and recipes tab) ----------
   Each build lists its layers from the bottom of the cup to the top.
   h      layer height in px (iced cup is 146 px tall, hot cup 198 px)
   c      fill color; ice:true draws cubes, foam:true draws bubbles, splash:true draws a striped splash
   steps  [[number, text], ...] that land in this layer; opt:true marks a step that is skipped for the plain drink
   group  caption for steps done off the cup (in the shaker), drawn as a bracket
   top    empty space above the last layer; line:true marks the iced fill line there */
const DC = {espresso:"#4A2C17", syrup:"#D99B4E", milk:"#F1E8D6", foam:"#FFFFFF", water:"#D6E8F3",
  matcha:"#8FAE5A", matchaMilk:"#E4E9CF", chaiIced:"#D6A577", chaiHot:"#C88B57", bsoe:"#9C6A3E", oat:"#EDE3CF",
  banana:"#D2AE84", puree:"#E48A90", tea:"#B88F5E", fogMilk:"#EDE4D6", vanilla:"#E3C48A", cider:"#C9853F"};

const DIAGRAMS = {
  latte: {name:"Latte", builds:{
    iced:{price:4.50, cost:0.919, top:10, line:true, note:"Plain latte: skip step 1.", layers:[
      {h:30, c:DC.syrup, steps:[[1,"2 pumps syrup (flavored only)"]], opt:true},
      {h:32, c:DC.espresso, steps:[[2,"Espresso shot"]]},
      {h:38, c:DC.milk, ice:true, steps:[[3,"2 scoops ice"]]},
      {h:36, c:DC.milk, steps:[[4,"Milk to the line"]]}]},
    hot:{price:4.50, cost:1.016, top:12, note:"Plain latte: skip step 1.", layers:[
      {h:46, c:DC.syrup, steps:[[1,"2 pumps syrup (flavored only)"]], opt:true},
      {h:50, c:DC.espresso, steps:[[2,"Espresso shot"]]},
      {h:80, c:DC.milk, steps:[[3,"Steam 8 oz cold milk, pour over the shot"]]},
      {h:10, c:DC.foam, foam:true}]}}},
  cappuccino: {name:"Cappuccino", builds:{
    hot:{price:4.00, cost:0.965, top:10, layers:[
      {h:52, c:DC.espresso, steps:[[1,"Espresso shot"]]},
      {h:72, c:DC.milk, steps:[[2,"Steam 6 oz milk, it foams up to fill the cup"]]},
      {h:64, c:DC.foam, foam:true, steps:[[3,"Pour the milk and foam over the shot"]]}]}}},
  americano: {name:"Americano", builds:{
    iced:{price:3.50, cost:0.716, top:0, line:true, note:"Leave room above the line for milk.", layers:[
      {h:44, c:DC.espresso, steps:[[1,"Espresso shot"]]},
      {h:40, c:DC.water, ice:true, steps:[[2,"2 scoops ice"]]},
      {h:50, c:DC.water, steps:[[3,"Water to the line"]]},
      {h:12, c:DC.milk, splash:true, steps:[[4,"Splash of milk if requested"]]}]},
    hot:{price:3.50, cost:0.813, top:10, layers:[
      {h:56, c:DC.espresso, steps:[[1,"Espresso shot"]]},
      {h:114, c:DC.water, steps:[[2,"Hot water, heated in kettle"]]},
      {h:18, c:DC.milk, splash:true, steps:[[3,"Splash of milk if requested"]]}]}}},
  brownsugaroatshakenespresso: {name:"Brown Sugar Oat Shaken Espresso", aliases:["Brown Sugar Shaken Espresso","BSOE"], builds:{
    iced:{price:5.00, cost:1.335, top:8, line:true, layers:[
      {h:108, c:DC.bsoe, ice:true, group:"IN THE SHAKER", steps:[[1,"2 pumps brown sugar syrup"],[2,"Espresso shot over the syrup"],[3,"2.5 scoops ice + 1 shake cinnamon"],[4,"Shake until foamy, pour ALL in"]]},
      {h:30, c:DC.oat, steps:[[5,"Top with oat milk to the line"]]}]}}},
  bananabreadlatte: {name:"Banana Bread Latte", aliases:["BBL"], builds:{
    iced:{price:5.00, cost:1.094, top:8, line:true, note:"The syrup is thick: stir before adding milk.", layers:[
      {h:104, c:DC.banana, group:"IN THE SHAKER", steps:[[1,"20 g banana bread syrup"],[2,"Espresso shot over the syrup, stir to dissolve"],[3,"250 mL milk"],[4,"Pour into the cup"]]},
      {h:34, c:DC.banana, ice:true, steps:[[5,"Add ice last"]]}]}}},
  chailatte: {name:"Chai Latte", aliases:["Chai"], builds:{
    iced:{price:4.50, cost:1.312, top:10, line:true, layers:[
      {h:44, c:DC.chaiIced, ice:true, steps:[[1,"2 scoops ice in the cup first"]]},
      {h:92, c:DC.chaiIced, group:"IN THE SHAKER", steps:[[2,"150 mL chai concentrate"],[3,"100 mL milk"],[4,"Mix, then pour over the ice"]]}]},
    hot:{price:4.50, cost:1.676, top:14, layers:[
      {h:98, c:DC.chaiHot, steps:[[1,"6 oz chai concentrate (room temp)"]]},
      {h:86, c:DC.milk, steps:[[2,"Steam 6 oz milk (extra hot)"],[3,"Pour the milk over the chai"]]}]}}},
  matchalatte: {name:"Matcha Latte", aliases:["Matcha"], builds:{
    iced:{price:5.00, cost:0.978, top:10, line:true, note:"Zero the scale after the milk, then weigh in the matcha.", layers:[
      {h:42, c:DC.milk, ice:true, steps:[[1,"2 scoops ice first"]]},
      {h:64, c:DC.milk, steps:[[2,"Milk to a little under the line"]]},
      {h:30, c:DC.matcha, steps:[[3,"Zero the scale, add 50 g matcha mix"]]}]},
    hot:{price:5.00, cost:1.127, top:12, layers:[
      {h:66, c:DC.matcha, steps:[[1,"50 g matcha mix in the cup"]]},
      {h:110, c:DC.matchaMilk, steps:[[2,"Steam 8 oz milk until hot"],[3,"Pour the steamed milk over the matcha"]]},
      {h:10, c:DC.foam, foam:true}]}}},
  strawberrymatchalatte: {name:"Strawberry Matcha Latte", aliases:["Strawberry Matcha"], builds:{
    iced:{price:5.50, cost:1.112, top:10, line:true, note:"Zero the scale after the milk, then weigh in the matcha.", layers:[
      {h:26, c:DC.puree, steps:[[1,"30 g strawberry purée"]]},
      {h:30, c:DC.milk, ice:true, steps:[[2,"2 scoops ice"]]},
      {h:54, c:DC.milk, steps:[[3,"Milk to a little under the line"]]},
      {h:26, c:DC.matcha, steps:[[4,"Zero the scale, add 50 g matcha mix"]]}]}}},
  londonfog: {name:"London Fog", builds:{
    hot:{price:3.50, cost:0.797, top:12, teabag:true, note:"Tea: Earl Grey.", layers:[
      {h:30, c:DC.vanilla, steps:[[1,"1 pump vanilla"]]},
      {h:76, c:DC.tea, steps:[[2,"3 oz hot water"],[3,"Add the Earl Grey tea bag, let it steep"]]},
      {h:70, c:DC.fogMilk, steps:[[4,"Foam 6 oz milk while it steeps"]]},
      {h:10, c:DC.foam, foam:true, steps:[[5,"Add the foamed milk"]]}]}}},
  caramelapplespicecider: {name:"Caramel Apple Spice Cider", aliases:["Caramel Apple Cider","CID"], builds:{
    hot:{price:4.50, cost:0.971, top:12, note:"Cold foam contains dairy.", layers:[
      {h:24, c:DC.syrup, steps:[[1,"1 pump cinnamon syrup"]]},
      {h:120, c:DC.cider, steps:[[2,"Steam 8 oz apple cider, pour in"]]},
      {h:30, c:DC.foam, foam:true, steps:[[3,"2 oz cold foam"]]},
      {h:12, c:DC.syrup, splash:true, steps:[[4,"Caramel drizzle"]]}]}}}
};

function diagramFor(d){
  const k = norm(d && d.name);
  if (DIAGRAMS[k]) return DIAGRAMS[k];
  return Object.values(DIAGRAMS).find(x => (x.aliases || []).some(a => norm(a) === k)) || null;
}

/* one build as an inline SVG: cup on the left, numbered steps on the right, arrows to the layer they land in */
function cupSVG(b, temp){
  const hot = temp === "hot", H = hot ? 198 : 146, W = hot ? 96 : 76, inset = hot ? .10 : .14;
  const x0 = 14, y0 = hot ? 24 : 12, lx = x0 + W + 34, VW = 340;
  const xl = y => x0 + W * inset * ((y - y0) / H), xr = y => x0 + W - W * inset * ((y - y0) / H);
  const cup = `M${x0} ${y0} L${x0 + W} ${y0} L${xr(y0 + H)} ${y0 + H} L${xl(y0 + H)} ${y0 + H} Z`;
  const id = "c" + Math.random().toString(36).slice(2, 8);
  let fills = "", deco = "", y = y0 + H;
  const marks = [];                                  // where each layer's steps should point
  b.layers.forEach(L => {
    const top = y - L.h;
    if (L.splash){
      fills += `<pattern id="${id}s${marks.length}" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="10" height="10" fill="#fff"/><rect width="5" height="10" fill="${L.c}"/></pattern><rect x="${x0 - 2}" y="${top}" width="${W + 4}" height="${L.h}" fill="url(#${id}s${marks.length})"/>`;
    } else fills += `<rect x="${x0 - 2}" y="${top}" width="${W + 4}" height="${L.h}" fill="${L.c}"/>`;
    if (L.ice){ const n = Math.max(2, Math.round(L.h / 14));
      for (let i = 0; i < n; i++){ const cx = x0 + W * (.25 + .5 * ((i * .618 + .1) % 1)), cy = top + 8 + (L.h - 16) * ((i + .5) / n);
        deco += `<rect x="${(cx - 6).toFixed(1)}" y="${(cy - 6).toFixed(1)}" width="12" height="12" rx="2" fill="rgba(255,255,255,.55)" stroke="currentColor" stroke-width="1.6" transform="rotate(${(i % 2 ? -1 : 1) * (12 + i * 5)} ${cx.toFixed(1)} ${cy.toFixed(1)})"/>`; } }
    if (L.foam && L.h >= 20){ const n = Math.round(L.h / 9);
      for (let i = 0; i < n; i++){ const cx = x0 + W * (.2 + .6 * ((i * .618 + .3) % 1)), cy = top + 6 + (L.h - 12) * ((i + .5) / n);
        deco += `<circle cx="${cx.toFixed(1)}" cy="${cy.toFixed(1)}" r="${3 + (i % 3)}" fill="#fff" stroke="currentColor" stroke-width="1.2"/>`; } }
    if (!L.foam && !L.splash) fills += `<line x1="${x0}" x2="${x0 + W}" y1="${top}" y2="${top}" stroke="rgba(0,0,0,.12)"/>`;
    if (L.steps) marks.push({L, mid: top + L.h / 2, top, bot: y});
    y = top;
  });
  if (b.line) deco += `<line x1="${x0 - 7}" x2="${x0 + W + 7}" y1="${y0 + b.top}" y2="${y0 + b.top}" stroke="currentColor" stroke-width="2" stroke-dasharray="5 4"/>`;
  if (b.teabag) deco += `<path d="M${x0 + W * .5} ${y0 + H * .55} C${x0 + W * .4} ${y0 + H * .3} ${x0 + W * .25} ${y0 + 6} ${x0 + 4} ${y0 - 10}" fill="none" stroke="currentColor" stroke-width="2.5"/><rect x="${x0 - 8}" y="${y0 - 22}" width="14" height="16" rx="2" fill="#fff" stroke="currentColor" stroke-width="2"/><rect x="${x0 + W * .32}" y="${y0 + H * .55}" width="30" height="36" rx="3" fill="#fff" stroke="currentColor" stroke-width="2"/><rect x="${x0 + W * .32}" y="${y0 + H * .55 + 18}" width="30" height="18" rx="2" fill="currentColor"/>`;
  const lid = hot ? `<rect x="${x0 - 5}" y="${y0 - 11}" width="${W + 10}" height="10" rx="3" fill="currentColor"/><rect x="${x0 + 10}" y="${y0 - 17}" width="${W - 20}" height="8" rx="4" fill="currentColor"/>` : "";

  /* label blocks: one per layer with steps, top layer first, pushed down so they never overlap */
  const wrap = (t, n = 34) => t.split(" ").reduce((ls, w) => { const l = ls[ls.length - 1]; if (l && (l + " " + w).length <= n) ls[ls.length - 1] = l + " " + w; else ls.push(w); return ls; }, [""]).filter(Boolean);
  const LH = 15, blocks = marks.slice().reverse().map(m => ({m, lines: m.L.steps.reduce((s, [, t]) => s + wrap(t).length, 0) + (m.L.group ? 1 : 0)}));
  let cursor = 4;
  blocks.forEach(bk => { const h = bk.lines * LH; bk.y = Math.max(cursor, bk.m.mid - h / 2); cursor = bk.y + h + 2 * bk.m.L.steps.length + 6; });
  const VH = Math.max(y0 + H + 10, cursor + 4) + (b.note ? 22 : 0);
  let labels = "";
  blocks.forEach(bk => {
    const {m} = bk; let ty = bk.y;
    const ay = Math.min(Math.max(m.mid, bk.y + 8), bk.y + bk.lines * LH - 8);
    labels += `<path d="M${lx - 4} ${ay} L${xr(m.mid) + 6} ${m.mid}" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M${xr(m.mid) + 12} ${m.mid - 4} L${xr(m.mid) + 6} ${m.mid} L${xr(m.mid) + 12} ${m.mid + 4}" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/>`;
    if (m.L.group){
      labels += `<text x="${lx + 10}" y="${ty + 12}" font-size="10" font-weight="700" letter-spacing="1.2" fill="currentColor">${esc(m.L.group)}</text>`;
      labels += `<path d="M${lx + 4} ${ty + 4} h-4 v${bk.lines * LH - 8} h4" fill="none" stroke="currentColor" stroke-width="1.6"/>`;
      ty += LH;
    }
    m.L.steps.forEach(([n, t]) => {
      const dim = m.L.opt ? ` opacity=".75"` : "", ls = wrap(t);
      labels += `<g${dim}><circle cx="${lx + 19}" cy="${ty + 8}" r="8" fill="none" stroke="currentColor" stroke-width="1.8"/><text x="${lx + 19}" y="${ty + 12}" font-size="11" font-weight="700" text-anchor="middle" fill="currentColor">${n}</text><text x="${lx + 32}" y="${ty + 12}" font-size="12.5" fill="currentColor">${ls.map((l, i) => `<tspan x="${lx + 32}" dy="${i ? LH : 0}">${esc(l)}</tspan>`).join("")}</text></g>`;
      ty += LH * ls.length + 2;
    });
  });
  const note = b.note ? `<text x="${x0}" y="${VH - 6}" font-size="12" font-style="italic" fill="currentColor">${esc(b.note)}</text>` : "";
  return `<svg class="cupsvg" viewBox="0 0 ${VW + 60} ${VH}" role="img" aria-label="${esc(temp)} build diagram">
    <defs><clipPath id="${id}"><path d="${cup}"/></clipPath></defs>
    ${lid}<g clip-path="url(#${id})">${fills}${deco}</g>
    <path d="${cup}" fill="none" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/>${labels}${note}</svg>`;
}

/* gallery of every drink on the menu; a click opens its diagrams */
function renderDiagramGrid(){
  const el = $("diagGrid"); if (!el) return;
  el.innerHTML = S.drinks.map((d, k) => { const g = diagramFor(d);
    return `<button class="dbtn diag-btn" data-act="diagram" data-k="${k}"${g ? "" : " disabled"}><b>${esc(d.name)}</b><span class="p">${g ? Object.keys(g.builds).map(t => t === "hot" ? "Hot" : "Iced").join(" and ") : "No diagram yet"}</span></button>`; }).join("");
}
function openDiagram(k){
  const d = S.drinks[k], g = diagramFor(d), dlg = $("diagDlg"); if (!g || !dlg) return;
  const builds = Object.entries(g.builds).sort(([a]) => a === "iced" ? -1 : 1);
  $("diagBody").innerHTML = `<div class="diag-h"><h2>${esc(d.name)}</h2><button class="btn ghost sm" data-act="diagClose">Close</button></div>
    <div class="diag-builds">${builds.map(([t, b]) => `<section class="diag-b"><h3>${t === "hot" ? "Hot, 12 oz cup" : "Iced, 16 oz cup"}</h3>
      ${cupSVG(b, t)}
      <div class="diag-m"><span>Price ${F.usd2(b.price)}</span><span>Cost ${F.usd2(b.cost)}</span><span>Margin ${Math.round((1 - b.cost / b.price) * 1000) / 10}%</span></div></section>`).join("")}</div>`;
  dlg.showModal();
}
```

### Step 4: Wire it up

Add one line at the end of `renderDrinkGrid()`, so the diagram buttons rebuild every time the menu changes (rename, swap a specialty, take a drink off the menu):

```js
  renderDiagramGrid();
```

Add two lines near the top of the click handler, after the `tab` branch:

```js
  if (a === "diagram"){ openDiagram(+t.dataset.k); return; }
  if (a === "diagClose"){ $("diagDlg").close(); return; }
```

Pressing Escape already closes a `<dialog>`. To close on a click outside it, add this once after the click handler:

```js
$("diagDlg").addEventListener("click", e => { if (e.target.id === "diagDlg") e.target.close(); });
```

### Data model

Each entry in `DIAGRAMS` is keyed by `norm(name)` and has `name`, optional `aliases`, and `builds` with an `iced` and/or `hot` build.

| Field | Meaning |
|:--|:--|
| `price`, `cost` | Menu price and cost per cup, used for the margin line |
| `top` | Empty space above the last layer, in px |
| `line` | Draws the iced fill line at the top of the drink |
| `note` | One italic line under the cup |
| `teabag` | Draws the tea bag (London Fog) |
| `layers` | Bottom of the cup to the top |

Each layer:

| Field | Meaning |
|:--|:--|
| `h` | Height in px. The iced cup is 146 px tall and the hot cup 198 px, so heights in a build should add up to about that minus `top` |
| `c` | Fill color, from `DC` |
| `steps` | `[[number, text], …]` for the steps that land in this layer |
| `ice`, `foam`, `splash` | Draws ice cubes, foam bubbles, or a striped splash |
| `group` | Caption for steps done off the cup, drawn with a bracket (`"IN THE SHAKER"`) |
| `opt` | Dims the step, for steps skipped on the plain drink |

### Adding a new drink

Copy the closest base build, change the swapped layer and its text, and set the price and cost. Example, a Vanilla Matcha Latte on the iced matcha base:

```js
vanillamatchalatte: {name:"Vanilla Matcha Latte", builds:{
  iced:{price:5.50, cost:1.11, top:10, line:true, layers:[
    {h:20, c:DC.syrup, steps:[[1,"2 pumps vanilla"]]},
    {h:34, c:DC.milk, ice:true, steps:[[2,"2 scoops ice"]]},
    {h:52, c:DC.milk, steps:[[3,"Milk to a little under the line"]]},
    {h:30, c:DC.matcha, steps:[[4,"Zero the scale, add 50 g matcha mix"]]}]}}},
```

The price and cost there are placeholders; take the real ones from the recipe lab. The key must equal `norm()` of the menu name, or the menu name must be in `aliases`.

### Check it

1. Open *Menu and recipes*. Every drink on the menu has a button; only drinks without data say "No diagram yet".
2. Click Latte: iced and hot builds appear side by side, steps 1 to 4 and 1 to 3, with margins 79.6% and 77.4%.
3. Click Brown Sugar Shaken Espresso: steps 1 to 4 sit under "IN THE SHAKER" with a bracket, step 5 points at the oat milk.
4. Rename a drink in Edit mode and press Done: the button follows the new name. If the name no longer matches, add it to `aliases`.
5. Switch the Mac to dark mode: outlines and text turn light, drink colors stay the same.
6. Escape, Close and a click outside the dialog all close it.
