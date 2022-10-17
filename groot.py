# !python3

import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'something.png'

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

# Loop over files in working directory

for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')) \
        or filename == LOGO_FILENAME:
            continue    # skip non-image filesand the logo file itself

        im = Image.open(filename)
        width, height = im.size

# Check if image needs to be resized 
  
if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
    # calculate to adjust
    if width > height:
        height = int((SQUARE_FIT_SIZE / width) * height)
        width = SQUARE_FIT_SIZE
    else:
        width = int((SQUARE_FIT_SIZE / height) * width)
        height = SQUARE_FIT_SIZE

        # Resize image
        print('Resizing %s...' % (filename))
        im = im.resize((width, height))

# Add the logo
print('Adding logo to %s...' % (filename))
im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)

# Save changes
im.save(os.path.join('withLogo', filename))
