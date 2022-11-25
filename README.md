# Dirty Line Detection

A toolset that is designed to be used to detect dirty borders in videos/images 

This is early development, currently it's only function is to find the edges of an image, and save the converted image.

Developed by Jessie Wilson (2022)

## Install

`pip install PyDirtyLineDetection`

## Uninstall

`pip uninstall PyDirtyLineDetection`

## Examples of How To Use

```python
from edge_converter import EdgeFinder

convert_image = EdgeFinder()
convert_image.find_edges(file_input="example.png")

# File output is optional
# e.g. convert_image.save_image()
convert_image.save_image(file_output="example(1).png")


```