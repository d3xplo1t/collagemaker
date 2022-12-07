# Import the Python Imaging Library
from PIL import Image

# Load the image
image = Image.open("strawberry.png")

# Resize the image to a specific width and height
image = image.resize((400, 400))

# Create a new image that is the size of an A4 sheet
a4_sheet = Image.new('RGBA', (2480, 3508), color=(0, 0, 0, 0))

# Set the number of rows and columns on the A4 sheet
rows = 8
cols = 5

# Calculate the width and height of each image
image_width = a4_sheet.width // cols
image_height = a4_sheet.height // rows

# Iterate over the rows and columns
for i in range(rows):
    for j in range(cols):
        # Calculate the coordinates for the current image
        x = j * image_width
        y = i * image_height

        # Paste the image at the current position
        a4_sheet.paste(image, (x, y))

# Save the resulting image to a file
a4_sheet.save("a4_sheet.png")
