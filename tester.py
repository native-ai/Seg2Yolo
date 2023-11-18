import cv2
import os
import numpy as np
import json
from PIL import ImageColor


def hex_to_rgb(hex_code):
    rgb_tuple = ImageColor.getcolor(hex_code, "RGB")
    return rgb_tuple[::-1]


def create_image_mask_from_yolo(txt_path, img_shape, class_colors):
    mask = np.zeros(img_shape, dtype=np.uint8)

    with open(txt_path, 'r') as file:
        lines = file.readlines()

        for line in lines:
            data = line.strip().split()
            class_id = int(data[0])
            points = list(map(float, data[1:]))

            # Convert normalized coordinates back to pixel coordinates
            points = [(int(points[i] * img_shape[1]), int(points[i + 1] * img_shape[0])) for i in
                      range(0, len(points), 2)]
            a = list(class_colors)[class_id]

            # Get the color for the current class name
            color = hex_to_rgb(a)

            # Draw filled polygon with the class color
            cv2.fillPoly(mask, [np.array(points)], color=color)

    return mask


def process_images(directory_path, class_colors):
    for filename in os.listdir(directory_path):
        if filename.endswith('.txt'):
            # Read the corresponding image
            img_filename = os.path.splitext(filename)[0] + '.png'
            img_path = os.path.join(
                '/20181107_132300/label/cam_front_center',
                img_filename)
            image = cv2.imread(img_path)

            # Get image shape
            img_shape = image.shape

            # Create mask
            txt_path = os.path.join(directory_path, filename)
            mask = create_image_mask_from_yolo(txt_path, img_shape, class_colors)

            # Show the original image
            cv2.imshow('Original Image', image)

            # Show the mask
            cv2.imshow('Image Mask', mask)
            cv2.waitKey(0)


# Specify the directory containing your YOLO-style text files
directory_path = '/20181107_132300/txt_labels/'

# Read class colors from JSON file
with open('samples/hex_class.json', 'r') as json_file:
    class_colors = json.load(json_file)

# Process YOLO-style text files and display image masks
process_images(directory_path, class_colors)

# Close OpenCV windows
cv2.destroyAllWindows()
