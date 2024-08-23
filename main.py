from utils.create_dir import create_download_dir
from utils.download_file import download_file
from extract import extract_file


if __name__ == "__main__":
    data_folder = create_download_dir()
    file_path, download_dir = download_file(data_folder)
    extract_file(file_path, download_dir)