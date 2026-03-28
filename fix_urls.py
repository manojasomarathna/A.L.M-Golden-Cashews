import os
import glob

old_urls = [
    'https://alm-golden-cashews.netlify.app',
    'https://almgoldencashews.netlify.app'
]
new_url = 'https://almgoldencashews.netlify.app'

files = glob.glob('*.html')
for fname in files:
    with open(fname, 'r', encoding='utf-8') as f:
        c = f.read()
    original = c
    for old in old_urls:
        c = c.replace(old, new_url)
    if c != original:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Updated: {fname}")
    else:
        print(f"No change: {fname}")

print("Done!")
