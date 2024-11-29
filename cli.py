from PySide6.QtGui import QTextLayout
from PySide6.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    argv = sys.argv
    if len(argv) < 2:
        text = "(╯‵□′)╯︵┻━┻"
    else:
        text = argv[1]
    app = QApplication()
    layout = QTextLayout(text)
    layout.beginLayout()
    layout.createLine()
    layout.endLayout()
    line = layout.lineAt(0)
    w = line.naturalTextWidth()
    size = layout.font().pointSize()
    delta_y = line.ascent()
    print(r"\begingroup")
    print(r"\begin{picture}(%.2fem, 1em)" % (w / 12))
    for run in layout.glyphRuns():
        name = run.rawFont().familyName()
        for g, p in zip(run.glyphIndexes(), run.positions()):
            print(
                r"\put(%.2fem,%.2fem){\fontspec{%s}\XeTeXglyph%d}" % (
                    p.x() / 12, (p.y() - delta_y) / 12, name, g
                )
            )
    print(r"\end{picture}")
    print(r"\endgroup")

# cli.py​
