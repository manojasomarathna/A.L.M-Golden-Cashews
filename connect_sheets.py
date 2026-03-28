# -*- coding: utf-8 -*-

SCRIPT_URL = "https://script.google.com/macros/s/AKfycbyE19D6DyU4zvITfYx-1Fsl9V0J6tXcI_VuHzMDLjQ7sxfmDsWnmStwyVzJiH1BYBbfOg/exec"

NEW_JS = """
<script>
  function submitOrder() {
    const name = document.getElementById('fname').value.trim();
    const phone = document.getElementById('fphone').value.trim();
    const product = document.getElementById('fproduct').value;
    const qty = document.getElementById('fqty').value.trim();
    const area = document.getElementById('farea').value.trim();
    const notes = document.getElementById('fnotes').value.trim();

    if (!name || !phone || !product || !qty) {
      alert('Please fill in Name, Phone, Product, and Quantity!');
      return;
    }

    // Save to Google Sheets
    fetch('""" + SCRIPT_URL + """', {
      method: 'POST',
      body: JSON.stringify({
        name: name,
        phone: phone,
        product: product,
        quantity: qty,
        area: area || 'Not specified',
        notes: notes || ''
      })
    }).catch(() => {});

    // Send WhatsApp message
    const msg = `Hello A.L.M. Golden Cashews! 🥜\\n\\n*New Order Request*\\n--------------------\\n*Name:* ${name}\\n*Phone:* ${phone}\\n*Product:* ${product}\\n*Quantity:* ${qty}\\n*Delivery Area:* ${area || 'To be confirmed'}\\n${notes ? `*Notes:* ${notes}` : ''}\\n\\nPlease confirm availability and pricing. Thank you!`;

    window.open(`https://wa.me/94742770633?text=${encodeURIComponent(msg)}`, '_blank');

    const toast = document.getElementById('toast');
    toast.classList.add('show');
    setTimeout(() => toast.classList.remove('show'), 4000);
  }
</script>
"""

# Update main site
path = r'c:\Users\Admin\Desktop\A.L.M. Golden Cashews\alm_golden_cashews.html'
with open(path, 'r', encoding='utf-8') as f:
    c = f.read()

# Replace old script
import re
c = re.sub(r'<script>\s*function submitOrder\(\).*?</script>', NEW_JS.strip(), c, flags=re.DOTALL)

with open(path, 'w', encoding='utf-8') as f:
    f.write(c)
print("Main site updated!")

# Update retail page
path2 = r'c:\Users\Admin\Desktop\A.L.M. Golden Cashews\retail-packed-cashews.html'
with open(path2, 'r', encoding='utf-8') as f:
    c2 = f.read()

NEW_JS2 = NEW_JS.replace("document.getElementById('fproduct')", "document.getElementById('fpack')")

c2 = re.sub(r'<script>\s*function submitOrder\(\).*?</script>', NEW_JS2.strip(), c2, flags=re.DOTALL)

with open(path2, 'w', encoding='utf-8') as f:
    f.write(c2)
print("Retail page updated!")

print("All done!")
