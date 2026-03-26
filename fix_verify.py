# -*- coding: utf-8 -*-
path = r'c:\Users\Admin\Desktop\A.L.M. Golden Cashews\alm_golden_cashews.html'

with open(path, 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('<meta charset="UTF-8">', '<meta charset="UTF-8">\n<meta name="google-site-verification" content="FLyYONPGn2vMKY8I9LclvuArTnlZ2xybm4CHjVijPAU" />')

with open(path, 'w', encoding='utf-8') as f:
    f.write(c)

print("Done!")
