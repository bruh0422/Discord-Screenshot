import requests, io

import PIL.ImageFile
import PIL.Image
from PIL import Image, ImageDraw, ImageFont

avatar_size = 40
font_size = 16
timestamp_font_size = 12

margin = 16

def crop_to_circle(image: PIL.ImageFile):
    image = image.resize((avatar_size, avatar_size))

    mask = Image.new('L', image.size, 0)
    draw = ImageDraw.Draw(mask)

    width, height = image.size
    draw.ellipse((0, 0, width, height), fill=255)

    image = image.convert('RGBA')
    result = Image.new('RGBA', image.size)
    result.paste(image, (0, 0), mask=mask)

    return result, mask

image = Image.new('RGBA', (500, margin*2+avatar_size), (49, 51, 56, 255))

avatar, mask = crop_to_circle(Image.open(io.BytesIO(requests.get('https://cdn.discordapp.com/avatars/518750068455768065/11eb73db9340a139ec567d10be3adc34.png?size=4096').content)))
image.paste(avatar, (margin, margin), mask=mask)

draw = ImageDraw.Draw(image)
font = ImageFont.truetype('fonts/gg-sans.ttf', font_size)
timestamp_font = ImageFont.truetype('fonts/gg-sans.ttf', timestamp_font_size)

author = 'BigApple'
timestamp = 'Today at 8:49 PM'
content = 'test'

draw.text((margin*2+avatar_size, margin-3), author, font=font, fill=(255, 255, 255, 255))

text1_bbox = draw.textbbox((0, 0), author, font=font)
text1_width = text1_bbox[2] - text1_bbox[0]
draw.text((margin*2+avatar_size + text1_width+8, margin-3 + (font_size-timestamp_font_size)), timestamp, font=timestamp_font, fill=(148, 155, 164, 255))

draw.text((margin*2+avatar_size, margin*2+3), content, font=font, fill=(255, 255, 255, 255))

image.save('test.png')