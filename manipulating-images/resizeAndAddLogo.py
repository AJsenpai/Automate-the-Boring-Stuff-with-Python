# resizeAndAddLogo.py - Resizes all images in current working directory to fit
# in a 300x300 square, and adds catlogo.png to the lower-right corner.
import os
from PIL import Image

os.chdir(r"C:\Users\Jai\Desktop\Docs\Zimages")

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = "catlogo.png"

with Image.open(LOGO_FILENAME) as logoIm:
    logoWidth, logoHeight = logoIm.size
    os.makedirs("withLogo", exist_ok=True)
    # loop over all the files in working directory
    for filename in os.listdir("."):
        if (
            not (filename.endswith("png") or filename.endswith("jpg"))
            or filename == LOGO_FILENAME
        ):
            continue  # skip non-images files and the logo file itself

        with Image.open(filename) as im:
            width, height = im.size

            # check if image needs to be resized
            if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
                # calculate the new width and height to resize to
                if width > height:
                    height = int((SQUARE_FIT_SIZE / width) * height)
                    width = SQUARE_FIT_SIZE
                else:
                    width = int((SQUARE_FIT_SIZE / height) * width)
                    height = SQUARE_FIT_SIZE

                # resize the image
                print(f"Resizing image {filename}...")
                im = im.resize((width, height))

            # add the logo
            print(f"Adding the logo to {filename}")
            im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)
            # save changes
            im.save(os.path.join("withLogo", filename))
