#!/usr/bin/env python3
"""
render.py — Renderiza cards de carrossel da 202 (Instagram, Ciclo 1) a partir de um JSON.

Uso:
    python3 render.py cards.json --out ./saida

O JSON descreve o carrossel. Cada card vira um PNG 1296×1620 fiel à métrica da 202
(design.rules.md). O motor é o wkhtmltoimage, com auto-instalação e falha visível.

FALHA VISÍVEL: se o renderizador não estiver disponível e não puder ser instalado,
o script PARA com instrução clara — nunca gera um card degradado em silêncio.
"""
import argparse, base64, html, json, os, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL_ROOT = os.path.dirname(HERE)
FONT_DIR = os.path.join(SKILL_ROOT, "assets", "fonts")
CSS_PATH = os.path.join(SKILL_ROOT, "templates", "card.css")

# ---------------------------------------------------------------- renderer setup
# Estratégia de dois motores:
#   1) PLAYWRIGHT (chromium) — PRIMÁRIO. Render nativo 1296×1620, fiel, sem upscale.
#   2) WKHTMLTOIMAGE — FALLBACK. Pagina em canvas alto, então renderizamos a meia
#      escala (648×810, via zoom:0.5 no CSS) e fazemos upscale 2× Lanczos.
# Se nenhum estiver disponível e não puder ser instalado, o script PARA com instrução
# clara — nunca gera um card degradado em silêncio.

def detect_playwright():
    """Retorna True se o playwright + chromium estiverem prontos."""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return False
    try:
        with sync_playwright() as p:
            b = p.chromium.launch()
            b.close()
        return True
    except Exception:
        # lib presente mas navegador não baixado — tenta instalar uma vez
        try:
            subprocess.run([sys.executable, "-m", "playwright", "install", "chromium"],
                           check=True, capture_output=True, timeout=300)
            from playwright.sync_api import sync_playwright as sp2
            with sp2() as p:
                b = p.chromium.launch(); b.close()
            return True
        except Exception:
            return False

def detect_wkhtml():
    exe = shutil.which("wkhtmltoimage")
    if exe:
        return exe
    for cmd in (["apt-get", "install", "-y", "wkhtmltopdf"],
                ["sudo", "apt-get", "install", "-y", "wkhtmltopdf"]):
        try:
            subprocess.run(cmd, check=True, capture_output=True, timeout=180)
            exe = shutil.which("wkhtmltoimage")
            if exe:
                return exe
        except Exception:
            continue
    return None

def choose_engine():
    """Retorna ('playwright', None) | ('wkhtml', exe). Aborta se nenhum servir."""
    if detect_playwright():
        return ("playwright", None)
    exe = detect_wkhtml()
    if exe:
        print("[aviso] chromium/playwright indisponível — usando wkhtmltoimage "
              "(fallback: render em meia escala + upscale 2×). Para qualidade máxima, "
              "disponibilize o chromium no ambiente.")
        return ("wkhtml", exe)
    sys.exit(
        "\n[ERRO] Nenhum renderizador disponível.\n"
        "A skill NÃO gera um card degradado sem o layout/fontes corretos.\n"
        "Instale UM destes e rode de novo:\n"
        "  • Playwright (recomendado):  pip install playwright && playwright install chromium\n"
        "  • wkhtmltoimage (fallback):  sudo apt-get install -y wkhtmltopdf\n"
    )

def check_fonts():
    """As fontes de produção precisam existir. The Seasons NÃO é usada (wordmark é textual/SVG)."""
    need = ["Playfair-Display.ttf", "Playfair-DisplayItalic.ttf",
            "Inter-Reg.ttf", "Inter-Bd.ttf", "IBMPlexMono-Regular.ttf"]
    missing = [f for f in need if not os.path.exists(os.path.join(FONT_DIR, f))]
    if missing:
        sys.exit(f"\n[ERRO] Fontes empacotadas ausentes em {FONT_DIR}: {missing}\n"
                 "A skill depende delas para a identidade da 202. Reinstale a skill.\n")

# ---------------------------------------------------------------- html building
def esc(s):
    """Escapa texto, mas preserva marcadores de marca-up simples do conteúdo."""
    return html.escape(s, quote=False)

def render_inline(text):
    """
    Converte marcação leve do conteúdo em spans:
      *palavra*      -> ênfase (itálico Fraunces)        <span class="enf">
      _palavra_      -> sublinhado verde                  <span class="sub">
      **palavra**    -> destaque bold (corpo)             <span class="hl">
    O ponto verde final é tratado separadamente (campo "ponto": true).
    """
    import re
    t = esc(text)
    t = re.sub(r'\*\*(.+?)\*\*', r'<span class="hl">\1</span>', t)
    t = re.sub(r'\*(.+?)\*',     r'<span class="enf">\1</span>', t)
    t = re.sub(r'_(.+?)_',       r'<span class="sub">\1</span>', t)
    return t

