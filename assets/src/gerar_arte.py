#!/usr/bin/env python3
"""
Gera a arte em pixel art do README (assets/banner.svg e assets/footer.svg).

Tudo é desenhado com <path> de retângulos: sem fontes externas, sem imagens
e sem serviços de terceiros, então o GitHub sempre consegue renderizar.
As animações usam CSS e SMIL dentro do próprio SVG (o GitHub mantém as duas
quando o SVG é exibido via <img>).

Uso:
    python3 assets/src/gerar_arte.py
"""
from __future__ import annotations

import math
import random
from pathlib import Path

ASSETS = Path(__file__).resolve().parent.parent

# --------------------------------------------------------------------------
# Paleta: jotape.exp (carvão/branco/violeta/cinza) + JPX Lab (azul elétrico)
# --------------------------------------------------------------------------
C = {
    "bg": "#0c0b12",
    "panel": "#14131d",
    "board": "#17142a",
    "frame": "#3f3f46",
    "wood": "#52525b",
    "white": "#f4f4f5",
    "gray": "#a1a1aa",
    "dim": "#71717a",
    "violet": "#a78bfa",
    "violet2": "#7c3aed",
    "violet3": "#4c1d95",
    "blue": "#3b82f6",
    "blue2": "#1d4ed8",
    "skin": "#b47a52",   # troque aqui o tom de pele do personagem
    "skin2": "#8a5a3a",
    "hair": "#141414",
    "hair2": "#2e2e33",
    "pants": "#1e293b",
    "shoe": "#09090b",
    "chalk": "#d4d4d8",
}

