from PIL import Image

img = Image.open('logo.png').convert('RGBA')
pixels = img.load()

for y in range(img.height):
    for x in range(img.width):
        r, g, b, a = pixels[x, y]
        if r < 30 and g < 30 and b < 30:
            pixels[x, y] = (26, 18, 8, 255)

img.save('logo.png')
print('Done')
