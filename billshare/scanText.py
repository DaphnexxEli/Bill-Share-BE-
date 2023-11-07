import pytesseract
from PIL import Image

image_path = "menu_image.jpg"
menu_image = Image.open(image_path)

menu_text = pytesseract.image_to_string(menu_image)


menu_items = menu_text.split("\n")  # Splitting by lines assuming each menu item is on a new line

# Jame will add something here

for item in menu_items:
    print(item)
