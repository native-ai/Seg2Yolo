import numpy as np
import json

def extract_mask(image, target_color):
    mask = np.zeros_like(image, dtype=int)
    mask[np.all(image == target_color[::-1], axis=-1)] = 1
    return mask.astype(np.uint8)*255

def get_colors(path):
    # Read class colors from JSON file
    with open(path, 'r') as json_file:
        class_colors = json.load(json_file)
    return  class_colors