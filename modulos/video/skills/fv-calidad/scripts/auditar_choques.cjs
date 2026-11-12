/* Auditor de choques para composiciones HyperFrames.
   Uso:  node audit_overlaps.cjs <index.html> [paso_s=0.1] [opacidad_min=0.5] [duracion_min_s=0.5]\n   Fuentes: AUDIT_FONTS="Montserrat:500;600;700;800;900,Inter:400;700" (por defecto Montserrat)
   Recorre la línea de tiempo (window.__timelines.main.seek(t)) y, en cada instante, detecta:
     - texto que pisa a otro texto o a un panel que no lo contiene,
     - paneles que se pisan entre sí (tarjetas, banners, sellos),
     - texto que se sale del lienzo (fuera de #cam).
   Respeta los <.clip> con data-start/data-duration (los oculta fuera de su ventana).
   Requiere puppeteer-core (se instala con: npm install --no-audit --no-fund puppeteer-core, dentro de esta carpeta) y Chrome o Edge. */
const path = require("path");
const { createRequire } = require("module");
const NM = process.env.PUPPETEER_NM || path.join(__dirname, "node_modules");
const puppeteer = createRequire(path.join(NM, "x.js"))("puppeteer-core");
const fs = require("fs");
const CANDIDATOS = [process.env.CHROME_PATH, "C:/Program Files/Google/Chrome/Application/chrome.exe", "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe",
  (process.env.LOCALAPPDATA || "") + "/Google/Chrome/Application/chrome.exe", "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe", "C:/Program Files/Microsoft/Edge/Application/msedge.exe",
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge", "/usr/bin/google-chrome", "/usr/bin/chromium", "/usr/bin/chromium-browser"];
const CHROME = CANDIDATOS.find((p) => p && fs.existsSync(p));
if (!CHROME) { console.error("No encuentro Chrome ni Edge. Instálalo o define CHROME_PATH."); process.exit(3); }
const [, , html, stepArg, opArg, minDurArg] = process.argv;
const MINDUR = parseFloat(minDurArg || "0.5");            // ignora choques que duran menos (animaciones de entrada/salida)
const FONTS = (process.env.AUDIT_FONTS || "Montserrat:500;600;700;800;900").split(",");   // familia:pesos separados por ;
if (!html) { console.error("uso: node audit_overlaps.cjs <index.html> [paso] [opacidad_min]"); process.exit(2); }
const STEP = parseFloat(stepArg || "0.1"), OPMIN = parseFloat(opArg || "0.5");

function inPage(t, OPMIN) {
  const tl = window.__timelines.main; tl.seek(t, false);
  const root = document.querySelector("[data-composition-id]");
  const W = parseFloat(root.getAttribute("data-width")), H = parseFloat(root.getAttribute("data-height"));
  const label = (el) => (el.id ? "#" + el.id : el.tagName.toLowerCase() + (el.className && typeof el.className === "string" ? "." + el.className.split(" ")[0] : ""));
  function alive(el) {            // visibilidad efectiva (opacidad acumulada, display y ventanas de .clip)
    let op = 1;
    for (let e = el; e && e !== document.documentElement; e = e.parentElement) {
      const cs = getComputedStyle(e);
      if (cs.display === "none" || cs.visibility === "hidden") return 0;
      op *= parseFloat(cs.opacity);
      if (e.classList && e.classList.contains("clip") && e.hasAttribute("data-start") && e.tagName !== "AUDIO" && e.tagName !== "VIDEO") {
        const s = parseFloat(e.getAttribute("data-start")), d = parseFloat(e.getAttribute("data-duration"));
        if (t < s || t >= s + d) return 0;
      }
    }
    return op;
  }
  const items = [];
  const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
  for (let n; (n = walker.nextNode());) {
    const txt = n.textContent.trim(); if (!txt) continue;
    const el = n.parentElement; if (!el || el.closest("script,style,audio")) continue;
    const op = alive(el); if (op < OPMIN) continue;
    const r = document.createRange(); r.selectNodeContents(n);
    const b = r.getBoundingClientRect(); if (b.width < 2 || b.height < 2) continue;
    items.push({ kind: "text", el, label: label(el) + ' "' + txt.slice(0, 18) + '"', x: b.left, y: b.top + b.height * 0.18, w: b.width, h: b.height * 0.62, cam: !!el.closest("#cam") });   // 62% central de la línea = cuerpo de las mayúsculas
  }
  document.querySelectorAll(".glass,.badge,.stamp,.pill,.tile,.pillbox,.badge2,.easy,#patch,.frame").forEach((el) => {
    const op = alive(el); if (op < OPMIN) return;
    const b = el.getBoundingClientRect(); if (b.width < 20 || b.height < 20) return;
    items.push({ kind: "panel", el, label: label(el), x: b.left, y: b.top, w: b.width, h: b.height, cam: !!el.closest("#cam") });
  });
  const out = [];
  for (let i = 0; i < items.length; i++) for (let j = i + 1; j < items.length; j++) {
    const a = items[i], b = items[j];
    if (a.el.contains(b.el) || b.el.contains(a.el)) continue;
    const inside = (p, q) => q.x >= p.x - 2 && q.y >= p.y - 2 && q.x + q.w <= p.x + p.w + 2 && q.y + q.h <= p.y + p.h + 2;
    if (inside(a, b) || inside(b, a)) continue;                      // etiqueta sobre una tarjeta/fondo: intencional
    if (a.cam && b.cam) continue;                                  // cosas pegadas al video no cuentan entre sí
    if (a.kind === "panel" && b.kind === "panel" && (a.el.closest(".glass") === b.el.closest(".glass"))) continue;
    const ix = Math.max(0, Math.min(a.x + a.w, b.x + b.w) - Math.max(a.x, b.x));
    const iy = Math.max(0, Math.min(a.y + a.h, b.y + b.h) - Math.max(a.y, b.y));
    const inter = ix * iy, minA = Math.min(a.w * a.h, b.w * b.h);
    if (minA > 0 && inter / minA > 0.12) out.push({ type: "choque", a: a.label, b: b.label, pct: Math.round((100 * inter) / minA) });
  }
  const PANEL = ".glass,.badge,.stamp,.pill,.tile,.pillbox,.badge2,.easy,#patch,.frame";
  for (const it of items) if (it.kind === "text") {                 // texto que se sale de su propia caja
    const pe = it.el.closest(PANEL); if (!pe) continue;
    const pb = pe.getBoundingClientRect();
    if (it.x < pb.left - 2 || it.x + it.w > pb.right + 2 || it.y < pb.top - 2 || it.y + it.h > pb.bottom + 2)
      out.push({ type: "texto-sale-del-panel", a: it.label, b: label(pe), pct: 0 });
  }
  for (const it of items) if (it.kind === "text" && !it.cam && (it.x < -1 || it.y < -1 || it.x + it.w > W + 1 || it.y + it.h > H + 1))
    out.push({ type: "fuera-de-lienzo", a: it.label, b: "", pct: 0 });
  return { out, dur: tl.duration() };
}

(async () => {
  const browser = await puppeteer.launch({ executablePath: CHROME, headless: "new", args: ["--allow-file-access-from-files", "--no-sandbox", "--autoplay-policy=no-user-gesture-required"] });
  const page = await browser.newPage();
  await page.setViewport({ width: 1080, height: 1920 });
  page.on("pageerror", (e) => console.error("[pageerror]", String(e.message || e).slice(0, 300)));
  page.on("requestfailed", (r) => console.error("[requestfailed]", r.url().slice(0, 120), r.failure() && r.failure().errorText));
  await page.evaluateOnNewDocument(() => { window.__timelines = window.__timelines || {}; });  // el runtime de HyperFrames lo crea al renderizar
  await page.goto("file:///" + path.resolve(html).replace(/\\/g, "/"), { waitUntil: "domcontentloaded", timeout: 60000 });
  await page.evaluate(() => document.fonts.ready);
  await page.waitForFunction(() => !!(window.__timelines && window.__timelines.main), { timeout: 30000, polling: 250 });
  // El runtime de HyperFrames inyecta las fuentes al renderizar; aquí las cargamos de Google Fonts para medir igual.
  for (const f of FONTS) {
    const [fam, w] = f.split(":");
    await page.addStyleTag({ content: `@import url('https://fonts.googleapis.com/css2?family=${fam.replace(/ /g, "+")}:wght@${w}&display=swap');` });
  }
  await new Promise((r) => setTimeout(r, 2500));
  await page.evaluate(async (fonts) => { for (const f of fonts) { const [fam, w] = f.split(":"); for (const wt of w.split(";")) await document.fonts.load(`${wt} 40px "${fam}"`); } await document.fonts.ready; }, FONTS);
  const dur = await page.evaluate(() => window.__timelines.main.duration());
  const issues = new Map();
  for (let t = 0; t <= dur - 0.01; t += STEP) {
    const r = await page.evaluate(inPage, t, OPMIN);
    for (const o of r.out) {
      const k = [o.type, [o.a, o.b].sort().join(" × ")].join("|");
      const e = issues.get(k) || { ...o, t0: t, t1: t, max: 0 };
      e.t1 = t; e.max = Math.max(e.max, o.pct); issues.set(k, e);
    }
  }
  await browser.close();
  const list = [...issues.values()].filter((e) => e.t1 - e.t0 + STEP >= MINDUR - 1e-6).sort((x, y) => x.t0 - y.t0);
  if (!list.length) { console.log("AUDITORÍA LIMPIA: 0 choques sostenidos (≥ " + MINDUR + " s) en " + dur.toFixed(1) + " s (paso " + STEP + " s)"); return; }
  console.log("CHOQUES DETECTADOS: " + list.length + "  (paso " + STEP + " s, opacidad ≥ " + OPMIN + ")");
  for (const e of list) console.log(`  ${e.t0.toFixed(1)}–${e.t1.toFixed(1)} s  ${e.type}  ${e.a}${e.b ? "  ×  " + e.b : ""}  (${e.max}% del menor)`);
  process.exitCode = 1;
})();





