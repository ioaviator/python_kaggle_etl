import shutil 
import zipfile

def extract_file(zip_file_path:str, download_dir:str) -> None:
    '''
        connect to directory where downloaded files are stored, extracts
        downloaded file and save to final destination

        args:
            zip_file_path(str): absolute directory path to downloaded file
            download_dir(str): download directory where files will be stored
        
        return:
            None
    '''

    dataset_dir = "data"

    try:
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(f'{dataset_dir}/orders')
            print(f"Downloaded and extracted to: {dataset_dir}")
    except:
        print("Failed to download the file.")
    finally:
        shutil.rmtree(f"{download_dir}")
        print('done')