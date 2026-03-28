# -*- coding: utf-8 -*-
path = r'c:\Users\Admin\Desktop\A.L.M. Golden Cashews\alm_golden_cashews.html'

with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'Call / WhatsApp' in line:
        print(f"Found at line {i+1}: {repr(line)}")
        for j in range(i, min(i+15, len(lines))):
            print(f"{j+1}: {repr(lines[j])}")
        break
