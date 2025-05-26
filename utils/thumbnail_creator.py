from PIL import Image, ImageDraw, ImageFont
import os
from config import THUMBNAIL_TEMPLATE_PATH, OUTPUT_THUMBNAIL_PATH

def create_thumbnail(text):
    base = Image.open(THUMBNAIL_TEMPLATE_PATH).convert('RGBA')
    draw = ImageDraw.Draw(base)
    font = ImageFont.truetype("arial.ttf", 40)
    draw.text((50, 50), text, font=font, fill='white')
    output_path = os.path.join(OUTPUT_THUMBNAIL_PATH, 'thumbnail.png')
    base.save(output_path)
    return output_path