def img_data_uri(path):
    ext = os.path.splitext(path)[1].lstrip(".").lower() or "jpeg"
    with open(path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    return f"data:image/{ext};base64,{b64}"

def build_card_html(card, css):
    fundo = card.get("fundo", "preto")          # "preto" | "papel"
    escala = card.get("escala", "L")            # "XL" | "L" | "M"
    # âncora vertical do bloco central: "top" | "center" | "low" | "fecho"
    # cards com imagem SEMPRE usam top (o offset vem da faixa de imagem, não da âncora)
    if card.get("imagem"):
        ancora = "top"
    else:
        ancora = card.get("ancora", "center")
    classes = ["card"]
    if fundo == "papel":
        classes.append("papel")
    if card.get("imagem"):
        classes.append("com-imagem")

    parts = [f'<div class="{" ".join(classes)}">']

    # marca d'água "202" (opcional; cards de abertura/fecho) — atrás de tudo
    if card.get("marca_dagua"):
        parts.append('<div class="marca-dagua">202</div>')

    # faixa de imagem (meia-composição) fica fora da coluna, no topo
    if card.get("imagem"):
        uri = img_data_uri(card["imagem"])
        parts.append(f'<div class="faixa-img" style="background-image:url({uri})"></div>')

    # kicker é ancorado ao topo (fora da coluna de fluxo vertical)
    # coluna central com âncora vertical (kicker + meio)
    parts.append(f'<div class="col v-{ancora}">')
    if card.get("kicker"):
        parts.append(f'<div class="kicker">{esc(card["kicker"])}</div>')
    parts.append('<div class="meio">')
    if card.get("titulo"):
        ponto = '<span class="ponto">.</span>' if card.get("ponto", True) else ''
        parts.append(f'<div class="titulo t-{escala}">{render_inline(card["titulo"])}{ponto}</div>')
    if card.get("hairline"):
        parts.append('<hr class="hairline">')
    if card.get("subtitulo"):
        parts.append(f'<div class="subtitulo">{render_inline(card["subtitulo"])}</div>')
    parts.append('</div>')  # fecha meio
    parts.append('</div>')  # fecha col

    # rodapé
    wm = '202 Lab<span class="ponto">.</span>'
    arr = '<div class="arraste">arraste &#8594;</div>' if card.get("arraste") else '<div></div>'
    parts.append(f'<div class="rodape"><div class="wordmark">{wm}</div>{arr}</div>')

    parts.append('</div>')  # fecha card

    body = "\n".join(parts)
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>
{css}
</style></head><body>{body}</body></html>"""

# ---------------------------------------------------------------- render
def render_playwright(html_str, out_png):
    """Render nativo 1296×1620, sem upscale. Requer o body SEM zoom (escala cheia)."""
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch()
        page = b.new_page(viewport={"width": 1296, "height": 1620}, device_scale_factor=1)
        page.set_content(html_str, wait_until="networkidle")
        page.screenshot(path=out_png, clip={"x": 0, "y": 0, "width": 1296, "height": 1620})
        b.close()

def render_wkhtml(exe, html_str, out_png):
    """
    Fallback: wkhtmltoimage pagina em canvas alto. Renderizamos em meia escala
    (648×810, o HTML aplica zoom:0.5) e upscale 2× Lanczos para 1296×1620.
    """
    from PIL import Image
    # injeta zoom:0.5 no body para render em meia escala
    html_half = html_str.replace("<body>", '<body style="zoom:0.5">', 1)
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
        f.write(html_half)
        tmp = f.name
    tmp_png = out_png + ".half.png"
    try:
        subprocess.run(
            [exe, "--encoding", "utf-8", "--width", "648", "--height", "810",
             "--disable-smart-width", "--quality", "100", "--enable-local-file-access",
             tmp, tmp_png],
            capture_output=True, timeout=120,
        )
        if not os.path.exists(tmp_png) or os.path.getsize(tmp_png) == 0:
            raise RuntimeError("PNG (meia escala) não gerado pelo wkhtmltoimage")
        Image.open(tmp_png).resize((1296, 1620), Image.LANCZOS).save(out_png)
    finally:
        for pth in (tmp, tmp_png):
            if os.path.exists(pth):
                os.unlink(pth)

def render_card(engine, exe, html_str, out_png):
    if engine == "playwright":
        render_playwright(html_str, out_png)
    else:
        render_wkhtml(exe, html_str, out_png)
    if not os.path.exists(out_png) or os.path.getsize(out_png) == 0:
        raise RuntimeError(f"Falha ao renderizar {out_png}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cards_json")
    ap.add_argument("--out", default="./saida")
    args = ap.parse_args()

    check_fonts()
    engine, exe = choose_engine()

    with open(CSS_PATH, encoding="utf-8") as f:
        css = f.read().replace("FONT_DIR", FONT_DIR)

    with open(args.cards_json, encoding="utf-8") as f:
        data = json.load(f)
    cards = data["cards"] if isinstance(data, dict) else data

    os.makedirs(args.out, exist_ok=True)
    written = []
    for i, card in enumerate(cards, 1):
        html_str = build_card_html(card, css)
        out_png = os.path.join(args.out, f"card{i}.png")
        render_card(engine, exe, html_str, out_png)
        written.append(out_png)
        print(f"  card {i}/{len(cards)} -> {out_png}")

    print(f"\nOK: {len(written)} card(s) em {args.out}  [motor: {engine}]")

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()