# --------------------------------------------------------------------------
# Fonte bitmap 5x7 (maiúsculas, números, acentos do português e símbolos)
# Linhas -3 e -2 guardam acentos; 7 e 8, a cedilha.
# --------------------------------------------------------------------------
G = {
    "A": [".XXX.", "X...X", "X...X", "XXXXX", "X...X", "X...X", "X...X"],
    "B": ["XXXX.", "X...X", "X...X", "XXXX.", "X...X", "X...X", "XXXX."],
    "C": [".XXX.", "X...X", "X....", "X....", "X....", "X...X", ".XXX."],
    "D": ["XXXX.", "X...X", "X...X", "X...X", "X...X", "X...X", "XXXX."],
    "E": ["XXXXX", "X....", "X....", "XXXX.", "X....", "X....", "XXXXX"],
    "F": ["XXXXX", "X....", "X....", "XXXX.", "X....", "X....", "X...."],
    "G": [".XXX.", "X...X", "X....", "X.XXX", "X...X", "X...X", ".XXXX"],
    "H": ["X...X", "X...X", "X...X", "XXXXX", "X...X", "X...X", "X...X"],
    "I": [".XXX.", "..X..", "..X..", "..X..", "..X..", "..X..", ".XXX."],
    "J": ["..XXX", "...X.", "...X.", "...X.", "...X.", "X..X.", ".XX.."],
    "K": ["X...X", "X..X.", "X.X..", "XX...", "X.X..", "X..X.", "X...X"],
    "L": ["X....", "X....", "X....", "X....", "X....", "X....", "XXXXX"],
    "M": ["X...X", "XX.XX", "X.X.X", "X.X.X", "X...X", "X...X", "X...X"],
    "N": ["X...X", "XX..X", "X.X.X", "X..XX", "X...X", "X...X", "X...X"],
    "O": [".XXX.", "X...X", "X...X", "X...X", "X...X", "X...X", ".XXX."],
    "P": ["XXXX.", "X...X", "X...X", "XXXX.", "X....", "X....", "X...."],
    "Q": [".XXX.", "X...X", "X...X", "X...X", "X.X.X", "X..X.", ".XX.X"],
    "R": ["XXXX.", "X...X", "X...X", "XXXX.", "X.X..", "X..X.", "X...X"],
    "S": [".XXXX", "X....", "X....", ".XXX.", "....X", "....X", "XXXX."],
    "T": ["XXXXX", "..X..", "..X..", "..X..", "..X..", "..X..", "..X.."],
    "U": ["X...X", "X...X", "X...X", "X...X", "X...X", "X...X", ".XXX."],
    "V": ["X...X", "X...X", "X...X", "X...X", "X...X", ".X.X.", "..X.."],
    "W": ["X...X", "X...X", "X...X", "X.X.X", "X.X.X", "X.X.X", ".X.X."],
    "X": ["X...X", "X...X", ".X.X.", "..X..", ".X.X.", "X...X", "X...X"],
    "Y": ["X...X", "X...X", ".X.X.", "..X..", "..X..", "..X..", "..X.."],
    "Z": ["XXXXX", "....X", "...X.", "..X..", ".X...", "X....", "XXXXX"],
    "0": [".XXX.", "X...X", "X..XX", "X.X.X", "XX..X", "X...X", ".XXX."],
    "1": ["..X..", ".XX..", "..X..", "..X..", "..X..", "..X..", ".XXX."],
    "2": [".XXX.", "X...X", "....X", "...X.", "..X..", ".X...", "XXXXX"],
    "3": ["XXXX.", "....X", "....X", ".XXX.", "....X", "....X", "XXXX."],
    "4": ["...X.", "..XX.", ".X.X.", "X..X.", "XXXXX", "...X.", "...X."],
    "5": ["XXXXX", "X....", "XXXX.", "....X", "....X", "X...X", ".XXX."],
    "6": [".XXX.", "X....", "X....", "XXXX.", "X...X", "X...X", ".XXX."],
    "7": ["XXXXX", "....X", "...X.", "..X..", ".X...", ".X...", ".X..."],
    "8": [".XXX.", "X...X", "X...X", ".XXX.", "X...X", "X...X", ".XXX."],
    "9": [".XXX.", "X...X", "X...X", ".XXXX", "....X", "....X", ".XXX."],
    " ": ["....."] * 7,
    "·": [".....", ".....", ".....", "..X..", ".....", ".....", "....."],
    ":": [".....", "..X..", ".....", ".....", ".....", "..X..", "....."],
    ".": [".....", ".....", ".....", ".....", ".....", ".....", "..X.."],
    ",": [".....", ".....", ".....", ".....", ".....", "..X..", ".X..."],
    "-": [".....", ".....", ".....", ".XXX.", ".....", ".....", "....."],
    "+": [".....", "..X..", "..X..", "XXXXX", "..X..", "..X..", "....."],
    "=": [".....", ".....", "XXXXX", ".....", "XXXXX", ".....", "....."],
    "(": ["...X.", "..X..", ".X...", ".X...", ".X...", "..X..", "...X."],
    ")": [".X...", "..X..", "...X.", "...X.", "...X.", "..X..", ".X..."],
    "/": ["....X", "....X", "...X.", "..X..", ".X...", "X....", "X...."],
    ">": [".X...", "..X..", "...X.", "....X", "...X.", "..X..", ".X..."],
    "?": [".XXX.", "X...X", "....X", "...X.", "..X..", ".....", "..X.."],
    "!": ["..X..", "..X..", "..X..", "..X..", "..X..", ".....", "..X.."],
    "_": [".....", ".....", ".....", ".....", ".....", ".....", "XXXXX"],
    "$": ["..X..", ".XXXX", "X.X..", ".XXX.", "..X.X", "XXXX.", "..X.."],
    "Π": ["XXXXX", ".X.X.", ".X.X.", ".X.X.", ".X.X.", ".X.X.", ".X.X."],
    "Σ": ["XXXXX", "X....", ".X...", "..X..", ".X...", "X....", "XXXXX"],
    "²": [".XX..", "...X.", "..X..", ".XXX.", ".....", ".....", "....."],
}
ACC = {
    "~": ([".XX.X", "X.XX."], None),
    "´": (["...X.", "..X.."], None),
    "^": (["..X..", ".X.X."], None),
    "¸": (None, ["..X..", ".X..."]),
}
COMPOSED = {
    "Ã": ("A", "~"), "Õ": ("O", "~"), "Á": ("A", "´"), "É": ("E", "´"),
    "Í": ("I", "´"), "Ó": ("O", "´"), "Ú": ("U", "´"), "Â": ("A", "^"),
    "Ê": ("E", "^"), "Ô": ("O", "^"), "Ç": ("C", "¸"),
}


