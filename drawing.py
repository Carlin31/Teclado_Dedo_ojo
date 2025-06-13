import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

FONT_PATH = "DejaVuSans.ttf"  # Ruta a la fuente .ttf con soporte UTF-8

def draw_keyboard(img, keys, selected_key=None):
    start_x, start_y = 100, 100
    key_size = 60
    spacing = 10

    # Dibujar los cuadros del teclado con OpenCV
    for i, row in enumerate(keys):
        for j, key in enumerate(row):
            x = start_x + j * (key_size + spacing)
            y = start_y + i * (key_size + spacing)
            color = (255, 0, 255) if (i, j) == selected_key else (200, 200, 200)
            border = (0, 0, 0)

            # Dibujar tecla
            cv2.rectangle(img, (x, y), (x + key_size, y + key_size), color, -1)
            cv2.rectangle(img, (x, y), (x + key_size, y + key_size), border, 2)

    # Convertir imagen a PIL para dibujar texto UTF-8
    pil_img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(pil_img)
    font = ImageFont.truetype(FONT_PATH, 26)

    # Dibujar texto centrado en cada tecla
    for i, row in enumerate(keys):
        for j, key in enumerate(row):
            x = start_x + j * (key_size + spacing)
            y = start_y + i * (key_size + spacing)
            bbox = draw.textbbox((0, 0), key, font=font)
            text_w = bbox[2] - bbox[0]
            text_h = bbox[3] - bbox[1]
            text_x = x + (key_size - text_w) // 2
            text_y = y + (key_size - text_h) // 2
            draw.text((text_x, text_y), key, font=font, fill=(0, 0, 0))

    # Volver a OpenCV
    return cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
