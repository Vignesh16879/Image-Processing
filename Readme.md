# Image Processing Pipeline

This project provides a Python-based image processing pipeline capable of handling a large dataset of images. The pipeline supports basic image operations such as resizing, filtering, and color transformations. It processes images from a specified input directory and saves the results in an output directory.

## Features

- Load images from a directory.
- Apply various image processing techniques.
- Save processed images to an output directory.

## Requirements

- Python 3.x
- The following Python libraries:
  - `numpy`
  - `pillow`
  - `opencv-python`
  - `scikit-image`
  - `matplotlib`

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-folder>
    ```

2. Install the required Python libraries:
    ```bash
    pip install numpy pillow opencv-python scikit-image matplotlib
    ```

## Usage
1. Prepare your images:
    - Place the images you want to process in the input_images folder.

2. Configure the processing script:
    - Update file.py if necessary to adjust processing parameters.

3. Run the processing pipeline:
    - Execute the script using Python: 
    ```bash 
    chmod u+x run.sh
    ./run.sh
    ```

## How It Works

### Setup Environment:

- **Dependencies Installation:** The `run.sh` script installs the necessary Python libraries (`numpy`, `pillow`, `opencv-python`, `scikit-image`, `matplotlib`) using `pip`.
- **Execution:** After installing the dependencies, it runs the `file.py` script.

### Image Preparation:

- **Input Folder:** Place your images in the `input_images` directory. This is the directory where the script will read images from.

### Processing Script (`file.py`):

- **Loading Images:** The script reads images from the `input_images` directory using OpenCV.
- **Processing:** It applies specified image processing techniques to each image. In the provided example, the image is converted to grayscale and then blurred using a Gaussian filter.
- **Saving Results:** The processed images are saved in the `processed_images` directory. The filenames remain the same, but the images have undergone the specified processing steps.

### Results:

- **Output Folder:** After processing, you can find the results in the `processed_images` folder. This will contain the images as per the processing steps defined in `file.py`.