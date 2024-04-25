from PIL import Image

#opening 2 images
image1 = Image.open('scrambled1.png')
image2 = Image.open('scrambled2.png')

#loading pixels
pixels1 = image1.load()
pixels2 = image2.load()

size = image1.size

#making a new image
new_image = Image.new('RGB', size)
new_pixels = new_image.load()

for i in range(size[0]):
	for j in range(size[1]):
		new_pixels[i,j] = (
			(pixels1[i,j][0] + pixels2[i,j][0]) % 256, #Adding the values for red (if it passes 255, then do -256)
			(pixels1[i,j][1] + pixels2[i,j][1]) % 256, #Adding the values for green (if it passes 255, then do -256)
			(pixels1[i,j][2] + pixels2[i,j][2]) % 256, #Adding the values for blue (if it passes 255, then do -256)
		)

new_image.show()
new_image.save('merged_image.png', "PNG")
