# pygbconv

Python ROM patcher to display custom graphics on a Gameboy.
Forked from https://github.com/cmar0ck/pygbconv

What I have changed:

- converted to Python 3
- added Pipfile (check for dependencies)
- added [black](https://github.com/psf/black) formatter
- added `reducer_colors.py` script for reducing image colors (to only 4 - requirement for original script)

## Usage

1.  Resize your image to 160 x 144px
2.  Reduce colors - `python reducer_color.py your_image.png`
3.  Generate ROM - `python pygbconv.py output.gb image0.png image1.png ...`
4.  Profit

## Notes

- The output ROM's type is **MBC5**
- Only checked with DMG GB, not sure about the other GB versions

Original script by [nitro2k01](http://blog.gg8.se), 2013
