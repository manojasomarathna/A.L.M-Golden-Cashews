from PIL import Image

img = Image.open('logo.png').convert('RGBA')
w, h = img.size
print(f"Size: {w}x{h}")
print(f"Top-left: {img.getpixel((0,0))}")
print(f"Top-right: {img.getpixel((w-1,0))}")
print(f"Bottom-left: {img.getpixel((0,h-1))}")
print(f"Bottom-right: {img.getpixel((w-1,h-1))}")
print(f"Center: {img.getpixel((w//2,h//2))}")
