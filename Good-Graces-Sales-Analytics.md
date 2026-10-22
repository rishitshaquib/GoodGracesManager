# Good Grace's Cafe: Sales Analytics

Updated October 22, 2026. All numbers come from Clover.

This file has the cafe's own sales analytics: sales curves, the most popular drinks, order sizes, peaks and add-on rates. Competitor numbers and labor are left out. Part 2 is the code that puts these into the portal's *Analytics* tab, reading `sales-data.json` from this folder.

## The data

| Dataset | What it has | Days |
|:--|:--|:--|
| Clover transaction logs | Every order's total and time, no items | Sat Oct 10, Sat Oct 17, Sun Oct 18 |
| Clover item sales report | Units, sales and modifiers per item, no times | Oct 1 to 15 (opening weekend; the 51 flat "Soft Launch Entry" lines are removed) |

The Oct 10 log arrived as "a Saturday" with no date. It is Sat Oct 10, opening weekend. It can't be the soft launch: Clover logged the soft launch as 51 flat $5 entries ($255), and this log has 78 orders at varied prices and runs until 6:10 PM, which matches the 10 to 6 opening-weekend hours.

## Days at a glance

| Day | Hours | Orders | Sales | Avg order | Median | Busiest 30 min | Before labor* |
|:--|:--|--:|--:|--:|--:|:--|--:|
| Sat Oct 10 | 10 AM to 6 PM | 78 | $442.75 | $5.68 | $5.00 | 9 orders from 10:06 AM | $322.05 |
| Sat Oct 17 | 9 AM to 5 PM | 80 | $450.50 | $5.63 | $5.00 | 13 orders from 1:49 PM | $327.62 |
| Sun Oct 18 | 9 AM to 5 PM | 83 | $444.25 | $5.35 | $5.00 | 15 orders from 12:47 PM | $322.65 |
| **All three** | | **241** | **$1,337.50** | **$5.55** | | | **$972.32** |

\*Sales minus COGS at 23.2% of sales and Clover fees of 2.3% + $0.10 per order. Sun Oct 18 is net of one $0.50 refund.

Every day landed between $442 and $451 and between 78 and 83 orders, across two different opening hours. About $445 and 80 orders a day is the steady level.

## Sales curves

Orders and sales in each half hour.

| Half hour | Sat Oct 10 | Sat Oct 17 | Sun Oct 18 |
|:--|--:|--:|--:|
| 9:00 AM |  | 1 / $7.50 |  |
| 9:30 AM | 1 / $9.25 | 2 / $18.25 |  |
| 10:00 AM | 7 / $39.50 | 2 / $6.00 | 1 / $5.25 |
| 10:30 AM | 4 / $24.00 | 2 / $13.00 | 3 / $14.00 |
| 11:00 AM | 6 / $60.25 | 4 / $25.50 | 5 / $27.25 |
| 11:30 AM | 5 / $25.75 | 6 / $28.50 | 2 / $16.50 |
| 12:00 PM | 5 / $39.50 | 8 / $40.50 | 6 / $26.50 |
| 12:30 PM | 5 / $29.50 | 6 / $37.50 | 9 / $45.25 |
| 1:00 PM | 6 / $25.50 | 5 / $24.25 | 12 / $71.25 |
| 1:30 PM | 6 / $28.00 | 10 / $52.25 | 9 / $55.25 |
| 2:00 PM | 5 / $24.00 | 10 / $53.50 | 10 / $51.75 |
| 2:30 PM | 4 / $20.50 | 5 / $27.50 | 7 / $35.75 |
| 3:00 PM | 8 / $37.00 | 8 / $49.50 | 4 / $23.00 |
| 3:30 PM | 3 / $17.00 | 6 / $34.50 | 5 / $27.50 |
| 4:00 PM | 5 / $28.75 | 3 / $24.25 | 7 / $31.50 |
| 4:30 PM | 2 / $9.50 | 2 / $8.00 | 3 / $14.00 |
| 5:00 PM | 1 / $2.00 |  |  |
| 5:30 PM | 4 / $15.75 |  |  |
| 6:00 PM | 1 / $7.00 |  |  |

