with open('cashew-guide.html', 'r', encoding='utf-8') as f:
    c = f.read()

old = '<div class="type-num">3</div>\n      </div>'
new = '<div class="type-num">3</div>\n        <a href="roasted-cashews.html" style="position:absolute;bottom:12px;left:50%;transform:translateX(-50%);background:rgba(200,146,42,0.95);color:#1A1208;padding:0.45rem 1.1rem;border-radius:20px;font-size:0.78rem;font-weight:700;text-decoration:none;white-space:nowrap;">\U0001f525 View Plain / Salted / Devilled \u2192</a>\n      </div>'

c = c.replace(old, new, 1)

with open('cashew-guide.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("Done!")
