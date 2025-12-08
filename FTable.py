from textwrap import dedent
from pathlib import Path

def ascii_to_tikz(ascii_text,
                  xscale=0.35, yscale=0.35,
                  open_radius=0.18,
                  filled_radius=0.35,
                  filled_thickness="ultra thick",
                  symmetric=True,
                  output_path="plus_star_symmetric.tex"):
    # --- Parse rows of + and * ---
    rows = []
    for line in ascii_text.strip().splitlines():
        tokens = [t for t in line.strip().split() if t in ['+','*']]
        if tokens:
            rows.append(tokens)

    # --- Enforce horizontal symmetry per row ---
    if symmetric:
        for row in rows:
            n = len(row)
            for c in range(n // 2):
                m = n - 1 - c
                if row[c] != row[m]:
                    # if either is *, both become *
                    if row[c] == '*' or row[m] == '*':
                        row[c] = row[m] = '*'
                    else:
                        row[c] = row[m] = '+'

    # --- Build TikZ code ---
    lines = []
    lines.append(r"\documentclass[tikz,border=5pt]{standalone}")
    lines.append(r"\usepackage{tikz}")
    lines.append(r"\begin{document}")
    lines.append(rf"\begin{{tikzpicture}}[x={xscale}cm,y={yscale}cm,line cap=round]")

    for r, row in enumerate(rows):
        n = len(row)
        yoff = -(n - 1) / 2.0
        for c, t in enumerate(row):
            x = float(r)
            y = yoff + c
            if t == '*':
                # bold filled black dot
                lines.append(
                    f"  \\filldraw[{filled_thickness}] ({x:.3f}, {y:.3f}) circle [radius={filled_radius:.3f}];"
                )
            else:
                # open circle
                lines.append(
                    f"  \\draw ({x:.3f}, {y:.3f}) circle [radius={open_radius:.3f}];"
                )

    lines.append(r"\end{tikzpicture}")
    lines.append(r"\end{document}")

    tikz_code = "\n".join(lines)

    # --- Save to file ---
    Path(output_path).write_text(tikz_code, encoding="utf-8")

    # --- Print full TikZ code ---
    print(tikz_code)
    print(f"\n\nTikZ code saved to: {output_path}\n")

    return tikz_code


# Example usage
if __name__ == "__main__":
    ascii_art = dedent("""
+ 
+  +  
+  +  +  
+  +  +  +  
+  +  +  +  +  
+  +  +  +  +  +  
+  +  +  +  +  +  +  
+  +  +  +  +  +  +  +  
+  +  +  +  +  +  +  +  +  
* * +  +  +  +  +  +  * *
+  +  +  * +  * +  +  +  
+  * * +  * * +  * * +  
* * +  * +  +  +  * +  * *
* +  * * +  +  * * +  *
* * * +  +  +  +  +  * * *
+  +  +  +  * * +  +  +  +  
+  * * +  * +  * +  * * +  
* +  +  * * +  +  * * +  +  *
* * +  +  +  +  +  +  +  * *
* * +  * +  * * +  * +  * *
* +  * * +  +  +  * * +  *
* +  * +  * +  +  * +  * +  *
+  * * * +  +  +  * * * +  
+  * * * +  +  +  +  * * * +  
* * * +  * * +  * * +  * * *
+  * * +  * +  +  * +  * * +  
* * * +  * * +  * * +  * * *
+  * * * +  +  +  +  * * * +  
* * * * * +  +  +  * * * * *
+  * +  * +  * * +  * +  * +  
* * * +  * * +  * * +  * * *
+  * +  +  * * * * +  +  * +  
* * * +  * * +  * * +  * * *
+  * +  * +  * * +  * +  * +  
* * * * * +  +  +  * * * * *
+  * * * +  +  +  +  * * * +  
* * +  * * +  +  +  * * +  * *
+  * +  * +  +  +  +  * +  * +  
* * +  +  * +  +  +  * +  +  * *
+  * +  +  +  +  +  +  +  +  * +  
* * +  +  +  +  +  +  +  +  +  * *
+  * +  +  * +  +  * +  +  * +  
* * +  +  * +  +  +  * +  +  * *
+  * +  * * +  +  * * +  * +  
* * +  * * +  +  +  * * +  * *
+  * * * * +  +  * * * * +  
* * * * * +  +  +  * * * * *
+  +  * * * +  +  * * * +  +  
* * +  * * +  +  +  * * +  * *
+  +  +  * * +  +  * * +  +  +  
* * +  +  * +  +  +  * +  +  * *
+  +  +  +  * +  +  * +  +  +  +  
* * +  +  +  +  +  +  +  +  +  * *
+  +  +  +  +  +  +  +  +  +  +  +  
* * +  +  +  * +  * +  +  +  * *
+  +  +  +  * +  +  * +  +  +  +  
* * +  +  * * +  * * +  +  * *
+  +  +  * * +  +  * * +  +  +  
* * +  * * * +  * * * +  * *
+  +  * * * +  +  * * * +  +  
* * * * * * +  * * * * * *
+  * * * * +  +  * * * * +  
* +  * * * * +  * * * * +  *
+  +  * * * +  +  * * * +  +  
* +  +  * * * +  * * * +  +  *
+  +  +  * * +  +  * * +  +  +  
* +  +  +  * * +  * * +  +  +  *
+  +  +  +  * +  +  * +  +  +  +  
* +  +  +  +  * +  * +  +  +  +  *
+  +  +  +  +  +  +  +  +  +  +  +  
* +  +  +  +  +  +  +  +  +  +  +  *
+  +  +  +  +  * * +  +  +  +  +  
* +  +  +  +  * +  * +  +  +  +  *
+  +  +  +  * * * * +  +  +  +  
* +  +  +  * * +  * * +  +  +  *
+  +  +  * * * * * * +  +  +  
* +  +  * * * +  * * * +  +  *
+  +  * * * * * * * * +  +  
* +  * * * * +  * * * * +  *
+  * * * * * * * * * * +  
* * * * * * +  * * * * * *
* * * * * * * * * * * *
* * * * * +  * * * * *
* * * * * * * * * *
* * * * +  * * * *
* * * * * * * *
* * * +  * * *
* * * * * *
* * +  * *
* * * *
* +  *
* *
    """)
    ascii_to_tikz(ascii_art)
