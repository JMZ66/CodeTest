from PIL import Image, ImageDraw

# 创建一个空白的图片
img = Image.new('RGB', (500, 500), color = 'white')

# 创建一个画笔对象
draw = ImageDraw.Draw(img)

# 绘制哈士奇的轮廓
draw.ellipse((100, 100, 400, 400), fill='lightgray', outline='black')
draw.ellipse((150, 150, 350, 350), fill='white', outline='black')
draw.ellipse((200, 200, 300, 300), fill='gray', outline='black')
draw.ellipse((225, 250, 275, 300), fill='black')

# 绘制哈士奇的眼睛和嘴巴
draw.ellipse((220, 180, 240, 200), fill='black')
draw.ellipse((260, 180, 280, 200), fill='black')
draw.line((240, 250, 260, 250), fill='black', width=5)

# 显示图片
img.show()

# 保存图片
img.save('husky.png')

