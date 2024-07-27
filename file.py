import os
import cv2
import numpy as np
from PIL import Image
from skimage import filters
import matplotlib.pyplot as plt

def load_images(image_folder):
    images = []
    for filename in os.listdir(image_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(image_folder, filename)
            img = cv2.imread(img_path)
            if img is not None:
                images.append((filename, img))
    return images

def process_image(img):
    # Example processing: Convert to grayscale and apply Gaussian blur
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred_img = cv2.GaussianBlur(gray_img, (5, 5), 0)
    return blurred_img

def save_image(filename, img, output_folder):
    output_path = os.path.join(output_folder, filename)
    cv2.imwrite(output_path, img)

def main():
    input_folder = 'images'
    output_folder = 'processed_images'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    images = load_images(input_folder)
    
    for filename, img in images:
        processed_img = process_image(img)
        save_image(filename, processed_img, output_folder)
    
    print("Processing completed. Processed images saved in", output_folder)

if __name__ == "__main__":
    main()
