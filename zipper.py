import argparse
import zipfile

def unzip(file_path, extraction_path):
    """Unzips a zip file to the specified directory."""
    with zipfile.ZipFile(file_path, "r") as zip_ref:
        zip_ref.extractall(extraction_path)

if __name__ == "__main__":
    args = argparse.ArgumentParser(description="Unzip specified zip file.")
    args.add_argument("-f", "--file_path", type=str, required=True, help="Path to the zip file to be extracted.")
    args.add_argument("-o", "--output_path", type=str, default="src/", help="Directory to extract the zip file into.")
    parsed_args = args.parse_args()
    unzip(parsed_args.file_path, parsed_args.output_path)
    


