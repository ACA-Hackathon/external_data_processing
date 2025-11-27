import zipfile

with zipfile.ZipFile("src/agreste_saa.zip", "r") as zip_ref:
    zip_ref.extractall("src")