def glyph(ch: str) -> list[tuple[int, int]]:
    """Retorna os pixels (col, linha) de um caractere."""
    acc = None
    if ch in COMPOSED:
        ch, acc = COMPOSED[ch]
    rows = G.get(ch, G["?"])
    pts = [(x, y) for y, r in enumerate(rows) for x, c in enumerate(r) if c == "X"]
    if acc:
        top, bottom = ACC[acc]
        if top:
            pts += [(x, y - 3) for y, r in enumerate(top) for x, c in enumerate(r) if c == "X"]
        if bottom:
            pts += [(x, y + 7) for y, r in enumerate(bottom) for x, c in enumerate(r) if c == "X"]
    return pts


def text_width(s: str, p: int) -> int:
    return len(s) * 6 * p - p


# --------------------------------------------------------------------------
# Canvas de pixels → <path> por cor (juntando pixels vizinhos em faixas)
# --------------------------------------------------------------------------
class Layer:
    def __init__(self) -> None:
        self.px: dict[tuple[int, int, int], str] = {}  # (x, y, tamanho) -> cor

    def dot(self, x: int, y: int, p: int, color: str) -> None:
        self.px[(x, y, p)] = color

    def rect(self, x: int, y: int, w: int, h: int, p: int, color: str) -> None:
        for j in range(h):
            for i in range(w):
                self.dot(x + i * p, y + j * p, p, color)

    def text(self, s: str, x: int, y: int, p: int, color: str) -> int:
        for k, ch in enumerate(s):
            for gx, gy in glyph(ch):
                self.dot(x + (k * 6 + gx) * p, y + gy * p, p, color)
        return text_width(s, p)

    def sprite(self, rows: list[str], x: int, y: int, p: int, pal: dict[str, str]) -> None:
        for j, r in enumerate(rows):
            for i, c in enumerate(r):
                if c in pal:
                    self.dot(x + i * p, y + j * p, p, pal[c])

    def svg(self, attrs: str = "") -> str:
        by_color: dict[str, list[tuple[int, int, int]]] = {}
        for (x, y, p), col in self.px.items():
            by_color.setdefault(col, []).append((x, y, p))
        out = []
        for col, pts in by_color.items():
            pts.sort(key=lambda t: (t[2], t[1], t[0]))
            d, run = [], None
            for x, y, p in pts:
                if run and run[1] == y and run[2] == p and run[0] + run[3] == x:
                    run[3] += p
                else:
                    if run:
                        d.append(f"M{run[0]} {run[1]}h{run[3]}v{run[2]}h-{run[3]}z")
                    run = [x, y, p, p]
            if run:
                d.append(f"M{run[0]} {run[1]}h{run[3]}v{run[2]}h-{run[3]}z")
            out.append(f'<path fill="{col}" d="{"".join(d)}"/>')
        inner = "".join(out)
        return f"<g {attrs}>{inner}</g>" if attrs else inner


