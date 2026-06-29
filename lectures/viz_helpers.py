"""
viz_helpers.py
================
Shared visual language used by the `visualize()` function inside every
lecture module. Each lecture calls into this module to render its own
figures using the SAME palette, so the whole masterclass looks like one
course. Figures are saved to figures/ AND shown inline if a display is
available (plt.show() is a no-op-safe call in headless environments after
saving, since we always save first).
"""

import os
import matplotlib
matplotlib.use("Agg")  # safe in headless/server environments; figures are saved to disk
import matplotlib.pyplot as plt
import matplotlib as mpl

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
FIGURES_DIR = os.path.join(THIS_DIR, "figures")
os.makedirs(FIGURES_DIR, exist_ok=True)

SPHERICAL = "#1B3B6F"     # deep blue  (h = -1/3, gamma5 = -1, left-handed)
HYPERBOLIC = "#D98A2B"    # warm amber (h = +1/3, gamma5 = +1, right-handed)
SEAM_LINE = "#A8324A"     # the seam boundary itself
NEUTRAL = "#3C3C3C"
GRID = "#DDDDDD"
ACCENT_GEN = ["#1B3B6F", "#5C8A8A", "#D98A2B"]   # generation 1, 2, 3
LIMITATION_RED = "#B23A48"

mpl.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 11,
    "axes.edgecolor": NEUTRAL,
    "axes.labelcolor": NEUTRAL,
    "xtick.color": NEUTRAL,
    "ytick.color": NEUTRAL,
    "axes.grid": True,
    "grid.color": GRID,
    "grid.linewidth": 0.6,
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "savefig.dpi": 150,
    "savefig.bbox": "tight",
})


def new_figure(figsize=(8, 5), title=None):
    fig, ax = plt.subplots(figsize=figsize)
    if title:
        ax.set_title(title, fontsize=12.5, fontweight="bold", color=NEUTRAL, pad=12)
    return fig, ax


def show_and_save(fig, name, lecture_label=""):
    """Save the figure to figures/, print the path, then display it inline
    (in a notebook / GUI backend this pops the window; in a headless run the
    Agg backend makes plt.show() a safe no-op after the save)."""
    path = os.path.join(FIGURES_DIR, f"{name}.png")
    fig.savefig(path)
    print(f"\n  [FIGURE] {lecture_label}{'  ' if lecture_label else ''}saved to figures/{name}.png")
    try:
        plt.show()
    except Exception:
        pass
    plt.close(fig)
    return path


def limitation_stamp(ax, text="KNOWN LIMITATION"):
    ax.text(0.985, 0.04, text, transform=ax.transAxes, ha="right", va="bottom",
             fontsize=9, fontweight="bold", color="white",
             bbox=dict(boxstyle="round,pad=0.35", facecolor=LIMITATION_RED, edgecolor="none"))
