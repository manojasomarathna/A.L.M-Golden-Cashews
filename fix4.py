# -*- coding: utf-8 -*-
path = r'c:\Users\Admin\Desktop\A.L.M. Golden Cashews\alm_golden_cashews.html'

with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'Order Any Product' in line and 'btn-primary' in line:
        # Replace this line with two buttons
        lines[i] = '    <div style="display:flex;gap:1rem;flex-wrap:wrap;">\n      <a href="cashew-prices.html" class="btn-primary">\U0001f4b0 View Prices &amp; Packs</a>\n      <a href="#sales" class="btn-primary" style="background:transparent;border:1px solid var(--gold);color:var(--gold);">Order Now \u2192</a>\n    </div>\n'
        print(f"Replaced line {i+1}")
        break

with open(path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Done!")
