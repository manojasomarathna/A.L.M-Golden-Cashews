with open('cashew-guide.html', 'r', encoding='utf-8') as f:
    c = f.read()

fixes = [
    # Type 1 - Raw Cashew
    ('Shell úú, testa (poththa) úú,úú, cashew. Processing, roasting, export úú,ú,ú, ú,ú,ú,ú,ú, ú,ú,ú,ú,ú,. Farmers directly sell ú,ú,ú, grade.',
     'Shell සහ testa (poththa) සහිත cashew. Processing, roasting, export සඳහා භාවිතා කරනවා. Farmers directly sell කරන grade.'),

    # Type 2 - Kernel
    ('Shell ú,ú,ú,ú, ú,ú,ú,ú,ú,, skin remove ú,ú,ú,ú,ú, ready to eat / pack ú,ú,ú, cashew. Premium quality kernels.',
     'Shell ඉවත් කරලා, skin remove කරලා ready to eat / pack කරන cashew. Premium quality kernels.'),

    # Type 3 - Roasted
    ('Kernel roasting úú, flavoring ú,ú,ú,ú,ú, ready-to-eat cashews. Consumer market ú,ú,ú,ú,ú, most popular grade.',
     'Kernel roasting සහ flavoring කරලා ready-to-eat cashews. Consumer market සඳහා most popular grade.'),

    # Type 4 - Retail
    ('Small consumer packs ready for sale in shops and supermarkets. Hygienically sealed for freshness.',
     'Small consumer packs ready for sale in shops and supermarkets. Hygienically sealed for freshness.'),

    # Price notes
    ('Quality ú,ú,ú,ú, vary ú,ú,ú,ú,',
     'Quality අනුව vary වෙනවා'),
]

for old, new in fixes:
    if old in c:
        c = c.replace(old, new)
        print(f"Fixed: {old[:40]}...")

with open('cashew-guide.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("Done!")
