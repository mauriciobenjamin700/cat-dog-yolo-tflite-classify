import cv2
from glob import glob
import os

TEMP_PATH = "temp/PetImages"
TEMP_CAT_PATH = os.path.join(TEMP_PATH, "Cat")
TEMP_DOG_PATH = os.path.join(TEMP_PATH, "Dog")
OUTPUT_PATH = "data"
OUTPUT_PATH_CAT = os.path.join(OUTPUT_PATH, "Cat")
OUTPUT_PATH_DOG = os.path.join(OUTPUT_PATH, "Dog")

def get_files(directory, extensions=None):
    """
    Get all files in a directory with specified extensions.
    
    Args:
        directory (str): The directory to search for files.
        extensions (list, optional): List of file extensions to filter by. If None, all files are returned.
    
    Returns:
        list: List of file paths that match the specified extensions.
    """
    if extensions is None:
        return glob(os.path.join(directory, '*'))
    
    files = []
    for ext in extensions:
        files.extend(glob(os.path.join(directory, f'*.{ext}')))
    
    return files


def process_and_save_image(image_path, output_path, size=(224, 224)):
    """
    Read an image, resize it, and save it to a specified path.
    
    Args:
        image_path (str): Path to the input image.
        output_path (str): Path where the resized image will be saved.
        size (tuple): Desired size for the resized image.
    """
    image = cv2.imread(image_path)
    if image is None:
        print(f"Failed to read image: {image_path}")
        return
    
    resized_image = cv2.resize(image, size)
    cv2.imwrite(os.path.join(output_path, os.path.basename(image_path)), resized_image)
    print(f"Saved resized image to: {output_path}")


cat = get_files(TEMP_CAT_PATH)
dog = get_files(TEMP_DOG_PATH)

print(f"Number of cat images: {len(cat)}")
print(f"Number of dog images: {len(dog)}")

os.makedirs(OUTPUT_PATH_CAT, exist_ok=True)
os.makedirs(OUTPUT_PATH_DOG, exist_ok=True)

for cat_file in cat:

    process_and_save_image(cat_file, OUTPUT_PATH_CAT)

for dog_file in dog:
    process_and_save_image(dog_file, OUTPUT_PATH_DOG)

print("Processing complete. Images saved to:", OUTPUT_PATH)