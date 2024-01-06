from PIL import Image
from rembg import remove

input_path = r"E:\Bgremoval-Python\1.jpg"
output_path = r"E:\Bgremoval-Python\img.png"

# Open the input image
img = Image.open(input_path)

# Use rembg to remove the background
result = remove(img)

# Save the result with a proper file extension (e.g., PNG)
result.save(output_path, format="PNG")
