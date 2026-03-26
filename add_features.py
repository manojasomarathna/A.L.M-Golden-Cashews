# -*- coding: utf-8 -*-

# ── WHATSAPP FLOATING BUTTON CSS + HTML ──
WA_FLOAT_CSS = """
  .wa-float {
    position: fixed; bottom: 1.5rem; right: 1.5rem; z-index: 9998;
    background: #25D366; color: white;
    width: 58px; height: 58px; border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    box-shadow: 0 4px 20px rgba(37,211,102,0.5);
    text-decoration: none; font-size: 1.6rem;
    transition: all 0.3s;
    animation: waPulse 2s infinite;
  }
  .wa-float:hover { transform: scale(1.12); box-shadow: 0 6px 28px rgba(37,211,102,0.6); }
  @keyframes waPulse {
    0% { box-shadow: 0 4px 20px rgba(37,211,102,0.5); }
    50% { box-shadow: 0 4px 30px rgba(37,211,102,0.8); }
    100% { box-shadow: 0 4px 20px rgba(37,211,102,0.5); }
  }
"""

WA_FLOAT_HTML = """
<!-- WhatsApp Float -->
<a href="https://wa.me/94742770633" target="_blank" class="wa-float" title="Chat on WhatsApp">
  <svg width="28" height="28" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347z"/><path d="M12 0C5.373 0 0 5.373 0 12c0 2.025.507 3.934 1.397 5.61L0 24l6.545-1.378A11.945 11.945 0 0012 24c6.627 0 12-5.373 12-12S18.627 0 12 0zm0 22c-1.885 0-3.652-.51-5.17-1.4l-.37-.22-3.884.818.824-3.785-.241-.389A9.929 9.929 0 012 12C2 6.477 6.477 2 12 2s10 4.477 10 10-4.477 10-10 10z"/></svg>
</a>
"""

# ── REVIEWS SECTION ──
REVIEWS_CSS = """
  #reviews { background: var(--cream); }
  .reviews-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1.5rem; margin-top: 3rem;
  }
  .review-card {
    background: var(--white);
    border-radius: 14px;
    padding: 1.75rem;
    border: 1px solid rgba(200,146,42,0.12);
    transition: transform 0.2s, box-shadow 0.2s;
  }
  .review-card:hover { transform: translateY(-4px); box-shadow: 0 12px 35px rgba(200,146,42,0.12); }
  .review-stars { color: var(--gold); font-size: 1.1rem; margin-bottom: 0.75rem; letter-spacing: 2px; }
  .review-text { font-size: 0.92rem; color: var(--text); line-height: 1.7; margin-bottom: 1.25rem; font-style: italic; }
  .review-author { display: flex; align-items: center; gap: 0.75rem; }
  .review-avatar {
    width: 42px; height: 42px; border-radius: 50%;
    background: linear-gradient(135deg, var(--gold), var(--gold-light));
    display: flex; align-items: center; justify-content: center;
    font-weight: 700; color: var(--dark); font-size: 1rem;
  }
  .review-name { font-weight: 600; color: var(--dark); font-size: 0.9rem; }
  .review-location { font-size: 0.78rem; color: var(--text-light); }
"""

REVIEWS_HTML = """
<!-- REVIEWS -->
<section id="reviews">
  <span class="section-tag">Customer Reviews</span>
  <h2 class="section-title">What Our Customers Say</h2>
  <p class="section-sub">Real feedback from our valued customers across Sri Lanka.</p>
  <div class="reviews-grid">
    <div class="review-card">
      <div class="review-stars">★★★★★</div>
      <p class="review-text">"Best cashews I have ever bought! Fresh, clean, and great quality. My shop customers love them. Will order again!"</p>
      <div class="review-author">
        <div class="review-avatar">K</div>
        <div><div class="review-name">Kamal Perera</div><div class="review-location">Colombo</div></div>
      </div>
    </div>
    <div class="review-card">
      <div class="review-stars">★★★★★</div>
      <p class="review-text">"Ordered 10kg bulk. Delivery was fast and the cashews were perfectly packed. Price is very reasonable. Highly recommend!"</p>
      <div class="review-author">
        <div class="review-avatar">S</div>
        <div><div class="review-name">Suresh Fernando</div><div class="review-location">Kandy</div></div>
      </div>
    </div>
    <div class="review-card">
      <div class="review-stars">★★★★★</div>
      <p class="review-text">"Farm fresh quality is unmatched. You can taste the difference. Our supermarket stocks only A.L.M. Golden Cashews now."</p>
      <div class="review-author">
        <div class="review-avatar">N</div>
        <div><div class="review-name">Nimal Silva</div><div class="review-location">Kurunegala</div></div>
      </div>
    </div>
    <div class="review-card">
      <div class="review-stars">★★★★★</div>
      <p class="review-text">"Very honest and reliable supplier. Called them, got the price immediately, and received my order the next day. Excellent service!"</p>
      <div class="review-author">
        <div class="review-avatar">A</div>
        <div><div class="review-name">Amara Dissanayake</div><div class="review-location">Gampaha</div></div>
      </div>
    </div>
  </div>
</section>
"""

