# Dirty Line Detection

A toolset that is designed to be used to detect dirty borders in videos/images 

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