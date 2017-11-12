from PIL import Image, ImageDraw, ImageFont

img = Image.open('processed_sample1.jpg')
draw = ImageDraw.Draw(img)

# 폰트 종류와 크기를 지정
font = ImageFont.truetype('~/Library/Fonts/Anonymice Powerline Bold Italic.ttf', 22)

# 텍스트 넣기
draw.text((63, 7), 'Python!', font=font, fill='#000')

img.save('drew_text.png', format='PNG')
