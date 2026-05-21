from PIL import Image, ImageDraw

# Triangle image
img1 = Image.new('RGB', (400, 400), 'white')
draw1 = ImageDraw.Draw(img1)
draw1.line((200,50,50,350), fill='black', width=4)
draw1.line((50,350,350,350), fill='black', width=4)
draw1.line((350,350,200,50), fill='black', width=4)
draw1.text((150,360), "H1 = 1", fill='black')
img1.save("triangle.png")

# Line image
img2 = Image.new('RGB', (400, 200), 'white')
draw2 = ImageDraw.Draw(img2)
draw2.line((50,100,350,100), fill='black', width=5)
draw2.text((150,120), "H1 = 0", fill='black')
img2.save("line.png")

# Mapping image
img3 = Image.new('RGB', (500, 300), 'white')
draw3 = ImageDraw.Draw(img3)
draw3.polygon([(100,50),(50,200),(150,200)], outline='black')
draw3.line((200,150,300,150), fill='black', width=4)
draw3.line((350,100,450,100), fill='black', width=5)
draw3.text((200,170), "mapping", fill='black')
img3.save("mapping.png")

# Flowchart image
img4 = Image.new('RGB', (400, 600), 'white')
draw4 = ImageDraw.Draw(img4)

steps = ["Start","Generate Maps","Check Simplicial","Compute Homology","Compare","End"]
y = 50

for s in steps:
    draw4.rectangle((100,y,300,y+40), outline='black')
    draw4.text((110,y+10), s, fill='black')
    if s != steps[-1]:
        draw4.line((200,y+40,200,y+70), fill='black', width=2)
    y += 80

img4.save("flowchart.png")

print("✅ Images generated successfully!")