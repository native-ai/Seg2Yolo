import cv2
import numpy as np
import os
import json
from tqdm import tqdm

def extract_mask(image, target_color):
    mask = np.zeros_like(image, dtype=int)
    mask[np.all(image == target_color[::-1], axis=-1)] = 1
    return mask.astype(np.uint8)*255