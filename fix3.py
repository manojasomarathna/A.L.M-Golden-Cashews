# -*- coding: utf-8 -*-
path = r'c:\Users\Admin\Desktop\A.L.M. Golden Cashews\alm_golden_cashews.html'

with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Line 699 (index 698) - change Order to Call
lines[698] = '          <a href="tel:+94742770633" class="order-btn">\U0001f4de Call</a>\n'

# After line 700 (index 700 = </div>), insert view details button before </div>
# Insert after index 700 (which is '      </div>\n' - closing product-body)
lines.insert(700, '        <div style="margin-top:0.75rem;"><a href="retail-packed-cashews.html" style="display:block;text-align:center;background:var(--dark);color:var(--gold-light);padding:0.55rem 1rem;border-radius:6px;font-size:0.82rem;font-weight:600;text-decoration:none;border:1px solid rgba(200,146,42,0.3);">\U0001f4c4 View Details &amp; Order \u2192</a></div>\n')

with open(path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Done!")
