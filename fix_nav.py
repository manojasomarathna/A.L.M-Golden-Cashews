# -*- coding: utf-8 -*-

NAV_CSS = """
  .nav-pages { display: flex; gap: 0.5rem; align-items: center; }
  .nav-page-btn {
    color: rgba(255,255,255,0.75);
    text-decoration: none;
    font-size: 0.85rem;
    font-weight: 500;
    padding: 0.4rem 0.9rem;
    border-radius: 5px;
    border: 1px solid transparent;
    transition: all 0.2s;
    white-space: nowrap;
  }
  .nav-page-btn:hover { color: var(--gold-light); border-color: rgba(200,146,42,0.4); }
  .nav-page-btn.active { background: var(--gold); color: var(--dark) !important; border-color: var(--gold); font-weight: 600; }
  @media (max-width: 600px) {
    .nav-page-btn span { display: none; }
  }
"""

# ── MAIN SITE ──────────────────────────────────────────────
main_path = r'c:\Users\Admin\Desktop\A.L.M. Golden Cashews\alm_golden_cashews.html'
with open(main_path, 'r', encoding='utf-8') as f:
    c = f.read()

# Add CSS before closing </style>
c = c.replace('</style>\n</head>', NAV_CSS + '\n</style>\n</head>')

# Replace nav
old_nav = '''<nav>
  <a class="nav-logo" href="#home">A.L.M. Golden Cashews <span>Premium Sri Lankan Cashews</span></a>
  <ul class="nav-links">
    <li><a href="#home">Home</a></li>
    <li><a href="#about">Our Process</a></li>
    <li><a href="#products">Products</a></li>
    <li><a href="#sales">Order Now</a></li>
    <li><a href="#contact" class="nav-cta">Contact</a></li>
  </ul>
</nav>'''

new_nav = '''<nav>
  <a class="nav-logo" href="#home">A.L.M. Golden Cashews <span>Premium Sri Lankan Cashews</span></a>
  <div style="display:flex;align-items:center;gap:1.5rem;">
    <div class="nav-pages">
      <a href="alm_golden_cashews.html" class="nav-page-btn active">🏠 <span>Home</span></a>
      <a href="cashew-prices.html" class="nav-page-btn">💰 <span>Prices</span></a>
      <a href="retail-packed-cashews.html" class="nav-page-btn">📦 <span>Retail Packs</span></a>
    </div>
    <ul class="nav-links">
      <li><a href="#about">Our Process</a></li>
      <li><a href="#products">Products</a></li>
      <li><a href="#sales">Order Now</a></li>
      <li><a href="#contact" class="nav-cta">Contact</a></li>
    </ul>
  </div>
</nav>'''

if old_nav in c:
    c = c.replace(old_nav, new_nav)
    print("Main nav updated!")
else:
    print("Main nav pattern not found - trying CRLF")
    old_nav2 = old_nav.replace('\n', '\r\n')
    new_nav2 = new_nav.replace('\n', '\r\n')
    if old_nav2 in c:
        c = c.replace(old_nav2, new_nav2)
        print("Main nav updated with CRLF!")
    else:
        print("Main nav still not found")

with open(main_path, 'w', encoding='utf-8') as f:
    f.write(c)


# ── PRICES PAGE ────────────────────────────────────────────
prices_path = r'c:\Users\Admin\Desktop\A.L.M. Golden Cashews\cashew-prices.html'
with open(prices_path, 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('</style>\n</head>', NAV_CSS + '\n</style>\n</head>')

old_nav_p = '''<nav>
  <a class="nav-logo" href="alm_golden_cashews.html">A.L.M. Golden Cashews <span>Premium Sri Lankan Cashews</span></a>
  <a class="nav-back" href="alm_golden_cashews.html">\u2190 Back to Main Site</a>
</nav>'''

new_nav_p = '''<nav>
  <a class="nav-logo" href="alm_golden_cashews.html">A.L.M. Golden Cashews <span>Premium Sri Lankan Cashews</span></a>
  <div class="nav-pages">
    <a href="alm_golden_cashews.html" class="nav-page-btn">🏠 <span>Home</span></a>
    <a href="cashew-prices.html" class="nav-page-btn active">💰 <span>Prices</span></a>
    <a href="retail-packed-cashews.html" class="nav-page-btn">📦 <span>Retail Packs</span></a>
  </div>
</nav>'''

if old_nav_p in c:
    c = c.replace(old_nav_p, new_nav_p)
    print("Prices nav updated!")
else:
    old_nav_p2 = old_nav_p.replace('\n', '\r\n')
    new_nav_p2 = new_nav_p.replace('\n', '\r\n')
    if old_nav_p2 in c:
        c = c.replace(old_nav_p2, new_nav_p2)
        print("Prices nav updated with CRLF!")
    else:
        print("Prices nav not found")

with open(prices_path, 'w', encoding='utf-8') as f:
    f.write(c)


# ── RETAIL PAGE ────────────────────────────────────────────
retail_path = r'c:\Users\Admin\Desktop\A.L.M. Golden Cashews\retail-packed-cashews.html'
with open(retail_path, 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('</style>\n</head>', NAV_CSS + '\n</style>\n</head>')

old_nav_r = '''<nav>
  <a class="nav-logo" href="alm_golden_cashews.html">A.L.M. Golden Cashews <span>Premium Sri Lankan Cashews</span></a>
  <a class="nav-back" href="alm_golden_cashews.html">\u2190 Back to Main Site</a>
</nav>'''

new_nav_r = '''<nav>
  <a class="nav-logo" href="alm_golden_cashews.html">A.L.M. Golden Cashews <span>Premium Sri Lankan Cashews</span></a>
  <div class="nav-pages">
    <a href="alm_golden_cashews.html" class="nav-page-btn">🏠 <span>Home</span></a>
    <a href="cashew-prices.html" class="nav-page-btn">💰 <span>Prices</span></a>
    <a href="retail-packed-cashews.html" class="nav-page-btn active">📦 <span>Retail Packs</span></a>
  </div>
</nav>'''

if old_nav_r in c:
    c = c.replace(old_nav_r, new_nav_r)
    print("Retail nav updated!")
else:
    old_nav_r2 = old_nav_r.replace('\n', '\r\n')
    new_nav_r2 = new_nav_r.replace('\n', '\r\n')
    if old_nav_r2 in c:
        c = c.replace(old_nav_r2, new_nav_r2)
        print("Retail nav updated with CRLF!")
    else:
        print("Retail nav not found")

with open(retail_path, 'w', encoding='utf-8') as f:
    f.write(c)

print("\nAll done!")