def frame(L: Layer, w: int, h: int) -> None:
    """Moldura dupla estilo tela de jogo."""
    p = 6
    L.rect(6, 6, (w - 12) // p, 1, p, C["white"])
    L.rect(6, h - 12, (w - 12) // p, 1, p, C["white"])
    L.rect(6, 6, 1, (h - 12) // p, p, C["white"])
    L.rect(w - 12, 6, 1, (h - 12) // p, p, C["white"])
    q = 3
    L.rect(21, 21, (w - 42) // q, 1, q, C["frame"])
    L.rect(21, h - 24, (w - 42) // q, 1, q, C["frame"])
    L.rect(21, 21, 1, (h - 42) // q, q, C["frame"])
    L.rect(w - 24, 21, 1, (h - 42) // q, q, C["frame"])


def stars(w: int, h: int, n: int, seed: int, avoid) -> str:
    rnd = random.Random(seed)
    parts = []
    k = 0
    while k < n:
        x = rnd.randrange(32, w - 40) // 5 * 5
        y = rnd.randrange(32, h - 40) // 5 * 5
        if avoid(x, y):
            continue
        s = 5 if rnd.random() < 0.25 else 3
        col = C["white"] if rnd.random() < 0.7 else C["violet"]
        dur = rnd.choice([2.4, 3.1, 3.8, 4.6])
        delay = round(rnd.random() * 4, 2)
        parts.append(
            f'<rect class="tw" x="{x}" y="{y}" width="{s}" height="{s}" fill="{col}" '
            f'style="animation-duration:{dur}s;animation-delay:-{delay}s"/>'
        )
        k += 1
    return "".join(parts)


# --------------------------------------------------------------------------
# Personagem (P = 5 px)
# --------------------------------------------------------------------------
HERO = [
    "....HHHHHHH.....",
    "...HHHHHHHHH....",
    "..HHHHhhHHHHH...",
    "..HHhSSSSSSHH...",
    "..HSSSSSSSSSH...",
    "..SgggSSgggSS...",
    "..SgEgggEgSSs...",
    "..SgggSSgggSs...",
    "..sSSSSSSSSSs...",
    "...SSSSmmSSS....",
    "....SSSSSSS.....",
    ".....sSSSs......",
    "...VVVVVVVVVV...",
    "..VVVVVWVVWVVV..",
    "..VVVVVWVVWVVVV.",
    "..VVVVVVVVVVVVV.",
    "..VVvvvvvvvVVVV.",
    "..VVvvvvvvvVVSS.",
    "..VVVVVVVVVVVSS.",
    "...BBBBBBBBB....",
    "...BBBBBBBBB....",
    "...BBBB.BBBB....",
    "...BBBB.BBBB....",
    "...BBBB.BBBB....",
    "..KKKKK.KKKKK...",
]
HERO_PAL = {
    "H": C["hair"], "h": C["hair2"], "S": C["skin"], "s": C["skin2"],
    "g": C["white"], "E": C["bg"], "m": C["skin2"], "V": C["violet2"],
    "v": C["violet3"], "W": C["white"], "B": C["pants"], "K": C["shoe"],
}
# Braço erguido (fora da grade do sprite): coordenadas relativas
ARM = [(1, 12, "V"), (1, 11, "V"), (0, 11, "V"), (0, 10, "V"), (-1, 10, "V"),
       (-1, 9, "V"), (-2, 9, "S"), (-2, 8, "S"), (-1, 8, "S")]

# Ícones 10x10 (P = 4 px)
ICONS = {
    "livro": (["..........",
               ".XXXX.YYYY",
               "XWWWX.YWWW",
               "XWDWX.YDWY",
               "XWWWX.YWWY",
               "XWDWX.YDWY",
               "XWWWX.YWWY",
               "XXXXXXYYYY",
               "....XXY...",
               ".........."],
              {"X": C["violet2"], "Y": C["violet"], "W": C["white"], "D": C["dim"]}),
    "jpx":   (["...XXXX...",
               ".XX....XX.",
               ".X.X....X.",
               "X...X....X",
               "X....X...X",
               "X.....X..X",
               "X......X.X",
               ".X......X.",
               ".XX....XX.",
               "...XXXX..."],
              {"X": C["blue"]}),
    "dados": (["........Y.",
               "........Y.",
               ".....X..Y.",
               ".....X..Y.",
               "..Z..X..Y.",
               "..Z..X..Y.",
               "..Z..X..Y.",
               "..Z..X..Y.",
               "..........",
               "WWWWWWWWWW"],
              {"X": C["blue"], "Y": C["violet"], "Z": C["blue2"], "W": C["gray"]}),
    "mat":   (["..........",
               "XXXXXXXXXX",
               "XXXXXXXXXX",
               "..XX..XX..",
               "..XX..XX..",
               "..XX..XX..",
               "..XX..XX..",
               ".XX...XX..",
               ".XX...XXX.",
               ".........."],
              {"X": C["violet"]}),
}


def banner() -> str:
    W, H = 1200, 420
    base = Layer()
    base.rect(0, 0, W // 10, H // 10, 10, C["bg"])
    frame(base, W, H)

    # ---- Quadro de giz ----------------------------------------------------
    P = 5
    bx, by, bw, bh = 50, 52, 70, 40  # em células de 5 px
    base.rect(bx, by, bw, bh, P, C["wood"])
    base.rect(bx + P, by + P, bw - 2, bh - 2, P, C["board"])
    base.rect(bx + 6 * P, by + bh * P, 8, 1, P, C["wood"])          # bandeja
    base.rect(bx + 8 * P, by + bh * P - P, 3, 1, P, C["chalk"])    # giz
    ox, oy = bx + 6 * P, by + 22 * P                               # origem dos eixos
    base.rect(bx + 4 * P, oy, 62, 1, P, C["dim"])                  # eixo x
    base.rect(ox, by + 5 * P, 1, 32, P, C["dim"])                  # eixo y
    base.dot(bx + 65 * P, oy - P, P, C["dim"]); base.dot(bx + 65 * P, oy + P, P, C["dim"])
    base.dot(ox - P, by + 6 * P, P, C["dim"]); base.dot(ox + P, by + 6 * P, P, C["dim"])
    base.text("F(X) = SEN(X)", bx + 9 * P, by + 4 * P, 2, C["chalk"])
    base.text("E", bx + 42 * P, by + 4 * P, 2, C["chalk"])
    base.text("IΠ", bx + 42 * P + 12, by + 4 * P - 8, 2, C["violet"])
    base.text("+ 1 = 0", bx + 42 * P + 42, by + 4 * P, 2, C["chalk"])
    base.text("Σ 1/N² = Π²/6", bx + 9 * P, by + 34 * P, 2, C["chalk"])

    wave = Layer()
    for i in range(0, 58):
        y = round(10 * math.sin(i / 58 * 2 * math.pi * 1.25))
        wave.dot(ox + (i + 1) * P, oy - y * P, P, C["violet"])
    # pontos de dados (dispersão) perto da curva
    data = Layer()
    rnd = random.Random(7)
    for i in range(4, 56, 6):
        y = round(10 * math.sin(i / 58 * 2 * math.pi * 1.25)) + rnd.choice([-2, -1, 1, 2])
        data.dot(ox + (i + 1) * P, oy - y * P, P, C["blue"])

    # ---- Gráfico de barras no chão ---------------------------------------
    floor_y = 372
    base.rect(40, floor_y, 77, 1, P, C["frame"])
    bars_svg = []
    for k, (hgt, col) in enumerate([(4, C["blue2"]), (7, C["blue"]), (5, C["blue2"]),
                                    (10, C["blue"]), (13, C["violet"])]):
        x = 70 + k * 30
        hp = hgt * P
        bars_svg.append(
            f'<rect x="{x}" y="{floor_y - hp}" width="20" height="{hp}" fill="{col}">'
            f'<animate attributeName="height" values="0;{hp};{hp}" keyTimes="0;0.25;1" dur="6s" '
            f'begin="{k * 0.15}s" repeatCount="indefinite" calcMode="discrete"/>'
            f'<animate attributeName="y" values="{floor_y};{floor_y - hp};{floor_y - hp}" '
            f'keyTimes="0;0.25;1" dur="6s" begin="{k * 0.15}s" repeatCount="indefinite" calcMode="discrete"/>'
            f'</rect>'
        )

    # ---- Personagem -------------------------------------------------------
    hx, hy = 330, floor_y - len(HERO) * P
    hero = Layer()
    hero.sprite(HERO, hx, hy, P, HERO_PAL)
    for ax, ay, c in ARM:
        hero.dot(hx + ax * P, hy + ay * P, P, HERO_PAL[c])
    # Varinha/apontador do braço até a curva
    pointer = Layer()
    sx, sy = hx - 3 * P, hy + 7 * P
    for t in range(0, 13):
        pointer.dot(sx - t * P, sy - t * P, P, C["gray"])
    pointer.dot(sx - 13 * P, sy - 13 * P, P, C["white"])
    # Pálpebra (piscar)
    blink = (f'<g class="blink"><rect x="{hx + 3 * P}" y="{hy + 6 * P}" width="{P}" height="{P}" fill="{C["white"]}"/>'
             f'<rect x="{hx + 8 * P}" y="{hy + 6 * P}" width="{P}" height="{P}" fill="{C["white"]}"/></g>')

    # ---- Lado direito: HUD, nome, EXP -----------------------------------
    tx = 470
    ui = Layer()
    ui.text("PLAYER 1  ·  CIENTISTA DE DADOS", tx, 52, 3, C["gray"])
    ui.text("JOÃO PEDRO", tx, 106, 8, C["white"])
    sub = "DADOS · IA · MATEMÁTICA · AUTOMAÇÃO"
    sw = ui.text(sub, tx, 192, 3, C["violet"])
    cursor = (f'<rect class="cur" x="{tx + sw + 9}" y="192" width="15" height="21" fill="{C["white"]}"/>')

    ui.text("JOTAPE.EXP", tx, 240, 3, C["white"])
    bar_x, bar_y, bar_w, bar_h = 668, 236, 372, 30
    ui.rect(bar_x, bar_y, bar_w // 3, 1, 3, C["white"])
    ui.rect(bar_x, bar_y + bar_h - 3, bar_w // 3, 1, 3, C["white"])
    ui.rect(bar_x, bar_y, 1, bar_h // 3, 3, C["white"])
    ui.rect(bar_x + bar_w - 3, bar_y, 1, bar_h // 3, 3, C["white"])
    ui.text("LV", 1062, 240, 3, C["gray"])
    fill_w = 250
    exp_fill = (
        f'<rect x="{bar_x + 6}" y="{bar_y + 6}" height="{bar_h - 12}" width="{fill_w}" fill="{C["violet2"]}">'
        f'<animate attributeName="width" values="0;{fill_w};{fill_w}" keyTimes="0;0.6;1" dur="5s" repeatCount="indefinite"/>'
        f'</rect>'
    )
    lvl = Layer(); lvl.text("1", 1104, 240, 3, C["white"])

    # Pop-up "+1 EXP"
    pop = Layer()
    px0, py0 = 990, 112
    pop.rect(px0, py0, 52, 1, 3, C["white"]); pop.rect(px0, py0 + 39, 52, 1, 3, C["white"])
    pop.rect(px0, py0, 1, 14, 3, C["white"]); pop.rect(px0 + 153, py0, 1, 14, 3, C["white"])
    pop.text("+1 EXP", px0 + 23, py0 + 10, 3, C["white"])

    # ---- Inventário ------------------------------------------------------
    inv = Layer()
    slots = [("livro", "JOTAPE.EXP"), ("jpx", "JPX LAB"), ("dados", "DADOS"), ("mat", "MATEMÁTICA")]
    sx0, sy0, sw_, sh_, gap = 470, 290, 155, 92, 20
    for i, (ico, label) in enumerate(slots):
        x = sx0 + i * (sw_ + gap)
        rows, pal = ICONS[ico]
        inv.sprite(rows, x + (sw_ - 40) // 2, sy0 + 12, 4, pal)
        lw = text_width(label, 2)
        inv.text(label, x + (sw_ - lw) // 2, sy0 + 66, 2, C["white"])
        inv.text(str(i + 1), x + 8, sy0 + 8, 2, C["dim"])
    slot_borders = "".join(
        f'<rect x="{sx0 + i * (sw_ + gap) + 1.5}" y="{sy0 + 1.5}" width="{sw_ - 3}" height="{sh_ - 3}" '
        f'fill="none" stroke="{C["frame"]}" stroke-width="3"/>'
        for i in range(4)
    )
    slot_panels = "".join(
        f'<rect x="{sx0 + i * (sw_ + gap)}" y="{sy0}" width="{sw_}" height="{sh_}" fill="{C["panel"]}"/>'
        for i in range(4)
    )
    xs = ";".join(str(sx0 + i * (sw_ + gap) - 4.5) for i in range(4))
    selector = (
        f'<rect x="{sx0 - 4.5}" y="{sy0 - 4.5}" width="{sw_ + 9}" height="{sh_ + 9}" fill="none" '
        f'stroke="{C["white"]}" stroke-width="3">'
        f'<animate attributeName="x" values="{xs}" dur="8s" repeatCount="indefinite" calcMode="discrete"/>'
        f'</rect>'
    )

    def avoid(x, y):
        return (40 <= x <= 420 and 40 <= y <= 380) or (460 <= x <= 1170 and 40 <= y <= 390 and not (y < 100 and x > 1050)) or y > 380

    style = (
        "<style>"
        ".tw{animation-name:tw;animation-iteration-count:infinite;animation-timing-function:steps(2,jump-none)}"
        "@keyframes tw{0%,100%{opacity:1}50%{opacity:.15}}"
        ".cur{animation:bl 1s steps(1) infinite}"
        "@keyframes bl{0%{opacity:1}50%{opacity:0}}"
        ".blink{opacity:0;animation:ey 4s steps(1) infinite}"
        "@keyframes ey{0%,92%{opacity:0}93%,97%{opacity:1}98%{opacity:0}}"
        ".bob{animation:bob 1.2s steps(1) infinite}"
        "@keyframes bob{0%{transform:translateY(0)}50%{transform:translateY(-5px)}}"
        ".pop{animation:pop 3s steps(6) infinite}"
        "@keyframes pop{0%{transform:translateY(10px);opacity:0}15%{opacity:1}70%{transform:translateY(-10px);opacity:1}100%{transform:translateY(-15px);opacity:0}}"
        ".dt{animation:dt 6s steps(1) infinite}"
        "@keyframes dt{0%,35%{opacity:0}36%,100%{opacity:1}}"
        "@media (prefers-reduced-motion:reduce){*{animation:none!important}}"
        "</style>"
    )
    wave_clip = (
        '<clipPath id="wv"><rect x="0" y="0" height="420" width="420">'
        '<animate attributeName="width" values="80;420;420" keyTimes="0;0.5;1" dur="6s" repeatCount="indefinite"/>'
        '</rect></clipPath>'
    )
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
        f'shape-rendering="crispEdges" role="img" aria-label="João Pedro — Dados, IA, Matemática e Automação">'
        f"<title>João Pedro · jotape.exp · JPX Lab</title>{style}<defs>{wave_clip}</defs>"
        f"{base.svg()}{stars(W, H, 34, 3, avoid)}"
        f'<g clip-path="url(#wv)">{wave.svg()}</g>{data.svg('class="dt"')}'
        f"{''.join(bars_svg)}"
        f'<g class="bob">{pointer.svg()}{hero.svg()}{blink}</g>'
        f"{ui.svg()}{cursor}{exp_fill}{lvl.svg()}"
        f'<g class="pop">{pop.svg()}</g>'
        f"{slot_panels}{inv.svg()}{slot_borders}{selector}"
        f"</svg>"
    )


def footer() -> str:
    W, H = 1200, 170
    base = Layer()
    base.rect(0, 0, W // 10, H // 10 + 1, 10, C["bg"])
    frame(base, W, H)
    # chão em blocos
    for i in range(0, 228):
        x = 30 + i * 5
        if x > W - 35:
            break
        base.dot(x, 116, 5, C["frame"] if (i // 4) % 2 else C["wood"])
    ui = Layer()
    t1 = "OBRIGADO PELA VISITA!"
    w1 = text_width(t1, 5)
    ui.text(t1, (W - w1) // 2, 36, 5, C["white"])
    t2 = "CONTINUE?"
    t3 = "SIM      NÃO"
    w2 = text_width(t2 + "   " + t3, 3) + 30
    x2 = (W - w2) // 2
    ui.text(t2, x2, 80, 3, C["gray"])
    xs = x2 + text_width(t2 + "   ", 3) + 30
    ui.text(t3, xs, 80, 3, C["white"])
    arrow = Layer(); arrow.text(">", xs - 30, 80, 3, C["violet"])
    motto = Layer()
    motto.text("LER ANTES DE CALCULAR.", 48, 128, 2, C["dim"])
    m2 = "JOTAPE.EXP · JPX LAB"
    motto.text(m2, W - 48 - text_width(m2, 2), 128, 2, C["dim"])
    style = ("<style>.cur{animation:bl 1s steps(1) infinite}@keyframes bl{0%{opacity:1}50%{opacity:0}}"
             ".tw{animation-name:tw;animation-iteration-count:infinite;animation-timing-function:steps(2,jump-none)}"
             "@keyframes tw{0%,100%{opacity:1}50%{opacity:.15}}"
             "@media (prefers-reduced-motion:reduce){*{animation:none!important}}</style>")

    def avoid(x, y):
        return y > 105 or (280 <= x <= 920 and 28 <= y <= 110)

    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
        f'shape-rendering="crispEdges" role="img" aria-label="Obrigado pela visita">'
        f"<title>Obrigado pela visita</title>{style}"
        f"{base.svg()}{stars(W, H, 14, 11, avoid)}{ui.svg()}"
        f'<g class="cur">{arrow.svg()}</g>{motto.svg()}</svg>'
    )


if __name__ == "__main__":
    (ASSETS / "banner.svg").write_text(banner(), encoding="utf-8")
    (ASSETS / "footer.svg").write_text(footer(), encoding="utf-8")
    print("ok:", ASSETS / "banner.svg", ASSETS / "footer.svg")