# ── GOOGLE MAPS ──
MAPS_HTML = """      <div class="contact-card">
        <div class="icon">🗺️</div>
        <h4>Find Us</h4>
        <div style="margin-top:0.75rem;border-radius:10px;overflow:hidden;border:1px solid rgba(200,146,42,0.2);">
          <iframe
            src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3956.0!2d79.9!3d7.9!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2sAnamaduwa%2C+Sri+Lanka!5e0!3m2!1sen!2slk!4v1"
            width="100%" height="180" style="border:0;display:block;" allowfullscreen="" loading="lazy">
          </iframe>
        </div>
        <p style="margin-top:0.5rem;font-size:0.8rem;color:#aaa;">Diulwewa, Anamaduwa, NWP</p>
      </div>"""

# ── FRESH STOCK NOTICE ──
STOCK_NOTICE = """  <!-- Fresh Stock Notice -->
  <div style="background:rgba(59,94,43,0.15);border:1px solid rgba(59,94,43,0.4);border-radius:8px;padding:0.6rem 1.2rem;display:inline-flex;align-items:center;gap:0.5rem;margin-bottom:1.5rem;position:relative;">
    <span style="width:8px;height:8px;background:#4ade80;border-radius:50%;display:inline-block;animation:waPulse 1.5s infinite;"></span>
    <span style="color:#4ade80;font-size:0.82rem;font-weight:600;letter-spacing:0.5px;">Fresh Stock Available Now</span>
  </div>
"""

# ══════════════════════════════════════════
# UPDATE MAIN SITE
# ══════════════════════════════════════════
main_path = r'c:\Users\Admin\Desktop\A.L.M. Golden Cashews\alm_golden_cashews.html'
with open(main_path, 'r', encoding='utf-8') as f:
    c = f.read()

# 1. Add WA float CSS + Reviews CSS
c = c.replace('</style>\n</head>', REVIEWS_CSS + WA_FLOAT_CSS + '\n</style>\n</head>')

# 2. Add fresh stock notice before hero-badge
c = c.replace('    <div class="hero-badge">', STOCK_NOTICE + '    <div class="hero-badge">')

# 3. Add reviews section before footer
c = c.replace('\n<!-- FOOTER -->', REVIEWS_HTML + '\n<!-- FOOTER -->')

# 4. Add Google Maps - replace location contact card
old_map = '''    <div class="contact-card">
      <div class="icon">📍</div>
      <h4>Location</h4>
      <p>Diulwewa, Anamaduwa<br>North Western Province, Sri Lanka<br><span style="font-size:0.8rem;color:#aaa">Island-wide delivery available</span></p>
    </div>'''
c = c.replace(old_map, MAPS_HTML)

# 5. Add WA float before </body>
c = c.replace('</body>\n</html>', WA_FLOAT_HTML + '\n</body>\n</html>')

with open(main_path, 'w', encoding='utf-8') as f:
    f.write(c)
print("Main site updated!")

# ══════════════════════════════════════════
# UPDATE PRICES PAGE
# ══════════════════════════════════════════
prices_path = r'c:\Users\Admin\Desktop\A.L.M. Golden Cashews\cashew-prices.html'
with open(prices_path, 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('</style>\n</head>', WA_FLOAT_CSS + '\n</style>\n</head>')
c = c.replace('</body>\n</html>', WA_FLOAT_HTML + '\n</body>\n</html>')

with open(prices_path, 'w', encoding='utf-8') as f:
    f.write(c)
print("Prices page updated!")

# ══════════════════════════════════════════
# UPDATE RETAIL PAGE
# ══════════════════════════════════════════
retail_path = r'c:\Users\Admin\Desktop\A.L.M. Golden Cashews\retail-packed-cashews.html'
with open(retail_path, 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('</style>\n</head>', WA_FLOAT_CSS + '\n</style>\n</head>')
c = c.replace('</body>\n</html>', WA_FLOAT_HTML + '\n</body>\n</html>')

with open(retail_path, 'w', encoding='utf-8') as f:
    f.write(c)
print("Retail page updated!")

print("\nAll done!")
