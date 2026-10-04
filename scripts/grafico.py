# /// script
# dependencies = ["matplotlib"]
# ///
"""Gera o gráfico de exemplo nas cores da Python Brasil 2026, em versão escura e clara.

    uv run scripts/grafico.py
"""

from pathlib import Path

import matplotlib.pyplot as plt

PRETO = "#0F0F0F"
OFF_WHITE = "#E8F4BA"
LIMAO = "#B7FF06"
CINZA = "#ABABAB"
CINZA_ESCURO = "#4A4A4A"

IMG = Path(__file__).resolve().parent.parent / "img"


def contraste(a: str, b: str) -> float:
    """Razão de contraste do WCAG 2.1 entre duas cores hexadecimais."""

    def luminancia(cor: str) -> float:
        r, g, b = (int(cor.lstrip("#")[i : i + 2], 16) / 255 for i in (0, 2, 4))
        canal = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
        return 0.2126 * canal(r) + 0.7152 * canal(g) + 0.0722 * canal(b)

    claro, escuro = sorted((luminancia(a), luminancia(b)), reverse=True)
    return round((claro + 0.05) / (escuro + 0.05), 1)


def grafico(arquivo: str, fundo: str, texto: str, cores: dict[str, str], minimo: str = "Mínimo", decimal: str = ",") -> None:
    rotulos = [*cores, minimo]
    valores = [*(contraste(cor, fundo) for cor in cores.values()), 4.5]

    plt.rcParams["font.family"] = ["Roboto", "DejaVu Sans"]
    fig, ax = plt.subplots(figsize=(11.5, 4.6), dpi=150, facecolor=fundo)
    ax.set_facecolor(fundo)
    # As barras ficam limão nos dois fundos: o número sobre cada barra leva a informação.
    barras = ax.bar(rotulos, valores, color=LIMAO, width=0.5)
    ax.bar_label(barras, labels=[f"{v:.1f}".replace(".", decimal) for v in valores], padding=6, color=texto, fontsize=18, fontweight="bold")
    ax.tick_params(axis="x", colors=texto, labelsize=18, length=0)
    ax.set_yticks([])
    for borda in ax.spines.values():
        borda.set_visible(False)
    fig.tight_layout()
    # Fundo transparente: o gráfico pega a cor do slide, sem um retângulo em volta.
    fig.savefig(IMG / arquivo, transparent=True)


# Um gráfico por idioma dos slides: rótulos e separador decimal de cada um.
IDIOMAS = {
    "": {"texto": "Texto", "limao": "Limão", "cinza": "Cinza", "minimo": "Mínimo", "decimal": ","},
    "-en": {"texto": "Text", "limao": "Lime", "cinza": "Gray", "minimo": "Minimum", "decimal": "."},
    "-es": {"texto": "Texto", "limao": "Lima", "cinza": "Gris", "minimo": "Mínimo", "decimal": ","},
}

for sufixo, r in IDIOMAS.items():
    grafico(f"grafico-contraste{sufixo}.png", PRETO, OFF_WHITE, {r["texto"]: OFF_WHITE, r["limao"]: LIMAO, r["cinza"]: CINZA}, r["minimo"], r["decimal"])
    grafico(f"grafico-contraste-claro{sufixo}.png", "#FFFFFF", PRETO, {r["texto"]: PRETO, r["cinza"]: CINZA_ESCURO}, r["minimo"], r["decimal"])
