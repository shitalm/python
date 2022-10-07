from rembg import remove
from PIL import Image
input_path = "bird-with-bg.jpg"
output_path = "bird-without-bg.png"
input = Image.open(input_path)
output = remove(input)
output.save(output_path)
