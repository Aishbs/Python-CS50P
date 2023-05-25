import sys
import os
from PIL import Image, ImageOps

def main():
    name1, ext1 = os.path.splitext(sys.argv[1])

    #Checks if input is image
    if ext1 != '.jpg' and ext1 != '.jpeg' and ext1 != '.png':
        sys.exit("Invalid Input")

    #Checks minimum commandline arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    #Checks maximum commandline arguments
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    #Checks if the input path exists
    elif not os.path.exists(sys.argv[1]):
        sys.exit("Input does not exist")

    #Checks for input and output extension match
    elif len(sys.argv) == 3:
        name2, ext2 = os.path.splitext(sys.argv[2])
        #Checks if input is image
        if ext2 != '.jpg' and ext1 != '.jpeg' and ext2 != '.png':
            sys.exit("Invalid Output")

        if ext1 != ext2:
            sys.exit("Input and output have different extensions")
        else:
            design_shirt(sys.argv[1], sys.argv[2])

def design_shirt(input, output):

        shirt = Image.open("shirt.png")
        img = Image.open(input)
        #Resizing
        cropImg = ImageOps.fit(img, shirt.size, Image.Resampling.BICUBIC, bleed=0.0, centering=(0.5, 0.5))
        #Paste
        cropImg.paste(shirt, box=None, mask=shirt)
        #save the changes as 2nd cmdline argument
        cropImg.save(output)

if __name__ == "__main__":
    main()