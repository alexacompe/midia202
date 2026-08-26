#!/usr/bin/env python3
"""
processa_imagem.py — Obtém e prepara imagens para cards da 202.

Dois tratamentos:
  - foto  : converte para P&B (dessaturada), recorta para a faixa de meia-composição.
  - print : mantém a cor, enquadra/recorta a notícia (fundo papel no card).

Obtenção (Arquitetura A com fallback):
  1. Se receber uma URL, TENTA baixar. Se o download falhar (403/bloqueio de rede),
     NÃO trava: reporta que a imagem deve ser fornecida manualmente e sai com aviso.
  2. Se receber um caminho local, usa direto (sempre funciona).

Uso:
    # foto por url (tenta baixar, processa P&B)
    python3 processa_imagem.py --tipo foto --url https://... --out ita.jpg
    # print por arquivo local (enquadra, mantém cor)
    python3 processa_imagem.py --tipo print --in /caminho/print.png --out exame.png
"""
import argparse, os, sys, urllib.request

try:
    from PIL import Image, ImageOps
except ImportError:
    sys.exit("[ERRO] Pillow não instalado. Rode: pip install pillow")

# Proporção da faixa de imagem no card (medido: 39% de 1620 = 632px, largura 1296).
FAIXA_W, FAIXA_H = 1296, 632

def obter(url, local_in, out):
    """Retorna caminho de um arquivo de imagem utilizável, ou None se precisar de humano."""
    if local_in:
        if not os.path.exists(local_in):
            sys.exit(f"[ERRO] Arquivo não encontrado: {local_in}")
        return local_in
    if url:
        tmp = out + ".download"
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=30) as r, open(tmp, "wb") as f:
                f.write(r.read())
            if os.path.getsize(tmp) == 0:
                raise RuntimeError("arquivo vazio")
            return tmp
        except Exception as e:
            # FALLBACK: não trava. Avisa que o download falhou e pede imagem manual.
            print(f"[fallback] Não consegui baixar automaticamente ({str(e)[:60]}).")
            print(f"[fallback] Baixe a imagem manualmente de:\n            {url}")
            print(f"[fallback] e rode de novo com  --in <arquivo>  em vez de --url.")
            return None
    sys.exit("[ERRO] Forneça --url ou --in.")

def processa_foto(src, out):
    """Foto: P&B + recorte para a faixa de meia-composição (cover, centralizado)."""
    im = Image.open(src).convert("RGB")
    im = ImageOps.grayscale(im).convert("RGB")          # P&B
    im = ImageOps.fit(im, (FAIXA_W, FAIXA_H), method=Image.LANCZOS, centering=(0.5, 0.4))
    im.save(out, quality=95)
    print(f"[ok] foto P&B -> {out}  ({FAIXA_W}x{FAIXA_H})")

def processa_print(src, out):
    """Print de notícia: mantém cor, enquadra na faixa (cover). Fundo do card é papel."""
    im = Image.open(src).convert("RGB")
    im = ImageOps.fit(im, (FAIXA_W, FAIXA_H), method=Image.LANCZOS, centering=(0.5, 0.2))
    im.save(out, quality=95)
    print(f"[ok] print (cor) -> {out}  ({FAIXA_W}x{FAIXA_H})")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tipo", choices=["foto", "print"], required=True)
    ap.add_argument("--url", help="URL para baixar (tenta; cai para fallback se bloquear)")
    ap.add_argument("--in", dest="local_in", help="Arquivo local (sempre funciona)")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    src = obter(args.url, args.local_in, args.out)
    if src is None:
        # fallback acionado: sai sem erro fatal, mas sinaliza que falta a imagem
        sys.exit(2)

    if args.tipo == "foto":
        processa_foto(src, args.out)
    else:
        processa_print(src, args.out)

    # limpa temporário de download, se houver
    tmp = args.out + ".download"
    if os.path.exists(tmp) and tmp != src:
        os.unlink(tmp)

if __name__ == "__main__":
    main()
