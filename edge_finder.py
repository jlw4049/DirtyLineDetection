from os import PathLike
from pathlib import Path
from typing import Union

from PIL import Image, ImageFilter


class EdgeFinder:
    """
    Uses pillow to convert image to grayscale and use the FIND_EDGES filter.
    This easily allows the user to quickly save an image to see edges/dirty borders
    """

    def __init__(self):
        self.file_input = None
        self.file_output = None
        self.converted_image = None

    def find_edges(self, file_input: Union[str, PathLike]):
        """
        Take an image as input and convert it to grayscale and use the FIND_EDGES filter from pillow.

        :param file_input: String or Pathlike object to an image file in any format
        :return: None
        """

        # update variable
        self.file_input = file_input

        # convert image
        self.converted_image = (
            Image.open(Path(self.file_input))
            .convert("L")
            .filter(ImageFilter.FIND_EDGES)
        )

    def save_image(self, file_output: Union[str, PathLike] = None):
        """
        Save the converted image. You can optionally define a save path with the suffix of '.png' or leave this value
        blank as the program will automatically generate a save file name.

        :param file_output: This is an optional variable, if no path is supplied the program will save the file in the
            same directory as the input file. If a path is provided it must have the suffix '.png'
        :return: None
        """

        # check if file_output path was provided
        if file_output:
            self.file_output = file_output

        # use pillow.save() to save the file
        self.converted_image.save(self._save_location())

    def _save_location(self):
        """Used to generate a proper save file/path"""

        if self.file_output:
            if Path(self.file_output).suffix != ".png":
                raise ValueError("Output file path should should end with '.png'")
            else:
                return Path(self.file_output)

        elif not self.file_output:
            self.file_output = Path(
                Path(self.file_input).parent
                / Path(Path(self.file_input).name).with_suffix(".png")
            )
            if self.file_output.is_file():
                self.file_output = Path(
                    str(self.file_output.with_suffix("")) + "(1)"
                ).with_suffix(".png")
            return self.file_output


# Example
if __name__ == "__main__":
    convert_img = EdgeFinder()
    convert_img.find_edges(r"C:\Users\jlw_4\Desktop\test image.png")
    convert_img.save_image(r"C:\Users\jlw_4\Desktop\test image_NEW_hi.png")
