# -*- coding: utf-8 -*-
path = r'c:\Users\Admin\Desktop\A.L.M. Golden Cashews\alm_golden_cashews.html'

with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Replace lines 965-968 (index 964-967)
new_lines = [
    '      <h4>Call / WhatsApp</h4>\n',
    '      <div style="margin:0.75rem 0;">\n',
    '        <a href="tel:+94742770633" style="display:block;font-family:\'Playfair Display\',serif;font-size:1.8rem;font-weight:700;color:var(--gold);text-decoration:none;letter-spacing:1px;">0742770633</a>\n',
    '        <div style="font-size:0.78rem;color:var(--text-light);margin-top:0.2rem;">Tap to call directly</div>\n',
    '      </div>\n',
    '      <p style="margin-top:0.5rem;">\n',
    '        <a href="tel:+94742770633" style="display:inline-block;background:#1a73e8;color:white;padding:0.5rem 1.2rem;border-radius:6px;text-decoration:none;font-weight:600;font-size:0.9rem;margin-right:0.5rem;">\U0001f4de Call</a>\n',
    '        <a href="https://wa.me/94742770633" target="_blank" style="display:inline-block;background:#25D366;color:white;padding:0.5rem 1.2rem;border-radius:6px;text-decoration:none;font-weight:600;font-size:0.9rem;">\U0001f4ac WhatsApp</a>\n',
    '      </p>\n',
    '      <p style="margin-top:0.5rem;font-size:0.8rem;color:#aaa">Mon - Sat · 8am to 6pm</p>\n',
    '    </div>\n',
]

lines[964:968] = new_lines

with open(path, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Done!")
