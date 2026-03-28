import glob
import re

files = glob.glob('*.html')
for fname in files:
    with open(fname, 'r', encoding='utf-8') as f:
        c = f.read()
    original = c
    # Add loading="lazy" to img tags that don't already have it
    c = re.sub(r'(<img)(?![^>]*loading=)', r'\1 loading="lazy"', c)
    if c != original:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Updated: {fname}")
    else:
        print(f"No change: {fname}")
print("Done!")
