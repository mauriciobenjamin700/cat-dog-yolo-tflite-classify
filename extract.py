import zipfile

CLASSES_PATH = "temp"
ZIP_FILE = "kagglecatsanddogs_5340.zip"

def extract_zip(zip_file, extract_to):
    """
    Extract a zip file to a specified directory.
    
    Args:
        zip_file (str): Path to the zip file.
        extract_to (str): Directory where the contents will be extracted.
    """
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Extracted {zip_file} to {extract_to}")

extract_zip(ZIP_FILE, CLASSES_PATH)
