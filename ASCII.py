from PIL import Image
im = Image.open("/home/adam/Pictures/ascii-pineapple.jpg")

basewidth = 300
wpercent = (basewidth/float(im.size[0]))
hsize = int((float(im.size[1])*float(wpercent)))
im = im.resize((basewidth,hsize), Image.Resampling.LANCZOS)
im.save('somepic.jpg')

w, h = im.size
pixels = list(im.getdata())
pixel_matrix = [pixels[i:i+w] for i in range(0, len(pixels), w)]

brightness_matrix = [[sum(pixel)//3 for pixel in row] for row in pixel_matrix]
lightness_matrix = [[(max(pixel) - min(pixel))//2 for pixel in row] for row in pixel_matrix]
luminosity_matrix = [[round((0.21*pixel[0]) + (0.72*pixel[1]) + (0.07*pixel[2])) for pixel in row] for row in pixel_matrix]

ascii = """"`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"""

def unit_to_ascii(unit):
    return ascii[int(unit/255*len(ascii))] 
    
num = input("Shall we break this image down by 1: brightness, 2: lightness, or 3: luminosity? ")

if num == "1":
    chosen_matrix = brightness_matrix
elif num == "2":
    chosen_matrix = lightness_matrix
elif num == "3":
    chosen_matrix = luminosity_matrix

ascii_matrix = [[unit_to_ascii(unit) for unit in row] for row in chosen_matrix]

def stretch(row):
    return [pixel*3 for pixel in row]

ascii_matrix = [stretch(row) for row in ascii_matrix]

def invert(matrix):
    return [[255-int(pixel) for pixel in row] for row in matrix]

ascii_image = "\n".join(["".join(row) for row in ascii_matrix])
print(ascii_image)


choice = input("Invert image? (y/n) ")
if choice == "y":
    chosen_matrix = invert(chosen_matrix)
    ascii_matrix = [[unit_to_ascii(unit) for unit in row] for row in chosen_matrix]
    ascii_matrix = [stretch(row) for row in ascii_matrix]
    ascii_image = "\n".join(["".join(row) for row in ascii_matrix])
    print(ascii_image)
else:
    pass