What the curves show:

- **Opening Saturday was front-loaded.** 35.9% of Oct 10 sales came before noon, with a rush right at the 10 AM open (7 orders in the first half hour) and another from 11:00 to 11:15. Orders then held at 4 to 6 a half hour all afternoon.
- **The later weekend peaked at midday.** Before noon was 21.9% of Oct 17 sales and 14.2% of Oct 18. From 12 to 3 PM was 52.3% of Oct 17 sales and 64.2% of Oct 18.
- **The busiest half hours are 1:00 to 2:30 PM.** Sunday 1:00 to 1:30 had 12 orders ($71.25), the most of any half hour logged.
- **The first and last hour are slow.** 9 to 10 AM had 3 orders on Oct 17 and none on Oct 18, and after 4:30 PM orders fall to 2 or 3 a half hour.

## Order size

| Order total | Orders | Share |
|:--|--:|--:|
| Under $4 | 35 | 14.5% |
| $4 to 4.99 | 61 | 25.3% |
| $5 to 5.99 | 94 | 39.0% |
| $6 to 7.99 | 16 | 6.6% |
| $8 to 11.99 | 29 | 12.0% |
| $12 and up | 6 | 2.5% |

Most orders are one drink: 78.8% are under $6. The 35 orders of $8 or more are almost all two or more items, and they come in at 10 to 14 a day. The largest single order was $20.50.

## Most popular drinks

Clover item report, Oct 1 to 15.

| Item | Sold | Share of drinks | Sales | Margin |
|:--|--:|--:|--:|--:|
| Banana Bread Latte | 53 | 21.8% | $274.00 | 74.1% |
| Brown Sugar Oatmilk Shaken Espresso | 45 | 18.5% | $226.50 | 73.4% |
| Latte | 35 | 14.4% | $165.50 | 74.9% |
| Strawberry Matcha Latte | 22 | 9.1% | $124.50 | 77.4% |
| Chai Latte | 20 | 8.2% | $92.50 | 65.6% |
| Matcha Latte | 18 | 7.4% | $92.25 | 77.4% |
| London Fog | 18 | 7.4% | $63.75 | 76.5% |
| Cappuccino | 12 | 4.9% | $48.50 | 75.0% |
| Caramel Apple Spice Cider | 9 | 3.7% | $40.50 | 78.4% |
| Americano | 9 | 3.7% | $31.50 | 78.2% |
| Espresso Shot | 2 | 0.8% | $2.00 | 41.7% |
| Coffee Cake Donut (pastry) | 37 | | $92.50 | 100% |
| Biscoff Cake (pastry) | 14 | | $28.00 | 100% |

243 drinks and 51 pastries; $1,161.50 in drink sales and $120.50 in pastry sales. Banana Bread Latte and BSOE alone were 98 drinks, 40.3% of the total. With Strawberry Matcha, the three specialty drinks were 49.4%. Chai has the lowest drink margin, 65.6%. Pastry margin is 100% because the house covers its cost.

## Add-ons

| Add-on | Count | Rate |
|:--|--:|:--|
| Alt milk | 42 | 18.8% of the 223 milk drinks |
| Added flavor syrup | 24 | 9.9% of all drinks |
| Cold foam | 2 | 0.8% of all drinks |
| Pastry | 51 | 2.1 per 10 drinks |

Alt milk is concentrated in three drinks: Banana Bread Latte (17), Latte (8) and Strawberry Matcha (7) make up 76% of it. Added syrup is mostly on the plain Latte (16 of 24).

---

## Part 2: Coding it into the Analytics tab

### What it adds

