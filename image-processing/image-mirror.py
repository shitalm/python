from PIL import Image
img=Image.open("bird-with-bg.jpg")
Mirror_Image=img.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
Mirror_Image.save("bird-mirror.jpg")

