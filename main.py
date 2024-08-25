from utils.create_dir import create_download_dir
from utils.download_file import download_file
from etl.extract import extract_file
from etl.transform import transform
from etl.load import load
from time import sleep

def main():
    
    data_folder = create_download_dir()

    file_path, download_dir = download_file(data_folder)
    
    extract_file(file_path, download_dir)

    sleep(2)
    
    data_df = transform()

    sleep(2)

    load(data_df)

    return None 

if __name__ == "__main__":
    main()