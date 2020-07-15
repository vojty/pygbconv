"""
Taken from here https://stackoverflow.com/a/237747
I'm not a python guy... :)
"""
import sys

from PIL import Image


def main():
    argsCount = len(sys.argv) - 1
    if argsCount < 1:
        print("Usage: python reducer_colors.py input.png output.png")
        return 0

    # fmt: off
    PALETTE = [
        0,   0,   0,  # black,  00
        0,   255, 0,  # green,  01
        255, 0,   0,  # red,    10
        255, 255, 0,  # yellow, 11
    ] + [0, ] * 252 * 3
    # fmt: on

    # a palette image to use for quant
    pimage = Image.new("P", (1, 1), 0)
    pimage.putpalette(PALETTE)

    # open the source image
    image = Image.open(sys.argv[1])
    image = image.convert("RGB")

    # quantize it using our palette image
    imagep = image.quantize(palette=pimage)

    # save
    if argsCount == 2:
        outputFile = sys.argv[2]
    else:
        outputFile = "output.png"
    imagep.save(outputFile)


if __name__ == "__main__":
    sys.exit(main())
