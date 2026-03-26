# -*- coding: utf-8 -*-
path = r'c:\Users\Admin\Desktop\A.L.M. Golden Cashews\retail-packed-cashews.html'

with open(path, 'r', encoding='utf-8') as f:
    c = f.read()

old = '''"offers": {
    "@type": "AggregateOffer",
    "priceCurrency": "LKR",
    "availability": "https://schema.org/InStock",
    "seller": {"@type": "Organization", "name": "A.L.M. Golden Cashews", "telephone": "+94742770633"}
  }'''

new = '''"offers": {
    "@type": "AggregateOffer",
    "priceCurrency": "LKR",
    "lowPrice": "0",
    "highPrice": "9999",
    "offerCount": "4",
    "availability": "https://schema.org/InStock",
    "seller": {"@type": "Organization", "name": "A.L.M. Golden Cashews", "telephone": "+94742770633"}
  }'''

if old in c:
    c = c.replace(old, new)
    print("Fixed!")
else:
    print("Pattern not found")

with open(path, 'w', encoding='utf-8') as f:
    f.write(c)
