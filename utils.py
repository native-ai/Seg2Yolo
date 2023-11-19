import numpy as np
import json
from PIL import ImageColor

def extract_mask(image, target_color):
    mask = np.zeros_like(image, dtype=int)
    mask[np.all(image == target_color[::-1], axis=-1)] = 1
    return mask.astype(np.uint8)*255

def get_colors(path):
    # Read class colors from JSON file
    with open(path, 'r') as json_file:
        class_colors = json.load(json_file)
    return  class_colors

def hex_to_rgb(hex_code):
    rgb_tuple = ImageColor.getcolor(hex_code, "RGB")
    return rgb_tuple[::-1]