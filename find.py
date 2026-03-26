# -*- coding: utf-8 -*-
path = r'c:\Users\Admin\Desktop\A.L.M. Golden Cashews\alm_golden_cashews.html'

with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find the products header section - look for "Our Cashew Range" line
for i, line in enumerate(lines):
    if 'Our Cashew Range' in line:
        print(f"Found at line {i+1}: {repr(line)}")
        # Insert a "View Prices" button after the section-sub line (2 lines after)
        for j in range(i, min(i+10, len(lines))):
            if 'Call for Price' in lines[j] and 'btn-primary' in lines[j]:
                print(f"Button line at {j+1}: {repr(lines[j])}")
                break
        break
