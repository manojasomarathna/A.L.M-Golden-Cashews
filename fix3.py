# -*- coding: utf-8 -*-
path = r'c:\Users\Admin\Desktop\A.L.M. Golden Cashews\alm_golden_cashews.html'

with open(path, 'r', encoding='utf-8') as f:
    c = f.read()

old = '<a href="#sales" class="order-btn">Order</a>\n        </div>\n      </div>\n\n    </div>\n    <div class="product-card">\n\n      <div class="product-img bg1" style="background: linear-gradient(135deg,#FEF9C3,#FDE047)">'

new = '<a href="tel:+94742770633" class="order-btn">📞 Call</a>\n        </div>\n        <div style="margin-top:0.75rem;">\n          <a href="retail-packed-cashews.html" style="display:block;text-align:center;background:var(--dark);color:var(--gold-light);padding:0.55rem 1rem;border-radius:6px;font-size:0.82rem;font-weight:600;text-decoration:none;border:1px solid rgba(200,146,42,0.3);">📄 View Details &amp; Order \u2192</a>\n        </div>\n      </div>\n\n    </div>\n    <div class="product-card">\n\n      <div class="product-img bg1" style="background: linear-gradient(135deg,#FEF9C3,#FDE047)">'

if old in c:
    c = c.replace(old, new)
    print("Done!")
else:
    # try with \r\n
    old2 = old.replace('\n', '\r\n')
    new2 = new.replace('\n', '\r\n')
    if old2 in c:
        c = c.replace(old2, new2)
        print("Done with CRLF!")
    else:
        print("Still not found")

with open(path, 'w', encoding='utf-8') as f:
    f.write(c)
