import cv2
import os
import numpy as np
from utils import hex_to_rgb,get_colors
import argparse

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


def process_images(original_labels,converted_labels, class_colors):
    for filename in os.listdir(original_labels):
        if filename.endswith('.txt'):
            # Read the corresponding image
            img_filename = os.path.splitext(filename)[0] + '.png'
            img_path = os.path.join(
                converted_labels,
                img_filename)
            image = cv2.imread(img_path)

            # Get image shape
            img_shape = image.shape

            # Create mask
            txt_path = os.path.join(original_labels, filename)
            mask = create_image_mask_from_yolo(txt_path, img_shape, class_colors)

            # Show the original image
            cv2.imshow('Original Image', image)

            # Show the mask
            cv2.imshow('Image Mask', mask)
            cv2.waitKey(0)


def parser():
    # Define the command line arguments
    parser = argparse.ArgumentParser(
        description='Process images with specified directory, target labels, and class colors.')
    parser.add_argument('-O', '--original_labels', type=str, help='Path to the directory containing images')
    parser.add_argument('-L', '--converted_labels', type=str, help='Target labels directory')
    parser.add_argument('-C', '--color_list', type=str, help='Color list.(hex_class.json)')

    # Parse the command line arguments
    args = parser.parse_args()

    return args

def main():
    args=parser()
    # Read class colors from JSON file
    class_list=get_colors(args.color_list)
    # Process YOLO-style text files and display image masks
    process_images(args.original_labels, args.converted_labels, class_list)
    # Close OpenCV windows
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
