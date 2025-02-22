#!/usr/bin/env python3

import os
import argparse
import logging
import sys

# Attempt to import Pillow. If it's not installed, display an error message and exit.
try:
    from PIL import Image
except ImportError:
    print("Error: The required Pillow library is not installed. Please ensure you have a segmented python virtual environment with the required Pillow library installed.")
    sys.exit(1)

# Set up logging for production debugging and monitoring.
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Define the directories to sort images into.
horizontal_dir = 'horizontal'
vertical_dir = 'vertical'
square_dir = 'square'

# Create the directories if they don't exist.
for directory in [horizontal_dir, vertical_dir, square_dir]:
    try:
        os.makedirs(directory, exist_ok=True)
        logging.info("Ensured directory exists: %s", directory)
    except Exception as e:
        logging.error("Error creating directory '%s': %s", directory, e)

def is_close_to_square(width, height, tolerance=0.1):
    """Determine if an image's dimensions are roughly square."""
    return abs(width - height) / max(width, height) <= tolerance

def sort_images(directory):
    """Scan the specified directory for images and move them based on dimensions."""
    try:
        files = os.listdir(directory)
    except Exception as e:
        logging.error("Error listing directory '%s': %s", directory, e)
        return

    # Filter for image files with supported extensions (case-insensitive).
    image_files = [f for f in files if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

    if not image_files:
        print(f"Error: The directory '{directory}' is empty or contains no images to process.")
        return

    for filename in image_files:
        filepath = os.path.join(directory, filename)
        try:
            with Image.open(filepath) as img:
                width, height = img.size
        except Exception as e:
            logging.error("Error opening image '%s': %s", filepath, e)
            continue

        # Determine the target directory based on image dimensions.
        if is_close_to_square(width, height):
            target_dir = square_dir
        elif width > height:
            target_dir = horizontal_dir
        else:
            target_dir = vertical_dir

        new_path = os.path.join(target_dir, filename)
        try:
            os.rename(filepath, new_path)
            logging.info("Moved '%s' to '%s'", filename, target_dir)
        except Exception as e:
            logging.error("Error moving '%s' to '%s': %s", filename, target_dir, e)

def main():
    parser = argparse.ArgumentParser(
        description="Sort images into categories based on their dimensions."
    )
    parser.add_argument(
        '-d', '--directory',
        default='./src_img',
        help="Directory containing images to sort (default: ./src_img)"
    )
    args = parser.parse_args()

    logging.info("Starting image sorting in directory: %s", args.directory)
    sort_images(args.directory)
    logging.info("Image sorting complete.")

if __name__ == '__main__':
    main()

