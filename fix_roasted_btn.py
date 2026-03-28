with open('cashew-guide.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Remove the wrapper div around the button and move button inside image section
old = '''      <div class="price-badge">

        <div class="plabel">Price Range</div>
        <div class="prange">Rs. 3,450'''

# Find the roasted card image section and add button there
old2 = '<div class="type-num">3</div>\n      </div>'
new2 = '''<div class="type-num">3</div>
        <a href="roasted-cashews.html" style="position:absolute;bottom:12px;left:50%;transform:translateX(-50%);background:rgba(200,146,42,0.95);color:#1A1208;padding:0.45rem 1.1rem;border-radius:20px;font-size:0.78rem;font-weight:700;text-decoration:none;white-space:nowrap;">🔥 View Plain / Salted / Devilled →</a>
      </div>'''

c = c.replace(old2, new2, 1)

# Remove the old button div below price badge
import re
c = re.sub(r'\s*<div style="padding:0 1\.75rem 1\.75rem;">\s*<a href="roasted-cashews\.html"[^>]+>[^<]+</a>\s*</div>', '', c)

with open('cashew-guide.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("Done!")
