import os
import json
import cv2
from utils import extract_mask


def process_images(directory_path, target_labels, class_colors):
    # Iterate through each image in the specified directory
    for filename in os.listdir(directory_path):
        if filename.endswith(('.jpg', '.jpeg', '.png')):  # Adjust file extensions as needed
            # Read the image using OpenCV
            image_path = os.path.join(directory_path, filename)
            image = cv2.imread(image_path)
            width, height, _ = image.shape

            # List to store contour points for each class
            contours_data = []

            # Iterate through each class and create a mask
            for idx, (class_name,color_code) in enumerate(class_colors.items()):
                class_mask = extract_mask(image, color_code)

                gray_mask = cv2.cvtColor(class_mask, cv2.COLOR_BGR2GRAY)

                # Find contours in the binary mask
                contours, _ = cv2.findContours(gray_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                # Iterate through contours and append contour points to the list
                for contour in contours:
                    contour_data = [idx]
                    for point in contour:
                        x, y = point[0]
                        contour_data.extend([x / height, y / width])
                    contours_data.append(contour_data)

            # Create a text file with YOLO format
            txt_file_path = os.path.join(target_labels, f"{os.path.splitext(filename)[0]}.txt")
            with open(txt_file_path, 'w') as txt_file:
                for contour_data in contours_data:
                    txt_file.write(" ".join(map(str, contour_data)) + "\n")



# Specify the directory containing your images
directory_path = ''
target_labels = ''

# Read class colors from JSON file
with open('audi_sample/rgb_class.json', 'r') as json_file:
    class_colors = json.load(json_file)

# Process images in the specified directory with the read class colors
process_images(directory_path, target_labels, class_colors)
