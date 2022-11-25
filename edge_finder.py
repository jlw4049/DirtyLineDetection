from PIL import Image, ImageFilter
from pathlib import Path
from os import PathLike
from typing import Union

# from tkinter import Tk, Label
#
# root = Tk()
#
# # Opening the image (R prefixed to string
# # in order to deal with '\' in paths)
# image = Image.open(r"C:\Users\jlw_4\Desktop\test image.png")
#
# # Converting the image to grayscale, as edge detection
# # requires input image to be of mode = Grayscale (L)
# image = image.convert("L")
#
# # Detecting Edges on the Image using the argument ImageFilter.FIND_EDGES
# image = image.filter(ImageFilter.FIND_EDGES)
# # image = Image.Image()
# new_img = ImageTk.PhotoImage(image)
#
# # Saving the Image Under the name Edge_Sample.png
# # image.save(r"C:\Users\jlw_4\Desktop\test image_NEW.png")
# # print(image.getbbox())
# # root = Tk()
# l = Label(root, image=new_img)
# l.image = new_img
# l.pack()
# # l
# root.mainloop()

class EdgeFinder:

    def __init__(self):

        self.file_input = None
        self.file_output = None
        self.converted_image = None

    def find_edges(self, file_input: Union[str, PathLike]):
        self.file_input = file_input
        # Converting the image to grayscale, as edge detection
        # requires input image to be of mode = Grayscale (L)
        # Detecting Edges on the Image using the argument ImageFilter.FIND_EDGES
        self.converted_image = Image.open(Path(self.file_input)).convert("L").filter(ImageFilter.FIND_EDGES)

        # image.save(self._save_location())

    def save_image(self, file_output: Union[str, PathLike] = None):
        if file_output:
            self.file_output = file_output
        self.converted_image.save(self._save_location())

    def _save_location(self):
        if self.file_output:
            if Path(self.file_output).suffix != ".png":
                raise ValueError("Output file path should should end with '.png'")
            else:
                return Path(self.file_output)

        elif not self.file_output:
            self.file_output = Path(Path(self.file_input).parent / Path(Path(self.file_input).name).with_suffix(".png"))
            if self.file_output.is_file():
                self.file_output = Path(str(self.file_output.with_suffix("")) + "(1)").with_suffix(".png")
            return self.file_output

# def get_edges(file,
#               output):
#     # in order to deal with '\' in paths)
#     image = Image.open(Path(file))
#
#     # Converting the image to grayscale, as edge detection
#     # requires input image to be of mode = Grayscale (L)
#     image = image.convert("L")
#
#     # Detecting Edges on the Image using the argument ImageFilter.FIND_EDGES
#     image = image.filter(ImageFilter.FIND_EDGES)
#
#     # Saving the Image Under the name Edge_Sample.png
#     # image.save(r"C:\Users\jlw_4\Desktop\test image_NEW.png")

if __name__ == '__main__':
    convert_img = EdgeFinder()
    convert_img.find_edges(r"C:\Users\jlw_4\Desktop\test image.png")
    convert_img.save_image(r"C:\Users\jlw_4\Desktop\test image_NEW_hi.png")

