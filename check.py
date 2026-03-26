# -*- coding: utf-8 -*-
path = r'c:\Users\Admin\Desktop\A.L.M. Golden Cashews\alm_golden_cashews.html'

with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Print lines 696-705 (0-indexed: 695-704)
for i in range(694, 706):
    print(f"{i+1}: {repr(lines[i])}")