A **Clover sales** tile on the *Analytics* tab with:
- **Orders per half hour:** one line per logged day, with a legend. Hover a point for that half hour's orders and sales.
- **Days:** orders, sales, average order, busiest 30 minutes and before-labor profit per day.
- **Order size:** the histogram above.
- **Top drinks:** the Clover item report, ranked, with share and margin.
- **Add-ons:** alt milk, syrup, cold foam and pastry rates.

It reads `sales-data.json`, so new Clover days only need a new entry in that file. It uses the portal's existing chart and table classes (`chart`, `gl`, `ax`, `t rank`, `rb`, `mlist`, `note-sm`, `muted`) and helpers (`$`, `esc`, `F`), so it needs no new CSS.

### Step 1: Files

`sales-data.json` sits next to `index.html` in this folder. Vercel serves it with the site, and the code fetches it by relative path.

Its shape:

```json
{
  "orders": {
    "2026-10-17": {"label": "Sat Oct 17", "open": "09:00", "close": "17:00",
                   "log": [["09:25", 7.5], ["09:30", 5.0], ["...", 0]]}
  },
  "items": {"label": "Oct 1 to 15 ...",
            "rows": [{"name": "Latte", "cat": "drink", "units": 35, "revenue": 165.5,
                      "cost": 41.62, "margin": 0.749, "alt": 8, "syrup": 16, "foam": 0}]},
  "cogsRate": 0.232,
  "card": {"pct": 0.023, "fixed": 0.10}
}
```

`log` is `[time, order total]` in 24-hour time, one row per Clover transaction. A refund is a negative total.

### Step 2: HTML

Paste inside `<section class="pane" id="pane-analytics">`, as a new `sec` in the right-hand column under *What sells*:

```html
<div class="sec">
  <h2>Clover sales</h2>
  <h3>Orders per half hour</h3>
  <svg class="chart" id="anCurve" viewBox="0 0 640 220"></svg>
  <h3>Days</h3>
  <div class="scroll"><table class="t"><thead><tr><th class="l">Day</th><th>Orders</th><th>Sales</th><th>Avg order</th><th>Busiest 30 min</th><th>Before labor</th></tr></thead><tbody id="anCloverDays"></tbody></table></div>
  <h3>Order size</h3>
  <table class="t rank" id="anOrderSize"></table>
  <h3>Top drinks, Clover item report</h3>
  <div class="scroll"><table class="t rank" id="anTop"></table></div>
  <h3>Add-ons</h3>
  <div class="mlist" id="anMods"></div>
</div>
```

### Step 3: JavaScript

Paste after `renderAnalytics()`:

