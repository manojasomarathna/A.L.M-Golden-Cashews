# -*- coding: utf-8 -*-
path = r'c:\Users\Admin\Desktop\A.L.M. Golden Cashews\alm_golden_cashews.html'

with open(path, 'r', encoding='utf-8') as f:
    c = f.read()

old = '<div class="product-desc">Hygienically packed in 250g, 500g &amp; 1kg retail bags. Ready-to-sell for shops and supermarkets.</div>'
new = '<div class="product-desc">Hygienically packed in 250g, 500g &amp; 1kg retail bags. Ready-to-sell for shops and supermarkets. Bulk quantities also available — call us for bulk pricing!<br><small style="color:var(--gold);font-weight:600;">Call for price: 0742770633</small></div>'

if old in c:
    c = c.replace(old, new)
    print("Replaced with &amp;")
else:
    old2 = '<div class="product-desc">Hygienically packed in 250g, 500g & 1kg retail bags. Ready-to-sell for shops and supermarkets.</div>'
    new2 = '<div class="product-desc">Hygienically packed in 250g, 500g & 1kg retail bags. Ready-to-sell for shops and supermarkets. Bulk quantities also available — call us for bulk pricing!<br><small style="color:var(--gold);font-weight:600;">Call for price: 0742770633</small></div>'
    c = c.replace(old2, new2)
    print("Replaced with &")

with open(path, 'w', encoding='utf-8') as f:
    f.write(c)

print("Done")

