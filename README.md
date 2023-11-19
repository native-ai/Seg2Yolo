# Seg2Yolo

## Overview

This tool is designed to streamline the process of converting segmented label data to the YOLO (You Only Look Once) segmentation format. The YOLO segmentation format is widely used in computer vision tasks, especially for object detection. This converter simplifies the transition from segmented label data to the format required by YOLO, making it easier for researchers and developers to integrate their segmentation datasets into YOLO-based models.

## Features

- **Efficient Conversion:** The converter efficiently transforms segmented label data into the YOLO segmentation format, ensuring a smooth transition between different annotation formats.

- **Batch Processing:** Support for batch processing enables users to convert multiple segmented label files simultaneously, saving time and effort.

- **Configurability:** The tool is designed to be configurable, allowing users to customize certain parameters to suit their specific dataset requirements.

## Getting Started

### Installation

To get started, follow these simple steps:

1. Clone this repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Run the converter script with the appropriate command-line arguments.

### Usage

1. **Input:** Provide the path to the directory containing segmented label files.
2. **Output:** Specify the directory where the converted YOLO segmentation files will be saved.
3. **color_list:** Helps create a mask that into image.

Example command:

```bash
python Seg2Yolo.py --input_path /path/to/segmented_labels --output_path /path/to/yolo_segmentation --color_list rgb_class.json
```

### Contribution

Contributions and feedback are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