```js
/* ---------- Clover analytics: sales curves, order sizes, peaks, top drinks ----------
   Reads sales-data.json from the same folder. Orders are Clover transaction totals with a time;
   items are the Clover item sales report. Each renderer draws into its own element and does
   nothing if that element is missing. */
let CLOVER = null;
fetch("sales-data.json").then(r => r.json()).then(d => { CLOVER = d; renderClover(); }).catch(() => {});

const toMin = t => { const [h, m] = t.split(":").map(Number); return h * 60 + m; };
const hhmm = m => { const h = Math.floor(m / 60), mm = m % 60; return `${h % 12 || 12}${mm ? ":" + String(mm).padStart(2, "0") : ""}${h < 12 ? "a" : "p"}`; };
const CLR = ["var(--tint)", "var(--orange)", "var(--green)", "var(--purple)", "var(--teal)"];

function cloverDays(){
  return Object.entries(CLOVER.orders).sort(([a], [b]) => a < b ? -1 : 1).map(([date, o], i) => {
    const sales = o.log.filter(([, v]) => v > 0), rev = o.log.reduce((s, [, v]) => s + v, 0);
    const bins = {}; sales.forEach(([t, v]) => { const k = Math.floor(toMin(t) / 30) * 30; (bins[k] = bins[k] || {n:0, rev:0}).n++; bins[k].rev += v; });
    const ms = sales.map(([t]) => toMin(t)).sort((a, b) => a - b);
    let peak = {n:0, at:0}; ms.forEach(m => { const n = ms.filter(x => x >= m && x < m + 30).length; if (n > peak.n) peak = {n, at:m}; });
    const card = sales.reduce((s, [, v]) => s + v * CLOVER.card.pct + CLOVER.card.fixed, 0);
    return {date, label:o.label, open:toMin(o.open), close:toMin(o.close), orders:sales.length, rev, avg:rev / sales.length,
      first:ms[0], last:ms[ms.length - 1], bins, peak, profit:rev - rev * CLOVER.cogsRate - card, color:CLR[i % CLR.length]};
  });
}

/* orders per half hour, one line per logged day */
function renderSalesCurve(D){
  const el = $("anCurve"); if (!el) return;
  const W = 640, Hh = 220, m = {l:30, r:10, t:14, b:40}, iw = W - m.l - m.r, ih = Hh - m.t - m.b;
  const t0 = Math.min(...D.map(d => d.open)), t1 = Math.max(...D.map(d => Math.max(d.close, d.last + 30)));
  const slots = []; for (let t = t0; t < t1; t += 30) slots.push(t);
  const mx = Math.max(4, ...D.flatMap(d => slots.map(s => (d.bins[s] || {n:0}).n))) * 1.1;
  const x = s => m.l + (s - t0 + 15) / (t1 - t0) * iw, y = v => m.t + ih - v / mx * ih;
  let g = "";
  [0, Math.round(mx / 2), Math.round(mx)].forEach(v => g += `<line class="gl" x1="${m.l}" x2="${W - m.r}" y1="${y(v)}" y2="${y(v)}"/><text class="ax" x="${m.l - 5}" y="${y(v) + 4}" text-anchor="end">${v}</text>`);
  slots.forEach((s, i) => { if (i % 2 === 0) g += `<text class="ax" x="${x(s)}" y="${m.t + ih + 16}" text-anchor="middle">${hhmm(s)}</text>`; });
  D.forEach(d => {
    const pts = slots.filter(s => s >= d.open - 30 && s < Math.max(d.close, d.last + 1)).map(s => [x(s), y((d.bins[s] || {n:0}).n), s]);
    g += `<polyline fill="none" stroke="${d.color}" stroke-width="2.2" stroke-linejoin="round" points="${pts.map(p => p[0].toFixed(1) + "," + p[1].toFixed(1)).join(" ")}"/>`;
    pts.forEach(([px, py, s]) => g += `<circle cx="${px.toFixed(1)}" cy="${py.toFixed(1)}" r="2.6" fill="${d.color}"><title>${esc(d.label)}, ${hhmm(s)}: ${(d.bins[s] || {n:0}).n} orders, ${F.usd2((d.bins[s] || {rev:0}).rev)}</title></circle>`);
  });
  let lx = m.l; D.forEach(d => { g += `<rect x="${lx}" y="${Hh - 12}" width="12" height="3" rx="1" fill="${d.color}"/><text class="ax" x="${lx + 16}" y="${Hh - 8}">${esc(d.label)}</text>`; lx += 30 + d.label.length * 6.2; });
  el.innerHTML = g;
}

/* order value histogram, all logged days together */
function renderOrderSizes(){
  const el = $("anOrderSize"); if (!el) return;
  const B = [["Under $4", 0, 4], ["$4 to 4.99", 4, 5], ["$5 to 5.99", 5, 6], ["$6 to 7.99", 6, 8], ["$8 to 11.99", 8, 12], ["$12 and up", 12, 1e9]];
  const all = Object.values(CLOVER.orders).flatMap(o => o.log.map(([, v]) => v)).filter(v => v > 0);
  const n = B.map(([, a, b]) => all.filter(v => v >= a && v < b).length), mx = Math.max(...n);
  el.innerHTML = `<tbody>${B.map(([l], i) => `<tr><td class="l">${l}</td><td class="bar"><div class="rb"><i style="width:${n[i] / mx * 100}%"></i></div></td><td>${F.int(n[i])}</td><td class="muted">${F.frac(n[i] / all.length)}</td></tr>`).join("")}</tbody>`;
}

/* one row per logged day */
function renderCloverDays(D){
  const el = $("anCloverDays"); if (!el) return;
  el.innerHTML = D.map(d => `<tr><td class="l">${esc(d.label)}</td><td>${F.int(d.orders)}</td><td>${F.usd2(d.rev)}</td><td>${F.usd2(d.avg)}</td><td>${hhmm(d.peak.at)}, ${d.peak.n}</td><td>${F.usd2(d.profit)}</td></tr>`).join("");
}

/* Clover item report: units, revenue, margin, modifier rates */
function renderTopDrinks(){
  const el = $("anTop"); if (!el) return;
  const rows = CLOVER.items.rows.slice().sort((a, b) => b.units - a.units), mx = Math.max(...rows.map(r => r.units));
  const drinks = rows.filter(r => r.cat === "drink").reduce((s, r) => s + r.units, 0);
  el.innerHTML = `<thead><tr><th class="l">Item</th><th></th><th>Sold</th><th>Share</th><th>Sales</th><th>Margin</th></tr></thead><tbody>${rows.map(r => `<tr><td class="l">${esc(r.name)}${r.cat === "pastry" ? ` <span class="note-sm">pastry</span>` : ""}</td><td class="bar"><div class="rb"><i style="width:${r.units / mx * 100}%"></i></div></td><td>${F.int(r.units)}</td><td class="muted">${r.cat === "drink" ? F.frac(r.units / drinks) : ""}</td><td>${F.usd2(r.revenue)}</td><td>${F.frac(r.margin)}</td></tr>`).join("")}</tbody>`;
  const milky = rows.filter(r => r.cat === "drink" && !["Americano", "Espresso Shot", "Caramel Apple Spice Cider"].includes(r.name));
  const sum = k => rows.reduce((s, r) => s + (r[k] || 0), 0), mu = milky.reduce((s, r) => s + r.units, 0);
  const box = $("anMods"); if (box) box.innerHTML = [["Alt milk, milk drinks", F.frac(sum("alt") / mu)], ["Added syrup, all drinks", F.frac(sum("syrup") / drinks)], ["Cold foam, all drinks", F.frac(sum("foam") / drinks)], ["Pastry per 10 drinks", F.n1(rows.filter(r => r.cat === "pastry").reduce((s, r) => s + r.units, 0) / drinks * 10)]]
    .map(([l, v]) => `<div><div class="l">${l}</div><div class="v">${v}</div></div>`).join("");
}

function renderClover(){
  if (!CLOVER) return;
  const D = cloverDays();
  renderSalesCurve(D); renderOrderSizes(); renderCloverDays(D); renderTopDrinks();
}
```

### Step 4: Wire it up

Add one line at the end of `renderAnalytics()`, so the Clover tile redraws with the rest of the tab:

```js
  renderClover();
```

The fetch at the top of the block draws the tile once the file loads. If the file is missing, the tile stays empty and nothing else breaks.

### Adding a new Clover day

1. In Clover, open Transactions for the day and copy each time and total.
2. Add an entry to `orders` in `sales-data.json`, keyed by the date, with `label`, `open`, `close` and the `log`.
3. Deploy. The curve gets a new line and the Days table a new row.

When a new item sales report comes in, replace `items.rows` and its `label`. `cost` and `margin` come from the COGS model; set `margin` to 1 for pastries while the house covers them.

### Check it

1. Analytics shows a Clover sales tile with three lines on the curve.
2. Days: Sat Oct 10 is 78 orders, $442.75; Sat Oct 17 is 80, $450.50; Sun Oct 18 is 83, $444.25.
3. Order size adds up to 241 orders.
4. Top drinks starts with Banana Bread Latte at 53.
5. Add-ons shows 18.8% alt milk.
