# -*- coding: utf-8 -*-
import os

files = [
    r'c:\Users\Admin\Desktop\A.L.M. Golden Cashews\alm_golden_cashews.html',
    r'c:\Users\Admin\Desktop\A.L.M. Golden Cashews\cashew-prices.html',
    r'c:\Users\Admin\Desktop\A.L.M. Golden Cashews\retail-packed-cashews.html',
]

for path in files:
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    old = '    <a href="retail-packed-cashews.html" class="nav-page-btn">📦 <span>Retail Packs</span></a>\n  </div>'
    new = '    <a href="retail-packed-cashews.html" class="nav-page-btn">📦 <span>Retail Packs</span></a>\n    <a href="suppliers.html" class="nav-page-btn">🌳 <span>Suppliers</span></a>\n  </div>'
    if old in c:
        c = c.replace(old, new)
        print(f"Updated: {os.path.basename(path)}")
    else:
        print(f"Not found in: {os.path.basename(path)}")
    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)

print("Done!")
